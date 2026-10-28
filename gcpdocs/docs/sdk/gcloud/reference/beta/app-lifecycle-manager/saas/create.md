---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/saas/create/
title: gcloud beta app-lifecycle-manager saas create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:40:21.899695+00:00
---

# gcloud beta app-lifecycle-manager saas create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/saas/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager saas create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager saas create - create a SaaS offering 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager saas create` (`SAAS` : `--location`=`LOCATION`) `--locations`=[`name`=`NAME`] [`--labels`=[`LABELS`,…]] [`--application-template`=`APPLICATION_TEMPLATE` : `--application-template-revision`=`APPLICATION_TEMPLATE_REVISION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create an App Lifecycle Manager SaaS offering. 

A SaaS offering (also called an app offering) represents a SaaS product managed by the service producer. It defines the locations in which the product is available. 

EXAMPLES
     To create a SaaS offering named `my-saas` in location `us-central1` that is available in `us-central1`, run: 
    
    
    gcloud beta app-lifecycle-manager saas create my-saas --location=us-central1 --locations=name=us-central1

To create a SaaS offering named `my-saas` that is available in `us-central1` and `europe-west1` and has the label `env=prod`, run: 
    
    
    gcloud beta app-lifecycle-manager saas create my-saas --location=us-central1 --locations=name=us-central1 --locations=name=europe-west1 --labels=env=prod

POSITIONAL ARGUMENTS
    

Saas resource - SaaS offering to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `saas` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SAAS`
     ID of the saas or fully qualified identifier for the saas. 

To set the `saas` attribute: 

  * provide the argument `saas` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location ID 

To set the `location` attribute: 

  * provide the argument `saas` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--locations`=[`name`=`NAME`]
     Required, Locations in which the SaaS offering is available. Rollouts use this list to generate a rollout plan. Repeat the flag to specify multiple locations. 

`name`
     Name of the location. 
`Shorthand Example:`
    
    
    --locations=name=string --locations=name=string

`JSON Example:`
    
    
    --locations='[{"name": "string"}]'

`File Example:`
    
    
    --locations=path_to_file.(yaml|json)

OPTIONAL FLAGS
    

`--labels`=[`LABELS`,…]
     Labels on the resource, which can be used for categorization, similar to Kubernetes resource labels. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

Composite application template. Specify only in source regions; leave unspecified in replica regions. When specified, the template components are imported into their equivalent unit kind, release, and blueprint resources. Deleting the reference does not delete imported resources. 
`--application-template`=`APPLICATION_TEMPLATE`
     Full resource name of the Application Design Center composite application template to import. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--application-template-revision`=`APPLICATION_TEMPLATE_REVISION`
     Revision of the application template to use. Changes to the revision trigger manual resynchronization. If empty, the application template is ignored. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `saasservicemgmt/v1beta1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/app-lifecycle-manager>
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
