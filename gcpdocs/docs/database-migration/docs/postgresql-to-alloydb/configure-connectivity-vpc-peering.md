---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/
title: Configure private IP connectivity \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:12:34.853034+00:00
---

# Configure private IP connectivity  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=de)
  * [Español](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=it)
  * [Português](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Configure connectivity using VPC peering](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#vpc-peering)
    * [Configuring private services access for Database Migration Service](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#configure-access)
    * [Allocating an IP address range](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#allocating_an_ip_address_range)
    * [Creating a private connection](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#creating_a_private_connection)
    * [Exporting custom routes](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#exporting_custom_routes)
    * [Granting the roles/servicenetworking.serviceAgent role](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#network-admin-role)
  * [Configure connectivity using Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#psc-interfaces)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)


Send feedback 
#  Configure private IP connectivity Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Configure connectivity using VPC peering](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#vpc-peering)
    * [Configuring private services access for Database Migration Service](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#configure-access)
    * [Allocating an IP address range](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#allocating_an_ip_address_range)
    * [Creating a private connection](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#creating_a_private_connection)
    * [Exporting custom routes](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#exporting_custom_routes)
    * [Granting the roles/servicenetworking.serviceAgent role](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#network-admin-role)
  * [Configure connectivity using Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#psc-interfaces)


  

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-vpc-peering) | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering) | PostgreSQL to AlloyDB
  
  
You can migrate your data over private networks by establishing connectivity between your source and destination databases private IP addresses. You can use one of the two approaches To configure private IP addresses for your destination database, you can use private services access or Private Service Connect. 
Each connection method offers distinct advantages and trade-offs. Make sure you choose the approach that best fits your scenario. For more information about private services access and Private Service Connect in AlloyDB for PostgreSQL, see [Private IP overview](https://docs.cloud.google.com/alloydb/docs/private-ip) in the AlloyDB for PostgreSQL documentation.
## Configure connectivity using VPC peering
VPC peering works by configuring the VPCs to communicate with one another. If your source is in the same Google Cloud project in AlloyDB or Compute Engine, then this allows the destination to communicate with the source directly. If your source is accessible with VPN, then configure the source network and Cloud VPN to communicate with each other with the VPN. For more information, see [ connecting VPCs through VPNs](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpns#vpc-vpn). 
VPC chaining isn't supported. If your source is in a different Google Cloud project, then see [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc) to learn how to connect resources from multiple projects to a common VPC network for VPC peering.
The source database server's firewall must be configured to allow the entire **internal IP range** allocated for the **private service connection** of the [VPC network that the AlloyDB destination instance is going to use](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job#dest).
To find the **internal IP range** in the console:
  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.
  2. Select the VPC network that you want to use.
  3. Select the **PRIVATE SERVICE CONNECTION** tab.

Make sure the replication connections section of the `pg_hba.conf` file or the security groups definitions in AWS RDS on the source database are updated to accept connections from the AlloyDB VPC's IP address range. 
VPC peering uses [private services access](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#configure-access), which must be configured once for each project using VPC peering. After you have established `private services access`, test your migration job to verify connectivity.
### Configuring private services access for Database Migration Service
If you are using private IP for any of your Database Migration Service instances, you only need to configure private services access one time for every Google Cloud project that has or needs to connect to a Database Migration Service instance.
Establishing private services access requires the [compute.networkAdmin](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#network-admin-role) IAM role. After private services access is established for your network, you no longer need the `compute.networkAdmin` IAM role to configure an instance to use private IP.
Private services access requires you to first allocate an internal IP address range, then create a private connection, and then export a custom route.
An allocated range is a reserved CIDR block that can't otherwise be used in your local VPC network. When you create a private connection, you specify an allocation. The private connection links your VPC network with the underlying ("service producer") VPC network.
When you create a private connection, the VPC network and service producer network exchange subnet routes only. You must export the VPC network's custom routes so that the service provider's network can import them and correctly route traffic to your on-premises network.
A peering configuration establishes the intent to connect to another VPC network. Your network and the other network are not connected until each one has a peering configuration for the other. After the other network has a corresponding configuration to peer with your network, the peering state changes to ACTIVE in both networks, and they are connected. If there's no matching peering configuration in the other network, the peering state remains INACTIVE, indicating that your network is not connected to the other one.
Once connected, the two networks always exchange subnet routes. You can optionally import both static and dynamic custom routes from a peered network if it has been configured to export them
There are two parts to the private services access configuration process:
  * Allocating an IP address range. The range encompasses all of your instances.
  * Creating a private connection from your VPC network to the service producer network.


### Allocating an IP address range
[Console](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#console)[gcloud](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#gcloud) More
  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.
  2. Select the VPC network that you want to use.
  3. Select the **Private service connection** tab.
  4. Select the **Allocated IP ranges for services** tab.
  5. Click **Allocate IP range**.
  6. For the **Name** of the allocated range, specify `google-managed-services-VPC_NETWORK_NAME`, where `VPC_NETWORK_NAME` is the name of the VPC network you are connecting (for example, `google-managed-services-default`). The **Description** is optional.
  7. Click **ALLOCATE** to create the allocated range.


Do one of the following:
  * To specify an address range and a prefix length (subnet mask), use the `addresses` and `prefix-length` flags. For example, to allocate the CIDR block `192.168.0.0/16`, specify `192.168.0.0` for the address and `16` for the prefix length.

```
gcloud compute addresses create google-managed-services-[VPC_NETWORK_NAME] \
    --global \
    --purpose=VPC_PEERING \
    --addresses=192.168.0.0 \
    --prefix-length=16 \
    --network=[VPC_NETWORK_NAME]

```

  * To specify a prefix length (subnet mask) only, just use the `prefix-length` flag. When you omit the address range, Google Cloud automatically selects an unused address range in your VPC network. The following example selects an unused IP address range with a `16` bit prefix length.

```
gcloud compute addresses create google-managed-services-[VPC_NETWORK_NAME] \
    --global \
    --purpose=VPC_PEERING \
    --prefix-length=16 \
    --network=[VPC_NETWORK_NAME]

```



Replace `[VPC_NETWORK_NAME]` with the name of your VPC network, such as `my-vpc-network`.
The following example allocates an IP range that allows resources in the VPC network `my-vpc-network` to connect to Database Migration Service instances using private IP.

```
gcloud compute addresses create google-managed-services-my-vpc-network \
    --global \
    --purpose=VPC_PEERING \
    --prefix-length=16 \
    --network=my-vpc-network \
    --project=my-project

```

### Creating a private connection
[Console](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#console)[gcloud](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#gcloud) More
  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.
  2. Select the VPC network that you want to use.
  3. Select the **Private service connection** tab.
  4. Select the **Private connections to services** tab.
  5. Click **Create connection** to create a private connection between your network and a service producer.
  6. For the **Assigned allocation** , select one or more existing allocated ranges that aren't being used by other service producers, and then click **OK**.
  7. Click **CONNECT** to create the connection.


  1. Create a private connection.

```
gcloud services vpc-peerings connect \
    --service=servicenetworking.googleapis.com \
    --ranges=google-managed-services-[VPC_NETWORK_NAME] \
    --network=[VPC_NETWORK_NAME] \
    --project=[PROJECT_ID]

```

Replace `[VPC_NETWORK_NAME]` with the name of your VPC network and `[PROJECT_ID]` with the ID of the project that contains your VPC network.
The command initiates a long-running operation, returning an operation name.
  2. Check whether the operation was successful.

```
gcloud services vpc-peerings operations describe \
    --name=[OPERATION_NAME]

```

Replace `[OPERATION_NAME]` with the operation name that was returned from the previous step.


You can specify more than one allocated range when you create a private connection. For example, if a range has been exhausted, you can assign additional allocated ranges. The service uses IP addresses from all the provided ranges in the order that you specified.
### Exporting custom routes
Update an existing VPC Network Peering connection to change whether your VPC network exports or imports custom routes to or from the peer VPC network.
Your network imports custom routes only if the peer network is also exporting custom routes, and the peer network receives custom routes only if it imports them.
[ Console ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#console)[ gcloud ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/#gcloud) More
  1. Go to the VPC Network Peering page in the Google Cloud console.   
[Go to the VPC Network Peering page](https://console.cloud.google.com/networking/vpc-connectivity/peering)
  2. Select the peering connection to update.
  3. Click **EDIT**.
  4. Update your custom route settings by selecting or deselecting **Import custom routes** or **Export custom routes**.
  5. Click **SAVE**.


Update the peering connection to change your import or export settings for custom routes.

```
gcloud compute networks peerings update [PEERING-NAME] \
    --network=[MY-LOCAL-NETWORK] \
    [--[no-]import-custom-routes] \
    [--[no-]export-custom-routes]

```

### Granting the `roles/servicenetworking.serviceAgent` role

```
  gcloud beta services identity create \
    --service=servicenetworking.googleapis.com \
    --project=project-id

```

```
  gcloud projects add-iam-policy-binding project-id \
    --member="service-account-prefix@service-networking.iam.gserviceaccount.com" \
    --role="roles/servicenetworking.serviceAgent"

```

## Configure connectivity using Private Service Connect interfaces
For homogeneous AlloyDB for PostgreSQL migrations, AlloyDB for PostgreSQL can use Private Service Connect interfaces to establish a connection over private networks. This connectivity method is only available when you [migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance).
To use Private Service Connect interfaces, do the following:
  1. Create an AlloyDB for PostgreSQL cluster enabled for Private Service Connect, and a primary instance in that cluster. See [Enable Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#enable-psc) in the AlloyDB for PostgreSQL documentation.
  2. Configure Private Service Connect for outbound connectivity on your instance. See [Configure outbound connectivity](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#configure-outbound-connectivity) in the AlloyDB for PostgreSQL documentation.
Make sure that the VPC network where you create the network attachment is the network where you can reach the private IP address of your source database.
  3. At a later stage, when you [create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance), select **PSC interface** for your connectivity method.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
