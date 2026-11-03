---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-connection-profiles/
title: About connection profiles \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:45:40.991758+00:00
---

# About connection profiles  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  About connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

Connection profiles capture identifiers for your source databases. For homogeneous migrations, Database Migration Service requires that you create source connection profiles when you migrate with the Google Cloud console.

_Destination connection profiles_ represent your destination AlloyDB for PostgreSQL cluster. They are required only if you use Google Cloud CLI for homogeneous migrations. You can't view or manage destination connection profiles in the Google Cloud console.

Each connection profile contains the minimum required amount of information Database Migration Service needs to facilitate data movement between the data source and destination. That information includes:

  * **Connection profile name** : A human-readable name for your connection profile. This value is displayed in Database Migration Service in the Google Cloud console.

  * **Connection profile ID** : A machine-readable identifier for your connection profile. This value is used when you work with connection profiles by using Database Migration Service Google Cloud CLI commands or API.

  * **Region** : The region where your connection profile is saved. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination AlloyDB for PostgreSQL clusters) must be saved in a single region. For more information on region requirements in Database Migration Service, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).

  * **Source database connection information** : The hostname or IP address, port, and username and password for Database Migration Service to connect to your source database.

  * **Destination cluster connection information** : For destination connection profiles used with Google Cloud CLI, the destination AlloyDB for PostgreSQL cluster identifier, database username, and password.




## What's next

  * [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles)
  * [ Manage connection profiles](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/manage-connection-profiles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
