---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/connect-bigquery/
title: Connect to BigQuery \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:41:28.666752+00:00
---

# Connect to BigQuery  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/connect-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Connect to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

With the Conversational Analytics API, you can connect a data agent to BigQuery to let users ask questions about your data in natural language and receive answers as text, tables, or charts.

To configure your data sources, define references to BigQuery tables, graphs, or both by using either the Python SDK or HTTP. You then provide these references when you create a persistent data agent or send a stateless chat query with inline context, as described in [Build a data agent using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http) and [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).

## Before you begin

Before you connect a data agent to BigQuery, complete the following tasks:

  1. In your Google Cloud project, [enable the required APIs](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api) for the Conversational Analytics API and BigQuery.
  2. Verify that you have the required Identity and Access Management (IAM) roles.
  3. Ensure that you have access to the BigQuery datasets, tables, or graphs that you want to query.



### Required roles

To get the permissions that you need to connect a data agent to BigQuery and run queries, ask your administrator to grant you the following IAM roles: 

  * Create or manage data agents: 
    * [Gemini Data Analytics Data Agent Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentCreator) (`roles/geminidataanalytics.dataAgentCreator`) on your project
    * [Gemini Data Analytics Data Agent Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentEditor) (`roles/geminidataanalytics.dataAgentEditor`) on your project
  * Chat with data agents: 
    * [Gemini Data Analytics Data Agent User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentUser) (`roles/geminidataanalytics.dataAgentUser`) on your project
    * [Gemini for Google Cloud User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`) on your project
  * Send stateless chat queries with inline context: [Gemini Data Analytics Stateless Chat User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentStatelessUser) (`roles/geminidataanalytics.dataAgentStatelessUser`) on your project 
  * Run BigQuery queries: [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on your billing project 
  * Read BigQuery data: [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on your dataset, table, or graph 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Connect to BigQuery tables

To connect to BigQuery tables, you specify table references in your data source configuration and attach them to a `published_context` object. You can connect to multiple tables across different projects and datasets. If you're sending stateless chat queries without creating a persistent data agent, you can provide this data source configuration in the `inline_context` field of your request instead.

To connect to Lakehouse tables that use the Apache Iceberg REST catalog or an external catalog, use the four-part [P.C.N.T syntax](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#pcnt). When configuring table references for Lakehouse tables, specify `catalog.namespace` for the dataset ID.

The following sample code connects to two tables and configures a `published_context` object with the data sources. The first table (`TABLE_ID_1`) defines optional custom descriptions for the table and a column to provide additional semantic context, while the second table (`TABLE_ID_2`) relies on automatic schema discovery:

### Python SDK
    
    
    # Table 1: Define a table reference with custom table and column descriptions
    table_reference_1 = geminidataanalytics.BigQueryTableReference()
    table_reference_1.project_id = "PROJECT_ID"
    table_reference_1.dataset_id = "DATASET_ID"
    table_reference_1.table_id = "TABLE_ID_1"
    # Optional: Provide semantic descriptions for the table and specific columns
    table_reference_1.schema = geminidataanalytics.Schema()
    table_reference_1.schema.description = "TABLE_DESCRIPTION"
    table_reference_1.schema.fields = [
        geminidataanalytics.Field(
            name="COLUMN_NAME",
            description="COLUMN_DESCRIPTION",
        )
    ]
    
    # Table 2: Minimal table reference that relies on automatic schema discovery
    table_reference_2 = geminidataanalytics.BigQueryTableReference()
    table_reference_2.project_id = "PROJECT_ID"
    table_reference_2.dataset_id = "DATASET_ID"
    table_reference_2.table_id = "TABLE_ID_2"
    
    # Combine table references into a data source configuration
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.bq.table_references = [
        table_reference_1,
        table_reference_2,
    ]
    
    # Attach the data source to published context
    published_context = geminidataanalytics.Context()
    published_context.datasource_references = datasource_references
    

Replace the sample values as follows:

  * PROJECT_ID: The ID of the Google Cloud project that contains your BigQuery dataset and tables. To connect to a [public dataset](https://docs.cloud.google.com/bigquery/public-data), specify `bigquery-public-data`.
  * DATASET_ID: The ID of the BigQuery dataset that contains your tables. For example, `san_francisco`.
  * TABLE_ID_1 and TABLE_ID_2: The IDs of the BigQuery tables to connect. For example, `street_trees`.
  * TABLE_DESCRIPTION: An optional description of the table's content and purpose.
  * COLUMN_NAME: The name of a column in the table for which you're providing an optional description.
  * COLUMN_DESCRIPTION: An optional description of the column's content and purpose.



### HTTP
    
    
    bigquery_data_sources = {
        "bq": {
            "tableReferences": [
                # Table 1: Define a table reference with custom table and column descriptions
                {
                    "projectId": "PROJECT_ID",
                    "datasetId": "DATASET_ID",
                    "tableId": "TABLE_ID_1",
                    # Optional: Provide semantic descriptions for the table and specific columns
                    "schema": {
                        "description": "TABLE_DESCRIPTION",
                        "fields": [
                            {
                                "name": "COLUMN_NAME",
                                "description": "COLUMN_DESCRIPTION",
                            }
                        ],
                    },
                },
                # Table 2: Minimal table reference that relies on automatic schema discovery
                {
                    "projectId": "PROJECT_ID",
                    "datasetId": "DATASET_ID",
                    "tableId": "TABLE_ID_2",
                },
            ],
        },
    }
    
    # Attach the data source to published context
    published_context = {
        "datasourceReferences": bigquery_data_sources,
    }
    

Replace the sample values as follows:

  * PROJECT_ID: The ID of the Google Cloud project that contains your BigQuery dataset and tables. To connect to a [public dataset](https://docs.cloud.google.com/bigquery/public-data), specify `bigquery-public-data`.
  * DATASET_ID: The ID of the BigQuery dataset that contains your tables. For example, `san_francisco`.
  * TABLE_ID_1 and TABLE_ID_2: The IDs of the BigQuery tables to connect. For example, `street_trees`.
  * TABLE_DESCRIPTION: An optional description of the table's content and purpose.
  * COLUMN_NAME: The name of a column in the table for which you're providing an optional description.
  * COLUMN_DESCRIPTION: An optional description of the column's content and purpose.



While there are no hard limits on the number of tables that you can connect, connecting a large number of tables or tables across unrelated domains can reduce query accuracy—particularly for queries that require complex joins—or exceed the model's input token limit. Configure each data agent with related tables for a specific use case.

To provide additional context for your tables, such as synonyms, tags, example queries, or user-defined functions, see [Define data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq).

## Connect to BigQuery Graph

You can connect to graphs by using [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview). You can configure a data agent to query graphs alone or to combine graph and table references in the same data source configuration. To connect, provide one or more graph references in the `property_graph_references` field (for the Python SDK) or the `propertyGraphReferences` field (for HTTP).

Depending on your graph schema and the question that is asked, the Conversational Analytics API queries a graph by using either Graph Query Language (GQL) or the [`GRAPH_EXPAND`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/graph-sql-queries#graph_expand) table-valued function in SQL:

  * GQL queries require a [BigQuery Enterprise or Enterprise Plus edition](https://docs.cloud.google.com/bigquery/docs/editions-intro) reservation. In projects with on-demand pricing, GQL queries fail with an error and aren't retried with `GRAPH_EXPAND`.
  * `GRAPH_EXPAND` queries can run with on-demand pricing but aren't supported for all graphs. For requirements and limitations, see the [BigQuery Graph overview](https://docs.cloud.google.com/bigquery/docs/graph-overview) and [`GRAPH_EXPAND`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/graph-sql-queries#graph_expand).



The following sample code defines a connection to a graph and configures a `published_context` object:

### Python SDK
    
    
    # Define a BigQuery Graph reference
    graph_reference = geminidataanalytics.BigQueryPropertyGraphReference()
    graph_reference.project_id = "GRAPH_PROJECT_ID"
    graph_reference.dataset_id = "GRAPH_DATASET_ID"
    graph_reference.property_graph_id = "GRAPH_ID"
    
    # Combine references into a data source configuration
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.bq.property_graph_references = [graph_reference]
    
    # Attach the data source to published context
    published_context = geminidataanalytics.Context()
    published_context.datasource_references = datasource_references
    

Replace the sample values as follows:

  * GRAPH_PROJECT_ID: The ID of the Google Cloud project that contains your BigQuery graph.
  * GRAPH_DATASET_ID: The ID of the BigQuery dataset that contains your graph. For example, `financial_data`.
  * GRAPH_ID: The ID of the BigQuery graph. For example, `FinGraph`.



### HTTP
    
    
    bigquery_data_sources = {
        "bq": {
            "propertyGraphReferences": [
                # Define a BigQuery Graph reference
                {
                    "projectId": "GRAPH_PROJECT_ID",
                    "datasetId": "GRAPH_DATASET_ID",
                    "propertyGraphId": "GRAPH_ID",
                },
            ],
        },
    }
    
    # Attach the data source to published context
    published_context = {
        "datasourceReferences": bigquery_data_sources,
    }
    

Replace the sample values as follows:

  * GRAPH_PROJECT_ID: The ID of the Google Cloud project that contains your BigQuery graph.
  * GRAPH_DATASET_ID: The ID of the BigQuery dataset that contains your graph. For example, `financial_data`.
  * GRAPH_ID: The ID of the BigQuery graph. For example, `FinGraph`.



To query both tables and graphs with the same data agent, include both `table_references` and `property_graph_references` (Python SDK) or `tableReferences` and `propertyGraphReferences` (HTTP) in your `bq` data source configuration.

## What's next

  * [Define data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq) to improve your agent's performance with descriptions, synonyms, and example queries.
  * Create a data agent or send stateless chat queries with your data source configuration, as described in [Build a data agent using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http) or [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
