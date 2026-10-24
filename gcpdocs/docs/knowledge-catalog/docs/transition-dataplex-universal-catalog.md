---
url: https://docs.cloud.google.com/knowledge-catalog/docs/transition-dataplex-universal-catalog/
title: Transition from Dataplex Universal Catalog to Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T08:50:32.265707+00:00
---

# Transition from Dataplex Universal Catalog to Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/transition-dataplex-universal-catalog/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Transition from Dataplex Universal Catalog to Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you unify enterprise data governance with generative AI capabilities using an active, AI-powered context graph. You can use this semantic context engine to ground AI agents and support autonomous actions across your databases, data warehouses, and AI tools. For more information, see [Agentic Data Cloud](https://cloud.google.com/data-cloud).

Your existing Dataplex Universal Catalog configurations, APIs, and deployments remain operational without manual migration, data movement, or downtime. You can continue to use core features such as data discovery, data lineage, data quality scans, and business glossaries. Your existing metadata and aspects transition automatically to Knowledge Catalog.

## API, CLI, and IAM compatibility

Although the product name changed to Knowledge Catalog, existing API endpoints, client libraries, Google Cloud CLI commands, and Identity and Access Management (IAM) roles and permissions still retain `dataplex` in their names and identifiers:

  * **REST API** : REST endpoints continue to use the `dataplex.googleapis.com` service endpoint (for example, `https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups`). For more information, see [Cloud Dataplex API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest).
  * **RPC API** : RPC services and protobuf packages continue to use the `dataplex.googleapis.com` service name and the `google.cloud.dataplex.v1` package (for example, `google.cloud.dataplex.v1.CatalogService`). For more information, see [Cloud Dataplex API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc).
  * **Client libraries** : Client library package names and namespaces still use `dataplex` (for example, `google-cloud-dataplex` for Python and `cloud.google.com/go/dataplex` for Go). For more information, see [Knowledge Catalog and Data Lineage client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries).
  * **Google Cloud CLI commands** : You continue to manage resources using `gcloud dataplex` commands (for example, `gcloud dataplex entries search` or `gcloud dataplex glossaries list`). For more information, see [`gcloud dataplex`](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex).
  * **IAM roles and permissions** : Predefined IAM roles and permissions continue to use the `dataplex` prefix, such as **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`), **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`), **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`), and permissions such as `dataplex.entries.get` and `dataplex.entryGroups.create`. For more information, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles) and [Knowledge Catalog IAM permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions).



## Key differences with conventional data catalogs

Because organizations accelerate generative AI adoption, AI agents require deep business context to prevent failures and errors. Knowledge Catalog bridges the gap between enterprise data governance and AI agent workflows. It provides the contextual framework that agents need to retrieve accurate, grounded responses.

Unlike conventional passive catalogs, Knowledge Catalog automatically curates metadata, business relationships, and operational rules into a unified context graph. It introduces active, AI-centric features, including verified example queries, and Model Context Protocol (MCP) integrations.

## What's next

Overview 

###  [ Knowledge Catalog overview ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)

Learn about the core capabilities and architecture of Knowledge Catalog. 

Concept 

###  [ About data context ](https://docs.cloud.google.com/knowledge-catalog/docs/about-context)

Discover how active data context powers generative AI grounding and eliminates hallucinations. 

Tutorial 

###  [ Establish foundational context ](https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context)

Get hands-on by creating business glossaries and custom aspect types in your project. 

Reference 

###  [ API and CLI reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest)

Explore REST and RPC APIs, client libraries, and gcloud CLI commands for automation. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-24 UTC."],[],[]] 
