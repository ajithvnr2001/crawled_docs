---
url: https://docs.cloud.google.com/sql/docs/postgres/instance-info/
title: View instance information \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T05:53:00.394788+00:00
---

# View instance information  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/instance-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  View instance information Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/instance-info "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info "View this page for the SQL Server database engine")

This page describes how to view information about a Cloud SQL instance.

## View instance summary information

You can view summary information about Cloud SQL instances by using the Google Cloud console, [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API.

**Important:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance. For more information about viewing this endpoint, see View the write endpoint.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

The following information appears about Cloud SQL instances that have [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) enabled for them:

     * **Internal connection method:** whether Private Service Connect or [private services access](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access) is used to connect to the instance
     * **Private IP address:** the IP addresses of the [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint) in the VPC network that connect to the [service attachment](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#service-attachment) of the instance
     * **DNS name:** the [DNS name](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#dns-name-record) of the instance
  2. To see the current instance state, hold the pointer over the status icon next to an instance name.

If the instance is in a `FAILED` or `MAINTENANCE` state, then you can [recover the instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#pitr-instance-not-available) by selecting a time from the past and restoring the instance to its state at that time.

  3. To open the **Overview** page of an instance, click the instance name. 

In the **Connect to this instance** card, the following additional information appears about Cloud SQL instances with Private Service Connect enabled:

     * **Private IP connectivity:** the status is **Enabled** because the instance must have an internal IP address
     * **Allowed projects:** these [projects](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#allowed-psc-projects) allow connections from Private Service Connect endpoints to the instance
     * **Service attachment:** the service attachment of the instance
     * **Public IP connectivity:** the status is **Disabled** because external IP connections aren't supported
  4. To see connectivity information about the instance, including whether an internal or external IP address is added to the instance, any authorized networks associated with the instance, and whether other Google Cloud services, such as BigQuery, can access data in Cloud SQL and make queries against this data over an internal connection, click the **Connections** tab.

For more information about this tab, see [About connection options](https://docs.cloud.google.com/sql/docs/postgres/connect-overview).

  5. Click the **Networking** tab. The following information appears about instances that have Private Service Connect enabled for them:

     * The **Private IP** checkbox is selected, but deactivated. The instance must have an internal IP address, and this setting can't be changed.
     * The allowed projects for the instance.
     * The **Public IP** checkbox is selected, but deactivated.
     * The **Authorized networks** field is deactivated because the instance uses Private Service Connect, which doesn't support this feature.



### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

  1. To view summary information about an instance, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe INSTANCE_NAME \
         --project=PROJECT_ID

Make the following replacements:

     * INSTANCE_NAME: the name of the Cloud SQL instance. If this instance has [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) enabled for it, then [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint) in VPC networks can connect to it.
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.

Here's an example of the output for running this command:
    
    gcloud sql instances describe myinstance \
    --project=12345
    ...
    dnsName: mydnsname
    ...
    pscServiceAttachmentLink: projects/myproject/regions/myregion/serviceAttachments/myserviceattachment
    ...
     settings:
      ...
      ipConfiguration:
      ipv4Enabled: false
      pscConfig:
        allowedConsumerProjects:
          - projects/23456
          - projects/34567
        pscEnabled: true

  2. To view more-detailed information about instances that have Private Service Connect enabled for them, add the following parameters:
Setting | Parameter | Notes  
---|---|---  
DNS Name | `dnsName` | The [DNS name](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#dns-name-record) for the instance. We recommend that you create a [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) with this name and point it to the IP address of the Private Service Connect endpoint. We also recommend that you use this name to connect to the instance.  
Service attachment | `pscServiceAttachmentLink` | The URI that points to the [service attachment](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#service-attachment) of the instance. Use this URI to create the Private Service Connect endpoint.  
Allowed consumer projects | `allowedConsumerProjects` | A list of the [allowed projects](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#allowed-psc-projects) for the instance. You can create Private Service Connect endpoints from any VPC networks in these projects to the service attachment of the instance.  
Enabling Private Service Connect | `pscEnabled` | Whether an instance has Private Service Connect enabled for it.  



**Note:** To obtain the write endpoint for your Cloud SQL instance, use the `[gcloud sql instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe)` command. This endpoint is the value that's associated with the `psaWriteEndpoint` parameter.

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_NAME: the name of the Cloud SQL instance. If this instance has [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) enabled for it, then [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint) in VPC networks can connect to it.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "POSTGRES_13",
      "settings": {
        "authorizedGaeApplications": [],
        "tier": "db-custom-2-7680",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration": {
          "authorizedNetworks": [],
          "pscConfig": {
            "allowedConsumerProjects": [
              "ALLOWED_PROJECTS"
            ],
            "pscEnabled": true
          },
          "ipv4Enabled": false
        },
      ...
      "createTime": "2023-06-14T18:48:34.975Z",
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE",
      "pscServiceAttachmentLink": "projects/PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_ID",
      "dnsName": "DNS_NAME"
    }
    

The following fields exist for instances that have Private Service Connect enabled for them:

  * `allowedConsumerProjects`: a list of the [allowed projects](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#allowed-psc-projects) for the instance. You can create Private Service Connect endpoints from any VPC networks in these projects to the [service attachment](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#service-attachment) of the instance.
  * `pscEnabled`: whether an instance has Private Service Connect enabled for it.
  * `pscServiceAttachmentLink`: the URI that points to the service attachment of the instance. Use this URI to create the Private Service Connect endpoint.
  * `dnsName`: the [DNS name](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#dns-name-record) for the instance. We recommend that you create a [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) with this name and point it to the IP address of the Private Service Connect endpoint. We also recommend that you use this name to connect to the instance.



To see how to construct the [underlying REST API request](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/get) for this task, see the [instances:get](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/get) page.

**Note:** To obtain the write endpoint for your Cloud SQL instance, use the [`instances:get`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/get) method. This endpoint is the value that's associated with the `psaWriteEndpoint` parameter.

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_NAME: the name of the Cloud SQL instance. If this instance has [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) enabled for it, then [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint) in VPC networks can connect to it.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "POSTGRES_13",
      "settings": {
        "authorizedGaeApplications": [],
        "tier": "db-custom-2-7680",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration": {
          "authorizedNetworks": [],
          "pscConfig": {
            "allowedConsumerProjects": [
              "ALLOWED_PROJECTS"
            ],
            "pscEnabled": true
          },
          "ipv4Enabled": false
        },
      ...
      "createTime": "2023-06-14T18:48:34.975Z",
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE",
      "pscServiceAttachmentLink": "projects/PROJECT_ID/regions/REGION_NAME/serviceAttachments/SERVICE_ATTACHMENT_ID",
      "dnsName": "DNS_NAME"
    }
    

The following fields exist for instances that have Private Service Connect enabled for them:

  * `allowedConsumerProjects`: a list of the [allowed projects](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#allowed-psc-projects) for the instance. You can create Private Service Connect endpoints from any VPC networks in these projects to the [service attachment](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#service-attachment) of the instance.
  * `pscEnabled`: whether an instance has Private Service Connect enabled for it.
  * `pscServiceAttachmentLink`: the URI that points to the service attachment of the instance. Use this URI to create the Private Service Connect endpoint.
  * `dnsName`: the [DNS name](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#dns-name-record) for the instance. We recommend that you create a [DNS record](https://docs.cloud.google.com/dns/docs/dns-overview#records) with this name and point it to the IP address of the Private Service Connect endpoint. We also recommend that you use this name to connect to the instance.



**Note:** To obtain the write endpoint for your Cloud SQL instance, use the [`instances:get`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/get) method. This endpoint is the value that's associated with the `psaWriteEndpoint` parameter.

You might see some banners at the top suggesting actions that you might want to take.

### View the write endpoint

A write endpoint is a global domain name service (DNS) name that resolves to the IP address of the current primary instance automatically. This endpoint redirects incoming connections to the new primary instance automatically in case of a replica [failover or switchover](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas) operation. You can use the write endpoint in a SQL connection string instead of an IP address. By using a write endpoint, you can avoid having to make application connection changes when a region outage occurs.

For more information about using a write endpoint to connect to an instance, see [Connect to an instance using a write endpoint](https://docs.cloud.google.com/sql/docs/postgres/connect-to-instance-using-write-endpoint).

## Metrics

This section provides usage charts of key instance metrics that you can use to monitor your instances. When working with metric data, keep the following facts in mind:

  * A data point for a metric is an aggregate over all databases hosted by the instance.
  * Data is reported in local time. 
  * Rendered charts don't refresh automatically; to see new data, you must refresh the page.
  * There is a delay of a few minutes between when metric data is recorded and the time it is displayed in the usage charts.



For more information about the metrics shown in the chart, see [Monitoring Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance#available-metrics).

For a complete list of Cloud SQL metrics provided by Cloud Monitoring, see the [Cloud SQL metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudsql).

For more information about using Cloud Monitoring with Google Cloud, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

## Connect to this instance

In the **Connect to this instance** section, you can find your instance's IP addresses, VPC network, and connection name.

To open a terminal and connect to your instance, click **Connect using Cloud Shell**.

To open a related tutorial in the right pane, click **Connect from a Compute Engine VM instance**.

To go to [Connection options](https://docs.cloud.google.com/sql/docs/postgres/external-connection-methods), click **See all connection methods**.

For more information about connecting to an instance, see [Connecting overview](https://docs.cloud.google.com/sql/docs/postgres/connect-overview).

## Service account

This section shows the instance's service account email address.

For more information, see the IAM [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) documentation.

## Configuration

This section shows current configuration settings of the instance.

To change configuration settings, click **Edit configuration**.

For more information about editing the instance configuration, see [editing an instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance).

## Operations and logs

This section lists recent instance operations, such as creating backups.

To see recent operations, click **View all operations**.

To see logging information, click **View PostgreSQL Error Logs**.

For more information about the Operations and the Logs Explorer pages, see [Cloud SQL logging](https://docs.cloud.google.com/sql/docs/postgres/logging).

For generic information about logging, see [Viewing logs](https://docs.cloud.google.com/logging/docs/view/logs_viewer) and [Exporting logs](https://docs.cloud.google.com/logging/docs/export/configure_export).

## Maintenance

This section shows the current maintenance update settings and schedule.

To change preferences, click **Edit maintenance preferences**.

To change notification settings, click **Edit notification preferences**.

For more information about maintenance in Cloud SQL, see [Maintenance overview](https://docs.cloud.google.com/sql/docs/postgres/maintenance).

## What's next

  * Learn more about [Cloud Monitoring metrics for Cloud SQL](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudsql).
  * Learn more about [instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings).
  * Learn more about [editing an instance](https://docs.cloud.google.com/sql/docs/postgres/edit-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
