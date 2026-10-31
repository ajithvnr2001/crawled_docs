---
url: https://docs.cloud.google.com/run/docs/configuring/task-timeout/
title: Set task timeout for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:49:12.666923+00:00
---

# Set task timeout for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/task-timeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set task timeout for jobs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Long running GPU jobs**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, each task runs for a maximum of 10 minutes: you can change this to a shorter time or a longer time up to 168 hours (7 days). For tasks using GPUs, the maximum available timeout is 12 hours (preview).

**Caution:** The task timeout is the maximum time a task attempt is allowed to run. It is not a guarantee of uninterrupted execution. Tasks that use GPUs are not live migrated, so routine infrastructure maintenance terminates them. A task configured with a multi-hour timeout should be expected to be interrupted at least once before it completes.

You can set the task timeout as described on this page. There is no explicit timeout on a job execution: when all tasks are done, the job execution is done.

The units specify a duration. You can specify the timeout duration as an integer value in seconds, minutes, or hours. For example, to set the timeout duration as 10 minutes and 5 seconds, specify the value as `605` seconds.

If your job has retries enabled, the timeout setting applies to each attempt of a task. If the task attempt does not complete within this time, it will be stopped. The longer a job runs, the more likely it is to run into issues that cause it to fail, such as downstream dependency failures, out of memory errors, or infrastructure issues. We recommend enabling retries for all jobs, but especially for jobs with long-running tasks.

### Maintenance events

Tasks that don't use GPUs are live migrated during maintenance events. Tasks that use GPUs cannot be live migrated and are terminated instead; learn more.

The migration process preserves the state of the task, with one notable exception: outbound VPC network connections break during maintenance events. We recommend that you use client libraries that can handle occasional connection resets.

Cloud Run prints out a log message every time a task starts and finishes migrating.

Additionally, if you want to monitor or handle maintenance events in a specific way, you can catch the `SIGTSTP` signal, which is sent 10 seconds before a task is migrated. After migration, the task receives a `SIGCONT` signal immediately after the task is restarted.

The following Go sample is a function that catches these signals and prints out a log entry:
    
    
    func testSignals() {
        sigs := make(chan os.Signal, 1)
        signal.Notify(sigs, syscall.SIGTSTP, syscall.SIGCONT)
        go func() {
            for  {
                sig := <-sigs
                log.Printf("Got Signal: %v", sig)
            }
        }()
     }
     

### Long-running GPU jobs

In certain cases like long-running GPU jobs, maintenance events might result in preemption or termination of instances without live migration.

To handle these events gracefully, one option is to catch the `SIGTERM` signal, which Cloud Run sends 10 seconds before task termination, to save progress by writing final checkpoints and saving state to persistent storage. See [Design resilient long-running GPU jobs](https://docs.cloud.google.com/run/docs/tutorials/long-running-gpu-jobs) for more details.

However, note that you have approximately 10 seconds after `SIGTERM` before the task is killed. This is not enough time to write a large model checkpoint. Treat the `SIGTERM` handler as a best-effort flush of small state only, and rely on periodic checkpointing as your primary protection. Choose your checkpoint interval based on how much work you can afford to lose.

Because GPU tasks are not live migrated, a task configured with a multi-hour timeout should be expected to be interrupted at least once before it completes. The task timeout is a maximum, not a guarantee of uninterrupted execution.

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set task timeout

To specify task timeout for a Cloud Run job:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. In the **Task timeout** field, specify the maximum duration for the job tasks in the current job, and select a **Time unit**. You can only specify the timeout duration as an integer value in **second** , **minute** , or **hour**. For example, to set a duration of 10 minutes and 5 seconds, in the **Task timeout** field, specify `605`, and select the **Time unit** as **second**.

  5. Click **Create** or **Update**.




###  gcloud 

  1. For a job you are creating:
         
         gcloud run jobs create JOB_NAME --image IMAGE_URL --task-timeout TIMEOUT

Replace

     * JOB_NAME with the name of your job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * TIMEOUT with the maximum duration for the job tasks, specifying the amount of time and the units: for example, `10m5s` is ten minutes and five seconds.
  2. For a job you are updating:
         
         gcloud run jobs update JOB_NAME --task-timeout TIMEOUT




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `timeoutSeconds:` attribute:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE
                   timeoutSeconds: TIMEOUT

Replace:

     * JOB_NAME with the name of your job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * TIMEOUT with the maximum duration for the job tasks, specifying the amount of time and the units. You can only specify time as an integer value in seconds, minutes, or hours. For example, to set a duration of 10 minutes and 5 seconds, specify `605`.

You can also specify more configuration details, such as environment variables or memory limits.

  3. Update the existing job configuration:
         
         gcloud run jobs replace job.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "cloud-run-job-timeout"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        template {
          timeout = "3.500s"
    
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/job:latest"
          }
        }
      }
    }

## View task timeout settings

To view the current task timeout settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the task timeout setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the task timeout setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
