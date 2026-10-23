---
url: https://docs.comfy.org/registry/api-reference/registry/unpublish-delete-a-specific-version-of-a-node/
title: Unpublish (delete) a specific version of a node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:23.443102+00:00
---

# Unpublish (delete) a specific version of a node - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/unpublish-delete-a-specific-version-of-a-node/

Unpublish (delete) a specific version of a node

cURL
    
    
    curl --request DELETE \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};
    
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

403

404

500
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

Registry API Reference

# Unpublish (delete) a specific version of a node

Copy pageCopy page

Copy pageCopy page

DELETE

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

Try it

Unpublish (delete) a specific version of a node

cURL
    
    
    curl --request DELETE \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};
    
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions/{versionId}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

403

404

500
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }
    
    
    {
      "details": [
        "<string>"
      ],
      "message": "<string>"
    }
    
    
    {
      "error": "<string>",
      "message": "<string>"
    }

#### Authorizations

​

Authorization

string

header

required

Bearer token authentication. Normally a Firebase or Cloud JWT. A 'comfyui-' prefixed API key is also accepted in this header: the prefix classifies the value as an API key and it is validated exactly as if it had been sent in X-API-Key. Accepted on the operations served by the comfyFirebase auth middleware (BE-9720, parity with ingest).

#### Path Parameters

​

publisherId

string

required

​

nodeId

string

required

​

versionId

string

required

#### Response

204

Version unpublished (deleted) successfully

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/unpublish-delete-a-specific-version-of-a-node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/unpublish-delete-a-specific-version-of-a-node)

[Update changelog and deprecation status of a node versionPrevious](https://docs.comfy.org/registry/api-reference/registry/update-changelog-and-deprecation-status-of-a-node-version)[Retrieves a list of nodesNext](https://docs.comfy.org/registry/api-reference/registry/retrieves-a-list-of-nodes)

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
