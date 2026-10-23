---
url: https://docs.comfy.org/registry/api-reference/registry/publish-a-new-version-of-a-node/
title: Publish a new version of a node - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:23.918726+00:00
---

# Publish a new version of a node - ComfyUI

> Source: https://docs.comfy.org/registry/api-reference/registry/publish-a-new-version-of-a-node/

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

Registry API Reference

# Publish a new version of a node

Copy pageCopy page

Copy pageCopy page

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

Try it

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

#### Body

application/json

​

node

object

required

Show child attributes

​

node_version

object

required

Show child attributes

​

personal_access_token

string

required

#### Response

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

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/api-reference/registry/publish-a-new-version-of-a-node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/api-reference/registry/publish-a-new-version-of-a-node)

[Claim nodeId into publisherId for the authenticated publisherPrevious](https://docs.comfy.org/registry/api-reference/registry/claim-nodeid-into-publisherid-for-the-authenticated-publisher)[Update changelog and deprecation status of a node versionNext](https://docs.comfy.org/registry/api-reference/registry/update-changelog-and-deprecation-status-of-a-node-version)

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
