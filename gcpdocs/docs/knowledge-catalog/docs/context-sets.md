---
url: https://docs.cloud.google.com/knowledge-catalog/docs/context-sets/
title: Context sets overview \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:45:42.920065+00:00
---

# Context sets overview  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/context-sets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Context sets overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knowledge Catalog context sets let you package data schemas, semantic definitions, and validated query patterns into bounded, domain-specific knowledge containers. You can use these containers to ground autonomous AI applications, such as Gemini Enterprise and custom agents, in verified domain knowledge.

This document is for data architects, governance leads, and AI engineers who want to understand how context sets structure domain knowledge for AI agents. To create and populate a context set right away, see [Manage context sets](https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets).

## What is a context set?

A _context set_ is a specialized Knowledge Catalog **entry group** (`type="context-set"`), which is a logical container for metadata entries and knowledge documents. Each context set packages a self-contained collection of semantic information and data asset references for specific analytical domains and AI agents.

Inside this container, knowledge is organized into **entries** , which represent individual business concepts, data assets, or documents such as guidelines, how-tos, and reference material. These entries are enriched with **aspects** , which are modular metadata attributes that store specific details like business terms, SQL templates, and Markdown documentation.

The following diagram shows how AI agents query a context set, including its root index, domain entries, aspects, and referenced data assets:

![AI agents querying a context set containing a root index, domain entries with aspects, and data asset links.](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/context-sets-architecture.svg)![AI agents querying a context set containing a root index, domain entries with aspects, and data asset links.](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/context-sets-architecture.svg)**Figure 1.** Context set architecture showing the root index, domain entries, aspects, and external data asset references (click to enlarge). 

Rather than forcing agents to search an entire enterprise catalog, which introduces latency, wastes prompt tokens, and risks hallucinated answers, context sets establish hermetic, domain-scoped knowledge containers that agents can consult with high precision.

Because context sets act as administrative containers, you can organize metadata by project ownership and apply Identity and Access Management (IAM) access control policies across all bundled entries at once without configuring permissions individually. For more information about entry groups, entries, and aspects, see [About metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).

## AI agent grounding requirements

As organizations deploy autonomous AI agents (such as Gemini Enterprise, Antigravity, and custom Agent Development Kit agents) to orchestrate data workflows and generate analytics, agents require reliable grounding:

  * **Semantic definitions** : What does a specific column or metric mean in business terms?
  * **Validated query patterns** : How have domain experts successfully queried and joined these tables?
  * **Operational rules** : What business policies, exception criteria, and standard operating procedures (SOPs) govern this data?



## How to populate a context set

You can populate entries in a context set by running an autonomous enrichment task that analyzes your schemas, query logs, and knowledge signals. For more information, see [Create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks).

Because a context set is a specialized entry group (`type="context-set"`), you can also create and update its entries programmatically using the Google Cloud CLI, client libraries, or the Dataplex API. For more information, see [Manage entries and ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources).

## Context set entry types and structure

Entries in a context set use the **Document** (`projects/dataplex-types/locations/global/entryTypes/document`) or **Query Template** (`projects/dataplex-types/locations/global/entryTypes/query-template`) system entry types, hierarchical entry IDs, and metadata aspects based on the knowledge they store. The following sections describe the entry structure and the core entry categories that ground AI agents.

### Automated enrichment agent entry structure

When an enrichment task populates a context set, the enrichment agent creates its generated entries using the **Document** system entry type (`projects/dataplex-types/locations/global/entryTypes/document`) with required `document` and `overview` aspects. The agent organizes these generated entries into a progressive-disclosure hierarchy using slash-separated (`/`) entry IDs and distinguishes each entry's role using the `document.type` field:

Entry category | Entry ID pattern | Generation source and attached metadata  
---|---|---  
**Context set root index** | `agents` _(fixed system ID)_ | 

  * **`document.type` value**: `context-set`
  * **Source** : Auto-generated on every enrichment run.
  * **Required aspects** : `document`, `overview`
  * **Role** : Provides a high-level orientation and entry point for AI agents reading the context set.

  
**Directory index** | 

  * `assets` _(fixed system ID)_
  * `assets/bigquery/PROJECT_ID/DATASET_ID` _(derived from data assets)_
  * `documents` _(fixed system ID)_
  * `documents/SUBFOLDER` _(agent-generated slug)_

| 

  * **`document.type` value**: `knowledge-base-index`
  * **Source** : Auto-generated on every enrichment run. Top-level tiers (`assets`, `documents`) are created unconditionally; sub-indexes are created when child entries exist.
  * **Required aspects** : `document`, `overview`
  * **Role** : Navigation index entries that list the tables or documents inside each folder tier.

  
**Data assets** | 

  * `assets/bigquery/PROJECT_ID/DATASET_ID/TABLE_ID`
  * `assets/biglake/PROJECT_ID/CATALOG_ID/NAMESPACE_ID/TABLE_ID`

 _(IDs derived from data assets)_ | 

  * **`document.type` value**: `table-context`
  * **Source** : Auto-generated from human-supplied **data assets** (BigQuery or Lakehouse tables) configured in the enrichment task.
  * **Required aspects** : `document`, `overview`
  * **Optional aspects** : `queries`, `schema`
  * **Entry links** : Links to the underlying `@bigquery` or `@biglake` table entry using a directed `reference` entry link (`projects/dataplex-types/locations/global/entryLinkTypes/reference`).

  
**Business concept** | `documents/concepts/CONCEPT_ID`  
 _(agent-generated slug)_ | 

  * **`document.type` value**: `concept`
  * **Source** : Auto-generated when human-supplied **knowledge signals** (such as documents or glossaries) are attached to the enrichment task.
  * **Required aspects** : `document`, `overview`
  * **Role** : Defines domain-specific business terminology and KPI formulas.

  
**Agent self-learning** | `documents/learnings/LEARNING_SLUG`  
 _(agent-generated slug)_ | 

  * **`document.type` value**: `learning`
  * **Source** : Auto-generated when human-supplied **self-learning sources** (such as Gemini Enterprise chat logs or BigQuery agent analytics) are attached to the enrichment task.
  * **Required aspects** : `document`, `overview`
  * **Role** : Captures tacit rules and disambiguations extracted from downstream agent conversation traces.

  
**Domain documentation** | 

  * `documents/SUBFOLDER/DOCUMENT_SLUG`
  * `documents/DOCUMENT_SLUG`

 _(agent-generated slugs)_ | 

  * **`document.type` value**: `knowledge-base`
  * **Source** : Auto-generated when human-supplied **knowledge signals** are attached to the enrichment task.
  * **Required aspects** : `document`, `overview`
  * **Role** : Stores general domain guides, policies, and reference documentation.

  
  
The following diagram illustrates how an enriched context set (`thelook-context`) organizes its entries under the `agents` root index (`context-set`). Navigation directory tiers (`knowledge-base-index`) group table context entries (`table-context` with attached SQL query counts) under `assets/bigquery/cymbal-style/thelook/*` and group domain guides (`knowledge-base`) and business terms (`concept`) under `documents/*`:

![Hierarchical tree of the thelook-context entry group showing the agents root index, assets directory hierarchy with table-context entries, and documents directory hierarchy with knowledge-base and concept entries.](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/context-set-entry-hierarchy.svg)![Hierarchical tree of the thelook-context entry group showing the agents root index, assets directory hierarchy with table-context entries, and documents directory hierarchy with knowledge-base and concept entries.](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/context-set-entry-hierarchy.svg)**Figure 2.** Example entry hierarchy inside an enriched context set (click to enlarge). 

In addition to the **Document** entries generated by an enrichment task, a context set can contain standalone **Query Template** (`projects/dataplex-types/locations/global/entryTypes/query-template`) entries created programmatically through the Google Cloud CLI, client libraries, or the Dataplex API. When an enrichment task runs on a context set that contains certified **Query Template** entries, the enrichment agent preserves those entries without modifying or deleting them. For more information, see the Query templates section of this document.

### Data assets

A data asset entry (`document.type: "table-context"` at `assets/bigquery/PROJECT_ID/DATASET_ID/TABLE_ID`) captures domain-specific instructions, column caveats, join hints, and verified SQL examples for a specific table without overwriting the physical table's description in BigQuery. Each data asset entry links to its target catalog asset through a directed `reference` entry link (`projects/dataplex-types/locations/global/entryLinkTypes/reference`).

**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/assets/bigquery/cymbal-style/store/orders
    entryType: projects/dataplex-types/locations/global/entryTypes/document
    aspects:
      dataplex-types.global.document:
        type: "table-context"
      dataplex-types.global.overview:
        content: "## Orders table context\nJoin `store.orders` to `store.returns` on `order_id` when calculating net sales..."
    

### Business concepts

A business concept entry (`document.type: "concept"` at `documents/concepts/CONCEPT_ID`) defines standardized business terminology, domain metrics, acronyms, and calculation formulas.

Key capabilities include the following:

  * **Terminology alignment** : Eliminates terminology ambiguity across business units and analytical teams.
  * **KPI formulas** : Provides mathematical formulas and logic for domain-specific key performance indicators (KPIs).
  * **Targeted asset linking** : Links to relevant tables using `reference` entry links so agents know where the concept applies.



For example, within an ecommerce context set, an entry at `documents/concepts/net-items-sold` specifies the exact net units sold calculation. When an agent receives a prompt asking for "net items sold," it consults the concept entry to apply the verified calculation rather than inventing SQL logic.

**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/documents/concepts/net-items-sold
    entryType: projects/dataplex-types/locations/global/entryTypes/document
    aspects:
      dataplex-types.global.document:
        type: "concept"
      dataplex-types.global.overview:
        content: "Calculates the absolute number of items sold minus customer returns in a given time period."
    

### Documents and self-learning rules

A document entry (`document.type: "knowledge-base"` or `"learning"` under `documents/*`) stores narrative and procedural context in structured Markdown (`document` and `overview` aspects).

Key capabilities include the following:

  * **Standard operating procedures (SOPs)** : Captures SOPs, runbook checklists, and onboarding guides directly within the catalog.
  * **Compliance policies** : Documents compliance policies, regulatory constraints (such as GDPR or HIPAA handling rules), and exception criteria.
  * **Agent self-learning** : Captures tacit rules and disambiguations (`documents/learnings/LEARNING_SLUG`) extracted from downstream agent conversation traces.



For example, an apparel context set includes `documents/policies/return-policy-rules` to instruct agents on how to exclude finalized sales and damaged-in-transit items when calculating standard return rates.

**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/documents/policies/return-policy-rules
    entryType: projects/dataplex-types/locations/global/entryTypes/document
    aspects:
      dataplex-types.global.document:
        type: "knowledge-base"
      dataplex-types.global.overview:
        content: "## Return Policy Rules\nItems marked FINAL_SALE or DAMAGED_IN_TRANSIT are excluded from return rates..."
    

### Query templates

You can also attach `queries` aspects to data asset entries or programmatically create dedicated **Query Template** (`projects/dataplex-types/locations/global/entryTypes/query-template`) entries in a context set to store verified, parameterized SQL queries mapped to natural language questions (`dataplex-types.global.query-template` aspect).

Key capabilities include the following:

  * **Pre-validated queries** : Stores verified join paths, filter conditions, and aggregation patterns mapped to an analytical `intent` and an example natural language question (`nlQuery`).
  * **Runtime parameterization** : Supports typed parameter placeholders (such as `@season` and `@limit`) with descriptions and sample values (`sampleValues`) for dynamic agent execution.
  * **Multi-engine support** : Specifies the target `sourceType` (such as `BIGQUERY`, `SPANNER`, `ALLOYDB`, `CLOUD_SQL`, or `LOOKER`) and optional `sourceDialect` (`GOOGLE_SQL`, `POSTGRESQL`, `MYSQL`, or `LOOKER_QUERY`).



**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/queries/top-categories-by-season
    entryType: projects/dataplex-types/locations/global/entryTypes/query-template
    aspects:
      dataplex-types.global.query-template:
        intent: "Identify top-performing product categories by revenue for a given season."
        nlQuery: "Which ecommerce product categories performed best in winter?"
        query: "SELECT category, SUM(revenue) FROM store.orders WHERE fiscal_season = @season GROUP BY category ORDER BY 2 DESC LIMIT @limit"
        sourceType: "BIGQUERY"
        sourceDialect: "GOOGLE_SQL"
        parameters:
          - name: "season"
            type: "STRING"
            sampleValues:
              - "WINTER"
          - name: "limit"
            type: "NUMBER"
            sampleValues:
              - "5"
    

## Example: Online clothing store context set

To show how entries in a context set work together, consider an online clothing retailer deploying an AI assistant for store merchandisers. Without bounded context, the agent might query raw staging tables or miscount popular items by not subtracting customer returns.

To ground the agent, a data steward creates and enriches a context set named `online-apparel-store`:
    
    
    EntryGroup: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store
    (EntryGroup.type = "context-set")
    │
    ├── agents (document.type = "context-set")
    │     Root directory index for AI agents consulting the context set
    │
    ├── assets/bigquery/cymbal-style/store/* (document.type = "table-context")
    │   ├── assets/bigquery/cymbal-style/store/orders
    │   │     Linked using entryLinkTypes/reference -> @bigquery .../tables/orders
    │   ├── assets/bigquery/cymbal-style/store/products
    │   │     Linked using entryLinkTypes/reference -> @bigquery .../tables/products
    │   └── assets/bigquery/cymbal-style/store/returns
    │         Linked using entryLinkTypes/reference -> @bigquery .../tables/returns
    │
    ├── documents/concepts/* (document.type = "concept")
    │   ├── documents/concepts/net-items-sold
    │   │     Formula: SUM(orders.quantity) - SUM(returns.quantity)
    │   └── documents/concepts/bestseller
    │         Definition: Any clothing item with >= 500 net units sold within a 30-day window
    │
    ├── documents/policies/* (document.type = "knowledge-base")
    │   └── documents/policies/return-policy-rules
    │         Markdown SOP: Exclude items marked 'FINAL_SALE' or 'DAMAGED_IN_TRANSIT' from standard return rates
    │
    └── documents/learnings/* (document.type = "learning")
        └── documents/learnings/winter-season-date-filter
              Learned rule: Filter winter season queries using fiscal_season = 'WINTER'
    

**Note:** Each context set document or data asset entry links to the catalog assets it describes using a directed `reference` entry link (`projects/dataplex-types/locations/global/entryLinkTypes/reference`).

### How an agent resolves a prompt

When a merchandiser asks the agent, _"What were our top 5 bestselling winter jacket styles, excluding damaged returns?"_ , the agent resolves the prompt through the context set:

  1. **Root index and concept lookup** : The agent reads the `agents` root index and inspects `documents/concepts/net-items-sold` and `documents/concepts/bestseller` to confirm that returned items must be subtracted from total order quantities.

  2. **SOP and learning enforcement** : The agent reads `documents/policies/return-policy-rules` and `documents/learnings/winter-season-date-filter`, adding the filter conditions `WHERE return_reason != 'DAMAGED_IN_TRANSIT'` and `fiscal_season = 'WINTER'`.

  3. **Table context and join validation** : Using the data asset entries at `assets/bigquery/cymbal-style/store/*` and their `reference` entry links to the underlying `@bigquery` tables, the agent joins `store.orders`, `store.products`, and `store.returns` using verified foreign keys and runs the SQL query.




## Architectural capabilities

Context sets provide several core capabilities for enterprise data environments:

  * **Hermetic execution boundaries** : By bounding context to a curated set of assets and semantic entries, agents operate within a hermetic sandbox. This boundary eliminates extraneous catalog noise, helps ensure deterministic evaluations, and minimizes token usage.

  * **Fast upload and bulk indexing** : Teams can upload and index sets of concepts, queries, and documents as a single atomic operation, which lets you integrate with continuous integration and deployment (CI/CD) pipelines.

  * **Zero-copy packaging** : Context sets package metadata and relationships without copying or moving underlying data storage, avoiding redundant storage costs and data synchronization lag.




## Agent consultation patterns

Downstream agents consume context sets through the Model Context Protocol (MCP) or direct Knowledge Catalog APIs. For more information, see [Retrieve context for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context).

To optimize response latency and minimize token consumption, agents follow a progressive-disclosure consultation hierarchy:

  1. **Root index and query matching** : The agent inspects the `agents` root index and any `queries` aspects attached to data asset entries. If a verified SQL example matches the user's intent, the agent adapts the query and runs it directly. This match provides a fast response with minimal risk of query error.

  2. **Table context and schema assembly** : If no exact query example matches, the agent reads the data asset entries (`assets/*`) and their `schema` aspects to understand entity relationships and construct a multi-table SQL statement.

  3. **Document and concept consultation** : For ambiguous edge cases (such as fiscal calendar cutoffs or dispute exclusions), the agent reads concept (`documents/concepts/*`), learning (`documents/learnings/*`), and knowledge base (`documents/*`) entries to apply business rules. If a definition in a context set entry conflicts with a definition in a business glossary term, consuming agents prioritize the context set definition.




## Consuming context in generative AI applications

Generative AI applications use curated context sets to understand enterprise domain semantics, navigate complex schemas, and generate reliable SQL without hallucinations. Applications typically consume these context sets through two primary patterns:

  * **Dynamic context discovery** : In conversational or self-service analytics environments, users ask ad hoc questions in natural language. The application dynamically evaluates the user's intent to identify and retrieve the most relevant context set from Knowledge Catalog, injecting the retrieved domain knowledge into the active prompt.

To ground a Gemini Enterprise application in Knowledge Catalog context, configure the **BigQuery** data connector in federated query mode in your Gemini Enterprise application and verify that the **Enable Knowledge Catalog** toggle is turned on in your Gemini Enterprise assistant settings. For more information, see [Connect to BigQuery](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery) and [Connect to Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog).

If users have access to multiple Google Cloud projects with similar tables, specify the target project ID and dataset name in a custom skill or in the Gemini Enterprise **Additional LLM system instructions** field to scope queries to the intended dataset. For more information, see [Configure the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant).

  * **Pre-configured context sets** : For dedicated agent applications, you can pre-configure the agent with an explicit context set reference by specifying its entry group resource name (`projects/PROJECT_ID/locations/LOCATION/entryGroups/CONTEXT_SET_ID`) in the agent's system instructions or tool configuration. The agent can then read the `entries/agents` root index and retrieve entries directly from that context set using `ListEntries`, `LookupEntry`, or `lookupContext` without broad catalog search overhead. The agent automatically inherits quality improvements as recurring enrichment workflows refine the context set over time.

To optimize these enrichment and self-learning capabilities, we recommend specifying a Gemini 3.8 Flash or later model in the Gemini Enterprise application. For more information about the model selection steps, see the "Create an agent using the flow builder" section in [Design agents in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/design-agents).




## How context sets compare to related constructs

To choose the right metadata construct for your architecture, compare Knowledge Catalog context sets with related platform capabilities:

Construct | Primary purpose | Scope and structure | Packaged contents | When to use  
---|---|---|---|---  
**Knowledge Catalog context set** | Grounds analytical AI agents in a hermetic domain sandbox. | Bounded entry group (`type="context-set"`) scoped to a business domain. | Data asset entries (with schema and SQL query aspects), business concepts, Markdown SOPs, and self-learning rules. | Use when building or grounding analytical AI agents (such as Gemini Enterprise or ADK agents) over BigQuery and lakehouse assets.  
**Context graph** | Visualizes and traverses the live semantic topology across your organization. | Open, interactive graph spanning all cataloged entries and entry links. | Physical data assets, business glossaries, data products, context sets, and lineage edges. | Use when interactively discovering assets and tracing multi-hop relationships in **New chat**.  
**Database context set (QueryData)** | Optimizes natural-language-to-SQL (NL2SQL) translation for operational databases. | Entry group (`type="context-set"`) tailored for transactional database schemas. | Golden SQL query templates, schema metadata, and filtering facets for AlloyDB for PostgreSQL, Cloud SQL, and Spanner. | Use when grounding conversational SQL experiences directly on operational, transactional databases.  
**Data product** | Shares and governs physical data assets across organizational teams. | Governed asset bundle with data contracts, SLAs, and data-plane access control. | Concrete BigQuery tables, views, Cloud Storage buckets, and streams. | Use when packaging and granting data-plane access to curated datasets for cross-team consumers.  
  
### Context sets compared to context graphs

The context graph and context sets are two separate constructs with distinct roles in the Knowledge Studio architecture:

  * **Context graph** : The live, comprehensive semantic topology across your organization. It links underlying data assets, business glossary terms, and interaction traces. You explore and traverse this open graph interactively in Knowledge Studio. For more information, see [Explore data assets in Knowledge Studio](https://docs.cloud.google.com/knowledge-catalog/docs/explore-data-assets).

  * **Context set** : A bounded, curated packaging unit. It extracts and hermetically packages a specific subset of domain knowledge into an entry group (`type="context-set"`) for downstream AI agents to query through the Model Context Protocol (MCP). A context set acts as a cohesive, high-density sub-graph within the broader context graph. For more information, see [About MCP servers in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview).




### Knowledge Catalog context sets compared to database context sets

Both Knowledge Catalog and Google Cloud operational databases use the term _context set_ to refer to curated information that grounds generative AI models.

Although both variations share the same underlying architecture—they are stored natively as Knowledge Catalog context sets (extensible entry groups with `type="context-set"`) and use standard Knowledge Catalog APIs—they target different layers of the enterprise data stack:

  * **Database context sets (QueryData)** : Built to serve operational, transactional databases (such as AlloyDB for PostgreSQL, Cloud SQL, and Spanner). These context sets are heavily optimized for SQL configurations. They bundle golden query templates, schema metadata, and filtering facets that a dedicated context engineering agent evaluates to improve natural language-to-SQL (NL2SQL) translation in operational runtimes.
  * **Knowledge Catalog context sets (Knowledge Studio)** : Built to serve analytical data estates (such as BigQuery, data lakehouses, and Knowledge Catalog data products). These context sets package broader, multi-modal knowledge across multiple entry categories, including data asset entries, business concepts, Markdown documentation wikis, and self-learning rules. They are curated using Knowledge Studio enrichment workflows and served to downstream analytical agents through the Model Context Protocol (MCP).



### Context sets compared to data products

Understanding how context sets interact with Knowledge Catalog data products helps you establish clear data and AI governance boundaries. For more information, see [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).

  * **Data products manage the underlying resources:** Data products securely bundle concrete resources like BigQuery tables, buckets, and streams, establishing a primary unit for data sharing, data contracts, and data-plane access control.

  * **Context sets bundle conversational semantics:** Context sets don't grant data access; instead, they bundle domain knowledge such as concepts, query templates, and documents required by AI agents and humans to understand the data. Data stewards can link a context set to a data product by declaring it in the product's `additional_context` references.




## Enterprise security and governance

Context sets integrate with Google Cloud security and governance controls to help protect sensitive enterprise metadata:

  * **Context set IAM roles** : Because context sets often contain sensitive semantic information, access is governed by dedicated IAM roles applied to the project or directly to the `context-set` entry group. This control lets you organize curated knowledge by geographic region and domain ownership. For more information, see the Required roles section in [Manage context sets](https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets#required-roles).

  * **Zero-copy underlying data security** : Granting an agent access to a context set lets the agent read semantic metadata and query templates, but it doesn't bypass access controls on underlying tables. To run a SQL query against BigQuery or read files in Cloud Storage, the identity running the query must hold the required data-plane IAM permissions on those underlying resources.

  * **Human-in-the-loop governance** : When autonomous Knowledge Studio enrichment tasks extract new concepts, SOPs, or query templates from operational logs, the proposals are staged as reviewable change requests. Data stewards inspect diff comparisons and evaluation scores before approving changes to a production context set. For more information about proposal review, see [Evaluate and approve enrichment proposals](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs).

  * **User-managed execution identity** : Automated enrichment tasks that populate context sets run under a user-managed service account impersonated by the Dataplex Service Agent through the **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) role.




## Preview scope and boundaries

During Preview, context sets operate within the following boundaries:

  * **Regional scope** : Single-region context sets (such as `us-central1`) must align with the region of the assets they package. Multi-region (such as `us` or `eu`) and `global` context sets can reference assets across compatible regions; when you configure an enrichment task for a multi-region or `global` context set, you select a single execution region for the task.

  * **One enrichment task per context set** : Each context set can be enriched by only one enrichment task.

  * **Cross-context-set references** : Referencing a subset of entries from one context set inside another context set isn't supported.

  * **Authoring and consumption interfaces** : You can create and manage context sets through Knowledge Studio in the Google Cloud console or programmatically as entry groups (`type="context-set"`). You populate context sets through Knowledge Studio enrichment workflows or by managing entries programmatically. Downstream AI agents can discover and query context sets programmatically by using the Knowledge Catalog APIs (`ListEntries` and `LookupEntry`) and the Model Context Protocol (MCP). For more information, see [About MCP servers in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview).

  * **Shared quotas** : Because context sets are fundamentally specialized entry groups (`type="context-set"`), they consume and share the same resource quotas as standard Knowledge Catalog entry groups. For more information, see [Quotas and limits](https://docs.cloud.google.com/knowledge-catalog/docs/quotas).




## Pricing

Context sets are stored as standard Knowledge Catalog entry groups and custom entries and aspects. An empty context set entry group or an unapproved enrichment batch change request incurs no metadata storage charge. When entries are created in a context set (for example, when you approve an enrichment change request or create entries directly), standard Knowledge Catalog metadata storage charges apply to the project hosting the entry group.

During Preview, running enrichment tasks and staging unapproved batch change requests are offered at no charge. Standard usage charges, including BigQuery query processing and Cloud Storage staging reads and writes, apply in your project when an enrichment task uses optional customer-managed resources, such as Cloud Storage buckets for knowledge signals or evaluation sets and BigQuery agent analytics trace tables for self-learning.

## What's next

Concept 

###  [ Knowledge Studio overview ](https://docs.cloud.google.com/knowledge-catalog/docs/knowledge-studio)

Learn how to orchestrate rich data context, build context sets, and ground AI agents using Knowledge Studio interfaces. 

Task 

###  [ Explore data assets in Knowledge Studio ](https://docs.cloud.google.com/knowledge-catalog/docs/explore-data-assets)

Use the visual canvas in Knowledge Studio to chat with your data and trace semantic relationships. 

Concept 

###  [ About metadata in Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)

Understand how entries, entry groups, and aspects form the structural foundation of context sets. 

Concept 

###  [ About MCP servers in Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview)

Expose context sets and rich metadata to downstream generative AI agents using MCP. 

Task 

###  [ Retrieve context for data assets ](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context)

Programmatically discover and retrieve context sets for generative AI reasoning using the `ListEntries` and `LookupEntry` APIs. 

Task 

###  [ Manage context sets ](https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets)

Learn how to create, view, edit, and delete context sets in the to organize domain knowledge. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
