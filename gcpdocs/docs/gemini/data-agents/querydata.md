---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/
title: Introduction to QueryData \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:53:51.236967+00:00
---

# Introduction to QueryData  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Introduction to QueryData Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

QueryData is a natural language to SQL (NL2SQL) tool in the [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview) that lets your AI agents and applications query operational databases using natural language. When an application or agent sends a question using natural language, QueryData translates the question into a dialect-specific SQL query, runs the query against your database, and returns the query results along with the generated SQL and an explanation of how QueryData interpreted the question.

For more information about using QueryData with your database, see the documentation for the supported databases:

  * [AlloyDB for PostgreSQL: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/alloydb/data-agent-overview)
  * [Cloud SQL for MySQL: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/data-agent-overview)
  * [Cloud SQL for PostgreSQL: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/data-agent-overview)
  * [Spanner: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/data-agent-overview) (GoogleSQL-dialect databases)
  * [Firestore with MongoDB compatibility: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/data-agent-overview)



## Key capabilities

QueryData provides the following capabilities for agentic database applications:

  * High accuracy: reach near-100% accuracy on business-critical queries by combining database schema metadata with context sets that you curate.
  * Business relevance: ground SQL generation in your organization's domain terminology, metric definitions, and business logic rather than relying only on raw table and column names.
  * Explainability: generate human-readable intent explanations alongside the synthesized SQL query and natural language answer so that you and your users can verify how QueryData translated a request.
  * Data security: enforce row-level access control and protect user data against prompt injection by using parameterized secure views in AlloyDB, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL.



## When to use QueryData

QueryData is designed for developers who are building interactive applications and AI agents that need fast, predictable, and accurate access to operational database data. For example, QueryData is ideal for the following use cases:

  * Customer service automation: answer high-volume user inquiries such as "Where is my order?" or "What is my current account balance?"
  * Ecommerce and catalog search assistants: help users filter and explore structured catalogs with multi-criteria questions such as "Show me lightweight laptops with at least 16 GB of RAM and a battery life of over 10 hours."
  * Field operations and internal tools: let employees query live inventory levels, part availability, or service ticket statuses in real time.
  * Multi-agent workflows: expose structured database querying as a tool in agentic frameworks such as [Agent Development Kit (ADK)](https://google.github.io/adk-docs/), [MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox), or [LangChain](https://www.langchain.com/).



## How QueryData works

Generic large language models (LLMs) don't have information about your organization's private data values, cryptic column names, or domain-specific business rules. To bridge the gap between how users ask questions and how your database stores data, QueryData uses the following layered context:

  * Schema ontologies: enriched table and column descriptions in your database catalog or Knowledge Catalog that explain the business meaning of tables, columns, status codes, and join relationships.
  * Context sets: curated collections associated with your database instance that define the following three building blocks: 
    * Query templates: representative natural language questions paired with validated, parameterized SQL statements and intent explanations.
    * Query facets: modular SQL predicates and filter fragments that QueryData dynamically combines with query templates to support faceted search without requiring a separate template for every filter combination.
    * Value searches: exact, fuzzy trigram, or semantic vector search queries that link informal user phrases, synonyms, or misspelled terms to actual values and columns in your database.



When your application calls the [`projects.locations.queryData`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/queryData) method in the Conversational Analytics API, QueryData performs the following steps:

  1. Value resolution: runs value search queries against your database to map entity phrases in the prompt (such as city names, product categories, or codes) to exact database column values.
  2. Intent matching and disambiguation: matches the user's question against the query templates and facets in your context set, as well as against your schema ontology. If a question is ambiguous or missing required parameters, QueryData can return disambiguation questions to clarify the user's intent.
  3. Query synthesis: synthesizes a dialect-specific SQL query by combining the matched template structure, applicable facets, and resolved literal values, or by generating SQL from your schema ontology when no template matches.
  4. Query execution and response: executes the generated SQL against the target database and returns the tabular result set, the generated SQL query, an intent explanation, and an optional natural language summary.



## Strategies for reaching near-100% accurate text-to-SQL

Reaching near-100% accuracy for text-to-SQL is an iterative engineering process known as _hill-climbing_. Instead of trying to anticipate every possible user question up front, you start with baseline schema descriptions, evaluate your agent against a representative benchmark of golden SQL queries using [EvalBench](https://github.com/GoogleCloudPlatform/evalbench), and then resolve accuracy gaps.

For more information about recommended strategies (or _recipes_) for resolving accuracy gaps, including architecture diagrams, SQL examples, and evaluation benchmarks, see [Six recipes for reaching near-100% accurate text-to-SQL](https://cloud.google.com/resources/content/six-recipes-text2sql-whitepaper?e=48754805) and try the [companion codelab to learn how to implement these text-to-SQL accuracy recipes](https://codelabs.developers.google.com/alloydb-ai-nla).

In summary, the six recipes are as follows:

  * Recipe 0: initialize a context set and connect your application. Start with descriptive table and column comments in your schema, and connect your application to QueryData by using the Conversational Analytics API client libraries or the [`cloud-gemini-data-analytics-query` tool in MCP Toolbox for Databases](https://mcp-toolbox.dev/integrations/cloudgda/tools/cloud-gda-query/).
  * Recipe 1: inject interpretation with query templates. Provide validated example SQL queries for your most important business questions, and generalize them into parameterized SQL templates, parameterized intent explanations, and manifests that capture semantically equivalent question variants.
  * Recipe 2: use faceted templates. Pair base query templates with modular query facets (reusable SQL conditions with their own manifests and intents) so that QueryData can dynamically compose multi-filter queries without requiring a separate template for each combination of conditions.
  * Recipe 3: disambiguate with value search. Define value search queries to link value phrases in natural language questions—including private terminology, synonyms, and misspellings—to actual database columns and values, and let QueryData prompt for clarification when a term matches multiple entity types.
  * Recipe 4: integrate semantic search and AI operators. Combine structured SQL templates and facets with vector search and in-database AI operators (such as `AI.IF` and `AI.RANK` in AlloyDB) to filter and rank unstructured text or multimodal data using semantic criteria.
  * Recipe 5: use parameterized secure views. Enforce strict row-level security and protect user data against prompt injection by binding authenticated user parameters in parameterized secure views for AlloyDB, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL.



You can apply these recipes manually or automate the hill-climbing workflow—expanding evaluation sets, running EvalBench evaluations, analyzing accuracy gaps, and proposing new templates, facets, and value searches—by using the open source [context engineering agent](https://github.com/GoogleCloudPlatform/db-context-enrichment).

## What's next

  * Read the [Six recipes for reaching near-100% accurate text-to-SQL white paper](https://services.google.com/fh/files/misc/six_recipes_text2sql_whitepaper.pdf).
  * Explore the QueryData documentation for your database: 
    * [AlloyDB: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/alloydb/data-agent-overview)
    * [Cloud SQL for MySQL: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/data-agent-overview)
    * [Cloud SQL for PostgreSQL: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-postgres/data-agent-overview)
    * [Spanner: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/spanner/data-agent-overview) (GoogleSQL-dialect databases)
    * [Firestore with MongoDB compatibility: QueryData overview](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/data-agent-overview)
  * Learn how to [define data agent context for database data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases) in the Conversational Analytics API.
  * View the [`projects.locations.queryData` REST API reference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/queryData).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
