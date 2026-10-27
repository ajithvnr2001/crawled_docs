---
url: https://ai.google.dev/api/credentials/
title: Gemini Credentials API
method: scrapling+scrapegraph
fetched_at: 2026-10-27T09:34:38.595158+00:00
---

# Gemini Credentials API

> Source: https://ai.google.dev/api/credentials/

The Credentials API allows you to create, retrieve, update, list, and delete server-managed credentials (such as API keys, OAuth2 tokens, HTTP Bearer tokens, and environment variables) to authenticate tool calls and MCP servers.

[View as markdown](https://ai.google.dev/static/api/credentials.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)

## CreateCredential

post  https://generativelanguage.googleapis.com/v1beta/credentials 

Creates a new credential.

  * Request body
  * Response



### Request body

The request body structure depends on the interaction mode you choose:

EnvironmentVariableConfig 

Configuration for environment variable credentials.

value string (required)

Required. Input only. Secret value of the environment variable. Write-only; never returned in responses.

injection_location InjectionLocation or array (InjectionLocation) (required)

Required. Locations where the environment variable can be injected in outgoing HTTP requests. Must contain at least one location. Accepts either a single location (e.g. "header") or an array of locations.

#### Possible Types

InjectionLocation

  * `header`: Injected into HTTP request headers. 
  * `query`: Injected into HTTP URL query parameters. 
  * `body`: Injected into HTTP request body. 



array (InjectionLocation)

  * `header`: Injected into HTTP request headers. 
  * `query`: Injected into HTTP URL query parameters. 
  * `body`: Injected into HTTP request body. 



id string (required)

No description provided.

type object (required)

No description provided.

trusted_domains array (string) (optional)

Optional. List of domains allowed to receive this environment variable value in HTTP requests.

HttpBearerConfig 

Configuration for HTTP Bearer token credentials.

token string (required)

Required. Input only. The static bearer token. Write-only; never returned in responses.

id string (required)

No description provided.

type object (required)

No description provided.

header_name string (optional)

Optional. Header name to inject the token into. Defaults to 'Authorization'.

prefix string (optional)

Optional. Prefix to prepend to the token. Defaults to 'Bearer'. Set to '' for no prefix.

OAuth2Config 

Configuration for OAuth2 credentials with automatic token refresh.

client_id string (required)

Required. OAuth2 client ID.

client_secret string (required)

Required. Input only. OAuth2 client secret. Write-only; never returned in responses.

refresh_token string (required)

Required. Input only. OAuth2 refresh token. Write-only; never returned in responses.

token_url string (required)

Required. OAuth2 token endpoint URL for refreshing access tokens.

id string (required)

No description provided.

type object (required)

No description provided.

scopes array (string) (optional)

Optional. List of OAuth2 scopes.

### Response

If successful, the response body contains data with the following structure:

id string (required)

Required. Output only. Identifier. Unique identifier for the credential.

type enum (string) (required)

Required. Output only. The type of credential.

Possible values:

  * `bearer_token`

Static token injected as header. No refresh logic.

  * `oauth2`

Auto-refresh expired access tokens using stored refresh token.

  * `environment_variable`

Environment variable injected into sandbox container.




status enum (string) (optional)

Output only. Current status of the credential.

Possible values:

  * `active`

The credential is active and valid for use.

  * `revoked`

The credential has been revoked and is no longer valid.




create_time string (optional)

Output only. The timestamp when the credential was created.

update_time string (optional)

Output only. The timestamp when the credential was last updated.

### Example

####  Example Response
    
    
    {
      "id": "string",
      "type": "bearer_token",
      "status": "active",
      "create_time": "string",
      "update_time": "string"
    }

## ListCredentials

get  https://generativelanguage.googleapis.com/v1beta/credentials 

Lists credentials.

  * Path / Query parameters
  * Response



### Path / Query Parameters

page_size integer (optional)

Optional. Maximum number of credentials to return.

page_token string (optional)

Optional. Pagination token.

### Response

If successful, the response body contains data with the following structure:

credentials array (Credential) (optional)

No description provided.

next_page_token string (optional)

No description provided.

### Example

####  Example Response
    
    
    {
      "credentials": [
        {
          "id": "string",
          "type": "bearer_token",
          "status": "active",
          "create_time": "string",
          "update_time": "string"
        }
      ],
      "next_page_token": "string"
    }

## GetCredential

get  https://generativelanguage.googleapis.com/v1beta/credentials/{id} 

Gets a credential by ID.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.

### Response

If successful, the response body contains data with the following structure:

id string (required)

Required. Output only. Identifier. Unique identifier for the credential.

type enum (string) (required)

Required. Output only. The type of credential.

Possible values:

  * `bearer_token`

Static token injected as header. No refresh logic.

  * `oauth2`

Auto-refresh expired access tokens using stored refresh token.

  * `environment_variable`

Environment variable injected into sandbox container.




status enum (string) (optional)

Output only. Current status of the credential.

Possible values:

  * `active`

The credential is active and valid for use.

  * `revoked`

The credential has been revoked and is no longer valid.




create_time string (optional)

Output only. The timestamp when the credential was created.

update_time string (optional)

Output only. The timestamp when the credential was last updated.

### Example

####  Example Response
    
    
    {
      "id": "string",
      "type": "bearer_token",
      "status": "active",
      "create_time": "string",
      "update_time": "string"
    }

## UpdateCredential

patch  https://generativelanguage.googleapis.com/v1beta/credentials/{id} 

Updates a credential.

  * Path / Query parameters
  * Request body
  * Response



### Path / Query Parameters

id string (required)

Required. Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.

update_mask string (optional)

Optional. The list of fields to update.

### Request body

The request body structure depends on the interaction mode you choose:

EnvironmentVariableUpdateConfig 

Configuration for updating environment variable credentials.

type object (required)

No description provided.

value string (optional)

Optional. Input only. Secret value of the environment variable. Write-only; never returned in responses.

trusted_domains array (string) (optional)

Optional. List of domains allowed to receive this environment variable value in HTTP requests.

injection_location InjectionLocation or array (InjectionLocation) (optional)

Optional. Locations where the environment variable can be injected in outgoing HTTP requests. Accepts either a single location (e.g. "header") or an array of locations.

#### Possible Types

InjectionLocation

  * `header`: Injected into HTTP request headers. 
  * `query`: Injected into HTTP URL query parameters. 
  * `body`: Injected into HTTP request body. 



array (InjectionLocation)

  * `header`: Injected into HTTP request headers. 
  * `query`: Injected into HTTP URL query parameters. 
  * `body`: Injected into HTTP request body. 



HttpBearerUpdateConfig 

Configuration for updating HTTP Bearer token credentials.

type object (required)

No description provided.

token string (optional)

Optional. Input only. The static bearer token. Write-only; never returned in responses.

header_name string (optional)

Optional. Header name to inject the token into. Defaults to 'Authorization'.

prefix string (optional)

Optional. Prefix to prepend to the token. Defaults to 'Bearer'. Set to '' for no prefix.

OAuth2UpdateConfig 

Configuration for updating OAuth2 credentials.

type object (required)

No description provided.

client_id string (optional)

Optional. OAuth2 client ID.

client_secret string (optional)

Optional. Input only. OAuth2 client secret. Write-only; never returned in responses.

refresh_token string (optional)

Optional. Input only. OAuth2 refresh token. Write-only; never returned in responses.

token_url string (optional)

Optional. OAuth2 token endpoint URL for refreshing access tokens.

scopes array (string) (optional)

Optional. List of OAuth2 scopes.

### Response

If successful, the response body contains data with the following structure:

id string (required)

Required. Output only. Identifier. Unique identifier for the credential.

type enum (string) (required)

Required. Output only. The type of credential.

Possible values:

  * `bearer_token`

Static token injected as header. No refresh logic.

  * `oauth2`

Auto-refresh expired access tokens using stored refresh token.

  * `environment_variable`

Environment variable injected into sandbox container.




status enum (string) (optional)

Output only. Current status of the credential.

Possible values:

  * `active`

The credential is active and valid for use.

  * `revoked`

The credential has been revoked and is no longer valid.




create_time string (optional)

Output only. The timestamp when the credential was created.

update_time string (optional)

Output only. The timestamp when the credential was last updated.

### Example

####  Example Response
    
    
    {
      "id": "string",
      "type": "bearer_token",
      "status": "active",
      "create_time": "string",
      "update_time": "string"
    }

## DeleteCredential

delete  https://generativelanguage.googleapis.com/v1beta/credentials/{id} 

Deletes a credential.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.

### Response

If successful, the response is empty.

### Example

## Resources

### Credential

Server-managed credential resource stored in Secret Manager.

#### Fields

id string (required)

Required. Output only. Identifier. Unique identifier for the credential.

type enum (string) (required)

Required. Output only. The type of credential.

Possible values:

  * `bearer_token`

Static token injected as header. No refresh logic.

  * `oauth2`

Auto-refresh expired access tokens using stored refresh token.

  * `environment_variable`

Environment variable injected into sandbox container.




status enum (string) (optional)

Output only. Current status of the credential.

Possible values:

  * `active`

The credential is active and valid for use.

  * `revoked`

The credential has been revoked and is no longer valid.




create_time string (optional)

Output only. The timestamp when the credential was created.

update_time string (optional)

Output only. The timestamp when the credential was last updated.
