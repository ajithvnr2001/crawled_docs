---
url: https://docs.comfy.org/api-reference/v2/jobs/request-cancellation/
title: Request cancellation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:25.403988+00:00
---

# Request cancellation - ComfyUI

> Source: https://docs.comfy.org/api-reference/v2/jobs/request-cancellation/

Request cancellation

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/jobs/{id}/cancel \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/jobs/{id}/cancel"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('http://127.0.0.1:8189/api/v2/jobs/{id}/cancel', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/jobs/{id}/cancel",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
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
    
    	url := "http://127.0.0.1:8189/api/v2/jobs/{id}/cancel"
    
    	req, _ := http.NewRequest("POST", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/jobs/{id}/cancel")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/jobs/{id}/cancel")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
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

# Request cancellation

Copy pageCopy page

Requests cancellation and returns the current job object — `canceling` (interruption takes effect at node/step boundaries), `canceled` where the provider’s record already shows the interrupt, or already-terminal. Idempotent: canceling a finished job is a no-op returning the terminal state. On serverless, GPU seconds consumed before the interrupt takes effect are still billed.

Copy pageCopy page

POST

http://127.0.0.1:8189https://cloud.comfy.orghttps://{deployment}.run.comfy.app

/

api

/

v2

/

jobs

/

{id}

/

cancel

Try it

Request cancellation

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/jobs/{id}/cancel \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/jobs/{id}/cancel"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('http://127.0.0.1:8189/api/v2/jobs/{id}/cancel', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/jobs/{id}/cancel",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
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
    
    	url := "http://127.0.0.1:8189/api/v2/jobs/{id}/cancel"
    
    	req, _ := http.NewRequest("POST", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/jobs/{id}/cancel")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/jobs/{id}/cancel")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
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

200

application/json

Current job state.

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/v2/jobs/request-cancellation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/v2/jobs/request-cancellation)

[Live event stream (SSE)Previous](https://docs.comfy.org/api-reference/v2/jobs/live-event-stream-sse)[v1 Cloud API OverviewNext](https://docs.comfy.org/development/cloud/overview)

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
