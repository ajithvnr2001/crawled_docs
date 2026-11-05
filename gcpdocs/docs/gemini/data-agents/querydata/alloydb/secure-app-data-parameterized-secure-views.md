---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/alloydb/secure-app-data-parameterized-secure-views/
title: Secure and control access to application data using parameterized secure views \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:04:49.460131+00:00
---

# Secure and control access to application data using parameterized secure views  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/alloydb/secure-app-data-parameterized-secure-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Secure and control access to application data using parameterized secure views Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Parameterized secure views provide data security and row access control to applications. They filter query results based on the application user's identity.

This tutorial describes how to set up parameterized secure views in AlloyDB for PostgreSQL, configure database roles and privileges to restrict access to base tables, and verify data security. The examples provided in this document are for demonstration purposes only.

## What are parameterized secure views?

As a general best practice, your application should run using a service account with the minimal required access to your database. For example, if your application shouldn't write to your database, it should use a role with read-only access. You should configure these access controls at the database level.

When your application needs more granular security than standard database-level access permits, you can use parameterized secure views to make sure that users view only their authorized data. Parameterized secure views provide dynamic data security and row access control suitable for multi-tenant SaaS applications without requiring separate database roles for each application end user.

Using parameterized secure views provides three main benefits:

  * Dynamic data security and row access control: Filters queries using end-user identifiers so users access only their authorized data regardless of query phrasing.
  * Easier role management: Uses a single shared database role for all application users instead of managing separate database roles for each individual.



## Objectives

  * Create parameterized secure views with named view parameters.
  * Create the database role that is used by the application to connect to the database and access parameterized secure views.
  * Grant the new role permissions to the parameterized secure views and revoke access to the base tables.
  * Connect using the new role and verify that the restricted tables can't be accessed. 
  * Run queries on the parameterized secure views using the `execute_parameterized_query()` function or using the QueryData API. 



## Costs

In this document, you use the following billable components of Google Cloud:

  * [ AlloyDB for PostgreSQL](https://cloud.google.com/alloydb/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

New Google Cloud users might be eligible for a [free trial](https://cloud.google.com/free).

To avoid continued billing, delete the resources you created when you finish the tasks in this document. For more information, see Clean up.

## Before you begin

Before you create parameterized secure views, complete the following prerequisites.

### Enable billing and required APIs

  1. In the Google Cloud console, select a project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Make sure that billing is enabled for your Google Cloud project.](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project)

  3. Enable the Cloud APIs necessary to create and connect to AlloyDB for PostgreSQL.

     1. [Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=alloydb.googleapis.com,dataplex.googleapis.com,geminidataanalytics.googleapis.com)

     2. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.

     3. In the **Enable APIs** step, click **Enable** to enable the following:

        * AlloyDB for PostgreSQL API
        * Knowledge Catalog API
        * Data Analytics API with Gemini (`geminidataanalytics.googleapis.com`)



### Create and connect to a database

  1. [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#create-cluster).
  2. [Connect to your instance and create a database](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#run).



### Grant required roles and create an IAM database user

To authenticate with Identity and Access Management (IAM) and run `queryData` requests against parameterized secure views, configure the IAM user or service account:

  1. Grant the following IAM roles to `IAM_USER_EMAIL` on your Google Cloud project:

     * `roles/geminidataanalytics.queryDataUser`
     * `roles/serviceusage.serviceUsageConsumer`
     * `roles/alloydb.databaseUser`

For more information about granting IAM roles, see [Add IAM policy binding for a project](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

  2. Enable IAM authentication on your AlloyDB instance and add `IAM_USER_EMAIL` as an IAM-based database user on your cluster. You must create this IAM database user before you grant the `psv_user` database role to it. For more information about setting up IAM database users, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).




## Prepare your environment

To prepare for running queries on a parameterized secure view, set up the database, database roles, the `parameterized_views` extension, and the application schema.

### Enable the database flag

Enable the `parameterized_views.enabled` database flag, which loads the required extension libraries. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags). **Note:** Enabling the `parameterized_views.enabled` database flag restarts your database to apply these changes. 

### Set up the database

  * Create a database called `database` for the application data and parameterized secure views. For more information, see [Create a database](https://docs.cloud.google.com/alloydb/docs/database-create).



### Create database roles, the extension, and the application schema

  1. In the Google Cloud console, go to the AlloyDB page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. Sign in to **Studio** using administrator account authentication.

  5. Click **Authenticate**. The Explorer pane displays a list of the objects in your database.

  6. Click **New SQL editor tab** or **New tab** to open a new tab.

  7. To use parameterized views, create the `parameterized_views` extension in your database:
         
         -- Requires parameterized_views.enabled set to true
         CREATE EXTENSION parameterized_views;
         

When the extension is created, the database also creates a schema named `parameterized_views` so that the APIs are contained in that schema's namespace and so that those APIs don't conflict with existing APIs.

**Note:** You must create an extension in every database in which parameterized views are created.
  8. Sign in as a user with superuser privileges, such as the built-in `postgres` user. If you want to create a new superuser, for example `admin_user`, then run the following commands:
         
         CREATE ROLE admin_user WITH LOGIN PASSWORD '...';
         GRANT ALL PRIVILEGES ON DATABASE database TO admin_user;
         

For more information, see [`CREATE USER`](https://www.postgresql.org/docs/15/sql-createuser.html).

  9. Create a new database role for executing queries against parameterized secure views, and grant `admin_user` the ability to administer this role. This is an AlloyDB role that the application uses to connect and sign into the database to execute queries with limited access to public functions or objects to the minimal required set.
         
         CREATE ROLE psv_user WITH LOGIN PASSWORD '...';
         GRANT psv_user TO admin_user WITH ADMIN OPTION;
         

For more information, see [`CREATE USER`](https://www.postgresql.org/docs/15/sql-createuser.html).

  10. Connect as the administrative user.
         
         SET role TO admin_user;
         

  11. Create the schema that contains the tables.
         
         CREATE SCHEMA store;
         

  12. Create the tables and insert data.
         
         CREATE TABLE store.checked_items(bag_id INT,timestamp TIMESTAMP, loc_code CHAR(3), scan_type CHAR(1), location TEXT, customer_id INT);
         
         INSERT INTO store.checked_items (bag_id, timestamp, loc_code, scan_type, location, customer_id) VALUES
         (101, '2023-10-26 10:00:00', 'ABC', 'I', 'Warehouse A', 123),
         (102, '2023-10-26 10:15:30', 'DEF', 'O', 'Loading Dock B', 456),
         (103, '2023-10-26 10:30:45', 'GHI', 'I', 'Conveyor Belt 1', 789),
         (104, '2023-10-26 11:00:00', 'JKL', 'O', 'Shipping Area C', 101),
         (105, '2023-10-26 11:45:15', 'MNO', 'I', 'Sorting Station D', 202),
         (106, '2023-10-26 12:00:00', 'PQR', 'O', 'Truck Bay E', 303);
         




## Create parameterized secure views and set up access privileges

To create parameterized secure views and to set up appropriate access privileges for the base table and views, follow these steps:

  1. In the Google Cloud console, go to the AlloyDB page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB Studio**. 

  4. Sign in to **Studio** and connect to the database named `database` as the `admin_user` user. 

  5. Click **Authenticate**. The Explorer pane displays a list of the objects in your database. 

  6. Click **New SQL editor tab** or **New tab** to open a new tab.

  7. To provide limited access to the view, create a parameterized view:
         
         CREATE VIEW store.secure_checked_items WITH (security_barrier) AS
         SELECT bag_id, timestamp, location
         FROM store.checked_items t
         WHERE customer_id = $@app_end_userid;
         

**Note:** Make sure that you use unique parameter names, such as `$@app_end_userid`, when creating parameterized secure views.
  8. Grant access to the view.
         
         GRANT SELECT ON store.secure_checked_items TO psv_user;
         

  9. To access the view, grant access to the schema.
         
         GRANT USAGE ON SCHEMA store TO psv_user;
         

  10. Revoke direct access to the base table.
         
         REVOKE ALL PRIVILEGES ON store.checked_items FROM psv_user;
         

**Note:** The owner of the parameterized view must have `SELECT` privileges on the base tables. In addition, the user of the parameterized view must have `USAGE` on the schema of the view and `SELECT` on the view. For example, the `admin_user` user owns the parameterized view, so it has `SELECT` privileges on the base tables while the `psv_user` must have `USAGE` on the `store` schema and `SELECT` on the view.

  11. Make sure that `IAM_USER_EMAIL` has been added to the cluster as an IAM database user, sign in as the `postgres` user or as `admin_user`, and grant the `psv_user` role to the IAM-authenticated user:
         
         GRANT psv_user TO "IAM_USER_EMAIL";
         

Replace `IAM_USER_EMAIL` with your IAM user email address.




## Verify data security

To verify that the parameterized secure views are restricting access to the designated views, sign into the database as the IAM-authenticated user. In AlloyDB, IAM users inherit the permissions of the database roles assigned to them.

  1. Sign into the database as the IAM-authenticated user.

  2. Verify that the base table can't be accessed.
         
         SELECT * FROM store.checked_items;
         ERROR:  permission denied for table checked_items
         

  3. Access the parameterized secure views using the `execute_parameterized_query` function:
         
         SELECT * FROM parameterized_views.execute_parameterized_query(
           query => 'SELECT * from store.secure_checked_items',
           param_names => ARRAY ['app_end_userid'],
           param_values => ARRAY ['303']
         );
         

  4. Sign in to the Google Cloud CLI as `IAM_USER_EMAIL` by running `gcloud auth application-default login` so that `gcloud auth application-default print-access-token` generates a token for the restricted IAM database user, and then query the parameterized secure views using the `queryData` method with PSV parameters:
         
         curl -X POST \
             "https://geminidataanalytics.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION:queryData" \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "x-goog-user-project: PROJECT_ID" \
             -H "Content-Type: application/json; charset=utf-8" \
             -d '{
               "prompt": "Show me the checked items.",
               "context": {
                 "datasource_references": {
                   "alloydb": {
                     "database_reference": {
                       "project_id": "PROJECT_ID",
                       "region": "REGION",
                       "cluster_id": "CLUSTER_ID",
                       "instance_id": "INSTANCE_ID",
                       "database_id": "DATABASE_ID",
                       "table_ids": [
                         "store.secure_checked_items"
                       ]
                     }
                   }
                 },
                 "parameterized_secure_view_parameters": {
                   "parameters": [
                     {
                       "key": "app_end_userid",
                       "value": "303"
                     }
                   ]
                 }
               },
               "generation_options": {
                 "generate_query_result": true,
                 "generate_natural_language_answer": true,
                 "generate_explanation": true
               }
             }'

Use the `table_ids` field in `database_reference` to ensure `QueryData` only generates SQL against the `store.secure_checked_items` parameterized secure view. If you omit `table_ids` and the database role has `SELECT` access on the `store.checked_items` base table, `QueryData` might query the base table directly, bypassing the secure view. Specify the schema-qualified view name because unqualified names in `table_ids` default to the `public` schema.

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region where your AlloyDB for PostgreSQL instance is located.
     * `CLUSTER_ID`: the ID of your AlloyDB for PostgreSQL cluster.
     * `INSTANCE_ID`: the ID of your AlloyDB for PostgreSQL instance.
     * `DATABASE_ID`: the ID of your AlloyDB for PostgreSQL database, which is `database` in this tutorial.

## Clean up

### Delete the cluster

When you delete the cluster that you created in the Before you begin section, you also delete all of the objects that you created.

     1. In the Google Cloud console, go to the AlloyDB page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

     2. Select a cluster from the list.

     3. Click **Delete cluster**.

     4. In **Delete cluster** , enter name of the cluster to confirm you want to delete your cluster.

## What's next

     * Learn about [parameterized secure views](https://docs.cloud.google.com/alloydb/docs/parameterized-secure-views-overview).
     * Learn how to [manage application data security using parameterized secure views](https://docs.cloud.google.com/alloydb/docs/manage-application-data-security-parameterized-secure-views). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
