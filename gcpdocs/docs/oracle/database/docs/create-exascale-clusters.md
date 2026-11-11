---
url: https://docs.cloud.google.com/oracle/database/docs/create-exascale-clusters/
title: Create Exascale VM Clusters \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:28:48.923412+00:00
---

# Create Exascale VM Clusters  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/create-exascale-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Create Exascale VM Clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create Exascale VM Clusters in Google Cloud.

Oracle Database@Google Cloud lets you create Exascale VM Clusters in the Google Cloud using Google Cloud console and the API.

You must create your Exascale VM Cluster in the same region and zone as your ODB Network to ensure optimal performance and seamless communication.

Each Exascale VM Cluster is associated with an Exascale Storage Vault. An Exascale Storage Vault provides instant, zero-downtime expansion of scalable, high-performance Exadata storage. While provisioning an Exascale VM Cluster, you can choose to create a new Exascale Storage Vault or select an existing one. You can use an Exascale Storage Vault with multiple Exascale VM Clusters.

For a list of regions and zones in which you can create Exascale VM Clusters, see [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones#exascale).

## Before you begin

  * [Set up the gcloud CLI and enable the API](https://docs.cloud.google.com/oracle/database/docs/set-up).

  * Confirm that you have an active marketplace order for Oracle Database@Google Cloud.

  * Enable the Oracle Database@Google Cloud API for the project.

[Enable the Oracle Database@Google Cloud API ](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  * [Create an ODB Network and ODB Subnets](https://docs.cloud.google.com/oracle/database/docs/create-odb-network). A DB system requires a single client subnet.

  * Confirm that you have the required Identity and Access Management (IAM) roles and permissions to create an Exascale VM Cluster:

    * `roles/oracledatabase.exadbVmClusterAdmin`
    * `roles/oracledatabase.exascaleDbStorageVaultAdmin`

For information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## Create an Exascale VM Cluster

To create an Exascale VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. On **VM Clusters** page, click **Create**.

  3. Enter a **Display name** for your Exascale VM Cluster. This name appears in the Google Cloud console. The display name must be unique within your Google Cloud project.

  4. Enter a **VM Cluster ID** as a unique identifier for your Exascale VM Cluster. You can't change the Exascale VM Cluster ID later.

  5. Select a **Region** and a **GCP Oracle zone**. The region and zone choice is permanent; you can't change it later.

  6. Select an **Oracle Grid Infrastructure release**.

  7. Select an **Oracle Grid Infrastructure version**.

  8. Select a **Database storage** based on the Oracle Grid Infrastructure version you selected.

If you selected `26ai` release, then you can select either `Exascale smart storage` or `Exascale block storage`.

If you selected `19c` release, then you can only select `Exascale block storage`.

  9. Enter the following values for **VM Cluster configuration** :

     * Number of VMs in the cluster. The maximum number of VMs per cluster is `10`.
     * Enabled ECPUs per VM. The number of Enabled ECPUs can range from `8` to `200`, and must be entered in multiples of 4.
     * Optional: Reserved ECPUs per VM. The number of reserved ECPUs can range from `0` to `192`, and must be entered in multiples of 4.

Reserved ECPUs let you scale and maintain consistent performance by eliminating allocation delays.

  10. To configure **VM file system storage** , enter a value for **Storage capacity per VM** which is the local storage allocated to each VM.

For `Exascale smart storage`, the storage capacity can range from `220 GiB` to `1100 GiB`. For `Exascale block storage`, the storage capacity can range from `260 GiB` to `1100 GiB`.

  11. License type. The available options are `License included` and `Bring Your Own License`.

  12. Configure an **Exascale Storage Vault** for your cluster.

Choose an existing vault or create a new one that meets your cluster's capacity, performance, and security requirements.

     * To use an existing vault, click **Select existing vault** and choose a vault from the list.

Select a vault that is in the same zone as your Exascale VM Cluster.

     * To create a new vault, do the following:

       1. Click **Create new vault**.
       2. Enter a **Display name** for your vault. This name appears in the Google Cloud console. The display name must be unique within your Google Cloud project.
       3. Enter a **Vault ID** as a unique identifier for your vault. You can't change the vault ID later.
       4. Enter a **Storage capacity for database**. The storage capacity can range from `300 GiB` to `100000 GiB`.

**Note:** The vault's storage capacity must match or exceed the total storage capacity across the cluster.
       5. Enter a value for **Smart flash and memory cache**.

  13. In the **SSH keys** section, add the SSH keys you'd like to use for the cluster. To add a key, enter the SSH key name in the **SSH Key 1** field. For each additional key, click **ADD ITEM**.

For more information about how to generate SSH keys, see [Generate SSH keys](https://docs.cloud.google.com/oracle/database/docs/generate-ssh-keys).

  14. In the **Networking** section, define the network configuration for the DB system:

     1. From the **Network project** list, select the project that contains your ODB Network.

     2. Select the **ODB Network**.

Select an ODB Network that is in the same zone as the your Exascale VM Cluster.

     3. Select a **Client subnet** and a **Backup subnet**.

     4. Enter a **Hostname prefix**. This prefix can only contain letters, numbers, or hyphens, and must start with a letter. The maximum allowed length is 12 characters.

     5. (Optional) In the **Advanced network settings** section, you can provide a **Private IP address**. This must be an available IP address within the subnet's CIDR.

If you don't specify an IP address, Google Cloud automatically assigns a private IP address from the subnet.

  15. In the **Diagnostics collection** section, configure monitoring for your Exascale VM Cluster:

     1. Select the **Enable diagnostic events** checkbox to track all cluster diagnostic events.

     2. Select the **Enable health monitoring** checkbox to use the monitoring console to monitor cluster health metrics.

     3. Select the **Enable incident logs and trace collection** checkbox to enable incident logging for your cluster.

  16. In the **Identity Connector** section, do the following:

Identity Connector lets your cluster connect to Google Cloud services, such as Cloud Key Management Service and Customer-managed encryption keys (CMEK).

Identity Connector is enabled by default.

If you don't want to enable Identity Connector now, you can disable it by clicking the **Identity Connector enabled** toggle to the off position.

You can also [enable Identity Connector](https://docs.cloud.google.com/oracle/database/docs/enable-disable-identity-connector#enable-exascale-cluster-connector) after provisioning the cluster.

**Note:** The Identity Connector is set up as a part of the cluster creation. In some cases, the cluster can be created successfully even if the Identity Connector setup fails. If the Identity Connector status shows `Not enabled` after the cluster is created, check the **Operations** tab on the **Exascale VM Cluster details** page for any errors in the setup. Then, try [enabling the Identity Connector](https://docs.cloud.google.com/oracle/database/docs/enable-disable-identity-connector#enable-identity-connector) again. Also, if your project is in a VPC Service Controls perimeter, the Identity Connector can't connect until you add the required egress rule. For more information, see [Configure VPC Service Controls](https://docs.cloud.google.com/oracle/database/docs/configure-vpc-service-controls).
  17. In the **Advanced settings** , you can optionally modify the following settings:

     * Select a **Timezone** which you'd like to use for diagnostic collection. This timezone applies to event timestamps.
     * Assign a **SCAN Listener Port (TCP/IP)**. The port value can range from `1024` to `8999`. The default value is `1521`.
  18. Click **Create**.

The provisioning workflow first creates the vault, and then creates the cluster.




### gcloud

To create an Exascale VM Cluster using the gcloud CLI, do the following:

  1. Create an Exascale Storage Vault. If you want to use an existing vault, you can skip this step and then proceed to create the Exascale VM Cluster as explained in the next step.

To create an Exascale Storage Vault, use the `gcloud oracle-database exascale-db-storage-vaults create` command.
         
         gcloud oracle-database exascale-db-storage-vaults create VAULT_ID \
             --project=PROJECT_ID \
             --location=REGION \
             --display-name="VAULT_DISPLAY_NAME" \
             --exascale-db-storage-details-total-size-gbs=VAULT_SIZE \
             --properties-additional-flash-cache-percent=FLASH_CACHE_PERCENT \
             --properties-description="VAULT_DESCRIPTION" \
             --async
         

Replace the following:

     * VAULT_ID: a unique ID for your vault.
     * PROJECT_ID: the ID of your Google Cloud project in which to create the vault.
     * REGION: the region in which to create the vault.
     * VAULT_DISPLAY_NAME: a name for your vault that appears in the Google Cloud console.
     * VAULT_SIZE: the storage capacity of your vault. It can range from 300 GiB to 100000 GiB.

**Note:** The storage capacity for the vault must match or exceed the total storage capacity across the Exadata VM Cluster.
     * FLASH_CACHE_PERCENT: the size of additional flash cache in percentage of high capacity database storage.

     * VAULT_DESCRIPTION: a description of your vault.

  2. Create an Exascale VM Cluster. Use the `gcloud oracle-database exadb-vm-clusters create` command.
         
         gcloud oracle-database exadb-vm-clusters create CLUSTER_ID \
             --project=PROJECT_ID \
             --location=REGION \
             --display-name="DISPLAY_NAME" \
             --properties-node-count=NODE_COUNT \
             --properties-enabled-ecpu-count-per-node=ENABLED_ECPU_COUNT \
             --properties-additional-ecpu-count-per-node=ADDITIONAL_ECPU_COUNT \
             --vm-file-system-storage-size-in-gbs-per-node=STORAGE_SIZE \
             --properties-license-model=LICENSE_TYPE \
             --properties-shape-attribute=SHAPE_ATTRIBUTE \
             --properties-exascale-db-storage-vault=projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_ID \
             --properties-hostname-prefix=HOSTNAME_PREFIX_NAME \
             --properties-ssh-public-keys="SSH_PUBLIC_KEY" \
             --odb-network=projects/ODB_NETWORK_PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID \
             --odb-subnet=projects/ODB_NETWORK_PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/CLIENT_SUBNET_ID \
             --backup-odb-subnet=projects/ODB_NETWORK_PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/BACKUP_SUBNET_ID \
             --properties-grid-image-id=projects/GRID_IMAGE_PROJECT_ID/locations/REGION/giVersions/GRID_IMAGE_ID \
             --data-collection-options-is-diagnostics-events-enabled \
             --data-collection-options-is-health-monitoring-enabled \
             --data-collection-options-is-incident-logs-enabled \
             --time-zone-id=TIME_ZONE_ID
         

Replace the following:

     * CLUSTER_ID: a unique ID for the cluster.
     * PROJECT_ID: the ID of the Google Cloud project in which you want to create the cluster.
     * REGION: the region where you want to create the cluster.
     * DISPLAY_NAME: a name to identify the cluster and is displayed in the Google Cloud console. The name must be unique within your Google Cloud project.
     * NODE_COUNT: the number of nodes for the cluster.
     * ENABLED_ECPU_COUNT: the number of enabled ECPUs per VM. The number of enabled ECPUs can range from 8 to 200, and must be entered in multiples of 4.
     * ADDITIONAL_ECPU_COUNT: the number of reserved ECPUs per VM. The number of reserved ECPUs can range from 0 to 192, and must be entered in multiples of 4.
     * STORAGE_SIZE: storage capacity per VM.

For Exascale 23ai smart storage, the storage capacity can range from `220 GiB` to `1100 GiB`. For Exascale 19c compatible block storage, the storage capacity can range from `260 GiB` to `1100 GiB`.

     * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. The only accepted values are `bring-your-own-license` or `license-included`.

     * SHAPE_ATTRIBUTE: the shape attribute of the cluster. The accepted values are `EXASCALE_23AI` and `EXASCALE_19C`.

     * For `properties-exascale-db-storage-vault` property, replace the following:

       * PROJECT_ID: the ID of the Google Cloud project which contains your Exascale Storage Vault.
       * REGION: the region where your Exascale Storage Vault is located.
       * VAULT_ID: the ID of the Exascale Storage Vault.
     * HOSTNAME_PREFIX: a hostname prefix. This prefix can only contain letters, numbers, or hyphens, and must start with a letter. The maximum allowed length is 12 characters.

     * SSH_PUBLIC_KEY: the SSH public keys for your cluster. You can enter a single value for a single key, or an array of values for multiple keys.

     * For `odb-network`, `odb-subnet`, and `backup-odb-subnet` properties, replace the following:

       * ODB_NETWORK_PROJECT_ID: the ID of the Google Cloud project which contains your ODB Network. If you're using a Shared VPC, then this is the ID of the host project.
       * REGION: the region where your ODB Network is located.
       * ODB_NETWORK_ID: the ID of the ODB Network.
       * CLIENT_SUBNET_ID: the ID of the client ODB Subnet.
       * BACKUP_SUBNET_ID: the ID of the backup ODB Subnet.
     * For `properties-grid-image-id` property, replace the following:

       * GRID_IMAGE_PROJECT_ID: the ID of the Google Cloud project which contains your Grid Infrastructure release version.
       * REGION: the region where your Grid Infrastructure images are located.
       * GRID_IMAGE_ID: the grid infrastructure version for your cluster.

To get a list of all available grid infrastructure versions, run the following command in gcloud CLI:
    
    gcloud oracle-database gi-versions list \
         --location=REGION
     ```
    
    Replace the following:
    
    * REGION: the region where your Grid Infrastructure
      images are located.
    

     * `--data-collection-options-is-diagnostics-events-enabled`: indicates whether to enable data collection for diagnostics.

     * `--data-collection-options-is-health-monitoring-enabled`: indicates whether to enable health monitoring.

     * `--data-collection-options-is-incident-logs-enabled`: indicates whether to enable incident logs and trace collection.

     * TIME_ZONE_ID: the timezone you'd like to use for diagnostic collection. This timezone applies to event timestamps.

     * `--identity-connector-disabled` (Optional): include this flag to create the cluster without the Identity Connector. If this flag is not specified, the Identity Connector is created by default.

Identity Connector lets your cluster connect to Google Cloud services, such as Cloud Key Management Service and Customer-managed encryption keys (CMEK).

You can also enable the Identity Connector after provisioning the cluster. For setup considerations, including VPC Service Controls, see [Enable and disable Identity Connector](https://docs.cloud.google.com/oracle/database/docs/enable-disable-identity-connector).




###  API 

To create an Exascale VM Cluster using the API, do the following:

  1. Create an Exascale Storage Vault. If you want to use an existing vault, you can skip this step and then proceed to create the Exascale VM Cluster as explained in the next step.

To create an Exascale Storage Vault, run the following `curl` command:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_ID"
         -d \
         '{
          "display_name": "VAULT_DISPLAY_NAME",
          "gcp_oracle_zone": "GCP_ORACLE_ZONE",
          "name": "projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_NAME",
          "properties": {
            "exascale_db_storage_details": {
              "total_size_gbs": "STORAGE_SIZE"
             }
           }
         }'
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project in which to create the vault.
     * REGION: the region in which to create the vault.
     * VAULT_ID: a unique identifier for your vault.
     * VAULT_DISPLAY_NAME: a name for your vault that appears in the Google Cloud console.
     * GCP_ORACLE_ZONE: the GCP Oracle zone for your vault. For the list of available regions and zones, see [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).
     * VAULT_NAME: a name for your vault.
     * STORAGE_SIZE: the storage capacity of your vault. It can range from 300 GiB to 100000 GiB.

**Note:** The storage capacity for the vault must match or exceed the total storage capacity across the cluster.
  2. Create an Exascale VM Cluster. Run the following `curl` command:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exadbVmClusters/CLUSTER_ID"
         -d \
         '{
          "display_name": "CLUSTER_DISPLAY_NAME",
          "gcp_oracle_zone": "GCP_ORACLE_ZONE",
          "name": "projects/PROJECT_ID/locations/REGION/exadbVmClusters/CLUSTER_NAME",
          "identityConnectorDisabled": IDENTITY_CONNECTOR_DISABLED,
          "odb_network": "projects/ODB_NETWORK_PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID",
          "odb_subnet": "projects/ODB_NETWORK_PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/CLIENT_SUBNET_ID",
          "backup_odb_subnet": "projects/ODB_NETWORK_PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/BACKUP_SUBNET_ID",
          "properties": {
            "cluster_name": "CLUSTER_NAME",
            "grid_image_id": GRID_IMAGE_ID,
            "node_count": NODE_COUNT,
            "enabled_ecpu_count_per_node": ENABLED_ECPU_COUNT,
            "additional_ecpu_count_per_node": "ADDITIONAL_ECPU_COUNT",
            "vm_file_system_storage": {
              "size_in_gbs_per_node": STORAGE_SIZE
            },
            "license_model": "LICENSE_TYPE",
            "exascaleDbStorageVault": "projects/PROJECT_ID/locations/REGION/exascaleDbStorageVaults/VAULT_ID",
            "hostname_prefix": "HOSTNAME_PREFIX",
            "ssh_public_keys": ["SSH_PUBLIC_KEY"],
            "data_collection_options": {
              "is_diagnostics_events_enabled": EVENTS_ENABLED,
              "is_health_monitoring_enabled": HEALTH_MONITORING_ENABLED,
              "is_incident_logs_enabled": INCIDENT_LOGS_ENABLE
             },
            "time_zone": {
              "id": "TIMEZONE"
             }
           }
         }'
         

Replace the following:

     * PROJECT_ID: the ID of your Google Cloud project in which to create the cluster.
     * REGION: the region in which to create the cluster.
     * CLUSTER_ID: a unique identifier for your cluster.
     * CLUSTER_DISPLAY_NAME: a name for your cluster that appears in the Google Cloud console.
     * GCP_ORACLE_ZONE: the GCP Oracle zone for your cluster. For the list of available regions and zones, see [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).
     * CLUSTER_NAME: a name for your cluster.
     * IDENTITY_CONNECTOR_DISABLED (Optional): set to `true` to create the cluster without the Identity Connector. If not specified, the Identity Connector is created by default.

Identity Connector lets your cluster connect to Google Cloud services, such as Cloud Key Management Service and Customer-managed encryption keys (CMEK).

You can also enable the Identity Connector after provisioning the cluster. For setup considerations, including VPC Service Controls, see [Enable and disable Identity Connector](https://docs.cloud.google.com/oracle/database/docs/enable-disable-identity-connector).

     * For `odb_network`, `odb_subnet`, and `backup_odb_subnet` properties, replace the following:

       * ODB_NETWORK_PROJECT_ID: the ID of your Google Cloud project which contains your ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
       * REGION: the region of your ODB Network.
       * ODB_NETWORK_ID: the ID of your ODB Network.
       * CLIENT_SUBNET_ID: the ID of your client ODB Subnet.
       * BACKUP_SUBNET_ID: the ID of your backup ODB Subnet.
     * GRID_IMAGE_ID: the Oracle Grid Infrastructure release image.

     * NODE_COUNT: the number of nodes for your cluster.

     * ENABLED_ECPU_COUNT: the number of enabled ECPUs per VM. The number of Enabled ECPUs can range from 8 to 200, and must be entered in multiples of 4.

     * ADDITIONAL_ECPU_COUNT: the number of reserved ECPUs per VM. The number of reserved ECPUs can range from 0 to 192, and must be entered in multiples of 4.

     * STORAGE_SIZE: storage capacity per VM.

For Exascale 23ai smart storage, the storage capacity can range from 220 GiB to 1100 GiB. For Exascale 19c compatible block storage, the storage capacity can range from 260 GiB to 1100 GiB.

     * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. The only accepted values are `bring-your-own-license` or `license-included`.

     * For `exascaleDbStorageVault` property, replace the following:

       * PROJECT_ID: the ID of your Google Cloud project which contains your Exascale Storage Vault.
       * REGION: the region of your Exascale Storage Vault.
       * VAULT_ID: the ID of your Exascale Storage Vault.
     * HOSTNAME_PREFIX: a hostname prefix. This prefix can only contain letters, numbers, or hyphens, and must start with a letter. The maximum allowed length is 12 characters.

     * SSH_PUBLIC_KEY: the SSH public keys for your cluster. You can enter a single value for a single key, or an array of values for multiple keys.

     * EVENTS_ENABLED: set to `true` to track all cluster diagnostic events.

     * HEALTH_MONITORING_ENABLED: set to `true` to enable the use of the monitoring console to monitor cluster health metrics.

     * INCIDENT_LOGS_ENABLE: set to `true` to enable incident logging for your cluster.

     * TIMEZONE: the timezone you'd like to use for diagnostic collection. This timezone applies to event timestamps.




## What's next

  * Learn about [Exadata Database Service on Exascale Infrastructure](https://docs.public.content.oci.oraclecloud.com/en-us/iaas/exadb-xs/doc/overview-exadb-xs-service.html)
  * Learn to [manage your Exascale VM Clusters](https://docs.cloud.google.com/oracle/database/docs/manage-exascale-clusters).
  * Learn to [delete an Exascale VM Cluster](https://docs.cloud.google.com/oracle/database/docs/delete-exascale-clusters).
  * Learn to [view details of an Exascale VM Cluster](https://docs.cloud.google.com/oracle/database/docs/view-exascale-cluster-information).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
