---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/customer-managed-certs/update/
title: gcloud sql ssl customer-managed-certs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:14.314624+00:00
---

# gcloud sql ssl customer-managed-certs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/customer-managed-certs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql ssl customer-managed-certs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql ssl customer-managed-certs update - create or update a customer managed certificate bundle for a Cloud SQL instance 
SYNOPSIS
    

`gcloud sql ssl customer-managed-certs update` `BUNDLE` `--instance`=`INSTANCE`, `-i` `INSTANCE` [`--allow-missing`] [`--async`] [`--client-cert-file`=`CLIENT_CERT_FILE`] [`--client-key-file`=`CLIENT_KEY_FILE`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--intent`=`INTENT`; default=`"PG_LOGICAL"`] [`--primary-dns`=`PRIMARY_DNS`] [`--primary-ipv4-address`=`PRIMARY_IPV4_ADDRESS`] [`--server-ca-file`=`SERVER_CA_FILE`] [`--update-mask`=`UPDATE_MASK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create or update a customer managed certificate bundle for a Cloud SQL instance. 
EXAMPLES
     To create or replace a customer managed certificate bundle `bundle1` for the Cloud SQL instance `my-instance`, run: 
    
    
    gcloud sql ssl customer-managed-certs update bundle1 --instance=my-instance --allow-missing --intent=PG_LOGICAL --server-ca-file=/path/to/server_ca.pem --client-cert-file=/path/to/client_cert.pem --client-key-file=/path/to/client_key.pem --primary-dns=primary.example.com --primary-ipv4-address=10.0.0.1

To partially update the primary IPv4 address and client certificate of an existing bundle `bundle1` for `my-instance`, run: 
    
    
    gcloud sql ssl customer-managed-certs update bundle1 --instance=my-instance --update-mask=primary_dns_record.ipv4_address,customer_managed_certificates --primary-ipv4-address=10.0.0.2 --client-cert-file=/path/to/new_client_cert.pem

POSITIONAL ARGUMENTS
    

`BUNDLE`
     Customer managed certificate bundle name. Constrained to `[a-zA-Z0-9]+` with a maximum length of 10 characters. 
REQUIRED FLAGS
    

`--instance`=`INSTANCE`, `-i` `INSTANCE`
     Cloud SQL instance ID. 
OPTIONAL FLAGS
    

`--allow-missing`
     If set, and the customer managed certificate bundle configuration is not found, a new customer managed certificate bundle configuration will be created. In this situation, `--update-mask` is ignored. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--client-cert-file`=`CLIENT_CERT_FILE`
     Path to a PEM-encoded file containing the peer client certificate. 
`--client-key-file`=`CLIENT_KEY_FILE`
     Path to a PEM-encoded file containing the peer client private key. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--intent`=`INTENT`; default=`"PG_LOGICAL"`
     Intent for the customer managed certificate bundle configuration. `INTENT` must be (only one value is supported): `PG_LOGICAL`. 
`--primary-dns`=`PRIMARY_DNS`
     DNS name associated with the primary instance in a replication topology. 
`--primary-ipv4-address`=`PRIMARY_IPV4_ADDRESS`
     IPv4 address for the primary DNS name. 
`--server-ca-file`=`SERVER_CA_FILE`
     Path to a PEM-encoded file containing the peer server CA certificate. 
`--update-mask`=`UPDATE_MASK`
     Comma-separated list of fields to be updated. Allowed values include: `*`, `intent`, `primary_dns_record`, `primary_dns_record.dns`, `primary_dns_record.ipv4_address`, and `customer_managed_certificates`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql ssl customer-managed-certs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/ssl/customer-managed-certs/update)
    
    
    [gcloud beta sql ssl customer-managed-certs update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/ssl/customer-managed-certs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
