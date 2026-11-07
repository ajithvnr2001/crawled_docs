---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets/
title: Manage context sets \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:53:32.786373+00:00
---

# Manage context sets  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage context sets Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Context sets let you organize semantic information and data asset references into bounded containers that ground AI agents. In Knowledge Studio, you can create, view, update, and delete context sets, and configure access control for each container.

You must configure a context set before you run an enrichment task to generate metadata proposals. You can create a context set as a standalone container or during enrichment task setup. For more information, see [Context sets overview](https://docs.cloud.google.com/knowledge-catalog/docs/context-sets) and [Create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks).

## Before you begin

Before you manage context sets, make sure that you have the required Identity and Access Management (IAM) roles.

### Required roles

To get the permissions that you need to create and manage context sets and their entries, ask your administrator to grant you the following IAM roles on the project or context set: 

  * To create context sets in a project: **Dataplex Content Creator** (`roles/dataplex.contentCreator`) or **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) 
  * To discover context sets without reading their entries: [**Dataplex Content Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.contentViewer) (`roles/dataplex.contentViewer`) 
  * To view entries and propose changes in a context set: [**Dataplex Content User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.contentUser) (`roles/dataplex.contentUser`) 
  * To create, update, delete, and link entries in a context set: [**Dataplex Content Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.contentEditor) (`roles/dataplex.contentEditor`) 
  * To manage IAM permissions on or delete a context set: [**Dataplex Content Admin** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.contentAdmin) (`roles/dataplex.contentAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage context sets and their entries. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage context sets and their entries:

  * Create context sets: `dataplex.entryGroups.createContextSet`
  * List context sets: `dataplex.entryGroups.list`
  * View context set details: `dataplex.entryGroups.getContextSet`
  * Update context sets: `dataplex.entryGroups.updateContextSet`
  * Delete context sets: `dataplex.entryGroups.deleteContextSet`
  * Propose changes to context sets: `dataplex.entryGroups.requestContextChanges`
  * Manage context set IAM policies: `dataplex.entryGroups.getIamPolicy, dataplex.entryGroups.setIamPolicy`
  * Create, view, list, update, and delete entries in a context set: `dataplex.entries.createContext, dataplex.entries.getContext, dataplex.entries.listContext, dataplex.entries.updateContext, dataplex.entries.deleteContext`
  * Link and unlink catalog assets on context set entries: `dataplex.entryLinks.create, dataplex.entryLinks.delete, dataplex.entries.link, dataplex.entryGroups.useReferenceEntryLink`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

When you create a context set, Knowledge Catalog automatically grants you the **Dataplex Content Admin** (`roles/dataplex.contentAdmin`) role on that context set.

**Caution:** Context set permissions (`dataplex.entryGroups.*ContextSet` and `dataplex.entries.*Context`) enforce access control on context sets as intended. However, the pre-existing **Dataplex Entry Group Owner** (`roles/dataplex.entryGroupOwner`) and **Dataplex Entry Owner** (`roles/dataplex.entryOwner`) roles include these context set permissions, which are scheduled to be removed from both roles in an upcoming update. If you want to prevent principals with **Dataplex Entry Group Owner** (`roles/dataplex.entryGroupOwner`) or **Dataplex Entry Owner** (`roles/dataplex.entryOwner`) from accessing context sets during Preview, avoid granting those two pre-existing roles (for example, by configuring custom roles) or create your context sets in a dedicated project where those pre-existing roles aren't granted.

## Create a context set

To create a context set to store your curated or enriched metadata, follow these steps:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the navigation pane, select **Context sets**.

  3. On the **Context sets** page, click **Create context set**.

  4. In the **Create context set** pane, enter a descriptive name in the **Display name** field and a unique identifier in the **Context set ID** field (or keep the auto-generated ID). The context set ID becomes the entry group resource ID in the API and can't be changed after creation.

  5. In the **Region** menu, select a Google Cloud location for the context set:

     * **Regional** (for example, `us-central1`): Recommended when all enriched assets reside in a single region.
     * **Multi-region** (for example, `us` or `eu`): Lets the context set span assets located across multiple single regions within that geographic boundary.
     * **Global** (`global`): Lets the context set reference assets across any region.
  6. Optional: Enter a **Description** summarizing the business domain and purpose of the context set, and click **Add label** to attach key-value labels.

  7. Click **Create**.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. On the **Metadata types** page, click **Create**.

  4. In the **Create context set** pane, enter a descriptive name in the **Display name** field and a unique identifier in the **Context set ID** field (or keep the auto-generated ID). The context set ID becomes the entry group resource ID in the API and can't be changed after creation.

  5. In the **Region** menu, select a Google Cloud location for the context set:

     * **Regional** (for example, `us-central1`): Recommended when all enriched assets reside in a single region.
     * **Multi-region** (for example, `us` or `eu`): Lets the context set span assets located across multiple single regions within that geographic boundary.
     * **Global** (`global`): Lets the context set reference assets across any region.
  6. Optional: Enter a **Description** summarizing the business domain and purpose of the context set, and click **Add label** to attach key-value labels.

  7. Click **Create**.




After you create the context set, you can select it as the target for an enrichment task. The enrichment run populates the container with proposed metadata documents, concepts, and data asset entries. For more information, see [About enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/about-enrichment-tasks).

## View context sets

To view existing context sets, follow these steps:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the navigation pane, select **Context sets** to view the context sets in the selected project.

  3. To view the details of a specific context set, click its name in the list.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. Optional: Turn on the **Show from all projects** toggle to browse context sets that you have permission to view across all Google Cloud projects.

  4. To view the details of a specific context set, click its name in the list.




The context set details page includes the following sections and controls:

  * **Container metadata** : Displays the context set's description, location, project ID, creation and modification timestamps, and labels.
  * **Top action bar** : Provides buttons to manage the context set (**Edit** , **Delete** , and **Permissions**).
  * **Entries table** : Lists the entries stored in the context set, including each entry's **Name** , **Description** , **Entry type** , **Created Date** , and **Linked assets**.



## Edit a context set

Using the Google Cloud console, you can edit the container properties of a context set, which include its **Display name** , **Description** , and **Labels**.

To update the metadata entries inside a context set, run an enrichment task targeting that context set and approve the generated change proposals. For more information about approving change proposals, see [Evaluate and approve enrichment proposals](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs).

To edit the properties of a context set, follow these steps:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the navigation pane, select **Context sets**.

  3. Click the name of the context set that you want to edit, and then click **Edit** on the details page. Alternatively, select the checkbox next to the context set in the list and click **Edit** in the top action bar, or click more_vert **More options** > **Edit** in the row.

  4. Modify the editable fields (**Display name** , **Description** , or **Labels**), and then click **Save**.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. Click the name of the context set that you want to edit, and then click **Edit** on the details page.

  4. Modify the editable fields (**Display name** , **Description** , or **Labels**), and then click **Save**.




## Delete a context set

Deleting a context set removes its entries and semantic associations from the data context graph. The console doesn't display a warning if you delete a context set that is referenced by an existing enrichment task. If you delete a context set while an enrichment run is active, the run fails to save its proposed metadata at completion because the target destination is no longer available. Subsequent runs of the enrichment task also fail after running until you recreate the context set or create a new enrichment task targeting a valid context set.

To delete a context set, follow these steps:

### Knowledge Studio

  1. In the Google Cloud console, go to the **Knowledge Studio** page.

[Go to Knowledge Studio](https://console.cloud.google.com/dataplex/studio)

  2. In the navigation pane, select **Context sets**.

  3. Click the name of the context set that you want to delete, and then click **Delete** on the details page. Alternatively, select the checkbox next to the context set in the list and click **Delete** in the top action bar, or click more_vert **More options** > **Delete** in the row.

  4. Confirm the deletion.




### Metadata types

  1. In the Google Cloud console, go to the **Metadata types** page.

[Go to Metadata types](https://console.cloud.google.com/dataplex/catalog/entry-groups)

  2. Click **Entry groups** > **Context set**.

  3. Click the name of the context set that you want to delete, and then click **Delete** on the details page.

  4. Confirm the deletion.




## Limitations

For information about limitations that apply during Preview, see the Preview scope and boundaries section in [Context sets overview](https://docs.cloud.google.com/knowledge-catalog/docs/context-sets#preview-scope).

## What's next

For more information, see the following resources:

  * [Configure prerequisites for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites)
  * [Create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks)
  * [Evaluate and approve enrichment proposals](https://docs.cloud.google.com/knowledge-catalog/docs/manage-enrichment-runs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
