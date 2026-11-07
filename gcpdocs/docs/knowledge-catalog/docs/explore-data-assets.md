---
url: https://docs.cloud.google.com/knowledge-catalog/docs/explore-data-assets/
title: Explore data assets in Knowledge Studio \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:45:18.763073+00:00
---

# Explore data assets in Knowledge Studio  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/explore-data-assets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Explore data assets in Knowledge Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knowledge Studio lets you discover data assets, query enterprise metadata in natural language, and visually explore asset relationships. You can use the conversational chat interface alongside an interactive context graph to navigate connections across your datasets, tables, and business terms.

This document is for data analysts, business analysts, and data stewards who want to explore catalog metadata and asset dependencies.

## How data exploration works

The **New chat** interface provides the following capabilities for interactive data discovery:

  * **Natural language interface** : Ask questions in English about your data estate (for example, "Which tables contain European customer churn metrics?").

  * **Chat powered by Gemini** : Powered by Gemini, the agent parses your natural language questions, runs search and metadata lookup tools against Knowledge Catalog, formulates multi-step exploration plans, and displays its progress in collapsible thought traces.

  * **Context graph visualizer** : Interactively navigate the relationships between datasets, tables, queries, and business terms. The visual graph displays the active nodes and entry links that constitute the working _context set_ for your exploration session. Click nodes to inspect detailed column schemas, review active node drawer listings, or filter the graph by asset type.

  * **BigQuery code assist execution** : Validate data relationships by running generated SQL queries directly against your data warehouse from within the exploration interface.




The context graph visualizes semantic business relationships, glossary definitions, and verified join paths. It isn't an operational ETL pipeline execution viewer. To inspect pipeline transformation steps, runtime jobs, or operational data flows (such as Dataflow pipelines), view Knowledge Catalog data lineage. For more information, see [Use data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Verify that your data assets exist. Knowledge Catalog automatically ingests structural and operational metadata from core Google Cloud services without requiring manual configuration. For organizations with bespoke knowledge bases, third-party governance tools, or on-premises systems, Knowledge Catalog provides flexible ingestion mechanisms: 
     * [Ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources)
     * [Metadata management overview](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)
  9. Optional: Verify that business glossaries and terms (such as business KPI definitions) are configured in Knowledge Catalog and linked to your underlying data assets. For more information, see [Manage a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  10. Enable the required APIs: 

**Required for core exploration:**

     * Dataplex API (`dataplex.googleapis.com`): Required for opening Knowledge Studio, searching the catalog, and exploring the context graph and glossaries.

**Required per feature (enabled on your project):**

     * BigQuery API (`bigquery.googleapis.com`): For browsing BigQuery datasets and tables, inspecting query jobs, and running SQL queries.
     * Data Lineage API (`datalineage.googleapis.com`): For browsing upstream and downstream data lineage and inspecting lineage processes.
     * Gemini Data Analytics API (`geminidataanalytics.googleapis.com`): For using BigQuery conversational analytics and generating data distribution insights.
     * Google Documents API (`docs.googleapis.com`): For reading Google Documents linked in chat prompts.



### Required roles

To get the permissions that you need to explore data assets and the context graph in Knowledge Studio, ask your administrator to grant you the following IAM roles on your project: 

  * Core catalog search and context graph exploration: 
    * [**Dataplex Catalog Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)
    * [**Dataplex Content User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.contentUser) (`roles/dataplex.contentUser`)
    * [**Service Usage Consumer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * Browsing BigQuery metadata and running SQL queries: 
    * [**BigQuery Metadata Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.metadataViewer) (`roles/bigquery.metadataViewer`)
    * [**BigQuery Data Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)
    * [**BigQuery Job User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * Using BigQuery conversational analytics: 
    * [**Gemini for Google Cloud Data Agent Stateless User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentStatelessUser) (`roles/geminidataanalytics.dataAgentStatelessUser`)
    * [**BigQuery Data Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)
    * [**BigQuery Job User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
  * Browsing data lineage: 
    * [**Data Lineage Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)
    * [**BigQuery Resource Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.resourceViewer) (`roles/bigquery.resourceViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:**

  * The **Dataplex Viewer** (`roles/dataplex.viewer`) role doesn't grant catalog read and search permissions. Ensure that you're granted **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`) and **Dataplex Content User** (`roles/dataplex.contentUser`).
  * To inspect SQL queries from lineage processes created by BigQuery jobs run by other users, you need the optional **BigQuery Resource Viewer** (`roles/bigquery.resourceViewer`) role.
  * To allow the agent to read Google Documents linked in chat, you must have Google Drive Viewer access to the referenced Google Doc.



## Open the exploration interface

In the Google Cloud console, go to **Knowledge Studio (Preview)**.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

The interface displays the following interface elements:

  * **Sidebar** : Lets you start a new exploration session (**New chat**), search previous chat sessions, or switch between the **New chat** , **Context sets** , and **Enrichments** interfaces.

  * **Conversational chat window** : Features a central prompt field with the thinking level and project scope selectors, starter prompt chips (such as **What data do I have in Knowledge Catalog?**), and up to four **Recently opened** resource cards for supported catalog entry types.

  * **Show graph panel** hub icon: Opens or closes the **Context graph** panel.


**Note:** If you open the graph panel before selecting any data asset, the panel is empty and displays the message: `No graph in this conversation yet.`

## Discover data assets using natural language

  1. To search for data assets, in the **New chat** interface prompt field, enter a question, or click one of the starter prompt chips (for example, **What data do I have in Knowledge Catalog?**).

Gemini analyzes your request, runs internal discovery tools, and displays structured results in the chat panel.

Depending on your query, the chat response from the agent can include:

     * **Matching assets expanders** : Displays interactive card summaries of the discovered data assets grouped by type (such as tables or glossaries).
     * **Text summaries** : Describes the core datasets, tables, and glossaries found. If a discovered table doesn't have an existing description in Knowledge Catalog, the agent generates a temporary one-line summary from the table name and schema for the chat response only. This summary doesn't require data profiling and isn't saved to the catalog. To generate and persist governed descriptions in the catalog, run an enrichment task. For more information, see [About enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks).
     * **Follow-up guidance** : The agent suggests next steps, such as exploring specific domains or inspecting table schemas.
     * **Add to graph button** : Appears after a completed agent response when the response includes discovered catalog entries. Click **Add to graph** to merge or restore those entries onto the context graph canvas. When all entries from that response are already on the canvas, the button displays **On graph**.
![A chat response showing Matching Assets panels and dataset summaries](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-key-assets.png)![Larger view of the chat response showing Matching Assets panels and dataset summaries](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-key-assets.png)**Figure 1.** The chat response displaying matching assets, dataset summaries, and follow-up guidance. (Click the image to enlarge.)
  2. Optional: To inspect the agent's reasoning steps and internal tool calls, expand the **Thinking** section in the chat response. The **Thinking** section provides a narrative explanation of the agent's multi-stage search strategy, including how it progresses from broad discovery queries to targeted asset filters. The reasoning trace might reference internal tool names or prompt instructions, which represent backend agent orchestration steps rather than standalone user-facing tools or documentation. The following list shows some of the internal operations the agent might perform to answer your requests:

     * **Catalog search** : Queries Knowledge Catalog with precise project constraints, using keyword and semantic matching (for example, filtering by `type=dataset` or `type=context-set`). For more information about the underlying mechanisms, see [Search for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).

     * **Metadata retrieval** : Retrieves schemas, descriptions, and lineage for matched entries. For BigQuery tables, it also fetches linked business glossaries and structurally related tables. For more information about the underlying API, see [Retrieve context for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context).

     * **UI rendering** : Formats the retrieved metadata as interactive cards in the chat panel.




## Configure search scope and reasoning

To help Gemini provide the most accurate answers while minimizing the time you wait for a response, you can configure the agent's target project scope and reasoning complexity within the prompt field using the following controls:

  * **Explore data across** : Controls which Google Cloud projects the agent searches. By default, a new chat scopes searches to your current project (labeled `Current`). Filtering by specific projects speeds up discovery and prevents the agent from returning similarly named tables from test or staging environments.

In the prompt field, click **Explore data across** to change the project scope:

    * **Filter** : Enter text in the **Filter** field to narrow the listed projects.
    * **All projects** (`Every project you can access`): Select this checkbox to search across every project that you can access when you don't know where the data resides. Selecting **All projects** clears any individual project selections.
    * **Project checkboxes** : Select one or more projects from the list of your current, recent, and starred projects. Selecting an individual project clears **All projects** , and clearing all checkboxes reverts the scope to your current project.
    * **Choose another project** : Click to open the Google Cloud console project picker and add another project to the selection list.
    * **Apply** : Click **Apply** (or click outside the menu) to apply your selection.
  * **Thinking level** : Controls how deeply the agent reasons about your prompt, dictating how exhaustively it evaluates query possibilities and iterates on search results before responding to you.

Choose this option when you need to balance response speed against the thoroughness of the search. * Select **Low** for fast, direct, and straightforward keyword lookups where the asset name is known. * Select **Medium** for typical exploration workflows where the agent might need to perform one or two follow-up queries. * Select **High** for complex, vague, or ambiguous questions where the agent must execute a multi-stage search strategy, evaluate the initial results, and refine its queries before returning a final answer.




## Run specialized analytical agents

By default, the chat powered by Gemini limits queries to structural metadata and descriptive catalogs. If your question requires deep data analysis or running queries against actual table data, you can invoke specialized analytical agents by entering their exact mention directly into your chat prompt.

The following list shows the supported analytical agents and their capabilities:

  * **`@BqJobs`** : Invokes the **BigQuery Query Job** agent. When included, this grants the chat powered by Gemini permission to execute SQL statements directly against your tables. Use this mention when you want the agent to answer your question by querying the data rather than just reviewing metadata.

  * **Google Document links** : Pasting a Google Document link into the chat lets the agent read the document's contents and use that external context to answer your questions. For the required API and document access permissions, see the Before you begin section of this document.

  * **`@BqCA`** : Invokes the **BigQuery Conversational Analytics** agent. When included, this transfers your analytical questions (for example, about trends, aggregations, or complex business intelligence workflows) alongside your table context to a highly specialized subagent capable of performing advanced, multi-step SQL reasoning.




For more information about the capabilities, required permissions, and pricing for these subagents, see [Conversational analytics in BigQuery](https://docs.cloud.google.com/bigquery/docs/conversational-analytics).

## Visualize semantic relationships

The context graph acts as an interactive canvas where you can view technical storage resources and their relationships to logical business semantics.

### Explore data connections

To load an initial context graph, click a **Recently opened** card on the welcome screen, click an entry card in **Matching assets** , or click **Add to graph** beneath an agent response. The **Context graph** panel displays an interactive topological graph for that data asset and its connected entities. For more information, see the Discover data assets using natural language section of this document.

For example, Figure 2 shows the `szelwico_curated_supply_chain` dataset container on the context graph canvas, grouping supply chain tables and views:

![A context graph showing the szelwico_curated_supply_chain dataset container with BigQuery tables and views](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-szelwico-graph.png)![Larger view of the szelwico_curated_supply_chain dataset container on the context graph](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-szelwico-graph.png)**Figure 2.** A context graph showing BigQuery tables and views grouped inside the `szelwico_curated_supply_chain` dataset container. (Click the image to enlarge.)

  * **BigQuery tables:** Blue nodes represent operational and analytical tables in the dataset, such as `fact_station_wetstock_reconciliation`.
  * **BigQuery views:** Teal nodes represent analytical views, such as `vw_active_ust_leak_alerts`, along with their structural connections to underlying tables.



For a complete list of node colors, relationship edges, and state badges, see the Graph visual reference section of this document.

Expanding a node reveals how the context graph maps schema joins, business logic, and curated context to data storage. Figure 3 shows the expanded connections for the `fact_station_wetstock_reconciliation` table:

![A context graph showing the fact_station_wetstock_reconciliation table connected by Schema Join, Definition, and Context edges across multiple containers](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-wetstock-connections-graph.png)![Larger view of the expanded connections for fact_station_wetstock_reconciliation](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-wetstock-connections-graph.png)**Figure 3.** Expanded relationships for `fact_station_wetstock_reconciliation` across datasets, business glossary terms, and a context set. (Click the image to enlarge.)

In this fuel supply chain scenario, the `fact_station_wetstock_reconciliation` table tracks fuel inventory and underground storage tank (UST) reconciliation at retail service stations. The expanded graph shows how technical storage, business rules, and curated context work together to explain the underlying data:

  * **Table and view joins (`Schema Join` edges):** Blue `Schema Join` lines indicate verified join paths that let you combine station inventory records with related operational, dimensional, and staging data: 
    * Joining with the `vw_active_ust_leak_alerts` view (in `szelwico_curated_supply_chain`) links daily tank reconciliation metrics to active environmental leak alerts.
    * Joining across datasets with `dim_stations_enriched` (in `szelwico_curated_retail_analytics`) enriches inventory readings with station attributes, such as location and tank configuration, while joining with `stg_ust_thermal_compensated_inventory` (in `szelwico_staging`) traces how raw temperature-adjusted tank readings feed the curated reconciliation table.
  * **Governed business logic (`Definition` edges):** Blue `Definition` lines connect the table's columns to yellow `GLOSSARY TERM` nodes (`Thermal Compensation Flag` and `Confirmed UST Environmental Leak Threshold`) in the business glossary. These links tell you—and the agent—which standardized business rules determine whether a tank reading is temperature-calibrated and when an inventory variance crosses the threshold for a confirmed leak.
  * **Curated context (`Context` edge):** A `Context` line connects the table to the `Station Wet-Stock Reconciliation Fact` (`CONTEXT`) node inside its context set container, providing curated domain guidance and query patterns that ground AI agents when they generate SQL against this table.



### Filter and customize the context graph

As your context graph grows, you can locate specific nodes, filter out surrounding noise, and adjust how relationships and containers are rendered on the canvas. You can also add catalog entries directly from the canvas toolbar. For more information, see the Add entries manually to the context graph section of this document.

  1. To locate a node that is already on the active canvas, enter its name in the toolbar **Search** field and select the matching node from the list (up to 50 matches) to highlight and center it in your view.

  2. To adjust how much of the graph is visible in the viewport, use the canvas viewport controls:

     1. Click **Zoom in** (zoom_in) or **Zoom out** (zoom_out) to scale the graph, or click **Fit to screen** (fit_screen) to center and resize the entire graph layout within your viewport.
     2. Optional: In the canvas header, click **Full screen** (fullscreen) to expand the canvas across your entire screen.
     3. Optional: To reset the canvas, click **Clear graph** (delete_sweep) and confirm **Clear graph** in the dialog. This action removes all nodes from the canvas and clears the agent focus for the current chat. Click **Undo** in the confirmation notification to restore the previous canvas state.
  3. To reduce visual density on a large graph, filter which node types, edges, and hop distances remain visible:

     1. On the canvas, click **Graph controls** (tune) to open the **Filters** panel.
     2. Select one or more filter criteria: 
        * **Types** : Filter nodes by entity type (**All types** , **Tables & views**, **Glossary terms** , **Data products** , or **Context**).
        * **Relationships** : Filter the colored edges connecting nodes by their relationship type (**All relationships** , **Schema join** , **Related** , **Definition** , **Lineage** , **Context** , or **Packages**).
        * **Isolated nodes** : Select **All** to display connected and isolated nodes, **Hide** to hide nodes with no visible connections, or **Only** to display only isolated nodes.
        * **Hop depth** : Click an anchor node on the canvas, and then select a hop distance (**1** , **2** , **3** , or **All**) to hide nodes further away from that anchor.
  4. To toggle how edges, containers, and focus nodes are displayed on the canvas, follow these steps:

     1. In the canvas toolbar, click **More options** (more_vert) to open the **Graph viewing options** menu.
     2. Select the rendering options that you want to turn on or off: 
        * **Focus nodes only** : Hides surrounding connections to highlight only the nodes in your agent focus.
        * **Show edges** : Shows or hides all relationship lines to declutter dense graphs.
        * **Highlight containers** : Emphasizes structural groupings—such as datasets, glossaries, or context sets—that enclose child nodes.
        * **Show explorer** : Shows or hides the node list sidebar explorer.
        * **Open graph legend** : Opens the visual legend explaining node colors, badges, and edge types.



### Expand and manage containers

Containers group entries on the canvas that share a parent resource—such as tables in a BigQuery dataset, terms in a business glossary, or documents and overlays in a context set. Each container is drawn as a shaded hull with a pill handle that names the parent container. To inspect a container's metadata details panel, see the Explore connections for a specific node, container, or edge section of this document.

You can expand, filter, hide, or collapse container members on the canvas in the following ways:

  1. **Expand or select child entries** : Double-click a container pill (or right-click the pill and select **Expand**) to load child entries from the catalog: 
     * **40 or fewer new child entries** : Knowledge Studio adds all child entries to the container on the canvas at once and displays a notification with an **Undo** option.
     * **More than 40 new child entries** : Knowledge Studio opens the **CONTAINER_NAME child entries** popover for the container pill so you can choose which entries to load. Use the **Filter child entries...** field to filter members by name or type, select the checkboxes for the child entries that you want to visualize, and click **Apply selection ( N)** to add them inside the container hull.
  2. **Toggle container member visibility** : Click the eye (visibility) icon on a container pill (**Hide entries** or **Show entries**) to collapse or restore its member nodes in the current view without removing them from your session graph. When hidden, the container pill displays a **+ N** badge (`<var>N</var> hidden entries`) and dynamically reroutes any cross-container relationship edges to the outer container pill so external connections remain visible. Selecting a hidden node from chat, toolbar search, or **\+ Add entries** automatically unhides its parent container.
  3. **Collapse a container** : Right-click an expanded container pill and select **Collapse** to remove all child entries inside that container from the canvas while keeping the container pill on the graph.

![The child entries popover on a context set container pill showing a filter input, document checkboxes, and the Apply selection button](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-child-entries-picker.png)![Larger view of the child entries popover on a context set container pill](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-child-entries-picker.png)**Figure 4.** Selecting child document entries from a context set container pill on the canvas. (Click the image to enlarge.)

### Graph visual reference

Use the following tables to interpret node colors, relationship edges, and node state badges on the context graph canvas.

#### Entry type color coding

The color of a node indicates its semantic entry type group in Knowledge Catalog, regardless of the underlying source system:

Node color | Entry type group | Included asset types  
---|---|---  
**Blue** | Tables and schemas | Tables, datasets, schemas, namespaces, and snapshots  
**Teal** | Views, streams, and code | Views, routines, streams, query templates, repositories, and code assets  
**Dark grey** | Storage and infrastructure | Instances, databases, buckets, folders, filesets, and connections  
**Pink** | AI, models, and context | ML models, agents, feature stores, `Context` entries, and `Document` entries  
**Purple** | Semantic models and graphs | Semantic models, semantic entities, semantic metrics, and property graphs  
**Yellow** | Glossary and catalog | Glossaries, categories, terms, catalogs, entry types, and aspect types  
**Orange and red** | Data products and governance | Data products, domains, exchanges, listings, shares, and data policies  
**Green** | Dashboards and BI | Dashboards, explores, and charts  
**Light grey** | Custom assets | Custom entry groups, custom entry types, and unsupported entry types  
  
#### Relationship edges

The lines connecting nodes represent semantic and structural relationships. To filter which edges appear on the canvas, use the **Filters** panel. For more information, see the Filter and customize the context graph section of this document.

Edge type | Visual style | Meaning  
---|---|---  
**Schema join** | Blue edge | Maps verified multi-table join paths, primary keys, and foreign keys.  
**Related** | Blue edge | Connects structurally or semantically related entries.  
**Definition** | Orange or blue edge | Connects underlying table columns directly to certified business glossary terms and KPI formulas.  
**Lineage** | Directed arrow | Shows data flow from a source to downstream assets built from it.  
**Reference** | Directed edge (`dataplex-types.global.reference`) | Connects context set documents and data asset entries to the cataloged assets they describe.  
**Context** | Grey edge (`dataplex-types.global.context`) | Connects context entries to target data assets.  
**Packages** | Grey edge (`dataplex-types.global.packages`) | Shows which data assets are bundled into a specific data product.  
  
#### Node state badges

Nodes display badges on the canvas to indicate their current interaction state:

Badge | Meaning  
---|---  
**Selected** | The entry that you are inspecting. Surrounding nodes dim so the selected entry's connections stand out.  
**In agent focus** | Part of your active focus—the working set that you and the agent are exploring.  
**Expanding** | Indicates that Knowledge Studio is loading related entries (such as lineage, joins, and glossary terms) and adding them to the graph.  
  
## Add entries manually to the context graph

Instead of relying solely on chat commands, you can manually seed the context graph with specific data assets, data products, glossaries, or context sets directly from the canvas toolbar. Manual entry selection is useful when you already know which resources you want to connect, visualize, and include in your agent focus.

To search for and add specific entries to the graph, perform the following steps:

  1. In the canvas toolbar, click **\+ Add entries**. The **Add entries** panel expands.
  2. Optional: To change the target project scope, click the **Project** filter button and select a Google Cloud project, or click close **Clear project filter** to search across **All projects**.
  3. Optional: Click a category chip to filter entries by type: **All** , **BigQuery Tables** , **BigQuery Datasets** , **BigQuery Views** , **Lakehouse** , **Glossaries** , **Data Products** , or **Context Sets**.
  4. Locate the entries you want to add using one of the following methods: 
     * Browse your **Starred entries** or **Recently opened** entries displayed by default when the panel opens (up to 3 items are previewed per section; click **Show all ( N)** to expand the full list).
     * Enter a keyword, dataset name, or description in the **Search entries by name, dataset, or description** field to view the top 20 matching entries in **Search results**. Entries that are already on the canvas display an `On graph` badge.
  5. Select the checkbox for one or more entries, and then click **Add to graph ( N)**.



Knowledge Studio adds the selected nodes (or container pills) to both the context graph canvas and your active **agent focus** , and automatically maps any existing semantic or structural relationships between them.

![The expanded Add entries panel showing the search bar, project selector, category filter chips, recently opened entries, and the Add to graph button](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-add-entries-ai.png)![Larger view of the expanded Add entries panel in the canvas header](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-add-entries-ai.png)**Figure 5.** The expanded **Add entries** panel with category filter chips, recently opened entries, and the **Add to graph** button. (Click the image to enlarge.)

## Explore connections for a specific node, container, or edge

To view metadata details, manage connected neighbors, expand relationships, or access additional actions for an element on the active canvas, interact directly with the element:

  * **View node or container metadata** : Single-click any node (such as a table, data product, or document) or any container pill (such as a **Context Set** or dataset) to open the metadata details side panel:

    * For a **table or asset node** , the panel displays the asset's **Description** , **Schema** (click a column's foreign key or annotation pill to open a stacked **Foreign keys** or **Annotations** details drawer), **Overview** , **Properties** , **Glossary terms** , **Representative queries** , **Other aspects** , and **Connected nodes**.
    * In the **Connected nodes** section, click any neighbor's name (**Show on graph**) to highlight and center that node on the canvas without closing the current details panel. Select one or more connected nodes to perform bulk actions: 
      * **Hide edges** : Hides the relationship edges between the inspected node and the selected neighbors while keeping all nodes on the canvas.
      * **Hide nodes** : Removes the selected neighbor nodes from the canvas.
      * **Add to focus** : Adds the selected neighbor nodes to your active agent focus.
    * For a **Context Set or container pill** , the panel displays the container's **Description** , **Properties** (`System`, `Platform`, `Entry Type`, `Location`, `Project`, `Source Resource (FQN)`, `Dataplex Resource Name`, and `Labels`), and **Other aspects**.
![A metadata details side panel for a selected Context Set container pill showing its description, properties, and Entry Group Aspect](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-context-set-details.png)![Larger view of the metadata details side panel for a selected Context Set container pill](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-context-set-details.png)**Figure 6.** A Context Set container pill selected on the canvas, showing its child document nodes and metadata properties panel. (Click the image to enlarge.)
  * **View relationship edge details** : Single-click any relationship line connecting two nodes (or right-click an edge and select **View details**) to open the edge details side panel and inspect the relationship's **Properties** and **Other aspects**.

  * **Open context menu actions** : Right-click a node or container pill to open its context menu and select from the following actions:

![A context menu for a selected node on the context graph canvas](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-node-action-bar.png)![Larger view of a context menu for a selected node](https://docs.cloud.google.com/static/knowledge-catalog/docs/images/explore-node-action-bar.png)**Figure 7.** A node's context menu. (Click the image to enlarge.)
    * **Expand** : Fetches and reveals immediate neighbor connections for a node. To expand or collapse child entries for a container pill, see the Expand and manage containers section of this document.
    * **Add to agent focus** or **Remove from agent focus** : Includes or excludes the entry from the working set you and the agent are exploring.
    * **Copy entry ID** : Copies the unique identifier for the asset.
    * **Upstream lineage** : Traces and expands data lineage flowing into the node (supported on BigQuery, Lakehouse, and Looker table nodes when Data Lineage is enabled).
    * **Downstream lineage** : Traces and expands data lineage flowing out of the node (supported on BigQuery, Lakehouse, and Looker table nodes when Data Lineage is enabled).
    * **Remove from graph** : Removes the node or container from the active canvas (with an **Undo** option in the notification banner).
  * **Expand all connections on double-click** : Double-click any node to expand its immediate connections at once (adding connected tables, views, glossary terms, and context entries to the graph). You can click **Undo** in the notification banner (`Added <var>N</var> nodes and <var>M</var> connections`) to revert the expansion, or press `Escape` at any time to close open panels and clear the current canvas selection.




## Query and expand the active context

The chat powered by Gemini maintains conversational context across prompts. Because the active context graph is held in working memory, you can ask follow-up questions, expand the graph outward, or generate queries without repeating earlier details.

### Ask questions about in-context assets

When you ask about assets already on the canvas, the agent inspects the in-memory context graph directly without re-invoking the discovery tools.

To ask a question about an asset on your canvas, follow these steps:

  1. In the prompt field, enter a question about connected business terms or metadata for an asset on your canvas, and then click send **Send**. For example:
         
         Are there any glossaries connected to TABLE_NAME?
         

Replace TABLE_NAME with the name of a table or data asset loaded in your context graph (for example, `customers`).

The agent inspects the active context graph in memory and returns a conversational summary of connected business glossary terms and column relationships without re-querying the catalog.




### Traverse and expand the semantic graph

When you ask to explore new or deeper relationships beyond the active graph, the agent dynamically switches its tool strategy to discover connections such as schema joins, glossary definitions, or custom semantic documentation.

To trace relationships outward from a business concept or entity, follow these steps:

  1. In the prompt field, enter a request to trace relationships outward, and then click send **Send**. For example:
         
         Show how my data is connected to GLOSSARY_TERM
         

Replace GLOSSARY_TERM with the name of a business glossary term in your catalog (for example, `Customer Value`).

The agent traverses semantic and structural graph edges, adds the newly discovered entries to the canvas, centers the graph on the newly explored node, and updates the **Active nodes** counter. For more information about edge types, see the Graph visual reference section of this document.




### Generate SQL and inspect distributions

When you explore assets in the chat interface, you can perform analysis directly against your data using inline BigQuery conversational analytics.

To generate a query and inspect data distributions using the active context, follow these steps:

  1. In the prompt field, ask the agent to write a query using the visible nodes, and then click send **Send**. For example:
         
         Generate a query to calculate average customer balance by region
         using the active tables.
         

The agent uses the active context graph as grounding to generate context-aware SQL containing verified join keys (such as `customer_id` and `region_id`).

  2. Optional: To evaluate data distributions, ask the agent for statistical summaries.

The agent can execute queries and render inline data distribution charts within the chat window to help you evaluate data distributions before writing custom code.




## Manage your chat history

Knowledge Studio automatically saves your exploration sessions, letting you search, resume, or delete previous chats directly from the navigation pane.

To view or manage your chat history, follow these steps:

  1. In the Knowledge Studio navigation pane, ensure the **Recent** section is expanded.
  2. To locate a specific past conversation, in the **Search chats** field, enter keywords related to the chat's previous questions or context.
  3. To resume an exploration session, click the name of the chat in the list. Selecting the chat restores your previous conversation thread.
  4. To delete a past conversation, point to the chat name in the list, and then click the delete **Delete** icon.



## Pricing

During Preview, Knowledge Studio data exploration is offered at no charge.

When the exploration agent in chat invokes BigQuery query jobs (for example, with `@BqJobs`) or invokes BigQuery conversational analytics (for example, with `@BqCA`), standard BigQuery query processing and conversational analytics charges apply.

## What's next

Concept 

###  [ Knowledge Studio overview ](https://docs.cloud.google.com/knowledge-catalog/docs/knowledge-studio)

Learn how to orchestrate rich data context, build context sets, and ground AI agents using Knowledge Studio interfaces. 

Concept 

###  [ About data context ](https://docs.cloud.google.com/knowledge-catalog/docs/about-context)

Understand how active context transforms passive metadata to ground AI agents and prevent hallucinations. 

Task 

###  [ Use data insights for structured data ](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-insights-structured-data)

Mine query logs to automatically generate column descriptions, table summaries, and recommended joins. 

Discovery 

###  [ Search for data assets in Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets)

Find and explore catalog resources across Google Cloud and third-party systems using natural language. 

Concept 

###  [ About enrichment tasks ](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks)

Learn how to configure AI-driven metadata extraction workflows to build data context automatically. 

Ai integration 

###  [ About MCP servers in Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview)

Connect AI agents and developer tools to Knowledge Catalog using Model Context Protocol. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
