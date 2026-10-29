---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses/
title: Migration job status codes \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:18:00.221468+00:00
---

# Migration job status codes  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Migration job status codes Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service uses similar status codes for both homogeneous SQL Server migration approaches, with specific substatuses and post-promotion behaviors depending on the type of migration you perform:

  * Status codes for backup and restore migrations
  * Status codes for Distributed Availability Group (DAG) migrations



## Status codes for backup and restore migrations

The following table lists and describes migration job statuses for [backup and restore migrations](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview#backup-and-restore-migrations):

Migration job status | Description | Possible substatus | Possible user actions  
---|---|---|---  
**Not started** | The migration job is ready but still not running. This status is relevant if the migration job was created but wasn't started. | None | Start. Delete.  
**Starting...** | The migration job is in the process of being started. This is an intermediate status that occurs when a migration job is started. Starting the migration job takes between a few seconds and a few minutes. The status changes to `Running`. | None | Delete.  
**Running** | The migration job is actively running. | `CDC`, `Promote in progress`. | Stop. Promote. Delete.  
**Running with errors** | This status means that Database Migration Service encountered errors with your migration. Faulty operations will be retried, and errors clear automatically once the underlying issue is resolved. Database Migration Service continues migrating data unaffected by the error. | Incremental load. | Stop. Restart. Promote.  
**Completed** | The migration job is completed. This status occurs after a successful promotion. | None | Delete.  
**Failed** | The migration job failed because of an error. You need to restart the migration job after the issue is fixed. | The last status before the migration job failed. Failed in CDC, Failed in full dump. | Restart. Delete. Promote.  
**Restarting** | The migration job is in the process of being restarted. | None | Delete.  
**Stopped** | The migration job is stopped. | The last status before the migration job has stopped. |   
**Resuming** | The migration job is in the process of being resumed. | None | Delete.  
**Stopping...** | The migration job is in the process of stopping after `Stop` was invoked. This is an intermediate status that occurs when a user stops a migration job. Stopping the job takes around a minute, during which the status is `Stopping`. Subsequently, the status changes to `Stopped`. | None | Delete  
**Ready to promote** | Database Migration Service stops continuous load when it detects a transaction log file whose name ends in the `.final` suffix (see [ naming convention associated with the final transaction log file](https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files). Once that transaction log file is replicated to the destination Cloud SQL instance, the migration job status changes to **Ready to promote**. This status doesn't occur if you just stop uploading transaction log backup files instead of using a file with the `.final` suffix in the name. | None | [ Promote](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration)  
  
## Status codes for Distributed Availability Group (DAG) migrations

The following table lists and describes migration job statuses for [Distributed Availability Group (DAG) migrations](https://docs.cloud.google.com/database-migration/docs/sqlserver/dag-migration-overview):

Migration job status | Description | Possible substatus | Possible user actions  
---|---|---|---  
**Not started** | The migration job is ready but still not running. Before starting a DAG migration job, run the `verify` command to validate connectivity and permissions. | None | Verify. Start. Delete.  
**Starting...** | The migration job is in the process of being started. This is an intermediate status that occurs when a migration job is started. Starting the migration job takes between a few seconds and a few minutes. The status changes to `Running`. | None | Delete.  
**Running** | The migration job is actively running. | `Full dump` (initial full load), `CDC` (continuous replication), `Promote in progress`, or `Failback` (`PHASE_FAILBACK` in Google Cloud CLI and API responses; post-promotion reverse replication from Cloud SQL for SQL Server to the source SQL Server instance). | Stop. Promote (in `CDC`). Promote with `--failback` (in `Failback`). Delete.  
**Running with errors** | This status means that Database Migration Service encountered errors with your migration. Faulty operations are retried, and errors clear automatically once the underlying issue is resolved. Database Migration Service continues migrating data unaffected by the error. | `Full dump`, `CDC`, or `Failback`. | Stop. Restart. Promote (in `CDC`). Promote with `--failback` (in `Failback`). Delete.  
**Completed** | For Distributed Availability Group (DAG) migrations, promoting the migration job transitions the job to the `Running` (`Failback`) substatus to support reverse replication rather than `Completed`. To finalize a DAG migration after promotion, you can stop replication and delete the migration job, which completes the migration and performs the necessary cleanup. | None | Delete.  
**Failed** | The migration job failed because of an error. You need to restart the migration job after the issue is fixed. | The last status before the migration job failed. Failed in CDC, Failed in full dump. | Restart. Delete. Promote.  
**Restarting** | The migration job is in the process of being restarted. Restarting drops the migrated databases on the destination Cloud SQL for SQL Server instance and re-runs the initial full load. | None | Delete.  
**Stopped** | The migration job is stopped and data replication is halted. Stopping a DAG migration job should only be used for a defined, short period because updates continue to accumulate in the transaction logs while replication is halted. From the `Stopped` state, you can either resume data replication (`Resume`) or complete the migration and perform cleanup (`Delete`). | The last status before the migration job has stopped. | Resume. Restart. Delete.  
**Resuming** | The migration job is in the process of being resumed. | None | Delete.  
**Stopping...** | The migration job is in the process of stopping after `Stop` was invoked. This is an intermediate status that occurs when a user stops a migration job. Stopping the job takes around a minute, during which the status is `Stopping`. Subsequently, the status changes to `Stopped`. | None | Delete.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
