---
url: https://docs.comfy.org/es/api-reference/v2/jobs/job-status-the-polling-workhorse/
title: Job status (the polling workhorse) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-28T13:54:35.158121+00:00
---

# Job status (the polling workhorse) - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/v2/jobs/job-status-the-polling-workhorse/

Job status (the polling workhorse)

cURL
    
    
    curl --request GET \
      --url http://127.0.0.1:8189/api/v2/jobs/{id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/jobs/{id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('http://127.0.0.1:8189/api/v2/jobs/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/jobs/{id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "http://127.0.0.1:8189/api/v2/jobs/{id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("http://127.0.0.1:8189/api/v2/jobs/{id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/jobs/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

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

jobs

# Job status (the polling workhorse)

Copiar páginaCopiar página

Returns the full job object: current status, the latest progress snapshot, and every output committed so far (`outputs` populates incrementally while the job runs). This is the authoritative, resumable view of a job; everything on the SSE stream is derived from it.

Copiar páginaCopiar página

GET

http://127.0.0.1:8189https://cloud.comfy.orghttps://{deployment}.run.comfy.app

/

api

/

v2

/

jobs

/

{id}

Pruébalo

Job status (the polling workhorse)

cURL
    
    
    curl --request GET \
      --url http://127.0.0.1:8189/api/v2/jobs/{id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/jobs/{id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('http://127.0.0.1:8189/api/v2/jobs/{id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/jobs/{id}",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "GET",
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
    
    	url := "http://127.0.0.1:8189/api/v2/jobs/{id}"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("http://127.0.0.1:8189/api/v2/jobs/{id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/jobs/{id}")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

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

#### Autorizaciones

​

Authorization

string

header

requerido

`Authorization: Bearer <credential>`. The credential is one of: an account-scoped API key (`comfyui-…`), accepted on Cloud and serverless; a Comfy Cloud session JWT; or an OAuth access token issued for the Comfy Cloud resource. Which kinds a given deployment accepts is deployment configuration — an API key always works on Cloud and serverless, and a deployment that does not accept JWT bearers answers `401` with a message saying so. Self-hosted accepts unauthenticated requests by default and can be configured with a static bearer token.

#### Parámetros de ruta

​

id

string

requerido

#### Respuesta

200

application/json

The job.

One execution of a workflow. Durable from creation until `expires_at`; `outputs` populates incrementally during execution.

​

id

string

requerido

Ejemplo:

`"7f3d2c1b-9a8e-4d6f-b012-3c4d5e6f7a8b"`

​

status

enum<string>

requerido

Lifecycle: queued → running → succeeded | failed | expired; a cancel request, or the deletion of the deployment the job is running on, moves running → canceling → canceled. Terminal states: succeeded, canceled, failed, expired.

Opciones disponibles: 

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

requerido

​

started_at

string<date-time> | null

requerido

​

completed_at

string<date-time> | null

requerido

​

expires_at

string<date-time>

requerido

Retention deadline — a platform property, not an API constant.

​

queue_position

integer | null

requerido

​

progress

object | null

requerido

The latest progress snapshot; same data the SSE stream pushes.

Show child attributes

​

outputs

object[]

requerido

Show child attributes

​

error

object | null

requerido

Execution failure detail, carried in `job.error` (not an HTTP error).

Show child attributes

​

urls

object

requerido

Embedded follow-up links — follow these, don't build URLs. A link is either an absolute URL or a host-relative reference (leading `/`) that already includes any prefix the serving surface is mounted under (e.g. a serverless gateway's `/deployment/{deployment_id}/api/v2`). Clients MUST resolve a host-relative link against the request origin (scheme + authority), never against a configured base URL — joining it to a base URL that carries the same mount prefix duplicates the prefix.

Show child attributes

​

metrics

object

Values are nullable (a metric not yet available — e.g. `execution_ms` before a job starts running — is `null`, not omitted); the example below is deliberately all-non-null purely to work around a Spectral/nimma lint-tooling crash on a literal `null` inside a schema `example` combined with `additionalProperties.nullable: true` — the schema itself is unchanged and still allows null values at runtime.

Show child attributes

Ejemplo:
    
    
    { "queue_ms": 9000, "execution_ms": 42000 }

​

deployment_id

string

The deployment the job was sent to: the id in the address it was posted at, which stays the same when the deployment moves to another release. Absent on a surface that runs jobs on no deployment.

Ejemplo:

`"dep-0f19a2b3c4d5"`

​

release_id

string

The release of the deployment's build that ran the job, which can differ from the release the deployment runs now. Absent where the serving surface does not report it.

Ejemplo:

`"7c1e9a40-3b2d-4f6a-9e81-0c5d2a7b4f13"`

​

release_version

integer

The version of the release in `release_id`, the number its build cut it as. Absent where the serving surface does not report it or could not look it up at the time of the answer.

Rango requerido: `x >= 1`

Ejemplo:

`3`

​

metadata

object

The labels the job was submitted with, exactly as sent. Absent when it was sent with none.

Show child attributes

Ejemplo:
    
    
    { "client": "acme" }

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/v2/jobs/job-status-the-polling-workhorse.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/v2/jobs/job-status-the-polling-workhorse)

[Submit a workflow for execution](https://docs.comfy.org/es/api-reference/v2/jobs/submit-a-workflow-for-execution)[The workflow behind a job — authoring version if pinned, executed graph otherwise](https://docs.comfy.org/es/api-reference/v2/jobs/the-workflow-behind-a-job-%E2%80%94-authoring-version-if-pinned-executed-graph-otherwise)
