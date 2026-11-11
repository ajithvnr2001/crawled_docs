---
url: https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations/
title: Quick-start migrations for homogeneous PostgreSQL \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:33:13.806996+00:00
---

# Quick-start migrations for homogeneous PostgreSQL  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/overview)



Send feedback 

#  Quick-start migrations for homogeneous PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes quick-start migrations for homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL. Quick-start migrations are a lightweight continuous migration flow for homogeneous PostgreSQL scenarios that streamline the migration process with features like automated networking, embedded discovery, fast replication (based on `pgnative`), and more. This page describes quick-start migrations for homogeneous PostgreSQL migrations to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL:

  * Overview provides the high-level description of what quick-start migrations are and how you can use them to enhance your migration experience.
  * Guides and supported scenarios contains links to step-by-step instructions for all quick-start migration flows.
  * Network connectivity explains the unique architecture employed by Database Migration Service in quick-start migrations.
  * Limitations describe known limitations and caveats to keep in mind when you follow quick-start migrations.



## Overview

With quick-start migrations, Database Migration Service can automatically set up everything you need to migrate sources accessible through private IP addresses in a VPC network, over VPC peering, or over public IP addresses. Destinations can be configured with either Private Service Connect or Private Services Access (PSA). Key highlights of quick-start migrations include:

  * **`pgnative` replication**: The native replication mechanism lets you migrate without installing extra PostgreSQL extensions or demoting the destination instance. Other databases on your destination instance remain operational, without any interruptions to your traffic. 
  * **Simplified networking** : Database Migration Service automatically handles network connectivity over private IPs. In quick-start migrations, all the required resources (private connectivity configuration, the network attachment and its subnet) are automatically created to enable connections over Private Service Connect interfaces. For more information, see the  Network connectivity section. 
  * **Embedded discovery** : You can start, manage, and monitor migrations directly in your destination Cloud SQL or AlloyDB for PostgreSQL instances with the [ Database Migration Service observability features](https://docs.cloud.google.com/database-migration/docs/overview#observability-metrics). 



The following table summarizes key differences between quick-start and standard homogeneous PostgreSQL migrations:

Feature | Standard migrations (pglogical) | Quick-start migrations (native replication)  
---|---|---  
**Extension installation** | Required. You must install and configure the `pglogical` extension on your source database. | Not required.  
**Destination instance state** | Must be empty and demoted (for Cloud SQL) or in bootstrapping mode (for AlloyDB for PostgreSQL). | Can be a live instance with active traffic to other databases (not being migrated).  
**Network connectivity** | Supports Private Service Connect interfaces, Virtual Private Cloud peering, reverse SSH tunnels, and public IP connectivity. The destination database connects directly to the source database, creating a dependency between source and destination network configurations.  | Uses a mediated architecture where Database Migration Service connects to the source and destination independently. For source connectivity method, Database Migration Service supports Private Service Connect interfaces, Virtual Private Cloud peering, and public IP connectivity (with dedicated private connectivity configuration for public IP).  For destination connectivity, Database Migration Service leverages dedicated internal networking. This means that your destination instance must have a private IP enabled, but can also allow public IP connections. For example, your destination can be configured to use any combination of Private Service Connect, Private Services Access (PSA), and incoming Public IP connections. Destinations configured without any private IP aren't supported.   
**Tables without primary keys** | Not supported. All tables must have primary keys. | Supported. You can replicate tables without primary keys by setting the replica identity to `INDEX` or `FULL`.   
**Parallel migration jobs** | Not supported. You can run only one migration job per source database instance. | Supported. You can run multiple migration jobs in parallel from the same source instance, with each job migrating different databases (up to 50 databases per job).  
**Destination object ownership** | Objects are owned by the `postgres` user. | Objects are owned by the migration user generated by Database Migration Service (if using the Google Cloud console) or the user you supply (if using Google Cloud CLI).   
  
## Guides and supported scenarios

_A video preview of the quick-start migration flow._

Quick-start migrations for homogeneous PostgreSQL facilitate continuous homogeneous migrations to new or existing Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL destinations. This migration flow supports migrating over public or private IP connections:

  * For sources accessible over public IP addresses by using a dedicated private connectivity configuration for public IP. Sources hosted outside Google Cloud can connect directly using public IP, or through private IP using network components such as a Cloud VPN connection or Cloud Interconnect.

  * For sources accessible over private IP addresses in your Google Cloud Virtual Private Cloud (VPC) network (using Private Service Connect interfaces), such as self-managed databases on Compute Engine or Cloud SQL for PostgreSQL instances.




You can begin your quick-start migration journey in multiple places in the Google Cloud console:

  * The Google Cloud console for Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL, where you begin the quick-start migration directly from your instance or cluster. For more information, see: 
    * [ Run a quick-start migration directly from your Cloud SQL for PostgreSQL instance or cluster](https://docs.cloud.google.com/sql/docs/postgres/quick-start-migrations-guide)
    * [ Run a quick-start migration directly from your AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/alloydb/docs/quick-start-migrations-guide)
  * Database Migration Service, where you can create a new destination cluster or instance as you configure the quick-start migration. For more information, see: 
    * [ Use quick-start migrations in Database Migration Service for Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide)
    * [ Use quick-start migrations in Database Migration Service for AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quick-start-migrations-guide)



## Network connectivity

At a high-level, quick-start migrations use a mediated networking architecture. Database Migration Service and destination Cloud SQL for PostgreSQL or AlloyDB for PostgreSQL instances reside in their own networks outside the VPC networks that you use in your Google Cloud project. Database Migration Service acts as an intermediary, establishing independent connections to your source database and to your destination database.

![](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/quick-start-migration-overall-connectivity.svg) **Figure 1.** Simplified view of networking for quick-start migrations (click to enlarge) ![](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/quick-start-migration-overall-connectivity.svg)

Database Migration Service fully facilitates both source and destination connectivity for quick-start migrations.

For **source database connectivity** , Database Migration Service can connect to your source database over  private IP with Private Service Connect interfaces or from a  dedicated public IP. You configure source connectivity with the private connectivity configuration resource in Database Migration Service.

For **destination database connectivity** , Database Migration Service fully manages network communication to your destination instance over private networks. This means that your destination instance must have a private IP configured, but depending on the scenario, different combinations of connectivity settings are supported:

  * _Cloud SQL for PostgreSQL destinations_ : For quick-start migrations, the Cloud SQL for PostgreSQL destinations are required to have a private IP configured, but they are also allowed to be enabled for public IP connectivity. These destination instances can be configured to use any combination of Private Service Connect, Private Services Access (PSA), and incoming Public IP connections. Destinations configured without any private IP aren't supported.

  * _AlloyDB for PostgreSQL destinations_ : For quick-start migrations, the AlloyDB for PostgreSQL destinations must be instances enabled for Private Service Connect connectivity. PSA or public IP connectivity can be enabled on the destination after you complete the quick-start migration.




### Source connectivity with Private Service Connect interfaces

#### Source connectivity to databases outside Google Cloud

When you migrate from a database hosted outside Google Cloud, you need additional network components to ensure that your database has a private IP address assigned in your Google Cloud VPC network (for example a VPC network). Database Migration Service creates the network attachment in the VPC network where your instance has a private IP assigned.

![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from databases hosted on-premise or
        as managed offerings outside Google Cloud.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/external-src-quick-start-migration-network.svg) **Figure 2.** Network connectivity facilitated by Database Migration Service for quick-start migrations from databases hosted on-premise or as managed offerings outside Google Cloud. (click to enlarge) ![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from databases hosted on-premise or
        as managed offerings outside Google Cloud.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/external-src-quick-start-migration-network.svg)

#### Source connectivity to self-hosted databases on Compute Engine

When you migrate from a self-hosted databases on Compute Engine, Database Migration Service creates the network attachment in the same VPC network where you have your VM.

![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from self-hosted databases on Compute Engine.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/gce-src-quick-start-migration-network.svg) **Figure 3.** Network connectivity facilitated by Database Migration Service for quick-start migrations from self-hosted databases on Compute Engine. (click to enlarge) ![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from self-hosted databases on Compute Engine.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/gce-src-quick-start-migration-network.svg)

#### Source connectivity to Cloud SQL for PostgreSQL

When you migrate from a Cloud SQL for PostgreSQL instance, Database Migration Service creates the network attachment in the VPC network where your instance has a private IP assigned. This IP can be a result of a Private Services Access (PSA) or Private Service Connect configuration. For more information, see [ Private IP configuration in the Cloud SQL documentation](https://docs.cloud.google.com/sql/docs/postgres/private-ip).

![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from a Cloud SQL for PostgreSQL instance.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/csql-src-quick-start-migration-network.svg) **Figure 4.** Network connectivity facilitated by Database Migration Service for quick-start migrations from a Cloud SQL for PostgreSQL instance. (click to enlarge) ![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from a Cloud SQL for PostgreSQL instance.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/csql-src-quick-start-migration-network.svg)

### Source connectivity using public IP

When you migrate from a source database that uses a public IP address, quick-start migrations rely on a specialized private connectivity configuration for public IP. When configured, Database Migration Service allocates a newly created, dedicated static public IP address available exclusively for that private connectivity configuration. If your source database is protected by a firewall or an incoming IP allowlist, you must add this dedicated public IP address to your source database firewall rules or incoming IP allowlist so that Database Migration Service can establish a connection.

![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from a database using public IP.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/quick-start-migrations-public-IP.svg) **Figure 5.** Network connectivity facilitated by Database Migration Service for quick-start migrations using public IP. (click to enlarge) ![This diagram shows network connectivity facilitated by Database Migration Service
        for quick-start migrations from a database using public IP.](https://docs.cloud.google.com/static/database-migration/docs/images/quick-start-migrations/quick-start-migrations-public-IP.svg)

## Limitations

The following limitations apply to quick-start migrations. If your migration scenario requires the use of any unsupported features, we recommend you follow the standard migration flow instead. For more information, see [Migrate to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest) or [ Migrate to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest) documentation pages.

  * Quick-start migrations don't support migrating from PostgreSQL versions `9.6` or lower.

  * Reverse SSH tunnels aren't supported for quick-start migrations. Source connectivity must use Private Service Connect interfaces, VPC peering, or public IP.

  * SSL encryption options for source connections only support `none` and `required` variants for quick-start migrations (standard migrations support `verify-ca` and `verify-full`).

  * Quick-start migrations can accommodate up to 50 databases per migration job. If your source server contains more than 50 databases, you can set up multiple parallel migration jobs to migrate them.

  * [ Standard migration fidelity limitations](https://docs.cloud.google.com/database-migration/docs/postgres/migration-fidelity) apply, with the following exceptions:

    * You don't have to install the `pglogical` extension for quick-start migrations.
    * Migrating tables without primary keys is supported.



## What's next

  * [ Discover the full capabilities of Database Migration Service](https://docs.cloud.google.com/database-migration/docs/overview).

  * [ Learn more about Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/introduction).

  * [ Learn more about AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
