---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/wait-for-reencryption/
title: gcloud alpha spanner databases wait-for-reencryption \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:32:00.139208+00:00
---

# gcloud alpha spanner databases wait-for-reencryption  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/wait-for-reencryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner databases wait-for-reencryption Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner databases wait-for-reencryption - wait for a Cloud Spanner database CMEK re-encryption to converge 
SYNOPSIS
    

`gcloud alpha spanner databases wait-for-reencryption` (`DATABASE` : `--instance`=`INSTANCE`) (`--clear-kms-keys` | `--kms-keys`=`KMS_KEY`,[`KMS_KEY`,…]) [`--endpoint-mode`=`ENDPOINT_MODE`] [`--timeout`=`TIMEOUT`; default="4h"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Wait for a Cloud Spanner database CMEK re-encryption transition to converge. 

Spanner CMEK transitions (`GMEK` to `CMEK`, `CMEK` to `CMEK`, and `CMEK` to `GMEK`) complete asynchronously in the background after the `UpdateDatabase` operation finishes. This command polls `databases.get` until `encryptionInfo` is non-empty and lists only the target `CUSTOMER_MANAGED_ENCRYPTION` KMS key(s) (`--kms-keys`) or only `GOOGLE_DEFAULT_ENCRYPTION` (`--clear-kms-keys`) across consecutive polls. Convergence is evaluated at the KMS key level (ignoring `/cryptoKeyVersions/<N>` suffixes), so older versions of the same KMS key may still wrap some data. 

This command can be run right after `gcloud spanner databases update --async`; it waits up to 10 minutes (measured on a monotonic clock, while `--timeout` uses wall-clock time) for the new configuration to apply before enforcing that `encryptionConfig` matches the requested target and has not diverged due to a concurrent update. 

When moving from Google-managed encryption to CMEK, `encryptionInfo` lists the new key(s) after they are in use. This indicates CMEK is active but may appear before all pre-existing data has been re-encrypted. 

Backups are not re-encrypted. Each backup keeps using the KMS key it was created with; keep that key until those backups are deleted or expire, or they can't be restored. 

To check convergence manually without this command, run: 
    
    
    [gcloud spanner databases describe](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/describe) DATABASE --instance=INSTANCE --format=json

and verify that `encryptionInfo` is non-empty and lists only the target `CUSTOMER_MANAGED_ENCRYPTION` KMS key(s) (or only `GOOGLE_DEFAULT_ENCRYPTION` when reverting to Google-managed encryption). 

EXAMPLES
     To wait for a Cloud Spanner database 'my-database' to finish re-encrypting to KMS keys, run: 
    
    
    gcloud alpha spanner databases wait-for-reencryption my-database --instance=my-instance --kms-keys="projects/project1/locations/location1/keyRings/ring1/cryptoKeys/key1,projects/project1/locations/location2/keyRings/ring2/cryptoKeys/key2"

To wait for a Cloud Spanner database 'my-database' to finish reverting to Google-managed encryption, run: 
    
    
    gcloud alpha spanner databases wait-for-reencryption my-database --instance=my-instance --clear-kms-keys

To wait with a custom timeout of 30 minutes, run: 
    
    
    gcloud alpha spanner databases wait-for-reencryption my-database --instance=my-instance --kms-keys="projects/project1/locations/location1/keyRings/ring1/cryptoKeys/key1" --timeout=30m

To start an asynchronous KMS key update and then wait for background re-encryption to converge, run: 
    
    
    [gcloud spanner databases update](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/update) my-database --instance=my-instance --kms-keys="projects/project1/locations/location1/keyRings/ring1/cryptoKeys/key1,projects/project1/locations/location2/keyRings/ring2/cryptoKeys/key2" --async
    gcloud alpha spanner databases wait-for-reencryption my-database --instance=my-instance --kms-keys="projects/project1/locations/location1/keyRings/ring1/cryptoKeys/key1,projects/project1/locations/location2/keyRings/ring2/cryptoKeys/key2"

POSITIONAL ARGUMENTS
    

Database resource - The Cloud Spanner database to wait for re-encryption. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `database` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The Cloud Spanner instance for the database. 

To set the `instance` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--clear-kms-keys`
     Wait for the database to converge to Google-managed encryption. 
`--kms-keys`=`KMS_KEY`,[`KMS_KEY`,…]
     Full set of KMS keys the database's encryption is expected to converge to. Must match the keys passed to `gcloud spanner databases update --kms-keys`. 
OPTIONAL FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--timeout`=`TIMEOUT`; default="4h"
     Maximum time to wait for database CMEK re-encryption to converge. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
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
