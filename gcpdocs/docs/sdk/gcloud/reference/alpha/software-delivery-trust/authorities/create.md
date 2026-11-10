---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/authorities/create/
title: gcloud alpha software-delivery-trust authorities create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:31:24.698061+00:00
---

# gcloud alpha software-delivery-trust authorities create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust/authorities/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha software-delivery-trust authorities create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha software-delivery-trust authorities create - create a Software Delivery Trust verification authority 
SYNOPSIS
    

`gcloud alpha software-delivery-trust authorities create` (`AUTHORITY` : `--location`=`LOCATION`) [`--description`=`DESCRIPTION`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--key-id`=`KEY_ID`] [`--kms-key-version`=`KMS_KEY_VERSION` | `--pkix-public-key-file`=`PKIX_PUBLIC_KEY_FILE` `--signature-algorithm`=`SIGNATURE_ALGORITHM`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` An Authority represents a trusted verification identity, containing public keys used to verify attestations for software artifacts. 
EXAMPLES
     To create an empty authority 'my-authority' in location 'us-central1': 
    
    
    gcloud alpha software-delivery-trust authorities create my-authority --location=us-central1 --description="Production GitHub Actions builder"

To create an authority with an initial Cloud KMS public key: 
    
    
    gcloud alpha software-delivery-trust authorities create my-authority --location=us-central1 --description="Authority backed by Cloud KMS asymmetric signing key" --kms-key-version="projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key/cryptoKeyVersions/1"

To create an authority with an initial local PKIX public key file: 
    
    
    gcloud alpha software-delivery-trust authorities create my-authority --location=us-central1 --description="Authority for CI/CD workload" --key-id="v1" --pkix-public-key-file="./public_key.pem" --signature-algorithm=ec-sign-p256-sha256

POSITIONAL ARGUMENTS
    

Authority resource - The authority to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`AUTHORITY`
     ID of the authority or fully qualified identifier for the authority. 

To set the `authority` attribute: 

  * provide the argument `AUTHORITY` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Google Cloud location for the authority. 

To set the `location` attribute: 

  * provide the argument `AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     Human-readable description of the authority. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--key-id`=`KEY_ID`
     Optional key slot identifier or signer key hint (max 512 characters). Must be unique within this authority. Defaults to the KMS key version resource name for KMS keys. For pkix-public-key-file, if omitted, will be left unassigned. 
At most one of these can be specified: 

Cloud KMS public key configuration 
`--kms-key-version`=`KMS_KEY_VERSION`
     The Cloud KMS CryptoKeyVersion resource name. Format: projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key}/cryptoKeyVersions/{version} 
Local PKIX public key configuration 
`--pkix-public-key-file`=`PKIX_PUBLIC_KEY_FILE`
     Path to a local file containing the PEM-encoded PKIX SubjectPublicKeyInfo public key. 
`--signature-algorithm`=`SIGNATURE_ALGORITHM`
     The signature and digest algorithm used with the local public key. `SIGNATURE_ALGORITHM` must be one of: `ec-sign-p256-sha256`, `ec-sign-p384-sha384`, `ec-sign-p521-sha512`, `rsa-sign-pss-2048-sha256`, `rsa-sign-pss-3072-sha256`, `rsa-sign-pss-4096-sha256`, `rsa-sign-pss-4096-sha512`, `rsa-sign-pkcs1-2048-sha256`, `rsa-sign-pkcs1-3072-sha256`, `rsa-sign-pkcs1-4096-sha256`, `rsa-sign-pkcs1-4096-sha512`. 
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
