---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/start-continuous-profiling/
title: gcloud alpha mldiagnostics machine-learning-run start-continuous-profiling \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:06.785101+00:00
---

# gcloud alpha mldiagnostics machine-learning-run start-continuous-profiling  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/start-continuous-profiling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha mldiagnostics machine-learning-run start-continuous-profiling Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha mldiagnostics machine-learning-run start-continuous-profiling - start continuous profiling for a machine learning run 
SYNOPSIS
    

`gcloud alpha mldiagnostics machine-learning-run start-continuous-profiling` `--targets`=[`TARGETS`,…] [`--async`] [`--device-tracer-level`=`DEVICE_TRACER_LEVEL`; default="enabled"] [`--host-tracer-level`=`HOST_TRACER_LEVEL`; default="info"] [`--location`=`LOCATION`] [`--machine-learning-run`=`MACHINE_LEARNING_RUN`] [`--python-tracer-level`=`PYTHON_TRACER_LEVEL`; default="disabled"] [`--xprof-server-port`=`XPROF_SERVER_PORT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Start continuous profiling on one or more profiler targets of an active machine learning run. 

While continuous profiling is active, the XProf profiler on each target keeps the most recent trace data in an in-memory circular buffer. To save the buffered data as a profiler session, run `[gcloud alpha mldiagnostics profiler-session capture](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/profiler-session/capture)` with `--kind=snapshot`. On-demand profiler sessions can't be captured while continuous profiling is active. 

Only one continuous profiling session can be active on a machine learning run at a time. The tracer levels and XProf server port can't be changed while continuous profiling is active. To change them, stop continuous profiling by running `[gcloud alpha mldiagnostics machine-learning-run stop-continuous-profiling](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run/stop-continuous-profiling)`, and then start it again. 

EXAMPLES
     To start continuous profiling on the profiler targets `my-node-0` and `my-node-1` of the machine learning run `my-run` in `us-central1`, run: 
    
    
    [gcloud alpha mldiagnostics machine-learning-run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run) start-continuous-profiling --machine-learning-run=my-run --location=us-central1 --targets=my-node-0,my-node-1

To start continuous profiling with the lowest-overhead host tracer level and device tracing disabled, run: 
    
    
    [gcloud alpha mldiagnostics machine-learning-run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/machine-learning-run) start-continuous-profiling --machine-learning-run=my-run --location=us-central1 --targets=my-node-0 --host-tracer-level=critical --device-tracer-level=disabled

To list the profiler targets of the machine learning run `my-run`, run: 
    
    
    [gcloud alpha mldiagnostics profiler-target list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/profiler-target/list) --machine-learning-run=my-run --location=us-central1

REQUIRED FLAGS
    

ProfilerTarget resource - Profiler targets on which to start continuous profiling. To list the profiler targets of a machine learning run, run `[gcloud alpha mldiagnostics profiler-target list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics/profiler-target/list)`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--targets` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--targets` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 



To set the `machine-learning-run` attribute: 

  * provide the argument `--targets` on the command line with a fully specified name; 
  * provide the argument `--machine-learning-run` on the command line. 



This must be specified. 

`--targets`=[`TARGETS`,…]
     IDs of the profilerTargets or fully qualified identifiers for the profilerTargets. 

To set the `profiler-target` attribute: 

  * provide the argument `--targets` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--device-tracer-level`=`DEVICE_TRACER_LEVEL`; default="enabled"
     Device tracer level for the session. If the field is not set or unspecified, the default is `DEVICE_TRACER_LEVEL_ENABLED`. `DEVICE_TRACER_LEVEL` must be one of: 

`disabled`
     Tracer level is disabled. 
`enabled`
     Tracer level is enabled. 
`--host-tracer-level`=`HOST_TRACER_LEVEL`; default="info"
     Host tracer level for the session. If the field is not set or unspecified, the default is `HOST_TRACER_LEVEL_INFO`. `HOST_TRACER_LEVEL` must be one of: 

`critical`
     Tracer level is critical. 
`disabled`
     Tracer level is disabled. 
`info`
     Tracer level is info. 
`verbose`
     Tracer level is verbose. 
`--location`=`LOCATION`
     For resources [machine-learning-run, targets], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--machine-learning-run`=`MACHINE_LEARNING_RUN`
     For resources [machine-learning-run, targets], provides fallback value for resource machine-learning-run attribute. When the resource's full URI path is not provided, machine-learning-run will fallback to this flag value. 
`--python-tracer-level`=`PYTHON_TRACER_LEVEL`; default="disabled"
     Python tracer level for the session. If the field is not set or unspecified, the default is `PYTHON_TRACER_LEVEL_DISABLED`. `PYTHON_TRACER_LEVEL` must be one of: 

`disabled`
     Tracer level is disabled. 
`enabled`
     Tracer level is enabled. 
`--xprof-server-port`=`XPROF_SERVER_PORT`
     Port of the XProf profiler server that runs in your workload on each profiler target. If unspecified, port 9999 is used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `hypercomputecluster/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/cluster-director/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
