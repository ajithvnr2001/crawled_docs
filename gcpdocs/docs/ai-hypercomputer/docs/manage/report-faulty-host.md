---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host/
title: Report faulty host \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T08:26:41.407738+00:00
---

# Report faulty host  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Report faulty host Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

If an A5X, A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) instance experiences hardware issues that you can't resolve on your own—such as slower performance or consistently high GPU temperatures—you can report its host as faulty to minimize downtime for your workload.

This document describes how to report a faulty host and track the repair status for Slurm clusters and other clusters that use Compute Engine instances. To report faulty hosts in a Google Kubernetes Engine (GKE) cluster, instead see [Report faulty hosts through GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters#report-faulty-hosts-how-to).

**Caution** : Reporting a faulty host can stop your compute instance and disrupt your workload. Before you report a host as faulty, investigate your environment to identify the root cause of the issue. Only report the host as faulty if you have no alternatives to resolve your issue. 

## Limitations

When you report a faulty host, the following limitations apply:

  * You can only report a faulty host if the compute instance that runs on the host meets all of the following conditions:

    * The compute instance is running.

    * The compute instance uses an A5X, A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machine type.

    * The compute instance uses the standard, flex-start, or reservation-bound provisioning model.

**Note:** To report a faulty host for a Spot VM or for a compute instance that has [General GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) attached, contact your account team or [Cloud Customer Care](https://docs.cloud.google.com/support/docs/overview).
  * If you delete a compute instance while the `reportHostAsFaulty` operation is in progress, then the `reportHostAsFaulty` operation fails.

  * Google Cloud makes best-effort attempts to fulfill all your report faulty host requests. However, due to capacity constraints or rate limits, a request might not always be fulfilled.




## Understand the faulty host report process

After you report a faulty host for a compute instance, the time when the compute instance restarts varies based on the [ reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode) that is specified in the reservation that the compute instance uses. To verify the reservation operational mode for a reservation, [view the `reservationOperationalMode` field in the reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation). The following table summarizes the faulty host process for the two available reservation operational modes: _all capacity mode_ and _managed mode_.  | All capacity mode (`ALL_CAPACITY`) | Managed mode (`HIGHLY_AVAILABLE_CAPACITY`)  
---|---|---  
Supported machine types | A4X Max and A4X | A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs)  
Faulty host report API rate limiting | No rate limits apply. | API calls might be rate-limited.  
Faulty host report process |  When you report a faulty host for a compute instance that runs in all capacity mode, the following occurs:

  1. **Report the faulty host** : the compute instance remains in the `RUNNING` state throughout the report faulty host operation, which usually takes between 10 and 12 minutes to complete. To review the operation state, see Review report faulty host operations in this document.
  2. **Repair the host** : after the report faulty host operation completes, the host repair operation starts within a minute. When the host repair operation starts, the compute instance stops and its state changes depending on the [automatic restart (`automaticRestart`) setting](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) that is specified for the compute instance:
     * If automatic restart is enabled for the compute instance, then the compute instance state changes to `REPAIRING`.
     * If automatic restart is disabled for the compute instance, then the compute instance state changes to `TERMINATED`.
Repairing the faulty host can take from 3 to 14 days, or even longer at times.
  3. **Restart the compute instance** : after the host repair operation completes, one of the following occurs:
     * If the compute instance is in the `REPAIRING` state and the resources are available when the repair completes, then Compute Engine automatically restarts the compute instance on the repaired host.
     * Otherwise, if the compute instance is in the `TERMINATED` state or if resources aren't available when the repair completes, then the compute instance state stays in or changes to `TERMINATED`. You must [manually restart the compute instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) when you want it to run. However, if resources aren't available when you restart the compute instance—for example, if other compute instances are already using the repaired host—then the restart might fail.

|  When you report a faulty host for a compute instance that runs in managed mode, the following occurs:

  1. **Report the faulty host** : the compute instance remains in the `RUNNING` state throughout the report faulty host operation, which usually takes between 10 and 12 minutes to complete. To review the operation state, see Review report faulty host operations in this document. 
  2. **Start repairing the host** : after the report faulty host operation completes, the host repair operation starts within a minute. The behavior of the compute instance when the host repair operation starts varies by machine series:
     * **A4 and A3 Ultra** : Compute Engine attempts to live migrate the compute instance to a different host. If you lack sufficient reserved capacity or capacity isn't available in the compute instance's zone, then the compute instance stops.
     * **A3 Mega and A3 High** : Compute Engine stops the compute instance and restarts it on a healthy host.
If a compute instance stops, then its state changes depending on the [automatic restart (`automaticRestart`) setting](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) that is specified for the compute instance:
     * If automatic restart is enabled for the compute instance, then the compute instance state changes to `REPAIRING`. Unless you stop the compute instance first, it automatically restarts when its host is healthy.
     * If automatic restart is disabled for the compute instance, then the compute instance state changes to `TERMINATED`. After its host is healthy, you must manually restart the compute instance.
Repairing the original faulty host can take from 3 to 14 days, or even longer at times.
  3. **Migrate or restart the compute instance** : after the host repair operation starts, Compute Engine attempts to reserve a healthy host to replace your reported faulty host in your reserved capacity. If Compute Engine finds a replacement host, then the following occurs:
     * **A4 and A3 Ultra** : if the compute instance was live-migrated in the previous step, then it continues to run on the replacement host. If the compute instance was stopped, then it restarts on the replacement host.
     * **A3 Mega and A3 High** : the compute instance restarts on the replacement host.
If Compute Engine can't find a replacement host right away, then the compute instance restarts as follows:
     * If the compute instance is in the `REPAIRING` state and resources are available before or when the repair completes, then Compute Engine automatically restarts the compute instance on a healthy host.
     * Otherwise, if the compute instance is in the `TERMINATED` state or if resources aren't available before or when the repair completes, then the compute instance state stays in or changes to `TERMINATED`. You must [manually restart the compute instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) when you want it to run.
Unlike in all capacity mode, you don't need to wait for the original faulty host to be repaired before your workload can resume.

  
  
## Troubleshoot issues before you report a faulty host

Before you report a faulty host, we recommend that you troubleshoot the issue to confirm if it's a hardware problem, rather than an issue with your workload or cluster configuration. This approach helps to prevent unnecessary downtime for your workloads.

### Check for GPU memory or Xid errors

If you observe GPU memory or Xid errors on a compute instance, then verify whether manual recovery measures—such as resetting the GPUs or rebooting the compute instance—can resolve the issue before you report the host as faulty. For more information, see [Review Xid messages](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#review-xid-messages).

### Check for GPU performance issues and stragglers

If you notice slow performance, then use the [straggler detection service](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance) to identify compute instances that might be performing slower than others in the cluster.

### Monitor GPU temperatures and thermal violations

If you see thermal violation warnings in your logs or reported by DCGM, then review the following guidance:

  * **Warnings versus critical errors** : DCGM diagnostics might report thermal violations as warnings with a severity of `monitor`. This severity means that the GPUs are still ready to execute workloads, but we recommend that you monitor them.

  * **False positives** : NVIDIA is investigating an increase in the frequency of thermal violation reports on GPUs that don't show signs of actual thermal issues.

  * **Recommendation** : before you report a host as faulty due to thermal warnings, check if the actual GPU temperatures exceed safe thresholds and if the performance of your workload is affected. If temperatures remain stable and performance is normal, then we recommend that you monitor the GPU instead of reporting it as faulty.




For more information about GPU troubleshooting, see [Troubleshoot GPU VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus) in the Compute Engine documentation.

## Before you begin

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### Required roles

To get the permissions that you need to report a faulty host, ask your administrator to grant you the following IAM roles: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project
  * View report faulty host operations by using Logging: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to report a faulty host. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to report a faulty host:

  * To report a faulty host: `compute.instances.update` on the compute instance or the project 
  * To view a list of operations by using Logging: `logging.logEntries.list` on the project 
  * To view a list of operations in Compute Engine: `compute.zoneOperations.list` on the project 
  * To view the details of an operation in Compute Engine: `compute.zoneOperations.get` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Report a faulty host

To report a faulty host, complete the following steps:

  1. **Review the host on which your compute instance runs**. You must check the ID of the host on which your compute instance runs.

For instructions, see [View topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology#view-topology).

  2. Optional: **Back up Local SSD data**. When the compute instance stops, Compute Engine automatically discards the data of any Local SSD disks that are attached to the compute instance. You can't recover Local SSD data after Compute Engine discards it.

For instructions on how to preserve Local SSD data, see [Local SSD data backup](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_backup).

  3. **Report the faulty host**. The host repair operation starts immediately, within a minute after the report faulty host operation completes. If the compute instance becomes unresponsive after you start the faulty host report operation, then, after you wait for at least 15 minutes, we recommend that you restart the compute instance.

**Important:** After you report a host as faulty, don't send additional requests until the operation completes. Compute Engine rejects additional requests while the operation is in progress.

To report a faulty host, select one of the following:

###  gcloud 

To report a faulty host, use the [`gcloud compute instances report-host-as-faulty` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty):
         
         gcloud compute instances report-host-as-faulty INSTANCE_NAME \
             --async \
             --disruption-schedule=IMMEDIATE \
             --fault-reasons=behavior=FAULT_REASON,description=DESCRIPTION \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance.

     * `FAULT_REASON`: a list of host issues that your compute instance encountered, separated by commas—for example, `ISSUE_1,ISSUE_2`. You can specify the following values:

       * **`PERFORMANCE`** : GPUs that are attached to the compute instance have performance issues compared to other GPUs in the cluster, you see no Xid errors in the logs, and Compute Engine detects no other usual failure patterns, such as silent data corruption.

       * **`SILENT_DATA_CORRUPTION`** : you see data corruption in your compute instance, but the compute instance keeps running. Silent data corruption can be due to issues like vCPUs defects, software bugs, or kernel issues.

       * **`UNRECOVERABLE_GPU_ERROR`** : you identified an unrecoverable GPU error with an Xid.

       * **`BEHAVIOR_UNSPECIFIED`** : you aren't sure about what the issue to your compute instance is.

     * `DESCRIPTION`: a description of the issue that is affecting your compute instance, such as Xid information or suspected performance problems.

     * `ZONE`: the zone where the compute instance exists.

###  REST 

To report a faulty host, make a `POST` request to the [`instances.reportHostAsFaulty` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/reportHostAsFaulty).

When you report a faulty host, you can specify multiple fault reasons at once. For example, to specify two fault reasons, make a request as follows:
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/reportHostAsFaulty
    
    {
      "disruptionSchedule": "IMMEDIATE",
      "faultReasons": [
        {
          "behavior": "FAULT_REASON_1",
          "description": "DESCRIPTION_1"
        },
        {
          "behavior": "FAULT_REASON_2",
          "description": "DESCRIPTION_2"
        }
      ]
    }
    

Replace the following:

     * `PROJECT_ID`: the ID of the project where the compute instance exists.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of the compute instance.

     * `FAULT_REASON_1` and `FAULT_REASON_2`: each host issue that your compute instance encountered. You can specify the following values:

       * **`PERFORMANCE`** : GPUs that are attached to the compute instance have performance issues compared to other GPUs in the cluster, you see no Xid errors in the logs, and Compute Engine detects no other common failure patterns, such as silent data corruption.

       * **`SILENT_DATA_CORRUPTION`** : you see data corruption in your compute instance, but the compute instance keeps running. Silent data corruption can be due to issues like vCPUs defects, software bugs, or kernel issues.

       * **`UNRECOVERABLE_GPU_ERROR`** : you identified an unrecoverable GPU error with an Xid.

       * **`BEHAVIOR_UNSPECIFIED`** : you aren't sure about what the issue to your compute instance is.

     * `DESCRIPTION_1` and `DESCRIPTION_2`: a description for each host issue that you specified, such as Xid information or suspected performance problems.




## Review report faulty host operations

After you report a faulty host, Compute Engine starts a series of operations to mark the host as faulty and prepares the host for repair. Specifically, during a report faulty host operation, the following process happens:

  1. **Mark the host as faulty**. Compute Engine creates the report faulty host operation. The report faulty host operation then creates a sequence of sub-operations. These sub-operations mark the underlying host as faulty.

  2. **Prepare the host for repairs**. After all sub-operations complete, the report faulty host operation starts. Compute Engine stops the compute instance and starts the repair faulty host operation. Depending on the reservation operational mode of the reservation and host availability, Compute Engine either keeps the compute instance stopped or attempts to migrate and restart it.

  3. **Report completion and repair the host**. Compute Engine completes the report faulty host operation, and the host repair operation runs.




For more information about other operations that you can use to track repairs, migration, and automatic restart, see [Maintenance and restart behaviors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) and [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) in the Compute Engine documentation.

To track the status of the report faulty host (`compute.instances.reportHostAsFaulty`) operations in your project, select one of the following:

###  Console (Instance operations) 

  1. In the Google Cloud console, go to the **Operations** page.

[Go to Operations](https://console.cloud.google.com/compute/operations)

  2. In the table that appears, locate the compute instance that you reported.

  3. In the row that contains the compute instance, in the **Status** column, you can see the status of the report faulty host operation. When the operation completes, the value is **Done**.

  4. Optional: To verify if Compute Engine has restarted the compute instance, [view the details of the instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).




###  Console (Compute instance logs) 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Verify that the **Show query** toggle is set to the on position.

  3. In the query editor, enter the following query:
         
         resource.type="gce_instance" AND protoPayload.methodName=~"compute\.instances\.reportHostAsFaulty"
         

  4. Click **Run query**. The **Query results** pane displays the query results.




###  gcloud 

  1. To view the status of the report faulty host operations in your project, use the [`gcloud compute operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) with the `--filter` flag set to `operationType:reportHostAsFaulty`:
         
         gcloud compute operations list --filter="operationType:reportHostAsFaulty"
         

  2. If you want to view the details of a specific faulty host operation, then use the [`gcloud compute operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe):
         
         gcloud compute operations describe OPERATION_NAME \
             --zone="ZONE"
         

Replace the following:

     * `OPERATION_NAME`: the name of the operation.

     * `ZONE`: the zone where the operation exists.




###  REST 

To view the status of the report faulty host operations in your project, make a `GET` request to the [`zoneOperations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list). In the request URL, include the `filter` query parameter set to `items.operationType:reportHostAsFaulty`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations&filter=items.operationType:reportHostAsFaulty
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the operations exist.

  * `ZONE`: the zone where the operations exist.




## What's next

  * If you encounter issues when reporting a faulty host, then see [Troubleshoot faulty host API](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
