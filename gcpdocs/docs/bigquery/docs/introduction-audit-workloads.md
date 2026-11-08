---
url: https://docs.cloud.google.com/bigquery/docs/introduction-audit-workloads/
title: Introduction to audit logs in BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T08:49:33.417756+00:00
---

# Introduction to audit logs in BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/introduction-audit-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to audit logs in BigQuery

You can use BigQuery audit logs to monitor administrative and data access activities in your projects. Logs are text files that are automatically created and record who performed specific actions, like creating tables or running jobs, to help you maintain security and ensure compliance. This document explains when to use audit logs and provides an overview of their format.

Google Cloud also writes logs, including audit logs that provide insight into operational concerns related to your use of Google Cloud services. For more information about how Google Cloud handles logging, see the [Cloud Logging](https://docs.cloud.google.com/logging/docs) documentation and [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit).

## Audit logs versus `INFORMATION_SCHEMA` views

Your Google Cloud projects contain audit logs only for the resources that are directly within the Google Cloud project. Other Google Cloud resources, such as folders, organizations, and billing accounts, contain their own audit logs.

Audit logs help you answer the question "Who did what, where, and when?" within your Google Cloud resources. Audit logs are the definitive source of information for system activity by user and access patterns and should be your primary source for audit or security questions.

[`INFORMATION_SCHEMA`](https://docs.cloud.google.com/bigquery/docs/information-schema-intro) views in BigQuery are another source of insights that you can use along with metrics and logs. These views contain metadata about jobs, datasets, tables, and other BigQuery entities. For example, you can get real-time metadata about which BigQuery jobs ran during a specified time. Then, you can group or filter the results by project, user, tables referenced, and other dimensions.

`INFORMATION_SCHEMA` views provide you information to perform a more detailed analysis about your BigQuery workloads, such as the following:

  * What is the average slot utilization for all queries over the past seven days for a given project?
  * What streaming errors occurred in the past 30 minutes, grouped by error code?



BigQuery audit logs contain log entries for API calls, but they don't describe the impact of the API calls. A subset of API calls creates jobs (such as query and load) whose information is captured by `INFORMATION_SCHEMA` views. For example, you can find information about the time and slots that are utilized by a specific query in `INFORMATION_SCHEMA` views but not in the audit logs.

To get insights into the performance of your BigQuery workloads in particular, see [jobs metadata](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs), [streaming metadata](https://docs.cloud.google.com/bigquery/docs/information-schema-streaming), and [reservations metadata](https://docs.cloud.google.com/bigquery/docs/information-schema-reservations).

For more information about the types of audit logs that Google Cloud services write, see [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types).

## Audit log format

Google Cloud services write audit logs in a structured JSON format. The base data type for Google Cloud log entries is the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) structure. This structure contains the name of the log, the resource that generated the log entry, the timestamp (UTC), and other basic information.

Logs include details of the logged event in a subfield that's called the _payload field_. For audit logs, the payload field is named `protoPayload`. This field's type (`protoPayload.@type`) is set to `type.googleapis.com/google.cloud.audit.AuditLog`, which indicates that the field uses the [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) log structure.

For operations on datasets, tables, and jobs, BigQuery writes audit logs in two different formats, although both formats share the `AuditLog` base type.

The older format includes the following fields and values:

  * The value for the `resource.type` field is `bigquery_resource`.
  * BigQuery writes the details about an operation in the `protoPayload.serviceData` field. The value of this field uses the [`AuditData`](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs/rest/Shared.Types/AuditData) log structure.



The newer format includes the following fields and values:

  * The value for the `resource.type` field is either `bigquery_project` or `bigquery_dataset`. The `bigquery_project` resource has log entries about jobs, while the `bigquery_dataset` resource has log entries about storage.
  * BigQuery writes the details about an operation in the `protoPayload.metadata` field. The value of this field uses the [`BigQueryAuditMetadata`](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs/rest/Shared.Types/BigQueryAuditMetadata) structure.



We recommend consuming logs in the newer format. For more information, see [Audit logs migration guide](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs/migration).

The following is an abbreviated example of a log entry that shows a failed operation:
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "code": 5,
          "message": "Not found: Dataset myproject:mydataset was not found in location US"
        },
        "authenticationInfo": { ... },
        "requestMetadata":  { ... },
        "serviceName": "bigquery.googleapis.com",
        "methodName": "google.cloud.bigquery.v2.JobService.InsertJob",
        "metadata": {
      },
      "resource": {
        "type": "bigquery_project",
        "labels": { .. },
      },
      "severity": "ERROR",
      "logName": "projects/myproject/logs/cloudaudit.googleapis.com%2Fdata_access",
      ...
    }
    

For operations on BigQuery reservations, the `protoPayload` field uses the `AuditLog` structure, and the `protoPayload.request` and `protoPayload.response` fields contain more information. You can find the field definitions in [BigQuery Reservation API](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rpc). For more information, see [Monitoring BigQuery reservations](https://docs.cloud.google.com/bigquery/docs/reservations-monitoring).

For a deeper understanding of the audit log format, see [Understand audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).

## Limitations

Log messages have a size limit of 100,000 bytes. For more information, see [Truncated log entry](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#truncated_log_entry).

## Visibility and access control

BigQuery audit logs can include information that users might consider sensitive, such as SQL text, schema definitions, and identifiers for resources such as tables and datasets. For information about managing access to this information, see the Cloud Logging [access control documentation](https://docs.cloud.google.com/logging/docs/access-control).

## Telemetry map

The following table maps BigQuery features and resources to their operational monitoring telemetry, audited API services and resources, and audit log reference documentation. You can use it to find the telemetry that you need to troubleshoot issues, optimize performance, control costs, audit usage, and maintain compliance.

Unlike many Google Cloud services that write operational job logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs), BigQuery writes operational job telemetry to [information schema views](https://docs.cloud.google.com/bigquery/docs/information-schema-intro) such as [`INFORMATION_SCHEMA.JOBS`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs). These views capture query execution stages, slot usage, bytes billed, and all submitted jobs, including in-flight and failed jobs.

BigQuery uses Logging primarily to emit [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), which record administrative and data access activity. When you audit this activity, you can determine who accessed resources or data, where, and when.

Audit logs aren't emitted for every job disruption or failure. For example, failed jobs don't generate `TableDataRead` or `TableDataChange` events, and `jobCompletedEvent` only records successful job completions. For details about scenarios that don't emit audit logs, see [Data access](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#data_access) in the [BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).

In the following table, an asterisk (`*`) in an `INFORMATION_SCHEMA` view name indicates scope-specific view variants, such as `_BY_PROJECT`, `_BY_USER`, `_BY_FOLDER`, and `_BY_ORGANIZATION`.

Feature or resource | Operational monitoring | Cloud Audit Logs  
---|---|---  
Queries and jobs |  **Information schema views:**

  * [`JOBS*`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs): real-time and historical job execution, slot milliseconds, bytes billed, execution stages, and all submitted jobs regardless of completion status
  * [`JOBS_TIMELINE*`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-timeline): per-timeslice job state and slot usage

**Console:**

  * [Jobs explorer](https://docs.cloud.google.com/bigquery/docs/admin-jobs-explorer) in the Google Cloud console
  * [Administrative resource charts](https://docs.cloud.google.com/bigquery/docs/admin-resource-charts)

**Metrics:** [Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquery), such as `query/count`, `query/execution_times`, and `job/num_in_flight`. |  **API service:** `bigquery.googleapis.com`. **Audited resources:** jobs in `JobService` (monitored resource: `bigquery_project`). **Audit logs:** Data Access logs using [`BigQueryAuditMetadata`](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs/rest/Shared.Types/BigQueryAuditMetadata) (`JobInsertion` and `JobChange` events), recording who submitted or canceled a job, job status, statement type, and referenced tables or views. See [BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#data_access).  
Tables and views |  **Information schema views:**

  * [`TABLES`](https://docs.cloud.google.com/bigquery/docs/information-schema-tables): table metadata
  * [`VIEWS`](https://docs.cloud.google.com/bigquery/docs/information-schema-views): view definitions and metadata
  * [`TABLE_STORAGE*`](https://docs.cloud.google.com/bigquery/docs/information-schema-table-storage): logical and physical bytes and storage billing
  * [`PARTITIONS`](https://docs.cloud.google.com/bigquery/docs/information-schema-partitions): partition row counts and storage size
  * [`STREAMING_TIMELINE*`](https://docs.cloud.google.com/bigquery/docs/information-schema-streaming): streaming insert throughput and errors
  * [`WRITE_API_TIMELINE*`](https://docs.cloud.google.com/bigquery/docs/information-schema-write-api): write stream throughput and errors

**Metrics:** [Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquery), such as `storage/stored_bytes` and `storage/table_count`. |  **API services:** `bigquery.googleapis.com` and `bigquerystorage.googleapis.com`. Data Access logs for BigQuery Storage API use `bigquery.googleapis.com`, while Policy Denied logs use `bigquerystorage.googleapis.com`. **Audited resources:** tables, views, and materialized views in `TableService` and `TableDataService`; and storage read sessions and write streams in `BigQueryRead` and `BigQueryWrite` (monitored resources: `bigquery_dataset` and `bigquery_table`). **Audit logs:** Data Access logs using `BigQueryAuditMetadata` (`TableDataRead` and `TableDataChange` events for table reads, modifications, referenced fields, source job, and BigQuery Storage API stream reads and writes), plus Admin Activity, Data Access, and System Event logs for `TableCreation`, `TableChange`, and `TableDeletion` events, including table Identity and Access Management (IAM) policy changes and table expirations. See [BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).  
Datasets |  **Information schema views:**

  * [`SCHEMATA`](https://docs.cloud.google.com/bigquery/docs/information-schema-datasets-schemata): dataset metadata and default expiration
  * [`SCHEMATA_OPTIONS`](https://docs.cloud.google.com/bigquery/docs/information-schema-datasets-schemata-options): dataset options and labels
  * [`SCHEMATA_REPLICAS`](https://docs.cloud.google.com/bigquery/docs/information-schema-schemata-replicas): cross-region replication status

|  **API service:** `bigquery.googleapis.com`. **Audited resources:** datasets, dataset IAM policies, and dataset ACLs in `DatasetService` and `IAMPolicy` (monitored resource: `bigquery_dataset`). **Audit logs:** Admin Activity and Data Access logs using `BigQueryAuditMetadata` (`DatasetCreation`, `DatasetChange`, and `DatasetDeletion` events), including dataset IAM policy changes in `bindingDeltas` and ACL updates in `accessChanges`. See [BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).  
Slots and reservations |  **Information schema views:**

  * [`RESERVATIONS*`](https://docs.cloud.google.com/bigquery/docs/information-schema-reservations): current reservation configurations
  * [`RESERVATIONS_TIMELINE*`](https://docs.cloud.google.com/bigquery/docs/information-schema-reservation-timeline): per-minute reservation metadata and autoscale details
  * [`ASSIGNMENTS*`](https://docs.cloud.google.com/bigquery/docs/information-schema-assignments): project, folder, and organization assignments
  * [`CAPACITY_COMMITMENTS*`](https://docs.cloud.google.com/bigquery/docs/information-schema-capacity-commitments): slot capacity commitments

**Console:**

  * [Administrative resource charts](https://docs.cloud.google.com/bigquery/docs/admin-resource-charts) in the Google Cloud console
  * [Slot estimator](https://docs.cloud.google.com/bigquery/docs/slot-estimator)

**Metrics:** [Monitoring metrics](https://docs.cloud.google.com/bigquery/docs/reservations-monitoring), such as `slots/allocated` and `slots/total_available`. |  **API service:** `bigqueryreservation.googleapis.com` for the BigQuery Reservation API. **Audited resources:** reservations, capacity commitments, and reservation assignments in `ReservationService` (monitored resource: `bigquery_project`). **Audit logs:** Admin Activity and Data Access logs for creating, modifying, deleting, and listing reservations, capacity commitments, and project or folder assignments. See [BigQuery Reservation API audit logging](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs/index-reservation).  
Column-level security and data masking |  **Information schema views:**

  * [`COLUMN_FIELD_PATHS`](https://docs.cloud.google.com/bigquery/docs/information-schema-column-field-paths): nested column paths, policy tags, and data policy assignments
  * [`COLUMNS`](https://docs.cloud.google.com/bigquery/docs/information-schema-columns): column schemas and data types

|  **API services:** `datacatalog.googleapis.com` for Data Catalog policy tags, `bigquerydatapolicy.googleapis.com` for the BigQuery Data Policy API, and `bigquery.googleapis.com`. **Audited resources:** taxonomies and policy tags in `PolicyTagManager`, data policies in `DataPolicyService`, and policy-tagged table columns (monitored resources: `audited_resource` and `bigquery_dataset`). **Audit logs:** Admin Activity and Data Access logs for taxonomy and policy tag management and IAM policy changes ([Audit policy tags](https://docs.cloud.google.com/bigquery/docs/auditing-policy-tags)); data policy management and grantee updates ([BigQuery Data Policy audit logging](https://docs.cloud.google.com/bigquery/docs/column-data-masking-audit-logging)); and `TableDataRead.fields` logs for reads on protected columns ([BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs)).  
Routines, including UDFs and stored procedures |  **Information schema views:**

  * [`ROUTINES`](https://docs.cloud.google.com/bigquery/docs/information-schema-routines): routine definitions and metadata
  * [`ROUTINE_OPTIONS`](https://docs.cloud.google.com/bigquery/docs/information-schema-routine-options): routine options
  * [`PARAMETERS`](https://docs.cloud.google.com/bigquery/docs/information-schema-parameters): routine input and output parameters
  * [`JOBS*`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs): routine execution jobs

|  **API service:** `bigquery.googleapis.com`. **Audited resources:** user-defined functions (UDFs), table functions, and stored procedures in `RoutineService` (monitored resources: `bigquery_dataset` and `bigquery_project`). **Audit logs:** Admin Activity and Data Access logs using `BigQueryAuditMetadata` (`RoutineCreation`, `RoutineChange`, and `RoutineDeletion` events), plus child job events for stored procedure runs. See [BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).  
External connections |  **Information schema views:**

  * [`OBJECT_PRIVILEGES`](https://docs.cloud.google.com/bigquery/docs/information-schema-object-privileges): connection privileges
  * [`JOBS*`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs): federated queries and remote function jobs that use connections

|  **API service:** `bigqueryconnection.googleapis.com` for the BigQuery Connection API. **Audited resources:** connections and connection IAM policies in `ConnectionService` (monitored resource: `audited_resource`). **Audit logs:** Admin Activity and Data Access logs for connection creation, credential updates, deletion, listing, and IAM policy changes. See [BigQuery Connection API audit logging](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs/index-connection).  
BigQuery sharing |  **Information schema views:**

  * [`SHARED_DATASET_USAGE`](https://docs.cloud.google.com/bigquery/docs/information-schema-shared-dataset-usage): subscriber usage of shared dataset tables
  * [`SCHEMATA_LINKS`](https://docs.cloud.google.com/bigquery/docs/information-schema-datasets-schemata-links): linked datasets and shared resources

**Dashboard:** [sharing usage metrics dashboard](https://docs.cloud.google.com/bigquery/docs/analytics-hub-monitor-listings). |  **API service:** `analyticshub.googleapis.com`. **Audited resources:** data exchanges, listings, subscriptions, and exchange or listing IAM policies in `AnalyticsHubService` (monitored resource: `audited_resource`). **Audit logs:** Admin Activity and Data Access logs for data exchange and listing creation, updates, deletion, IAM policy changes, and subscriber operations. See [Sharing audit logging](https://docs.cloud.google.com/bigquery/docs/analytics-hub-audit-logging).  
BigQuery Data Transfer Service |  **Metrics and logs:**

  * [Monitoring transfer metrics](https://docs.cloud.google.com/bigquery/docs/dts-monitor)
  * Operational transfer run logs in Logging under `resource.type="bigquery_dts_config"`

|  **API service:** `bigquerydatatransfer.googleapis.com` for the BigQuery Data Transfer Service API. **Audited resources:** transfer configurations, transfer runs, and data sources in `DataTransferService` (monitored resource: `audited_resource`). **Audit logs:** Admin Activity and Data Access logs for creating, updating, deleting, listing, and starting transfer configurations and runs. See [BigQuery Data Transfer Service audit logging](https://docs.cloud.google.com/bigquery/docs/audit-logging).  
BigLake catalogs and tables |  **Information schema views:**

  * [`TABLES`](https://docs.cloud.google.com/bigquery/docs/information-schema-tables): table metadata
  * [`JOBS*`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs): external object storage query statistics (`metadata_cache_statistics` and `object_storage_stats`)

|  **API services:** `biglake.googleapis.com` and `bigquery.googleapis.com`. **Audited resources:** metastore catalogs, databases, tables, and partitions in `MetastoreService` and `HiveMetastoreService`, and Apache Iceberg catalogs, namespaces, and tables in `IcebergCatalogService` (monitored resources: `audited_resource` and `bigquery_dataset`). **Audit logs:** Admin Activity and Data Access logs for catalog, database, namespace, table, partition, and catalog IAM policy operations. See [BigLake audit logging](https://docs.cloud.google.com/bigquery/docs/biglake-audit-logging).  
BigQuery Migration Service |  **Status and reports:**

  * [Batch SQL translation](https://docs.cloud.google.com/bigquery/docs/batch-sql-translator) job status in the Google Cloud console
  * Workflow and subtask status in the BigQuery Migration API
  * Translation summary reports in Cloud Storage

|  **API service:** `bigquerymigration.googleapis.com` for the BigQuery Migration API. **Audited resources:** migration workflows, migration subtasks, and SQL translation requests in `MigrationService` and `SqlTranslationService` (monitored resource: `audited_resource`). **Audit logs:** Data Access logs for creating, starting, listing, viewing, and deleting migration workflows and subtasks, and translating SQL queries. See [BigQuery Migration Service audit logging](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs/audit-logging-bq-migration).  
  
## What's next

  * To learn how to use Cloud Logging to audit activities that are related to policy tags, see [Audit policy tags](https://docs.cloud.google.com/bigquery/docs/auditing-policy-tags).
  * To learn how to use BigQuery to analyze logged activity, see [BigQuery audit logs overview](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
