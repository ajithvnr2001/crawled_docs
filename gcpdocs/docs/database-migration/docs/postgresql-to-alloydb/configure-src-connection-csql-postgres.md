---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-src-connection-csql-postgres/
title: Configure network connectivity for Cloud SQL for PostgreSQL sources \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:33:46.944574+00:00
---

# Configure network connectivity for Cloud SQL for PostgreSQL sources  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-src-connection-csql-postgres/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Configure network connectivity for Cloud SQL for PostgreSQL sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity for Cloud SQL for PostgreSQL sources for homogeneous migrations to AlloyDB for PostgreSQL clusters with Database Migration Service.

There are several methods you can use to configure connectivity between Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL:

  * Private IP connectivity with Private Service Connect interfaces

  * Private IP connectivity with Virtual Private Cloud peering

  * Public IP allowlist




For migrations between Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL with Database Migration Service, we don't recommend using the reverse-SSH tunnel connectivity method.

## Configure Private Service Connect interfaces

This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering-quotas). Private Service Connect interfaces are the recommended method for private IP connectivity when migrating to an AlloyDB for PostgreSQL cluster. Private Service Connect interfaces are only available when you [ migrate to an existing AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance).

To use private connectivity with Private Service Connect interfaces, follow these steps:

  1. In your project, ensure you have a Virtual Private Cloud network with [ private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

This is the network that connects to your source database server using Private Services Access (PSA). 

  2. Make sure your source Cloud SQL instance is configured with a private IP and Private Service Access (PSA) with the VPC network described in the previous step. For more information, see [ Use private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip) in the Cloud SQL documentation. 
  3. Create or select a destination AlloyDB for PostgreSQL cluster enabled for Private Service Connect. See [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  4. Configure Private Service Connect for outbound connectivity from your destination cluster. At a high level, this process involves: 
     1. Creating a network attachment in the VPC network where your source instance has a private IP address with PSA. The subnet range reserved for the network attachment must be within RFC 1918 range. 
     2. Assigning the network attachment to your destination AlloyDB for PostgreSQL cluster. 

For more information, see [ Configure Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect) in the AlloyDB for PostgreSQL documentation. 

  5. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the private IP address of your source Cloud SQL for PostgreSQL instance. 
  6. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **PSC interface** for your connectivity method. 



## Configure private connectivity with VPC peering

Private connectivity with Virtual Private Cloud (VPC) peering connects your destination AlloyDB for PostgreSQL cluster to your source Cloud SQL for PostgreSQL instance across a shared VPC network configured for Private Services Access (PSA).

**Note:** Direct VPC peering connectivity requires that your source Cloud SQL for PostgreSQL instance uses the newer Private Services Access producer network architecture and is peered with the same VPC network as your destination AlloyDB for PostgreSQL cluster. If your source Cloud SQL instance uses the older producer network architecture or is peered with a different VPC network, you must instead deploy an intermediary TCP proxy VM. For instructions, see [ Configure connectivity using a TCP proxy through a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm). 

To use private connectivity with VPC peering, follow these steps:

  1. In your project, ensure you have a Virtual Private Cloud network with [ private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

You need sufficient allocated IP range space to support both your source Cloud SQL instance and your destination AlloyDB for PostgreSQL cluster. 

  2. Make sure your source Cloud SQL instance is configured with a private IP and Private Services Access (PSA) in the Virtual Private Cloud network described in the previous step. For more information, see [ Use private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip) in the Cloud SQL documentation. 
  3. Make sure your destination AlloyDB for PostgreSQL cluster is configured with Private Services Access (PSA) using the same Virtual Private Cloud network. For more information, see [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), select your source Cloud SQL for PostgreSQL instance and enter its private IP address. 

You can view your instance's **private IP address** when you [ view instance summary information](https://docs.cloud.google.com/sql/docs/postgres/instance-info). 

  5. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), use **VPC peering** for your connectivity method (in the Google Cloud console, Database Migration Service automatically selects **VPC peering** when your source Cloud SQL instance uses the newer producer network architecture). 



## Configure IP allowlist connectivity

To configure IP allowlist connectivity for Cloud SQL for PostgreSQL sources, follow these steps:

  1. Ensure that outbound public IP is enabled on your destination AlloyDB for PostgreSQL primary instance. For more information, see [ Enable outbound public IP](https://docs.cloud.google.com/alloydb/docs/connect-outbound-public-ip) in the AlloyDB for PostgreSQL documentation. 
  2. Enable public IP for your source Cloud SQL instance and add both outbound public IP addresses of your destination AlloyDB for PostgreSQL primary instance to the list of authorized networks. For more information, see [ Enable public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) in the Cloud SQL documentation. 

You can find the outbound public IP addresses of your destination AlloyDB for PostgreSQL primary instance on the cluster details page in the Google Cloud console. See [ View cluster and instance details](https://docs.cloud.google.com/alloydb/docs/instance-view). 

  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the public IP address of your source instance. 
  4. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **IP allowlist** for your connectivity method. 



## What's next

  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
