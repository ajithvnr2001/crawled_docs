---
url: https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/
title: Configure network connectivity for Cloud SQL for PostgreSQL sources \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:52:19.616013+00:00
---

# Configure network connectivity for Cloud SQL for PostgreSQL sources  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdatabase-migration%2Fdocs%2Fpostgres%2Fconfigure-src-connection-csql-postgres%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Configure Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#private-psc-interfaces)
  * [Configure specialized VPC peering](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#private-vpc-peering)
  * [Configure IP allowlist connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#ip-allowlist)
  * [What's next](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)


Was this helpful?
Send feedback 
#  Configure network connectivity for Cloud SQL for PostgreSQL sources Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Configure Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#private-psc-interfaces)
  * [Configure specialized VPC peering](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#private-vpc-peering)
  * [Configure IP allowlist connectivity](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#ip-allowlist)
  * [What's next](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#whats_next)


This page describes how to configure network connectivity for Cloud SQL for PostgreSQL sources for homogeneous migrations to Cloud SQL for PostgreSQL migrations with Database Migration Service. There are several different methods you can use:
  * [ Private IP connectivity with Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#private-psc-interfaces)
  * [ Private IP connectivity with specialized Virtual Private Cloud peering](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#private-vpc-peering)
  * [ Public IP allowlist](https://docs.cloud.google.com/database-migration/docs/postgres/configure-src-connection-csql-postgres/#ip-allowlist)


For homogeneous migrations between two Cloud SQL for PostgreSQL instances with Database Migration Service, we don't recommend using the reverse-SSH tunnel connectivity method.
## Configure Private Service Connect interfaces
This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering). Private Service Connect interfaces are only available when you [ migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance).
To use private connectivity with Private Service Connect interfaces, follow these steps:
  1. In your project, ensure you have a Virtual Private Cloud network with [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 
This is the network that you peer with Database Migration Service and your source database server. You need to have enough space to allocate IP ranges for both components. 
  2. Make sure your source Cloud SQL instance is configured with a private IP and Private Service Access (PSA) with the VPC network described in the previous step. For more information, see [ Use private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#configure_an_instance_to_use_private_ip) in the Cloud SQL documentation. 
  3. Create a destination Cloud SQL instance enabled for Private Service Connect. See [ Create a Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-cloud-sql-instance-psc-enabled-2) in the Cloud SQL documentation. 
  4. Configure Private Service Connect for outbound connectivity on your destination instance. At a high level, this process involves: 
    1. Creating a network attachment in the VPC network where your source instance has a private IP address with PSA. Note that the subnet range reserved for the network attachment must be within RFC 1918 range. 
    2. Assigning the network attachment to your destination Cloud SQL for PostgreSQL instance. 
For the full process, see [ Configure outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#configure-outbound-connectivity) in the Cloud SQL documentation. 
  5. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles) use the private IP address of your source Cloud SQL for PostgreSQL instance. 
  6. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/about-migration-jobs) select **PSC interface** for your connectivity method. 


## Configure specialized VPC peering
Private connectivity with Cloud SQL for PostgreSQL sources for heterogeneous migrations uses Virtual Private Cloud (VPC) peering to create a connection between Database Migration Service and your source database over VPC networks in Google Cloud. Transitive peering isn't supported, so for this connectivity method to work, you need to set up a reverse proxy Virtual Machine (VM) in your Virtual Private Cloud network.
To use private connectivity with VPC peering, follow these steps:
  1. In your project, ensure you have a Virtual Private Cloud network with [ Virtual Private Cloud network with private services access enabled](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 
This is the network that you peer with Database Migration Service and your source database server. You need to have enough space to allocate IP ranges for both components. 
  2. Make sure your source Cloud SQL instance is configured with a private IP and Private Service Access (PSA) with the VPC network described in the previous step. For more information, see [ Use private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#configure_an_instance_to_use_private_ip) in the Cloud SQL documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles), do the following: 
    1. In the **Define connection details** section, enter the private IP of your source Cloud SQL instance. 
You can view your instance's **private IP address** when you [ view instance summary information](https://docs.cloud.google.com/sql/docs/postgres/instance-info). 
    2. In the **Define connectivity method** section, select **Private connectivity**. 
    3. From the drop-down menu, select the private connectivity configuration you created in the previous step. 


## Configure IP allowlist connectivity
To configure IP allowlist connectivity for Cloud SQL for PostgreSQL sources, follow these steps:
  1. Enable public IP for your source Cloud SQL instance and add the outbound public IP of your destination instance to the list of authorized networks. For more information, see [ Enable public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) in the Cloud SQL documentation. 
If you are migrating to a new destination instance, make sure to create the destination with a public IP enabled. 
  2. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles) use the public IP address of your source instance. 
  3. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/about-migration-jobs) select **IP allowlist** for your connectivity method. 


## What's next
  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods).
  * To get a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
