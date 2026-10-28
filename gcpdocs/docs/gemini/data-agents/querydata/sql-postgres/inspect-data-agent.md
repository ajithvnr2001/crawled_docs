---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/
title: Test QueryData using Cloud SQL Studio \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:15:04.688926+00:00
---

# Test QueryData using Cloud SQL Studio  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/

[ Skip to main content ](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/)
  * [Deutsch](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/gemini-color.svg) ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#before-you-begin)
  * [Test QueryData](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#test-context-set)
  * [Download and update a context set](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#download-update-context)
  * [Find the context set ID](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#find-context-set-id)
  * [Connect QueryData to application](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#connect-to-your-application)
    * [Example QueryData request with authored context](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#example_querydata_request_with_authored_context)
    * [Example QueryData response](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#example_querydata_response)
  * [What's next](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)


Was this helpful?
Send feedback 
#  Test QueryData using Cloud SQL Studio Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#before-you-begin)
  * [Test QueryData](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#test-context-set)
  * [Download and update a context set](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#download-update-context)
  * [Find the context set ID](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#find-context-set-id)
  * [Connect QueryData to application](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#connect-to-your-application)
    * [Example QueryData request with authored context](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#example_querydata_request_with_authored_context)
    * [Example QueryData response](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#example_querydata_response)
  * [What's next](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/inspect-data-agent/#whats-next)


This document describes how to test QueryData and update the context set file. You can test QueryData's ability to generate SQL queries from natural language questions. If a generated query is not accurate, you can update the context set file.
To learn about context sets, see [Context sets overview](https://docs.cloud.google.com/sql/docs/postgres/context-sets-overview). 
## Before you begin
Make sure that a context set is already created and the context set file is uploaded to the QueryData agent. For more information, see [Manage context sets in Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-agents).
To download, update, and upload context set files, make sure that the IAM user has the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role on the project. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).
## Test QueryData
To test a QueryData, perform the following steps:
  1. In the Google Cloud console, go to the Cloud SQL page.
[Go to Cloud SQL](https://console.cloud.google.com/sql)
  2. Select an instance from the list.
  3. In the navigation menu, click **Cloud SQL Studio**. 
  4. Sign in to **Studio** using Identity and Access Management authentication. 
  5. In the **Explorer pane** , click **View actions** next to the context set you're using.
  6. Click **Test context set**.
  7. In the query editor, click **Generate SQL** to open the **Help me code** panel.
  8. Enter a natural language question in the editor to generate a SQL query, and click **Generate**.
  9. Review the SQL query for accuracy.


## Download and update a context set
If you are not satisfied with the generated SQL query for a natural language question, download the existing context set file. You can then review and update the query template, and reupload the updated context file to the agent.
To download and update a context set, perform the following steps:
  1. In the **Explorer pane** , click **View actions**.
  2. Click **Download context file**.
  3. Follow steps in [Build contexts sets using the context engineering agent](https://docs.cloud.google.com/sql/docs/postgres/build-context-gemini-cli) to update context with additional query pairs.
  4. In the **Explorer pane** , click **View actions** next to the context set you're using.
  5. Click **Edit context set**.
  6. Click **Browse** in the **Upload context set file** section, and select the updated context set file.
  7. Click **Save** to update the context set.


After you are satisfied with the accuracy of your responses, you can use the `QueryData` endpoint to connect your application to the context set.
## Find the context set ID
To connect a data application to the QueryData agent, you need the context set's ID.
  1. In the Google Cloud console, go to the Cloud SQL page.
[Go to Cloud SQL](https://console.cloud.google.com/sql)
  2. Select an instance from the list.
  3. In the navigation menu, click **Cloud SQL Studio**. 
  4. Sign into **Studio** using Identity and Access Management authentication. 
  5. In the **Explorer pane** , click **View actions** next to the context set you're using.
  6. Click **Edit context set**.
  7. Note the context ID in **Context set ID**. The context set ID format is similar to `projects/data-agents-project/locations/us-central1/contextSets/bdf_pg_all_templates`.


## Connect QueryData to application
Set the context set ID in the `QueryData` method call to provide authored context for database data sources such as AlloyDB, Spanner, Cloud SQL, Cloud SQL for PostgreSQL, and Firestore. For more information, see [Define data agent context for database data sources](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/data-agent-authored-context-databases).
After testing the context set, you can reference the database data source in your `QueryData` call.
### Example `QueryData` request with authored context
The following example shows a `QueryData` request using `cloud_sql_reference` database data source. The `agent_context_reference.context_set_id` field is used to link to pre-authored context stored in the database.

```
{
  "parent": "projects/context-set-project/locations/us-central1",
  "prompt": "How many accounts in the Prague region are eligible for loans?? A3 contains the data of region.",
  "context": {
    "datasource_references": [
      {
        "cloud_sql_reference": {
          "database_reference": {
            "engine": "POSTGRESQL"
            "project_id": "context-set-project",
            "region": "us-central1",
            "instance_id": "context-set-primary",
            "database_id": "financial"
          },
          "agent_context_reference": {
            "context_set_id": "projects/context-set-project/locations/us-central1/contextSets/bdf_pg_all_templates"
          }
        }
      }
    ]
  },
  "generation_options": {
    "generate_query_result": true,
    "generate_natural_language_answer": true,
    "generate_disambiguation_question": true,
    "generate_explanation": true
  }
}
```

The request body contains the following fields:
  * `prompt`: The natural language question from the end user.
  * `context`: Contains information about the data sources. 
    * `datasource_references`: Specifies the data source type. 
      * `cloud_sql_reference`: Required when querying the database. This field changes based on the database you are querying. 
        * `database_reference`: Specifies information related to your database instance. 
          * `engine`: The database engine. Set to `POSTGRESQL` for Cloud SQL instances.
          * `project_id`: The project ID of the database instance.
          * `region`: The region of the Cloud SQL instance.
          * `instance_id`: The instance ID of the Cloud SQL instance.
          * `database_id`: The ID of the database.
        * `agent_context_reference`: Links to authored context in the database. 
          * `context_set_id`: The complete context set ID of the context stored in the database. For example, `projects/context-set-project/locations/us-central1/contextSets/bdf_gsql_gemini_all_templates`.
  * `generationOptions`: Configures the type of output to generate. 
    * `generate_query_result`: Set to true to generate and return the query results.
    * `generate_natural_language_answer`: Optional. If set to true, generates a natural language answer.
    * `generate_explanation`: Optional. If set to true, generates an explanation of the SQL query.
    * `generate_disambiguation_question`: Optional. If set to true, generates disambiguation questions if the query is ambiguous.


### Example `QueryData` response
Here is an example of a successful response from a `QueryData` call:

```
{
  "generated_query": "-- Count the number of accounts in Prague that are eligible for loans\nSELECT\n  COUNT(DISTINCT \"loans\".\"account_id\")\nFROM \"loans\"\nJOIN \"district\" -- Join based on district ID\n  ON \"loans\".\"district_id\" = \"district\".\"district_id\"\nWHERE\n  \"district\".\"A3\" = 'Prague'; -- Filter for the Prague region",
  "intent_explanation": "The question asks for the number of accounts eligible for loans in the Prague region. I need to join the `district` table with the `loans` table to filter by region and count the distinct accounts. The `A3` column in the `district` table contains the region information, and I'll filter for 'Prague'. The `loans` table contains information about loans, including the `account_id` and `district_id`. I will join these two tables on their respective district IDs.",
  "query_result": {
    "columns": [
      {
        "name": "count"
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
    "total_row_count": 1
  },
  "natural_language_answer": "There are 2 accounts in Prague that are eligible for loans."
}

```

## What's next
  * Learn more about [context sets](https://docs.cloud.google.com/sql/docs/postgres/context-sets-overview).
  * Learn how to [build contexts sets using the context engineering agent](https://docs.cloud.google.com/sql/docs/postgres/build-context-gemini-cli).
  * Learn how to [Manage context sets in Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-agents).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
