---
url: https://docs.comfy.org/api-reference/v2/assets/upload-an-asset-single-call-multipart/
title: Upload an asset (single-call multipart) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:26.493608+00:00
---

# Upload an asset (single-call multipart) - ComfyUI

> Source: https://docs.comfy.org/api-reference/v2/assets/upload-an-asset-single-call-multipart/

Upload an asset (single-call multipart)

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/assets \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form file=@example-file \
      --form content_type=image/png \
      --form file_path=photo.png \
      --form expected_hash=blake3:9f8a1c0d... \
      --form 'tags=<string>' \
      --form expires_in=86400
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets"
    
    files = { "file": ("example-file", open("example-file", "rb")) }
    payload = {
        "content_type": "image/png",
        "file_path": "photo.png",
        "expected_hash": "blake3:9f8a1c0d...",
        "tags": "<string>",
        "expires_in": "86400"
    }
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('file', '<string>');
    form.append('content_type', 'image/png');
    form.append('file_path', 'photo.png');
    form.append('expected_hash', 'blake3:9f8a1c0d...');
    form.append('tags', '<string>');
    form.append('expires_in', '86400');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('http://127.0.0.1:8189/api/v2/assets', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: multipart/form-data"
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
    
    	url := "http://127.0.0.1:8189/api/v2/assets"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/assets")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

201

401

403

409

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

# Upload an asset (single-call multipart)

Copy pageCopy page

Single-call `multipart/form-data` upload. The platform streams the bytes through its trusted byte-path, dedups by the server-computed hash, and mints the asset record.

The blake3 hash is always computed server-side from the received bytes — a client-declared `expected_hash` is verified, never trusted. The uploaded asset is referenceable immediately; any content scanning runs in the background and does not block the response.

~100 MB single-request expectation for v1; chunked/resumable large uploads are a deliberate open question.

On Comfy Cloud an upload fails with 422 `upload_timed_out` when no request bytes arrive for 30 seconds, or when the whole request takes longer than 10 minutes, however steadily bytes keep arriving.

Copy pageCopy page

POST

http://127.0.0.1:8189https://cloud.comfy.orghttps://{deployment}.run.comfy.app

/

api

/

v2

/

assets

Try it

Upload an asset (single-call multipart)

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/assets \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form file=@example-file \
      --form content_type=image/png \
      --form file_path=photo.png \
      --form expected_hash=blake3:9f8a1c0d... \
      --form 'tags=<string>' \
      --form expires_in=86400
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets"
    
    files = { "file": ("example-file", open("example-file", "rb")) }
    payload = {
        "content_type": "image/png",
        "file_path": "photo.png",
        "expected_hash": "blake3:9f8a1c0d...",
        "tags": "<string>",
        "expires_in": "86400"
    }
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('file', '<string>');
    form.append('content_type', 'image/png');
    form.append('file_path', 'photo.png');
    form.append('expected_hash', 'blake3:9f8a1c0d...');
    form.append('tags', '<string>');
    form.append('expires_in', '86400');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('http://127.0.0.1:8189/api/v2/assets', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: multipart/form-data"
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
    
    	url := "http://127.0.0.1:8189/api/v2/assets"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/assets")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

201

401

403

409

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

#### Authorizations

​

Authorization

string

header

required

`Authorization: Bearer <credential>`. The credential is one of: an account-scoped API key (`comfyui-…`), accepted on Cloud and serverless; a Comfy Cloud session JWT; or an OAuth access token issued for the Comfy Cloud resource. Which kinds a given deployment accepts is deployment configuration — an API key always works on Cloud and serverless, and a deployment that does not accept JWT bearers answers `401` with a message saying so. Self-hosted accepts unauthenticated requests by default and can be configured with a static bearer token.

#### Headers

​

Idempotency-Key

string

Client-generated UUID (recommended). Single-use: the first request to present a key is processed; any later request with the same key is rejected `422` `idempotency_key_reuse` (reject-on-duplicate, no response replay). Keys expire after 24h.

#### Body

multipart/form-data

​

file

file

required

The raw bytes.

​

content_type

string

required

Example:

`"image/png"`

​

file_path

string

required

Placement path / filename (global-namespace-root form, e.g. `photo.png` or `models/checkpoints/x.safetensors`).

Example:

`"photo.png"`

​

expected_hash

string

Optional client-computed blake3 (`blake3:<hex>`). Verified against the server-computed hash; mismatch is rejected with 409 `hash_mismatch` and no asset is minted.

Example:

`"blake3:9f8a1c0d..."`

​

tags

string[]

Category tags (e.g. `input`).

​

expires_in

integer

Optional retention override in seconds (60s–7d): the asset's `expires_at` becomes now + `expires_in`, replacing the platform's default retention. Implementations without configurable retention ignore it. The bounds apply to this override only — the platform default is operator-configured and may lie outside them.

Required range: `60 <= x <= 604800`

Example:

`86400`

#### Response

200

application/json

Bytes deduped to an existing blob; asset minted over it.

A user-owned record identified by a server-assigned UUID, backing an immutable blob whose content carries a server-computed blake3 hash. `hash` may be computed lazily: an asset record (and its retrievable bytes) can exist before its hash is filled in. On an output, `job_metadata` carries the labels its producing job was submitted with, so code holding only the asset knows which run it came from. It is absent for assets no job produced, for outputs of a job sent without labels, where the serving surface keeps no job labels, and when the labels could not be read: so `job_id` without `job_metadata` does not prove the job had no labels. A create whose file path and bytes match an existing output answers with that output, so its `job_id` and `job_metadata` are the output's.

​

id

string

required

Example:

`"9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b"`

​

hash

string | null

required

`blake3:<hex>`; null while lazily computed.

Example:

`"blake3:9f8a1c0d..."`

​

size_bytes

integer<int64>

required

Example:

`4816293`

​

content_type

string

required

Example:

`"image/png"`

​

created_at

string<date-time>

required

​

url

string<uri>

required

Short-lived content URL (signed, or proxy-served).

​

url_expires_at

string<date-time>

required

​

file_path

string | null

Example:

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

Example:
    
    
    { "client": "acme" }
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/v2/assets/upload-an-asset-single-call-multipart.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/v2/assets/upload-an-asset-single-call-multipart)

[Design NotesPrevious](https://docs.comfy.org/development/api-development/sdks-design)[Mint an asset over existing bytes (dedup fast-path)Next](https://docs.comfy.org/api-reference/v2/assets/mint-an-asset-over-existing-bytes-dedup-fast-path)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
