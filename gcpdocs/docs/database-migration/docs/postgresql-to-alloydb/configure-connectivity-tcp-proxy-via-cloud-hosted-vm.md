---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm/
title: Configure connectivity using a TCP proxy through a cloud-hosted VM \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T09:54:18.404300+00:00
---

# Configure connectivity using a TCP proxy through a cloud-hosted VM  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Configure connectivity using a TCP proxy through a cloud-hosted VM Stay organized with collections  Save and categorize content based on your preferences. 

You can use a TCP proxy on a Compute Engine Virtual Machine (VM) when you want to establish private connectivity over Virtual Private Cloud (VPC) peering, but non-transitive VPC peering prevents direct routing between your source database and your destination AlloyDB for PostgreSQL cluster (for example, when migrating from a Cloud SQL for PostgreSQL instance that uses the older producer network architecture, or from a self-hosted source database in a separate VPC network). For a conceptual overview of how this method works, see [ TCP proxy through a cloud-hosted VM](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods) in the networking methods overview.

![An architecture diagram for a private database connection that uses the TCP proxy VM.](https://docs.cloud.google.com/static/database-migration/docs/images/tcp-proxy-diagram-vpc.svg) **Figure 1.** Connectivity example: TCP proxy used for routing traffic between source databases and destination AlloyDB for PostgreSQL clusters. (click to enlarge) ![An architecture diagram for a private database connection that uses the TCP proxy VM.](https://docs.cloud.google.com/static/database-migration/docs/images/tcp-proxy-diagram-vpc.svg)

When you create a continuous migration job in the Google Cloud console, Database Migration Service collects the required parameters and generates a `gcloud` script that creates a Compute Engine container VM running the TCP proxy and a firewall rule allowing incoming TCP traffic on port `5432` from the destination AlloyDB for PostgreSQL cluster to the proxy VM.

## Set up the TCP proxy VM

In the Google Cloud console, when you [ set up connectivity between the source and destination](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job), perform the following steps:

  1. In the **Connectivity method** drop-down menu, select **Proxy via cloud-hosted VM - TCP**.

  2. Specify the following configuration parameters for the Compute Engine instance that serves as the proxy bastion host: 

     * **Compute Engine VM instance name** : A unique name for the proxy VM instance.
     * **Machine type** : The Compute Engine machine type (for example, `e2-standard-2` or `n1-standard-1`).
     * **Subnetwork** : The subnet of your VPC network that connects to the destination cluster.
**Note:** The Compute Engine VM instance created by the script isn't managed by Database Migration Service. Your organization is charged for the instance based on standard [Compute Engine pricing](https://docs.cloud.google.com/database-migration/pricing), and you're responsible for its management, including deleting the instance when it's no longer needed. 
  3. Click **View script** to review the generated deployment script.

**Key point:** By default, the script generates a public IP address for the Compute Engine VM. If your organization doesn't permit creating a VM with a public IP address, or you require strict private IP isolation, perform the following steps: 
     1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) on the subnet used for the proxy. This is required to allow the Compute Engine instance to download the necessary proxy container images from Artifact Registry or Container Registry. 
     2. Append the `no-address` key to the `--network-interface` flag of the [`gcloud compute instances create-with-container`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container) command in the script: 

`gcloud compute instances create-with-container ... --network-interface subnet=SUBNET_NAME,no-address`

If your source database resides in a different VPC network or Shared VPC than the destination AlloyDB for PostgreSQL cluster, you can also attach an additional network interface to the proxy VM by adding a second `--network-interface` flag to the `gcloud compute instances create-with-container` command (using a machine type with sufficient vCPUs to support multiple network interfaces): 

`--network-interface network=SOURCE_NETWORK_NAME,subnet=SOURCE_SUBNET_NAME,no-address`

  4. Run the script on a machine that has administrative access to your Google Cloud project.

  5. Ensure that the source database network settings are updated to accept connections from the outgoing IP address of the TCP proxy VM:

     * For self-hosted PostgreSQL: Update the replication section in `pg_hba.conf`.
     * For Cloud SQL for PostgreSQL: Add the proxy VM's internal IP address to the authorized networks or ensure VPC routing permits the traffic.
  6. Click **Configure & continue**.

  7. [ Test and create your migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job) to verify that the destination AlloyDB for PostgreSQL primary instance can reach the source database through the proxy VM.




## What's next

  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
