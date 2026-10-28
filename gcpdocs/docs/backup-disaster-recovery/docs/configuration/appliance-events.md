---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/
title: Backup/recovery appliance event logs \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:48:47.953235+00:00
---

# Backup/recovery appliance event logs  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/

[ Skip to main content ](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/)
  * [Deutsch](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=de)
  * [Español](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=es-419)
  * [Français](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=id)
  * [Italiano](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=it)
  * [Português](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=ja)
  * [한국어](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fbackup-disaster-recovery%2Fdocs%2Fconfiguration%2Fappliance-events%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/operations-color.svg) ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Permissions and roles](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#permissions_and_roles)
  * [View event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#view_event_logs)
  * [Event log format](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#format)
  * [Sample queries](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#log)
  * [What's next](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)


Was this helpful?
Send feedback 
#  Backup/recovery appliance event logs Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Permissions and roles](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#permissions_and_roles)
  * [View event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#view_event_logs)
  * [Event log format](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#format)
  * [Sample queries](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#log)
  * [What's next](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#whats_next)


This page explains how to view the event logs created on a backup/recovery appliance in **Cloud Logging**. Event logs provide insight on your backup/recovery appliance, such as system events or errors.
## Permissions and roles
[IAM](https://docs.cloud.google.com/iam/docs) permissions and roles determine if you can access event logs data of Backup and DR.
You need the permission `roles/logging.viewer` to view the event logs. The **Logs Viewer** role gives you read-only access to view event logs of all backup/recovery appliances in the specified project. For more information about the IAM permissions and roles that apply to event logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).
## View event logs
You can view Backup and DR event logs in **Cloud Logging** by using the Google Cloud console and the Google Cloud CLI.
[Console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#console)[gcloud](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#gcloud)[API](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#api) More
In the Google Cloud console, you can use the **Logs Explorer** to retrieve the Backup and DR event log entries for your backup/recovery appliances:
  1. In the Google Cloud console, go to the **Logging > Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, follow these steps:
    1. From the **Resource** drop-down, select the _Backup Recovery Appliance_.
    2. From the **Select Log name** drop-down, select the _backup_recovery_appliance_events_ to view event logs of backup/recovery appliances.


The Google Cloud CLI provides a command-line interface to the **Logging API**. Supply a valid resource identifier in each of the log names. To read your event log entries of backup/recovery appliances in a project, run the following command:

```
```gcloud
gcloud logging read "logName : projects/PROJECT_ID/logs/backup_recovery_appliance_events"\
 --project=PROJECT_ID
 ```

```

To view your audit log entries of backup/recovery appliances in a project, do the following:
  1. Go to the **Try this API** section in the documentation for the [entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method.
  2. Put the following into the **Request body** part of the **Try this API** form. Clicking this [prepopulated form](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) automatically fills the request body, but you need to supply a valid PROJECT_ID in each of the log name field.

```
```API
{
  "resourceNames": [
    "projects/PROJECT_ID"
  ],
  "pageSize": 5,
  "filter": "logName : projects/PROJECT_ID/logs/backupdr_audit_log"
}
```

```

  3. Click **Execute**.


## Event log format
Backup and DR event log entries include the following fields:
  * **appName** : This field displays the name of the application associated with the event.
  * **srcid** : This field displays a unique ID of the event occurring in the backup/recovery appliance.
  * **jobName** : This field displays the name of the job associated with the event.
  * **appType** : This field displays the type of the application associated with the event.
  * **eventId** : This field displays a unique ID associated with the error.
  * **component** : This field displays the source of the event.
  * **eventTime** : This field displays the time when the event was reported.
  * **errorMessage** : This field describes the detailed error associated with the event.


The following sample is an example log entry logged on a backup/recovery appliance `ba-1-52973` for a failed snapshot job.

```
    {
    "insertId": "aop2oko38hsami1c",
    "jsonPayload": {
    "appName": "instance-2",
    "srcid": "111428",
    "jobName": "Job_0110906c",
    "appType": "GCPInstance",
    "eventId": 43901,
    "component": "udp",
    "eventTime": "2023-02-06T20:24:52.450Z",
    "errorMessage": "Failed snapshot Job_0110906c for application instance-2 on host instance-2, Error: 1249: Failed to get VM details , sltname: pd snaps, slpname: ba-1-52973_Profile. "
    },
    "resource": {
    "type": "backupdr.googleapis.com/BackupRecoveryAppliance",
    "labels": {
    "backup_recovery_appliance_id": "test-backup-recovery-appliances",
    "resource_container": "projects/1234567",
    "management_server_id": "abcd-efgh-1234-5678-6789",
    "location": ""
    }
    },
    "timestamp": "2023-02-06T20:24:55.275029393Z",
    "severity": "ERROR",
    "logName": "projects/project1/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events",
    "receiveTimestamp": "2023-02-06T20:24:56.388937247Z"
    }

```

## Sample queries
You can write custom event queries in the query section to view the event logs that you want.
Use the following query to view all the event logs associated with backup/recovery appliances for a given PROJECT_ID:

```
    logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events"

```

If you are looking for event logs for a specific backup/recovery appliance, add the following backup/recovery appliance name:

```
    logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events"
    resource.labels.backup_recovery_appliance_id= "backup/recovery appliance name"

```

If you are looking for event logs for a specific event ID, then use the following log query. Make sure you use an uppercase _AND_.

```
    logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events"
    AND jsonPayload.eventId = event ID

```

If you are looking for event logs for multiple specific event IDs, then use the following log query. Make sure you use an uppercase _AND_ and _OR_.

```
    logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events"
    AND jsonPayload.eventId = (event ID 1 OR event ID 2 OR event ID 3)

```

If you are looking for event logs and you want to exclude specific event IDs, then use the following log query. Make sure you use uppercase _AND NOT_ and _OR_.

```
    logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events"
    AND NOT jsonPayload.eventId = (event ID 1 OR event ID 2 OR event ID 3)

```

If you are looking for event logs for a specific application, then use the following log query. Make sure you use uppercase _AND_.

```
    logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events" AND jsonPayload.app_name = appname

```

## What's next
  * To configure log-based alerts for Backup and DR, create a log query, using the [filter event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events/#log), and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).
  * To create log-based metrics for Backup and DR, see [Log-based metrics overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
