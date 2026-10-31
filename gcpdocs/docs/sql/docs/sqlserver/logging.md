---
url: https://docs.cloud.google.com/sql/docs/sqlserver/logging/
title: View instance logs \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:53:25.481849+00:00
---

# View instance logs  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  View instance logs Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/logging "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/logging "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to use Cloud Logging to view and query logs for your Cloud SQL instance.

Cloud Logging automatically collects log data from your Cloud SQL instances. You can use Logging to query, view, and analyze your log data to help you troubleshoot problems and improve observability. For more information, see the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs) and review the [Cloud SQL sample queries](https://docs.cloud.google.com/logging/docs/view/query-library-preview#sql-filters).

## Before you begin

To get the permissions that you need to use the Logs Explorer to view log entries, ask your administrator to grant you the following IAM roles: 

  * To view log entries in the `_Required` bucket and those in the `_Default` view on the `_Default` bucket, or to select a log scope: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on your project, folder, or organization. 
  * To view all log entries in the `_Required` and `_Default` buckets: [Private Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer) (`roles/logging.privateLogViewer`) on your project, folder, or organization. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View logs

To view log entries for your Cloud SQL instance, do the following:

### Console

  1. In the Google Cloud console, go to the **Cloud Logging** page.

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

  2. Select a Cloud SQL project.
  3. In the **Query** pane, make the following selections:
     * All resources: select **Cloud SQL Database**. In the dialog, select a Cloud SQL instance.
     * All log names: go to the Cloud SQL section and select appropriate log files for your instance. For example: 
       * `cloudsql.googleapis.com/sqlagent.out`
       * `cloudsql.googleapis.com/sqlserver.err`
     * All severities: select a severity level. For example, select `Error` to view logs with a severity level of at least `Error`.
     * Time-range selector: select a preset time option, specify a custom start and end time, or center the time range around a specific timestamp.



### gcloud

Use the [`gcloud logging`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view log entries. In the example below, replace `PROJECT_ID`. The [`limit`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--limit) flag is an optional parameter that indicates the maximum number of entries to return.
    
    
    gcloud logging read "resource.type=cloudsql_database" \
    --project=PROJECT-ID \
    --limit=10 \
    --format=json

## View instance operations log

You can view the logs for an instance in the **Operations** pane. The **Operations** pane logs every operation performed on the instance with the following information:

  * The time the operation completed, reported in your local time zone.
  * The type of operation.
  * The status of the operation.
  * A message describing the outcome of the operation.



If the operation fails, you can use the message to troubleshoot the problem.

**To view an instance operations log:**

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Go to the **Operations and logs** pane to view the operations log.

**Note:** The operations log does not include operations performed by using external management tools, such as SQL Server command-line tools. Only user management and password change operations performed by using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the Cloud SQL Admin API appear in the operations log. 

## View application logs

Applications that connect to Cloud SQL store their logs in different locations.

### App Engine (flexible environment)

To view logs for your App Engine services, do the following:

  1. Go to the App Engine **Services** page in the Google Cloud console:

[Go to Services](https://console.cloud.google.com/appengine/services)

  2. Select a service from the table, and click **Logs** in the **Diagnose** column.

You are redirected to the Logs Explorer with a query that retrieves the logs for your App Engine service.




To view App Engine logs in the **Logs Explorer** section of the Google Cloud console, use a query like the following:
    
    
    resource.type="gae_app"
    resource.labels.module_id="default"
    

### Cloud Run

To view Cloud Run logs in the **Logs Explorer** section of the Google Cloud console, use a query like the following:
    
    
    resource.type="cloud_run_revision"
    resource.labels.service_name="$SERVICE_NAME"
    resource.labels.revision_name="$REVISION_NAME"
    

Note that Cloud Run only reports error messages from the Cloud SQL Auth Proxy.

### Cloud SQL Auth Proxy

To view Cloud SQL Auth Proxy logs in the **Logs Explorer** section of the Google Cloud console, use a query like the following:
    
    
    log_id("appengine.googleapis.com/cloud-sql-proxy")
    

## View audit logs

Cloud SQL writes Cloud Audit Logs to record administrative activities and data access across your resources. You can view the following types of audit logs for your Cloud SQL instances:

  * Admin Activity: log entries written by user-driven API calls or other actions that modify the configuration or metadata of resources. You can't deactivate these logs.
  * Data Access: log entries written by API calls that read the configuration or metadata of resources.. These logs also include operations that read or write user-provided data. To write Data Access audit logs, you must [enable them](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable).
  * System Event: log entries written by Google Cloud systems and managed service agents that modify the configuration of resources. You can't deactivate these logs.



For more information about viewing Cloud SQL audit logs, including a full list of audited methods, see [Cloud SQL for SQL Server audit logging](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging).

## Pricing

For more information about Cloud Logging pricing, see [Cloud Logging pricing summary](https://cloud.google.com/products/observability/pricing#logs-costs).

## Troubleshoot

Issue | Troubleshooting  
Audit logs are not found. | Data-Access logs are only written if the operation is an authenticated user-driven API call that creates, modifies, or reads user-created data, or if the operation accesses configuration files or metadata of resources.   
Operations information is not found in logs. | You want to find more information about an operation. For example, a user was deleted but you can't find out who did it. The logs show the operation started but don't provide any more information. You must [enable audit logging](https://docs.cloud.google.com/logging/docs/audit) for detailed and personal identifying information (PII) like this to be logged.  
Some logs are filtered from the `error.log` log of a Cloud SQL for SQL Server instance.  | Filtered logs include AD logs without timestamps, and include: `Login failed for user 'x'. Reason: Token-based server access validation failed with an infrastructure error. Login lacks connect endpoint permission. [CLIENT: 127.0.0.1]`. These logs are filtered because they potentially can cause confusion.   
Log files are hard to read. | You'd rather view the logs as json or text.You can use the [ `gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command along with linux post-processing commands to download the logs. To download the logs as JSON:
    
    
    gcloud logging read \
    "resource.type=cloudsql_database \
    AND logName=projects/PROJECT_ID \
    /logs/cloudsql.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d" \
    > downloaded-log.json
        

To download the logs as TEXT:
    
    
    gcloud logging read \
    "resource.type=cloudsql_database \
    AND logName=projects/PROJECT_ID \
    /logs/cloudsql.googleapis.com%2FLOG_NAME" \
    --format json \
    --project=PROJECT_ID \
    --freshness="1d"| jq -rnc --stream 'fromstream(1|truncate_stream(inputs)) \
    | .textPayload' \
    --order=asc
    > downloaded-log.txt
         
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
