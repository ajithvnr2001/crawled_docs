---
url: https://docs.cloud.google.com/oracle/database/docs/create-odb-network/
title: Create ODB Network and ODB Subnets \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:19:14.312367+00:00
---

# Create ODB Network and ODB Subnets  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/create-odb-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Create ODB Network and ODB Subnets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an ODB Network and ODB Subnets in Google Cloud.

An ODB Network provides connectivity between Oracle Database@Google Cloud resources in the Oracle Cloud Infrastructure (OCI) child site and your Google Cloud VPC network. The ODB Network maps OCI network resources, such as Virtual Cloud Networks (VCNs), and their related subnets back to Google Cloud.

When you create an ODB Network, Oracle Database@Google Cloud automatically provisions all of the underlying components that are required to establish this connectivity. This includes the VCN, subnets, DNS zones, and the other objects that maintain the private connection between Google Cloud and the OCI child site.

Oracle Database@Google Cloud also lets you create up to five ODB Subnets within an ODB Network for the ease of network management.

You can also enable service connectivity on an ODB Network to be used with Database Connections to execute SQL statements on your databases. You can either create a new ODB Network with service connectivity enabled or enable service connectivity on an existing ODB Network.

## Before you begin

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to create an ODB Network and ODB Subnets as described in [Deploy Oracle Database@Google Cloud environment](https://docs.cloud.google.com/oracle/database/docs/setup-oracle-database-environment#deploy-odb-environment).

  * If you plan to use your ODB Network with Database Connections to execute SQL statements on your databases, [Create a network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments).

To execute SQL statements, Oracle Database@Google Cloud uses Private Service Connect to connect to the databases. Therefore, the ODB Network must reference a network attachment in the same region.

When creating the network attachment, consider the following:

    * The network attachment must be in the same region as the ODB Network.
    * The network attachment must reference a subnet in your VPC network.
    * The network attachment must accept the Oracle Database service.
    * You can't change the network attachment once set. You must remove it and set a new one or create a new ODB Network.

Set `connection_preference = ACCEPT_AUTOMATIC`.

To use an ODB Network with a Database Connection, you must have the following permissions on your ODB Network:

    * `oracledatabase.odbNetworks.use`
    * `oracledatabase.odbNetworks.get`

The ODB Network Admin (`roles/oracledatabase.odbNetworkAdmin`) and Network Admin (`roles/oracledatabase.networkAdmin`) roles contain these permissions.




## Create an ODB Network

An ODB Network must be created in the Google Cloud project that is associated to the billing account that you used for your marketplace order. In the case of a Shared VPC deployment, this project is also your host project and contains the Shared VPC network as well.

You must create the ODB Network in the same region and zone where you plan to create your Exadata Infrastructure, Exadata VM Cluster, or DB system. This ensures optimal performance and seamless communication.

To create an ODB Network, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click **Create**.

  3. From the **Associated network** list, select a VPC network which you want to associate with the ODB Network.

  4. Select a **Region** and a **GCP Oracle zone**.

The region and zone choice is permanent and can't be changed later. If you aren't sure about which zone to select, you can select `Any` and Google Cloud automatically chooses a zone for you.

  5. Enter a name for the ODB network.

  6. Optional. If you want to use this ODB Network with a Database Connection to execute SQL statements on your databases, then in the **Google Cloud service connectivity** section, do the following:

**Note:** You can also [enable service connectivity](https://docs.cloud.google.com/oracle/database/docs/create-odb-network#enable-service-connectivity) later after creating the ODB Network.
     1. To enable service connectivity, click the **Private Service Connect (PSC) interface** toggle to the on position.

     2. From the **Network attachment** , select a network attachment.

  7. Click **Create**.




### gcloud

Use the `gcloud oracle-database odb-networks create` command to create an ODB Network.
    
    
    gcloud oracle-database odb-networks create ODB_NETWORK_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --network=projects/PROJECT_ID/global/networks/VPC_NETWORK \
        --gcp-oracle-zone=GCP_ORACLE_ZONE \
        --psc-interface-config-network-attachment=projects/PROJECT_ID/regions/REGION/networkAttachments/NETWORK_ATTACHMENT_ID
    

Replace the following:

  * ODB_NETWORK_ID: a unique identifier for your ODB Network.
  * PROJECT_ID: the ID of your Google Cloud project in which to create the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region in which to create the ODB Network.
  * VPC_NETWORK: the ID of the VPC network which you want to associate with the ODB Network.
  * GCP_ORACLE_ZONE: the GCP Oracle zone in which to create the ODB Network.
  * For `psc-interface-config-network-attachment` property, replace the following:

**Important:** Only configure `psc-interface-config-network-attachment` if you intend to associate this ODB Network with a Database Connection to execute SQL on the database. Otherwise, you can skip this configuration.
    * PROJECT_ID: the ID of the Google Cloud project that contains the network attachment.
    * REGION: the region where your network attachment is located.
    * NETWORK_ATTACHMENT_ID: the ID of the network attachment.



###  API 

To create an ODB Network, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID"
    -d \
    '{
      "network": "projects/PROJECT_ID/global/networks/VPC_NETWORK",
      "gcpOracleZone": "GCP_ORACLE_ZONE"
      "serviceConnectivityConfig": {
        "pscInterfaceConfig": {
          "networkAttachment": "projects/PROJECT_ID/regions/REGION/networkAttachments/NETWORK_ATTACHMENT_ID"
        }
      }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region in which to create the ODB Network.
  * ODB_NETWORK_ID: a unique identifier for your ODB Network.
  * VPC_NETWORK: the ID of the VPC network which you want to associate with the ODB Network.
  * GCP_ORACLE_ZONE: the GCP Oracle zone in which to create the ODB Network.
  * For `networkAttachment` and `pscInterfaceConfig` properties in `serviceConnectivityConfig`, replace the following:

**Important:** Only configure `pscInterfaceConfig` and `networkAttachment` properties if you intend to associate this ODB Network with a Database Connection to execute SQL on the database. Otherwise, you can skip this configuration.
    * PROJECT_ID: the ID of the Google Cloud project that contains the network attachment.
    * REGION: the region where your network attachment is located.
    * NETWORK_ATTACHMENT_ID: the ID of the network attachment.



After you create the ODB Network, you can create ODB Subnets and custom DNS domains.

## Create an ODB Subnet

You can create two types of ODB Subnets:

  * Client ODB Subnets to connect to applications.
  * Backup ODB Subnets to back up database services.



For an ODB Network, you can create up to five ODB Subnets. A single Client ODB Subnet can be used by both Autonomous AI Databases and Exadata VM Clusters.

The number of ODB Subnets required depends on which service you want to use:

  * A Exadata VM Cluster requires one client subnet and one backup subnet.
  * An Autonomous AI Database requires one client subnet.



To create a subnet, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the ODB Network for which you want to create the subnet.

  3. On the **ODB Network details** page, go to the **Subnets** section, and click **Create**.

  4. On **Create ODB Subnet** page, do the following:

     1. Enter a name for the subnet.

     2. Enter a range for the subnet in CIDR notation.

     3. Select the **Subnet type**.

     4. Click **Create**.




### gcloud

Use the `gcloud oracle-database odb-networks odb-subnets create` command to create an ODB Subnet.
    
    
    gcloud oracle-database odb-networks odb-subnets create ODB_SUBNET_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --odb-network=ODB_NETWORK_ID \
        --cidr-range=CIDR_RANGE \
        --purpose=PURPOSE
    

Replace the following:

  * ODB_SUBNET_ID: a unique identifier for your ODB Subnet.
  * PROJECT_ID: the ID of your Google Cloud project in which to create the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region in which to create the ODB Subnet.
  * ODB_NETWORK_ID: the ID of your ODB Network for which you're creating the ODB Subnet.
  * CIDR_RANGE: To create a client subnet, provide the IPv4 address or address range that can access your cluster. If you're creating a backup subnet, then provide the IPv4 address or address range that serves as backup to access your cluster.

Address ranges must use a valid [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) (for example, 10.10.10.0/24).

  * PURPOSE: the type of the ODB Subnet that you want to create. The accepted values are `client_subnet` or `backup_subnet`.




###  API 

To create an ODB Subnet, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/ODB_SUBNET_ID"
    -d \
    '{
      "cidr_range": "CIDR_RANGE",
      "purpose": "PURPOSE"
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project that contains your ODB Network for which you want to create an ODB Subnet. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.
  * ODB_NETWORK_ID: the ID of your ODB Network for which you're creating the ODB Subnet.
  * ODB_SUBNET_ID: a unique identifier for your ODB Subnet.
  * CIDR_RANGE: To create a client subnet, provide the IPv4 address or address range that can access your cluster. If you're creating a backup subnet, then provide the IPv4 address or address range that serves as backup to access your cluster.

Address ranges must use a valid [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) (for example, 10.10.10.0/24).

  * PURPOSE: the type of the ODB Subnet that you want to create. The accepted values are `client_subnet` or `backup_subnet`.




## Enable service connectivity on an existing ODB Network

To use Database Connections to execute SQL statements on your databases, you can enable service connectivity on an existing ODB Network by updating it. Oracle Database@Google Cloud uses Private Service Connect to establish private connectivity to the database.

If you don't intend to associate this ODB Network with a Database Connection, don't enable service connectivity.

Before enabling service connectivity, ensure that you have created a network attachment as described in Before you begin.

Consider the following:

  * You can't change the network attachment once set. You must remove it and set a new one or create a new ODB Network.
  * You can't disable service connectivity if any Database Connection is using the ODB Network.
  * Enabling service connectivity might take several minutes. Wait for the enable operation to complete before creating or using Database Connection.



To enable service connectivity on an existing ODB Network, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the name of the ODB Network for which you want to enable service connectivity.

  3. On the **ODB Network details** page, go to the **Google Cloud service connectivity** section, and click **Manage**.

  4. On the **Google Cloud service connectivity** page, click the **Private Service Connect (PSC) interface** toggle to the on position.

  5. Click **Save**.




### gcloud

Run the `gcloud oracle-database odb-networks update` command.
    
    
    gcloud oracle-database odb-networks update ODB_NETWORK_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --psc-interface-config-network-attachment=projects/PROJECT_ID/regions/REGION/networkAttachments/NETWORK_ATTACHMENT_ID
    

Replace the following:

  * ODB_NETWORK_ID: the ID of your ODB Network.
  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.
  * For `psc-interface-config-network-attachment` property, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project that contains the network attachment.
    * REGION: the region where your network attachment is located.
    * NETWORK_ATTACHMENT_ID: the ID of the network attachment.



###  API 

Run the following `curl` command:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID"
    -d \
    '{
      "serviceConnectivityConfig": {
        "pscInterfaceConfig": {
          "networkAttachment": "projects/PROJECT_ID/regions/REGION/networkAttachments/NETWORK_ATTACHMENT_ID"
        }
      }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region in which to create the ODB Network.
  * ODB_NETWORK_ID: the ID of your ODB Network.
  * For `networkAttachment` and `pscInterfaceConfig` properties in `serviceConnectivityConfig`, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project that contains the network attachment.
    * REGION: the region where your network attachment is located.
    * NETWORK_ATTACHMENT_ID: the ID of the network attachment.



## Disable service connectivity on an existing ODB Network

If a Database Connection is using the ODB Network, then you can't disable service connectivity. First, delete the Database Connection, and then disable service connectivity.

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the name of the ODB Network for which you want to disable service connectivity.

  3. On the **ODB Network details** page, go to the **Google Cloud service connectivity** section, and click **Manage**.

  4. On the **Google Cloud service connectivity** page, click the **Private Service Connect (PSC) interface** toggle to the off position.

  5. Click **Save**.




### gcloud

Run the `gcloud oracle-database odb-networks update` command.
    
    
    gcloud oracle-database odb-networks update ODB_NETWORK_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --clear-service-connectivity-config
    

Replace the following:

  * ODB_NETWORK_ID: the ID of your ODB Network.
  * PROJECT_ID: the ID of your Google Cloud project which contains the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region of your ODB Network.



###  API 

Run the following `curl` command:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID?updateMask=serviceConnectivityConfig"
    -d '{}'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region in which to create the ODB Network.
  * ODB_NETWORK_ID: the ID of your ODB Network.
  * For `networkAttachment` and `pscInterfaceConfig` properties in `serviceConnectivityConfig`, replace the following:

    * PROJECT_ID: the ID of the Google Cloud project that contains the network attachment.
    * REGION: the region where your network attachment is located.
    * NETWORK_ATTACHMENT_ID: the ID of the network attachment.



## What's next

  * [Create custom DNS domains](https://docs.cloud.google.com/oracle/database/docs/create-manage-custom-dns).
  * [Create Exadata Infrastructure](https://docs.cloud.google.com/oracle/database/docs/create-instances).
  * [Create Exadata VM Cluster](https://docs.cloud.google.com/oracle/database/docs/create-clusters).
  * [Create Autonomous AI Database](https://docs.cloud.google.com/oracle/database/docs/create-databases).
  * [Create Database Connections](https://docs.cloud.google.com/oracle/database/docs/create-database-connection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
