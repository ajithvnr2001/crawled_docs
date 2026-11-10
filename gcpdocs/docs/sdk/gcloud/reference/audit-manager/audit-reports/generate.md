---
url: https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-reports/generate/
title: gcloud audit-manager audit-reports generate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:33:17.609584+00:00
---

# gcloud audit-manager audit-reports generate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-reports/generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud audit-manager audit-reports generate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud audit-manager audit-reports generate - generate Audit Report 
SYNOPSIS
    

`gcloud audit-manager audit-reports generate` `--compliance-framework`=`COMPLIANCE_FRAMEWORK` `--gcs-uri`=`GCS_URI` `--location`=`LOCATION` `--report-format`=`REPORT_FORMAT` (`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`) [`--parameter-overrides`=[`PARAMETER_OVERRIDES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Generate a new Audit Report. 
EXAMPLES
     To generate an Audit Report in the `us-central1` region, for a project with ID `123` against the compliance framework `organizations/456/locations/global/frameworks/builtin-nist-800-53-revision5` in `odf` format and store it in `gs://testbucketauditmanager` bucket, run: 
    
    
    gcloud audit-manager audit-reports generate --project=123 --location=us-central1 --compliance-framework=organizations/456/locations/global/frameworks/builtin-nist-800-53-revision5 --report-format=odf --gcs-uri=gs://testbucketauditmanager

If the compliance framework is parameterized, to generate the same Audit Report while overriding cloud control parameters defined in the file `overrides.json`, run: 
    
    
    gcloud audit-manager audit-reports generate --project=123 --location=us-central1 --compliance-framework=organizations/456/locations/global/frameworks/builtin-nist-800-53-revision5 --report-format=odf --gcs-uri=gs://testbucketauditmanager --parameter-overrides=overrides.json

REQUIRED FLAGS
    

`--compliance-framework`=`COMPLIANCE_FRAMEWORK`
     Compliance Framework against which the Report must be generated. Eg: FEDRAMP_MODERATE 
`--gcs-uri`=`GCS_URI`
     Destination Cloud storage bucket where report and evidence must be uploaded. The Cloud storage bucket provided here must be selected among the buckets entered during the enrollment process. 
`--location`=`LOCATION`
     The location where the report should be generated. 
`--report-format`=`REPORT_FORMAT`
     The format in which the audit report should be created. `REPORT_FORMAT` must be (only one value is supported): `odf`. 
Exactly one of these must be specified: 

`--folder`=`FOLDER`
     Folder Id for which to generate audit report 
`--organization`=`ORGANIZATION`
     Organization Id for which to generate audit report 
`--project`=`PROJECT`
     Project Id for which to generate audit report 
OPTIONAL FLAGS
    

`--parameter-overrides`=[`PARAMETER_OVERRIDES`,…]
     Overrides for the parameters of parameterized cloud controls, applied when the audit runs. Map from cloud control resource name to the overrides for that cloud control. 

`KEY`
     Full resource name of the cloud control, for example `organizations/123/locations/global/cloudControls/my-control`, as returned by `[gcloud compliance-manager cloud-controls list](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/list)`. 
`VALUE`
     Parameter overrides for the cloud control. 

`parameters`
     Parameters to override. 

`name`
     Name of the parameter. 
`parameterValue`
     Value of the parameter. Set exactly one of the following fields. 

`boolValue`
     A boolean value. 
`numberValue`
     A numeric value. 
`oneofValue`
     The selected sub-parameter of a `oneOf` parameter, with its own `name` and `parameterValue`. Can be nested up to 3 levels. 

`name`
     Name of the parameter. 
`parameterValue`
     Value of the parameter. Set exactly one of the following fields. 

`boolValue`
     A boolean value. 
`numberValue`
     A numeric value. 
`stringListValue`
     A list of strings. 

`values`
     The strings in the list. 
`stringValue`
     A string value. 
`stringListValue`
     A list of strings. 

`values`
     The strings in the list. 
`stringValue`
     A string value. 
`Shorthand Example:`
    
    
    --parameter-overrides=string={parameters=[{name=string,parameterValue={boolValue=boolean,numberValue=float,oneofValue={name=string,parameterValue={boolValue=boolean,numberValue=float,stringListValue={values=[string]},stringValue=string}},stringListValue={values=[string]},stringValue=string}}]}

`JSON Example:`
    
    
    --parameter-overrides='{"string": {"parameters": [{"name": "string", "parameterValue": {"boolValue": boolean, "numberValue": float, "oneofValue": {"name": "string", "parameterValue": {"boolValue": boolean, "numberValue": float, "stringListValue": {"values": ["string"]}, "stringValue": "string"}}, "stringListValue": {"values": ["string"]}, "stringValue": "string"}}]}}'

`File Example:`
    
    
    --parameter-overrides=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha audit-manager audit-reports generate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/audit-reports/generate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
