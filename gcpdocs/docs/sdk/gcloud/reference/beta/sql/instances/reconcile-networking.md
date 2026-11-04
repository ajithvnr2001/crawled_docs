---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/reconcile-networking/
title: gcloud beta sql instances reconcile-networking \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:36.993849+00:00
---

# gcloud beta sql instances reconcile-networking  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/reconcile-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql instances reconcile-networking Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql instances reconcile-networking - reconciles network infrastructure for a Cloud SQL instance 
SYNOPSIS
    

`gcloud beta sql instances reconcile-networking` `INSTANCE` [`--async`] [`--force`] [`--networks`=[`NETWORK`,…]] [`--psc-dns`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Reconciles network infrastructure (e.g. Service Connection Maps, Automated DNS Records) for a Cloud SQL instance. 
EXAMPLES
     To reconcile PSC DNS networking for a Cloud SQL instance: 
    
    
    gcloud beta sql instances reconcile-networking instance-foo --psc-dns

To reconcile PSC DNS networking for specific consumer VPC networks: 
    
    
    gcloud beta sql instances reconcile-networking instance-foo --psc-dns --networks=projects/p1/global/networks/n1,projects/p2/global/networks/n2

To force PSC DNS reconciliation: 
    
    
    gcloud beta sql instances reconcile-networking instance-foo --psc-dns --force

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--force`
     Forces service connection mapping disablement and enablement during PSC networking reconciliation. Bypasses safety checks and may cause transient connectivity disruption for connected VPCs while the networking settings are reapplied. 
`--networks`=[`NETWORK`,…]
     List of specific consumer VPC networks to reconcile, specified as full resource paths (e.g. `projects/my-consumer-project/global/networks/prod-vpc`). If omitted, reconciles all consumer networks associated with the instance. 
`--psc-dns`
     Reconciles the instance's Private Service Connect (PSC) DNS records. If the DNS zones or records associated with the PSC endpoints are missing or incorrect, they will be recreated or updated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud sql instances reconcile-networking](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/reconcile-networking)
    
    
    [gcloud alpha sql instances reconcile-networking](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/reconcile-networking)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
