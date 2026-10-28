---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/audit-backup-restore/
title: Secure and restore audit logs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T22:37:19.400576+00:00
---

# Secure and restore audit logs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/audit-backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Secure and restore audit logs Stay organized with collections  Save and categorize content based on your preferences. 

Audit log backups in Google Distributed Cloud (GDC) air-gapped preserve historical records in remote storage buckets for compliance, security analysis, and disaster recovery. To back up or restore platform audit logs, identify your source log bucket and share its endpoint and credentials with your [infrastructure operator (IO)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences). Your IO installs and configures the components required to transfer and recover historical audit logs from remote backups.

## Identify the source bucket

You must identify the source GDC bucket that contains the original audit logs you want to secure.

**Note:** You must explicitly list the `audit-logs-loki-pa bucket` to identify the bucket that contains the original audit logs that need to be secured. 

To get the permissions you need to view platform audit logs buckets, ask your IAM Org Admin to grant you the Audit Logs Platform Bucket Viewer (`audit-logs-platform-bucket-viewer`) role in the Management API server in the `audit-logs-loki-pa-buckets` namespace.

You must share with the IO the name and endpoint of the bucket that contains the logs you want to secure. To learn how to view bucket configurations, see [List and view storage bucket configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/list-view-storage-buckets).

## Contact your IO to create a backup and restore audit logs

To request a backup and restore process for audit logs, contact your Infrastructure Operator (IO) and provide them with the backup bucket's endpoint and access credentials. You are responsible for ensuring the IO gets these permissions upon request.

To learn how to grant access, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
