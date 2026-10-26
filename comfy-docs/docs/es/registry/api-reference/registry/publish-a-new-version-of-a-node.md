---
url: https://docs.comfy.org/es/registry/api-reference/registry/publish-a-new-version-of-a-node/
title: Publish a new version of a node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:36.147609+00:00
---

# Publish a new version of a node - ComfyUI

> Source: https://docs.comfy.org/es/registry/api-reference/registry/publish-a-new-version-of-a-node/

Publish a new version of a node

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "node": {
        "author": "<string>",
        "banner_url": "<string>",
        "category": "<string>",
        "created_at": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "downloads": 123,
        "github_stars": 123,
        "icon": "<string>",
        "id": "<string>",
        "latest_version": {
          "changelog": "<string>",
          "comfy_node_extract_status": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "dependencies": [
            "<string>"
          ],
          "deprecated": true,
          "downloadUrl": "<string>",
          "id": "<string>",
          "node_id": "<string>",
          "status_reason": "<string>",
          "supported_accelerators": [
            "<string>"
          ],
          "supported_comfyui_frontend_version": "<string>",
          "supported_comfyui_version": "<string>",
          "supported_os": [
            "<string>"
          ],
          "tags": [
            "<string>"
          ],
          "tags_admin": [
            "<string>"
          ],
          "version": "<string>"
        },
        "license": "<string>",
        "name": "<string>",
        "preempted_comfy_node_names": [
          "<string>"
        ],
        "publisher": {
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
        },
        "rating": 123,
        "repository": "<string>",
        "search_ranking": 123,
        "status_detail": "<string>",
        "supported_accelerators": [
          "<string>"
        ],
        "supported_comfyui_frontend_version": "<string>",
        "supported_comfyui_version": "<string>",
        "supported_os": [
          "<string>"
        ],
        "tags": [
          "<string>"
        ],
        "tags_admin": [
          "<string>"
        ],
        "translations": {}
      },
      "node_version": {
        "changelog": "<string>",
        "comfy_node_extract_status": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "dependencies": [
          "<string>"
        ],
        "deprecated": true,
        "downloadUrl": "<string>",
        "id": "<string>",
        "node_id": "<string>",
        "status_reason": "<string>",
        "supported_accelerators": [
          "<string>"
        ],
        "supported_comfyui_frontend_version": "<string>",
        "supported_comfyui_version": "<string>",
        "supported_os": [
          "<string>"
        ],
        "tags": [
          "<string>"
        ],
        "tags_admin": [
          "<string>"
        ],
        "version": "<string>"
      },
      "personal_access_token": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions"
    
    payload = {
        "node": {
            "author": "<string>",
            "banner_url": "<string>",
            "category": "<string>",
            "created_at": "2023-11-07T05:31:56Z",
            "description": "<string>",
            "downloads": 123,
            "github_stars": 123,
            "icon": "<string>",
            "id": "<string>",
            "latest_version": {
                "changelog": "<string>",
                "comfy_node_extract_status": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "dependencies": ["<string>"],
                "deprecated": True,
                "downloadUrl": "<string>",
                "id": "<string>",
                "node_id": "<string>",
                "status_reason": "<string>",
                "supported_accelerators": ["<string>"],
                "supported_comfyui_frontend_version": "<string>",
                "supported_comfyui_version": "<string>",
                "supported_os": ["<string>"],
                "tags": ["<string>"],
                "tags_admin": ["<string>"],
                "version": "<string>"
            },
            "license": "<string>",
            "name": "<string>",
            "preempted_comfy_node_names": ["<string>"],
            "publisher": {
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
            },
            "rating": 123,
            "repository": "<string>",
            "search_ranking": 123,
            "status_detail": "<string>",
            "supported_accelerators": ["<string>"],
            "supported_comfyui_frontend_version": "<string>",
            "supported_comfyui_version": "<string>",
            "supported_os": ["<string>"],
            "tags": ["<string>"],
            "tags_admin": ["<string>"],
            "translations": {}
        },
        "node_version": {
            "changelog": "<string>",
            "comfy_node_extract_status": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "dependencies": ["<string>"],
            "deprecated": True,
            "downloadUrl": "<string>",
            "id": "<string>",
            "node_id": "<string>",
            "status_reason": "<string>",
            "supported_accelerators": ["<string>"],
            "supported_comfyui_frontend_version": "<string>",
            "supported_comfyui_version": "<string>",
            "supported_os": ["<string>"],
            "tags": ["<string>"],
            "tags_admin": ["<string>"],
            "version": "<string>"
        },
        "personal_access_token": "<string>"
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
        node: {
          author: '<string>',
          banner_url: '<string>',
          category: '<string>',
          created_at: '2023-11-07T05:31:56Z',
          description: '<string>',
          downloads: 123,
          github_stars: 123,
          icon: '<string>',
          id: '<string>',
          latest_version: {
            changelog: '<string>',
            comfy_node_extract_status: '<string>',
            createdAt: '2023-11-07T05:31:56Z',
            dependencies: ['<string>'],
            deprecated: true,
            downloadUrl: '<string>',
            id: '<string>',
            node_id: '<string>',
            status_reason: '<string>',
            supported_accelerators: ['<string>'],
            supported_comfyui_frontend_version: '<string>',
            supported_comfyui_version: '<string>',
            supported_os: ['<string>'],
            tags: ['<string>'],
            tags_admin: ['<string>'],
            version: '<string>'
          },
          license: '<string>',
          name: '<string>',
          preempted_comfy_node_names: ['<string>'],
          publisher: {
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
          },
          rating: 123,
          repository: '<string>',
          search_ranking: 123,
          status_detail: '<string>',
          supported_accelerators: ['<string>'],
          supported_comfyui_frontend_version: '<string>',
          supported_comfyui_version: '<string>',
          supported_os: ['<string>'],
          tags: ['<string>'],
          tags_admin: ['<string>'],
          translations: {}
        },
        node_version: {
          changelog: '<string>',
          comfy_node_extract_status: '<string>',
          createdAt: '2023-11-07T05:31:56Z',
          dependencies: ['<string>'],
          deprecated: true,
          downloadUrl: '<string>',
          id: '<string>',
          node_id: '<string>',
          status_reason: '<string>',
          supported_accelerators: ['<string>'],
          supported_comfyui_frontend_version: '<string>',
          supported_comfyui_version: '<string>',
          supported_os: ['<string>'],
          tags: ['<string>'],
          tags_admin: ['<string>'],
          version: '<string>'
        },
        personal_access_token: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'node' => [
            'author' => '<string>',
            'banner_url' => '<string>',
            'category' => '<string>',
            'created_at' => '2023-11-07T05:31:56Z',
            'description' => '<string>',
            'downloads' => 123,
            'github_stars' => 123,
            'icon' => '<string>',
            'id' => '<string>',
            'latest_version' => [
                    'changelog' => '<string>',
                    'comfy_node_extract_status' => '<string>',
                    'createdAt' => '2023-11-07T05:31:56Z',
                    'dependencies' => [
                                    '<string>'
                    ],
                    'deprecated' => true,
                    'downloadUrl' => '<string>',
                    'id' => '<string>',
                    'node_id' => '<string>',
                    'status_reason' => '<string>',
                    'supported_accelerators' => [
                                    '<string>'
                    ],
                    'supported_comfyui_frontend_version' => '<string>',
                    'supported_comfyui_version' => '<string>',
                    'supported_os' => [
                                    '<string>'
                    ],
                    'tags' => [
                                    '<string>'
                    ],
                    'tags_admin' => [
                                    '<string>'
                    ],
                    'version' => '<string>'
            ],
            'license' => '<string>',
            'name' => '<string>',
            'preempted_comfy_node_names' => [
                    '<string>'
            ],
            'publisher' => [
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
            ],
            'rating' => 123,
            'repository' => '<string>',
            'search_ranking' => 123,
            'status_detail' => '<string>',
            'supported_accelerators' => [
                    '<string>'
            ],
            'supported_comfyui_frontend_version' => '<string>',
            'supported_comfyui_version' => '<string>',
            'supported_os' => [
                    '<string>'
            ],
            'tags' => [
                    '<string>'
            ],
            'tags_admin' => [
                    '<string>'
            ],
            'translations' => [
                    
            ]
        ],
        'node_version' => [
            'changelog' => '<string>',
            'comfy_node_extract_status' => '<string>',
            'createdAt' => '2023-11-07T05:31:56Z',
            'dependencies' => [
                    '<string>'
            ],
            'deprecated' => true,
            'downloadUrl' => '<string>',
            'id' => '<string>',
            'node_id' => '<string>',
            'status_reason' => '<string>',
            'supported_accelerators' => [
                    '<string>'
            ],
            'supported_comfyui_frontend_version' => '<string>',
            'supported_comfyui_version' => '<string>',
            'supported_os' => [
                    '<string>'
            ],
            'tags' => [
                    '<string>'
            ],
            'tags_admin' => [
                    '<string>'
            ],
            'version' => '<string>'
        ],
        'personal_access_token' => '<string>'
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions"
    
    	payload := strings.NewReader("{\n  \"node\": {\n    \"author\": \"<string>\",\n    \"banner_url\": \"<string>\",\n    \"category\": \"<string>\",\n    \"created_at\": \"2023-11-07T05:31:56Z\",\n    \"description\": \"<string>\",\n    \"downloads\": 123,\n    \"github_stars\": 123,\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"latest_version\": {\n      \"changelog\": \"<string>\",\n      \"comfy_node_extract_status\": \"<string>\",\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"dependencies\": [\n        \"<string>\"\n      ],\n      \"deprecated\": true,\n      \"downloadUrl\": \"<string>\",\n      \"id\": \"<string>\",\n      \"node_id\": \"<string>\",\n      \"status_reason\": \"<string>\",\n      \"supported_accelerators\": [\n        \"<string>\"\n      ],\n      \"supported_comfyui_frontend_version\": \"<string>\",\n      \"supported_comfyui_version\": \"<string>\",\n      \"supported_os\": [\n        \"<string>\"\n      ],\n      \"tags\": [\n        \"<string>\"\n      ],\n      \"tags_admin\": [\n        \"<string>\"\n      ],\n      \"version\": \"<string>\"\n    },\n    \"license\": \"<string>\",\n    \"name\": \"<string>\",\n    \"preempted_comfy_node_names\": [\n      \"<string>\"\n    ],\n    \"publisher\": {\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"description\": \"<string>\",\n      \"id\": \"<string>\",\n      \"logo\": \"<string>\",\n      \"members\": [\n        {\n          \"id\": \"<string>\",\n          \"role\": \"<string>\",\n          \"user\": {\n            \"email\": \"<string>\",\n            \"id\": \"<string>\",\n            \"name\": \"<string>\"\n          }\n        }\n      ],\n      \"name\": \"<string>\",\n      \"source_code_repo\": \"<string>\",\n      \"support\": \"<string>\",\n      \"website\": \"<string>\"\n    },\n    \"rating\": 123,\n    \"repository\": \"<string>\",\n    \"search_ranking\": 123,\n    \"status_detail\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"translations\": {}\n  },\n  \"node_version\": {\n    \"changelog\": \"<string>\",\n    \"comfy_node_extract_status\": \"<string>\",\n    \"createdAt\": \"2023-11-07T05:31:56Z\",\n    \"dependencies\": [\n      \"<string>\"\n    ],\n    \"deprecated\": true,\n    \"downloadUrl\": \"<string>\",\n    \"id\": \"<string>\",\n    \"node_id\": \"<string>\",\n    \"status_reason\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"version\": \"<string>\"\n  },\n  \"personal_access_token\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"node\": {\n    \"author\": \"<string>\",\n    \"banner_url\": \"<string>\",\n    \"category\": \"<string>\",\n    \"created_at\": \"2023-11-07T05:31:56Z\",\n    \"description\": \"<string>\",\n    \"downloads\": 123,\n    \"github_stars\": 123,\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"latest_version\": {\n      \"changelog\": \"<string>\",\n      \"comfy_node_extract_status\": \"<string>\",\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"dependencies\": [\n        \"<string>\"\n      ],\n      \"deprecated\": true,\n      \"downloadUrl\": \"<string>\",\n      \"id\": \"<string>\",\n      \"node_id\": \"<string>\",\n      \"status_reason\": \"<string>\",\n      \"supported_accelerators\": [\n        \"<string>\"\n      ],\n      \"supported_comfyui_frontend_version\": \"<string>\",\n      \"supported_comfyui_version\": \"<string>\",\n      \"supported_os\": [\n        \"<string>\"\n      ],\n      \"tags\": [\n        \"<string>\"\n      ],\n      \"tags_admin\": [\n        \"<string>\"\n      ],\n      \"version\": \"<string>\"\n    },\n    \"license\": \"<string>\",\n    \"name\": \"<string>\",\n    \"preempted_comfy_node_names\": [\n      \"<string>\"\n    ],\n    \"publisher\": {\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"description\": \"<string>\",\n      \"id\": \"<string>\",\n      \"logo\": \"<string>\",\n      \"members\": [\n        {\n          \"id\": \"<string>\",\n          \"role\": \"<string>\",\n          \"user\": {\n            \"email\": \"<string>\",\n            \"id\": \"<string>\",\n            \"name\": \"<string>\"\n          }\n        }\n      ],\n      \"name\": \"<string>\",\n      \"source_code_repo\": \"<string>\",\n      \"support\": \"<string>\",\n      \"website\": \"<string>\"\n    },\n    \"rating\": 123,\n    \"repository\": \"<string>\",\n    \"search_ranking\": 123,\n    \"status_detail\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"translations\": {}\n  },\n  \"node_version\": {\n    \"changelog\": \"<string>\",\n    \"comfy_node_extract_status\": \"<string>\",\n    \"createdAt\": \"2023-11-07T05:31:56Z\",\n    \"dependencies\": [\n      \"<string>\"\n    ],\n    \"deprecated\": true,\n    \"downloadUrl\": \"<string>\",\n    \"id\": \"<string>\",\n    \"node_id\": \"<string>\",\n    \"status_reason\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"version\": \"<string>\"\n  },\n  \"personal_access_token\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"node\": {\n    \"author\": \"<string>\",\n    \"banner_url\": \"<string>\",\n    \"category\": \"<string>\",\n    \"created_at\": \"2023-11-07T05:31:56Z\",\n    \"description\": \"<string>\",\n    \"downloads\": 123,\n    \"github_stars\": 123,\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"latest_version\": {\n      \"changelog\": \"<string>\",\n      \"comfy_node_extract_status\": \"<string>\",\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"dependencies\": [\n        \"<string>\"\n      ],\n      \"deprecated\": true,\n      \"downloadUrl\": \"<string>\",\n      \"id\": \"<string>\",\n      \"node_id\": \"<string>\",\n      \"status_reason\": \"<string>\",\n      \"supported_accelerators\": [\n        \"<string>\"\n      ],\n      \"supported_comfyui_frontend_version\": \"<string>\",\n      \"supported_comfyui_version\": \"<string>\",\n      \"supported_os\": [\n        \"<string>\"\n      ],\n      \"tags\": [\n        \"<string>\"\n      ],\n      \"tags_admin\": [\n        \"<string>\"\n      ],\n      \"version\": \"<string>\"\n    },\n    \"license\": \"<string>\",\n    \"name\": \"<string>\",\n    \"preempted_comfy_node_names\": [\n      \"<string>\"\n    ],\n    \"publisher\": {\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"description\": \"<string>\",\n      \"id\": \"<string>\",\n      \"logo\": \"<string>\",\n      \"members\": [\n        {\n          \"id\": \"<string>\",\n          \"role\": \"<string>\",\n          \"user\": {\n            \"email\": \"<string>\",\n            \"id\": \"<string>\",\n            \"name\": \"<string>\"\n          }\n        }\n      ],\n      \"name\": \"<string>\",\n      \"source_code_repo\": \"<string>\",\n      \"support\": \"<string>\",\n      \"website\": \"<string>\"\n    },\n    \"rating\": 123,\n    \"repository\": \"<string>\",\n    \"search_ranking\": 123,\n    \"status_detail\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"translations\": {}\n  },\n  \"node_version\": {\n    \"changelog\": \"<string>\",\n    \"comfy_node_extract_status\": \"<string>\",\n    \"createdAt\": \"2023-11-07T05:31:56Z\",\n    \"dependencies\": [\n      \"<string>\"\n    ],\n    \"deprecated\": true,\n    \"downloadUrl\": \"<string>\",\n    \"id\": \"<string>\",\n    \"node_id\": \"<string>\",\n    \"status_reason\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"version\": \"<string>\"\n  },\n  \"personal_access_token\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

201

400

403

500
    
    
    {
      "node_version": {
        "changelog": "<string>",
        "comfy_node_extract_status": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "dependencies": [
          "<string>"
        ],
        "deprecated": true,
        "downloadUrl": "<string>",
        "id": "<string>",
        "node_id": "<string>",
        "status": "NodeVersionStatusActive",
        "status_reason": "<string>",
        "supported_accelerators": [
          "<string>"
        ],
        "supported_comfyui_frontend_version": "<string>",
        "supported_comfyui_version": "<string>",
        "supported_os": [
          "<string>"
        ],
        "tags": [
          "<string>"
        ],
        "tags_admin": [
          "<string>"
        ],
        "version": "<string>"
      },
      "signedUrl": "<string>"
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

# Publish a new version of a node

Copiar páginaCopiar página

Copiar páginaCopiar página

POST

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

Pruébalo

Publish a new version of a node

cURL
    
    
    curl --request POST \
      --url https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "node": {
        "author": "<string>",
        "banner_url": "<string>",
        "category": "<string>",
        "created_at": "2023-11-07T05:31:56Z",
        "description": "<string>",
        "downloads": 123,
        "github_stars": 123,
        "icon": "<string>",
        "id": "<string>",
        "latest_version": {
          "changelog": "<string>",
          "comfy_node_extract_status": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "dependencies": [
            "<string>"
          ],
          "deprecated": true,
          "downloadUrl": "<string>",
          "id": "<string>",
          "node_id": "<string>",
          "status_reason": "<string>",
          "supported_accelerators": [
            "<string>"
          ],
          "supported_comfyui_frontend_version": "<string>",
          "supported_comfyui_version": "<string>",
          "supported_os": [
            "<string>"
          ],
          "tags": [
            "<string>"
          ],
          "tags_admin": [
            "<string>"
          ],
          "version": "<string>"
        },
        "license": "<string>",
        "name": "<string>",
        "preempted_comfy_node_names": [
          "<string>"
        ],
        "publisher": {
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
        },
        "rating": 123,
        "repository": "<string>",
        "search_ranking": 123,
        "status_detail": "<string>",
        "supported_accelerators": [
          "<string>"
        ],
        "supported_comfyui_frontend_version": "<string>",
        "supported_comfyui_version": "<string>",
        "supported_os": [
          "<string>"
        ],
        "tags": [
          "<string>"
        ],
        "tags_admin": [
          "<string>"
        ],
        "translations": {}
      },
      "node_version": {
        "changelog": "<string>",
        "comfy_node_extract_status": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "dependencies": [
          "<string>"
        ],
        "deprecated": true,
        "downloadUrl": "<string>",
        "id": "<string>",
        "node_id": "<string>",
        "status_reason": "<string>",
        "supported_accelerators": [
          "<string>"
        ],
        "supported_comfyui_frontend_version": "<string>",
        "supported_comfyui_version": "<string>",
        "supported_os": [
          "<string>"
        ],
        "tags": [
          "<string>"
        ],
        "tags_admin": [
          "<string>"
        ],
        "version": "<string>"
      },
      "personal_access_token": "<string>"
    }
    '
    
    
    import requests
    
    url = "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions"
    
    payload = {
        "node": {
            "author": "<string>",
            "banner_url": "<string>",
            "category": "<string>",
            "created_at": "2023-11-07T05:31:56Z",
            "description": "<string>",
            "downloads": 123,
            "github_stars": 123,
            "icon": "<string>",
            "id": "<string>",
            "latest_version": {
                "changelog": "<string>",
                "comfy_node_extract_status": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "dependencies": ["<string>"],
                "deprecated": True,
                "downloadUrl": "<string>",
                "id": "<string>",
                "node_id": "<string>",
                "status_reason": "<string>",
                "supported_accelerators": ["<string>"],
                "supported_comfyui_frontend_version": "<string>",
                "supported_comfyui_version": "<string>",
                "supported_os": ["<string>"],
                "tags": ["<string>"],
                "tags_admin": ["<string>"],
                "version": "<string>"
            },
            "license": "<string>",
            "name": "<string>",
            "preempted_comfy_node_names": ["<string>"],
            "publisher": {
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
            },
            "rating": 123,
            "repository": "<string>",
            "search_ranking": 123,
            "status_detail": "<string>",
            "supported_accelerators": ["<string>"],
            "supported_comfyui_frontend_version": "<string>",
            "supported_comfyui_version": "<string>",
            "supported_os": ["<string>"],
            "tags": ["<string>"],
            "tags_admin": ["<string>"],
            "translations": {}
        },
        "node_version": {
            "changelog": "<string>",
            "comfy_node_extract_status": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "dependencies": ["<string>"],
            "deprecated": True,
            "downloadUrl": "<string>",
            "id": "<string>",
            "node_id": "<string>",
            "status_reason": "<string>",
            "supported_accelerators": ["<string>"],
            "supported_comfyui_frontend_version": "<string>",
            "supported_comfyui_version": "<string>",
            "supported_os": ["<string>"],
            "tags": ["<string>"],
            "tags_admin": ["<string>"],
            "version": "<string>"
        },
        "personal_access_token": "<string>"
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
        node: {
          author: '<string>',
          banner_url: '<string>',
          category: '<string>',
          created_at: '2023-11-07T05:31:56Z',
          description: '<string>',
          downloads: 123,
          github_stars: 123,
          icon: '<string>',
          id: '<string>',
          latest_version: {
            changelog: '<string>',
            comfy_node_extract_status: '<string>',
            createdAt: '2023-11-07T05:31:56Z',
            dependencies: ['<string>'],
            deprecated: true,
            downloadUrl: '<string>',
            id: '<string>',
            node_id: '<string>',
            status_reason: '<string>',
            supported_accelerators: ['<string>'],
            supported_comfyui_frontend_version: '<string>',
            supported_comfyui_version: '<string>',
            supported_os: ['<string>'],
            tags: ['<string>'],
            tags_admin: ['<string>'],
            version: '<string>'
          },
          license: '<string>',
          name: '<string>',
          preempted_comfy_node_names: ['<string>'],
          publisher: {
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
          },
          rating: 123,
          repository: '<string>',
          search_ranking: 123,
          status_detail: '<string>',
          supported_accelerators: ['<string>'],
          supported_comfyui_frontend_version: '<string>',
          supported_comfyui_version: '<string>',
          supported_os: ['<string>'],
          tags: ['<string>'],
          tags_admin: ['<string>'],
          translations: {}
        },
        node_version: {
          changelog: '<string>',
          comfy_node_extract_status: '<string>',
          createdAt: '2023-11-07T05:31:56Z',
          dependencies: ['<string>'],
          deprecated: true,
          downloadUrl: '<string>',
          id: '<string>',
          node_id: '<string>',
          status_reason: '<string>',
          supported_accelerators: ['<string>'],
          supported_comfyui_frontend_version: '<string>',
          supported_comfyui_version: '<string>',
          supported_os: ['<string>'],
          tags: ['<string>'],
          tags_admin: ['<string>'],
          version: '<string>'
        },
        personal_access_token: '<string>'
      })
    };
    
    fetch('https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'node' => [
            'author' => '<string>',
            'banner_url' => '<string>',
            'category' => '<string>',
            'created_at' => '2023-11-07T05:31:56Z',
            'description' => '<string>',
            'downloads' => 123,
            'github_stars' => 123,
            'icon' => '<string>',
            'id' => '<string>',
            'latest_version' => [
                    'changelog' => '<string>',
                    'comfy_node_extract_status' => '<string>',
                    'createdAt' => '2023-11-07T05:31:56Z',
                    'dependencies' => [
                                    '<string>'
                    ],
                    'deprecated' => true,
                    'downloadUrl' => '<string>',
                    'id' => '<string>',
                    'node_id' => '<string>',
                    'status_reason' => '<string>',
                    'supported_accelerators' => [
                                    '<string>'
                    ],
                    'supported_comfyui_frontend_version' => '<string>',
                    'supported_comfyui_version' => '<string>',
                    'supported_os' => [
                                    '<string>'
                    ],
                    'tags' => [
                                    '<string>'
                    ],
                    'tags_admin' => [
                                    '<string>'
                    ],
                    'version' => '<string>'
            ],
            'license' => '<string>',
            'name' => '<string>',
            'preempted_comfy_node_names' => [
                    '<string>'
            ],
            'publisher' => [
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
            ],
            'rating' => 123,
            'repository' => '<string>',
            'search_ranking' => 123,
            'status_detail' => '<string>',
            'supported_accelerators' => [
                    '<string>'
            ],
            'supported_comfyui_frontend_version' => '<string>',
            'supported_comfyui_version' => '<string>',
            'supported_os' => [
                    '<string>'
            ],
            'tags' => [
                    '<string>'
            ],
            'tags_admin' => [
                    '<string>'
            ],
            'translations' => [
                    
            ]
        ],
        'node_version' => [
            'changelog' => '<string>',
            'comfy_node_extract_status' => '<string>',
            'createdAt' => '2023-11-07T05:31:56Z',
            'dependencies' => [
                    '<string>'
            ],
            'deprecated' => true,
            'downloadUrl' => '<string>',
            'id' => '<string>',
            'node_id' => '<string>',
            'status_reason' => '<string>',
            'supported_accelerators' => [
                    '<string>'
            ],
            'supported_comfyui_frontend_version' => '<string>',
            'supported_comfyui_version' => '<string>',
            'supported_os' => [
                    '<string>'
            ],
            'tags' => [
                    '<string>'
            ],
            'tags_admin' => [
                    '<string>'
            ],
            'version' => '<string>'
        ],
        'personal_access_token' => '<string>'
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
    
    	url := "https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions"
    
    	payload := strings.NewReader("{\n  \"node\": {\n    \"author\": \"<string>\",\n    \"banner_url\": \"<string>\",\n    \"category\": \"<string>\",\n    \"created_at\": \"2023-11-07T05:31:56Z\",\n    \"description\": \"<string>\",\n    \"downloads\": 123,\n    \"github_stars\": 123,\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"latest_version\": {\n      \"changelog\": \"<string>\",\n      \"comfy_node_extract_status\": \"<string>\",\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"dependencies\": [\n        \"<string>\"\n      ],\n      \"deprecated\": true,\n      \"downloadUrl\": \"<string>\",\n      \"id\": \"<string>\",\n      \"node_id\": \"<string>\",\n      \"status_reason\": \"<string>\",\n      \"supported_accelerators\": [\n        \"<string>\"\n      ],\n      \"supported_comfyui_frontend_version\": \"<string>\",\n      \"supported_comfyui_version\": \"<string>\",\n      \"supported_os\": [\n        \"<string>\"\n      ],\n      \"tags\": [\n        \"<string>\"\n      ],\n      \"tags_admin\": [\n        \"<string>\"\n      ],\n      \"version\": \"<string>\"\n    },\n    \"license\": \"<string>\",\n    \"name\": \"<string>\",\n    \"preempted_comfy_node_names\": [\n      \"<string>\"\n    ],\n    \"publisher\": {\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"description\": \"<string>\",\n      \"id\": \"<string>\",\n      \"logo\": \"<string>\",\n      \"members\": [\n        {\n          \"id\": \"<string>\",\n          \"role\": \"<string>\",\n          \"user\": {\n            \"email\": \"<string>\",\n            \"id\": \"<string>\",\n            \"name\": \"<string>\"\n          }\n        }\n      ],\n      \"name\": \"<string>\",\n      \"source_code_repo\": \"<string>\",\n      \"support\": \"<string>\",\n      \"website\": \"<string>\"\n    },\n    \"rating\": 123,\n    \"repository\": \"<string>\",\n    \"search_ranking\": 123,\n    \"status_detail\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"translations\": {}\n  },\n  \"node_version\": {\n    \"changelog\": \"<string>\",\n    \"comfy_node_extract_status\": \"<string>\",\n    \"createdAt\": \"2023-11-07T05:31:56Z\",\n    \"dependencies\": [\n      \"<string>\"\n    ],\n    \"deprecated\": true,\n    \"downloadUrl\": \"<string>\",\n    \"id\": \"<string>\",\n    \"node_id\": \"<string>\",\n    \"status_reason\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"version\": \"<string>\"\n  },\n  \"personal_access_token\": \"<string>\"\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"node\": {\n    \"author\": \"<string>\",\n    \"banner_url\": \"<string>\",\n    \"category\": \"<string>\",\n    \"created_at\": \"2023-11-07T05:31:56Z\",\n    \"description\": \"<string>\",\n    \"downloads\": 123,\n    \"github_stars\": 123,\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"latest_version\": {\n      \"changelog\": \"<string>\",\n      \"comfy_node_extract_status\": \"<string>\",\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"dependencies\": [\n        \"<string>\"\n      ],\n      \"deprecated\": true,\n      \"downloadUrl\": \"<string>\",\n      \"id\": \"<string>\",\n      \"node_id\": \"<string>\",\n      \"status_reason\": \"<string>\",\n      \"supported_accelerators\": [\n        \"<string>\"\n      ],\n      \"supported_comfyui_frontend_version\": \"<string>\",\n      \"supported_comfyui_version\": \"<string>\",\n      \"supported_os\": [\n        \"<string>\"\n      ],\n      \"tags\": [\n        \"<string>\"\n      ],\n      \"tags_admin\": [\n        \"<string>\"\n      ],\n      \"version\": \"<string>\"\n    },\n    \"license\": \"<string>\",\n    \"name\": \"<string>\",\n    \"preempted_comfy_node_names\": [\n      \"<string>\"\n    ],\n    \"publisher\": {\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"description\": \"<string>\",\n      \"id\": \"<string>\",\n      \"logo\": \"<string>\",\n      \"members\": [\n        {\n          \"id\": \"<string>\",\n          \"role\": \"<string>\",\n          \"user\": {\n            \"email\": \"<string>\",\n            \"id\": \"<string>\",\n            \"name\": \"<string>\"\n          }\n        }\n      ],\n      \"name\": \"<string>\",\n      \"source_code_repo\": \"<string>\",\n      \"support\": \"<string>\",\n      \"website\": \"<string>\"\n    },\n    \"rating\": 123,\n    \"repository\": \"<string>\",\n    \"search_ranking\": 123,\n    \"status_detail\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"translations\": {}\n  },\n  \"node_version\": {\n    \"changelog\": \"<string>\",\n    \"comfy_node_extract_status\": \"<string>\",\n    \"createdAt\": \"2023-11-07T05:31:56Z\",\n    \"dependencies\": [\n      \"<string>\"\n    ],\n    \"deprecated\": true,\n    \"downloadUrl\": \"<string>\",\n    \"id\": \"<string>\",\n    \"node_id\": \"<string>\",\n    \"status_reason\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"version\": \"<string>\"\n  },\n  \"personal_access_token\": \"<string>\"\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.comfy.org/publishers/{publisherId}/nodes/{nodeId}/versions")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"node\": {\n    \"author\": \"<string>\",\n    \"banner_url\": \"<string>\",\n    \"category\": \"<string>\",\n    \"created_at\": \"2023-11-07T05:31:56Z\",\n    \"description\": \"<string>\",\n    \"downloads\": 123,\n    \"github_stars\": 123,\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"latest_version\": {\n      \"changelog\": \"<string>\",\n      \"comfy_node_extract_status\": \"<string>\",\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"dependencies\": [\n        \"<string>\"\n      ],\n      \"deprecated\": true,\n      \"downloadUrl\": \"<string>\",\n      \"id\": \"<string>\",\n      \"node_id\": \"<string>\",\n      \"status_reason\": \"<string>\",\n      \"supported_accelerators\": [\n        \"<string>\"\n      ],\n      \"supported_comfyui_frontend_version\": \"<string>\",\n      \"supported_comfyui_version\": \"<string>\",\n      \"supported_os\": [\n        \"<string>\"\n      ],\n      \"tags\": [\n        \"<string>\"\n      ],\n      \"tags_admin\": [\n        \"<string>\"\n      ],\n      \"version\": \"<string>\"\n    },\n    \"license\": \"<string>\",\n    \"name\": \"<string>\",\n    \"preempted_comfy_node_names\": [\n      \"<string>\"\n    ],\n    \"publisher\": {\n      \"createdAt\": \"2023-11-07T05:31:56Z\",\n      \"description\": \"<string>\",\n      \"id\": \"<string>\",\n      \"logo\": \"<string>\",\n      \"members\": [\n        {\n          \"id\": \"<string>\",\n          \"role\": \"<string>\",\n          \"user\": {\n            \"email\": \"<string>\",\n            \"id\": \"<string>\",\n            \"name\": \"<string>\"\n          }\n        }\n      ],\n      \"name\": \"<string>\",\n      \"source_code_repo\": \"<string>\",\n      \"support\": \"<string>\",\n      \"website\": \"<string>\"\n    },\n    \"rating\": 123,\n    \"repository\": \"<string>\",\n    \"search_ranking\": 123,\n    \"status_detail\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"translations\": {}\n  },\n  \"node_version\": {\n    \"changelog\": \"<string>\",\n    \"comfy_node_extract_status\": \"<string>\",\n    \"createdAt\": \"2023-11-07T05:31:56Z\",\n    \"dependencies\": [\n      \"<string>\"\n    ],\n    \"deprecated\": true,\n    \"downloadUrl\": \"<string>\",\n    \"id\": \"<string>\",\n    \"node_id\": \"<string>\",\n    \"status_reason\": \"<string>\",\n    \"supported_accelerators\": [\n      \"<string>\"\n    ],\n    \"supported_comfyui_frontend_version\": \"<string>\",\n    \"supported_comfyui_version\": \"<string>\",\n    \"supported_os\": [\n      \"<string>\"\n    ],\n    \"tags\": [\n      \"<string>\"\n    ],\n    \"tags_admin\": [\n      \"<string>\"\n    ],\n    \"version\": \"<string>\"\n  },\n  \"personal_access_token\": \"<string>\"\n}"
    
    response = http.request(request)
    puts response.read_body

201

400

403

500
    
    
    {
      "node_version": {
        "changelog": "<string>",
        "comfy_node_extract_status": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "dependencies": [
          "<string>"
        ],
        "deprecated": true,
        "downloadUrl": "<string>",
        "id": "<string>",
        "node_id": "<string>",
        "status": "NodeVersionStatusActive",
        "status_reason": "<string>",
        "supported_accelerators": [
          "<string>"
        ],
        "supported_comfyui_frontend_version": "<string>",
        "supported_comfyui_version": "<string>",
        "supported_os": [
          "<string>"
        ],
        "tags": [
          "<string>"
        ],
        "tags_admin": [
          "<string>"
        ],
        "version": "<string>"
      },
      "signedUrl": "<string>"
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

​

nodeId

string

requerido

#### Cuerpo

application/json

​

node

object

requerido

Show child attributes

​

node_version

object

requerido

Show child attributes

​

personal_access_token

string

requerido

#### Respuesta

201

application/json

New version published successfully

​

node_version

object

Show child attributes

​

signedUrl

string

The signed URL to upload the node version token.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/api-reference/registry/publish-a-new-version-of-a-node.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/api-reference/registry/publish-a-new-version-of-a-node)

[Retrieve permissions the user has for a given publisher](https://docs.comfy.org/es/registry/api-reference/registry/retrieve-permissions-the-user-has-for-a-given-publisher)[Update changelog and deprecation status of a node version](https://docs.comfy.org/es/registry/api-reference/registry/update-changelog-and-deprecation-status-of-a-node-version)
