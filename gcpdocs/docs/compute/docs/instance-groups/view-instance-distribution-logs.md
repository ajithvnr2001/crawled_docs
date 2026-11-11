---
url: https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-distribution-logs/
title: View instance distribution logs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:19:58.746953+00:00
---

# View instance distribution logs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-distribution-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View instance distribution logs Stay organized with collections  Save and categorize content based on your preferences. 

When you create a regional managed instance group (MIG) or increase its target size, Compute Engine evaluates real-time resource availability to distribute new compute instances across zones and machine types. During this process, Compute Engine records an instance distribution log entry in Cloud Logging.

This document describes how to view and interpret these instance distribution logs. It also explains how to use these logs to investigate pending allocations and configure alerts.

To see the actual distribution of your running instances, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

## About instance distribution logs

Instance distribution logs provide a one-time snapshot of the MIG's planned allocations for compute instances. In these logs, an _allocated_ instance means that the MIG found capacity and plans to create the compute instance on that machine type and in that zone. An allocated size doesn't mean that the compute instances are successfully created yet.

Because the logs provide a snapshot, Compute Engine doesn't update these logs when the MIG creates the remaining compute instances later. The log entry lets you view the following details:

  * **Machine type distribution** : the number of compute instances that the MIG has allocated per machine type. This information is present only for regional MIGs that use [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

  * **Zonal distribution** : the number of compute instances that the MIG has allocated per zone.

  * **Instances awaiting capacity** : the number of instances for which the MIG couldn't allocate capacity immediately and is actively seeking capacity.




## Limitations

  * Instance distribution logs are available only for regional MIGs.

  * For regional MIGs that use the `EVEN` target distribution shape without autoscaling, the log entry includes only the `oldSize`, `newSize`, `deltaSize`, and `targetShape` fields, without any instance distribution details.

  * Compute Engine logs instance distribution details only when you create a MIG or increase its target size. Compute Engine doesn't log these details when the target size decreases, or during instance repair, recreate, and update operations.




## View instance distribution logs of a specific MIG

To view the instance distribution logs of a specific MIG, use one of the following options:

###  Console 

You can view the logs for a specific MIG directly from the instance group details page.

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG that you want to view.

  3. Click the **Monitoring** tab.

  4. In the left pane, select **Logs**.

  5. In the log results filter, type `instanceDistribution`, and press `Enter`.

  6. To view the instance distribution data, expand a log entry and then expand `protoPayload.metadata.details`.




###  gcloud 

To view the instance distribution logs of a specific MIG, use the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read):
    
    
    gcloud logging read "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND \
      protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\" AND \
      resource.labels.instance_group_manager_name=\"MIG_NAME\""
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `MIG_NAME`: the name of the MIG.




###  REST 

To view the instance distribution logs of a specific MIG, make a `POST` request to the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list).
    
    
    POST https://logging.googleapis.com/v2/entries:list
    {
    "resourceNames": [
      "projects/PROJECT_ID"
    ],
    "filter": "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\" AND resource.labels.instance_group_manager_name=\"MIG_NAME\""
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `MIG_NAME`: the name of the MIG.




For more information about each field in a log, see Instance distribution log entry.

## View all instance distribution logs in a project

To view all instance distribution logs in a project, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter a query. The following are some examples:

     * To view all instance distribution logs in the project:
           
           logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
           protoPayload.methodName="compute.instanceGroupManagers.instanceDistribution"
           

     * To view the instance distribution logs where part of the resize is still waiting for capacity:
           
           logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
           protoPayload.methodName="compute.instanceGroupManagers.instanceDistribution"
           protoPayload.metadata.details.data.activeSeekDeltaSize > 0
           

Replace `PROJECT_ID` with the ID of your project.

  3. Click **Run query**.

  4. In the results, expand a log entry.

     * To see the summary and the data, expand `protoPayload.metadata.details`.
     * To see the summary on each row, click `message` and select **Add field to summary line**.



###  gcloud 

To view the instance distribution logs, use the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).

  * To view all instance distribution logs in the project:


    
    
    gcloud logging read "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND \
      protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\""
    

  * To view all logs in the project from the last day, specify the `--freshness=1d` flag as follows:


    
    
    gcloud logging read "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND \
        protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\"" \
        --freshness=1d
    

  * To view the instance distribution logs where part of the resize is still waiting for capacity:


    
    
    gcloud logging read "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND \
        protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\" AND \
        protoPayload.metadata.details.data.activeSeekDeltaSize > 0"
    

Replace `PROJECT_ID` with the ID of your project.

###  REST 

To view the instance distribution logs, make a `POST` request to the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list).

  * To view all instance distribution logs in the project:


    
    
    POST https://logging.googleapis.com/v2/entries:list
    {
      "resourceNames": [
        "projects/PROJECT_ID"
      ],
      "filter": "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\""
    }
    

  * To view all logs in the project from the last day, add a `timestamp` condition to the filter:


    
    
    POST https://logging.googleapis.com/v2/entries:list
    {
      "resourceNames": [
        "projects/PROJECT_ID"
      ],
      "filter": "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\" AND timestamp >= \"YYYY-MM-DDThh:mm:ssZ\""
    }
    

  * To view the instance distribution logs where part of the resize is still waiting for capacity:


    
    
    POST https://logging.googleapis.com/v2/entries:list
    {
      "resourceNames": [
        "projects/PROJECT_ID"
      ],
      "filter": "logName=\"projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event\" AND protoPayload.methodName=\"compute.instanceGroupManagers.instanceDistribution\" AND protoPayload.metadata.details.data.activeSeekDeltaSize > 0"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `YYYY-MM-DDThh:mm:ssZ`: the RFC 3339 timestamp for the start time—for example, `2024-10-22T00:00:00Z`.




For more information about each field in a log, see Instance distribution log entry.

## Instance distribution log entry

The following is a sample log entry (`protoPayload.metadata.details`). Because this event is a one-time snapshot, the log entry isn't updated when the remaining instances are created later. The log entry lets you view the details as follows:

  * **`details.data`** : shows the structured details about the instance distribution.

  * **`details.message`** : shows the summary of the instance distribution.




In this example, a regional MIG with instance flexibility is scaling out from `0` to `100`. The MIG immediately allocates `80` of the `100` new instances across two ranked instance selections (`20` `c2-standard-4` instances in `rank2-c2` selection and `60` `n2d-standard-4` instances in `rank3-n2d` selection). The entry also shows that `40` compute instances are allocated in `us-central1-b` and `us-central1-c` each. For the remaining `20` instances (`activeSeekDeltaSize`), the MIG continues to seek capacity across all configured instance selections and zones. For regional MIGs without instance flexibility, the log entry omits the `instanceSelections` field and shows only the zonal distribution.
    
    
    "metadata": {
      "details": {
        "data": {
          "oldSize": 0,
          "newSize": 100,
          "deltaSize": 100,
          "targetShape": "BALANCED",
          "activeSeekDeltaSize": 20,
          "instanceSelections": {
            "rank1-n2": {
              "rank": 1,
              "machineSelections": [
                {
                  "machineType": "n2-standard-4",
                  "allocatedSize": 0
                }
              ]
            },
            "rank2-c2": {
              "rank": 2,
              "machineSelections": [
                {
                  "machineType": "c2-standard-4",
                  "allocatedSize": 20
                }
              ]
            },
            "rank3-n2d": {
              "rank": 3,
              "machineSelections": [
                {
                  "machineType": "n2d-standard-4",
                  "allocatedSize": 60
                }
              ]
            }
          },
          "zonalDistribution": {
            "us-central1-a": {
              "allocatedSize": 0
            },
            "us-central1-b": {
              "allocatedSize": 40
            },
            "us-central1-c": {
              "allocatedSize": 40
            }
          }
        },
        "message": "Increasing MIG target size from 0 to 100 instances (+100).
        Allocated 80 of 100 new instances. Allocated instances across instance
        selections: rank2-c2 (rank 2; c2-standard-4: 20); rank3-n2d (rank 3;
        n2d-standard-4: 60). Allocated instances across zones based on target
        distribution shape BALANCED: us-central1-a: 0, us-central1-b: 40,
        us-central1-c: 40. MIG continues to allocate the remaining 20 new instances
        across all instance selections and zones. The final distribution across zones
        and machine types may differ as instances are created. View the group's
        instances for the current distribution."
      }
    }
    

The following table describes each field in a log entry.

Field | Description  
---|---  
`details.data.oldSize` | The target size of the regional MIG before the resize operation.  
`details.data.newSize` | The requested target size of the regional MIG.  
`details.data.deltaSize` |  The change in the target size (`newSize - oldSize`).   
`details.data.targetShape` |  The target distribution shape of the regional MIG.   
`details.data.activeSeekDeltaSize` | The number of new instances for which the MIG is still seeking capacity across configured instance selections and zones. This field is omitted when its value is `0`.   
`details.data.instanceSelections` |  The configured instance selections evaluated during the allocation. This field is present only for MIGs that use [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility). Each key is the name of an instance selection, and its value contains the following fields: 

  * `rank`: the priority rank configured for the instance selection. 
  * `machineSelections`: a list of machine type allocations within the selection, where each entry specifies the machine type (`machineType`) and the number of compute instances allocated using that machine type (`allocatedSize`). 

  
`details.data.zonalDistribution` |  The configured zones and their allocated instance distribution. Each key is a zone name, and its value contains the number of compute instances allocated in that zone (`allocatedSize`).   
`details.message` |  A summary message describing the instance distribution, including allocated counts and seeking capacity details.   
  
## Interpret instance distribution logs

The instance distribution log provides a snapshot of the MIG's plan for compute instance creation. Because the log indicates that the MIG allocates compute instances before they are successfully created, you should use the log data alongside compute instance status and error messages to understand your MIG's actual behavior.

Use the following table to interpret common log outputs and determine if you need to take action:

Log output | Explanation | Recommended action  
---|---|---  
**`activeSeekDeltaSize` is greater than `0`** | The MIG couldn't find enough capacity to fulfill the entire resize request immediately. The MIG keeps trying to create the remaining instances across all configured options. | Check the MIG's instance errors to see why instance creation has failed. Consider adding machine types from other machine families, adding zones, or checking your quotas.  
**A higher-preference (lower rank number) selection has an`allocatedSize` of `0`** | At decision time, the MIG checked your most preferred machine types but didn't find enough capacity. The MIG used a lower-preference (higher rank number) selection instead. Compute Engine doesn't log instance errors for skipped selections. | If the MIG skips your most preferred selection often, then consider adding more machine types to your most preferred selection or accepting lower-preference options.  
**A configured zone has an`allocatedSize` of `0`** | The MIG didn't allocate any new instances in this zone. | If your target shape is `ANY` or `ANY_SINGLE_ZONE`, this uneven distribution is normal. Otherwise, review your quota, reservations, and zone support for your instance template.  
**A machine type is missing from the`message` summary** | The MIG didn't use that machine type for allocation. | Check the structured `details.data` block. The summary message leaves out selections and machine types that got `0` new instances, but the structured data lists all evaluated options.  
  
## Check pending instance allocations

If your MIG is still waiting for capacity (`activeSeekDeltaSize > 0`), then you can check the following to understand the reasons behind the pending allocations:

  * **Check instance creation errors.** To see if instance creation failed after the MIG allocated capacity, or if compute instances are still waiting for capacity, check the instance errors. For more information, see [List instance errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors).

  * **Check instance status.** To see the status and current action of each instance, list the instances in the MIG and check their `instanceStatus` field. For more information, see [Check the status of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

  * **Review your configuration.** If you've configured an instance flexibility policy in the MIG, then review your regional quotas for the machine families in the policy. Also, verify that your selected zones support the requested machine types. For more information, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage) and [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).




## Create alerting policies based on logs

To get notified when MIG resize operations wait for capacity, you can create a log-based alerting policy in **Logs Explorer**. For example, you can trigger an alert when `activeSeekDeltaSize` is greater than `0`.

To create this alert, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query:
         
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
         protoPayload.methodName="compute.instanceGroupManagers.instanceDistribution"
         protoPayload.metadata.details.data.activeSeekDeltaSize > 0
         

Replace `PROJECT_ID` with the ID of your project.

  3. Click **Run query** to validate the query.

  4. Create the alerting policy by following the instructions in the [create a log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition) section of the Cloud Logging documentation.




## What's next

  * Learn [how regional MIGs distribute compute instances across zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
  * Learn [how multiple machine type selection works in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).
  * [View instance flexibility configuration](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration) in a MIG.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
