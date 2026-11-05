---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake/hive/catalogs/update/
title: gcloud beta biglake hive catalogs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T11:10:36.324556+00:00
---

# gcloud beta biglake hive catalogs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake/hive/catalogs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta biglake hive catalogs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta biglake hive catalogs update - update a BigLake Hive catalog 
SYNOPSIS
    

`gcloud beta biglake hive catalogs update` `CATALOG` [`--description`=`DESCRIPTION`] [`--clear-kms-key` | `--kms-key`=`KMS_KEY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Updates a BigLake Hive catalog. 
EXAMPLES
     To update a BigLake Hive catalog named 'my-catalog' with the following arguments, run: 
    
    
    gcloud beta biglake hive catalogs update my-catalog --description="My updated catalog"

To update a BigLake Hive catalog named 'my-catalog' with Cloud KMS key `projects/my-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-key`, run: 
    
    
    gcloud beta biglake hive catalogs update my-catalog --kms-key=projects/my-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-key

POSITIONAL ARGUMENTS
    

Hive catalog resource - The Hive Catalog to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `catalog` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CATALOG`
     ID of the hive_catalog or fully qualified identifier for the hive_catalog. 

To set the `catalog` attribute: 

  * provide the argument `catalog` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     Description of the Hive catalog. 
At most one of these can be specified: 

`--clear-kms-key`
     Clear the Cloud KMS key from the catalog and revert to Google-managed encryption. 
`--kms-key`=`KMS_KEY`
     Cloud KMS key name used to encrypt cached data fetched from the catalog. Format: projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `biglake/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/bigquery/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud biglake hive catalogs update](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/hive/catalogs/update)
    
    
    [gcloud alpha biglake hive catalogs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/hive/catalogs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
