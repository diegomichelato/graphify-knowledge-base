// RoslynEdges — statically verified structural relationships for the knowledge graph.
//
// Usage: dotnet run --project tools/RoslynEdges -- <repo-root> <output.json>
//
// Emits ONLY relationships provable from a full-solution Roslyn compilation:
//   implements  (type -> interface, method -> interface method)
//   inherits    (type -> base type)
//   overrides   (method -> overridden method)
//   calls       (method -> in-solution method it invokes)
//   references  (type -> in-solution type it uses, cross-file only)
//   tested_by   (production type -> test type that references it)
//   imports     (file -> in-solution namespace from a using directive)
//   exports     (namespace -> its public types)
// No AI. No heuristics beyond symbol resolution. Unresolvable symbols are skipped.

using System.Text.Json;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

if (args.Length < 2)
{
    Console.Error.WriteLine("usage: RoslynEdges <repo-root> <output.json>");
    return 1;
}

var root = Path.GetFullPath(args[0]);
var outPath = args[1];
string[] skipDirs = ["/bin/", "/obj/", "/.git/", "/graphify-out/", "/node_modules/"];

var files = Directory.EnumerateFiles(root, "*.cs", SearchOption.AllDirectories)
    .Where(f => !skipDirs.Any(s => f.Replace('\\', '/').Contains(s)))
    .ToList();

var parseOpts = new CSharpParseOptions(LanguageVersion.Preview);
var trees = files.Select(f => CSharpSyntaxTree.ParseText(
    File.ReadAllText(f), parseOpts, path: f)).ToList();

// The app builds with <ImplicitUsings>enable</ImplicitUsings>; replicate it so
// framework symbols resolve instead of binding to error types.
trees.Add(CSharpSyntaxTree.ParseText("""
    global using System;
    global using System.Collections.Generic;
    global using System.IO;
    global using System.Linq;
    global using System.Net.Http;
    global using System.Threading;
    global using System.Threading.Tasks;
    """, parseOpts, path: "__GlobalUsings.cs"));

// Reference the running runtime's assemblies so framework symbols resolve.
var refs = new Dictionary<string, MetadataReference>(StringComparer.OrdinalIgnoreCase);
foreach (var p in ((string)AppContext.GetData("TRUSTED_PLATFORM_ASSEMBLIES")!).Split(Path.PathSeparator))
    refs[Path.GetFileName(p)] = MetadataReference.CreateFromFile(p);

// Plus restored NuGet package assemblies (best-effort; one version per assembly name).
var nuget = Environment.ExpandEnvironmentVariables(
    Environment.GetEnvironmentVariable("NUGET_PACKAGES")
    ?? Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), ".nuget", "packages"));
if (Directory.Exists(nuget))
{
    var candidates = Directory.EnumerateFiles(nuget, "*.dll", SearchOption.AllDirectories)
        .Where(p => p.Replace('\\', '/').Contains("/lib/"))
        .Where(p => p.Contains("net10.0") || p.Contains("net9.0") || p.Contains("net8.0")
                    || p.Contains("netstandard2."))
        .OrderByDescending(p => p.Contains("net10.0")).ThenByDescending(p => p.Contains("net9.0"))
        .ThenByDescending(p => p.Contains("net8.0"));
    foreach (var p in candidates)
        refs.TryAdd(Path.GetFileName(p), MetadataReference.CreateFromFile(p));
}
var tpa = refs.Values;

var compilation = CSharpCompilation.Create("KnowledgeGraphAnalysis", trees, tpa,
    new CSharpCompilationOptions(OutputKind.DynamicallyLinkedLibrary));

string Rel(string path) => Path.GetRelativePath(root, path).Replace('\\', '/');

string? FileOf(ISymbol sym) =>
    sym.Locations.FirstOrDefault(l => l.IsInSource)?.SourceTree?.FilePath is string p ? Rel(p) : null;

bool InSolution(ISymbol? sym) =>
    sym is not null
    && sym is not IErrorTypeSymbol                      // unresolved: skip, never fabricate
    && (sym as INamedTypeSymbol)?.TypeKind != TypeKind.Error
    && sym.Locations.Any(l => l.IsInSource)             // must be declared in our files
    && SymbolEqualityComparer.Default.Equals(sym.ContainingAssembly, compilation.Assembly);

var edges = new List<Dictionary<string, string?>>();
var seen = new HashSet<string>();

void Emit(string rel, string srcKind, string srcName, string? srcFile,
          string tgtKind, string tgtName, string? tgtFile)
{
    var key = $"{rel}|{srcName}|{srcFile}|{tgtName}|{tgtFile}";
    if (!seen.Add(key)) return;
    edges.Add(new()
    {
        ["relationship"] = rel,
        ["source_kind"] = srcKind, ["source_name"] = srcName, ["source_file"] = srcFile,
        ["target_kind"] = tgtKind, ["target_name"] = tgtName, ["target_file"] = tgtFile,
    });
}

string MethodLabel(IMethodSymbol m) => m.Name + "()";
bool IsTestType(INamedTypeSymbol t) =>
    (FileOf(t) ?? "").Contains("/tests/", StringComparison.OrdinalIgnoreCase)
    || (FileOf(t) ?? "").Contains("Tests/", StringComparison.Ordinal);

var typeRefs = new Dictionary<INamedTypeSymbol, HashSet<INamedTypeSymbol>>(SymbolEqualityComparer.Default);

foreach (var tree in trees)
{
    var model = compilation.GetSemanticModel(tree);
    var relFile = Rel(tree.FilePath);
    var rootNode = tree.GetRoot();

    // ---- imports: using directives that resolve to an in-solution namespace
    foreach (var u in rootNode.DescendantNodes().OfType<UsingDirectiveSyntax>())
    {
        if (u.Name is null) continue;
        var sym = model.GetSymbolInfo(u.Name).Symbol as INamespaceSymbol;
        if (sym is null) continue;
        // in-solution check for namespaces: any member type in our assembly
        bool ours = sym.GetTypeMembers().Any(InSolution) ||
                    sym.GetNamespaceMembers().Any(ns => ns.GetTypeMembers().Any(InSolution));
        if (ours)
            Emit("imports", "File", Path.GetFileName(relFile), relFile,
                 "Namespace", sym.ToDisplayString(), null);
    }

    foreach (var decl in rootNode.DescendantNodes().OfType<BaseTypeDeclarationSyntax>())
    {
        if (model.GetDeclaredSymbol(decl) is not INamedTypeSymbol type) continue;
        var typeFile = FileOf(type) ?? relFile;

        // ---- inherits / implements (type level)
        if (type.BaseType is { SpecialType: SpecialType.None } baseType && InSolution(baseType))
            Emit("inherits", "Type", type.Name, typeFile, "Type", baseType.Name, FileOf(baseType));
        foreach (var iface in type.Interfaces.Where(InSolution))
        {
            Emit("implements", "Type", type.Name, typeFile, "Type", iface.Name, FileOf(iface));
            // ---- implements (method level)
            foreach (var im in iface.GetMembers().OfType<IMethodSymbol>()
                         .Where(m => m.MethodKind == MethodKind.Ordinary))
            {
                if (type.FindImplementationForInterfaceMember(im) is IMethodSymbol impl
                    && InSolution(impl)
                    && SymbolEqualityComparer.Default.Equals(impl.ContainingType, type))
                    Emit("implements", "Method", MethodLabel(impl), FileOf(impl),
                         "Method", MethodLabel(im), FileOf(im));
            }
        }

        // ---- exports: public types belong to their namespace's public surface
        if (type.DeclaredAccessibility == Accessibility.Public && !type.ContainingNamespace.IsGlobalNamespace)
            Emit("exports", "Namespace", type.ContainingNamespace.ToDisplayString(), null,
                 "Type", type.Name, typeFile);
    }

    foreach (var m in rootNode.DescendantNodes().OfType<MethodDeclarationSyntax>())
    {
        if (model.GetDeclaredSymbol(m) is not IMethodSymbol method) continue;
        var mFile = FileOf(method) ?? relFile;

        // ---- overrides
        if (method.IsOverride && method.OverriddenMethod is { } om && InSolution(om))
            Emit("overrides", "Method", MethodLabel(method), mFile,
                 "Method", MethodLabel(om), FileOf(om));

        // ---- calls: invocations resolving to in-solution methods
        foreach (var inv in m.DescendantNodes().OfType<InvocationExpressionSyntax>())
        {
            if (model.GetSymbolInfo(inv).Symbol is not IMethodSymbol callee) continue;
            var target = callee.ReducedFrom ?? callee.OriginalDefinition;
            if (!InSolution(target) || target.MethodKind != MethodKind.Ordinary) continue;
            Emit("calls", "Method", MethodLabel(method), mFile,
                 "Method", MethodLabel(target), FileOf(target));
        }
    }

    // ---- references: cross-file type usage (identifiers + object creation)
    foreach (var id in rootNode.DescendantNodes().OfType<IdentifierNameSyntax>())
    {
        if (model.GetSymbolInfo(id).Symbol is not INamedTypeSymbol used || !InSolution(used)) continue;
        var enclosing = model.GetEnclosingSymbol(id.SpanStart);
        var owner = enclosing?.ContainingType ?? enclosing as INamedTypeSymbol;
        if (owner is null || SymbolEqualityComparer.Default.Equals(owner, used)) continue;
        var usedFile = FileOf(used);
        if (usedFile is null || usedFile == Rel(tree.FilePath)) continue; // cross-file only
        if (!typeRefs.TryGetValue(owner, out var set))
            typeRefs[owner] = set = new(SymbolEqualityComparer.Default);
        set.Add(used);
    }
}

// references + tested_by from the collected cross-file usage map
foreach (var (owner, useds) in typeRefs)
{
    var ownerFile = FileOf(owner);
    foreach (var used in useds)
    {
        Emit("references", "Type", owner.Name, ownerFile, "Type", used.Name, FileOf(used));
        if (IsTestType(owner) && !IsTestType(used))
            Emit("tested_by", "Type", used.Name, FileOf(used), "Type", owner.Name, ownerFile);
    }
}

var diag = compilation.GetDiagnostics().Count(d => d.Severity == DiagnosticSeverity.Error);
Console.Error.WriteLine($"files: {files.Count}, compilation errors: {diag} (unresolved symbols are skipped, not fabricated)");
Console.Error.WriteLine($"edges emitted: {edges.Count}");
foreach (var grp in edges.GroupBy(e => e["relationship"]).OrderByDescending(g => g.Count()))
    Console.Error.WriteLine($"  {grp.Key}: {grp.Count()}");

File.WriteAllText(outPath, JsonSerializer.Serialize(edges, new JsonSerializerOptions { WriteIndented = false }));
return 0;
