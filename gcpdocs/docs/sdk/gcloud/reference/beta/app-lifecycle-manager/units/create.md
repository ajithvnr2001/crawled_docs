---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/units/create/
title: gcloud beta app-lifecycle-manager units create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:41:14.860317+00:00
---

# gcloud beta app-lifecycle-manager units create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/units/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager units create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager units create - create a unit 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager units create` `UNIT` [`--application`=`APPLICATION`] [`--flag-revisions`=[`FLAG_REVISIONS`,…]] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--maintenance-pinned-until-time`=`MAINTENANCE_PINNED_UNTIL_TIME`] [`--management-mode`=`MANAGEMENT_MODE`] [`--tenant`=`TENANT`] [`--unit-kind`=`UNIT_KIND`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create an App Lifecycle Manager unit. 

A unit is an instance of a unit kind whose lifecycle is managed through an actuation engine, for example, one based on Terraform. Units are the building blocks of a tenant. Use unit operations to provision, upgrade, or deprovision a unit. 

EXAMPLES
     To create a unit named `my-unit` of the unit kind `my-unit-kind` in location `us-central1`, run: 
    
    
    gcloud beta app-lifecycle-manager units create my-unit --location=us-central1 --unit-kind=my-unit-kind

To create a unit named `my-unit` that belongs to the tenant `my-tenant`, is managed by the user, and has the label `env=prod`, run: 
    
    
    gcloud beta app-lifecycle-manager units create my-unit --location=us-central1 --unit-kind=my-unit-kind --tenant=my-tenant --management-mode=user --labels=env=prod

POSITIONAL ARGUMENTS
    

Unit resource - Unit to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `unit` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `unit` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`UNIT`
     ID of the unit or fully qualified identifier for the unit. 

To set the `unit` attribute: 

  * provide the argument `unit` on the command line. 


FLAGS
    

`--application`=`APPLICATION`
     App Hub application that this unit belongs to. All resources deployed in this unit are associated with the specified application. 
FlagRevision resource - Flag revisions used by this unit. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--flag-revisions` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--flag-revisions` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--flag-revisions`=[`FLAG_REVISIONS`,…]
     IDs of the flagRevisions or fully qualified identifiers for the flagRevisions. 

To set the `flag-revision` attribute: 

  * provide the argument `--flag-revisions` on the command line. 


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

`--location`=`LOCATION`
     For resources [unit, flag-revisions, tenant, unit-kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Requested directives for performing future maintenance on the unit. These directives include a request for the unit to skip maintenance for a period of time and remain pinned to its current release. They also include controls for postponing scheduled maintenance. 
`--maintenance-pinned-until-time`=`MAINTENANCE_PINNED_UNTIL_TIME`
     Time until which the release of the unit is pinned. Until this time, changes to the release of the unit are rejected, and rollouts do not request an upgrade of the unit. 
`--management-mode`=`MANAGEMENT_MODE`
     Management mode of the unit, which indicates whether the lifecycle of the unit is controlled by the user or by the system. The management mode cannot be changed after the unit is created. `MANAGEMENT_MODE` must be one of: 

`system`
     The system decides when to deprovision and delete the unit. The unit can still be deprovisioned or deleted manually. 
`user`
     The user manages the lifecycle of the unit. 
Tenant resource - Tenant that this unit belongs to. For example, the tenant informs the maintenance policies to use for scheduling future updates on the unit. The tenant is optional and cannot be changed after the unit is created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--tenant` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--tenant` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--tenant`=`TENANT`
     ID of the tenant or fully qualified identifier for the tenant. 

To set the `tenant` attribute: 

  * provide the argument `--tenant` on the command line. 


UnitKind resource - Unit kind that this unit belongs to. The unit kind cannot be changed after it is set. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--unit-kind`=`UNIT_KIND`
     ID of the unitKind or fully qualified identifier for the unitKind. 

To set the `unit-kind` attribute: 

  * provide the argument `--unit-kind` on the command line. 


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
