---
url: https://docs.comfy.org/es/registry/api-reference/registry/update-changelog-and-deprecation-status-of-a-node-version/
title: Update changelog and deprecation status of a node version - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-30T13:55:14.783017+00:00
---

# Update changelog and deprecation status of a node version - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/update-changelog-and-deprecation-status-of-a-node-version/

Update changelog and deprecation status of a node version

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "changelog": "<string>",
      "deprecated": true
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    payload = {
        "changelog": "<string>",
        "deprecated": True
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.put(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PUT',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({changelog: '<string>', deprecated: true})
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'changelog' => '<string>',
        'deprecated' => true
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
      ],
    ]);
    
    $response = curl_exec($curl);
    $err = curl_error($curl);
    
    curl_close($curl);
    
    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    	payload := strings.NewReader("{\n  \"changelog\": \"<string>\",\n  \"deprecated\": true\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"changelog\": \"<string>\",\n  \"deprecated\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"changelog\": \"<string>\",\n  \"deprecated\": true\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

403

404

500
    
    
    {
      "changelog": "<string>",
      "comfy_node_extract_status": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "dependencies": [
        "<string>"
      ],
      "deprecated": true,
      "downloadUrl": "<string>",
      "id": "<string>",
      "node_id": "<string>",
      "status": "NodeVersionStatusActive",
      "status_reason": "<string>",
      "supported_accelerators": [
        "<string>"
      ],
      "supported_comfyui_frontend_version": "<string>",
      "supported_comfyui_version": "<string>",
      "supported_os": [
        "<string>"
      ],
      "tags": [
        "<string>"
      ],
      "tags_admin": [
        "<string>"
      ],
      "version": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry

# Update changelog and deprecation status of a node version

Copiar páginaCopiar página

Update only the changelog and deprecated status of a specific version of a node.

Copiar páginaCopiar página

PUT

/

publishers

/

{publisherId}

/

nodes

/

{nodeId}

/

versions

/

{versionId}

Pruébalo

Update changelog and deprecation status of a node version

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "changelog": "<string>",
      "deprecated": true
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    payload = {
        "changelog": "<string>",
        "deprecated": True
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.put(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'PUT',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({changelog: '<string>', deprecated: true})
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'changelog' => '<string>',
        'deprecated' => true
      ]),
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: application/json"
      ],
    ]);
    
    $response = curl_exec($curl);
    $err = curl_error($curl);
    
    curl_close($curl);
    
    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    	payload := strings.NewReader("{\n  \"changelog\": \"<string>\",\n  \"deprecated\": true\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"changelog\": \"<string>\",\n  \"deprecated\": true\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"changelog\": \"<string>\",\n  \"deprecated\": true\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

403

404

500
    
    
    {
      "changelog": "<string>",
      "comfy_node_extract_status": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "dependencies": [
        "<string>"
      ],
      "deprecated": true,
      "downloadUrl": "<string>",
      "id": "<string>",
      "node_id": "<string>",
      "status": "NodeVersionStatusActive",
      "status_reason": "<string>",
      "supported_accelerators": [
        "<string>"
      ],
      "supported_comfyui_frontend_version": "<string>",
      "supported_comfyui_version": "<string>",
      "supported_os": [
        "<string>"
      ],
      "tags": [
        "<string>"
      ],
      "tags_admin": [
        "<string>"
      ],
      "version": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Autorizaciones

​

Authorization

string

header

requerido

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Parámetros de ruta

​

publisherId

string

requerido

​

nodeId

string

requerido

​

versionId

string

requerido

#### Cuerpo

application/json

​

changelog

string

The changelog describing the version changes.

​

deprecated

boolean

Whether the version is deprecated.

#### Respuesta

200

application/json

Version updated successfully

​

changelog

string

Summary of changes made in this version

​

comfy_node_extract_status

string

The status of comfy node extraction process.

​

createdAt

string<date-time>

The date and time the version was created.

​

dependencies

string[]

A list of pip dependencies required by the node.

​

deprecated

boolean

Indicates if this version is deprecated.

​

downloadUrl

string

[Output Only] URL to download this version of the node

​

id

string

​

node_id

string

The unique identifier of the node.

​

status

enum<string>

Opciones disponibles: 

`NodeVersionStatusActive`, 

`NodeVersionStatusDeleted`, 

`NodeVersionStatusBanned`, 

`NodeVersionStatusPending`, 

`NodeVersionStatusFlagged`

​

status_reason

string

​

supported_accelerators

string[]

List of accelerators (e.g. CUDA, DirectML, ROCm) that this node supports

​

supported_comfyui_frontend_version

string

Supported versions of ComfyUI frontend

​

supported_comfyui_version

string

Supported versions of ComfyUI

​

supported_os

string[]

List of operating systems that this node supports

​

tags

string[]

​

tags_admin

string[]

Admin-only tags for security warnings and admin metadata. Read-only for publishers - omitted from all public responses and ignored if sent on publish; only returned on admin-authenticated responses.

​

version

string

The version identifier, following semantic versioning. Must be unique for the node.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/update-changelog-and-deprecation-status-of-a-node-version.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/update-changelog-and-deprecation-status-of-a-node-version)

[Publish a new version of a node](https://docs.comfy.org/es/registry/api-reference/registry/publish-a-new-version-of-a-node)[Unpublish (delete) a specific version of a node](https://docs.comfy.org/es/registry/api-reference/registry/unpublish-delete-a-specific-version-of-a-node)
