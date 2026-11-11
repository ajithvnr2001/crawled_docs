---
url: https://docs.cloud.google.com/bigquery/docs/sessions-intro/
title: Introduction to sessions \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:51:12.850469+00:00
---

# Introduction to sessions  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/sessions-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to sessions

A BigQuery session lets you capture your SQL activities and maintain state across multiple queries. Within a session, you can define temporary tables, temporary functions, and variables once and reuse them as you interactively build queries or run multi-statement transactions.

Multiple sessions can be active at the same time, and BigQuery saves the history of each session for up to 20 days after the session ends. Before you work with sessions, make sure that you are familiar with [BigQuery](https://docs.cloud.google.com/bigquery/docs) and [GoogleSQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax).

## Use cases

Typical uses for a session include the following:

  * **Maintain transient session data.** Define variables and temporary tables once and use them throughout the session.

  * **Look up query history by session.** If you want to keep track of a behavior that happened at a particular time during the session, you can view the history of changes that were made during the session.

  * **Create multi-statement transactions over multiple queries.** Within a session, you can begin a transaction, make changes, and view the temporary result before deciding to commit or rollback. You can do this over several queries in the session. If you don't use a session, a multi-statement transaction needs to be completed in a single query.




## Pricing

  * There are no additional costs for using sessions.

  * For projects that use on-demand pricing, queries against `INFORMATION_SCHEMA` incur charges. For more information, see [`INFORMATION_SCHEMA` pricing](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#pricing).

  * You are charged for temporary tables that you create in sessions. Storage charges are based on how much data is stored in the tables. For information about storage pricing, see [Storage pricing](https://cloud.google.com/bigquery/pricing#storage).




## Limitations

  * Every query in a session is run in the location where the session was created. If the location isn't specified, or if it can't be inferred from the query that creates the session, the session is created in the [default location](https://docs.cloud.google.com/bigquery/docs/default-configuration#global-settings).

  * A session is automatically terminated after 24 hours of inactivity.

  * A session is automatically terminated 7 days after its creation.

  * The maximum size of a session variable is 1 MB, and the maximum size of all variables used in a session is 10 MB.

  * Concurrent queries aren't allowed within a session.




## Roles and permissions

This section describes the [Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/bigquery/docs/access-control#bq-permissions) and the [IAM roles](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery) that you need to perform actions with sessions.

Actions | Required permissions | Default roles  
---|---|---  
Create a new session. Work with an existing session that you created.  | `bigquery.jobs.create` |  `bigquery.user`  
`bigquery.Jobuser`  
`bigquery.admin`  
  
Terminate a session that you created.  | `bigquery.jobs.create` |  `bigquery.user`  
`bigquery.Jobuser`  
`bigquery.admin`  
  
Terminate a session another user created.  |  `bigquery.jobs.create`  
`bigquery.jobs.update`  
|  `bigquery.admin`  
  
View a list of your sessions in a project. This list includes the IDs for sessions you've created in a project with `[INFORMATION_SCHEMA.JOBS_BY_USER](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-by-user)`.  | `bigquery.jobs.list` |  `bigquery.user`  
`bigquery.Jobuser`  
`bigquery.admin`  
  
View all sessions for all users in a project. This list includes the IDs for all sessions created in the project with `[INFORMATION_SCHEMA.JOBS](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs)`.  | `bigquery.jobs.listAll` |  `bigquery.admin`  
View metadata for sessions created by the current user in the current project with `[INFORMATION_SCHEMA.SESSIONS_BY_USER](https://docs.cloud.google.com/bigquery/docs/information-schema-sessions-by-user)`.  | `bigquery.jobs.list` |  `bigquery.user`  
`bigquery.Jobuser`  
`bigquery.admin`  
  
View metadata for all sessions in the current project with `[INFORMATION_SCHEMA.SESSIONS_BY_PROJECT](https://docs.cloud.google.com/bigquery/docs/information-schema-sessions-by-project)`.  | `bigquery.jobs.listAll` |  `bigquery.admin`  
  
## What's next

  * Learn more about how to [write queries in sessions](https://docs.cloud.google.com/bigquery/docs/sessions-write-queries).
  * Learn more about how to [work with sessions](https://docs.cloud.google.com/bigquery/docs/sessions), including how to create, use, terminate, and list your sessions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
