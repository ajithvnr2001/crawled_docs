---
url: https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager/
title: Troubleshooting VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T08:52:03.406046+00:00
---

# Troubleshooting VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Troubleshooting VM Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to troubleshoot issues with VM Manager.

For more information about VM Manager, see [VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Overview

To troubleshoot issues, first verify that VM Manager [is set up properly](https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/verify-setup). If the setup is correct and you have still have issues, you can then review logs. When you review logs, you can identify issues with your VM or in your VM Manager workflow, such as errors in commands or scripts, that you can isolate and resolve.

You can collect the following information from logs:

  * Any error message or warning logged by the VM. These logs help you identify VM-level errors, or errors from other services running on your VM. To review these logs, see Inspect Cloud Logging.

  * Verbose debug information logged by the OS Config agent. These logs help you identify issues with any of the operations run by VM Manager. To inspect debug logs for the OS Config agent, see Inspect debug logs.




After you identify the issues or errors, you can also review the common errors section to see potential fixes, or see the workaround for managing patch deployments across an organization.

## Inspect Cloud Logging

You can use the Google Cloud console quick links for each feature to view logs.

### OS patch

  1. In the Google Cloud console, go to the **Jobs run** tab on the **Patch** page. 

[ Go to Jobs run](https://console.cloud.google.com/compute/patch/jobs)

  2. Click the name of the patch job that you want to debug.
  3. Go to the **Updated VM instances** section.
  4. For a specific VM, under **Logs** , click **View**.



### OS policies

This procedure is supported for OS policies. For guest policies (beta), use the debug logs option, in the following section.

  1. In the Google Cloud console, go to the **VM instances** tab on the **OS policies** page. 

[ Go to VM instances](https://console.cloud.google.com/compute/config/instances)

  2. Click the name of the VM that you want to debug.
  3. Go to the **Policies** section.
  4. Under **Logs** , click **View**.



### OS policy orchestrators

  1. In the Google Cloud console, go to the **OS policy orchestrators** tab on the **OS policies** page. 

[ Go to OS policy orchestrators](https://console.cloud.google.com/compute/config/orchestrators)

  2. Click the name of the OS policy orchestrator that you want to debug.
  3. Go to the **Logs** section and verify the log entry.



## Inspect debug logs

You can identify issues with any VM Manager feature by enabling debugging for the OS Config agent and viewing debug log.

### Enable debug logging for the OS Config agent

You can enable debug logging by setting the `osconfig-log-level=debug` metadata on the VM instance or project.

To enable debug logging on your VM, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM for which you want to set the metadata value.

  3. On the **Instance details** page, click **Edit** to edit the settings.

  4. Under **Custom metadata** , add the following metadata entries:

Key: `osconfig-log-level`  
Value: `debug`

  5. Click **Save** to apply your changes to the VM.




###  gcloud 

Use the [`instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata) with the `--metadata=osconfig-log-level=debug` flag.
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata=osconfig-log-level=debug
    

Replace `VM_NAME` with the name of your VM.

###  REST 

For instructions on setting instance metadata, follow the API instructions for [setting instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#updatinginstancemetadata).

The following key-value pair is required as part of the metadata property:

Key: `osconfig-log-level`  
Value: `debug`

### View debug logs

When debug logging is enabled, the OS Config agent writes log entries to Cloud Logging and the serial port console.

After you enable debug logging on your VM, it takes the OS Config agent approximately ten minutes to start writing debug messages in Cloud Logging. You can reduce this wait time by restarting the agent or rebooting your VM. For more information about Cloud Logging, see [Viewing Cloud Logging logs](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud#explore).

To view debug logs you can use the following options:

  * Cloud Logging: use the Google Cloud console or Google Cloud CLI
  * Serial port console




###  Console 

  1. Go to the **Logging > Logs Explorer** (Logs Explorer) page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. If needed, select an existing Google Cloud project at the top of the page, or create a new project.

  3. In the **Resource** drop-down list, select **VM Instance**. A list of available VMs (`instance_id`) displays.

  4. Click the VM that you want to view.

  5. Click **Add**.

  6. In the **Log name** drop-down list, select **OSConfigAgent**.

  7. Click **Add**.

  8. Your query should be similar to the following:
         
         resource.type="gce_instance" resource.labels.instance_id="INSTANCE_ID"
         logName="projects/PROJECT_ID/logs/OSConfigAgent"
         

  9. Click **Run query**.




###  gcloud 

Run the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).
    
    
     gcloud logging read "resource.type=gce_instance AND logName=projects/PROJECT_ID/logs/OSConfigAgent"
     

Replace `PROJECT_ID` with your project ID.

###  Serial port 

To view debug log information from the serial port console, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output).

## Common errors

### Authentication issues

For VM Manager to work, you must have the following:

  * An attached service account. VM Manager uses this service account to sign requests to the API service.
  * Make sure that the attached service account has the [`roles/logging.logWriter`](https://docs.cloud.google.com/iam/docs/understanding-roles?hl=en#logging-roles) role to write logs to the Logging API.
  * [Google Cloud OS Config Service Agent](https://docs.cloud.google.com/compute/vm-manager/docs/overview#service-agent). VM Manager creates this service agent when starting patch jobs and gives it the Cloud OS Config Service Agent role. To create OS policies, you need not configure this service agent.



If you use VM Manager and you don't have an attached service account, or a Google Cloud OS Config Service Agent, you might see the following errors while working with patch jobs:
    
    
    Service account permissions are missing. Verify that the service account has the correct permissions and try again.
    
    
    OSConfigAgent Error main.go:88: error getting token from metadata: metadata: GCE metadata "instance/service-accounts/default/identity?audience=osconfig.googleapis.com&format=full" not defined
    
    
    message: "Error running OPERATION_NAME: error calling OPERATION_NAME: code: "PermissionDenied", message: "The caller does not have permission", details: []"
    

Authentication issues might also prevent VM instances from showing up on the [Patch dashboard](https://docs.cloud.google.com/compute/vm-manager/docs/patch#dashboard).

To resolve these issues, try one or all of the following:

  * Verify that all VMs have an [attached service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-to-resources).
  * Ensure that the Cloud OS Config Service Agent role (`roles/osconfig.serviceAgent`) is set on the Google Cloud OS Config Service Agent.
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
          --member='serviceAccount:service-PROJECT_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com' \
          --role='roles/osconfig.serviceAgent'
        

Replace the following:

    * `PROJECT_ID`: your project ID
    * `PROJECT_NUMBER`: your [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)



### Error when excluding packages for patch updates

If you specify wildcards or special characters for the name of packages when excluding packages in a patch job, OS patch management might ignore the list and update all packages.

To resolve this issue, [update the OS Config agent](https://docs.cloud.google.com/compute/vm-manager/docs/upgrade-vm-manager#update-agent) to version `20220829.00` and use forward slashes (`/`) to wrap the package name.

In the following example, OS patch management excludes `yum` packages with prefix `google-` in the package name.
    
    
          gcloud compute os-config patch-jobs execute --instance-filter-all   
    
            --yum-excludes=/google-.*/
        

## Workaround for managing patch deployments across an organization

[Patch deployments](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs) and [patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job) are scoped to individual Google Cloud projects, unlike [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/about-policy-orchestrator), which you can orchestrate across an organization or folder by using policy orchestrators.

As a workaround to manage patch deployments at scale, you can use Cloud Asset Inventory and the Google Cloud CLI in a Bash script to iterate through all projects in your organization. This script lets you complete the following tasks:

  1. Enable VM Manager across projects

  2. Create a patch deployment across projects

  3. Export patch job results across projects to CSV




### Required permissions and organization ID

Before you run the scripts in this section, ensure that you have the required Identity and Access Management (IAM) permissions and your organization ID:

  * **Organization level** : to list all projects in your organization by using Cloud Asset Inventory, your user account or service account must have the `cloudasset.assets.searchAllResources` permission (included in the Cloud Asset Viewer role, `roles/cloudasset.viewer`) on the organization.

  * **Target project level** : depending on the tasks that you run across your organization, your user account or service account must have the following permissions on each target project (for example, inherited from an organization-level role binding):

    * To enable the OS Config API and set project metadata: `serviceusage.services.enable` (Service Usage Admin, `roles/serviceusage.serviceUsageAdmin`) and `compute.projects.setCommonInstanceMetadata` (Compute Instance Admin (v1), `roles/compute.instanceAdmin.v1`).

    * To create patch deployments: `osconfig.patchDeployments.create` (OS Config Patch Deployment Admin, `roles/osconfig.patchDeploymentAdmin`).

    * To list patch jobs and view VM instance details: `osconfig.patchJobs.list` and `osconfig.patchJobs.get` (OS Config Patch Job Viewer, `roles/osconfig.patchJobViewer`).




To find your organization ID, run the [`gcloud projects get-ancestors` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-ancestors) for any project in your organization:
    
    
    gcloud projects get-ancestors PROJECT_ID
    

Replace `PROJECT_ID` with the ID of a project in your organization. The output lists the project's parent folders and the `organization` ID.

### Enable VM Manager across projects

To enable VM Manager across all existing and future projects in an organization or folder, Google recommends using [hierarchical service activation and organization policies](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-api-hierarchical) or [Terraform](https://docs.cloud.google.com/compute/vm-manager/docs/vm-manager-org-terraform).

Alternatively, to enable the OS Config API (`osconfig.googleapis.com`) and set the `enable-osconfig=TRUE` project metadata across all existing projects in your organization by using a Bash script, run the following command:
    
    
    for project in $(gcloud asset search-all-resources \
        --scope=organizations/ORGANIZATION_ID \
        --asset-types=cloudresourcemanager.googleapis.com/Project \
        --format="csv(additionalAttributes.projectId)" | sed 1d | sort); do
      gcloud services enable osconfig.googleapis.com --project="$project"
      gcloud compute project-info add-metadata --project="$project" \
          --metadata=enable-osconfig=TRUE
    done
    

Replace `ORGANIZATION_ID` with your organization ID.

### Create a patch deployment across projects

To apply a standardized patch deployment schedule across all projects in your organization, create a patch deployment configuration file and apply it to each project:

  1. Create a JSON or YAML template file named `patch_deployment_template.json` that defines your target instance filter, patch configuration, and schedule. For more information about the supported configuration fields, see [Creating a patch deployment](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs#create-patch-deployment) and the [`PatchDeployment` resource reference](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments#PatchDeployment).

For example, the following `patch_deployment_template.json` file schedules a recurring weekly patch job every Tuesday at 7:30 PM in the `America/Los_Angeles` time zone for all VM instances in a project:
         
         {
           "instanceFilter": {
             "all": true
           },
           "patchConfig": {
             "rebootConfig": "DEFAULT"
           },
           "recurringSchedule": {
             "frequency": "WEEKLY",
             "weekly": {
               "dayOfWeek": "TUESDAY"
             },
             "timeOfDay": {
               "hours": 19,
               "minutes": 30
             },
             "timeZone": {
               "id": "America/Los_Angeles"
             }
           }
         }
         

  2. Run the following loop to create the patch deployment in each project across your organization by using the [`gcloud compute os-config patch-deployments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create):
         
         for project in $(gcloud asset search-all-resources \
             --scope=organizations/ORGANIZATION_ID \
             --asset-types=cloudresourcemanager.googleapis.com/Project \
             --format="csv(additionalAttributes.projectId)" | sed 1d | sort); do
           gcloud compute os-config patch-deployments create patch-"$project" \
               --project="$project" \
               --file=patch_deployment_template.json
         done
         

Replace `ORGANIZATION_ID` with your organization ID.




### Export patch job results across projects to CSV

To audit patch job results, you can use the [`gcloud compute os-config patch-jobs list-instance-details` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/list-instance-details) to export VM instance details for failed or succeeded patch jobs to a CSV file.

  * **Single patch job** : to export the VM instances that failed or succeeded in a specific patch job, run the following commands:

    * Export failed VM instances:
          
          gcloud compute os-config patch-jobs list-instance-details PATCH_JOB_ID \
              --project=PROJECT_ID \
              --filter="state:(FAILED OR TIMED_OUT OR NO_AGENT_DETECTED)" \
              --format="csv(name.basename():label=INSTANCE_NAME,zone:label=ZONE,state:label=STATE,failureReason:label=FAILURE_REASON)" > failed_patches.csv
          

    * Export succeeded VM instances:
          
          gcloud compute os-config patch-jobs list-instance-details PATCH_JOB_ID \
              --project=PROJECT_ID \
              --filter="state=SUCCEEDED" \
              --format="csv(name.basename():label=INSTANCE_NAME,zone:label=ZONE,state:label=STATE,attemptCount:label=ATTEMPT_COUNT)" > succeeded_patches.csv
          

Replace the following:

    * `PATCH_JOB_ID`: the ID of the patch job

    * `PROJECT_ID`: the project ID

  * **All projects in an organization** : to iterate through all projects in your organization and export failed and succeeded VM instances across patch jobs into CSV files, run the following script:
        
        echo "PROJECT_ID,PATCH_JOB_ID,INSTANCE_NAME,ZONE,STATE,FAILURE_REASON" > failed_patches.csv
        echo "PROJECT_ID,PATCH_JOB_ID,INSTANCE_NAME,ZONE,STATE,ATTEMPT_COUNT" > succeeded_patches.csv
        
        for project in $(gcloud asset search-all-resources \
            --scope=organizations/ORGANIZATION_ID \
            --asset-types=cloudresourcemanager.googleapis.com/Project \
            --format="csv(additionalAttributes.projectId)" | sed 1d | sort); do
          for job in $(gcloud compute os-config patch-jobs list \
              --project="$project" \
              --format="value(name.basename())"); do
            gcloud compute os-config patch-jobs list-instance-details "$job" \
                --project="$project" \
                --filter="state:(FAILED OR TIMED_OUT OR NO_AGENT_DETECTED)" \
                --format="csv[no-heading](name.basename(),zone,state,failureReason)" | \
                sed "s/^/${project},${job},/" >> failed_patches.csv
            gcloud compute os-config patch-jobs list-instance-details "$job" \
                --project="$project" \
                --filter="state=SUCCEEDED" \
                --format="csv[no-heading](name.basename(),zone,state,attemptCount)" | \
                sed "s/^/${project},${job},/" >> succeeded_patches.csv
          done
        done
        

Replace `ORGANIZATION_ID` with your organization ID.

By default, the `gcloud compute os-config patch-jobs list` command returns up to 10 patch jobs per project. To export results from only the most recent patch job in each project, add `--sort-by="~update_time" --limit=1` to the `gcloud compute os-config patch-jobs list` command.




For organization-wide patch compliance and vulnerability reporting in the Google Cloud console or BigQuery, see [View patch summary for VMs in an organization or folder](https://docs.cloud.google.com/compute/vm-manager/docs/patch/view-patch-summary#patch-summary) and [View vulnerability reports for your organization](https://docs.cloud.google.com/compute/vm-manager/docs/patch/view-org-vulnerability-reports).

## What's next?

  * [Manage your patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).
  * [Manage OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
