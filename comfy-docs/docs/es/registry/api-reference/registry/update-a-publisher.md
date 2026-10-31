---
url: https://docs.comfy.org/es/registry/api-reference/registry/update-a-publisher/
title: Update a publisher - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-31T13:26:48.113527+00:00
---

# Update a publisher - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/update-a-publisher/

Update a publisher

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/publishers/{publisherId} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "<string>",
      "logo": "<string>",
      "members": [
        {
          "id": "<string>",
          "role": "<string>",
          "user": {
            "email": "<string>",
            "id": "<string>",
            "name": "<string>"
          }
        }
      ],
      "name": "<string>",
      "source_code_repo": "<string>",
      "support": "<string>",
      "website": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}"
    
    payload = {
        "createdAt": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "id": "<string>",
        "logo": "<string>",
        "members": [
            {
                "id": "<string>",
                "role": "<string>",
                "user": {
                    "email": "<string>",
                    "id": "<string>",
                    "name": "<string>"
                }
            }
        ],
        "name": "<string>",
        "source_code_repo": "<string>",
        "support": "<string>",
        "website": "<string>"
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
      body: JSON.stringify({
        createdAt: '2023-11-07T05:31:56Z',
        description: '<string>',
        id: '<string>',
        logo: '<string>',
        members: [
          {
            id: '<string>',
            role: '<string>',
            user: {email: '<string>', id: '<string>', name: '<string>'}
          }
        ],
        name: '<string>',
        source_code_repo: '<string>',
        support: '<string>',
        website: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'createdAt' => '2023-11-07T05:31:56Z',
        'description' => '<string>',
        'id' => '<string>',
        'logo' => '<string>',
        'members' => [
            [
                    'id' => '<string>',
                    'role' => '<string>',
                    'user' => [
                                    'email' => '<string>',
                                    'id' => '<string>',
                                    'name' => '<string>'
                    ]
            ]
        ],
        'name' => '<string>',
        'source_code_repo' => '<string>',
        'support' => '<string>',
        'website' => '<string>'
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}"
    
    	payload := strings.NewReader("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"<string>\",\n  \"logo\": \"<string>\",\n  \"members\": [\n    {\n      \"id\": \"<string>\",\n      \"role\": \"<string>\",\n      \"user\": {\n        \"email\": \"<string>\",\n        \"id\": \"<string>\",\n        \"name\": \"<string>\"\n      }\n    }\n  ],\n  \"name\": \"<string>\",\n  \"source_code_repo\": \"<string>\",\n  \"support\": \"<string>\",\n  \"website\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/publishers/{publisherId}")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"<string>\",\n  \"logo\": \"<string>\",\n  \"members\": [\n    {\n      \"id\": \"<string>\",\n      \"role\": \"<string>\",\n      \"user\": {\n        \"email\": \"<string>\",\n        \"id\": \"<string>\",\n        \"name\": \"<string>\"\n      }\n    }\n  ],\n  \"name\": \"<string>\",\n  \"source_code_repo\": \"<string>\",\n  \"support\": \"<string>\",\n  \"website\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"<string>\",\n  \"logo\": \"<string>\",\n  \"members\": [\n    {\n      \"id\": \"<string>\",\n      \"role\": \"<string>\",\n      \"user\": {\n        \"email\": \"<string>\",\n        \"id\": \"<string>\",\n        \"name\": \"<string>\"\n      }\n    }\n  ],\n  \"name\": \"<string>\",\n  \"source_code_repo\": \"<string>\",\n  \"support\": \"<string>\",\n  \"website\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

404

500
    
    
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "<string>",
      "logo": "<string>",
      "members": [
        {
          "id": "<string>",
          "role": "<string>",
          "user": {
            "email": "<string>",
            "id": "<string>",
            "name": "<string>"
          }
        }
      ],
      "name": "<string>",
      "source_code_repo": "<string>",
      "status": "PublisherStatusActive",
      "support": "<string>",
      "website": "<string>"
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

# Update a publisher

Copiar páginaCopiar página

Copiar páginaCopiar página

PUT

/

publishers

/

{publisherId}

Pruébalo

Update a publisher

cURL
    
    
    curl --request PUT \
      --url https://api.comfy.org/publishers/{publisherId} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "<string>",
      "logo": "<string>",
      "members": [
        {
          "id": "<string>",
          "role": "<string>",
          "user": {
            "email": "<string>",
            "id": "<string>",
            "name": "<string>"
          }
        }
      ],
      "name": "<string>",
      "source_code_repo": "<string>",
      "support": "<string>",
      "website": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}"
    
    payload = {
        "createdAt": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "id": "<string>",
        "logo": "<string>",
        "members": [
            {
                "id": "<string>",
                "role": "<string>",
                "user": {
                    "email": "<string>",
                    "id": "<string>",
                    "name": "<string>"
                }
            }
        ],
        "name": "<string>",
        "source_code_repo": "<string>",
        "support": "<string>",
        "website": "<string>"
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
      body: JSON.stringify({
        createdAt: '2023-11-07T05:31:56Z',
        description: '<string>',
        id: '<string>',
        logo: '<string>',
        members: [
          {
            id: '<string>',
            role: '<string>',
            user: {email: '<string>', id: '<string>', name: '<string>'}
          }
        ],
        name: '<string>',
        source_code_repo: '<string>',
        support: '<string>',
        website: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "PUT",
      CURLOPT_POSTFIELDS => json_encode([
        'createdAt' => '2023-11-07T05:31:56Z',
        'description' => '<string>',
        'id' => '<string>',
        'logo' => '<string>',
        'members' => [
            [
                    'id' => '<string>',
                    'role' => '<string>',
                    'user' => [
                                    'email' => '<string>',
                                    'id' => '<string>',
                                    'name' => '<string>'
                    ]
            ]
        ],
        'name' => '<string>',
        'source_code_repo' => '<string>',
        'support' => '<string>',
        'website' => '<string>'
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}"
    
    	payload := strings.NewReader("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"<string>\",\n  \"logo\": \"<string>\",\n  \"members\": [\n    {\n      \"id\": \"<string>\",\n      \"role\": \"<string>\",\n      \"user\": {\n        \"email\": \"<string>\",\n        \"id\": \"<string>\",\n        \"name\": \"<string>\"\n      }\n    }\n  ],\n  \"name\": \"<string>\",\n  \"source_code_repo\": \"<string>\",\n  \"support\": \"<string>\",\n  \"website\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.put("https://api.comfy.org/publishers/{publisherId}")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"<string>\",\n  \"logo\": \"<string>\",\n  \"members\": [\n    {\n      \"id\": \"<string>\",\n      \"role\": \"<string>\",\n      \"user\": {\n        \"email\": \"<string>\",\n        \"id\": \"<string>\",\n        \"name\": \"<string>\"\n      }\n    }\n  ],\n  \"name\": \"<string>\",\n  \"source_code_repo\": \"<string>\",\n  \"support\": \"<string>\",\n  \"website\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Put.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"createdAt\": \"2023-11-07T05:31:56Z\",\n  \"description\": \"<string>\",\n  \"id\": \"<string>\",\n  \"logo\": \"<string>\",\n  \"members\": [\n    {\n      \"id\": \"<string>\",\n      \"role\": \"<string>\",\n      \"user\": {\n        \"email\": \"<string>\",\n        \"id\": \"<string>\",\n        \"name\": \"<string>\"\n      }\n    }\n  ],\n  \"name\": \"<string>\",\n  \"source_code_repo\": \"<string>\",\n  \"support\": \"<string>\",\n  \"website\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

200

400

404

500
    
    
    {
      "createdAt": "2023-11-07T05:31:56Z",
      "description": "<string>",
      "id": "<string>",
      "logo": "<string>",
      "members": [
        {
          "id": "<string>",
          "role": "<string>",
          "user": {
            "email": "<string>",
            "id": "<string>",
            "name": "<string>"
          }
        }
      ],
      "name": "<string>",
      "source_code_repo": "<string>",
      "status": "PublisherStatusActive",
      "support": "<string>",
      "website": "<string>"
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

#### Cuerpo

application/json

​

createdAt

string<date-time>

The date and time the publisher was created.

​

description

string

​

id

string

The unique identifier for the publisher. It's akin to a username. Should be lowercase.

​

logo

string

URL to the publisher's logo.

​

members

object[]

A list of members in the publisher.

Show child attributes

​

name

string

​

source_code_repo

string

​

status

enum<string>

Opciones disponibles: 

`PublisherStatusActive`, 

`PublisherStatusBanned`

​

support

string

​

website

string

#### Respuesta

200

application/json

Publisher updated successfully

​

createdAt

string<date-time>

The date and time the publisher was created.

​

description

string

​

id

string

The unique identifier for the publisher. It's akin to a username. Should be lowercase.

​

logo

string

URL to the publisher's logo.

​

members

object[]

A list of members in the publisher.

Show child attributes

​

name

string

​

source_code_repo

string

​

status

enum<string>

Opciones disponibles: 

`PublisherStatusActive`, 

`PublisherStatusBanned`

​

support

string

​

website

string

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/update-a-publisher.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/update-a-publisher)

[Retrieve a publisher by ID](https://docs.comfy.org/es/registry/api-reference/registry/retrieve-a-publisher-by-id)[Delete a publisher](https://docs.comfy.org/es/registry/api-reference/registry/delete-a-publisher)
