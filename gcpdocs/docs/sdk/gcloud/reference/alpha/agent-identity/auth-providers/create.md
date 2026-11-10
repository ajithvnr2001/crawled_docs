---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/create/
title: gcloud alpha agent-identity auth-providers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:33:59.049794+00:00
---

# gcloud alpha agent-identity auth-providers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity/auth-providers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha agent-identity auth-providers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha agent-identity auth-providers create - create an auth provider 
SYNOPSIS
    

`gcloud alpha agent-identity auth-providers create` `AUTH_PROVIDER` (`--api-key`=`API_KEY` | [`--connector-reference-auth-provider`=`CONNECTOR_REFERENCE_AUTH_PROVIDER` : `--connector-reference-auth-provider-authorization-details`=`CONNECTOR_REFERENCE_AUTH_PROVIDER_AUTHORIZATION_DETAILS`] | `--three-legged-oauth-authorization-url`=`THREE_LEGGED_OAUTH_AUTHORIZATION_URL` `--three-legged-oauth-client-id`=`THREE_LEGGED_OAUTH_CLIENT_ID` `--three-legged-oauth-client-secret`=`THREE_LEGGED_OAUTH_CLIENT_SECRET` `--three-legged-oauth-default-continue-uri`=`THREE_LEGGED_OAUTH_DEFAULT_CONTINUE_URI` `--three-legged-oauth-enable-pkce` `--three-legged-oauth-token-url`=`THREE_LEGGED_OAUTH_TOKEN_URL` | `--two-legged-oauth-client-id`=`TWO_LEGGED_OAUTH_CLIENT_ID` `--two-legged-oauth-client-secret`=`TWO_LEGGED_OAUTH_CLIENT_SECRET` `--two-legged-oauth-token-url`=`TWO_LEGGED_OAUTH_TOKEN_URL` | `--xaa-auth-provider-additional-parameters`=[`XAA_AUTH_PROVIDER_ADDITIONAL_PARAMETERS`,…] `--xaa-auth-provider-client-assertion-jwt-id`=`XAA_AUTH_PROVIDER_CLIENT_ASSERTION_JWT_ID` | `--xaa-auth-provider-client-secret`=`XAA_AUTH_PROVIDER_CLIENT_SECRET` `--xaa-auth-provider-client-secret-id`=`XAA_AUTH_PROVIDER_CLIENT_SECRET_ID` [`--xaa-auth-provider-custom-issuer-token-url`=`XAA_AUTH_PROVIDER_CUSTOM_ISSUER_TOKEN_URL` : `--xaa-auth-provider-custom-issuer`=`XAA_AUTH_PROVIDER_CUSTOM_ISSUER`] `--xaa-auth-provider-id-token-input-jag`=`XAA_AUTH_PROVIDER_ID_TOKEN_INPUT_JAG` `--xaa-auth-provider-id-token-input-jag-additional-claims`=`XAA_AUTH_PROVIDER_ID_TOKEN_INPUT_JAG_ADDITIONAL_CLAIMS`) [`--allowed-scopes`=[`ALLOWED_SCOPES`,…]] [`--blocked-scopes`=[`BLOCKED_SCOPES`,…]] [`--description`=`DESCRIPTION`] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--request-id`=`REQUEST_ID`] [`--workload-ids`=[`WORKLOAD_IDS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new auth provider in a given project and location. 
EXAMPLES
     To create an API key auth provider 'my-auth-provider' in location 'us-central1' and project 'my-project', run: 
    
    
    gcloud alpha agent-identity auth-providers create my-auth-provider --location=us-central1 --project=my-project --api-key=my-api-key

POSITIONAL ARGUMENTS
    

AuthProvider resource - Identifier. The full resource name of the auth provider. Format: projects/{project}/locations/{location}/authProviders/{auth_provider} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `auth_provider` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `auth_provider` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`AUTH_PROVIDER`
     ID of the authProvider or fully qualified identifier for the authProvider. 

To set the `auth_provider` attribute: 

  * provide the argument `auth_provider` on the command line. 


REQUIRED FLAGS
    

Required. Parameters specific to the auth provider type. 

This must be specified. 

Arguments for the type. 

At most one of these can be specified: 

Configuration for API key authentication. 
`--api-key`=`API_KEY`
     The API key for this auth provider. 
Configuration parameters for the Connector Reference auth provider. 
`--connector-reference-auth-provider`=`CONNECTOR_REFERENCE_AUTH_PROVIDER`
     The name of the referenced connector. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--connector-reference-auth-provider-authorization-details`=`CONNECTOR_REFERENCE_AUTH_PROVIDER_AUTHORIZATION_DETAILS`
     Rich Authorization Requests (RFC 9396) detailing targeted OAuth resources/scopes, formatted as a JSON array of JSON objects. 
Configuration for 3-legged OAuth (3LO) authentication. 
`--three-legged-oauth-authorization-url`=`THREE_LEGGED_OAUTH_AUTHORIZATION_URL`
     The authorization endpoint to send users to for consenting to delegate to the agent. For example, "https://auth.atlassian.com/authorize". 
`--three-legged-oauth-client-id`=`THREE_LEGGED_OAUTH_CLIENT_ID`
     The client ID of the OAuth client. 
`--three-legged-oauth-client-secret`=`THREE_LEGGED_OAUTH_CLIENT_SECRET`
     The client secret of the OAuth client. 
`--three-legged-oauth-default-continue-uri`=`THREE_LEGGED_OAUTH_DEFAULT_CONTINUE_URI`
     The default continue URI for the 3LO flow, used when no continue URI is provided in the RetrieveCredentials request. 
`--three-legged-oauth-enable-pkce`
     Enables Proof Key for Code Exchange (PKCE) for the OAuth flow to prevent authorization code interception attacks. 
`--three-legged-oauth-token-url`=`THREE_LEGGED_OAUTH_TOKEN_URL`
     The token endpoint for requesting tokens on behalf of an end user. For example, "https://auth.atlassian.com/oauth/token". 
Configuration for 2-legged OAuth (2LO) authentication. 
`--two-legged-oauth-client-id`=`TWO_LEGGED_OAUTH_CLIENT_ID`
     The client ID of the OAuth client. 
`--two-legged-oauth-client-secret`=`TWO_LEGGED_OAUTH_CLIENT_SECRET`
     The client secret of the OAuth client. 
`--two-legged-oauth-token-url`=`TWO_LEGGED_OAUTH_TOKEN_URL`
     The token endpoint of the OAuth client. 
Configuration parameters for the Cross-App Access auth provider. 
`--xaa-auth-provider-additional-parameters`=[`XAA_AUTH_PROVIDER_ADDITIONAL_PARAMETERS`,…]
     Additional parameters to be passed to the token endpoint. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --xaa-auth-provider-additional-parameters=string=string

`JSON Example:`
    
    
    --xaa-auth-provider-additional-parameters='{"string": "string"}'

`File Example:`
    
    
    --xaa-auth-provider-additional-parameters=path_to_file.(yaml|json)

Arguments for the client authentication. 

At most one of these can be specified: 

Configuration for client ID and client assertion JWT authentication. 
`--xaa-auth-provider-client-assertion-jwt-id`=`XAA_AUTH_PROVIDER_CLIENT_ASSERTION_JWT_ID`
     The client identifier. 
Configuration for client ID and client secret authentication. 
`--xaa-auth-provider-client-secret`=`XAA_AUTH_PROVIDER_CLIENT_SECRET`
     The client secret. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--xaa-auth-provider-client-secret-id`=`XAA_AUTH_PROVIDER_CLIENT_SECRET_ID`
     The client identifier. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Arguments for the issuer type. 

At most one of these can be specified: 

Configuration for a custom or third-party authorization server issuer. 
`--xaa-auth-provider-custom-issuer-token-url`=`XAA_AUTH_PROVIDER_CUSTOM_ISSUER_TOKEN_URL`
     The token endpoint of the target OAuth authorization server to retrieve resource tokens. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--xaa-auth-provider-custom-issuer`=`XAA_AUTH_PROVIDER_CUSTOM_ISSUER`
     The issuer identifier of the target Authorization Server. 
Arguments for the identity source. 

At most one of these can be specified: 

Defines how to process an input ID token to obtain an ID-JAG. 
Arguments for the id jag source. 

At most one of these can be specified: 

AuthProvider resource - The resource name of the ID-JAG auth provider. Format: "projects/{project}/locations/{location}/authProviders/{auth_provider}" This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--xaa-auth-provider-id-token-input-jag` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--xaa-auth-provider-id-token-input-jag` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--xaa-auth-provider-id-token-input-jag`=`XAA_AUTH_PROVIDER_ID_TOKEN_INPUT_JAG`
     ID of the authProvider or fully qualified identifier for the authProvider. 

To set the `auth-provider` attribute: 

  * provide the argument `--xaa-auth-provider-id-token-input-jag` on the command line. 


`--xaa-auth-provider-id-token-input-jag-additional-claims`=`XAA_AUTH_PROVIDER_ID_TOKEN_INPUT_JAG_ADDITIONAL_CLAIMS`
     Optional additional claims to include when fetching an ID-JAG. 
OPTIONAL FLAGS
    

`--allowed-scopes`=[`ALLOWED_SCOPES`,…]
     List of scopes that are allowed to be requested for this auth provider. If this list is non-empty, only scopes within this list may be requested. If this list is empty, all scopes may be requested. Scopes appearing in `blocked_scopes` are disallowed even if they appear in `allowed_scopes`. The number of allowed scopes is limited to 200. 
`--blocked-scopes`=[`BLOCKED_SCOPES`,…]
     List of scopes that are blocked from being requested for this auth provider. If a scope appears in this list, it will not be requested, even if it also appears in `allowed_scopes`. `blocked_scopes` takes precedence over `allowed_scopes`. The number of blocked scopes is limited to 200\. 
`--description`=`DESCRIPTION`
     Description of the resource. Must be less than 256 characters. 
`--labels`=[`LABELS`,…]
     Labels as key-value pairs. 

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
     For resources [auth_provider, xaa-auth-provider-id-token-input-jag], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--workload-ids`=[`WORKLOAD_IDS`,…]
     Identifiers for the agents that will use this auth provider, starting with `principal://`. For example: `principal://agents.global.org-${ORG_ID}.system.id.goog/resources/aiplatform/projects/{PROJECT_ID}/locations/{LOCATIONS}/reasoningEngines/{ID}`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentidentity/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud agent-identity auth-providers create](https://docs.cloud.google.com/sdk/gcloud/reference/agent-identity/auth-providers/create)
    
    
    [gcloud beta agent-identity auth-providers create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/agent-identity/auth-providers/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
