---
url: https://docs.comfy.org/api-reference/v2/assets/delete-an-asset-record/
title: Delete an asset record - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:08.168362+00:00
---

# Delete an asset record - ComfyUI

> Source: https://docs.comfy.org/api-reference/v2/assets/delete-an-asset-record/

Delete an asset record

cURL
    
    
    curl --request DELETE \
      --url http://127.0.0.1:8189/api/v2/assets/{id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets/{id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('http://127.0.0.1:8189/api/v2/assets/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets/{id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "DELETE",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "http://127.0.0.1:8189/api/v2/assets/{id}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("http://127.0.0.1:8189/api/v2/assets/{id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Delete.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

401

403

404

409

429

500

503
    
    
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

# Delete an asset record

Copy pageCopy page

Deletes the asset RECORD. The underlying content-addressed blob is untouched while any other asset still references it (hash dedup means blobs are shared) — deleting an asset never destroys another asset’s bytes.

A second delete of the same id returns `404`, indistinguishable from an id that never existed or belongs to another account.

Copy pageCopy page

DELETE

http://127.0.0.1:8189https://cloud.comfy.orghttps://{deployment}.run.comfy.app

/

api

/

v2

/

assets

/

{id}

Try it

Delete an asset record

cURL
    
    
    curl --request DELETE \
      --url http://127.0.0.1:8189/api/v2/assets/{id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets/{id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('http://127.0.0.1:8189/api/v2/assets/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets/{id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "DELETE",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>"
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
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "http://127.0.0.1:8189/api/v2/assets/{id}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("http://127.0.0.1:8189/api/v2/assets/{id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Delete.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

401

403

404

409

429

500

503
    
    
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

#### Path Parameters

​

id

string

required

#### Response

204

Record deleted.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/v2/assets/delete-an-asset-record.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/v2/assets/delete-an-asset-record)

[Asset metadata](https://docs.comfy.org/api-reference/v2/assets/asset-metadata)[Asset bytes](https://docs.comfy.org/api-reference/v2/assets/asset-bytes)
