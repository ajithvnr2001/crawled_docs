---
url: https://docs.cloud.google.com/run/docs/tutorials/long-running-gpu-jobs/
title: Design resilient long-running GPU jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:11.065711+00:00
---

# Design resilient long-running GPU jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/long-running-gpu-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Design resilient long-running GPU jobs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Long running GPU jobs**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial explains how to design and deploy resilient, GPU-enabled Cloud Run jobs running up to 12 hours.

Although Cloud Run supports extended task timeouts, it does not offer an SLA for uninterrupted execution. Because GPU-enabled tasks are not live-migrated, routine weekly maintenance will terminate them mid-run. Consequently, any extended task should be expected to be interrupted at least once. To ensure your job finishes successfully without wasting compute resources, design your application to checkpoint and resume rather than relying on a single, uninterrupted run.

This tutorial guides you on how to implement checkpointing, handle platform `SIGTERM` signals, and configure maximum retries.

## Objectives

In this tutorial, you will do the following:

  * Prepare a Python application that implements checkpointing and handles `SIGTERM` signals.
  * Create a Cloud Storage bucket to persist checkpoints.
  * Build and deploy a Cloud Run job with GPU enabled, a 12 hour task timeout, and a configured retry policy.
  * Run the job and understand how to monitor for preemption events in the logs.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build/docs)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Run](https://docs.cloud.google.com/run)
  * [Cloud Storage](https://docs.cloud.google.com/storage)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Cloud Run, Artifact Registry, Cloud Build, and Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com storage.googleapis.com

  13. Set your region as an environment variable: 
         
         export REGION=REGION

  14. Create a service account for the job: 
         
         gcloud iam service-accounts create gpu-job-sa

  15. Ensure you have [sufficient GPU quota](/run/docs/configuring/jobs/gpu#request-quota) (e.g., Nvidia L4) in your chosen region.



## Prepare your application

To make a long-running job resilient, your application must:

  1. Periodically save progress (checkpointing) to a persistent location, such as a mounted Cloud Storage bucket.

You have approximately 10 seconds after `SIGTERM` before the task is killed. This is not enough time to write a large model checkpoint. Treat the `SIGTERM` handler as a best-effort flush of small state only, and rely on periodic checkpointing as your primary protection. Choose your checkpoint interval based on how much work you can afford to lose, bearing in mind that more frequent checkpoints mean more time not spent doing useful work. The goal is to achieve the right balance for your use case.

  2. Restore state from the last checkpoint upon startup.

  3. Listen for the `SIGTERM` signal, which Cloud Run sends 10 seconds before the maintenance process, and attempt to save a final checkpoint before exiting.




The following example illustrates how to implement these features.

### Create the application code

  1. Create a directory for your project:
         
         mkdir gc-run-gpu-resilience
         cd gc-run-gpu-resilience
         

  2. Create a file named `task.py`, and paste in the following script to simulate a training or batch process that supports checkpointing and signal handling:
         
         import os
         import sys
         import time
         import signal
         
         # The checkpoint directory will be mounted to this path
         CHECKPOINT_DIR = "/checkpoints"
         # Cloud Run sets these variables automatically
         JOB_NAME = os.environ.get("CLOUD_RUN_JOB", "local-job")
         TASK_INDEX = os.environ.get("CLOUD_RUN_TASK_INDEX", "0")
         CHECKPOINT_FILE = os.path.join(
             CHECKPOINT_DIR, f"{JOB_NAME}-task-{TASK_INDEX}-checkpoint.txt")
         TOTAL_STEPS = 100
         current_step = 0
         is_exiting = False
         
         def save_checkpoint(step):
             print(f"Saving checkpoint at step {step} to {CHECKPOINT_FILE}...")
             try:
                 # Write to a temp file and rename to ensure atomicity
                 temp_file = CHECKPOINT_FILE + ".tmp"
                 with open(temp_file, "w") as f:
                     f.write(str(step))
                 os.rename(temp_file, CHECKPOINT_FILE)
                 print("Checkpoint saved successfully.")
             except Exception as e:
                 print(f"Failed to save checkpoint: {e}")
         
         def load_checkpoint():
             print(f"Looking for a checkpoint at {CHECKPOINT_FILE}...")
             global current_step
             if os.path.exists(CHECKPOINT_FILE):
                 try:
                     with open(CHECKPOINT_FILE, "r") as f:
                         current_step = int(f.read().strip())
                     print(f"Resuming from checkpointed step {current_step}.")
                 except Exception as e:
                     print(f"Failed to load checkpoint: {e}. Starting from scratch.")
             else:
                 print("No checkpoint found. Starting from scratch.")
         
         def sigterm_handler(signum, frame):
             global is_exiting
             print("Received SIGTERM signal from platform. Initiating graceful shutdown...")
             is_exiting = True
         
         # Register the signal handler for SIGTERM
         signal.signal(signal.SIGTERM, sigterm_handler)
         
         # Load existing checkpoint if any to resume work
         load_checkpoint()
         
         # Simulate work loop
         while current_step < TOTAL_STEPS and not is_exiting:
             print(f"Processing step {current_step}/{TOTAL_STEPS}...")
             # Simulate heavy GPU computation
             time.sleep(1)
             current_step += 1
             # Periodically save checkpoint (e.g., every 5 steps)
             if current_step % 5 == 0:
                 save_checkpoint(current_step)
         
         if is_exiting:
             # Save final state before exiting due to preemption
             # Best-effort only: with ~10s before SIGKILL this will not complete for
             # large state. Periodic checkpointing (above) is what actually protects
             # you.
             save_checkpoint(current_step)
             # Note that save_checkpoint already writes-then-renames for atomicity,
             # which is good, but the reason it matters here is that a truncated
             # checkpoint from an interrupted final save must not clobber the last
             # good one.
             print("Graceful shutdown complete. Exiting with error code to trigger retry.")
             # Exit with a non-zero code to signal to Cloud Run that the task
             # was interrupted and needs to be retried from the checkpoint.
             sys.exit(143)
             # Note that this statement deliberately consumes of the configured retry
             # attempts.
         
         print("Task completed successfully.")
         sys.exit(0)
         

  3. Create a `Dockerfile` to containerize the application:




See this [example](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/ai-ml/finetune_gemma/README.md) for a more detailed, realistic implementation.

## Create a Cloud Storage bucket for checkpoints

Create a Cloud Storage bucket to store the checkpoint files, and grant your job's service account permission to access it.

  1. Create the bucket:
         
         gcloud storage buckets create gs://gpu-checkpoints-PROJECT_ID \
             --location REGION
         

  2. Grant the Storage Object Admin role to the job's service account:
         
         gcloud storage buckets add-iam-policy-binding gs://gpu-checkpoints-PROJECT_ID \
             --member="serviceAccount:gpu-job-sa@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/storage.objectAdmin"
         




## Deploy the job

Deploy the job to Cloud Run:
    
    
    gcloud beta run jobs deploy gpu-resilient-job \
        --source=. \
        --region REGION \
        --gpu 1 \
        --gpu-type nvidia-l4 \
        --no-gpu-zonal-redundancy \
        --task-timeout 168h \
        --max-retries 3 \
        --service-account gpu-job-sa@PROJECT_ID.iam.gserviceaccount.com \
        --add-volume=name=checkpoint-volume,type=cloud-storage,bucket=gpu-checkpoints-PROJECT_ID \
        --add-volume-mount=volume=checkpoint-volume,mount-path=/checkpoints
    

Note the following critical flags:

  * `--task-timeout 168h`: Allows the task to run for up to 12 hours.
  * `--max-retries 3`: For GPU jobs with a timeout greater than 1 hour, we recommend setting the default configuration of 3 retries. To prevent silent failures during platform maintenance, we recommend against setting 0 retries. Finally, we recommend budgeting for at least 1 retry for maintenance-related failure as well as for additional retries for application failures over a 12 hour execution period.
  * `--add-volume` and `--add-volume-mount`: Mounts the Cloud Storage bucket to `/checkpoints` so the application can persist state across task retries.

**Caution:** Note that timeout is per attempt, the total exposure is timeout x (retries + 1), and that GPU time is billed for the full duration of each attempt.



## Run and monitor the job

  1. Execute the job:
         
         gcloud run jobs execute gpu-resilient-job --region REGION
         

This command returns a message resembling the following:
         
         Execution [gpu-resilient-job-abcde] has been successfully started.
         
         View details about this execution by running `gcloud run jobs executions
         describe gpu-resilient-job-abcde`.
         
         See logs for this execution at: https://console.cloud.google.com/logs/viewer?project=YOUR_PROJECT_ID&resource=cloud_run_job/job_name/my-job/location/my-region/execution_id/gpu-resilient-job-abcde
         

The string `gpu-resilient-job-abcde` is the auto-generated unique ID for this specific execution attempt. You can use it to monitor or cancel this specific run. The output also includes a direct link to the Logs Explorer page in the Google Cloud console to view output or errors from your job tasks.

  2. Monitor the logs. If a maintenance event occurs, Cloud Run logs a warning. You will see:

     * Your application logs: `Received SIGTERM signal from platform. Initiating graceful shutdown...` followed by `Saving checkpoint...`.
     * A system log indicating preemption: `Container instance preemption initiated by the platform due to underlying hardware maintenance.` with reason `INSTANCE_PREEMPTED`.
     * Cloud Run automatically restarting the task.
     * Your application logs upon restart: `Resuming from checkpointed step X.`.



## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this quickstart.

### Delete your repository

Cloud Run only charges for the time your job executes. However, you might still be [charged for storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing). To delete Artifact Registry repositories, follow the steps in [Delete repositories](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#delete) in the Artifact Registry documentation.

### Delete your job

Cloud Run jobs only incur cost when a job task is executing. To delete your Cloud Run job, follow one of these steps:

### Console

To delete a job:

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Locate the job you want to delete in the jobs list, and click its checkbox to select it.

  3. Click **Delete**. This terminates all the job executions in progress and all running container instances.




###  gcloud 

To delete a job, run the following command:
    
    
    gcloud run jobs delete JOB_NAME

Replace `JOB_NAME` with the name of the job.

### Delete your test project

Deleting your Google Cloud project stops billing for all resources in that project. To release all Google Cloud resources in your project, follow these steps:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




Delete the Cloud Storage bucket:
    
    
    gcloud storage buckets delete gs://gpu-checkpoints-PROJECT_ID
    

## What's next

  * Learn more about [Jobs retries and checkpoints](https://docs.cloud.google.com/run/docs/jobs-retries).
  * Review [GPU performance best practices](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
