---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/access-control/
title: Database Migration Service IAM roles and permissions for AlloyDB for PostgreSQL \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:08:07.657866+00:00
---

# Database Migration Service IAM roles and permissions for AlloyDB for PostgreSQL  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Database Migration Service IAM roles and permissions for AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service uses IAM (IAM) roles and permissions to manage access to your migration resources.

## Accounts involved in data migration

When you perform homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL with Database Migration Service, the following accounts are involved in the migration process:

User account that performs the migration
    This is the [Google Account](https://docs.cloud.google.com/iam/docs/overview#google_account) that you sign in with to create connection profiles, create and run the migration job, and manage destination AlloyDB for PostgreSQL resources.
Database Migration Service service account
    This is the service account that is created for you when you enable the Database Migration Service API. The email address associated with this account is generated automatically and can't be changed. This email address uses the following format: 
    
    
    service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com
    

Each account involved in the data migration process requires a specific set of roles and permissions.

## Permissions and roles

To get the permissions that you need to perform continuous migrations to AlloyDB for PostgreSQL with Database Migration Service, ask your administrator to grant the required IAM roles on your project for the following accounts:

  * User account that performs the migration: 
    * [Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`)
    * [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)
  * Database Migration Service service account: 
    * [Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`)
    * [AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL with Database Migration Service:

  * User account that performs the migration: 
    * `datamigration.*`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `alloydb.operations.get`
    * `alloydb.clusters.create`
    * `alloydb.clusters.get`
    * `alloydb.clusters.list`
    * `alloydb.clusters.update`
    * `alloydb.clusters.delete`
    * `alloydb.instances.create`
    * `alloydb.instances.get`
    * `alloydb.instances.list`
    * `alloydb.instances.update`
    * `alloydb.instances.delete`
    * `alloydb.users.list`
    * `alloydb.users.get`
    * `alloydb.users.create`
    * `alloydb.users.update`
    * `alloydb.users.delete`
    * `compute.networks.get`
    * `compute.networks.list`
    * `compute.subnetworks.get`
    * `compute.subnetworks.list`
  * Database Migration Service service account: 
    * `datamigration.*`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
    * `alloydb.clusters.create`
    * `alloydb.clusters.get`
    * `alloydb.clusters.list`
    * `alloydb.clusters.update`
    * `alloydb.instances.create`
    * `alloydb.instances.get`
    * `alloydb.instances.list`
    * `alloydb.instances.update`
    * `alloydb.instances.executeSql`
    * `alloydb.operations.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
