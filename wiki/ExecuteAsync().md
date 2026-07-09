# ExecuteAsync()

> Auto-generated from the knowledge graph (refine_wiki.py, static). Node id: `analyzer_executeasync`

- **File:** `src/Graphify/Pipeline/Analyzer.cs`
- **Type:** Entity
- **Community:** [[Community 30]]
- **Also known as:** `filedetector_executeasync`, `semanticextractor_executeasync`, `copilotextractor_executeasync`, `graphbuilder_executeasync`, `clusterengine_executeasync`, `extractor_executeasync`, `ipipelinestage_executeasync`

## Relationships

- ← *contains* `Analyzer.cs`
- ← *contains* `Analyzer.cs`
- → *implements* `ExecuteAsync()`
- → *calls* `FindGodNodes()`
- → *calls* `FindSurprisingConnections()`
- → *calls* `GenerateSuggestedQuestions()`
- → *calls* `CalculateStatistics()`
- ← *calls* `FullPipeline_WithMockExtractor_ProducesValidGraph()`
- ← *calls* `ReportGeneration_ProducesMarkdownReport()`
- ← *calls* `ExecuteAsync_GodNodeDetection_FindsHighestDegree()`
- ← *calls* `ExecuteAsync_SurprisingConnections_FindsCrossCommunity()`
- ← *calls* `ExecuteAsync_Statistics_CalculatedCorrectly()`
- ← *calls* `ExecuteAsync_EmptyGraph_ReturnsEmptyAnalysis()`
- ← *calls* `ExecuteAsync_SuggestedQuestions_Generated()`
- ← *calls* `ExecuteAsync_IsolatedNodes_DetectedInQuestions()`
- ← *calls* `ExecuteAsync_BridgeNodes_DetectedInQuestions()`
- ← *calls* `ExecuteAsync_TopGodNodesCount_LimitsResults()`
- ← *calls* `ExecuteAsync_CrossFileSurprises_DetectedWithMultipleSources()`
- ← *calls* `ExecuteAsync_NoSignal_ReturnsNoSignalQuestion()`
