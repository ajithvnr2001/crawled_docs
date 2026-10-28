---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/database-connections/create/
title: gcloud oracle-database database-connections create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:38:53.047353+00:00
---

# gcloud oracle-database database-connections create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/database-connections/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database database-connections create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database database-connections create - create a new DatabaseConnection 
SYNOPSIS
    

`gcloud oracle-database database-connections create` `DATABASE_CONNECTION` `--connection-string`=`CONNECTION_STRING` [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--odb-network`=`ODB_NETWORK`] [`--password-secret-version`=`PASSWORD_SECRET_VERSION`] [`--request-id`=`REQUEST_ID`] [`--secret`=`SECRET`] [`--username`=`USERNAME`] [`--wallet-secret-version`=`WALLET_SECRET_VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new DatabaseConnection. 
EXAMPLES
     To create a DatabaseConnection with id `my-connection` in the location `us-east4` with display-name `my connection`, connection-string `my-db-host.example.com:1521/my-service`, username `admin`, password-secret-version `projects/my-project/secrets/my-secret/versions/1`, and odb-network `projects/my-project/locations/us-east4/odbNetworks/my-odbnetwork`, run: 
    
    
    gcloud oracle-database database-connections create my-connection --location=us-east4 --display-name="my connection" --connection-string="my-db-host.example.com:1521/my-service" --username="admin" --password-secret-version=projects/my-project/secrets/my-secret/versions/1 --odb-network=projects/my-project/locations/us-east4/odbNetworks/my-odbnetwork

POSITIONAL ARGUMENTS
    

DatabaseConnection resource - Identifier. The resource name of the DatabaseConnection. Format: projects/{project}/locations/{location}/databaseConnections/{database_connection} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database_connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `database_connection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`DATABASE_CONNECTION`
     ID of the databaseConnection or fully qualified identifier for the databaseConnection. 

To set the `database_connection` attribute: 

  * provide the argument `database_connection` on the command line. 


REQUIRED FLAGS
    

`--connection-string`=`CONNECTION_STRING`
     Oracle Easy Connect or TNS connection string. Example: "your-db-host.example.com:1521/YOUR_SERVICE_NAME" 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     User-friendly display name for the connection. 
`--labels`=[`LABELS`,…]
     Optional: Labels as key-value pairs to organize the resource. 

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
     For resources [database_connection, odb-network], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Arguments for the network configuration. 
OdbNetwork resource - For Oracle Database@Google cloud resources. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--odb-network` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--odb-network` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--odb-network`=`ODB_NETWORK`
     ID of the odbNetwork or fully qualified identifier for the odbNetwork. 

To set the `odb-network` attribute: 

  * provide the argument `--odb-network` on the command line. 


SecretVersion resource - The resource name of the GCP Secret Manager secret version containing the password for the specified username. Format: projects/{project}/secrets/{secret_id}/versions/{version_id} The service's Per-Product Per-Project Service Account (P4SA) must have the 'secretmanager.secretAccessor' permission on this secret. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--password-secret-version` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `secret` attribute: 

  * provide the argument `--password-secret-version` on the command line with a fully specified name; 
  * provide the argument `--secret` on the command line. 


`--password-secret-version`=`PASSWORD_SECRET_VERSION`
     ID of the secretVersion or fully qualified identifier for the secretVersion. 

To set the `secret-version` attribute: 

  * provide the argument `--password-secret-version` on the command line. 


`--request-id`=`REQUEST_ID`
     An optional ID to identify the request. This value is used to identify duplicate requests. If you make a request with the same request ID and the original request is still in progress or completed, the server ignores the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--secret`=`SECRET`
     For resources [password-secret-version, wallet-secret-version], provides fallback value for resource secret attribute. When the resource's full URI path is not provided, secret will fallback to this flag value. 
`--username`=`USERNAME`
     The default database username to use for connections. 
Arguments for the wallet source. 
SecretVersion resource - Optional: The resource name of the GCP Secret Manager secret version containing base64 encoded content of the Oracle Wallet ZIP file required for mTLS/TLS connections. Format: projects/{project}/secrets/{secret_id}/versions/{version_id} The service's Per-Product Per-Project Service Account (P4SA) must have the 'secretmanager.secretAccessor' permission on this secret. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--wallet-secret-version` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `secret` attribute: 

  * provide the argument `--wallet-secret-version` on the command line with a fully specified name; 
  * provide the argument `--secret` on the command line. 


`--wallet-secret-version`=`WALLET_SECRET_VERSION`
     ID of the secretVersion or fully qualified identifier for the secretVersion. 

To set the `secret-version` attribute: 

  * provide the argument `--wallet-secret-version` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
