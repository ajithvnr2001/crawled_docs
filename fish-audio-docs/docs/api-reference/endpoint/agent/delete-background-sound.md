---
url: https://docs.fish.audio/api-reference/endpoint/agent/delete-background-sound/
title: Delete Background Sound - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:42:08.418232+00:00
---

# Delete Background Sound - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/agent/delete-background-sound/

Delete Background Sound

cURL
    
    
    curl --request DELETE \
      --url https://api.fish.audio/v1/agent/background-sounds/{asset_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/background-sounds/{asset_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/agent/background-sounds/{asset_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/background-sounds/{asset_id}",
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
    
    	url := "https://api.fish.audio/v1/agent/background-sounds/{asset_id}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://api.fish.audio/v1/agent/background-sounds/{asset_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/background-sounds/{asset_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

401

404

503
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }

Background Sounds

# Delete Background Sound

Copy pageCopy page

Delete an uploaded background sound clip. An agent that still has it selected plays no background sound from its next session on.

Copy pageCopy page

DELETE

/

v1

/

agent

/

background-sounds

/

{asset_id}

Try it

Delete Background Sound

cURL
    
    
    curl --request DELETE \
      --url https://api.fish.audio/v1/agent/background-sounds/{asset_id} \
      --header 'Authorization: Bearer <token>'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/background-sounds/{asset_id}"
    
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.delete(url, headers=headers)
    
    print(response.text)
    
    
    const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};
    
    fetch('https://api.fish.audio/v1/agent/background-sounds/{asset_id}', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/background-sounds/{asset_id}",
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
    
    	url := "https://api.fish.audio/v1/agent/background-sounds/{asset_id}"
    
    	req, _ := http.NewRequest("DELETE", url, nil)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.delete("https://api.fish.audio/v1/agent/background-sounds/{asset_id}")
      .header("Authorization", "Bearer <token>")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/background-sounds/{asset_id}")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Delete.new(url)
    request["Authorization"] = 'Bearer <token>'
    
    response = http.request(request)
    puts response.read_body

401

404

503
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }

#### Authorizations

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

asset_id

string

required

#### Response

204

Request fulfilled, nothing follows

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/agent/delete-background-sound.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/agent/delete-background-sound)

[Create Background Sound](https://docs.fish.audio/api-reference/endpoint/agent/create-background-sound)[Search Available Phone Numbers](https://docs.fish.audio/api-reference/endpoint/agent/search-available-phone-numbers)
