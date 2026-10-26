---
url: https://docs.comfy.org/es/api-reference/v2/assets/mint-an-asset-over-existing-bytes-dedup-fast-path/
title: Mint an asset over existing bytes (dedup fast-path) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:28.817567+00:00
---

# Mint an asset over existing bytes (dedup fast-path) - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/v2/assets/mint-an-asset-over-existing-bytes-dedup-fast-path/

Mint an asset over existing bytes (dedup fast-path)

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/assets/from-hash \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "hash": "blake3:9f8a1c0d...",
      "file_path": "photo.png",
      "tags": [
        "<string>"
      ],
      "expires_in": 86400
    }
    '
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets/from-hash"
    
    payload = {
        "hash": "blake3:9f8a1c0d...",
        "file_path": "photo.png",
        "tags": ["<string>"],
        "expires_in": 86400
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        hash: 'blake3:9f8a1c0d...',
        file_path: 'photo.png',
        tags: ['<string>'],
        expires_in: 86400
      })
    };
    
    fetch('http://127.0.0.1:8189/api/v2/assets/from-hash', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets/from-hash",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'hash' => 'blake3:9f8a1c0d...',
        'file_path' => 'photo.png',
        'tags' => [
            '<string>'
        ],
        'expires_in' => 86400
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
    
    	url := "http://127.0.0.1:8189/api/v2/assets/from-hash"
    
    	payload := strings.NewReader("{\n  \"hash\": \"blake3:9f8a1c0d...\",\n  \"file_path\": \"photo.png\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"expires_in\": 86400\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/assets/from-hash")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"hash\": \"blake3:9f8a1c0d...\",\n  \"file_path\": \"photo.png\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"expires_in\": 86400\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets/from-hash")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"hash\": \"blake3:9f8a1c0d...\",\n  \"file_path\": \"photo.png\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"expires_in\": 86400\n}"
    
    response = http.request(request)
    puts response.read_body

200

201

401

403

404

422

429

500

503
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }

assets

# Mint an asset over existing bytes (dedup fast-path)

Copiar páginaCopiar página

Zero-byte fast-path: mints a new asset UUID over a blob the platform already has, identified by its blake3 hash.

Trust boundary: resolves only against blobs the platform itself ingested and hashed, and only those the calling account is authorized to use — the client hash is a lookup key, never an authority to register new content. A miss and “exists but not yours” are deliberately indistinguishable (`404` `blob_not_found`).

The lookup key is the `hash` an upload returned, which is the hash of the stored bytes. When location metadata was removed from an image before it was stored, that differs from the client’s digest of the file it sent, and the client’s digest finds nothing.

Copiar páginaCopiar página

POST

http://127.0.0.1:8189https://cloud.comfy.orghttps://{deployment}.run.comfy.app

/

api

/

v2

/

assets

/

from-hash

Pruébalo

Mint an asset over existing bytes (dedup fast-path)

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/assets/from-hash \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "hash": "blake3:9f8a1c0d...",
      "file_path": "photo.png",
      "tags": [
        "<string>"
      ],
      "expires_in": 86400
    }
    '
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets/from-hash"
    
    payload = {
        "hash": "blake3:9f8a1c0d...",
        "file_path": "photo.png",
        "tags": ["<string>"],
        "expires_in": 86400
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.text)
    
    
    const options = {
      method: 'POST',
      headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
      body: JSON.stringify({
        hash: 'blake3:9f8a1c0d...',
        file_path: 'photo.png',
        tags: ['<string>'],
        expires_in: 86400
      })
    };
    
    fetch('http://127.0.0.1:8189/api/v2/assets/from-hash', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets/from-hash",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'hash' => 'blake3:9f8a1c0d...',
        'file_path' => 'photo.png',
        'tags' => [
            '<string>'
        ],
        'expires_in' => 86400
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
    
    	url := "http://127.0.0.1:8189/api/v2/assets/from-hash"
    
    	payload := strings.NewReader("{\n  \"hash\": \"blake3:9f8a1c0d...\",\n  \"file_path\": \"photo.png\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"expires_in\": 86400\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/assets/from-hash")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"hash\": \"blake3:9f8a1c0d...\",\n  \"file_path\": \"photo.png\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"expires_in\": 86400\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets/from-hash")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"hash\": \"blake3:9f8a1c0d...\",\n  \"file_path\": \"photo.png\",\n  \"tags\": [\n    \"<string>\"\n  ],\n  \"expires_in\": 86400\n}"
    
    response = http.request(request)
    puts response.read_body

200

201

401

403

404

422

429

500

503
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }

#### Autorizaciones

​

Authorization

string

header

requerido

`Authorization: Bearer <credential>`. The credential is one of: an account-scoped API key (`comfyui-…`), accepted on Cloud and serverless; a Comfy Cloud session JWT; or an OAuth access token issued for the Comfy Cloud resource. Which kinds a given deployment accepts is deployment configuration — an API key always works on Cloud and serverless, and a deployment that does not accept JWT bearers answers `401` with a message saying so. Self-hosted accepts unauthenticated requests by default and can be configured with a static bearer token.

#### Cuerpo

application/json

​

hash

string

requerido

Ejemplo:

`"blake3:9f8a1c0d..."`

​

file_path

string

Placement path / filename; its last segment becomes the asset name. On Comfy Cloud a `file_path` that fails path validation, or whose last segment breaks the `file_path` rules of `POST /api/v2/assets`, is answered with 404 `blob_not_found`, the same as an unknown hash. The UTF-8 rule cannot fire here: invalid UTF-8 bytes and lone surrogate escapes (`\ud800`) are replaced with U+FFFD when the JSON body is decoded, so such a name is stored with U+FFFD in their place.

Ejemplo:

`"photo.png"`

​

tags

string[]

A create carries at most 64 tags, each a non-empty UTF-8 string of at most 256 bytes (surrounding whitespace included) with no NUL byte. A deployment adds `input` to every asset and counts it, so it takes at most 63 of the caller's own; the `model_type:` tags derived for a model asset are not counted. A tag set breaking a limit is refused with 422. Invalid UTF-8 or a lone surrogate escape (e.g. `\ud800`) inside a JSON-encoded tag is not refused: JSON decoding replaces it with U+FFFD (3 bytes each), and the 256-byte limit applies to the replaced value.

​

expires_in

integer

Optional retention override in seconds (60s–7d): the asset's `expires_at` becomes now + `expires_in`, replacing the platform's default retention. Implementations without configurable retention ignore it. The bounds apply to this override only — the platform default is operator-configured and may lie outside them.

Rango requerido: `60 <= x <= 604800`

Ejemplo:

`86400`

#### Respuesta

200

application/json

An identical reference already existed; returned as-is.

A user-owned record identified by a server-assigned UUID, backing an immutable blob whose content carries a server-computed blake3 hash. `hash` may be computed lazily: an asset record (and its retrievable bytes) can exist before its hash is filled in. On an output, `job_metadata` carries the labels its producing job was submitted with, so code holding only the asset knows which run it came from. It is absent for assets no job produced, for outputs of a job sent without labels, where the serving surface keeps no job labels, and when the labels could not be read: so `job_id` without `job_metadata` does not prove the job had no labels. A create whose file path and bytes match an existing output answers with that output, so its `job_id` and `job_metadata` are the output's.

​

id

string

requerido

Ejemplo:

`"9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b"`

​

hash

string | null

requerido

`blake3:<hex>`; null while lazily computed.

Ejemplo:

`"blake3:9f8a1c0d..."`

​

size_bytes

integer<int64>

requerido

Ejemplo:

`4816293`

​

content_type

string

requerido

Ejemplo:

`"image/png"`

​

created_at

string<date-time>

requerido

​

url

string<uri>

requerido

Short-lived content URL (signed, or proxy-served).

​

url_expires_at

string<date-time>

requerido

​

file_path

string | null

Ejemplo:

`"photo.png"`

​

created_new

boolean

On create responses: distinguishes a brand-new blob (true) from a dedup hit against bytes the platform already had (false).

​

expires_at

string<date-time> | null

Retention deadline for the asset itself (distinct from `url_expires_at`, the signed URL's validity). Null or absent means the asset is non-expiring. On a dedup-hit create response the deadline may be later than now + the requested/default retention: re-referencing content extends its retention, never shortens it.

​

job_id

string | null

ID of the job that produced this asset. Absent for assets no job produced, such as a fresh upload.

​

job_metadata

object

The labels the producing job was submitted with, read through `job_id` on each read. Absent for assets no job produced, for outputs of a job sent without labels, where the serving surface keeps no job labels, when the job is gone, and when the labels could not be read: so `job_id` without `job_metadata` does not prove the job had no labels.

Show child attributes

Ejemplo:
    
    
    { "client": "acme" }

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/v2/assets/mint-an-asset-over-existing-bytes-dedup-fast-path.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/v2/assets/mint-an-asset-over-existing-bytes-dedup-fast-path)

[Upload an asset (single-call multipart)](https://docs.comfy.org/es/api-reference/v2/assets/upload-an-asset-single-call-multipart)[Existence check for a blob by blake3 hash](https://docs.comfy.org/es/api-reference/v2/assets/existence-check-for-a-blob-by-blake3-hash)
