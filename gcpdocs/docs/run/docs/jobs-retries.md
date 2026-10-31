---
url: https://docs.cloud.google.com/run/docs/jobs-retries/
title: Jobs retries and checkpoints best practices \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:50:07.726958+00:00
---

# Jobs retries and checkpoints best practices  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/jobs-retries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Jobs retries and checkpoints best practices Stay organized with collections  Save and categorize content based on your preferences. 

Individual job tasks or even job executions can fail for a variety of reasons. This page contains best practices to handle these failures, centered around task restarts and job checkpointing.

## Use task retries

Individual job tasks can fail for a variety of reasons, including issues with application dependencies, quotas, or even internal system events. Often such issues are transient and the task will succeed after a retry.

By default, each task will automatically retry up to 3 times. This helps ensure a job will run to completion even if it encounters transient task failures. You can also [customize the maximum number of retries](https://docs.cloud.google.com/run/docs/configuring/max-retries). However, if you do change the default, you should specify at least one retry.

### Plan for job task restarts

Make your jobs [idempotent](https://en.wikipedia.org/wiki/Idempotence), so that a task restart does not result in corrupt or duplicate output. That is, write repeatable logic that has the same behavior for a given set of inputs no matter how many times it is repeated or when it is executed.

Write your output to a different location than the input data, leaving input data intact. This way, if the job runs again, the job can repeat the process from the beginning and get the same result.

Avoid duplicating output data by reusing the same unique identifier or checking if the output already exists. Duplicate data represents _collection-level_ data corruption.

## Use checkpointing

Where possible, use checkpointing when designing your jobs. If a task fails and restarts, checkpointing allows it to resume from its last saved state rather than starting over—speeding up your runtimes and minimizing unnecessary costs.

To implement checkpointing:

  * Save progress: Periodically write partial results and progress markers to a persistent store, such as Cloud Storage or a database.

  * Check on startup: Configure your tasks to look for and resume from these partial results when starting up.

  * Enable retries: Configure multiple retries to safeguard your job against preemption events.




If your job cannot be checkpointed, divide the workload into smaller chunks and run a larger number of tasks instead.

### Checkpointing example 1: calculating Pi

If you have a job that executes a recursive algorithm, such as calculating Pi to many decimal places, and uses parallelism set to a value of 1:

  * Write your progress every 10 minutes or whatever your lost work tolerance allows, to a `pi-progress.txt` Cloud Storage object.
  * When a task starts, query the `pi-progress.txt` object and load the value as a starting place. Use that value as the initial input to your function.
  * Write your final result to Cloud Storage as an object named `pi-complete.txt` to avoid duplication via parallel or repeated execution or `pi-complete-DATE.txt` to differentiate by completion date.



### Checkpointing example 2: processing 10,000 records from Cloud SQL

If you have a job processing 10,000 records in a relational database such as Cloud SQL:

  * Retrieve records to be processed with a SQL query such as `SELECT * FROM example_table LIMIT 10000`
  * Write out updated records in batches of 100 so significant processing work is not lost on interruption.
  * When records are written, note which ones have been processed. You might add a boolean column processed to the table which is set to 1 only if processing is confirmed.
  * When a task starts, the query used to retrieve items for processing should add the condition processed = 0.
  * In addition to clean retries, this technique also supports breaking up work into smaller tasks, such as by modifying your query to select 100 records at a time: `LIMIT 100 OFFSET $CLOUD_RUN_TASK_INDEX*100`, and running 100 tasks to process all 10,000 records. `CLOUD_RUN_TASK_INDEX` is a built-in environment variable present inside the container running Cloud Run jobs.



Using all these pieces together, the final query might look like this: `SELECT * FROM example_table WHERE processed = 0 LIMIT 100 OFFSET $CLOUD_RUN_TASK_INDEX*100`

### Checkpointing example 3: Application-level checkpointing and task retries

GPU-enabled jobs can be configured with a task timeout of up to 12 hours, but that timeout is a maximum rather than a guarantee of uninterrupted execution. Infrastructure maintenance restarts these tasks regularly, so a task that runs for several hours should be expected to be restarted at least once. To handle this without losing progress, use application-level checkpointing paired with task retries (`--max-retries`).

When a task restarts, it starts in a brand new container (which completely resets memory and VRAM, preventing any memory leaks). On startup, the script auto-detects existing checkpoints inside a Cloud Storage-mounted directory and automatically resumes from the last step.

To learn more, see this [example](https://github.com/GoogleCloudPlatform/devrel-demos/blob/main/ai-ml/finetune_gemma/README.md) as well as the tutorial [Design resilient long-running GPU jobs](https://docs.cloud.google.com/run/docs/tutorials/long-running-gpu-jobs).

## What's next

  * To create a Cloud Run job, see [Create jobs](https://docs.cloud.google.com/run/docs/create-jobs).
  * To execute a job, see [Execute jobs](https://docs.cloud.google.com/run/docs/execute/jobs).
  * To execute a job on a schedule, see [Execute jobs on a schedule](https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
