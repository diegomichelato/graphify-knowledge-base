# Graph Report - graphify-dotnet  (2026-07-09)

## Summary
- 1620 nodes · 2852 edges · 167 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS

## God Nodes (most connected - your core abstractions)
1. `Graphify.Security` - 2 edges
2. `MiniLibrary` - 2 edges
3. `Graphify.Export` - 2 edges
4. `Graphify.Tests.Export` - 2 edges
5. `Graphify.Cli` - 2 edges
6. `Third` - 2 edges
7. `Test` - 2 edges
8. `Graphify.Cli.Configuration` - 2 edges
9. `Graphify.Cache` - 2 edges
10. `ICacheProvider` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Entity (Community 0)"
Cohesion: 0.12
Nodes (34): ModelTests.cs, ModelTests.cs, GraphEdge_Construction_SetsRequiredProperties(), GodNode_Construction(), FileType_HasExpectedValues(), Graphify.Tests.ModelTests, GraphEdge_Equality_BySourceTargetRelationship(), GraphReport_Construction() (+26 more)

### Community 1 - "Entity (Community 1)"
Cohesion: 0.12
Nodes (32): InputValidatorTests.cs, InputValidatorTests.cs, ValidateInput_ManyInjectionPatterns_ReturnsFailure(), ValidateInput_ExceedsMaxLength_ReturnsFailure(), ValidateInput_EmptyOrWhitespace_ReturnsFailure(), SanitizeLabel_CleanLabel_ReturnsUnchanged(), InputValidatorTests, ValidateInput_NullInput_ReturnsFailure() (+24 more)

### Community 3 - "Entity (Community 3)"
Cohesion: 0.14
Nodes (29): LadybugExporterTests.cs, LadybugExporterTests.cs, ExportAsync_WhitespaceOnlyOutputPath_ThrowsArgumentException(), Graphify.Tests.Export, Format_ReturnsLadybug(), ExportAsync_RelationshipTableUsesManyMany(), ExportAsync_NodeWithoutCommunity_OmitsCommunityProperty(), ExportAsync_NullGraph_ThrowsArgumentNullException() (+21 more)

### Community 2 - "Entity (Community 2)"
Cohesion: 0.14
Nodes (29): ConfigSetCommandTests.cs, ConfigSetCommandTests.cs, Command(), AzureOpenAIProviderRouting_SetsAllRequiredKeys(), CleanupUserSecrets(), CopilotSdkDefaults_EmptyInput_UsesGpt41(), ConfigSetCommand_ExistsUnderConfigCommand(), ConfigSetCommandTests (+21 more)

### Community 4 - "Entity (Community 4)"
Cohesion: 0.14
Nodes (28): KnowledgeGraphTests.cs, KnowledgeGraphTests.cs, UnderlyingGraph_ProvidesAccessToQuikGraph(), AddEdge_MissingSourceNode_ReturnsFalse(), Graphify.Tests.Graph, GetNodes_ReturnsAllNodes(), GetNodesByCommunity_ReturnsNodesInCommunity(), MergeGraph_OverwritesDuplicateNodes() (+20 more)

### Community 6 - "Entity (Community 6)"
Cohesion: 0.16
Nodes (25): FileDetectorTests.cs, FileDetectorTests.cs, Graphify.Tests.Pipeline, if(), ExecuteAsync_SetsCorrectSizeBytes(), ExecuteAsync_ResultsAreSortedByRelativePath(), ExecuteAsync_SetsCorrectFilePath(), ExecuteAsync_SetsCorrectRelativePath() (+17 more)

### Community 5 - "Entity (Community 5)"
Cohesion: 0.16
Nodes (25): HtmlExporterTests.cs, HtmlExporterTests.cs, ExportAsync_Html_ContainsEdgeData(), ExportAsync_EmptyGraph_ProducesValidHtml(), ExportAsync_CreatesDirectory_IfNotExists(), ExportAsync_Format_ReturnsHtml(), ExportAsync_NodeSizes_ProportionalToDegree(), ExportAsync_LargeGraph_ThrowsException() (+17 more)

### Community 7 - "Entity (Community 7)"
Cohesion: 0.16
Nodes (24): ConfigurationFactoryTests.cs, ConfigurationFactoryTests.cs, Build_AzureOpenAICliOptions_SetsAzureFields(), Build_CopilotSdkCliOptions_ApiKeyDoesNotSetCopilotSdkKey(), Build_CopilotSdkCanBindToGraphifyConfig(), Build_CliOverridesAreHighestPriority(), Build_CliArgs_OverrideLocalConfig(), Graphify.Tests.Cli (+16 more)

### Community 8 - "Entity (Community 8)"
Cohesion: 0.18
Nodes (22): ConfigPersistenceTests.cs, ConfigPersistenceTests.cs, Save_CreatesValidJson_WithGraphifyWrapper(), Load_ReturnsNull_WhenGraphifySectionMissing(), Load_ReturnsNull_WhenFileDoesNotExist(), Save_AzureOpenAI_DoesNotIncludeOllamaOrCopilotSdkFields(), Save_CopilotSdk_DoesNotIncludeAzureOrOllamaFields(), ConfigPersistenceTests() (+14 more)

### Community 9 - "Entity (Community 9)"
Cohesion: 0.18
Nodes (22): CopilotSdkConfigTests.cs, CopilotSdkConfigTests.cs, CopilotSdkConfig_ModelId_AcceptsVariousValues(), CopilotSdkConfig_DefaultModelId_IsGpt41(), GraphifyConfig_HasAllThreeProviderConfigs(), CopilotSdkConfigTests, Graphify.Tests.Cli, GraphifyConfig_CopilotSdk_DefaultModelId_IsGpt41() (+14 more)

### Community 10 - "Entity (Community 10)"
Cohesion: 0.10
Nodes (21): RelativePathHandlingTests.cs, PathNormalization_MixedPathSeparators_Handled(), JsonExport_MultipleOutputLocations_PreservesRelativePaths(), MultipleExports_ProduceSamePaths(), JsonExport_NodeFilePaths_CorrectlyNormalized(), OutputDirWithinProjectRoot_RelativePathsCorrect(), JsonExport_NodeFilePaths_AreRelative(), CreateGraphWithTestFiles() (+13 more)

### Community 15 - "Entity (Community 15)"
Cohesion: 0.19
Nodes (20): JsonExporterTests.cs, JsonExporterTests.cs, CreateSampleGraph(), CreateNode(), if(), Graphify.Tests.Export, foreach(), ExportAsync_NodeMetadata_Preserved() (+12 more)

### Community 14 - "Entity (Community 14)"
Cohesion: 0.19
Nodes (20): UrlIngesterTests.cs, UrlIngesterTests.cs, UrlIngesterTests(), IngestToFileAsync_WithAuthor_IncludesContributor(), SendAsync(), Graphify.Tests.Ingest, IngestAsync_FtpScheme_ThrowsArgumentException(), if() (+12 more)

### Community 12 - "Entity (Community 12)"
Cohesion: 0.19
Nodes (20): EdgeCaseTests.cs, EdgeCaseTests.cs, SemanticCache_ConcurrentWrites_ThreadSafe(), new(), TestData(), SemanticCache_ConcurrentReads_ThreadSafe(), Random(), if() (+12 more)

### Community 11 - "Entity (Community 11)"
Cohesion: 0.19
Nodes (20): ExportSecurityTests.cs, ExportSecurityTests.cs, if(), Neo4jExporter_CypherInjectionPayload_IsNeutralized(), Neo4jExporter_SingleQuoteInLabel_IsEscaped(), while(), Neo4jExporter_EscapeCypher_EscapesAllDangerousChars(), ContainsInScriptBlock() (+12 more)

### Community 16 - "Entity (Community 16)"
Cohesion: 0.10
Nodes (20): Extractor.cs, ExecuteAsync(), CreateEdge(), ArrowFunctionPattern(), CreateNode(), FromImportPattern(), abstract(), Extractor() (+12 more)

### Community 13 - "Entity (Community 13)"
Cohesion: 0.19
Nodes (20): SemanticExtractorTests.cs, SemanticExtractorTests.cs, ExecuteAsync_WithMockClient_ReturnsParsedNodesAndEdges(), ExecuteAsync_JsonInMarkdownCodeBlock_ParsedCorrectly(), ExecuteAsync_HandlesAiResponseParsingFailure(), ExecuteAsync_SourceFilePathPreserved(), ExecuteAsync_FileSizeExceedsLimit_ReturnsEmpty(), ExecuteAsync_RespectsCancellationToken() (+12 more)

### Community 21 - "Entity (Community 21)"
Cohesion: 0.11
Nodes (19): ExtractionValidatorTests.cs, Validate_EdgeWithEmptySourceFile_ReturnsFailure(), Graphify.Tests.Validation, ExtractionValidatorTests, Validate_EdgeWithEmptyRelation_ReturnsFailure(), Validate_EdgeWithEmptySource_ReturnsFailure(), Validate_ValidExtractionResult_ReturnsSuccess(), Validate_NullExtractionResult_ReturnsFailure() (+11 more)

### Community 20 - "Entity (Community 20)"
Cohesion: 0.20
Nodes (19): AnalyzerTests.cs, AnalyzerTests.cs, Graphify.Tests.Pipeline, if(), KnowledgeGraph(), for(), ExecuteAsync_SuggestedQuestions_Generated(), ExecuteAsync_GodNodeDetection_FindsHighestDegree() (+11 more)

### Community 19 - "Entity (Community 19)"
Cohesion: 0.20
Nodes (19): Neo4jExporterTests.cs, Neo4jExporterTests.cs, ExportAsync_EmptyGraph_ProducesValidButEmptyOutput(), CreateSampleGraph(), Dispose(), ExportAsync_CreatesIndexStatements(), ExportAsync_EdgesExportedWithCorrectRelationshipTypes(), ExportAsync_SpecialCharactersInLabels_AreEscaped() (+11 more)

### Community 18 - "Entity (Community 18)"
Cohesion: 0.20
Nodes (19): CopilotChatClientTests.cs, CopilotChatClientTests.cs, CreateUnstartedCopilotClient(), GetService_UnknownType_ReturnsNull(), CopilotClient(), GetService_IChatClientType_ReturnsNull(), GetService_CopilotClientType_ReturnsUnderlyingClient(), DisposeAsync_OwnsClientFalse_DoesNotDisposeCopilotClient() (+11 more)

### Community 22 - "Entity (Community 22)"
Cohesion: 0.20
Nodes (19): InputValidationSecurityTests.cs, InputValidationSecurityTests.cs, Dispose(), catch(), OutputDirectory_PathTraversal_IsRejected(), FileDetector_SymlinkDirectory_IsSkipped(), OutputDirectory_AbsolutePath_IsAllowed(), InputValidationSecurityTests() (+11 more)

### Community 17 - "Entity (Community 17)"
Cohesion: 0.20
Nodes (19): SvgExporterTests.cs, SvgExporterTests.cs, ExportAsync_EdgesRenderedAsLines(), ExportAsync_NodesRenderedAsCircles(), ExportAsync_HasStyleDefinitions(), ExportAsync_NodeTitlesIncludeLabel(), ExportAsync_EmptyGraph_ProducesValidEmptySvg(), ExportAsync_IncludesLegendWithStats() (+11 more)

### Community 24 - "Entity (Community 24)"
Cohesion: 0.22
Nodes (18): ChatClientFactoryTests.cs, ChatClientFactoryTests.cs, Graphify.Tests.Sdk, AiProvider_HasExpectedValues(), AiProviderOptions_CopilotSdk_ConstructionWorks(), AiProvider_HasExactlyThreeValues(), AiProviderOptions_AzureOpenAI_ConstructionWorks(), Create_AzureOpenAI_MissingDeploymentName_Throws() (+10 more)

### Community 23 - "Entity (Community 23)"
Cohesion: 0.22
Nodes (18): SemanticCache.cs, SemanticCache.cs, InvalidateAsync(), EnsureCacheDirectoryExists(), foreach(), ExistsAsync(), FileNotFoundException(), ComputeHashAsync() (+10 more)

### Community 25 - "Entity (Community 25)"
Cohesion: 0.12
Nodes (17): UrlIngester.cs, ExtractArxivAuthors(), EscapeYaml(), ExtractArxivAbstract(), ArgumentException(), DetectUrlType(), AddContributorMetadata(), IngestAsync() (+9 more)

### Community 28 - "Entity (Community 28)"
Cohesion: 0.23
Nodes (17): BenchmarkRunnerTests.cs, BenchmarkRunnerTests.cs, PrintBenchmark_NullWriter_ThrowsArgumentNullException(), Graphify.Tests.Pipeline, PrintBenchmark_NullResult_ThrowsArgumentNullException(), BenchmarkRunnerTests(), CreateSampleGraphFile(), Dispose() (+9 more)

### Community 27 - "Entity (Community 27)"
Cohesion: 0.12
Nodes (17): SecurityHardeningTests.cs, SemanticCache_DirectoryCreated_HasRestrictedPermissions(), LlmResponseValidator_ScriptTagInNodeLabel_IsSanitized(), LlmResponseValidator_MalformedSchema_ReturnsNull(), LlmResponseValidator_InvalidJson_ReturnsNull(), ConfigPersistence_ValidJson_LoadsSuccessfully(), LlmResponseValidator_ValidJson_ReturnsResult(), ErrorMessage_NonVerbose_DoesNotLeakDetails() (+9 more)

### Community 29 - "Entity (Community 29)"
Cohesion: 0.23
Nodes (17): FormatRoutingTests.cs, FormatRoutingTests.cs, Dispose(), CreateTestProject(), RunAsync_WithSvgFormat_CreatesSvgFile(), RunAsync_WithCommaFormats_ParsesCorrectly(), RunAsync_WithHtmlFormat_CreatesHtmlFile(), RunAsync_WithEmptyFormats_CompletesSuccessfully() (+9 more)

### Community 26 - "Entity (Community 26)"
Cohesion: 0.23
Nodes (17): ObsidianExporterTests.cs, ObsidianExporterTests.cs, ExportAsync_LinksBetweenNodesUseWikiLinkSyntax(), ExportAsync_CommunityAssignment_IncludedInFrontmatter(), Dispose(), ExportAsync_EmptyGraph_ProducesEmptyVault(), ExportAsync_CreatesMarkdownFilePerNode(), ExportAsync_CreatesOutputDirectory() (+9 more)

### Community 30 - "Entity (Community 30)"
Cohesion: 0.12
Nodes (16): Analyzer.cs, IsConceptNode(), var(), private(), return(), IsFileNode(), Graphify.Pipeline, GetFileCategory() (+8 more)

### Community 31 - "Entity (Community 31)"
Cohesion: 0.12
Nodes (16): ExtractorTests.cs, App(), Add(), calculate_sum(), Second, MyMethod(), MyClass, main() (+8 more)

### Community 32 - "Entity (Community 32)"
Cohesion: 0.24
Nodes (16): ClusterEngineTests.cs, ClusterEngineTests.cs, ExecuteAsync_IsolatedNodes_GetOwnCommunities(), CalculateCohesion_NoEdges_ReturnsZero(), ExecuteAsync_BridgeNode_ConnectsTwoCommunities(), CalculateCohesion_SingleNode_ReturnsOne(), CalculateModularity_FullyConnectedGraph_ReturnsValue(), ExecuteAsync_EmptyGraph_ReturnsUnchanged() (+8 more)

### Community 36 - "Entity (Community 36)"
Cohesion: 0.26
Nodes (15): ConfigWizard.cs, ConfigWizard.cs, PromptAzureOpenAI(), ParseSelectedFormats(), MaskSecret(), foreach(), Graphify.Cli.Configuration, if() (+7 more)

### Community 35 - "Entity (Community 35)"
Cohesion: 0.13
Nodes (15): ExtractorTests.cs, Third, Test, Reset(), process(), Fifth(), DataProcessor, Dispose() (+7 more)

### Community 33 - "Entity (Community 33)"
Cohesion: 0.26
Nodes (15): ExtractionPromptsTests.cs, ExtractionPromptsTests.cs, CodeSemanticExtraction_IncludesExpectedKeywords(), AllPrompts_RequestJsonOutput(), AllPrompts_AreNonEmpty(), DocumentationExtraction_IncludesFileContent(), ImageVisionExtraction_IncludesMaxNodes(), ImageVisionExtraction_IncludesFileName() (+7 more)

### Community 34 - "Entity (Community 34)"
Cohesion: 0.26
Nodes (15): ExportIntegrationTests.cs, ExportIntegrationTests.cs, ReportGeneration_ProducesMarkdownReport(), LadybugExport_ProducesValidCypher(), foreach(), Graphify.Integration.Tests, JsonExport_ThenReimport_PreservesGraph(), ExportIntegrationTests() (+7 more)

### Community 37 - "Entity (Community 37)"
Cohesion: 0.27
Nodes (14): SemanticCacheRegressionTests.cs, SemanticCacheRegressionTests.cs, if(), Graphify.Tests.Regression, SemanticCacheRegressionTests(), Dispose(), for(), SaveAsync_CalledExternally_NoDeadlock_RegressionBug1() (+6 more)

### Community 38 - "Entity (Community 38)"
Cohesion: 0.27
Nodes (14): CopilotSdkOptionsTests.cs, CopilotSdkOptionsTests.cs, CustomModelId_IsPreserved(), CustomModelId_VariousModels_ArePreserved(), CopilotSdkOptionsTests, Graphify.Tests.Sdk, ToString_ContainsModelId(), RecordEquality_DefaultInstances_AreEqual() (+6 more)

### Community 44 - "Entity (Community 44)"
Cohesion: 0.15
Nodes (13): PipelineRunner.cs, CalculateCohesion(), BuildCommunityLabels(), async(), ArgumentException(), PipelineRunner(), for(), switch() (+5 more)

### Community 43 - "Entity (Community 43)"
Cohesion: 0.15
Nodes (13): WatchMode.cs, WatchMode(), ShouldReportProgress(), WatchAsync(), switch(), OnFileEvent(), JsonExporter(), SetInitialGraph() (+5 more)

### Community 45 - "Entity (Community 45)"
Cohesion: 0.15
Nodes (13): SemanticCacheTests.cs, Dispose(), ComputeHashAsync_NonExistentFile_ThrowsFileNotFoundException(), ClearAsync_RemovesAllEntries(), ComputeHashAsync_SameContent_ReturnsSameHash(), SemanticCacheTests(), Graphify.Tests.Cache, SetAsync_AndGetAsync_RoundTrip() (+5 more)

### Community 41 - "Entity (Community 41)"
Cohesion: 0.29
Nodes (13): ChatClientResolverTests.cs, ChatClientResolverTests.cs, Resolve_AzureOpenAI_MissingApiKey_Throws(), ChatClientResolverTests, Graphify.Tests.Cli, Resolve_UnknownProvider_ThrowsInvalidOperationException(), Resolve_AzureOpenAI_MissingEndpoint_Throws(), Resolve_OllamaProvider_ReturnsNonNullClient() (+5 more)

### Community 40 - "Entity (Community 40)"
Cohesion: 0.15
Nodes (13): SampleProjectTests.cs, ProcessSampleProject_AllFormatsSucceed(), ProcessSampleProject_DetectsAllFiles(), IRepository, IService, Model, ProcessSampleProject_ProducesNonEmptyGraph(), Repository (+5 more)

### Community 42 - "Entity (Community 42)"
Cohesion: 0.29
Nodes (13): ReportGenerator.cs, ReportGenerator.cs, AppendCommunities(), for(), AppendSummary(), AppendSurprisingConnections(), AppendKnowledgeGaps(), AppendSuggestedQuestions() (+5 more)

### Community 39 - "Entity (Community 39)"
Cohesion: 0.15
Nodes (13): GraphTools.cs, catch(), Analyze(), foreach(), GenerateInsights(), Query(), Path(), var() (+5 more)

### Community 49 - "Entity (Community 49)"
Cohesion: 0.32
Nodes (12): CliIntegrationTests.cs, CliIntegrationTests.cs, Cli_HelpFlag_PrintsUsage(), for(), InvokeCliAsync(), Graphify.Integration.Tests, if(), Dispose() (+4 more)

### Community 48 - "Entity (Community 48)"
Cohesion: 0.32
Nodes (12): GraphifyConfigTests.cs, GraphifyConfigTests.cs, GraphifyConfig_Provider_IsNullByDefault(), OllamaConfig_DefaultEndpoint_IsLocalhost(), OllamaConfig_Properties_CanBeOverridden(), GraphifyConfig_HasDefaultOllamaAndAzureSubConfigs(), GraphifyConfig_Provider_CanBeSet(), AzureOpenAIConfig_Properties_CanBeSet() (+4 more)

### Community 47 - "Entity (Community 47)"
Cohesion: 0.32
Nodes (12): GraphBuilderTests.cs, GraphBuilderTests.cs, ExecuteAsync_SkipMissingNodes_DoesNotCreateDanglingEdges(), ExecuteAsync_SingleExtraction_CreatesGraph(), ExecuteAsync_MultipleExtractions_MergesGraph(), ExecuteAsync_MinEdgeWeight_FiltersLowWeightEdges(), ExecuteAsync_CreateFileNodes_AddsFileNodes(), ExecuteAsync_EdgeWeightAccumulation_WorksCorrectly() (+4 more)

### Community 46 - "Entity (Community 46)"
Cohesion: 0.32
Nodes (12): InputValidatorRegressionTests.cs, InputValidatorRegressionTests.cs, SanitizeLabel_TabAndNewline_Handling_RegressionBug2(), SanitizeLabel_OnlyControlChars_ReturnsClean_RegressionBug2(), SanitizeLabel_UnicodeControlChars_Handled_RegressionBug2(), SanitizeLabel_VeryLongInput_HandledGracefully_RegressionBug2(), SanitizeLabel_NullByte_Removed_RegressionBug2(), SanitizeLabel_ExtendedAscii_Preserved_RegressionBug2() (+4 more)

### Community 58 - "Entity (Community 58)"
Cohesion: 0.18
Nodes (11): InputValidator.cs, ValidateInput(), foreach(), InjectionPattern(), Graphify.Security, IsPrivateIp(), SanitizeLabel(), HtmlTagPattern() (+3 more)

### Community 59 - "Entity (Community 59)"
Cohesion: 0.18
Nodes (11): SemanticCacheTests.cs, CacheResultAsync_AndRetrieve_ReturnsOriginalData(), CacheRecovery_LoadsExistingIndex(), ComputeHashAsync_DifferentContent_ReturnsDifferentHash(), if(), foreach(), GetCachedResultAsync_MissingResultFile_ReturnsNull(), InvalidateAsync_RemovesEntry() (+3 more)

### Community 57 - "Entity (Community 57)"
Cohesion: 0.35
Nodes (11): WatchModeIntegrationTests.cs, WatchModeIntegrationTests.cs, WatchModeIntegrationTests(), WatchMode_IgnoresNonCodeFiles(), Graphify.Integration.Tests, WatchMode_DetectsNewFile(), WatchMode_DebounceCoalescesRapidChanges(), foreach() (+3 more)

### Community 51 - "Entity (Community 51)"
Cohesion: 0.18
Nodes (11): SampleProjectTests.cs, Service(), Add(), Controller(), GetAll(), Process(), MiniLibrary, GetById() (+3 more)

### Community 50 - "Entity (Community 50)"
Cohesion: 0.35
Nodes (11): PipelineIntegrationTests.cs, PipelineIntegrationTests.cs, Graphify.Integration.Tests, Pipeline_WithNestedDirectories_FindsAllFiles(), Pipeline_RespectsCancellation(), PipelineIntegrationTests(), Pipeline_WithEmptyDirectory_ProducesEmptyGraph(), foreach() (+3 more)

### Community 56 - "Entity (Community 56)"
Cohesion: 0.18
Nodes (11): Extractor.cs, if(), ImportPattern(), MethodPattern(), override(), return(), var(), foreach() (+3 more)

### Community 55 - "Entity (Community 55)"
Cohesion: 0.35
Nodes (11): CopilotSdkClientFactoryTests.cs, CopilotSdkClientFactoryTests.cs, Options_DefaultConstruction_HasExpectedModelId(), ChatClientFactory_CreateAsync_NullOptions_ThrowsArgumentNullException(), CopilotSdkClientFactoryTests, ChatClientFactory_CopilotSdk_SyncCreate_ThrowsInvalidOperationException(), AiProviderOptions_CopilotSdk_WithModelId_IsPreserved(), AiProviderOptions_CopilotSdk_DefaultModelIdIsNull() (+3 more)

### Community 54 - "Entity (Community 54)"
Cohesion: 0.35
Nodes (11): SecurityIntegrationTests.cs, SecurityIntegrationTests.cs, Pipeline_PathTraversalAttempt_IsBlocked(), SecurityIntegrationTests(), Pipeline_MaliciousSourceFile_DoesNotProduceXssInHtmlExport(), foreach(), for(), Export_AllFormats_SanitizeNodeLabels() (+3 more)

### Community 53 - "Entity (Community 53)"
Cohesion: 0.18
Nodes (11): ReportGeneratorTests.cs, static(), Generate_IncludesNodeAndEdgeCount(), Generate_IncludesTopConnectedNodes(), Generate_IncludesSuggestedQuestions(), Generate_NullAnalysis_ThrowsArgumentNullException(), Graphify.Tests.Pipeline, Generate_IncludesCommunityCount() (+3 more)

### Community 52 - "Entity (Community 52)"
Cohesion: 0.35
Nodes (11): OllamaClientFactoryTests.cs, OllamaClientFactoryTests.cs, OllamaOptions_DefaultValues_AreCorrect(), OllamaClientFactoryTests, OllamaOptions_CustomEndpoint_IsPreserved(), OllamaOptions_FullyCustom_AllValuesPreserved(), OllamaOptions_CustomModelId_IsPreserved(), OllamaOptions_With_CreatesModifiedCopy() (+3 more)

### Community 64 - "Entity (Community 64)"
Cohesion: 0.20
Nodes (10): FileDetector.cs, ExecuteAsync(), DirectoryNotFoundException(), EnumerateFilesAsync(), DetectedFile(), ArgumentException(), FileDetector, while() (+2 more)

### Community 62 - "Entity (Community 62)"
Cohesion: 0.20
Nodes (10): WikiExporterTests.cs, WikiExporterTests(), ExportAsync_EmptyPath_ThrowsArgumentException(), ExportAsync_GodNodeArticlesCreated(), Dispose(), ExportAsync_CommunityArticleContainsKeyConcepts(), ExportAsync_CreatesIndexFile(), ExportAsync_IndexShowsGodNodes() (+2 more)

### Community 63 - "Entity (Community 63)"
Cohesion: 0.20
Nodes (10): Neo4jExporter.cs, SanitizePropertyName(), while(), SanitizeRelationshipType(), ExportAsync(), EscapeCypher(), GenerateVariableName(), SanitizeNodeType() (+2 more)

### Community 60 - "Entity (Community 60)"
Cohesion: 0.38
Nodes (10): PipelineRunnerTests.cs, PipelineRunnerTests.cs, RunAsync_ReportsFileProgressDuringExtraction(), PipelineRunnerTests, Constructor_WithChatClient_IsAccepted(), Constructor_NullChatClient_IsAccepted(), Graphify.Tests.Cli, Constructor_DefaultParameters_ChatClientIsOptional() (+2 more)

### Community 61 - "Entity (Community 61)"
Cohesion: 0.20
Nodes (10): BenchmarkRunner.cs, PrintBenchmark(), EstimateQueryTokens(), Graphify.Pipeline, for(), EstimateCorpusWords(), LoadGraphFromJson(), RunAsync() (+2 more)

### Community 66 - "Entity (Community 66)"
Cohesion: 0.38
Nodes (10): ChatClientFactory.cs, ChatClientFactory.cs, Graphify.Sdk, if(), CreateAsync(), Create(), OllamaOptions(), AzureOpenAIOptions() (+2 more)

### Community 65 - "Entity (Community 65)"
Cohesion: 0.38
Nodes (10): HtmlTemplate.cs, HtmlTemplate.cs, focusNode(), Graphify.Export, addField(), showInfo(), GetScript(), GetStyles() (+2 more)

### Community 70 - "Entity (Community 70)"
Cohesion: 0.22
Nodes (9): WikiExporterTests.cs, ExportAsync_CommunityArticlesCreated(), ExportAsync_EmptyGraph_ProducesValidIndex(), CreateGraphWithCommunities(), ExportAsync_CommunityArticleContainsAuditTrail(), if(), Format_ReturnsWiki(), ExportAsync_NullGraph_ThrowsArgumentNullException() (+1 more)

### Community 68 - "Entity (Community 68)"
Cohesion: 0.42
Nodes (9): ExtractionValidator.cs, ExtractionValidator.cs, Validate(), ValidateNodes(), ValidateEdges(), for(), ExtractionValidator, if() (+1 more)

### Community 69 - "Entity (Community 69)"
Cohesion: 0.22
Nodes (9): UserRepository.cs, GetAllAsync(), FindByEmailAsync(), DeleteAsync(), AddAsync(), UpdateAsync(), MiniLibrary, UserRepository (+1 more)

### Community 67 - "Entity (Community 67)"
Cohesion: 0.42
Nodes (9): AzureOpenAIClientFactoryTests.cs, AzureOpenAIClientFactoryTests.cs, AzureOpenAIOptions_DefaultConstruction_HasEmptyStrings(), AzureOpenAIOptions(), AzureOpenAIOptions_With_CreatesModifiedCopy(), AzureOpenAIOptions_CustomValues_ArePreserved(), Graphify.Tests.Sdk, AzureOpenAIOptions_RecordEquality_WorksCorrectly() (+1 more)

### Community 74 - "Entity (Community 74)"
Cohesion: 0.42
Nodes (9): CacheIntegrationTests.cs, CacheIntegrationTests.cs, Dispose(), Cache_SaveAndReload_PreservesEntries(), Cache_ClearAndReload_IsEmpty(), Cache_DetectsFileChanges(), CacheIntegrationTests(), TestPayload() (+1 more)

### Community 72 - "Entity (Community 72)"
Cohesion: 0.22
Nodes (9): KnowledgeGraph.cs, GetNodesByCommunity(), AssignCommunities(), GetDegree(), GetNeighbors(), GetNodes(), MergeGraph(), Graphify.Graph (+1 more)

### Community 71 - "Entity (Community 71)"
Cohesion: 0.42
Nodes (9): ExtractionPrompts.cs, ExtractionPrompts.cs, TruncateContent(), DocumentationExtraction(), if(), Graphify.Pipeline, PaperExtraction(), CodeSemanticExtraction() (+1 more)

### Community 73 - "Entity (Community 73)"
Cohesion: 0.47
Nodes (9): ValidationResult.cs, ValidationResult.cs, ValidationResult.cs, Failure(), Success(), ValidationResult(), Graphify.Validation, new() (+1 more)

### Community 84 - "Entity (Community 84)"
Cohesion: 0.46
Nodes (8): CopilotExtractorOptionsTests.cs, CopilotExtractorOptionsTests.cs, Graphify.Tests.Sdk, Temperature_AcceptsValidRange(), MaxNodesPerFile_AcceptsPositiveValues(), Construction_WithAllParameters(), ApiKey_CanBeSetAndRetrieved(), DefaultValues_AreCorrect()

### Community 79 - "Entity (Community 79)"
Cohesion: 0.25
Nodes (8): SvgExporter.cs, ExportAsync(), EscapeXml(), GetCommunityColor(), TruncateLabel(), Graphify.Export, GenerateEmptySvg(), GenerateSvg()

### Community 77 - "Entity (Community 77)"
Cohesion: 0.25
Nodes (8): ClusterEngine.cs, DetectCommunities(), CalculateModularity(), ClusterEngine(), ExecuteAsync(), Graphify.Pipeline, SplitCommunity(), CalculateCohesion()

### Community 78 - "Entity (Community 78)"
Cohesion: 0.25
Nodes (8): CopilotChatClient.cs, CopilotChatClient(), Graphify.Sdk, GetStreamingResponseAsync(), Dispose(), ChatResponse(), BuildPrompt(), GetResponseAsync()

### Community 80 - "Entity (Community 80)"
Cohesion: 0.46
Nodes (8): IRepository.cs, IRepository.cs, UpdateAsync(), MiniLibrary, DeleteAsync(), AddAsync(), GetAllAsync(), IRepository

### Community 81 - "Entity (Community 81)"
Cohesion: 0.25
Nodes (8): LlmResponseValidator.cs, ExtractJsonFromMarkdown(), Graphify.Pipeline, LlmEdgeData, LlmExtractionData, Truncate(), ContainsSuspiciousContent(), LlmNodeData

### Community 76 - "Entity (Community 76)"
Cohesion: 0.25
Nodes (8): HtmlExporter.cs, InvalidOperationException(), Graphify.Export, BuildVisNodes(), SanitizeLabel(), BuildLegend(), BuildVisEdges(), BuildCommunityMap()

### Community 75 - "Entity (Community 75)"
Cohesion: 0.25
Nodes (8): UserService.cs, MiniLibrary, UpdateUserAsync(), DeleteUserAsync(), CreateUserAsync(), DeactivateUserAsync(), IsUserActiveAsync(), GetActiveUsersAsync()

### Community 82 - "Entity (Community 82)"
Cohesion: 0.46
Nodes (8): ISecurityValidator.cs, ISecurityValidator.cs, Graphify.Security, ValidateInput(), ValidatePath(), ISecurityValidator, ValidateUrl(), SanitizeLabel()

### Community 83 - "Entity (Community 83)"
Cohesion: 0.25
Nodes (8): WikiExporter.cs, SafeFilename(), GenerateCommunityArticle(), Graphify.Export, GenerateIndex(), ExportAsync(), GenerateGodNodeArticle(), CalculateCohesion()

### Community 92 - "Entity (Community 92)"
Cohesion: 0.52
Nodes (7): ICacheProvider.cs, ICacheProvider.cs, InvalidateAsync(), Graphify.Cache, ICacheProvider, ClearAsync(), ExistsAsync()

### Community 91 - "Entity (Community 91)"
Cohesion: 0.29
Nodes (7): SemanticExtractor.cs, new(), Graphify.Pipeline, BuildPrompt(), catch(), ExtractFromFileAsync(), ExecuteAsync()

### Community 90 - "Entity (Community 90)"
Cohesion: 0.52
Nodes (7): WatchModeTests.cs, WatchModeTests.cs, WatchModeTests(), if(), Graphify.Tests.Pipeline, TestRoot_DirectoryExists_ForTestInfrastructure(), Dispose()

### Community 89 - "Entity (Community 89)"
Cohesion: 0.29
Nodes (7): Program.cs, return(), PathArg(), AddPipelineOptions(), MaskSecret(), FormatValue(), catch()

### Community 87 - "Entity (Community 87)"
Cohesion: 0.29
Nodes (7): CopilotExtractor.cs, ExtractFromFileAsync(), new(), Graphify.Sdk, ExecuteAsync(), BuildPrompt(), catch()

### Community 88 - "Entity (Community 88)"
Cohesion: 0.52
Nodes (7): GraphifyConfig.cs, GraphifyConfig.cs, GraphifyConfig, CopilotSdkConfig, OllamaConfig, Graphify.Cli.Configuration, AzureOpenAIConfig

### Community 86 - "Entity (Community 86)"
Cohesion: 0.29
Nodes (7): GraphBuilder.cs, Graphify.Pipeline, switch(), GraphBuilder(), ExecuteAsync(), EdgeData, MergeNodes()

### Community 85 - "Entity (Community 85)"
Cohesion: 0.29
Nodes (7): ObsidianExporter.cs, EscapeYaml(), Graphify.Export, GenerateIndexFile(), GenerateNodeFile(), ExportAsync(), SafeFilename()

### Community 96 - "Entity (Community 96)"
Cohesion: 0.33
Nodes (6): UserRepository.cs, ArgumentException(), if(), lock(), InvalidOperationException(), ArgumentNullException()

### Community 95 - "Entity (Community 95)"
Cohesion: 0.60
Nodes (6): ServiceCollectionExtensions.cs, ServiceCollectionExtensions.cs, ArgumentNullException(), if(), MiniLibrary, AddMiniLibrary()

### Community 94 - "Entity (Community 94)"
Cohesion: 0.33
Nodes (6): KnowledgeGraph.cs, foreach(), if(), AddNode(), GetEdges(), AddEdge()

### Community 93 - "Entity (Community 93)"
Cohesion: 0.33
Nodes (6): SemanticExtractor.cs, SemanticExtractor(), CreateEmptyResult(), if(), foreach(), ConvertToExtractionResult()

### Community 103 - "Entity (Community 103)"
Cohesion: 0.33
Nodes (6): CopilotChatClient.cs, new(), if(), DisposeAsync(), ChatResponseUpdate(), foreach()

### Community 98 - "Entity (Community 98)"
Cohesion: 0.33
Nodes (6): CopilotExtractor.cs, CreateEmptyResult(), CopilotExtractor(), ConvertToExtractionResult(), if(), foreach()

### Community 99 - "Entity (Community 99)"
Cohesion: 0.33
Nodes (6): LadybugExporter.cs, EscapeLadybugString(), FormatMetadataMap(), ExportAsync(), GenerateLadybugCypher(), Graphify.Export

### Community 97 - "Entity (Community 97)"
Cohesion: 0.33
Nodes (6): ReportGeneratorTests.cs, return(), Generate_NullGraph_ThrowsArgumentNullException(), var(), Generate_IncludesKnowledgeGapsForIsolatedNodes(), Generate_IncludesSurprisingConnections()

### Community 102 - "Entity (Community 102)"
Cohesion: 0.60
Nodes (6): AgentFactory.cs, AgentFactory.cs, CreateExtractionAgent(), Graphify.Sdk, ChatClientAgent(), CreateCopilotAgent()

### Community 101 - "Entity (Community 101)"
Cohesion: 0.47
Nodes (6): Program.cs, Program.cs, if(), var(), foreach(), ShowStyledConfig()

### Community 100 - "Entity (Community 100)"
Cohesion: 0.33
Nodes (6): ConfigPersistence.cs, Save(), StoreApiKeyInUserSecrets(), switch(), GetLocalConfigPath(), Graphify.Cli.Configuration

### Community 117 - "Entity (Community 117)"
Cohesion: 0.40
Nodes (5): WatchMode.cs, catch(), ProcessChangesAsync(), if(), foreach()

### Community 112 - "Entity (Community 112)"
Cohesion: 0.70
Nodes (5): SampleIntegrationTests.cs, SampleIntegrationTests.cs, SampleIntegrationTests, SampleIntegrationTest_ShouldPass(), Graphify.Integration.Tests

### Community 113 - "Entity (Community 113)"
Cohesion: 0.40
Nodes (5): ClusterEngine.cs, foreach(), while(), if(), for()

### Community 115 - "Entity (Community 115)"
Cohesion: 0.40
Nodes (5): UserService.cs, UserService(), if(), InvalidOperationException(), ArgumentException()

### Community 116 - "Entity (Community 116)"
Cohesion: 0.40
Nodes (5): TestGraphFactory.cs, Graphify.Integration.Tests.Helpers, CreateSmallGraph(), CreateMockExtractionResults(), CreateClusterableGraph()

### Community 114 - "Entity (Community 114)"
Cohesion: 0.70
Nodes (5): CopilotSdkClientFactory.cs, CopilotSdkClientFactory.cs, CreateAsync(), CopilotChatClient(), Graphify.Sdk

### Community 108 - "Entity (Community 108)"
Cohesion: 0.70
Nodes (5): GraphEdge.cs, GraphEdge.cs, GetHashCode(), Graphify.Models, Equals()

### Community 109 - "Entity (Community 109)"
Cohesion: 0.40
Nodes (5): PipelineRunner.cs, WriteLineAsync(), if(), foreach(), catch()

### Community 111 - "Entity (Community 111)"
Cohesion: 0.70
Nodes (5): IGraphValidator.cs, IGraphValidator.cs, IGraphValidator, Validate(), Graphify.Validation

### Community 110 - "Entity (Community 110)"
Cohesion: 0.70
Nodes (5): OllamaClientFactory.cs, OllamaClientFactory.cs, Create(), OllamaApiClient(), Graphify.Sdk

### Community 107 - "Entity (Community 107)"
Cohesion: 0.70
Nodes (5): GraphNode.cs, GraphNode.cs, GetHashCode(), Equals(), Graphify.Models

### Community 106 - "Entity (Community 106)"
Cohesion: 0.70
Nodes (5): IGraphExporter.cs, IGraphExporter.cs, Graphify.Export, ExportAsync(), IGraphExporter

### Community 104 - "Entity (Community 104)"
Cohesion: 0.40
Nodes (5): LadybugExporter.cs, if(), AppendCreateEdge(), foreach(), AppendCreateNode()

### Community 105 - "Entity (Community 105)"
Cohesion: 0.40
Nodes (5): Analyzer.cs, if(), FindCrossFileSurprises(), FindCrossCommunityBridges(), foreach()

### Community 118 - "Entity (Community 118)"
Cohesion: 0.70
Nodes (5): ChatClientResolver.cs, ChatClientResolver.cs, Graphify.Cli.Configuration, if(), InvalidOperationException()

### Community 121 - "Entity (Community 121)"
Cohesion: 0.70
Nodes (5): User.cs, User.cs, MiniLibrary, User, Validate()

### Community 119 - "Entity (Community 119)"
Cohesion: 0.70
Nodes (5): JsonExporter.cs, JsonExporter.cs, if(), Graphify.Export, ExportAsync()

### Community 120 - "Entity (Community 120)"
Cohesion: 0.70
Nodes (5): IPipelineStage.cs, IPipelineStage.cs, Graphify.Pipeline, ExecuteAsync(), IPipelineStage

### Community 129 - "Entity (Community 129)"
Cohesion: 0.50
Nodes (4): BenchmarkRunner.cs, CharactersToTokens(), if(), foreach()

### Community 124 - "Entity (Community 124)"
Cohesion: 0.83
Nodes (4): ExtractedNode.cs, ExtractedNode.cs, Graphify.Models, ExtractedNode

### Community 123 - "Entity (Community 123)"
Cohesion: 0.83
Nodes (4): DetectedFile.cs, DetectedFile.cs, Graphify.Models, DetectedFile()

### Community 127 - "Entity (Community 127)"
Cohesion: 0.50
Nodes (4): HtmlExporter.cs, if(), foreach(), ExportAsync()

### Community 128 - "Entity (Community 128)"
Cohesion: 0.83
Nodes (4): AzureOpenAIOptions.cs, AzureOpenAIOptions.cs, AzureOpenAIOptions(), Graphify.Sdk

### Community 125 - "Entity (Community 125)"
Cohesion: 0.50
Nodes (4): SvgExporter.cs, for(), foreach(), if()

### Community 126 - "Entity (Community 126)"
Cohesion: 0.83
Nodes (4): AzureOpenAIClientFactory.cs, AzureOpenAIClientFactory.cs, Create(), Graphify.Sdk

### Community 122 - "Entity (Community 122)"
Cohesion: 0.50
Nodes (4): FileDetector.cs, if(), catch(), foreach()

### Community 136 - "Entity (Community 136)"
Cohesion: 0.50
Nodes (4): RelativePathHandlingTests.cs, foreach(), for(), if()

### Community 130 - "Entity (Community 130)"
Cohesion: 0.50
Nodes (4): TimeoutRegressionTests.cs, AllAsyncTests_HaveTimeoutAttribute_RegressionBug3(), foreach(), Graphify.Tests.Regression

### Community 131 - "Entity (Community 131)"
Cohesion: 0.50
Nodes (4): GraphBuilder.cs, EdgeKey(), foreach(), if()

### Community 133 - "Entity (Community 133)"
Cohesion: 0.83
Nodes (4): CacheEntry.cs, CacheEntry.cs, CacheEntry(), Graphify.Cache

### Community 134 - "Entity (Community 134)"
Cohesion: 0.83
Nodes (4): ExtractedEdge.cs, ExtractedEdge.cs, ExtractedEdge, Graphify.Models

### Community 135 - "Entity (Community 135)"
Cohesion: 0.83
Nodes (4): ExtractionResult.cs, ExtractionResult.cs, ExtractionResult, Graphify.Models

### Community 132 - "Entity (Community 132)"
Cohesion: 0.50
Nodes (4): LlmResponseValidator.cs, ScriptPattern(), if(), foreach()

### Community 144 - "Entity (Community 144)"
Cohesion: 0.83
Nodes (4): CopilotSdkOptions.cs, CopilotSdkOptions.cs, CopilotSdkOptions(), Graphify.Sdk

### Community 145 - "Entity (Community 145)"
Cohesion: 0.83
Nodes (4): CliProviderOptions.cs, CliProviderOptions.cs, Graphify.Cli.Configuration, CliProviderOptions()

### Community 139 - "Entity (Community 139)"
Cohesion: 0.83
Nodes (4): CopilotExtractorOptions.cs, CopilotExtractorOptions.cs, Graphify.Sdk, CopilotExtractorOptions

### Community 141 - "Entity (Community 141)"
Cohesion: 0.83
Nodes (4): FileDetectorOptions.cs, FileDetectorOptions.cs, FileDetectorOptions(), Graphify.Pipeline

### Community 142 - "Entity (Community 142)"
Cohesion: 0.83
Nodes (4): GraphBuilderOptions.cs, GraphBuilderOptions.cs, Graphify.Pipeline, GraphBuilderOptions

### Community 138 - "Entity (Community 138)"
Cohesion: 0.83
Nodes (4): SemanticExtractorOptions.cs, SemanticExtractorOptions.cs, Graphify.Pipeline, SemanticExtractorOptions

### Community 140 - "Entity (Community 140)"
Cohesion: 0.83
Nodes (4): IDataIngester.cs, IDataIngester.cs, Graphify.Ingest, IDataIngester

### Community 137 - "Entity (Community 137)"
Cohesion: 0.50
Nodes (4): UrlIngester.cs, if(), FetchWebpageAsync(), ValidateUrl()

### Community 143 - "Entity (Community 143)"
Cohesion: 0.83
Nodes (4): OllamaOptions.cs, OllamaOptions.cs, OllamaOptions(), Graphify.Sdk

### Community 157 - "Entity (Community 157)"
Cohesion: 1.00
Nodes (3): ClusterOptions.cs, Graphify.Pipeline, ClusterOptions.cs

### Community 161 - "Entity (Community 161)"
Cohesion: 1.00
Nodes (3): AnalysisResult.cs, AnalysisResult.cs, Graphify.Models

### Community 162 - "Entity (Community 162)"
Cohesion: 0.67
Nodes (3): ConfigPersistence.cs, if(), catch()

### Community 160 - "Entity (Community 160)"
Cohesion: 0.67
Nodes (3): TestGraphFactory.cs, CreateMultiFileExtractionResults(), for()

### Community 156 - "Entity (Community 156)"
Cohesion: 1.00
Nodes (3): AnalyzerOptions.cs, AnalyzerOptions.cs, Graphify.Pipeline

### Community 155 - "Entity (Community 155)"
Cohesion: 1.00
Nodes (3): Graphify.Models, GraphReport.cs, GraphReport.cs

### Community 158 - "Entity (Community 158)"
Cohesion: 0.67
Nodes (3): InputValidator.cs, if(), ControlCharPattern()

### Community 159 - "Entity (Community 159)"
Cohesion: 0.67
Nodes (3): ObsidianExporter.cs, foreach(), if()

### Community 154 - "Entity (Community 154)"
Cohesion: 1.00
Nodes (3): FileType.cs, Graphify.Models, FileType.cs

### Community 153 - "Entity (Community 153)"
Cohesion: 1.00
Nodes (3): Confidence.cs, Graphify.Models, Confidence.cs

### Community 152 - "Entity (Community 152)"
Cohesion: 1.00
Nodes (3): Graphify.Models, FileCategory.cs, FileCategory.cs

### Community 146 - "Entity (Community 146)"
Cohesion: 1.00
Nodes (3): McpServerOptions.cs, Graphify.Mcp, McpServerOptions.cs

### Community 147 - "Entity (Community 147)"
Cohesion: 0.67
Nodes (3): GraphTools.cs, if(), GraphTools()

### Community 151 - "Entity (Community 151)"
Cohesion: 0.67
Nodes (3): Neo4jExporter.cs, foreach(), if()

### Community 150 - "Entity (Community 150)"
Cohesion: 0.67
Nodes (3): ConfigurationFactory.cs, Graphify.Cli.Configuration, Build()

### Community 149 - "Entity (Community 149)"
Cohesion: 0.67
Nodes (3): TimeoutRegressionTests.cs, if(), SemaphoreSlim_DoubleAcquire_DetectedByTimeout_RegressionBug3()

### Community 148 - "Entity (Community 148)"
Cohesion: 0.67
Nodes (3): WikiExporter.cs, foreach(), if()

### Community 166 - "Entity (Community 166)"
Cohesion: 1.00
Nodes (2): SecurityHardeningTests.cs, if()

### Community 163 - "Entity (Community 163)"
Cohesion: 1.00
Nodes (2): squad.config.ts, squad.config.ts

### Community 165 - "Entity (Community 165)"
Cohesion: 1.00
Nodes (2): ConfigurationFactory.cs, if()

### Community 164 - "Entity (Community 164)"
Cohesion: 1.00
Nodes (2): ExtractionValidatorTests.cs, new()

## Suggested Questions
_Not enough signal to generate questions. The graph has no ambiguous edges, no bridge nodes, and all communities are well-connected._

## Knowledge Gaps
- **2 isolated node(s):** `squad.config.ts`, `squad.config.ts`
  These have ≤1 connection - possible missing edges or undocumented components.

