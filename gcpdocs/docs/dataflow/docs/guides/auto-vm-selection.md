---
url: https://docs.cloud.google.com/dataflow/docs/guides/auto-vm-selection/
title: Auto VM Selection \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:24:24.353945+00:00
---

# Auto VM Selection  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/auto-vm-selection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Auto VM Selection Stay organized with collections  Save and categorize content based on your preferences. 

When you pin a job to a specific machine type using the [`workerMachineType` pipeline option](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm#machine-type), you risk experiencing delays or job failures due to resource stockouts. Auto VM Selection addresses this problem by automatically choosing workers from a pool of compatible and available machine types using Compute Engine [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility). This helps to ensure that your Dataflow pipelines acquire capacity reliably, helping you maintain consistent performance and avoid interruptions.

## Unsupported configurations

Auto VM Selection is turned off if your pipeline is configured with any of the following:

  * [Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime) is enabled.
  * The `min_cpu_platform` pipeline option is set.
  * [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) disks or custom provisioned performance (IOPS and throughput) are used. Jobs started with these configurations will fail.
  * [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm) is enabled.
  * Accelerators (GPUs or TPUs) are required.
  * Jobs that don't use Dataflow Shuffle or Streaming Engine.

**Note:** To ensure maximum compatibility and allow the use of newer machine generations, don't specify a disk type when using Auto VM Selection.

## Enable Auto VM Selection

Auto VM Selection is enabled automatically in any of the following scenarios:

  * If you set `min_ram` or `cpu_count` [resource hints](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting) for pipeline steps that don't require accelerators (GPUs or TPUs). For information about how to use resource hints with template-based jobs, see [Pipeline resource hints](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#pipeline_resource_hints).



## Auto VM Selection behavior

Configure `min_ram` and `cpu_count` resource hints either in isolation or in combination. For example:

  1. A job with only `cpu_count=2` may provision instances with `n4-standard-2` (2 vCPUs, 8 GB RAM), `c4-standard-2` (2 vCPUs, 7 GB RAM) and other machine types.
  2. A job with both `cpu_count=4` and `min_ram=16GB` may provision instances with `n4-standard-4` (4 vCPUs, 16 GB RAM), `c4-highmem-4` (4 vCPUs, 31 GB RAM) and other machine types.



Auto VM Selection optimizes VM selection for resource obtainability. This means that you might experience reduced performance while using Auto VM Selection to improve the obtainability of some of your highly-tuned jobs. We recommend that you test Auto VM Selection on a subset of your existing jobs before gradually deploying them more broadly. For more information about obtainability, see [Improve resource obtainability for jobs](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview) in the Batch documentation.

Dataflow attempts to use 4th generation machine families first (for example, N4 or C4) to offer better efficiency. If 4th generation machines are unavailable in your region, lack sufficient quota, or are incompatible with your configurations, Dataflow automatically falls back to widely available 2nd generation machine families (for example, N2 or E2) to ensure your job can start without capacity delays.

If you specify a disk type such as `pd-ssd` or `pd-standard` when enabling Auto VM Selection using resource hints (right fitting), Dataflow only provisions compatible 2nd generation machine families. To ensure maximum compatibility and allow the use of newer machine generations, don't assign a disk type.

## View selected machine types

Because Auto VM Selection chooses machine types when it creates worker VMs, the workers of a job can use different machine types. To see which machine types your jobs use, query worker VM metrics with the Cloud Monitoring API. Cloud Monitoring records the machine type of each worker VM in the `machine_type` system metadata label. Dataflow adds a `dataflow_job_id` label to each worker VM.

To run the following command, you need the Google Cloud CLI and curl. To get the permission that you need to query metrics, ask your administrator to grant you the [Monitoring Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) role on the project.

The following command lists the machine types that the workers of a Dataflow job used. The command calls the [`projects.timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method and formats the response as a table by using only built-in shell commands:
    
    
    PROJECT_ID="PROJECT_ID"
    JOB_ID="JOB_ID"
    START_TIME="${JOB_ID%%_*}T00:00:00Z"
    END_TIME="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    
    TOKEN="$(gcloud auth print-access-token)" &&
    RESPONSE="$(curl -fsS --get \
        "https://monitoring.googleapis.com/v3/projects/${PROJECT_ID}/timeSeries" \
        -H "Authorization: Bearer ${TOKEN}" \
        --data-urlencode "filter=metric.type=\"compute.googleapis.com/instance/cpu/utilization\" resource.type=\"gce_instance\" metadata.user_labels.\"dataflow_job_id\"=\"${JOB_ID}\"" \
        --data-urlencode "interval.startTime=${START_TIME}" \
        --data-urlencode "interval.endTime=${END_TIME}" \
        --data-urlencode "aggregation.alignmentPeriod=60s" \
        --data-urlencode "aggregation.perSeriesAligner=ALIGN_MEAN" \
        --data-urlencode "aggregation.crossSeriesReducer=REDUCE_COUNT" \
        --data-urlencode 'aggregation.groupByFields=metadata.system_labels."machine_type"' \
        --data-urlencode "view=FULL" \
        --data-urlencode "prettyPrint=true" \
        --data-urlencode "fields=timeSeries.metadata,timeSeries.points.value,nextPageToken")" &&
    printf '%s\n' "$RESPONSE" | {
      printf '%-22s%s\n' MACHINE_TYPE PEAK_INSTANCES
      type= peak=0
      while IFS= read -r line; do
        case $line in
          *'"int64Value": "'*)
            v=${line#*'"int64Value": "'}; v=${v%%'"'*}
            [ "$v" -gt "$peak" ] && peak=$v ;;
          *'"machine_type": "'*)
            type=${line#*'"machine_type": "'}; type=${type%%'"'*} ;;
          '    }' | '    },')
            [ -n "$type" ] && printf '%-22s%s\n' "$type" "$peak"
            type= peak=0 ;;
          *'"nextPageToken":'*)
            printf 'Warning: output is incomplete; use a shorter time range.\n' >&2 ;;
        esac
      done
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that runs the job
  * `JOB_ID`: the ID of the Dataflow job



The output has a row for each machine type that the job's workers used. The `PEAK_INSTANCES` column shows the maximum number of workers of that machine type that ran at the same time. The output is similar to the following:
    
    
    MACHINE_TYPE          PEAK_INSTANCES
    c4-standard-2         1
    n4-standard-2         4
    

The command counts the job's VMs of each machine type in each minute, based on the `compute.googleapis.com/instance/cpu/utilization` metric, which every running VM reports. Metric data can take up to 4 minutes to appear in Monitoring, and the command might not count VMs that run for less than 1 minute.

A job ID starts with the job's creation date in Pacific Time. By default, `START_TIME` is midnight UTC on that date, which is always before the job started, and `END_TIME` is the current time. To query a different time range, set `START_TIME` and `END_TIME` to UTC timestamps in RFC 3339 format. For example, `START_TIME="2026-11-04T18:00:00Z"` and `END_TIME="2026-11-05T18:00:00Z"`.

If the command prints a warning that the output is incomplete, run the command for shorter time ranges. This warning can appear for jobs that run for several weeks.

Monitoring stores data that's older than 6 weeks at 10-minute intervals. To query that data, change `aggregation.alignmentPeriod` to `600s`.

## Limitations

When using Auto VM Selection, [Portable Runner container image updates](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#portable_runner_harness_update) are disabled for streaming jobs that use the [Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner).

## Compute Engine reservations

If you use Compute Engine reservations with Auto VM Selection, note the following:

  * If you have reservations configured to be [consumed automatically](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#auto-reservations), they might be used if Auto VM Selection provisions machine types that match the reservation.
  * Auto VM Selection consumes compute instances as they are available. Consequently, you can't specify that the service [consume instances from a specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).



## Known issues

When using Auto VM Selection, be aware of the following known issues:

### Unexpected parallelism

If you observe low CPU utilization or unexpected parallelism on worker VMs when using Auto VM Selection with right fitting, check the following settings.

#### Horizontal Autoscaling

If you disable Horizontal Autoscaling, your job might run with lower parallelism than expected. To avoid this issue, keep Horizontal Autoscaling enabled. For more information, see [Right fitting support and limitations](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#limitations_and_requirements).

#### Worker harness threads

By default, Dataflow sets the number of threads per worker based on the vCPU count of the selected machine type. If you still observe low CPU utilization or unexpected parallelism, you can override the default by setting the `numberOfWorkerHarnessThreads` or `number_of_worker_harness_threads` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#resource_utilization). This option applies globally to all worker pools in the pipeline.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
