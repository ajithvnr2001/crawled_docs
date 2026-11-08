---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel/
title: Configure connectivity using reverse SSH tunnel \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:08:47.814250+00:00
---

# Configure connectivity using reverse SSH tunnel  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Configure connectivity using reverse SSH tunnel Stay organized with collections  Save and categorize content based on your preferences. 

You can establish connectivity from the destination AlloyDB for PostgreSQL cluster to the source database through a secure reverse SSH tunnel. This method requires a bastion host VM in the Google Cloud project as well as a machine (for example, a server or workstation on the source network) that has connectivity to the source database.

**Important:** If your source is within a VPN (in AWS, for example, or your own on-premises VPN), your source connection profile should use the VPN IP address and port instead of the public source IP address and port.

Database Migration Service collects the required information at migration job creation time and automatically generates a script for configuring the tunnel components.

![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH server.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/alloydb/alloydb_hmm_reverse_ssh.svg) **Figure 1.** Migration networking example: source connectivity over an SSH tunnel. (click to enlarge) ![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH server.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/alloydb/alloydb_hmm_reverse_ssh.svg)

## Set up a reverse SSH tunnel

The following steps are performed in the Database Migration Service flow when [ creating a migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job), to set up a reverse SSH tunnel between the source database and the destination AlloyDB for PostgreSQL cluster. After you provide some parameters, you execute a set of `gcloud` commands on a machine that has connectivity to both the source database and Google Cloud.

  1. In the **Connectivity method** drop-down menu, select **Proxy via cloud-hosted VM - Reverse-SSH tunnel**.

  2. Select the VM instance used to establish connectivity between the source database and the destination AlloyDB for PostgreSQL cluster. Typically this is a VM running in the VPC where the application accessing the AlloyDB for PostgreSQL database runs. The VM instance serves as the SSH tunnel bastion server.

  3. You can use an existing Compute Engine VM instance for this purpose:

     1. Choose the Compute Engine VM instance from the list.
     2. Provide a free port that the SSH tunnel can use.
**Note:** For the reverse SSH tunnel to work, set the `GatewayPorts` parameter to `yes` in the `/etc/ssh/sshd_config` file on the bastion server. After you update the file, restart the sshd service using the `sudo systemctl restart sshd.service` command. If you don't want to change the configuration of your existing VM, create a new VM instead. 
  4. Alternatively, you can create a new VM at this step. Select **CREATE A COMPUTE ENGINE VM INSTANCE** and the generated script includes instructions to create it.

     1. Provide a name for the VM instance.
     2. Select a machine type for the VM.
     3. Specify a subnet for the VM.
**Note:** A Compute Engine VM instance created by the script isn't managed by Database Migration Service. If one is created, your organization is charged for the instance based on standard pricing, and you're responsible for its management, including deleting the instance when it's no longer needed. 
  5. Click **VIEW SCRIPT** to view the generated script.

By default, the script generates a public IP address for the Compute Engine VM server. If you want the IP address to be private, perform the following steps:

     * Alter the `gcloud compute instances create` command by adding the [ `--no-address` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--address). 
     * Alter the `gcloud compute ssh` command by adding the [ `--internal-ip` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh#--internal-ip). 

Also, if you want to create a bastion host VM on a subnet that is on a shared VPC, alter the `export SUBNET_NAME` command from the generated script to point to `projects/project_name/regions/region_name/subnetworks/subnetwork_name`. 

For example:

`export SUBNET_NAME=projects/myproject/regions/myregion/subnetworks/mysubnetwork`

project_name is the name of the project where the shared VPC resides. region_name and subnetwork_name are the names of the region and subnetwork associated with the VPC project. 

**Note:** Make sure the replication connections section of the `pg_hba.conf` file (for self-hosted PostgreSQL) or the cloud security groups (for AWS RDS or Aurora) on the source database are updated to accept incoming connections on port `5432` from the bastion host VM IP address and the destination AlloyDB for PostgreSQL VPC network range. 
  6. **Run the script on a machine that has access to both the source database and the Compute Engine VM**. The script performs the following operations:

     * Configures the Compute Engine VM as an SSH tunnel bastion server.
     * Establishes a secure SSH connection forwarding traffic from the bastion host port to the source PostgreSQL database server (default port `5432`).
     * If you're creating a new Compute Engine VM, then after successfully running the script, copy the VM server IP address from the script output and enter it in the provided text field. The destination AlloyDB for PostgreSQL cluster configuration is updated as needed when you later test or start the migration job.
  7. Click **CONFIGURE & CONTINUE**.

  8. [ Verify your migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/verify-migration) to confirm that it correctly connects and migrates data from your source database instance to the destination AlloyDB for PostgreSQL cluster.

  9. Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) in the Cloud VPN documentation.

  10. After your migration job is configured, connectivity is verified, and VPNs are configured successfully if necessary, you can run the continuous migration job.




## What's next

  * To learn more about database network connectivity in Database Migration Service, see [ Networking methods overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with AlloyDB for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/get-started-with-alloydb-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
