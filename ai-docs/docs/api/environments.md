---
url: https://ai.google.dev/api/environments/
title: Gemini Environments API
method: scrapling+scrapegraph
fetched_at: 2026-10-25T08:55:33.656448+00:00
---

# Gemini Environments API

> Source: https://ai.google.dev/api/environments/

Environments provide isolated execution contexts for running agent code, tools, and services securely.

[View as markdown](https://ai.google.dev/static/api/environments.md.txt) [View the OpenAPI Spec](https://ai.google.dev/static/api/interactions.openapi.json)

## CreateEnvironment

post  https://generativelanguage.googleapis.com/v1beta/environments 

Creates an environment.

  * Request body
  * Response



### Request body

The request body contains data with the following structure:

network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




sources array (Source) (optional)

Sources to be mounted into the environment.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

from_environment string (optional)

Optional. The source environment to copy/fork from. Format: `environments/{environment_id}` or `{environment_id}`. When specified, `sources` and `env` must be empty.

### Response

If successful, the response body contains data with the following structure:

id string (required)

Required. Output only. The ID of the environment.

sources array (Source) (optional)

Sources to be mounted into the environment.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

created string (optional)

Output only. The time at which the environment was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Output only. The time at which the environment was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

last_accessed string (optional)

Output only. The time at which the environment was last accessed in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

status enum (string) (optional)

Output only. The status of the environment container.

Possible values:

  * `active`

Output only. The status of the environment container.

  * `expired`

Output only. The status of the environment container.




network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




file_count string (optional)

Output only. The number of files in the environment, output only.

size_bytes string (optional)

Output only. The total size of the environment files in bytes, output only.

### Create

### Copy

## ListEnvironments

get  https://generativelanguage.googleapis.com/v1beta/environments 

Lists environments.

  * Path / Query parameters
  * Response



### Path / Query Parameters

page_size integer (optional)

Optional. Maximum number of environments to return. If unspecified, defaults to 50. Maximum is 1000.

page_token string (optional)

Optional. Pagination token.

### Response

If successful, the response body contains data with the following structure:

environments array (Environment) (optional)

Environments belonging to the provided project.

next_page_token string (optional)

Pagination token.

### List

## GetEnvironmentFiles

get  https://generativelanguage.googleapis.com/v1beta/environments/{environment}/files/{path} 

Retrieves file metadata or directory contents from an environment's snapshot. To download file content, use the download URL returned in the response.

  * Path / Query parameters
  * Response



### Path / Query Parameters

page_size integer (optional)

Optional. Maximum number of entries to return per page (for directory listing).

page_token string (optional)

Optional. Pagination token for directory listing.

recursive boolean (optional)

Optional. If true and the path is a directory, recursively lists all files.

### Response

If successful, the response body contains data with the following structure:

files array (EnvironmentFile) (optional)

If the requested path is a directory, this contains its contents. If the requested path is a file, this contains a single entry with the file's metadata. If alt=media was specified, this is empty (content is served via `blob`).

Metadata for a file or directory within an environment.

#### Fields

name string (optional)

Output only. The name of the file or directory (e.g., "main.py" or "src").

path string (optional)

Output only. The full relative path within the environment (e.g., "workspace/src/main.py").

type enum (string) (optional)

Output only. The type of the entry.

Possible values:

  * `file`

A regular file.

  * `directory`

A directory.




size_bytes string (optional)

Output only. The size of the file/directory in bytes. NOLINT

mime_type string (optional)

Output only. The MIME type of the file (e.g., "text/python", "image/png"). Empty for directories. NOLINT

created string (optional)

Output only. The creation time of the file/directory.

modified string (optional)

Output only. The modification time of the file/directory.

next_page_token string (optional)

Pagination token for directory listing. NOLINT

### List Files

### Get File

### Download File

## GetEnvironment

get  https://generativelanguage.googleapis.com/v1beta/environments/{id} 

Gets an environment.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.

### Response

If successful, the response body contains data with the following structure:

id string (required)

Required. Output only. The ID of the environment.

sources array (Source) (optional)

Sources to be mounted into the environment.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

created string (optional)

Output only. The time at which the environment was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Output only. The time at which the environment was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

last_accessed string (optional)

Output only. The time at which the environment was last accessed in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

status enum (string) (optional)

Output only. The status of the environment container.

Possible values:

  * `active`

Output only. The status of the environment container.

  * `expired`

Output only. The status of the environment container.




network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




file_count string (optional)

Output only. The number of files in the environment, output only.

size_bytes string (optional)

Output only. The total size of the environment files in bytes, output only.

### Get

## Start an environment file upload

put  https://generativelanguage.googleapis.com/upload/v1beta/environments/{environment}/files/{path} 

Starts a resumable upload session for a file in an environment workspace. Upload the file bytes to the URL returned in the `X-Goog-Upload-URL` response header, using the resumable upload protocol. 

  * Path / Query parameters
  * Response



### Path / Query Parameters

X-Goog-Upload-Command string (required)

Command that starts the resumable upload session.

_Defaults to:`start`_

X-Goog-Upload-Header-Content-Length integer (required)

Total number of file bytes that will be uploaded to the session URL.

X-Goog-Upload-Header-Content-Type string (required)

MIME type of the file that will be uploaded to the session URL.

X-Goog-Upload-Protocol string (required)

Resumable upload protocol selector.

_Defaults to:`resumable`_

extract boolean (optional)

Optional. If true, treats the uploaded file as a tar/tar.gz archive and unpacks it into `path`.

overwrite boolean (optional)

Optional. Whether to overwrite the destination file if it already exists.

### Response

If successful, the response is empty.

### Start Upload

## DeleteEnvironment

delete  https://generativelanguage.googleapis.com/v1beta/environments/{id} 

Deletes an environment.

  * Path / Query parameters
  * Response



### Path / Query Parameters

id string (required)

Required. Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.

### Response

If successful, the response is empty.

### Delete

## Resources

### Environment

An execution environment for an agent.

#### Fields

id string (required)

Required. Output only. The ID of the environment.

sources array (Source) (optional)

Sources to be mounted into the environment.

A source to be mounted into the environment.

#### Fields

type enum (string) (optional)

No description provided.

Possible values:

  * `gcs`

A Cloud Storage bucket.

  * `inline`

Inline content.

  * `repository`

A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).




source string (optional)

The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.

target string (optional)

Where the source should appear in the environment.

content string (optional)

The inline content if `type` is `INLINE`.

encoding string (optional)

Optional encoding for inline content (e.g. `base64`).

created string (optional)

Output only. The time at which the environment was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

updated string (optional)

Output only. The time at which the environment was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

last_accessed string (optional)

Output only. The time at which the environment was last accessed in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).

status enum (string) (optional)

Output only. The status of the environment container.

Possible values:

  * `active`

Output only. The status of the environment container.

  * `expired`

Output only. The status of the environment container.




network EnvironmentNetworkEgressAllowlist or enum (string) (optional)

Network configuration for the environment.

Network egress configuration for the environment.

#### Fields

allowlist array (EgressRule) or enum (string) (optional)

List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.

Possible values:

  * `disabled`

All network egress is blocked.




file_count string (optional)

Output only. The number of files in the environment, output only.

size_bytes string (optional)

Output only. The total size of the environment files in bytes, output only.
