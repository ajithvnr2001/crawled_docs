---
url: https://docs.cloud.google.com/oracle/database/docs/enable-disable-identity-connector/
title: Enable and disable Identity Connector \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:28:13.222734+00:00
---

# Enable and disable Identity Connector  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/enable-disable-identity-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Enable and disable Identity Connector Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and disable Identity Connector to use with Google Cloud CMEK for Oracle Database@Google Cloud resources.

Identity Connector lets your clusters connect to Google Cloud services, such as Cloud Key Management Service and Customer-managed encryption keys (CMEK). Therefore, if you plan to use Google Cloud CMEK with your clusters, it is mandatory to enable the Identity Connector.

When you create an Oracle Database@Google Cloud resource, such as an Exadata VM Cluster or an Exascale VM Cluster, an Identity Connector is created by default. However, you can choose to create a cluster without the Identity Connector, and you can enable or disable it anytime after the creation of the cluster by following the steps in this document.

**Note:** In some cases, the cluster can be created successfully even if the Identity Connector setup fails. If the Identity Connector status shows `Not enabled` after the cluster is created, check the cluster's **Operations** tab for any errors in the setup. Then, try [enabling the Identity Connector](https://docs.cloud.google.com/oracle/database/docs/enable-disable-identity-connector#enable-identity-connector) again. Also, if your project is in a VPC Service Controls perimeter, the Identity Connector can't connect until you add the required egress rule. For more information, see [Configure VPC Service Controls](https://docs.cloud.google.com/oracle/database/docs/configure-vpc-service-controls).

## Before you begin

Ensure that you have the following Identity and Access Management (IAM) roles and permissions to manage Identity Connector:

  * For Exadata VM Clusters:

    * `oracledatabase.cloudVmClusters.enableIdentityConnector`
    * `oracledatabase.cloudVmClusters.disableIdentityConnector`

These permissions are included in the following IAM roles:

    * Oracle Database@Google Cloud admin (`roles/oracledatabase.admin`)
    * Oracle Database@Google Cloud VM Cluster admin (`roles/oracledatabase.cloudVmClusterAdmin`)
  * For Exascale VM Clusters:

    * `oracledatabase.exadbVmClusters.enableIdentityConnector`
    * `oracledatabase.exadbVmClusters.disableIdentityConnector`

These permissions are included in the following IAM roles:

    * Oracle Database@Google Cloud admin (`roles/oracledatabase.admin`)
    * Oracle Database@Google Cloud Exascale Infrastructure VM Cluster admin (`roles/oracledatabase.exadbVmClusterAdmin`)



For information about how to grant roles and permissions, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).

## Enable the Identity Connector

This section explains how you can enable the Identity Connector for an Exadata VM Cluster and an Exascale VM Cluster.

Enabling the Identity Connector might take a few minutes or longer in some regions.

### Exadata VM Cluster

To enable the Identity Connector for an Exadata VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service** page.

[Go to Exadata Database Service](https://console.cloud.google.com/oracle/exadata/)

  2. Select the **Exadata VM Clusters** tab.

  3. Click the name of the cluster for which you want to enable the Identity Connector.

  4. On the **Exadata VM Cluster details** page, go to the **Identity Connector** section.

  5. Click **Manage**.

  6. In the **Manage Identity Connector** dialog, click the **Identity Connector enabled** toggle to the on position.

  7. Click **Save**.




You can view the status of the enable operation in the **Operations** tab on the **Exadata VM Cluster details** page.

### gcloud

To enable the Identity Connector for an Exadata VM Cluster, use the `gcloud oracle-database cloud-vm-clusters enable-identity-connector` command:
    
    
    gcloud oracle-database cloud-vm-clusters enable-identity-connector CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.



###  API 

To enable the Identity Connector for an Exadata VM Cluster, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/cloudVmClusters/CLUSTER_ID:enableIdentityConnector" \
    -d '{}'
    

Replace the following:

  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * CLUSTER_ID: the ID of the cluster.



### Exascale VM Cluster

To enable the Identity Connector for an Exascale VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the Exascale VM Cluster for which you want to enable the Identity Connector.

  4. On the **Exascale VM Cluster details** page, go to the **Identity Connector** section.

  5. Click **Manage**.

  6. In the **Manage Identity Connector** dialog, click the **Identity Connector enabled** toggle to the on position.

  7. Click **Save**.




You can view the status of the enable operation in the **Operations** tab on the **Exascale VM Cluster details** page.

### gcloud

To enable the Identity Connector for an Exascale VM Cluster, use the `gcloud oracle-database exadb-vm-clusters enable-identity-connector` command:
    
    
    gcloud oracle-database exadb-vm-clusters enable-identity-connector CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.



###  API 

To enable the Identity Connector for an Exascale VM Cluster, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exadbVmClusters/CLUSTER_ID:enableIdentityConnector" \
    -d '{}'
    

Replace the following:

  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * CLUSTER_ID: the ID of the cluster.



## Disable the Identity Connector

This section explains how you can disable the Identity Connector for an Exadata VM Cluster and an Exascale VM Cluster.

Before disabling the Identity Connector, consider the following:

  * You can't disable the Identity Connector while any databases on the cluster use Google Cloud CMEK. You must switch those databases to Oracle-managed keys before disabling the Identity Connector.
  * Disabling the Identity Connector deletes the service account (including the Principal) associated with the cluster. When you re-enable the Identity Connector, a new service account (including the Principal) is created, and the previous IAM roles and permissions aren't carried over. Grant the new Principal access to your key as described in [Use CMEK](https://docs.cloud.google.com/oracle/database/docs/use-cmek).



### Exadata VM Cluster

To disable the Identity Connector for an Exadata VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service** page.

[Go to Exadata Database Service](https://console.cloud.google.com/oracle/exadata/)

  2. Select the **Exadata VM Clusters** tab.

  3. Click the name of the cluster for which you want to disable the Identity Connector.

  4. On the **Exadata VM Cluster details** page, go to the **Identity Connector** section.

  5. Click **Manage**.

  6. In the **Manage Identity Connector** dialog, click the **Identity Connector enabled** toggle to the off position.

  7. Click **Save**.




You can check the status of the disable operation in the **Operations** tab on the **Exadata VM Cluster details** page.

### gcloud

To disable the Identity Connector, use the `gcloud oracle-database cloud-vm-clusters disable-identity-connector` command:
    
    
    gcloud oracle-database cloud-vm-clusters disable-identity-connector CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.



###  API 

To disable the Identity Connector for an Exadata VM Cluster, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/cloudVmClusters/CLUSTER_ID:disableIdentityConnector" \
    -d '{}'
    

Replace the following:

  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * CLUSTER_ID: the ID of the cluster.



### Exascale VM Cluster

To disable the Identity Connector for an Exascale VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the Exascale VM Cluster for which you want to disable the Identity Connector.

  4. On the **Exascale VM Cluster details** page, go to the **Identity Connector** section.

  5. Click **Manage**.

  6. In the **Manage Identity Connector** dialog, click the **Identity Connector enabled** toggle to the off position.

  7. Click **Save**.




You can check the status of the enable or disable operation in the **Operations** tab on the **Exascale VM Cluster details** page.

### gcloud

To disable the Identity Connector, use the `gcloud oracle-database exadb-vm-clusters disable-identity-connector` command:
    
    
    gcloud oracle-database exadb-vm-clusters disable-identity-connector CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.



###  API 

To disable the Identity Connector for an Exascale VM Cluster, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exadbVmClusters/CLUSTER_ID:disableIdentityConnector" \
    -d '{}'
    

Replace the following:

  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * CLUSTER_ID: the ID of the cluster.



## View Identity Connector information

For an Identity Connector, you can view the following details:

  * **Status** : indicates the connection state of the Identity Connector. An Identity Connector can be in the following states:

State | Description  
---|---  
`Connected` | The Identity Connector is connected. You can enable CMEK on your resource.  
`Disconnected` | The Identity Connector is disconnected. Do the following: 
    1. Click **View details** to read the Oracle Cloud Infrastructure (OCI) message.
    2. If you use VPC Service Controls, check the egress rule. For more information, see [Configure VPC Service Controls](https://docs.cloud.google.com/oracle/database/docs/configure-vpc-service-controls).
    3. After fixing the cause, the status of the Identity Connector updates within 24 hours. You can also manually trigger a refresh through the OCI console, by going to your cluster's **Identity Connector** section.
    4. If the status still shows `Disconnected`, contact [Cloud Customer Care](https://cloud.google.com/support-hub).  
`Not enabled` | The Identity Connector isn't enabled. If you didn't disable it when you created the cluster, check the **Operations** tab on the cluster's details page for any errors in the setup. Then, try enabling the Identity Connector again.  
`Enabling` | The Identity Connector is being enabled.  
`Disabling` | The Identity Connector is being disabled.  
  * **Principal** : the email of the Oracle Database@Google Cloud service agent.

  * **Workload identity pool** : the identity pool to manage and organize your external entities.

  * **Identity connector ID** : the ID of the Identity Connector.

  * **Lifecycle state details** : the lifecycle state details, including any error messages from OCI when the Identity Connector fails to connect.




### Exadata VM Cluster

To view Identity Connector information for an Exadata VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service** page.

[Go to Exadata Database Service](https://console.cloud.google.com/oracle/exadata/)

  2. Select the **Exadata VM Clusters** tab.

  3. Click the name of the Exadata VM Cluster for which you want to view Identity Connector information.

  4. On the **Exadata VM Cluster details** page, go to the **Identity Connector** section.




### gcloud

To view the information about the Identity Connector of an Exadata VM Cluster, use the `gcloud oracle-database cloud-vm-clusters describe` command:
    
    
    gcloud oracle-database cloud-vm-clusters describe CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --format="yaml(identityConnector)"
    

Replace the following:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * `--format="yaml(identityConnector)"`: use this flag to obtain the Identity Connector details, including the workload identity pool. For example, for the VPC-SC egress rule, use `--format="value(identityConnector.workloadIdentityPool)"` with the `gcloud oracle-database cloud-vm-clusters describe` command.



###  API 

To view the information about the Identity Connector of an Exadata VM Cluster, run the following `curl` command:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/cloudVmClusters/CLUSTER_ID"
    

Replace the following:

  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * CLUSTER_ID: the ID of the cluster.



### Exascale VM Cluster

To view Identity Connector information for an Exascale VM Cluster, do the following:

### Console

  1. Go to the **Exadata Database Service > Exascale Infrastructure** page.

[Go to Exascale Infrastructure](https://console.cloud.google.com/oracle/exascale/)

  2. Select the **VM Clusters** tab.

  3. Click the name of the Exascale VM Cluster for which you want to view the Identity Connector information.

  4. On the **Exascale VM Cluster details** page, go to the **Identity Connector** section.




### gcloud

To view the information about the Identity Connector of an Exascale VM Cluster, use the `gcloud oracle-database exadb-vm-clusters describe` command:
    
    
    gcloud oracle-database exadb-vm-clusters describe CLUSTER_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --format="yaml(identityConnector)"
    

Replace the following:

  * CLUSTER_ID: the ID of the cluster.
  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * `--format="yaml(identityConnector)"`: use this flag to obtain the Identity Connector details, including the workload identity pool. For example, for the VPC-SC egress rule, use `--format="value(identityConnector.workloadIdentityPool)"` with the `gcloud oracle-database exadb-vm-clusters describe` command.



###  API 

To view the information about the Identity Connector of an Exascale VM Cluster, run the following `curl` command:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/exadbVmClusters/CLUSTER_ID"
    

Replace the following:

  * PROJECT_ID: the ID of the Google Cloud project which contains the cluster.
  * REGION: the region where the cluster is located.
  * CLUSTER_ID: the ID of the cluster.



## What's next

  * Learn how to [use CMEK](https://docs.cloud.google.com/oracle/database/docs/use-cmek) with your Oracle Database@Google Cloud resources.
  * Learn about [Cloud KMS](https://docs.cloud.google.com/kms/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
