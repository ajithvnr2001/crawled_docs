---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/accelerator-pod-controllers/create/
title: gcloud alpha compute accelerator-pod-controllers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:20.619422+00:00
---

# gcloud alpha compute accelerator-pod-controllers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/accelerator-pod-controllers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute accelerator-pod-controllers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute accelerator-pod-controllers create - create a Google Compute Engine accelerator pod controller 
SYNOPSIS
    

`gcloud alpha compute accelerator-pod-controllers create` (`ACCELERATOR_POD_CONTROLLER` : `--zone`=`ZONE`) `--target`=`TARGET` [`--async`] [`--description`=`DESCRIPTION`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--management-interface`=[`KEY`=`VALUE`,…]] [`--management-interfaces-file`=`MANAGEMENT_INTERFACES_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Google Compute Engine accelerator pod controller. 
EXAMPLES
     To create an accelerator pod controller named `my-apc` in zone `us-east5-staginga` with target reservation sub-block: 
    
    
    gcloud alpha compute accelerator-pod-controllers create my-apc --zone=us-east5-staginga --target=projects/my-project/zones/us-east5-staginga/reservations/my-res/reservationBlocks/my-block/reservationSubBlocks/my-subblock

To create an accelerator pod controller with a switch monitoring management interface: 
    
    
    gcloud alpha compute accelerator-pod-controllers create my-apc --zone=us-east5-staginga --target=projects/my-project/zones/us-east5-staginga/reservations/my-res/reservationBlocks/my-block/reservationSubBlocks/my-subblock --management-interface=key=gnmi-nvswitch-0,type=TYPE_NVLINK_SWITCH_MONITORING,network=projects/my-project/global/networks/my-net,subnetwork=projects/my-project/regions/us-east5/subnetworks/my-sub,ipv4-address=10.0.0.1

POSITIONAL ARGUMENTS
    

Accelerator pod controller resource - The name of the accelerator pod controller to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `accelerator_pod_controller` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ACCELERATOR_POD_CONTROLLER`
     ID of the accelerator pod controller or fully qualified identifier for the accelerator pod controller. 

To set the `accelerator_pod_controller` attribute: 

  * provide the argument `accelerator_pod_controller` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     The name of the Google Compute Engine zone. 

To set the `zone` attribute: 

  * provide the argument `accelerator_pod_controller` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * set the property `compute/zone`. 


REQUIRED FLAGS
    

`--target`=`TARGET`
     The target accelerator domain this controller manages (e.g. a Reservation Sub-block URI). 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     An optional description of this resource. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--management-interface`=[`KEY`=`VALUE`,…]
     Management interface configuration for the accelerator pod controller. Can be specified multiple times. Keys include `key`, `type`, `network`, `subnetwork`, `ipv4-address`, `ipv6-address`, and `trust-config`. 
`--management-interfaces-file`=`MANAGEMENT_INTERFACES_FILE`
     Path to a YAML or JSON file containing management interface configurations. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
