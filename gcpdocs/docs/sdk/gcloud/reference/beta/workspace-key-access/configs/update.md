---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/workspace-key-access/configs/update/
title: gcloud beta workspace-key-access configs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:38:49.111548+00:00
---

# gcloud beta workspace-key-access configs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/workspace-key-access/configs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta workspace-key-access configs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta workspace-key-access configs update - update a Workspace Key Access config 
SYNOPSIS
    

`gcloud beta workspace-key-access configs update` (`CONFIG` : `--location`=`LOCATION`) [`--admin-emails`=[`ADMIN_EMAILS`,…]] [`--async`] [`--kacls-owner-domains`=[`KACLS_OWNER_DOMAINS`,…]] [`--request-id`=`REQUEST_ID`] [`--annotations`=[`ANNOTATIONS`,…] | `--update-annotations`=[`UPDATE_ANNOTATIONS`,…] `--clear-annotations` | `--remove-annotations`=`REMOVE_ANNOTATIONS`] [`--idp-configs`=[`additionalAudiences`=`ADDITIONALAUDIENCES`],[`audience`=`AUDIENCE`],[`idpType`=`IDPTYPE`],[`issuer`=`ISSUER`],[`jwksUri`=`JWKSURI`] | `--add-idp-configs`=[`additionalAudiences`=`ADDITIONALAUDIENCES`],[`audience`=`AUDIENCE`],[`idpType`=`IDPTYPE`],[`issuer`=`ISSUER`],[`jwksUri`=`JWKSURI`] `--clear-idp-configs` | `--remove-idp-configs`=[`additionalAudiences`=`ADDITIONALAUDIENCES`],[`audience`=`AUDIENCE`],[`idpType`=`IDPTYPE`],[`issuer`=`ISSUER`],[`jwksUri`=`JWKSURI`]] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--tags`=[`TAGS`,…] | `--update-tags`=[`UPDATE_TAGS`,…] `--clear-tags` | `--remove-tags`=`REMOVE_TAGS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Workspace Key Access config. 
EXAMPLES
     To replace the admin emails of config `my-config`, run: 
    
    
    gcloud beta workspace-key-access configs update my-config --location=us-east1 --admin-emails=admin2@example.com

POSITIONAL ARGUMENTS
    

Config resource - Identifier. name of resource The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONFIG`
     ID of the config or fully qualified identifier for the config. 

To set the `config` attribute: 

  * provide the argument `config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the config resource. 

To set the `location` attribute: 

  * provide the argument `config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--admin-emails`=[`ADMIN_EMAILS`,…]
     Email addresses of administrators for this workspace configuration. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--kacls-owner-domains`=[`KACLS_OWNER_DOMAINS`,…]
     List of allowed Google Workspace customer domains where the KACLS is registered. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

Update annotations. 

At most one of these can be specified: 

`--annotations`=[`ANNOTATIONS`,…]
     Set annotations to new value. Annotations as key value pairs. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --annotations=string=string

`JSON Example:`
    
    
    --annotations='{"string": "string"}'

`File Example:`
    
    
    --annotations=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-annotations`=[`UPDATE_ANNOTATIONS`,…]
     Update annotations value or add key value pair. Annotations as key value pairs. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-annotations=string=string

`JSON Example:`
    
    
    --update-annotations='{"string": "string"}'

`File Example:`
    
    
    --update-annotations=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-annotations`
     Clear annotations value and set to empty map. 
`--remove-annotations`=`REMOVE_ANNOTATIONS`
     Remove existing value from map annotations. Sets `remove_annotations` value. `Shorthand Example:`
    
    
    --remove-annotations=string,string

`JSON Example:`
    
    
    --remove-annotations=["string"]

`File Example:`
    
    
    --remove-annotations=path_to_file.(yaml|json)

Update idp_configs. 

At most one of these can be specified: 

`--idp-configs`=[`additionalAudiences`=`ADDITIONALAUDIENCES`],[`audience`=`AUDIENCE`],[`idpType`=`IDPTYPE`],[`issuer`=`ISSUER`],[`jwksUri`=`JWKSURI`]
     Set idp_configs to new value. The Identity Provider configurations. 

`additionalAudiences`
     The expected additional audiences in the JWTs. 
`audience`
     The expected audience in the JWTs. 
`idpType`
     The type of the IdP. 
`issuer`
     The issuer of the IdP. 
`jwksUri`
     The JSON Web Key Set (JWKS) URI of the IdP. 
`Shorthand Example:`
    
    
    --idp-configs=additionalAudiences=[string],audience=string,idpType=string,issuer=string,jwksUri=string --idp-configs=additionalAudiences=[string],audience=string,idpType=string,issuer=string,jwksUri=string

`JSON Example:`
    
    
    --idp-configs='[{"additionalAudiences": ["string"], "audience": "string", "idpType": "string", "issuer": "string", "jwksUri": "string"}]'

`File Example:`
    
    
    --idp-configs=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-idp-configs`=[`additionalAudiences`=`ADDITIONALAUDIENCES`],[`audience`=`AUDIENCE`],[`idpType`=`IDPTYPE`],[`issuer`=`ISSUER`],[`jwksUri`=`JWKSURI`]
     Add new value to idp_configs list. The Identity Provider configurations. 

`additionalAudiences`
     The expected additional audiences in the JWTs. 
`audience`
     The expected audience in the JWTs. 
`idpType`
     The type of the IdP. 
`issuer`
     The issuer of the IdP. 
`jwksUri`
     The JSON Web Key Set (JWKS) URI of the IdP. 
`Shorthand Example:`
    
    
    --add-idp-configs=additionalAudiences=[string],audience=string,idpType=string,issuer=string,jwksUri=string --add-idp-configs=additionalAudiences=[string],audience=string,idpType=string,issuer=string,jwksUri=string

`JSON Example:`
    
    
    --add-idp-configs='[{"additionalAudiences": ["string"], "audience": "string", "idpType": "string", "issuer": "string", "jwksUri": "string"}]'

`File Example:`
    
    
    --add-idp-configs=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-idp-configs`
     Clear idp_configs value and set to empty list. 
`--remove-idp-configs`=[`additionalAudiences`=`ADDITIONALAUDIENCES`],[`audience`=`AUDIENCE`],[`idpType`=`IDPTYPE`],[`issuer`=`ISSUER`],[`jwksUri`=`JWKSURI`]
     Remove existing value from idp_configs list. The Identity Provider configurations. 

`additionalAudiences`
     The expected additional audiences in the JWTs. 
`audience`
     The expected audience in the JWTs. 
`idpType`
     The type of the IdP. 
`issuer`
     The issuer of the IdP. 
`jwksUri`
     The JSON Web Key Set (JWKS) URI of the IdP. 
`Shorthand Example:`
    
    
    --remove-idp-configs=additionalAudiences=[string],audience=string,idpType=string,issuer=string,jwksUri=string --remove-idp-configs=additionalAudiences=[string],audience=string,idpType=string,issuer=string,jwksUri=string

`JSON Example:`
    
    
    --remove-idp-configs='[{"additionalAudiences": ["string"], "audience": "string", "idpType": "string", "issuer": "string", "jwksUri": "string"}]'

`File Example:`
    
    
    --remove-idp-configs=path_to_file.(yaml|json)

Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. Labels as key value pairs. 

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

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

Update tags. 

At most one of these can be specified: 

`--tags`=[`TAGS`,…]
     Set tags to new value. Tag bindings as key value pairs. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --tags=string=string

`JSON Example:`
    
    
    --tags='{"string": "string"}'

`File Example:`
    
    
    --tags=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-tags`=[`UPDATE_TAGS`,…]
     Update tags value or add key value pair. Tag bindings as key value pairs. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-tags=string=string

`JSON Example:`
    
    
    --update-tags='{"string": "string"}'

`File Example:`
    
    
    --update-tags=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-tags`
     Clear tags value and set to empty map. 
`--remove-tags`=`REMOVE_TAGS`
     Remove existing value from map tags. Sets `remove_tags` value. `Shorthand Example:`
    
    
    --remove-tags=string,string

`JSON Example:`
    
    
    --remove-tags=["string"]

`File Example:`
    
    
    --remove-tags=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `workspacekeyaccess/v1beta` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/kms/docs/hsm-for-workspace>
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
