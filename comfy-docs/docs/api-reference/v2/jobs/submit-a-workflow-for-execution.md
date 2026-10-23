---
url: https://docs.comfy.org/api-reference/v2/jobs/submit-a-workflow-for-execution/
title: Submit a workflow for execution - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:25.799541+00:00
---

# Submit a workflow for execution - ComfyUI

> Source: https://docs.comfy.org/api-reference/v2/jobs/submit-a-workflow-for-execution/

Submit a workflow for execution

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/jobs \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "workflow": {},
      "extra_data": {
        "api_key_comfy_org": "<string>",
        "auth_token_comfy_org": "<string>"
      },
      "metadata": {
        "client": "acme",
        "batch": "2026-10-05"
      }
    }
    '
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/jobs"
    
    payload = {
        "workflow": {},
        "extra_data": {
            "api_key_comfy_org": "<string>",
            "auth_token_comfy_org": "<string>"
        },
        "metadata": {
            "client": "acme",
            "batch": "2026-10-05"
        }
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
        workflow: {},
        extra_data: {api_key_comfy_org: '<string>', auth_token_comfy_org: '<string>'},
        metadata: {client: 'acme', batch: '2026-10-05'}
      })
    };
    
    fetch('http://127.0.0.1:8189/api/v2/jobs', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/jobs",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'workflow' => [
            
        ],
        'extra_data' => [
            'api_key_comfy_org' => '<string>',
            'auth_token_comfy_org' => '<string>'
        ],
        'metadata' => [
            'client' => 'acme',
            'batch' => '2026-10-05'
        ]
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
    
    	url := "http://127.0.0.1:8189/api/v2/jobs"
    
    	payload := strings.NewReader("{\n  \"workflow\": {},\n  \"extra_data\": {\n    \"api_key_comfy_org\": \"<string>\",\n    \"auth_token_comfy_org\": \"<string>\"\n  },\n  \"metadata\": {\n    \"client\": \"acme\",\n    \"batch\": \"2026-10-05\"\n  }\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/jobs")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"workflow\": {},\n  \"extra_data\": {\n    \"api_key_comfy_org\": \"<string>\",\n    \"auth_token_comfy_org\": \"<string>\"\n  },\n  \"metadata\": {\n    \"client\": \"acme\",\n    \"batch\": \"2026-10-05\"\n  }\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/jobs")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"workflow\": {},\n  \"extra_data\": {\n    \"api_key_comfy_org\": \"<string>\",\n    \"auth_token_comfy_org\": \"<string>\"\n  },\n  \"metadata\": {\n    \"client\": \"acme\",\n    \"batch\": \"2026-10-05\"\n  }\n}"
    
    response = http.request(request)
    puts response.read_body

201

400

401

402

403

404

422

429

500

503
    
    
    {
      "id": "7f3d2c1b-9a8e-4d6f-b012-3c4d5e6f7a8b",
      "status": "queued",
      "created_at": "2023-11-07T05:31:56Z",
      "started_at": "2023-11-07T05:31:56Z",
      "completed_at": "2023-11-07T05:31:56Z",
      "expires_at": "2023-11-07T05:31:56Z",
      "queue_position": 123,
      "progress": {
        "value": 0.42,
        "nodes_done": 11,
        "nodes_total": 31,
        "current_node": "12",
        "current_node_class": "KSampler",
        "step": 21,
        "steps": 50,
        "message": "KSampler 21/50"
      },
      "outputs": [
        {
          "node_id": "9",
          "name": "ComfyUI_00001_.png",
          "type": "image",
          "content_type": "image/png",
          "size_bytes": 1848320,
          "id": "9f8a1c0d-2b3e-4f56-...",
          "hash": "<string>",
          "url": "<string>",
          "url_expires_at": "2023-11-07T05:31:56Z",
          "job_id": "<string>"
        }
      ],
      "error": {
        "code": "node_execution_error",
        "message": "<string>",
        "node_id": "<string>",
        "class_type": "<string>",
        "traceback": "<string>",
        "node_errors": {
          "22": {
            "class_type": "LoraLoader",
            "errors": [
              {
                "type": "value_not_in_list",
                "message": "Value not in list",
                "details": "lora_name: 'sdxl\\Hyper-SDXL-8steps-lora.safetensors' not in (list of length 40)"
              }
            ]
          }
        }
      },
      "urls": {
        "self": "<string>",
        "events": "<string>",
        "cancel": "<string>",
        "logs": "<string>"
      },
      "metrics": {
        "queue_ms": 9000,
        "execution_ms": 42000
      },
      "deployment_id": "dep-0f19a2b3c4d5",
      "release_id": "7c1e9a40-3b2d-4f6a-9e81-0c5d2a7b4f13",
      "release_version": 3,
      "metadata": {
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

jobs

# Submit a workflow for execution

Copy pageCopy page

Accepts the API-format workflow graph verbatim. Validation is synchronous: graph structure, unknown node classes, and asset references (`core/ASSET` objects — every referenced `id` must exist and be owned by the caller). A `201` means the job is durably recorded and queued.

UI-format workflow JSON (the export with `nodes`/`links`) is rejected with `workflow_format_ui`.

`Idempotency-Key` is single-use (reject-on-duplicate, NOT record-and-replay): the first request to present a given key is processed normally; ANY later request presenting the same key — a retry, a concurrent duplicate, or a same-key request with a different body — is rejected `422` `idempotency_key_reuse` and is never re-executed. The key is claimed only for a request that actually reaches submission and is released if that submission definitively fails without creating a job (a validation error, or an upstream reject such as out-of-credits or queue-full), so a legitimate retry with the same key can proceed. If a submission’s outcome is unknown (an upstream timeout or 5xx where the job may or may not have been created), the key stays claimed and the retry is rejected: poll or list your jobs to find the possibly-created job rather than resubmitting. Keys expire after 24h. There is no response replay and no `Idempotency-Replayed` header.

Reserved for post-MVP and rejected if present today: `webhook_url`, `inputs`.

Copy pageCopy page

POST

http://127.0.0.1:8189https://cloud.comfy.orghttps://{deployment}.run.comfy.app

/

api

/

v2

/

jobs

Try it

Submit a workflow for execution

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/jobs \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "workflow": {},
      "extra_data": {
        "api_key_comfy_org": "<string>",
        "auth_token_comfy_org": "<string>"
      },
      "metadata": {
        "client": "acme",
        "batch": "2026-10-05"
      }
    }
    '
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/jobs"
    
    payload = {
        "workflow": {},
        "extra_data": {
            "api_key_comfy_org": "<string>",
            "auth_token_comfy_org": "<string>"
        },
        "metadata": {
            "client": "acme",
            "batch": "2026-10-05"
        }
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
        workflow: {},
        extra_data: {api_key_comfy_org: '<string>', auth_token_comfy_org: '<string>'},
        metadata: {client: 'acme', batch: '2026-10-05'}
      })
    };
    
    fetch('http://127.0.0.1:8189/api/v2/jobs', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/jobs",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'workflow' => [
            
        ],
        'extra_data' => [
            'api_key_comfy_org' => '<string>',
            'auth_token_comfy_org' => '<string>'
        ],
        'metadata' => [
            'client' => 'acme',
            'batch' => '2026-10-05'
        ]
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
    
    	url := "http://127.0.0.1:8189/api/v2/jobs"
    
    	payload := strings.NewReader("{\n  \"workflow\": {},\n  \"extra_data\": {\n    \"api_key_comfy_org\": \"<string>\",\n    \"auth_token_comfy_org\": \"<string>\"\n  },\n  \"metadata\": {\n    \"client\": \"acme\",\n    \"batch\": \"2026-10-05\"\n  }\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/jobs")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"workflow\": {},\n  \"extra_data\": {\n    \"api_key_comfy_org\": \"<string>\",\n    \"auth_token_comfy_org\": \"<string>\"\n  },\n  \"metadata\": {\n    \"client\": \"acme\",\n    \"batch\": \"2026-10-05\"\n  }\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/jobs")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"workflow\": {},\n  \"extra_data\": {\n    \"api_key_comfy_org\": \"<string>\",\n    \"auth_token_comfy_org\": \"<string>\"\n  },\n  \"metadata\": {\n    \"client\": \"acme\",\n    \"batch\": \"2026-10-05\"\n  }\n}"
    
    response = http.request(request)
    puts response.read_body

201

400

401

402

403

404

422

429

500

503
    
    
    {
      "id": "7f3d2c1b-9a8e-4d6f-b012-3c4d5e6f7a8b",
      "status": "queued",
      "created_at": "2023-11-07T05:31:56Z",
      "started_at": "2023-11-07T05:31:56Z",
      "completed_at": "2023-11-07T05:31:56Z",
      "expires_at": "2023-11-07T05:31:56Z",
      "queue_position": 123,
      "progress": {
        "value": 0.42,
        "nodes_done": 11,
        "nodes_total": 31,
        "current_node": "12",
        "current_node_class": "KSampler",
        "step": 21,
        "steps": 50,
        "message": "KSampler 21/50"
      },
      "outputs": [
        {
          "node_id": "9",
          "name": "ComfyUI_00001_.png",
          "type": "image",
          "content_type": "image/png",
          "size_bytes": 1848320,
          "id": "9f8a1c0d-2b3e-4f56-...",
          "hash": "<string>",
          "url": "<string>",
          "url_expires_at": "2023-11-07T05:31:56Z",
          "job_id": "<string>"
        }
      ],
      "error": {
        "code": "node_execution_error",
        "message": "<string>",
        "node_id": "<string>",
        "class_type": "<string>",
        "traceback": "<string>",
        "node_errors": {
          "22": {
            "class_type": "LoraLoader",
            "errors": [
              {
                "type": "value_not_in_list",
                "message": "Value not in list",
                "details": "lora_name: 'sdxl\\Hyper-SDXL-8steps-lora.safetensors' not in (list of length 40)"
              }
            ]
          }
        }
      },
      "urls": {
        "self": "<string>",
        "events": "<string>",
        "cancel": "<string>",
        "logs": "<string>"
      },
      "metrics": {
        "queue_ms": 9000,
        "execution_ms": 42000
      },
      "deployment_id": "dep-0f19a2b3c4d5",
      "release_id": "7c1e9a40-3b2d-4f6a-9e81-0c5d2a7b4f13",
      "release_version": 3,
      "metadata": {
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

application/json

​

workflow

object

required

API-format workflow graph, verbatim.

​

extra_data

object

Per-prompt ComfyUI `extra_data`, same shape as Comfy Cloud and local ComfyUI. Closed object: only the enumerated keys are accepted, keeping the contract fully typed. Forwarded to the worker per-prompt and excluded from idempotency comparison. On a deployment it is dispatch-only and never stored; on Comfy Cloud it is persisted with the prompt, because the worker needs it, and redacted on every path that returns a workflow to a caller.

Send the one credential you hold: an API key as `api_key_comfy_org`, or the session token an interactively signed-in client has instead as `auth_token_comfy_org`. Sending both is accepted and both are forwarded, but it is not a supported combination and which one a node uses is not defined here. Note a session token is short-lived and is not re-minted for you, so one submitted long before it executes may expire in the queue.

Show child attributes

​

metadata

object

Your own labels for the job, such as which of your customers it ran for. At most 16 pairs. A key is 1 to 40 characters from `A-Z a-z 0-9 _ - .`; a value is a string of at most 256 bytes in UTF-8 (bytes, not characters: 200 `é` is 400 bytes) with no control character (U+0000 to U+001F, tab and newline included, and U+007F to U+009F) and no bidirectional embedding, override or isolate (U+202A to U+202E, U+2066 to U+2069). Anything else is refused `422` `metadata_invalid` and no job is created: a bad key or value is named in the message and in `details.key`, while more than 16 pairs is refused with the count and no `details`. A `metadata` that is not an object is refused `400` `invalid_request`; `null` is the same as none. Stored with the job, returned on it, and filterable on `GET /api/v2/jobs`. Set once, here: nothing changes it later. Only jobs sent to a deployment keep it today: Comfy Cloud refuses a non-empty `metadata` with `422` `metadata_not_supported`, and runs a job with empty or absent `metadata` as before.

Show child attributes

Example:
    
    
    { "client": "acme", "batch": "2026-10-05" }

#### Response

201

application/json

Job created and queued.

One execution of a workflow. Durable from creation until `expires_at`; `outputs` populates incrementally during execution.

​

id

string

required

Example:

`"7f3d2c1b-9a8e-4d6f-b012-3c4d5e6f7a8b"`

​

status

enum<string>

required

Lifecycle: queued → running → succeeded | failed | expired; a cancel request, or the deletion of the deployment the job is running on, moves running → canceling → canceled. Terminal states: succeeded, canceled, failed, expired.

Available options: 

`queued`, 

`running`, 

`succeeded`, 

`canceling`, 

`canceled`, 

`failed`, 

`expired`

​

created_at

string<date-time>

required

​

started_at

string<date-time> | null

required

​

completed_at

string<date-time> | null

required

​

expires_at

string<date-time>

required

Retention deadline — a platform property, not an API constant.

​

queue_position

integer | null

required

​

progress

object | null

required

The latest progress snapshot; same data the SSE stream pushes.

Show child attributes

​

outputs

object[]

required

Show child attributes

​

error

object | null

required

Execution failure detail, carried in `job.error` (not an HTTP error).

Show child attributes

​

urls

object

required

Embedded follow-up links — follow these, don't build URLs. A link is either an absolute URL or a host-relative reference (leading `/`) that already includes any prefix the serving surface is mounted under (e.g. a serverless gateway's `/deployment/{deployment_id}/api/v2`). Clients MUST resolve a host-relative link against the request origin (scheme + authority), never against a configured base URL — joining it to a base URL that carries the same mount prefix duplicates the prefix.

Show child attributes

​

metrics

object

Values are nullable (a metric not yet available — e.g. `execution_ms` before a job starts running — is `null`, not omitted); the example below is deliberately all-non-null purely to work around a Spectral/nimma lint-tooling crash on a literal `null` inside a schema `example` combined with `additionalProperties.nullable: true` — the schema itself is unchanged and still allows null values at runtime.

Show child attributes

Example:
    
    
    { "queue_ms": 9000, "execution_ms": 42000 }

​

deployment_id

string

The deployment the job was sent to: the id in the address it was posted at, which stays the same when the deployment moves to another release. Absent on a surface that runs jobs on no deployment.

Example:

`"dep-0f19a2b3c4d5"`

​

release_id

string

The release of the deployment's build that ran the job, which can differ from the release the deployment runs now. Absent where the serving surface does not report it.

Example:

`"7c1e9a40-3b2d-4f6a-9e81-0c5d2a7b4f13"`

​

release_version

integer

The version of the release in `release_id`, the number its build cut it as. Absent where the serving surface does not report it or could not look it up at the time of the answer.

Required range: `x >= 1`

Example:

`3`

​

metadata

object

The labels the job was submitted with, exactly as sent. Absent when it was sent with none.

Show child attributes

Example:
    
    
    { "client": "acme" }

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/v2/jobs/submit-a-workflow-for-execution.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/v2/jobs/submit-a-workflow-for-execution)

[List jobs, newest firstPrevious](https://docs.comfy.org/api-reference/v2/jobs/list-jobs-newest-first)[Job status (the polling workhorse)Next](https://docs.comfy.org/api-reference/v2/jobs/job-status-the-polling-workhorse)

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
