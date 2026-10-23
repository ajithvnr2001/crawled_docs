---
url: https://docs.comfy.org/api-reference/router/comfy-router/read-the-queue-state-of-one-submitted-request/
title: Read the queue state of one submitted request. - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:11.712681+00:00
---

# Read the queue state of one submitted request. - ComfyUI

> Source: https://docs.comfy.org/api-reference/router/comfy-router/read-the-queue-state-of-one-submitted-request/

Read the queue state of one submitted request.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

410

503

default
    
    
    {
      "status_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status",
      "response_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "cancel_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel",
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "IN_QUEUE",
      "queue_position": 3,
      "error_type": "invalid_input"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }

Comfy Router

# Read the queue state of one submitted request.

Copy pageCopy page

The poll endpoint. It answers with the request’s current state and never with the result, so a client can watch a long generation without transferring its output on every poll - the result is collected once, from the read below, when this says `COMPLETED`.

Copy pageCopy page

GET

/

v2

/

models

/

{provider}

/

{model}

/

requests

/

{request_id}

/

status

Try it

Read the queue state of one submitted request.

cURL
    
    
    curl --request GET \
      --url https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.get(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status",
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
    
    	url := "https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.get("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/v2/models/{provider}/{model}/requests/{request_id}/status")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Get.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

200

401

403

404

410

503

default
    
    
    {
      "status_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status",
      "response_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "cancel_url": "https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel",
      "request_id": "6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21",
      "status": "IN_QUEUE",
      "queue_position": 3,
      "error_type": "invalid_input"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }
    
    
    {
      "detail": "<string>",
      "error_type": "invalid_input",
      "upstream_detail": "<string>",
      "refusal_subject": "<string>"
    }

#### Authorizations

BearerAuthApiKeyAuthBearerAuthApiKeyAuth

​

Authorization

string

header

required

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key.

#### Path Parameters

​

provider

string

required

Lowercase provider segment of the canonical `{provider}/{model}` model ID - the partner whose model is being run. Lowercase `provider` segment of the canonical `{provider}/{model}` model ID - the partner whose model is being addressed. The invocation route's `provider` path parameter and a catalog entry's `provider` field both reference this one schema, which is what keeps the listed IDs and the accepted IDs from drifting apart.

Maximum string length: `64`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"bfl"`

​

model

string

required

Lowercase model segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Lowercase `model` segment of the canonical `{provider}/{model}` model ID - the model to run within that provider. Shared by the invocation route's `model` path parameter and a catalog entry's `model` field, for the same no-drift reason as `RouterProviderSegment`.

Maximum string length: `128`

Pattern: `^[a-z0-9]+([._-][a-z0-9]+)*$`

Example:

`"flux-2-pro"`

​

request_id

string<uuid>

required

The queued request to address - the `request_id` the submission returned in its body. It is not the submission's `X-Comfy-Request-Id`: that header carries the id of one HTTP call and addresses nothing, as the `RouterQueueRequestId` schema spells out. Identifier of one queued Router request - the handle a caller polls, cancels and collects a result by.

Maximum string length: `36`

Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

Example:

`"6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

#### Response

200

application/json

OK - the request's current queue state. `status` is one of the three states; `queue_position` is present while the request is still `IN_QUEUE`; `error_type` is present only on a `COMPLETED` request that failed or was cancelled.

One queued request's current state, composed with the same three URLs the submission returned.

​

status_url

string<uri>

required

Absolute URL of this request's status read.

Example:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/status"`

​

response_url

string<uri>

required

Absolute URL this request's result is collected from.

Example:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

​

cancel_url

string<uri>

required

Absolute URL a cancellation is asked for at.

Example:

`"https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21/cancel"`

​

request_id

string<uuid>

required

Identifier of one queued Router request - the handle a caller polls, cancels and collects a result by.

Maximum string length: `36`

Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

Example:

`"6f1a1a6e-6a53-4a5f-9d3a-2b3b0a1f9c21"`

​

status

enum<string>

required

The state of a queued Router request. It has exactly three values, and unlike `RouterErrorType` this one is a closed `enum`, because the two schemas are closed in opposite directions on purpose. `RouterErrorType` classifies failures and its set is expected to grow, so a generated client that hard-rejected an unrecognised bucket would fail hardest exactly when something had already gone wrong. This one is a lifecycle, and a lifecycle with a fourth state added later is a breaking change to every polling loop written against it whether it is declared as an enum or not - so it is declared as one, and the constraint is stated where a client can see it.

Available options: 

`IN_QUEUE`, 

`IN_PROGRESS`, 

`COMPLETED`

Example:

`"IN_QUEUE"`

​

queue_position

integer

How many requests are ahead of this one in the queue, at the instant the response was composed. Zero means this request is at the front.

Required range: `x >= 0`

Example:

`3`

​

error_type

string

Present only on a `COMPLETED` request that did not succeed, carrying the same coarse bucket the result read puts on `X-Comfy-Error-Type` when it returns that failure. It is what distinguishes a terminal request that succeeded from one that failed or was cancelled - there is no separate terminal status for either - and it is absent on success rather than null, so branch on its presence.

Example:

`"invalid_input"`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/api-reference/router/comfy-router/read-the-queue-state-of-one-submitted-request.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/router/comfy-router/read-the-queue-state-of-one-submitted-request)

[Ask for one submitted request to be cancelled.Previous](https://docs.comfy.org/api-reference/router/comfy-router/ask-for-one-submitted-request-to-be-cancelled)[Comfy Router modelsNext](https://docs.comfy.org/development/comfy-router/models)

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
