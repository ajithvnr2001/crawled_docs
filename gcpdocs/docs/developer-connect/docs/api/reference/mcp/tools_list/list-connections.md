---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/list-connections/
title: MCP Tools Reference: developerconnect.googleapis.com \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:00.483377+00:00
---

# MCP Tools Reference: developerconnect.googleapis.com  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/list-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  MCP Tools Reference: developerconnect.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list-connections`

List connections in a given project and location.

The following code sample shows how to use `curl` to call the `list-connections` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://developerconnect.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list-connections",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Message for requesting list of Connections

### ListConnectionsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. Parent value for ListConnectionsRequest  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results.  
`orderBy` |  `string` Optional. Hint for how to order the results.  
  
## Output Schema

Message for response to listing Connections

### ListConnectionsResponse

JSON representation  
---  
      
    
    {
      "connections": [
        {
          object ([Connection](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.Connection))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`connections[]` |  `object (`[Connection](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.Connection)`)` The list of Connections.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Connection

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "labels": {
        string: string,
        ...
      },
      "installationState": {
        object ([InstallationState](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.InstallationState))
      },
      "disabled": boolean,
      "reconciling": boolean,
      "annotations": {
        string: string,
        ...
      },
      "etag": string,
      "uid": string,
      "cryptoKeyConfig": {
        object ([CryptoKeyConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.CryptoKeyConfig))
      },
      "gitProxyConfig": {
        object ([GitProxyConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitProxyConfig))
      },
    
      // Union field connection_config can be only one of the following:
      "githubConfig": {
        object ([GitHubConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitHubConfig))
      },
      "githubEnterpriseConfig": {
        object ([GitHubEnterpriseConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitHubEnterpriseConfig))
      },
      "gitlabConfig": {
        object ([GitLabConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitLabConfig))
      },
      "gitlabEnterpriseConfig": {
        object ([GitLabEnterpriseConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitLabEnterpriseConfig))
      },
      "bitbucketDataCenterConfig": {
        object ([BitbucketDataCenterConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BitbucketDataCenterConfig))
      },
      "bitbucketCloudConfig": {
        object ([BitbucketCloudConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BitbucketCloudConfig))
      },
      "secureSourceManagerInstanceConfig": {
        object ([SecureSourceManagerInstanceConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.SecureSourceManagerInstanceConfig))
      },
      "httpConfig": {
        object ([GenericHTTPEndpointConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GenericHTTPEndpointConfig))
      }
      // End of list of possible types for union field connection_config.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Delete timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`installationState` |  `object (`[InstallationState](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.InstallationState)`)` Output only. Installation state of the Connection.  
`disabled` |  `boolean` Optional. If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.  
`reconciling` |  `boolean` Output only. Set to true when the connection is being set up or updated in the background.  
`annotations` |  `map (key: string, value: string)` Optional. Allows clients to store small amounts of arbitrary data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`uid` |  `string` Output only. A system-assigned unique identifier for the Connection.  
`cryptoKeyConfig` |  `object (`[CryptoKeyConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.CryptoKeyConfig)`)` Optional. The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.  
`gitProxyConfig` |  `object (`[GitProxyConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitProxyConfig)`)` Optional. Configuration for the Git proxy feature. Enabling the Git proxy allows clients to perform Git operations on the repositories linked in the connection. [Learn more](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy).  
Union field `connection_config`. Configuration for the connection depending on the type of provider. `connection_config` can be only one of the following:  
`githubConfig` |  `object (`[GitHubConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitHubConfig)`)` Configuration for connections to github.com.  
`githubEnterpriseConfig` |  `object (`[GitHubEnterpriseConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitHubEnterpriseConfig)`)` Configuration for connections to an instance of GitHub Enterprise.  
`gitlabConfig` |  `object (`[GitLabConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitLabConfig)`)` Configuration for connections to gitlab.com.  
`gitlabEnterpriseConfig` |  `object (`[GitLabEnterpriseConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitLabEnterpriseConfig)`)` Configuration for connections to an instance of GitLab Enterprise.  
`bitbucketDataCenterConfig` |  `object (`[BitbucketDataCenterConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BitbucketDataCenterConfig)`)` Configuration for connections to an instance of Bitbucket Data Center.  
`bitbucketCloudConfig` |  `object (`[BitbucketCloudConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BitbucketCloudConfig)`)` Configuration for connections to an instance of Bitbucket Clouds.  
`secureSourceManagerInstanceConfig` |  `object (`[SecureSourceManagerInstanceConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.SecureSourceManagerInstanceConfig)`)` Configuration for connections to an instance of Secure Source Manager.  
`httpConfig` |  `object (`[GenericHTTPEndpointConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GenericHTTPEndpointConfig)`)` Optional. Configuration for connections to an HTTP service provider.  
  
### GitHubConfig

JSON representation  
---  
      
    
    {
      "githubApp": enum ([GitHubApp](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitHubApp)),
      "authorizerCredential": {
        object ([OAuthCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.OAuthCredential))
      },
      "appInstallationId": string,
      "installationUri": string
    }  
  
Fields  
---  
`githubApp` |  `enum (`[GitHubApp](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.GitHubApp)`)` Required. Immutable. The GitHub Application that was installed to the GitHub user or organization.  
`authorizerCredential` |  `object (`[OAuthCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.OAuthCredential)`)` Optional. OAuth credential of the account that authorized the GitHub App. It is recommended to use a robot account instead of a human user account. The OAuth token must be tied to the GitHub App of this config.  
`appInstallationId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. GitHub App installation id.  
`installationUri` |  `string` Output only. The URI to navigate to in order to manage the installation associated with this GitHubConfig.  
  
### OAuthCredential

JSON representation  
---  
      
    
    {
      "oauthTokenSecretVersion": string,
      "username": string
    }  
  
Fields  
---  
`oauthTokenSecretVersion` |  `string` Required. A SecretManager resource containing the OAuth token that authorizes the connection. Format: `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location).  
`username` |  `string` Output only. The username associated with this token.  
  
### GitHubEnterpriseConfig

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "appId": string,
      "appSlug": string,
      "privateKeySecretVersion": string,
      "webhookSecretSecretVersion": string,
      "appInstallationId": string,
      "installationUri": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig))
      },
      "serverVersion": string,
      "sslCaCertificate": string,
      "organization": string
    }  
  
Fields  
---  
`hostUri` |  `string` Required. The URI of the GitHub Enterprise host this connection is for.  
`appId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. ID of the GitHub App created from the manifest.  
`appSlug` |  `string` Output only. The URL-friendly name of the GitHub App.  
`privateKeySecretVersion` |  `string` Optional. SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location).  
`webhookSecretSecretVersion` |  `string` Optional. SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location).  
`appInstallationId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. ID of the installation of the GitHub App.  
`installationUri` |  `string` Output only. The URI to navigate to in order to manage the installation associated with this GitHubEnterpriseConfig.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig)`)` Optional. Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet.  
`serverVersion` |  `string` Output only. GitHub Enterprise version installed at the host_uri.  
`sslCaCertificate` |  `string` Optional. SSL certificate to use for requests to GitHub Enterprise.  
`organization` |  `string` Optional. Immutable. GitHub Enterprise organization in which the GitHub App is created.  
  
### ServiceDirectoryConfig

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The Service Directory service name. Format: projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}.  
  
### GitLabConfig

JSON representation  
---  
      
    
    {
      "webhookSecretSecretVersion": string,
      "readAuthorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      },
      "authorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      }
    }  
  
Fields  
---  
`webhookSecretSecretVersion` |  `string` Required. Immutable. SecretManager resource containing the webhook secret of a GitLab project, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). This is used to validate webhooks.  
`readAuthorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. A GitLab personal access token with the minimum `read_api` scope access and a minimum role of `reporter`. The GitLab Projects visible to this Personal Access Token will control which Projects Developer Connect has access to.  
`authorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. A GitLab personal access token with the minimum `api` scope access and a minimum role of `maintainer`. The GitLab Projects visible to this Personal Access Token will control which Projects Developer Connect has access to.  
  
### UserCredential

JSON representation  
---  
      
    
    {
      "userTokenSecretVersion": string,
      "username": string
    }  
  
Fields  
---  
`userTokenSecretVersion` |  `string` Required. A SecretManager resource containing the user token that authorizes the Developer Connect connection. Format: `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location).  
`username` |  `string` Output only. The username associated with this token.  
  
### GitLabEnterpriseConfig

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "webhookSecretSecretVersion": string,
      "readAuthorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      },
      "authorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig))
      },
      "sslCaCertificate": string,
      "serverVersion": string
    }  
  
Fields  
---  
`hostUri` |  `string` Required. The URI of the GitLab Enterprise host this connection is for.  
`webhookSecretSecretVersion` |  `string` Required. Immutable. SecretManager resource containing the webhook secret of a GitLab project, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). This is used to validate webhooks.  
`readAuthorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. A GitLab personal access token with the minimum `read_api` scope access and a minimum role of `reporter`. The GitLab Projects visible to this Personal Access Token will control which Projects Developer Connect has access to.  
`authorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. A GitLab personal access token with the minimum `api` scope access and a minimum role of `maintainer`. The GitLab Projects visible to this Personal Access Token will control which Projects Developer Connect has access to.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig)`)` Optional. Configuration for using Service Directory to privately connect to a GitLab Enterprise instance. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet.  
`sslCaCertificate` |  `string` Optional. SSL Certificate Authority certificate to use for requests to GitLab Enterprise instance.  
`serverVersion` |  `string` Output only. Version of the GitLab Enterprise server running on the `host_uri`.  
  
### BitbucketDataCenterConfig

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "webhookSecretSecretVersion": string,
      "readAuthorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      },
      "authorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig))
      },
      "sslCaCertificate": string,
      "serverVersion": string
    }  
  
Fields  
---  
`hostUri` |  `string` Required. The URI of the Bitbucket Data Center host this connection is for.  
`webhookSecretSecretVersion` |  `string` Required. Immutable. SecretManager resource containing the webhook secret used to verify webhook events, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). This is used to validate webhooks.  
`readAuthorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. An http access token with the minimum `Repository read` access. It's recommended to use a system account to generate the credentials.  
`authorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. An http access token with the minimum `Repository admin` scope access. This is needed to create webhooks. It's recommended to use a system account to generate these credentials.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig)`)` Optional. Configuration for using Service Directory to privately connect to a Bitbucket Data Center instance. This should only be set if the Bitbucket Data Center is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the Bitbucket Data Center will be made over the public internet.  
`sslCaCertificate` |  `string` Optional. SSL certificate authority to trust when making requests to Bitbucket Data Center.  
`serverVersion` |  `string` Output only. Version of the Bitbucket Data Center server running on the `host_uri`.  
  
### BitbucketCloudConfig

JSON representation  
---  
      
    
    {
      "workspace": string,
      "webhookSecretSecretVersion": string,
      "readAuthorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      },
      "authorizerCredential": {
        object ([UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential))
      }
    }  
  
Fields  
---  
`workspace` |  `string` Required. The Bitbucket Cloud Workspace ID to be connected to Google Cloud Platform.  
`webhookSecretSecretVersion` |  `string` Required. Immutable. SecretManager resource containing the webhook secret used to verify webhook events, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). This is used to validate and create webhooks.  
`readAuthorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. An access token with the minimum `repository` access. It can either be a workspace, project or repository access token. It's recommended to use a system account to generate the credentials.  
`authorizerCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.UserCredential)`)` Required. An access token with the minimum `repository`, `pullrequest` and `webhook` scope access. It can either be a workspace, project or repository access token. This is needed to create webhooks. It's recommended to use a system account to generate these credentials.  
  
### SecureSourceManagerInstanceConfig

JSON representation  
---  
      
    
    {
      "instance": string
    }  
  
Fields  
---  
`instance` |  `string` Required. Immutable. Secure Source Manager instance resource, formatted as `projects/*/locations/*/instances/*`  
  
### GenericHTTPEndpointConfig

JSON representation  
---  
      
    
    {
      "hostUri": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig))
      },
      "sslCaCertificate": string,
    
      // Union field authentication can be only one of the following:
      "basicAuthentication": {
        object ([BasicAuthentication](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BasicAuthentication))
      },
      "bearerTokenAuthentication": {
        object ([BearerTokenAuthentication](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BearerTokenAuthentication))
      }
      // End of list of possible types for union field authentication.
    }  
  
Fields  
---  
`hostUri` |  `string` Required. Immutable. The service provider's https endpoint.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.ServiceDirectoryConfig)`)` Optional. Configuration for using Service Directory to privately connect to a HTTP service provider. This should only be set if the Http service provider is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the HTTP service provider will be made over the public internet.  
`sslCaCertificate` |  `string` Optional. The SSL certificate to use for requests to the HTTP service provider.  
Union field `authentication`. The authentication mechanism to use for requests to the HTTP service provider. `authentication` can be only one of the following:  
`basicAuthentication` |  `object (`[BasicAuthentication](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BasicAuthentication)`)` Optional. Basic authentication with username and password.  
`bearerTokenAuthentication` |  `object (`[BearerTokenAuthentication](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.BearerTokenAuthentication)`)` Optional. Bearer token authentication with a token.  
  
### BasicAuthentication

JSON representation  
---  
      
    
    {
      "username": string,
    
      // Union field password can be only one of the following:
      "passwordSecretVersion": string
      // End of list of possible types for union field password.
    }  
  
Fields  
---  
`username` |  `string` Required. The username to authenticate as.  
Union field `password`. The password to authenticate as. `password` can be only one of the following:  
`passwordSecretVersion` |  `string` The password SecretManager secret version to authenticate as.  
  
### BearerTokenAuthentication

JSON representation  
---  
      
    
    {
    
      // Union field token can be only one of the following:
      "tokenSecretVersion": string
      // End of list of possible types for union field token.
    }  
  
Fields  
---  
Union field `token`. The token to authenticate as. `token` can be only one of the following:  
`tokenSecretVersion` |  `string` Optional. The token SecretManager secret version to authenticate as.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### InstallationState

JSON representation  
---  
      
    
    {
      "stage": enum ([Stage](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.Stage)),
      "message": string,
      "actionUri": string
    }  
  
Fields  
---  
`stage` |  `enum (`[Stage](https://docs.cloud.google.com/developer-connect/docs/api/reference/mcp/tools_list/create-connection#Input.Schema.Stage)`)` Output only. Current step of the installation process.  
`message` |  `string` Output only. Message of what the user should do next to continue the installation. Empty string if the installation is already complete.  
`actionUri` |  `string` Output only. Link to follow for next action. Empty string if the installation is already complete.  
  
### AnnotationsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### CryptoKeyConfig

JSON representation  
---  
      
    
    {
      "keyReference": string
    }  
  
Fields  
---  
`keyReference` |  `string` Required. The name of the key which is used to encrypt/decrypt customer data. For key in Cloud KMS, the key should be in the format of `projects/*/locations/*/keyRings/*/cryptoKeys/*`.  
  
### GitProxyConfig

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "httpProxyBaseUri": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Setting this to true allows the Git proxy to be used for performing Git operations on the repositories linked in the connection.  
`httpProxyBaseUri` |  `string` Output only. The base URI for the HTTP proxy endpoint. Has the format `https://{generatedID}-c-h-{shortRegion}.developerconnect.dev` Populated only when enabled is set to true. This endpoint is used by other Google services that integrate with Developer Connect.  
  
### GitHubApp

Represents the various GitHub Applications that can be installed to a GitHub user or organization and used with Developer Connect.

Enums  
---  
`GIT_HUB_APP_UNSPECIFIED` | GitHub App not specified.  
`DEVELOPER_CONNECT` | The Developer Connect GitHub Application.  
`FIREBASE` | The Firebase GitHub Application.  
`GEMINI_CODE_ASSIST` | The Gemini Code Assist Application.  
`DATAFORM` | The Dataform GitHub Application.  
  
### Stage

Stage of the installation process.

Enums  
---  
`STAGE_UNSPECIFIED` | No stage specified.  
`PENDING_CREATE_APP` | Only for GitHub Enterprise. An App creation has been requested. The user needs to confirm the creation in their GitHub enterprise host.  
`PENDING_USER_OAUTH` | User needs to authorize the GitHub (or Enterprise) App via OAuth.  
`PENDING_INSTALL_APP` | User needs to follow the link to install the GitHub (or Enterprise) App.  
`COMPLETE` | Installation process has been completed.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
