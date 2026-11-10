---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/express-links/create/
title: gcloud alpha network-services express-links create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:33:30.337986+00:00
---

# gcloud alpha network-services express-links create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/express-links/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-services express-links create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-services express-links create - create an express link 
SYNOPSIS
    

`gcloud alpha network-services express-links create` (`EXPRESS_LINK` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--destination-services`=[`DESTINATION_SERVICES`,…]] [`--matches-hostname`=[`MATCHES_HOSTNAME`,…]] [`--source-services`=[`SOURCE_SERVICES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new express link with the given name. 
EXAMPLES
     Create an express link with the name "my-express-link" and location "global". 
    
    
    gcloud alpha network-services express-links create my-express-link --location=global

POSITIONAL ARGUMENTS
    

Express link resource - Name of the express link to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `express_link` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`EXPRESS_LINK`
     ID of the express link or fully qualified identifier for the express link. 

To set the `express_link` attribute: 

  * provide the argument `express_link` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. 

To set the `location` attribute: 

  * provide the argument `express_link` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description for the express link. 
`--destination-services`=[`DESTINATION_SERVICES`,…]
     List of service URIs to which the ExpressLink resource is bound. 
`--matches-hostname`=[`MATCHES_HOSTNAME`,…]
     List of hostnames to match against the HTTP request host header. 
`--source-services`=[`SOURCE_SERVICES`,…]
     List of resources attached to the ExpressLink. The resources can be Cloud Run services. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta network-services express-links create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/express-links/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
