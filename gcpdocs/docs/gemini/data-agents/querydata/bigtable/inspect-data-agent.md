---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/inspect-data-agent/
title: Test QueryData in Bigtable Studio \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:08:29.301799+00:00
---

# Test QueryData in Bigtable Studio  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/inspect-data-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Test QueryData in Bigtable Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to test QueryData and update the context set file. You can test QueryData's ability to generate SQL queries from natural language questions. If a generated query is not accurate, you can update the context set file.

To learn about context sets, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview). 

## Before you begin

Make sure that a context set is already created and the context set file is uploaded to the QueryData agent. For more information, see [Manage context sets in Bigtable Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/manage-data-agents).

To download, update, and upload context set files, make sure that the IAM user has the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role on the project. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).

## Test QueryData

To test a QueryData, perform the following steps:

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. In the **Explorer pane** , click **View actions** next to the context set you're using.

  5. Click **Test context set**.

  6. In the query editor, click **Generate SQL using QueryData with: CONTEXT_SET_NAME** to open the **Help me code** panel.

  7. Enter a natural language question in the editor to generate a SQL query, and click **Generate**.

  8. Review the SQL query for accuracy. Click **Insert** to add the query to the editor.




## Download and update a context set

If you are not satisfied with the generated SQL query for a natural language question, download the existing context set file. You can then review and update the query template, and reupload the updated context file to the agent.

To download and update a context set, perform the following steps:

  1. In the **Explorer pane** , click **View actions** next to the context set you're using.
  2. Click **Download context file**.
  3. Follow steps in [Build context sets using the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/build-context-sets) to update context with additional query pairs.
  4. In the **Explorer pane** , click **View actions** next to the context set you're using.
  5. Click **Edit context set**.
  6. Click **Browse** in the **Upload context file** section, and select the updated context set file.
  7. Click **Save** to update the context set.



After you are satisfied with the accuracy of your responses, you can use the `QueryData` endpoint to connect your application to the context set.

**Note:** After you upload the updated context set file, it overwrites the existing context set.

## Find the context set ID

To connect a data application to the QueryData agent, you need the context set's ID.

  1. In the Google Cloud console, go to the Bigtable page.

[Go to Bigtable](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation menu, click **Bigtable Studio**. 

  4. In the **Explorer pane** , click **View actions** next to the context set you're using.

  5. Click **Edit context set**.

  6. Note the context ID in **Context set ID**. The context set ID format is similar to `projects/PROJECT_ID/locations/LOCATION/contextSetGroups/GROUP_ID/contextSets/CONTEXT_SET_ID@v1`.




## Connect QueryData to application

Set the context set ID in the `QueryData` method call to provide authored context for database data sources such as AlloyDB, Spanner, Cloud SQL, Cloud SQL for PostgreSQL, Firestore, and Bigtable. For more information, see [Define data agent context for database data sources](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview).

After testing the context set, you can reference the database data source in your `QueryData` call.

### Example `QueryData` request with authored context

The following example shows a `QueryData` request using `bigtable_reference` database data source. The `agent_context_reference.context_set_id` field is used to link to the context set that contains your authored context.
    
    
    POST https://geminidataanalytics.googleapis.com/v1beta/projects/context-set-project/locations/us-central1:queryData
    
    
    {
      "parent": "projects/context-set-project/locations/us-central1",
      "prompt": "List the names and ratings of all hotels located in London.",
      "context": {
        "datasource_references": {
          "bigtable_reference": {
            "database_reference": {
              "project_id": "context-set-project",
              "instance_id": "evalbench"
            },
            "agent_context_reference": {
              "context_set_id": "projects/context-set-project/locations/us-central1/contextSets/hotels_bigtable_all_templates"
            }
          }
        }
      },
      "generation_options": {
        "generate_query_result": true,
        "generate_natural_language_answer": true,
        "generate_disambiguation_question": true,
        "generate_explanation": true
      }
    }

The request body contains the following fields:

  * `prompt`: The natural language question from the end user.
  * `context`: Contains information about the data sources. 
    * `datasource_references`: Specifies the data source type. 
      * `bigtable_reference`: Required when querying the database. This field changes based on the database you are querying. 
        * `database_reference`: Specifies information related to your Bigtable instance. 
          * `project_id`: The project ID that the Bigtable instance belongs to.
          * `instance_id`: The instance ID of the Bigtable instance.
          * `table_ids`: Optional. The table IDs to scope the agent to. If unset, all tables in the instance are included.
        * `agent_context_reference`: Links to authored context. 
          * `context_set_id`: The complete context set ID of the context set that contains your authored context. For example, `projects/PROJECT_ID/locations/LOCATION/contextSetGroups/GROUP_ID/contextSets/CONTEXT_SET_ID@v1`.
  * `generation_options`: Configures the type of output to generate. 
    * `generate_query_result`: Set to true to generate and return the query results.
    * `generate_natural_language_answer`: Optional. If set to true, generates a natural language answer.
    * `generate_explanation`: Optional. If set to true, generates an explanation of the SQL query.
    * `generate_disambiguation_question`: Optional. If set to true, generates disambiguation questions if the query is ambiguous.



### Example `QueryData` response

Here is an example of a successful response from a `QueryData` call:
    
    
    {
      "generatedQuery": "SELECT COUNT(*) FROM `hotels` WHERE CAST(cf['location'] AS STRING) = 'London'",
      "intentExplanation": "count of hotels in London",
      "queryResult": {
        "columns": [
          {
            "name": "$col1",
            "type": "int64_type:{}"
          }
        ],
        "rows": [
          {
            "values": [
              {
                "value": "2"
              }
            ]
          }
        ],
        "totalRowCount": "1"
      },
      "naturalLanguageAnswer": "Based on the data, there are 2 hotels located in London."
    }
    

## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/context-sets-overview).
  * Learn how to [build context sets using the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/build-context-sets).
  * Learn how to [Manage context sets in Bigtable Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/bigtable/manage-data-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
