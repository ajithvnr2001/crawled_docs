---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/convert-sql/
title: Convert Oracle code and schema to PostgreSQL syntax \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:21:58.688369+00:00
---

# Convert Oracle code and schema to PostgreSQL syntax  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/convert-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Convert Oracle code and schema to PostgreSQL syntax Stay organized with collections  Save and categorize content based on your preferences. 

After you [ create your conversion workspace and perform the initial schema conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace), you can fix conversion issues, modify your objects with the interactive editor, and apply converted schema to your destination database.

Databases can often have thousands of objects. Converting them all in a single session might be a challenging process. With conversion workspaces, you can divide the conversion process into multiple phases where you add new objects to the conversion, fix the issues, and then test them in your destination database.

Conversion workspaces can produce deterministic conversion results, or enhance them with [ Gemini auto-conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini#auto-conversion). When Gemini auto-conversion is enabled, Database Migration Service applies auto-conversion augmentations to all your objects every time you convert the source schema. If you want to use only deterministic conversion rules, disable Gemini auto-conversion in your workspace.

To convert objects from your source database, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces**. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. From the list of available conversion workspaces, select your workspace. 

Conversion workspace editor opens.

  3. Use the **Oracle** schema panel to check your source objects for conversion issues. This panel contains all the objects you pulled from your schema during [ workspace creation](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace). 

We also recommend that you check the converted code with Gemini-powered conversion features. Features such as the [ conversion assistant](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini#conversion-assistant) or [ quality assessments](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini#quality-assessments) can greatly expedite your conversion process. 

  4. [ Fix your conversion issues](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#fix-conversion-issues). 

You can use the interactive SQL editor, upload a conversion mapping file to convert the object in a specific way, or utilize Gemini-powered conversion features. 

  5. Optional: You can also use the interactive SQL editor to adjust the converted schema to better meet your needs, even if there are no conversion issues with your object. For a list of editable Oracle objects, see [ Supported object types](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-conversion-workspaces). 
  6. After you fix conversion issues or adjust your schema, click move_down **Convert source**. Database Migration Service now analyzes your changes and generates the updated PostgreSQL schema. 

You can inspect the converted schema in the **Cloud SQL for PostgreSQL draft** tab. 

  7. Test the converted schema in your destination database. Do the following: 
     1. Click apps **Apply to destination** > **Test**.
     2. On the **Define destination** page, use the **Destination connection profile**
drop-down menu to select your destination connection profile. 
     3. Click **Define and continue**.
     4. On the **Select objects and test application** page, use the checkboxes to select which 
converted PostgreSQL schema you want to apply in your destination database. 
     5. Click **Test application**.

Depending on the test results, you might need to further adjust your converted schema.

  8. If the schema snapshot you pulled from the source has more objects that you haven't migrated yet, add these objects to the workspace: 
     1. In the **Oracle** panel, click add **Add objects**. 

The object selection panel opens.

     2. In the schema tree, use the checkboxes to select which objects you want to add to the conversion and then click **Add objects**. 
  9. Repeat steps 3 through 8 until you convert all the objects that you want to migrate. 
  10. When you finish converting your schema, click apps **Apply to destination** > **Apply**. 

Database Migration Service now creates the schema definitions in your destination database. 




## What's next

  * Your conversion workspace is ready for migration. You can now [ create the migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-migration-job).

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
