---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-src-connection-aws/
title: Configure network connectivity for Amazon Aurora and Amazon RDS sources \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:08:05.113719+00:00
---

# Configure network connectivity for Amazon Aurora and Amazon RDS sources  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-src-connection-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Configure network connectivity for Amazon Aurora and Amazon RDS sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity for Amazon Aurora and Amazon RDS sources for homogeneous PostgreSQL migrations to AlloyDB for PostgreSQL clusters with Database Migration Service. There are several methods you can use:

  * Private IP connectivity with Private Service Connect interfaces

  * Private IP connectivity with Virtual Private Cloud peering

  * Public IP allowlist




You can also use a [ reverse-SSH tunnel](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel), but this approach requires creating an intermediate Compute Engine Virtual Machine (VM) to host the necessary network components.

## Configure Private Service Connect interfaces

This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering-quotas). Private Service Connect interfaces are the recommended method for private IP connectivity when migrating to an AlloyDB for PostgreSQL cluster. Private Service Connect interfaces are supported when you [ migrate to an existing AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance).

To use private connectivity with Private Service Connect interfaces for Amazon RDS or Amazon Aurora sources, follow these steps:

  1. Set up direct connectivity with Cloud VPN from Google Cloud to your source VPC in AWS. 

Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) in the Cloud VPN documentation. 

  2. Create or select a destination AlloyDB for PostgreSQL cluster enabled for Private Service Connect. See [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  3. Configure Private Service Connect for outbound connectivity from your destination cluster. At a high level, this process involves: 
     1. Creating a network attachment in the Virtual Private Cloud network where you set up your Cloud VPN. The subnet range reserved for the network attachment must be within RFC 1918 range. 
     2. Assigning the network attachment to your destination AlloyDB for PostgreSQL cluster. 

For more information, see [ Configure Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect) in the AlloyDB for PostgreSQL documentation. 

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the private IP address or private DNS endpoint of your source database instance in AWS. 
  5. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **PSC interface** for your connectivity method. 



## Configure VPC peering

To use private connectivity with Virtual Private Cloud peering for Amazon RDS or Amazon Aurora sources, follow these steps:

  1. Set up direct connectivity with Cloud VPN from Google Cloud to your source VPC in AWS. 

Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) in the Cloud VPN documentation. 

Ensure the Virtual Private Cloud network is configured for private services access. For more information, see [ Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

  2. Make sure your destination AlloyDB for PostgreSQL cluster is configured with a private IP and Private Services Access (PSA) using the same Virtual Private Cloud network. For more information, see [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the private IP address of your source database instance. 
  4. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **VPC Peering** for your connectivity method. 



## Configure IP allowlist connectivity

To use the public IP allowlist connectivity method, follow these steps:

  1. In the AWS Management Console, perform the following steps: 
     1. Ensure that your source Amazon RDS or Amazon Aurora database is configured for public IP connections. 
     2. Identify the database endpoint name and port number. You need to enter these values when you create the connection profile. 

PostgreSQL servers by default use port `5432`.

  2. Ensure that outbound public IP is enabled on your destination AlloyDB for PostgreSQL primary instance, and check both of its outbound public IP addresses. For more information, see [ Enable outbound public IP](https://docs.cloud.google.com/alloydb/docs/connect-outbound-public-ip) and [ View cluster and instance details](https://docs.cloud.google.com/alloydb/docs/instance-view). 
  3. In your AWS VPC, create or update a security group that allows inbound traffic on port `5432` from both outbound public IP addresses of your destination AlloyDB for PostgreSQL primary instance. See [ Provide access to your DB instance in your VPC by creating a security group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html#CHAP_SettingUp.SecurityGroup) in the AWS documentation. 

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the endpoint name for the source database IP or hostname. 
  5. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **IP allowlist** for your connectivity method. 



## What's next

  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
