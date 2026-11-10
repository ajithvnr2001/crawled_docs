---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-considerations/
title: Plan your networking configuration \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T12:43:07.134120+00:00
---

# Plan your networking configuration  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Plan your networking configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a high-level overview of what you need to consider when you plan network connectivity for your migration.

From a networking perspective, Database Migration Service and AlloyDB for PostgreSQL are _service producers_ that reside in their own dedicated networks (known as _service networks_), outside the Virtual Private Cloud (VPC) networks that you use in your Google Cloud project.

Depending on whether you perform a **standard migration** or a **quick-start migration** , Database Migration Service leverages different networking architectures to connect to your databases. This page focuses primarily on networking considerations for **standard continuous migrations**.

## Standard migration connectivity

For standard homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL, Database Migration Service connects to the _destination_ AlloyDB for PostgreSQL cluster and manages the migration process on its behalf. It's the destination cluster that establishes the direct network connection to your source instance, while Database Migration Service oversees the process.

The goal of configuring network connectivity for a standard migration is to ensure that the destination AlloyDB for PostgreSQL cluster can route to and reach your source database server over the network.

Different connectivity methods are available depending on your source database offering and your destination AlloyDB for PostgreSQL network configuration:

  * **IP allowlist** : Connects over the public internet by adding the destination outbound IP address to the source firewall or allowlist.
  * **Reverse SSH tunnel** : Routes replication traffic through an intermediate Compute Engine bastion host over an encrypted SSH tunnel.
  * **TCP proxy through a cloud-hosted VM** : Routes replication traffic through a containerized TCP proxy on an intermediate Compute Engine VM when direct routing between networks isn't possible.
  * **Private connectivity with VPC peering** : Connects to the private IP address of your source database across peered VPC networks (for Private Services Access destination clusters).
  * **Private connectivity with Private Service Connect interfaces** : Connects to the private IP address of your source database using network attachments (for PSC-enabled destination clusters).



Before you configure your source instance for migration, see the [ Networking overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods) page to evaluate the end-to-end networking landscape and pick the best method for your scenario.

## Quick-start migrations connectivity

Quick-start migrations use a mediated networking model where Database Migration Service acts as an intermediary sitting _between_ your source database and the destination AlloyDB for PostgreSQL cluster:

  * **Source connectivity** : Database Migration Service supports multiple connectivity methods for your source database, including Private Service Connect interfaces, Virtual Private Cloud peering, and public IP connectivity using a dedicated private connectivity configuration for public IP. When you use public IP connectivity, Database Migration Service allocates a dedicated public IP address that you allowlist on your source database firewall.

  * **Destination connectivity** : Database Migration Service fully manages network communication to your destination cluster. The destination cluster must be enabled for Private Service Connect.




For a comprehensive explanation of the quick-start networking architecture, component diagrams, and limitations, see [ Network connectivity for quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) in the main Database Migration Service documentation.

## What's next

  * To configure a quick-start migration, see the [ Quick-start migrations guide](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/quick-start-migrations-guide).
  * For complete, step-by-step migration walkthroughs, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).
  * To review known limitations before migrating, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
