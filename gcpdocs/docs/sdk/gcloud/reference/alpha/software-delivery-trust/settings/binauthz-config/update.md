---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/settings/binauthz-config/update/
title: gcloud alpha software-delivery-trust settings binauthz-config update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:31:30.327207+00:00
---

# gcloud alpha software-delivery-trust settings binauthz-config update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/settings/binauthz-config/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha software-delivery-trust settings binauthz-config update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha software-delivery-trust settings binauthz-config update - update a Binary Authorization trust config 
SYNOPSIS
    

`gcloud alpha software-delivery-trust settings binauthz-config update` `--location`=`LOCATION` [`--async`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--publish-destination`=`PUBLISH_DESTINATION`] [`--attestors-file`=`FILE_PATH` | `--clear-attestors` | `--add-attestor`=[`gate`=`GATE`,`signing-crypto-key-version`=`KEY_VERSION`,…] `--remove-attestor`=[`GATE`,…], `--remove-attestors`=[`GATE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Binary Authorization trust config. 

To replace the signing key for an existing gate: 

  * Running `--remove-attestors` and `--add-attestor` on the same gate in a single command modifies the gate in place. 
  * Running `--remove-attestors` followed by `--add-attestor` in a separate command deletes and recreates the gate. 


EXAMPLES
     To enable automatic publishing and configure attestors for prod and staging in location `us-central1`, run: 
    
    
    [gcloud alpha software-delivery-trust settings binauthz-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/settings/binauthz-config) update --location=us-central1 --publish-destination=container-analysis --add-attestor="gate=prod,signing-crypto-key-version=projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/prod-key/cryptoKeyVersions/1" --add-attestor="gate=staging,signing-crypto-key-version=projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/staging-key/cryptoKeyVersions/1"

To disable automatic publishing in location `us-central1`, run: 
    
    
    [gcloud alpha software-delivery-trust settings binauthz-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/settings/binauthz-config) update --location=us-central1 --publish-destination=none

To clear all configured attestors in location `us-central1`, run: 
    
    
    [gcloud alpha software-delivery-trust settings binauthz-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/settings/binauthz-config) update --location=us-central1 --clear-attestors

REQUIRED FLAGS
    

Location resource - Location of the Software Delivery Trust settings. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--publish-destination`=`PUBLISH_DESTINATION`
     Destination where SD Trust automatically publishes signed VSAs upon evaluation. `PUBLISH_DESTINATION` must be one of: 

`container-analysis`
     Automatically publish/revoke signed VSA occurrences in Container Analysis. 
`none`
     Disable automatic publishing. 
At most one of these can be specified: 

`--attestors-file`=`FILE_PATH`
     Path to a local YAML or JSON file defining the complete list of attestors. 
`--clear-attestors`
     Clears all configured attestors. 
Or at least one of these can be specified: 

Incremental attestor update flags. 
`--add-attestor`=[`gate`=`GATE`,`signing-crypto-key-version`=`KEY_VERSION`,…]
     Key-value pair defining the lifecycle gate and asymmetric KMS signing key version. Can be repeated. Attributes: gate: Identifier of the gate corresponding to PolicyBinding custom_gate (e.g., prod). signing-crypto-key-version: Cloud KMS CryptoKeyVersion resource name. Fails if the gate already exists; pass \--remove-attestors and --add-attestor on the same gate in a single command to modify in place, or in separate commands to delete and recreate. 
`--remove-attestor`=[`GATE`,…], `--remove-attestors`=[`GATE`,…]
     Comma-separated list of gate identifiers to remove. Using --remove-attestors and \--add-attestor on the same gate in a single command modifies it in place; using them in separate commands deletes and recreates it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
