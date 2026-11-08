---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-src-connection-self-hosted/
title: Configure network connectivity to self-hosted PostgreSQL sources \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:08:46.267091+00:00
---

# Configure network connectivity to self-hosted PostgreSQL sources  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-src-connection-self-hosted/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Configure network connectivity to self-hosted PostgreSQL sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity to self-hosted PostgreSQL sources for homogeneous PostgreSQL to AlloyDB for PostgreSQL migrations with Database Migration Service.

There are several methods you can use to configure the necessary network connectivity for migrations from self-hosted PostgreSQL sources:

  * Public IP allowlist
  * Private IP connectivity with Private Service Connect interfaces
  * Private IP connectivity with Virtual Private Cloud peering



You can also use a [ reverse-SSH tunnel](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel) or a [ TCP proxy through a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm), but these approaches require creating an intermediate Compute Engine Virtual Machine (VM) to host the necessary network components.

## Configure IP allowlist connectivity

To use the public IP allowlist connectivity method, follow these steps:

  1. Ensure that your source database has an IP address that can be reached from the public internet. You don't need to use the IP address to connect. If you have a DNS record associated with the IP, you can use that instead. 
  2. Ensure that outbound public IP is enabled on your destination AlloyDB for PostgreSQL primary instance. For more information, see [ Enable outbound public IP](https://docs.cloud.google.com/alloydb/docs/connect-outbound-public-ip) in the AlloyDB for PostgreSQL documentation. 
  3. Create an inbound firewall rule on your source database server or network perimeter to accept connections from both outbound public IP addresses of your destination AlloyDB for PostgreSQL primary instance. Use the following configuration: 
     1. For the rule type, use `port`.
     2. For the allowed IP address range, add both outbound public IP addresses of your destination AlloyDB for PostgreSQL primary instance. You can check the outbound IP addresses of your primary instance on the cluster details page in the Google Cloud console. See [ View cluster and instance details](https://docs.cloud.google.com/alloydb/docs/instance-view) in the AlloyDB for PostgreSQL documentation. 
     3. Set the protocol to `TCP`.
     4. Set the port number associated with the rule to the port where your source database is listening for incoming connections. This is the same port number that you need to enter in the source connection profile. 

PostgreSQL servers by default use the `5432` port. 

The steps for configuring firewall rules differ depending on what server software or firewall appliance you use. For more information, refer to the documentation of your firewall product. 

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), enter the public IP address or hostname of your source database. 
  5. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **IP allowlist** for your connectivity method. 



## Configure Private Service Connect interfaces

This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering-quotas). Private Service Connect interfaces are the recommended method for private IP connectivity when migrating to an AlloyDB for PostgreSQL cluster. Private Service Connect interfaces are supported when you [ migrate to an existing AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance).

### For self-hosted sources in Google Cloud

To use private connectivity with Private Service Connect interfaces for a source PostgreSQL database hosted on a Compute Engine VM, follow these steps:

  1. Create or select a destination AlloyDB for PostgreSQL cluster enabled for Private Service Connect. See [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  2. Configure Private Service Connect for outbound connectivity from your destination cluster. At a high level, this process involves: 
     1. Creating a network attachment in the Virtual Private Cloud network where you can reach the private IP address of your source database. The subnet range reserved for the network attachment must be within RFC 1918 range. 
     2. Assigning the network attachment to your destination AlloyDB for PostgreSQL cluster. 

For more information, see [ Configure Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect) in the AlloyDB for PostgreSQL documentation. 

  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the IP address of the Compute Engine VM where you host the PostgreSQL database. 

You can [ view the IP address of the VM](https://docs.cloud.google.com/compute/docs/instances/view-ip-address) in the Google Cloud console. 

  4. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **PSC interface** for your connectivity method. 



### For self-hosted sources outside Google Cloud

To use private connectivity with Private Service Connect interfaces for a self-hosted PostgreSQL source database that resides in a network outside Google Cloud, follow these steps:

  1. Set up direct connectivity with Cloud VPN from Google Cloud to your PostgreSQL source network. 

Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) in the Cloud VPN documentation. 

  2. Create or select a destination AlloyDB for PostgreSQL cluster enabled for Private Service Connect. See [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  3. Configure Private Service Connect for outbound connectivity from your destination cluster. At a high level, this process involves: 
     1. Creating a network attachment in the Virtual Private Cloud network where you can reach the private IP address of your source database. The subnet range reserved for the network attachment must be within RFC 1918 range. 
     2. Assigning the network attachment to your destination AlloyDB for PostgreSQL cluster. 

For more information, see [ Configure Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect) in the AlloyDB for PostgreSQL documentation. 

  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the private IP address of your source database instance. 
  5. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **PSC interface** for your connectivity method. 



## Configure private connectivity with VPC peering

This connectivity method requires that your source database IP address or hostname can be reached from your Google Cloud VPC. Self-hosted sources that reside in networks outside Google Cloud require that you use additional network components such as Cloud VPN or Cloud Interconnect.

### For self-hosted sources in Google Cloud

To use private connectivity with Virtual Private Cloud peering for a source PostgreSQL database hosted on a Compute Engine VM, follow these steps:

  1. Ensure the Virtual Private Cloud network where your VM has an IP address assigned is configured for private services access. For more information, see [ Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 
  2. Make sure your destination AlloyDB for PostgreSQL cluster is configured with a private IP and Private Services Access (PSA) using the same Virtual Private Cloud network. For more information, see [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the IP address of the Compute Engine VM where you host the PostgreSQL database. 

You can [ view the IP address of the VM](https://docs.cloud.google.com/compute/docs/instances/view-ip-address) in the Google Cloud console. 

  4. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **VPC Peering** for your connectivity method. 



### For self-hosted sources outside Google Cloud

To use private connectivity with Virtual Private Cloud peering for a self-hosted PostgreSQL source database that resides in a network outside Google Cloud, follow these steps:

  1. Set up direct connectivity with Cloud VPN to your PostgreSQL source network. 

Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) in the Cloud VPN documentation. 

Ensure the Virtual Private Cloud network is configured for private services access. For more information, see [ Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). 

  2. Make sure your destination AlloyDB for PostgreSQL cluster is configured with a private IP and Private Services Access (PSA). For more information, see [ Create a cluster and primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) in the AlloyDB for PostgreSQL documentation. 
  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-connection-profiles), use the private IP address of your source database instance. 
  4. When you [ create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/about-migration-jobs), select **VPC Peering** for your connectivity method. 



## What's next

  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
