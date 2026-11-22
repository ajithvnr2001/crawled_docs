---
url: https://docs.fish.audio/api-reference/endpoint/agent/create-agent/
title: Create Voice Agent - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:30:39.555197+00:00
---

# Create Voice Agent - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/agent/create-agent/

Create Agent

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/agent/agents \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
        "name": "Receptionist",
        "description": "Handles inbound calls.",
        "config": {
          "prompt": {
            "system_prompt": "You are the receptionist for Fish Dental."
          },
          "voice": {
            "voice_id": "<voice-model-id>",
            "speaking_language": "en"
          }
        }
      }'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/agents"
    
    payload = {
        "name": "<string>",
        "description": "",
        "config": {
            "prompt": {
                "system_prompt": "<string>",
                "first_message": "<string>",
                "first_message_prompt": "<string>"
            },
            "voice": {
                "voice_id": "<string>",
                "expressive": True,
                "speed": 1.25,
                "live3_prompt": "<string>",
                "pronunciation_dictionary_ids": ["<string>"],
                "background_sound": {
                    "preset": "off",
                    "volume": 0.15,
                    "custom_asset_id": "<string>"
                }
            },
            "asr": {
                "multilingual": True,
                "strict_language": True,
                "keyterms": ["<string>"]
            },
            "conversation": {
                "max_duration_seconds": 1830,
                "response_wait_ms": 1150,
                "response_max_wait_ms": 2000,
                "interruptible": True,
                "interruption_ignore_phrases": ["<string>"],
                "backchannel": {
                    "enabled": True,
                    "strength": 5
                },
                "speculative_response": True,
                "reengage": {
                    "enabled": True,
                    "steps": [
                        {
                            "after_seconds": 301,
                            "message": ""
                        }
                    ],
                    "exhausted_after_seconds": 301,
                    "schedule": {
                        "first_seconds": 301,
                        "interval_seconds": 301,
                        "count": 5,
                        "messages": ["<string>"]
                    }
                },
                "hangup_after_seconds": 1805,
                "hangup_farewell_message": "<string>",
                "record_audio": True,
                "timezone": "<string>",
                "transfer_destinations": [
                    {
                        "type": "phone",
                        "label": "",
                        "phone_number": "<string>",
                        "sip_uri": "<string>",
                        "headers": {},
                        "description": "",
                        "mode": "cold",
                        "warm_connect": "confirm",
                        "warm_briefing_instructions": "",
                        "warm_briefing_speed": 1.25,
                        "warm_ring_timeout_seconds": 30,
                        "warm_confirm_timeout_seconds": 60,
                        "warm_human_detection": False,
                        "warm_consult_uses_agent_settings": True,
                        "on_failure": {
                            "action": "return_to_agent",
                            "message": ""
                        },
                        "announcement_mode": "generated",
                        "announcement_message": "",
                        "auth_username": "<string>",
                        "auth_password": "<string>"
                    }
                ],
                "transfer_refuse_questions": True,
                "outbound": {
                    "amd_enabled": True,
                    "voicemail": {
                        "action": "hangup",
                        "message": ""
                    }
                },
                "keypad_menu": {
                    "enabled": False,
                    "prompt": "",
                    "options": [],
                    "accept_speech": True,
                    "variable": "menu_choice",
                    "no_input_timeout_seconds": 5,
                    "max_attempts": 2,
                    "retry_message": "",
                    "fallback_value": ""
                },
                "keypad_input": {
                    "enabled": False,
                    "terminator": "#",
                    "inter_digit_timeout_seconds": 2
                },
                "echo_guard": {
                    "web_voice": True,
                    "phone_inbound": True,
                    "phone_outbound": True
                },
                "turn_detector": {}
            },
            "tools": {
                "enabled": True,
                "tool_ids": ["<string>"],
                "system_tools": {
                    "hang_up_call": True,
                    "hang_up_call_farewell_message": "<string>",
                    "hang_up_call_refuse_questions": True
                }
            },
            "webhooks": {
                "conversation_init": {
                    "url": "<string>",
                    "secret": "<string>",
                    "keep_previous_secret_for_seconds": 302400,
                    "timeout_seconds": 5
                },
                "post_call": [
                    {
                        "url": "<string>",
                        "secret": "<string>",
                        "keep_previous_secret_for_seconds": 302400
                    }
                ]
            },
            "knowledge_base": {
                "enabled": True,
                "knowledge_source_ids": ["<string>"]
            },
            "analysis": {
                "summary": {
                    "enabled": True,
                    "prompt": "<string>",
                    "language": "en"
                },
                "data_fields": [
                    {
                        "name": "<string>",
                        "type": "text",
                        "description": "",
                        "enum_options": ["<string>"]
                    }
                ],
                "criteria": [
                    {
                        "name": "<string>",
                        "description": ""
                    }
                ]
            },
            "guardrails": {
                "focus": True,
                "manipulation": True,
                "pre_tool_speech": True
            },
            "context": { "current_time": True },
            "llm": {
                "custom": {
                    "base_url": "<string>",
                    "model": "<string>",
                    "api_key": "<string>",
                    "headers": {}
                },
                "fallback": {
                    "models": [
                        {
                            "custom": {
                                "base_url": "<string>",
                                "model": "<string>",
                                "api_key": "<string>",
                                "headers": {}
                            },
                            "ttft_timeout_ms": 15250,
                            "total_timeout_ms": 60500,
                            "parallel": { "kick_in_ms": 1500 }
                        }
                    ],
                    "primary": {
                        "ttft_timeout_ms": 15250,
                        "total_timeout_ms": 60500
                    }
                }
            },
            "variables": { "defaults": {} }
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
        name: '<string>',
        description: '',
        config: {
          prompt: {
            system_prompt: '<string>',
            first_message: '<string>',
            first_message_prompt: '<string>'
          },
          voice: {
            voice_id: '<string>',
            expressive: true,
            speed: 1.25,
            live3_prompt: '<string>',
            pronunciation_dictionary_ids: ['<string>'],
            background_sound: {preset: 'off', volume: 0.15, custom_asset_id: '<string>'}
          },
          asr: {multilingual: true, strict_language: true, keyterms: ['<string>']},
          conversation: {
            max_duration_seconds: 1830,
            response_wait_ms: 1150,
            response_max_wait_ms: 2000,
            interruptible: true,
            interruption_ignore_phrases: ['<string>'],
            backchannel: {enabled: true, strength: 5},
            speculative_response: true,
            reengage: {
              enabled: true,
              steps: [{after_seconds: 301, message: ''}],
              exhausted_after_seconds: 301,
              schedule: {first_seconds: 301, interval_seconds: 301, count: 5, messages: ['<string>']}
            },
            hangup_after_seconds: 1805,
            hangup_farewell_message: '<string>',
            record_audio: true,
            timezone: '<string>',
            transfer_destinations: [
              {
                type: 'phone',
                label: '',
                phone_number: '<string>',
                sip_uri: '<string>',
                headers: {},
                description: '',
                mode: 'cold',
                warm_connect: 'confirm',
                warm_briefing_instructions: '',
                warm_briefing_speed: 1.25,
                warm_ring_timeout_seconds: 30,
                warm_confirm_timeout_seconds: 60,
                warm_human_detection: false,
                warm_consult_uses_agent_settings: true,
                on_failure: {action: 'return_to_agent', message: ''},
                announcement_mode: 'generated',
                announcement_message: '',
                auth_username: '<string>',
                auth_password: '<string>'
              }
            ],
            transfer_refuse_questions: true,
            outbound: {amd_enabled: true, voicemail: {action: 'hangup', message: ''}},
            keypad_menu: {
              enabled: false,
              prompt: '',
              options: [],
              accept_speech: true,
              variable: 'menu_choice',
              no_input_timeout_seconds: 5,
              max_attempts: 2,
              retry_message: '',
              fallback_value: ''
            },
            keypad_input: {enabled: false, terminator: '#', inter_digit_timeout_seconds: 2},
            echo_guard: {web_voice: true, phone_inbound: true, phone_outbound: true},
            turn_detector: {}
          },
          tools: {
            enabled: true,
            tool_ids: ['<string>'],
            system_tools: {
              hang_up_call: true,
              hang_up_call_farewell_message: '<string>',
              hang_up_call_refuse_questions: true
            }
          },
          webhooks: {
            conversation_init: {
              url: '<string>',
              secret: '<string>',
              keep_previous_secret_for_seconds: 302400,
              timeout_seconds: 5
            },
            post_call: [
              {url: '<string>', secret: '<string>', keep_previous_secret_for_seconds: 302400}
            ]
          },
          knowledge_base: {enabled: true, knowledge_source_ids: ['<string>']},
          analysis: {
            summary: {enabled: true, prompt: '<string>', language: 'en'},
            data_fields: [{name: '<string>', type: 'text', description: '', enum_options: ['<string>']}],
            criteria: [{name: '<string>', description: ''}]
          },
          guardrails: {focus: true, manipulation: true, pre_tool_speech: true},
          context: {current_time: true},
          llm: {
            custom: {base_url: '<string>', model: '<string>', api_key: '<string>', headers: {}},
            fallback: {
              models: [
                {
                  custom: {base_url: '<string>', model: '<string>', api_key: '<string>', headers: {}},
                  ttft_timeout_ms: 15250,
                  total_timeout_ms: 60500,
                  parallel: {kick_in_ms: 1500}
                }
              ],
              primary: {ttft_timeout_ms: 15250, total_timeout_ms: 60500}
            }
          },
          variables: {defaults: {}}
        }
      })
    };
    
    fetch('https://api.fish.audio/v1/agent/agents', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/agents",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'name' => '<string>',
        'description' => '',
        'config' => [
            'prompt' => [
                    'system_prompt' => '<string>',
                    'first_message' => '<string>',
                    'first_message_prompt' => '<string>'
            ],
            'voice' => [
                    'voice_id' => '<string>',
                    'expressive' => true,
                    'speed' => 1.25,
                    'live3_prompt' => '<string>',
                    'pronunciation_dictionary_ids' => [
                                    '<string>'
                    ],
                    'background_sound' => [
                                    'preset' => 'off',
                                    'volume' => 0.15,
                                    'custom_asset_id' => '<string>'
                    ]
            ],
            'asr' => [
                    'multilingual' => true,
                    'strict_language' => true,
                    'keyterms' => [
                                    '<string>'
                    ]
            ],
            'conversation' => [
                    'max_duration_seconds' => 1830,
                    'response_wait_ms' => 1150,
                    'response_max_wait_ms' => 2000,
                    'interruptible' => true,
                    'interruption_ignore_phrases' => [
                                    '<string>'
                    ],
                    'backchannel' => [
                                    'enabled' => true,
                                    'strength' => 5
                    ],
                    'speculative_response' => true,
                    'reengage' => [
                                    'enabled' => true,
                                    'steps' => [
                                                                    [
                                                                                                                                    'after_seconds' => 301,
                                                                                                                                    'message' => ''
                                                                    ]
                                    ],
                                    'exhausted_after_seconds' => 301,
                                    'schedule' => [
                                                                    'first_seconds' => 301,
                                                                    'interval_seconds' => 301,
                                                                    'count' => 5,
                                                                    'messages' => [
                                                                                                                                    '<string>'
                                                                    ]
                                    ]
                    ],
                    'hangup_after_seconds' => 1805,
                    'hangup_farewell_message' => '<string>',
                    'record_audio' => true,
                    'timezone' => '<string>',
                    'transfer_destinations' => [
                                    [
                                                                    'type' => 'phone',
                                                                    'label' => '',
                                                                    'phone_number' => '<string>',
                                                                    'sip_uri' => '<string>',
                                                                    'headers' => [
                                                                                                                                    
                                                                    ],
                                                                    'description' => '',
                                                                    'mode' => 'cold',
                                                                    'warm_connect' => 'confirm',
                                                                    'warm_briefing_instructions' => '',
                                                                    'warm_briefing_speed' => 1.25,
                                                                    'warm_ring_timeout_seconds' => 30,
                                                                    'warm_confirm_timeout_seconds' => 60,
                                                                    'warm_human_detection' => false,
                                                                    'warm_consult_uses_agent_settings' => true,
                                                                    'on_failure' => [
                                                                                                                                    'action' => 'return_to_agent',
                                                                                                                                    'message' => ''
                                                                    ],
                                                                    'announcement_mode' => 'generated',
                                                                    'announcement_message' => '',
                                                                    'auth_username' => '<string>',
                                                                    'auth_password' => '<string>'
                                    ]
                    ],
                    'transfer_refuse_questions' => true,
                    'outbound' => [
                                    'amd_enabled' => true,
                                    'voicemail' => [
                                                                    'action' => 'hangup',
                                                                    'message' => ''
                                    ]
                    ],
                    'keypad_menu' => [
                                    'enabled' => false,
                                    'prompt' => '',
                                    'options' => [
                                                                    
                                    ],
                                    'accept_speech' => true,
                                    'variable' => 'menu_choice',
                                    'no_input_timeout_seconds' => 5,
                                    'max_attempts' => 2,
                                    'retry_message' => '',
                                    'fallback_value' => ''
                    ],
                    'keypad_input' => [
                                    'enabled' => false,
                                    'terminator' => '#',
                                    'inter_digit_timeout_seconds' => 2
                    ],
                    'echo_guard' => [
                                    'web_voice' => true,
                                    'phone_inbound' => true,
                                    'phone_outbound' => true
                    ],
                    'turn_detector' => [
                                    
                    ]
            ],
            'tools' => [
                    'enabled' => true,
                    'tool_ids' => [
                                    '<string>'
                    ],
                    'system_tools' => [
                                    'hang_up_call' => true,
                                    'hang_up_call_farewell_message' => '<string>',
                                    'hang_up_call_refuse_questions' => true
                    ]
            ],
            'webhooks' => [
                    'conversation_init' => [
                                    'url' => '<string>',
                                    'secret' => '<string>',
                                    'keep_previous_secret_for_seconds' => 302400,
                                    'timeout_seconds' => 5
                    ],
                    'post_call' => [
                                    [
                                                                    'url' => '<string>',
                                                                    'secret' => '<string>',
                                                                    'keep_previous_secret_for_seconds' => 302400
                                    ]
                    ]
            ],
            'knowledge_base' => [
                    'enabled' => true,
                    'knowledge_source_ids' => [
                                    '<string>'
                    ]
            ],
            'analysis' => [
                    'summary' => [
                                    'enabled' => true,
                                    'prompt' => '<string>',
                                    'language' => 'en'
                    ],
                    'data_fields' => [
                                    [
                                                                    'name' => '<string>',
                                                                    'type' => 'text',
                                                                    'description' => '',
                                                                    'enum_options' => [
                                                                                                                                    '<string>'
                                                                    ]
                                    ]
                    ],
                    'criteria' => [
                                    [
                                                                    'name' => '<string>',
                                                                    'description' => ''
                                    ]
                    ]
            ],
            'guardrails' => [
                    'focus' => true,
                    'manipulation' => true,
                    'pre_tool_speech' => true
            ],
            'context' => [
                    'current_time' => true
            ],
            'llm' => [
                    'custom' => [
                                    'base_url' => '<string>',
                                    'model' => '<string>',
                                    'api_key' => '<string>',
                                    'headers' => [
                                                                    
                                    ]
                    ],
                    'fallback' => [
                                    'models' => [
                                                                    [
                                                                                                                                    'custom' => [
                                                                                                                                                                                                                                                                    'base_url' => '<string>',
                                                                                                                                                                                                                                                                    'model' => '<string>',
                                                                                                                                                                                                                                                                    'api_key' => '<string>',
                                                                                                                                                                                                                                                                    'headers' => [
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                    ]
                                                                                                                                    ],
                                                                                                                                    'ttft_timeout_ms' => 15250,
                                                                                                                                    'total_timeout_ms' => 60500,
                                                                                                                                    'parallel' => [
                                                                                                                                                                                                                                                                    'kick_in_ms' => 1500
                                                                                                                                    ]
                                                                    ]
                                    ],
                                    'primary' => [
                                                                    'ttft_timeout_ms' => 15250,
                                                                    'total_timeout_ms' => 60500
                                    ]
                    ]
            ],
            'variables' => [
                    'defaults' => [
                                    
                    ]
            ]
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
    
    	url := "https://api.fish.audio/v1/agent/agents"
    
    	payload := strings.NewReader("{\n  \"name\": \"<string>\",\n  \"description\": \"\",\n  \"config\": {\n    \"prompt\": {\n      \"system_prompt\": \"<string>\",\n      \"first_message\": \"<string>\",\n      \"first_message_prompt\": \"<string>\"\n    },\n    \"voice\": {\n      \"voice_id\": \"<string>\",\n      \"expressive\": true,\n      \"speed\": 1.25,\n      \"live3_prompt\": \"<string>\",\n      \"pronunciation_dictionary_ids\": [\n        \"<string>\"\n      ],\n      \"background_sound\": {\n        \"preset\": \"off\",\n        \"volume\": 0.15,\n        \"custom_asset_id\": \"<string>\"\n      }\n    },\n    \"asr\": {\n      \"multilingual\": true,\n      \"strict_language\": true,\n      \"keyterms\": [\n        \"<string>\"\n      ]\n    },\n    \"conversation\": {\n      \"max_duration_seconds\": 1830,\n      \"response_wait_ms\": 1150,\n      \"response_max_wait_ms\": 2000,\n      \"interruptible\": true,\n      \"interruption_ignore_phrases\": [\n        \"<string>\"\n      ],\n      \"backchannel\": {\n        \"enabled\": true,\n        \"strength\": 5\n      },\n      \"speculative_response\": true,\n      \"reengage\": {\n        \"enabled\": true,\n        \"steps\": [\n          {\n            \"after_seconds\": 301,\n            \"message\": \"\"\n          }\n        ],\n        \"exhausted_after_seconds\": 301,\n        \"schedule\": {\n          \"first_seconds\": 301,\n          \"interval_seconds\": 301,\n          \"count\": 5,\n          \"messages\": [\n            \"<string>\"\n          ]\n        }\n      },\n      \"hangup_after_seconds\": 1805,\n      \"hangup_farewell_message\": \"<string>\",\n      \"record_audio\": true,\n      \"timezone\": \"<string>\",\n      \"transfer_destinations\": [\n        {\n          \"type\": \"phone\",\n          \"label\": \"\",\n          \"phone_number\": \"<string>\",\n          \"sip_uri\": \"<string>\",\n          \"headers\": {},\n          \"description\": \"\",\n          \"mode\": \"cold\",\n          \"warm_connect\": \"confirm\",\n          \"warm_briefing_instructions\": \"\",\n          \"warm_briefing_speed\": 1.25,\n          \"warm_ring_timeout_seconds\": 30,\n          \"warm_confirm_timeout_seconds\": 60,\n          \"warm_human_detection\": false,\n          \"warm_consult_uses_agent_settings\": true,\n          \"on_failure\": {\n            \"action\": \"return_to_agent\",\n            \"message\": \"\"\n          },\n          \"announcement_mode\": \"generated\",\n          \"announcement_message\": \"\",\n          \"auth_username\": \"<string>\",\n          \"auth_password\": \"<string>\"\n        }\n      ],\n      \"transfer_refuse_questions\": true,\n      \"outbound\": {\n        \"amd_enabled\": true,\n        \"voicemail\": {\n          \"action\": \"hangup\",\n          \"message\": \"\"\n        }\n      },\n      \"keypad_menu\": {\n        \"enabled\": false,\n        \"prompt\": \"\",\n        \"options\": [],\n        \"accept_speech\": true,\n        \"variable\": \"menu_choice\",\n        \"no_input_timeout_seconds\": 5,\n        \"max_attempts\": 2,\n        \"retry_message\": \"\",\n        \"fallback_value\": \"\"\n      },\n      \"keypad_input\": {\n        \"enabled\": false,\n        \"terminator\": \"#\",\n        \"inter_digit_timeout_seconds\": 2\n      },\n      \"echo_guard\": {\n        \"web_voice\": true,\n        \"phone_inbound\": true,\n        \"phone_outbound\": true\n      },\n      \"turn_detector\": {}\n    },\n    \"tools\": {\n      \"enabled\": true,\n      \"tool_ids\": [\n        \"<string>\"\n      ],\n      \"system_tools\": {\n        \"hang_up_call\": true,\n        \"hang_up_call_farewell_message\": \"<string>\",\n        \"hang_up_call_refuse_questions\": true\n      }\n    },\n    \"webhooks\": {\n      \"conversation_init\": {\n        \"url\": \"<string>\",\n        \"secret\": \"<string>\",\n        \"keep_previous_secret_for_seconds\": 302400,\n        \"timeout_seconds\": 5\n      },\n      \"post_call\": [\n        {\n          \"url\": \"<string>\",\n          \"secret\": \"<string>\",\n          \"keep_previous_secret_for_seconds\": 302400\n        }\n      ]\n    },\n    \"knowledge_base\": {\n      \"enabled\": true,\n      \"knowledge_source_ids\": [\n        \"<string>\"\n      ]\n    },\n    \"analysis\": {\n      \"summary\": {\n        \"enabled\": true,\n        \"prompt\": \"<string>\",\n        \"language\": \"en\"\n      },\n      \"data_fields\": [\n        {\n          \"name\": \"<string>\",\n          \"type\": \"text\",\n          \"description\": \"\",\n          \"enum_options\": [\n            \"<string>\"\n          ]\n        }\n      ],\n      \"criteria\": [\n        {\n          \"name\": \"<string>\",\n          \"description\": \"\"\n        }\n      ]\n    },\n    \"guardrails\": {\n      \"focus\": true,\n      \"manipulation\": true,\n      \"pre_tool_speech\": true\n    },\n    \"context\": {\n      \"current_time\": true\n    },\n    \"llm\": {\n      \"custom\": {\n        \"base_url\": \"<string>\",\n        \"model\": \"<string>\",\n        \"api_key\": \"<string>\",\n        \"headers\": {}\n      },\n      \"fallback\": {\n        \"models\": [\n          {\n            \"custom\": {\n              \"base_url\": \"<string>\",\n              \"model\": \"<string>\",\n              \"api_key\": \"<string>\",\n              \"headers\": {}\n            },\n            \"ttft_timeout_ms\": 15250,\n            \"total_timeout_ms\": 60500,\n            \"parallel\": {\n              \"kick_in_ms\": 1500\n            }\n          }\n        ],\n        \"primary\": {\n          \"ttft_timeout_ms\": 15250,\n          \"total_timeout_ms\": 60500\n        }\n      }\n    },\n    \"variables\": {\n      \"defaults\": {}\n    }\n  }\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/v1/agent/agents")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"name\": \"<string>\",\n  \"description\": \"\",\n  \"config\": {\n    \"prompt\": {\n      \"system_prompt\": \"<string>\",\n      \"first_message\": \"<string>\",\n      \"first_message_prompt\": \"<string>\"\n    },\n    \"voice\": {\n      \"voice_id\": \"<string>\",\n      \"expressive\": true,\n      \"speed\": 1.25,\n      \"live3_prompt\": \"<string>\",\n      \"pronunciation_dictionary_ids\": [\n        \"<string>\"\n      ],\n      \"background_sound\": {\n        \"preset\": \"off\",\n        \"volume\": 0.15,\n        \"custom_asset_id\": \"<string>\"\n      }\n    },\n    \"asr\": {\n      \"multilingual\": true,\n      \"strict_language\": true,\n      \"keyterms\": [\n        \"<string>\"\n      ]\n    },\n    \"conversation\": {\n      \"max_duration_seconds\": 1830,\n      \"response_wait_ms\": 1150,\n      \"response_max_wait_ms\": 2000,\n      \"interruptible\": true,\n      \"interruption_ignore_phrases\": [\n        \"<string>\"\n      ],\n      \"backchannel\": {\n        \"enabled\": true,\n        \"strength\": 5\n      },\n      \"speculative_response\": true,\n      \"reengage\": {\n        \"enabled\": true,\n        \"steps\": [\n          {\n            \"after_seconds\": 301,\n            \"message\": \"\"\n          }\n        ],\n        \"exhausted_after_seconds\": 301,\n        \"schedule\": {\n          \"first_seconds\": 301,\n          \"interval_seconds\": 301,\n          \"count\": 5,\n          \"messages\": [\n            \"<string>\"\n          ]\n        }\n      },\n      \"hangup_after_seconds\": 1805,\n      \"hangup_farewell_message\": \"<string>\",\n      \"record_audio\": true,\n      \"timezone\": \"<string>\",\n      \"transfer_destinations\": [\n        {\n          \"type\": \"phone\",\n          \"label\": \"\",\n          \"phone_number\": \"<string>\",\n          \"sip_uri\": \"<string>\",\n          \"headers\": {},\n          \"description\": \"\",\n          \"mode\": \"cold\",\n          \"warm_connect\": \"confirm\",\n          \"warm_briefing_instructions\": \"\",\n          \"warm_briefing_speed\": 1.25,\n          \"warm_ring_timeout_seconds\": 30,\n          \"warm_confirm_timeout_seconds\": 60,\n          \"warm_human_detection\": false,\n          \"warm_consult_uses_agent_settings\": true,\n          \"on_failure\": {\n            \"action\": \"return_to_agent\",\n            \"message\": \"\"\n          },\n          \"announcement_mode\": \"generated\",\n          \"announcement_message\": \"\",\n          \"auth_username\": \"<string>\",\n          \"auth_password\": \"<string>\"\n        }\n      ],\n      \"transfer_refuse_questions\": true,\n      \"outbound\": {\n        \"amd_enabled\": true,\n        \"voicemail\": {\n          \"action\": \"hangup\",\n          \"message\": \"\"\n        }\n      },\n      \"keypad_menu\": {\n        \"enabled\": false,\n        \"prompt\": \"\",\n        \"options\": [],\n        \"accept_speech\": true,\n        \"variable\": \"menu_choice\",\n        \"no_input_timeout_seconds\": 5,\n        \"max_attempts\": 2,\n        \"retry_message\": \"\",\n        \"fallback_value\": \"\"\n      },\n      \"keypad_input\": {\n        \"enabled\": false,\n        \"terminator\": \"#\",\n        \"inter_digit_timeout_seconds\": 2\n      },\n      \"echo_guard\": {\n        \"web_voice\": true,\n        \"phone_inbound\": true,\n        \"phone_outbound\": true\n      },\n      \"turn_detector\": {}\n    },\n    \"tools\": {\n      \"enabled\": true,\n      \"tool_ids\": [\n        \"<string>\"\n      ],\n      \"system_tools\": {\n        \"hang_up_call\": true,\n        \"hang_up_call_farewell_message\": \"<string>\",\n        \"hang_up_call_refuse_questions\": true\n      }\n    },\n    \"webhooks\": {\n      \"conversation_init\": {\n        \"url\": \"<string>\",\n        \"secret\": \"<string>\",\n        \"keep_previous_secret_for_seconds\": 302400,\n        \"timeout_seconds\": 5\n      },\n      \"post_call\": [\n        {\n          \"url\": \"<string>\",\n          \"secret\": \"<string>\",\n          \"keep_previous_secret_for_seconds\": 302400\n        }\n      ]\n    },\n    \"knowledge_base\": {\n      \"enabled\": true,\n      \"knowledge_source_ids\": [\n        \"<string>\"\n      ]\n    },\n    \"analysis\": {\n      \"summary\": {\n        \"enabled\": true,\n        \"prompt\": \"<string>\",\n        \"language\": \"en\"\n      },\n      \"data_fields\": [\n        {\n          \"name\": \"<string>\",\n          \"type\": \"text\",\n          \"description\": \"\",\n          \"enum_options\": [\n            \"<string>\"\n          ]\n        }\n      ],\n      \"criteria\": [\n        {\n          \"name\": \"<string>\",\n          \"description\": \"\"\n        }\n      ]\n    },\n    \"guardrails\": {\n      \"focus\": true,\n      \"manipulation\": true,\n      \"pre_tool_speech\": true\n    },\n    \"context\": {\n      \"current_time\": true\n    },\n    \"llm\": {\n      \"custom\": {\n        \"base_url\": \"<string>\",\n        \"model\": \"<string>\",\n        \"api_key\": \"<string>\",\n        \"headers\": {}\n      },\n      \"fallback\": {\n        \"models\": [\n          {\n            \"custom\": {\n              \"base_url\": \"<string>\",\n              \"model\": \"<string>\",\n              \"api_key\": \"<string>\",\n              \"headers\": {}\n            },\n            \"ttft_timeout_ms\": 15250,\n            \"total_timeout_ms\": 60500,\n            \"parallel\": {\n              \"kick_in_ms\": 1500\n            }\n          }\n        ],\n        \"primary\": {\n          \"ttft_timeout_ms\": 15250,\n          \"total_timeout_ms\": 60500\n        }\n      }\n    },\n    \"variables\": {\n      \"defaults\": {}\n    }\n  }\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/agents")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"name\": \"<string>\",\n  \"description\": \"\",\n  \"config\": {\n    \"prompt\": {\n      \"system_prompt\": \"<string>\",\n      \"first_message\": \"<string>\",\n      \"first_message_prompt\": \"<string>\"\n    },\n    \"voice\": {\n      \"voice_id\": \"<string>\",\n      \"expressive\": true,\n      \"speed\": 1.25,\n      \"live3_prompt\": \"<string>\",\n      \"pronunciation_dictionary_ids\": [\n        \"<string>\"\n      ],\n      \"background_sound\": {\n        \"preset\": \"off\",\n        \"volume\": 0.15,\n        \"custom_asset_id\": \"<string>\"\n      }\n    },\n    \"asr\": {\n      \"multilingual\": true,\n      \"strict_language\": true,\n      \"keyterms\": [\n        \"<string>\"\n      ]\n    },\n    \"conversation\": {\n      \"max_duration_seconds\": 1830,\n      \"response_wait_ms\": 1150,\n      \"response_max_wait_ms\": 2000,\n      \"interruptible\": true,\n      \"interruption_ignore_phrases\": [\n        \"<string>\"\n      ],\n      \"backchannel\": {\n        \"enabled\": true,\n        \"strength\": 5\n      },\n      \"speculative_response\": true,\n      \"reengage\": {\n        \"enabled\": true,\n        \"steps\": [\n          {\n            \"after_seconds\": 301,\n            \"message\": \"\"\n          }\n        ],\n        \"exhausted_after_seconds\": 301,\n        \"schedule\": {\n          \"first_seconds\": 301,\n          \"interval_seconds\": 301,\n          \"count\": 5,\n          \"messages\": [\n            \"<string>\"\n          ]\n        }\n      },\n      \"hangup_after_seconds\": 1805,\n      \"hangup_farewell_message\": \"<string>\",\n      \"record_audio\": true,\n      \"timezone\": \"<string>\",\n      \"transfer_destinations\": [\n        {\n          \"type\": \"phone\",\n          \"label\": \"\",\n          \"phone_number\": \"<string>\",\n          \"sip_uri\": \"<string>\",\n          \"headers\": {},\n          \"description\": \"\",\n          \"mode\": \"cold\",\n          \"warm_connect\": \"confirm\",\n          \"warm_briefing_instructions\": \"\",\n          \"warm_briefing_speed\": 1.25,\n          \"warm_ring_timeout_seconds\": 30,\n          \"warm_confirm_timeout_seconds\": 60,\n          \"warm_human_detection\": false,\n          \"warm_consult_uses_agent_settings\": true,\n          \"on_failure\": {\n            \"action\": \"return_to_agent\",\n            \"message\": \"\"\n          },\n          \"announcement_mode\": \"generated\",\n          \"announcement_message\": \"\",\n          \"auth_username\": \"<string>\",\n          \"auth_password\": \"<string>\"\n        }\n      ],\n      \"transfer_refuse_questions\": true,\n      \"outbound\": {\n        \"amd_enabled\": true,\n        \"voicemail\": {\n          \"action\": \"hangup\",\n          \"message\": \"\"\n        }\n      },\n      \"keypad_menu\": {\n        \"enabled\": false,\n        \"prompt\": \"\",\n        \"options\": [],\n        \"accept_speech\": true,\n        \"variable\": \"menu_choice\",\n        \"no_input_timeout_seconds\": 5,\n        \"max_attempts\": 2,\n        \"retry_message\": \"\",\n        \"fallback_value\": \"\"\n      },\n      \"keypad_input\": {\n        \"enabled\": false,\n        \"terminator\": \"#\",\n        \"inter_digit_timeout_seconds\": 2\n      },\n      \"echo_guard\": {\n        \"web_voice\": true,\n        \"phone_inbound\": true,\n        \"phone_outbound\": true\n      },\n      \"turn_detector\": {}\n    },\n    \"tools\": {\n      \"enabled\": true,\n      \"tool_ids\": [\n        \"<string>\"\n      ],\n      \"system_tools\": {\n        \"hang_up_call\": true,\n        \"hang_up_call_farewell_message\": \"<string>\",\n        \"hang_up_call_refuse_questions\": true\n      }\n    },\n    \"webhooks\": {\n      \"conversation_init\": {\n        \"url\": \"<string>\",\n        \"secret\": \"<string>\",\n        \"keep_previous_secret_for_seconds\": 302400,\n        \"timeout_seconds\": 5\n      },\n      \"post_call\": [\n        {\n          \"url\": \"<string>\",\n          \"secret\": \"<string>\",\n          \"keep_previous_secret_for_seconds\": 302400\n        }\n      ]\n    },\n    \"knowledge_base\": {\n      \"enabled\": true,\n      \"knowledge_source_ids\": [\n        \"<string>\"\n      ]\n    },\n    \"analysis\": {\n      \"summary\": {\n        \"enabled\": true,\n        \"prompt\": \"<string>\",\n        \"language\": \"en\"\n      },\n      \"data_fields\": [\n        {\n          \"name\": \"<string>\",\n          \"type\": \"text\",\n          \"description\": \"\",\n          \"enum_options\": [\n            \"<string>\"\n          ]\n        }\n      ],\n      \"criteria\": [\n        {\n          \"name\": \"<string>\",\n          \"description\": \"\"\n        }\n      ]\n    },\n    \"guardrails\": {\n      \"focus\": true,\n      \"manipulation\": true,\n      \"pre_tool_speech\": true\n    },\n    \"context\": {\n      \"current_time\": true\n    },\n    \"llm\": {\n      \"custom\": {\n        \"base_url\": \"<string>\",\n        \"model\": \"<string>\",\n        \"api_key\": \"<string>\",\n        \"headers\": {}\n      },\n      \"fallback\": {\n        \"models\": [\n          {\n            \"custom\": {\n              \"base_url\": \"<string>\",\n              \"model\": \"<string>\",\n              \"api_key\": \"<string>\",\n              \"headers\": {}\n            },\n            \"ttft_timeout_ms\": 15250,\n            \"total_timeout_ms\": 60500,\n            \"parallel\": {\n              \"kick_in_ms\": 1500\n            }\n          }\n        ],\n        \"primary\": {\n          \"ttft_timeout_ms\": 15250,\n          \"total_timeout_ms\": 60500\n        }\n      }\n    },\n    \"variables\": {\n      \"defaults\": {}\n    }\n  }\n}"
    
    response = http.request(request)
    puts response.read_body

201

401

403

422

503
    
    
    {
      "agent_id": "<string>",
      "workspace_id": "<string>",
      "name": "<string>",
      "status": "active",
      "publication_state": "live",
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "description": "",
      "public_enabled": false,
      "allowed_origins": [
        "<string>"
      ],
      "restrict_origins": false,
      "overrides_allowed": [
        "first_message"
      ]
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

Agents

# Create Voice Agent

Copy pageCopy page

Create an agent, optionally with its full initial configuration inline — one call provisions a ready-to-publish agent.

Copy pageCopy page

POST

/

v1

/

agent

/

agents

Try it

Create Agent

cURL
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/agent/agents \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
        "name": "Receptionist",
        "description": "Handles inbound calls.",
        "config": {
          "prompt": {
            "system_prompt": "You are the receptionist for Fish Dental."
          },
          "voice": {
            "voice_id": "<voice-model-id>",
            "speaking_language": "en"
          }
        }
      }'
    
    
    import requests
    
    url = "https://api.fish.audio/v1/agent/agents"
    
    payload = {
        "name": "<string>",
        "description": "",
        "config": {
            "prompt": {
                "system_prompt": "<string>",
                "first_message": "<string>",
                "first_message_prompt": "<string>"
            },
            "voice": {
                "voice_id": "<string>",
                "expressive": True,
                "speed": 1.25,
                "live3_prompt": "<string>",
                "pronunciation_dictionary_ids": ["<string>"],
                "background_sound": {
                    "preset": "off",
                    "volume": 0.15,
                    "custom_asset_id": "<string>"
                }
            },
            "asr": {
                "multilingual": True,
                "strict_language": True,
                "keyterms": ["<string>"]
            },
            "conversation": {
                "max_duration_seconds": 1830,
                "response_wait_ms": 1150,
                "response_max_wait_ms": 2000,
                "interruptible": True,
                "interruption_ignore_phrases": ["<string>"],
                "backchannel": {
                    "enabled": True,
                    "strength": 5
                },
                "speculative_response": True,
                "reengage": {
                    "enabled": True,
                    "steps": [
                        {
                            "after_seconds": 301,
                            "message": ""
                        }
                    ],
                    "exhausted_after_seconds": 301,
                    "schedule": {
                        "first_seconds": 301,
                        "interval_seconds": 301,
                        "count": 5,
                        "messages": ["<string>"]
                    }
                },
                "hangup_after_seconds": 1805,
                "hangup_farewell_message": "<string>",
                "record_audio": True,
                "timezone": "<string>",
                "transfer_destinations": [
                    {
                        "type": "phone",
                        "label": "",
                        "phone_number": "<string>",
                        "sip_uri": "<string>",
                        "headers": {},
                        "description": "",
                        "mode": "cold",
                        "warm_connect": "confirm",
                        "warm_briefing_instructions": "",
                        "warm_briefing_speed": 1.25,
                        "warm_ring_timeout_seconds": 30,
                        "warm_confirm_timeout_seconds": 60,
                        "warm_human_detection": False,
                        "warm_consult_uses_agent_settings": True,
                        "on_failure": {
                            "action": "return_to_agent",
                            "message": ""
                        },
                        "announcement_mode": "generated",
                        "announcement_message": "",
                        "auth_username": "<string>",
                        "auth_password": "<string>"
                    }
                ],
                "transfer_refuse_questions": True,
                "outbound": {
                    "amd_enabled": True,
                    "voicemail": {
                        "action": "hangup",
                        "message": ""
                    }
                },
                "keypad_menu": {
                    "enabled": False,
                    "prompt": "",
                    "options": [],
                    "accept_speech": True,
                    "variable": "menu_choice",
                    "no_input_timeout_seconds": 5,
                    "max_attempts": 2,
                    "retry_message": "",
                    "fallback_value": ""
                },
                "keypad_input": {
                    "enabled": False,
                    "terminator": "#",
                    "inter_digit_timeout_seconds": 2
                },
                "echo_guard": {
                    "web_voice": True,
                    "phone_inbound": True,
                    "phone_outbound": True
                },
                "turn_detector": {}
            },
            "tools": {
                "enabled": True,
                "tool_ids": ["<string>"],
                "system_tools": {
                    "hang_up_call": True,
                    "hang_up_call_farewell_message": "<string>",
                    "hang_up_call_refuse_questions": True
                }
            },
            "webhooks": {
                "conversation_init": {
                    "url": "<string>",
                    "secret": "<string>",
                    "keep_previous_secret_for_seconds": 302400,
                    "timeout_seconds": 5
                },
                "post_call": [
                    {
                        "url": "<string>",
                        "secret": "<string>",
                        "keep_previous_secret_for_seconds": 302400
                    }
                ]
            },
            "knowledge_base": {
                "enabled": True,
                "knowledge_source_ids": ["<string>"]
            },
            "analysis": {
                "summary": {
                    "enabled": True,
                    "prompt": "<string>",
                    "language": "en"
                },
                "data_fields": [
                    {
                        "name": "<string>",
                        "type": "text",
                        "description": "",
                        "enum_options": ["<string>"]
                    }
                ],
                "criteria": [
                    {
                        "name": "<string>",
                        "description": ""
                    }
                ]
            },
            "guardrails": {
                "focus": True,
                "manipulation": True,
                "pre_tool_speech": True
            },
            "context": { "current_time": True },
            "llm": {
                "custom": {
                    "base_url": "<string>",
                    "model": "<string>",
                    "api_key": "<string>",
                    "headers": {}
                },
                "fallback": {
                    "models": [
                        {
                            "custom": {
                                "base_url": "<string>",
                                "model": "<string>",
                                "api_key": "<string>",
                                "headers": {}
                            },
                            "ttft_timeout_ms": 15250,
                            "total_timeout_ms": 60500,
                            "parallel": { "kick_in_ms": 1500 }
                        }
                    ],
                    "primary": {
                        "ttft_timeout_ms": 15250,
                        "total_timeout_ms": 60500
                    }
                }
            },
            "variables": { "defaults": {} }
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
        name: '<string>',
        description: '',
        config: {
          prompt: {
            system_prompt: '<string>',
            first_message: '<string>',
            first_message_prompt: '<string>'
          },
          voice: {
            voice_id: '<string>',
            expressive: true,
            speed: 1.25,
            live3_prompt: '<string>',
            pronunciation_dictionary_ids: ['<string>'],
            background_sound: {preset: 'off', volume: 0.15, custom_asset_id: '<string>'}
          },
          asr: {multilingual: true, strict_language: true, keyterms: ['<string>']},
          conversation: {
            max_duration_seconds: 1830,
            response_wait_ms: 1150,
            response_max_wait_ms: 2000,
            interruptible: true,
            interruption_ignore_phrases: ['<string>'],
            backchannel: {enabled: true, strength: 5},
            speculative_response: true,
            reengage: {
              enabled: true,
              steps: [{after_seconds: 301, message: ''}],
              exhausted_after_seconds: 301,
              schedule: {first_seconds: 301, interval_seconds: 301, count: 5, messages: ['<string>']}
            },
            hangup_after_seconds: 1805,
            hangup_farewell_message: '<string>',
            record_audio: true,
            timezone: '<string>',
            transfer_destinations: [
              {
                type: 'phone',
                label: '',
                phone_number: '<string>',
                sip_uri: '<string>',
                headers: {},
                description: '',
                mode: 'cold',
                warm_connect: 'confirm',
                warm_briefing_instructions: '',
                warm_briefing_speed: 1.25,
                warm_ring_timeout_seconds: 30,
                warm_confirm_timeout_seconds: 60,
                warm_human_detection: false,
                warm_consult_uses_agent_settings: true,
                on_failure: {action: 'return_to_agent', message: ''},
                announcement_mode: 'generated',
                announcement_message: '',
                auth_username: '<string>',
                auth_password: '<string>'
              }
            ],
            transfer_refuse_questions: true,
            outbound: {amd_enabled: true, voicemail: {action: 'hangup', message: ''}},
            keypad_menu: {
              enabled: false,
              prompt: '',
              options: [],
              accept_speech: true,
              variable: 'menu_choice',
              no_input_timeout_seconds: 5,
              max_attempts: 2,
              retry_message: '',
              fallback_value: ''
            },
            keypad_input: {enabled: false, terminator: '#', inter_digit_timeout_seconds: 2},
            echo_guard: {web_voice: true, phone_inbound: true, phone_outbound: true},
            turn_detector: {}
          },
          tools: {
            enabled: true,
            tool_ids: ['<string>'],
            system_tools: {
              hang_up_call: true,
              hang_up_call_farewell_message: '<string>',
              hang_up_call_refuse_questions: true
            }
          },
          webhooks: {
            conversation_init: {
              url: '<string>',
              secret: '<string>',
              keep_previous_secret_for_seconds: 302400,
              timeout_seconds: 5
            },
            post_call: [
              {url: '<string>', secret: '<string>', keep_previous_secret_for_seconds: 302400}
            ]
          },
          knowledge_base: {enabled: true, knowledge_source_ids: ['<string>']},
          analysis: {
            summary: {enabled: true, prompt: '<string>', language: 'en'},
            data_fields: [{name: '<string>', type: 'text', description: '', enum_options: ['<string>']}],
            criteria: [{name: '<string>', description: ''}]
          },
          guardrails: {focus: true, manipulation: true, pre_tool_speech: true},
          context: {current_time: true},
          llm: {
            custom: {base_url: '<string>', model: '<string>', api_key: '<string>', headers: {}},
            fallback: {
              models: [
                {
                  custom: {base_url: '<string>', model: '<string>', api_key: '<string>', headers: {}},
                  ttft_timeout_ms: 15250,
                  total_timeout_ms: 60500,
                  parallel: {kick_in_ms: 1500}
                }
              ],
              primary: {ttft_timeout_ms: 15250, total_timeout_ms: 60500}
            }
          },
          variables: {defaults: {}}
        }
      })
    };
    
    fetch('https://api.fish.audio/v1/agent/agents', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_URL => "https://api.fish.audio/v1/agent/agents",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => json_encode([
        'name' => '<string>',
        'description' => '',
        'config' => [
            'prompt' => [
                    'system_prompt' => '<string>',
                    'first_message' => '<string>',
                    'first_message_prompt' => '<string>'
            ],
            'voice' => [
                    'voice_id' => '<string>',
                    'expressive' => true,
                    'speed' => 1.25,
                    'live3_prompt' => '<string>',
                    'pronunciation_dictionary_ids' => [
                                    '<string>'
                    ],
                    'background_sound' => [
                                    'preset' => 'off',
                                    'volume' => 0.15,
                                    'custom_asset_id' => '<string>'
                    ]
            ],
            'asr' => [
                    'multilingual' => true,
                    'strict_language' => true,
                    'keyterms' => [
                                    '<string>'
                    ]
            ],
            'conversation' => [
                    'max_duration_seconds' => 1830,
                    'response_wait_ms' => 1150,
                    'response_max_wait_ms' => 2000,
                    'interruptible' => true,
                    'interruption_ignore_phrases' => [
                                    '<string>'
                    ],
                    'backchannel' => [
                                    'enabled' => true,
                                    'strength' => 5
                    ],
                    'speculative_response' => true,
                    'reengage' => [
                                    'enabled' => true,
                                    'steps' => [
                                                                    [
                                                                                                                                    'after_seconds' => 301,
                                                                                                                                    'message' => ''
                                                                    ]
                                    ],
                                    'exhausted_after_seconds' => 301,
                                    'schedule' => [
                                                                    'first_seconds' => 301,
                                                                    'interval_seconds' => 301,
                                                                    'count' => 5,
                                                                    'messages' => [
                                                                                                                                    '<string>'
                                                                    ]
                                    ]
                    ],
                    'hangup_after_seconds' => 1805,
                    'hangup_farewell_message' => '<string>',
                    'record_audio' => true,
                    'timezone' => '<string>',
                    'transfer_destinations' => [
                                    [
                                                                    'type' => 'phone',
                                                                    'label' => '',
                                                                    'phone_number' => '<string>',
                                                                    'sip_uri' => '<string>',
                                                                    'headers' => [
                                                                                                                                    
                                                                    ],
                                                                    'description' => '',
                                                                    'mode' => 'cold',
                                                                    'warm_connect' => 'confirm',
                                                                    'warm_briefing_instructions' => '',
                                                                    'warm_briefing_speed' => 1.25,
                                                                    'warm_ring_timeout_seconds' => 30,
                                                                    'warm_confirm_timeout_seconds' => 60,
                                                                    'warm_human_detection' => false,
                                                                    'warm_consult_uses_agent_settings' => true,
                                                                    'on_failure' => [
                                                                                                                                    'action' => 'return_to_agent',
                                                                                                                                    'message' => ''
                                                                    ],
                                                                    'announcement_mode' => 'generated',
                                                                    'announcement_message' => '',
                                                                    'auth_username' => '<string>',
                                                                    'auth_password' => '<string>'
                                    ]
                    ],
                    'transfer_refuse_questions' => true,
                    'outbound' => [
                                    'amd_enabled' => true,
                                    'voicemail' => [
                                                                    'action' => 'hangup',
                                                                    'message' => ''
                                    ]
                    ],
                    'keypad_menu' => [
                                    'enabled' => false,
                                    'prompt' => '',
                                    'options' => [
                                                                    
                                    ],
                                    'accept_speech' => true,
                                    'variable' => 'menu_choice',
                                    'no_input_timeout_seconds' => 5,
                                    'max_attempts' => 2,
                                    'retry_message' => '',
                                    'fallback_value' => ''
                    ],
                    'keypad_input' => [
                                    'enabled' => false,
                                    'terminator' => '#',
                                    'inter_digit_timeout_seconds' => 2
                    ],
                    'echo_guard' => [
                                    'web_voice' => true,
                                    'phone_inbound' => true,
                                    'phone_outbound' => true
                    ],
                    'turn_detector' => [
                                    
                    ]
            ],
            'tools' => [
                    'enabled' => true,
                    'tool_ids' => [
                                    '<string>'
                    ],
                    'system_tools' => [
                                    'hang_up_call' => true,
                                    'hang_up_call_farewell_message' => '<string>',
                                    'hang_up_call_refuse_questions' => true
                    ]
            ],
            'webhooks' => [
                    'conversation_init' => [
                                    'url' => '<string>',
                                    'secret' => '<string>',
                                    'keep_previous_secret_for_seconds' => 302400,
                                    'timeout_seconds' => 5
                    ],
                    'post_call' => [
                                    [
                                                                    'url' => '<string>',
                                                                    'secret' => '<string>',
                                                                    'keep_previous_secret_for_seconds' => 302400
                                    ]
                    ]
            ],
            'knowledge_base' => [
                    'enabled' => true,
                    'knowledge_source_ids' => [
                                    '<string>'
                    ]
            ],
            'analysis' => [
                    'summary' => [
                                    'enabled' => true,
                                    'prompt' => '<string>',
                                    'language' => 'en'
                    ],
                    'data_fields' => [
                                    [
                                                                    'name' => '<string>',
                                                                    'type' => 'text',
                                                                    'description' => '',
                                                                    'enum_options' => [
                                                                                                                                    '<string>'
                                                                    ]
                                    ]
                    ],
                    'criteria' => [
                                    [
                                                                    'name' => '<string>',
                                                                    'description' => ''
                                    ]
                    ]
            ],
            'guardrails' => [
                    'focus' => true,
                    'manipulation' => true,
                    'pre_tool_speech' => true
            ],
            'context' => [
                    'current_time' => true
            ],
            'llm' => [
                    'custom' => [
                                    'base_url' => '<string>',
                                    'model' => '<string>',
                                    'api_key' => '<string>',
                                    'headers' => [
                                                                    
                                    ]
                    ],
                    'fallback' => [
                                    'models' => [
                                                                    [
                                                                                                                                    'custom' => [
                                                                                                                                                                                                                                                                    'base_url' => '<string>',
                                                                                                                                                                                                                                                                    'model' => '<string>',
                                                                                                                                                                                                                                                                    'api_key' => '<string>',
                                                                                                                                                                                                                                                                    'headers' => [
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                    ]
                                                                                                                                    ],
                                                                                                                                    'ttft_timeout_ms' => 15250,
                                                                                                                                    'total_timeout_ms' => 60500,
                                                                                                                                    'parallel' => [
                                                                                                                                                                                                                                                                    'kick_in_ms' => 1500
                                                                                                                                    ]
                                                                    ]
                                    ],
                                    'primary' => [
                                                                    'ttft_timeout_ms' => 15250,
                                                                    'total_timeout_ms' => 60500
                                    ]
                    ]
            ],
            'variables' => [
                    'defaults' => [
                                    
                    ]
            ]
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
    
    	url := "https://api.fish.audio/v1/agent/agents"
    
    	payload := strings.NewReader("{\n  \"name\": \"<string>\",\n  \"description\": \"\",\n  \"config\": {\n    \"prompt\": {\n      \"system_prompt\": \"<string>\",\n      \"first_message\": \"<string>\",\n      \"first_message_prompt\": \"<string>\"\n    },\n    \"voice\": {\n      \"voice_id\": \"<string>\",\n      \"expressive\": true,\n      \"speed\": 1.25,\n      \"live3_prompt\": \"<string>\",\n      \"pronunciation_dictionary_ids\": [\n        \"<string>\"\n      ],\n      \"background_sound\": {\n        \"preset\": \"off\",\n        \"volume\": 0.15,\n        \"custom_asset_id\": \"<string>\"\n      }\n    },\n    \"asr\": {\n      \"multilingual\": true,\n      \"strict_language\": true,\n      \"keyterms\": [\n        \"<string>\"\n      ]\n    },\n    \"conversation\": {\n      \"max_duration_seconds\": 1830,\n      \"response_wait_ms\": 1150,\n      \"response_max_wait_ms\": 2000,\n      \"interruptible\": true,\n      \"interruption_ignore_phrases\": [\n        \"<string>\"\n      ],\n      \"backchannel\": {\n        \"enabled\": true,\n        \"strength\": 5\n      },\n      \"speculative_response\": true,\n      \"reengage\": {\n        \"enabled\": true,\n        \"steps\": [\n          {\n            \"after_seconds\": 301,\n            \"message\": \"\"\n          }\n        ],\n        \"exhausted_after_seconds\": 301,\n        \"schedule\": {\n          \"first_seconds\": 301,\n          \"interval_seconds\": 301,\n          \"count\": 5,\n          \"messages\": [\n            \"<string>\"\n          ]\n        }\n      },\n      \"hangup_after_seconds\": 1805,\n      \"hangup_farewell_message\": \"<string>\",\n      \"record_audio\": true,\n      \"timezone\": \"<string>\",\n      \"transfer_destinations\": [\n        {\n          \"type\": \"phone\",\n          \"label\": \"\",\n          \"phone_number\": \"<string>\",\n          \"sip_uri\": \"<string>\",\n          \"headers\": {},\n          \"description\": \"\",\n          \"mode\": \"cold\",\n          \"warm_connect\": \"confirm\",\n          \"warm_briefing_instructions\": \"\",\n          \"warm_briefing_speed\": 1.25,\n          \"warm_ring_timeout_seconds\": 30,\n          \"warm_confirm_timeout_seconds\": 60,\n          \"warm_human_detection\": false,\n          \"warm_consult_uses_agent_settings\": true,\n          \"on_failure\": {\n            \"action\": \"return_to_agent\",\n            \"message\": \"\"\n          },\n          \"announcement_mode\": \"generated\",\n          \"announcement_message\": \"\",\n          \"auth_username\": \"<string>\",\n          \"auth_password\": \"<string>\"\n        }\n      ],\n      \"transfer_refuse_questions\": true,\n      \"outbound\": {\n        \"amd_enabled\": true,\n        \"voicemail\": {\n          \"action\": \"hangup\",\n          \"message\": \"\"\n        }\n      },\n      \"keypad_menu\": {\n        \"enabled\": false,\n        \"prompt\": \"\",\n        \"options\": [],\n        \"accept_speech\": true,\n        \"variable\": \"menu_choice\",\n        \"no_input_timeout_seconds\": 5,\n        \"max_attempts\": 2,\n        \"retry_message\": \"\",\n        \"fallback_value\": \"\"\n      },\n      \"keypad_input\": {\n        \"enabled\": false,\n        \"terminator\": \"#\",\n        \"inter_digit_timeout_seconds\": 2\n      },\n      \"echo_guard\": {\n        \"web_voice\": true,\n        \"phone_inbound\": true,\n        \"phone_outbound\": true\n      },\n      \"turn_detector\": {}\n    },\n    \"tools\": {\n      \"enabled\": true,\n      \"tool_ids\": [\n        \"<string>\"\n      ],\n      \"system_tools\": {\n        \"hang_up_call\": true,\n        \"hang_up_call_farewell_message\": \"<string>\",\n        \"hang_up_call_refuse_questions\": true\n      }\n    },\n    \"webhooks\": {\n      \"conversation_init\": {\n        \"url\": \"<string>\",\n        \"secret\": \"<string>\",\n        \"keep_previous_secret_for_seconds\": 302400,\n        \"timeout_seconds\": 5\n      },\n      \"post_call\": [\n        {\n          \"url\": \"<string>\",\n          \"secret\": \"<string>\",\n          \"keep_previous_secret_for_seconds\": 302400\n        }\n      ]\n    },\n    \"knowledge_base\": {\n      \"enabled\": true,\n      \"knowledge_source_ids\": [\n        \"<string>\"\n      ]\n    },\n    \"analysis\": {\n      \"summary\": {\n        \"enabled\": true,\n        \"prompt\": \"<string>\",\n        \"language\": \"en\"\n      },\n      \"data_fields\": [\n        {\n          \"name\": \"<string>\",\n          \"type\": \"text\",\n          \"description\": \"\",\n          \"enum_options\": [\n            \"<string>\"\n          ]\n        }\n      ],\n      \"criteria\": [\n        {\n          \"name\": \"<string>\",\n          \"description\": \"\"\n        }\n      ]\n    },\n    \"guardrails\": {\n      \"focus\": true,\n      \"manipulation\": true,\n      \"pre_tool_speech\": true\n    },\n    \"context\": {\n      \"current_time\": true\n    },\n    \"llm\": {\n      \"custom\": {\n        \"base_url\": \"<string>\",\n        \"model\": \"<string>\",\n        \"api_key\": \"<string>\",\n        \"headers\": {}\n      },\n      \"fallback\": {\n        \"models\": [\n          {\n            \"custom\": {\n              \"base_url\": \"<string>\",\n              \"model\": \"<string>\",\n              \"api_key\": \"<string>\",\n              \"headers\": {}\n            },\n            \"ttft_timeout_ms\": 15250,\n            \"total_timeout_ms\": 60500,\n            \"parallel\": {\n              \"kick_in_ms\": 1500\n            }\n          }\n        ],\n        \"primary\": {\n          \"ttft_timeout_ms\": 15250,\n          \"total_timeout_ms\": 60500\n        }\n      }\n    },\n    \"variables\": {\n      \"defaults\": {}\n    }\n  }\n}")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    	req.Header.Add("Content-Type", "application/json")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("https://api.fish.audio/v1/agent/agents")
      .header("Authorization", "Bearer <token>")
      .header("Content-Type", "application/json")
      .body("{\n  \"name\": \"<string>\",\n  \"description\": \"\",\n  \"config\": {\n    \"prompt\": {\n      \"system_prompt\": \"<string>\",\n      \"first_message\": \"<string>\",\n      \"first_message_prompt\": \"<string>\"\n    },\n    \"voice\": {\n      \"voice_id\": \"<string>\",\n      \"expressive\": true,\n      \"speed\": 1.25,\n      \"live3_prompt\": \"<string>\",\n      \"pronunciation_dictionary_ids\": [\n        \"<string>\"\n      ],\n      \"background_sound\": {\n        \"preset\": \"off\",\n        \"volume\": 0.15,\n        \"custom_asset_id\": \"<string>\"\n      }\n    },\n    \"asr\": {\n      \"multilingual\": true,\n      \"strict_language\": true,\n      \"keyterms\": [\n        \"<string>\"\n      ]\n    },\n    \"conversation\": {\n      \"max_duration_seconds\": 1830,\n      \"response_wait_ms\": 1150,\n      \"response_max_wait_ms\": 2000,\n      \"interruptible\": true,\n      \"interruption_ignore_phrases\": [\n        \"<string>\"\n      ],\n      \"backchannel\": {\n        \"enabled\": true,\n        \"strength\": 5\n      },\n      \"speculative_response\": true,\n      \"reengage\": {\n        \"enabled\": true,\n        \"steps\": [\n          {\n            \"after_seconds\": 301,\n            \"message\": \"\"\n          }\n        ],\n        \"exhausted_after_seconds\": 301,\n        \"schedule\": {\n          \"first_seconds\": 301,\n          \"interval_seconds\": 301,\n          \"count\": 5,\n          \"messages\": [\n            \"<string>\"\n          ]\n        }\n      },\n      \"hangup_after_seconds\": 1805,\n      \"hangup_farewell_message\": \"<string>\",\n      \"record_audio\": true,\n      \"timezone\": \"<string>\",\n      \"transfer_destinations\": [\n        {\n          \"type\": \"phone\",\n          \"label\": \"\",\n          \"phone_number\": \"<string>\",\n          \"sip_uri\": \"<string>\",\n          \"headers\": {},\n          \"description\": \"\",\n          \"mode\": \"cold\",\n          \"warm_connect\": \"confirm\",\n          \"warm_briefing_instructions\": \"\",\n          \"warm_briefing_speed\": 1.25,\n          \"warm_ring_timeout_seconds\": 30,\n          \"warm_confirm_timeout_seconds\": 60,\n          \"warm_human_detection\": false,\n          \"warm_consult_uses_agent_settings\": true,\n          \"on_failure\": {\n            \"action\": \"return_to_agent\",\n            \"message\": \"\"\n          },\n          \"announcement_mode\": \"generated\",\n          \"announcement_message\": \"\",\n          \"auth_username\": \"<string>\",\n          \"auth_password\": \"<string>\"\n        }\n      ],\n      \"transfer_refuse_questions\": true,\n      \"outbound\": {\n        \"amd_enabled\": true,\n        \"voicemail\": {\n          \"action\": \"hangup\",\n          \"message\": \"\"\n        }\n      },\n      \"keypad_menu\": {\n        \"enabled\": false,\n        \"prompt\": \"\",\n        \"options\": [],\n        \"accept_speech\": true,\n        \"variable\": \"menu_choice\",\n        \"no_input_timeout_seconds\": 5,\n        \"max_attempts\": 2,\n        \"retry_message\": \"\",\n        \"fallback_value\": \"\"\n      },\n      \"keypad_input\": {\n        \"enabled\": false,\n        \"terminator\": \"#\",\n        \"inter_digit_timeout_seconds\": 2\n      },\n      \"echo_guard\": {\n        \"web_voice\": true,\n        \"phone_inbound\": true,\n        \"phone_outbound\": true\n      },\n      \"turn_detector\": {}\n    },\n    \"tools\": {\n      \"enabled\": true,\n      \"tool_ids\": [\n        \"<string>\"\n      ],\n      \"system_tools\": {\n        \"hang_up_call\": true,\n        \"hang_up_call_farewell_message\": \"<string>\",\n        \"hang_up_call_refuse_questions\": true\n      }\n    },\n    \"webhooks\": {\n      \"conversation_init\": {\n        \"url\": \"<string>\",\n        \"secret\": \"<string>\",\n        \"keep_previous_secret_for_seconds\": 302400,\n        \"timeout_seconds\": 5\n      },\n      \"post_call\": [\n        {\n          \"url\": \"<string>\",\n          \"secret\": \"<string>\",\n          \"keep_previous_secret_for_seconds\": 302400\n        }\n      ]\n    },\n    \"knowledge_base\": {\n      \"enabled\": true,\n      \"knowledge_source_ids\": [\n        \"<string>\"\n      ]\n    },\n    \"analysis\": {\n      \"summary\": {\n        \"enabled\": true,\n        \"prompt\": \"<string>\",\n        \"language\": \"en\"\n      },\n      \"data_fields\": [\n        {\n          \"name\": \"<string>\",\n          \"type\": \"text\",\n          \"description\": \"\",\n          \"enum_options\": [\n            \"<string>\"\n          ]\n        }\n      ],\n      \"criteria\": [\n        {\n          \"name\": \"<string>\",\n          \"description\": \"\"\n        }\n      ]\n    },\n    \"guardrails\": {\n      \"focus\": true,\n      \"manipulation\": true,\n      \"pre_tool_speech\": true\n    },\n    \"context\": {\n      \"current_time\": true\n    },\n    \"llm\": {\n      \"custom\": {\n        \"base_url\": \"<string>\",\n        \"model\": \"<string>\",\n        \"api_key\": \"<string>\",\n        \"headers\": {}\n      },\n      \"fallback\": {\n        \"models\": [\n          {\n            \"custom\": {\n              \"base_url\": \"<string>\",\n              \"model\": \"<string>\",\n              \"api_key\": \"<string>\",\n              \"headers\": {}\n            },\n            \"ttft_timeout_ms\": 15250,\n            \"total_timeout_ms\": 60500,\n            \"parallel\": {\n              \"kick_in_ms\": 1500\n            }\n          }\n        ],\n        \"primary\": {\n          \"ttft_timeout_ms\": 15250,\n          \"total_timeout_ms\": 60500\n        }\n      }\n    },\n    \"variables\": {\n      \"defaults\": {}\n    }\n  }\n}")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("https://api.fish.audio/v1/agent/agents")
    
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request["Content-Type"] = 'application/json'
    request.body = "{\n  \"name\": \"<string>\",\n  \"description\": \"\",\n  \"config\": {\n    \"prompt\": {\n      \"system_prompt\": \"<string>\",\n      \"first_message\": \"<string>\",\n      \"first_message_prompt\": \"<string>\"\n    },\n    \"voice\": {\n      \"voice_id\": \"<string>\",\n      \"expressive\": true,\n      \"speed\": 1.25,\n      \"live3_prompt\": \"<string>\",\n      \"pronunciation_dictionary_ids\": [\n        \"<string>\"\n      ],\n      \"background_sound\": {\n        \"preset\": \"off\",\n        \"volume\": 0.15,\n        \"custom_asset_id\": \"<string>\"\n      }\n    },\n    \"asr\": {\n      \"multilingual\": true,\n      \"strict_language\": true,\n      \"keyterms\": [\n        \"<string>\"\n      ]\n    },\n    \"conversation\": {\n      \"max_duration_seconds\": 1830,\n      \"response_wait_ms\": 1150,\n      \"response_max_wait_ms\": 2000,\n      \"interruptible\": true,\n      \"interruption_ignore_phrases\": [\n        \"<string>\"\n      ],\n      \"backchannel\": {\n        \"enabled\": true,\n        \"strength\": 5\n      },\n      \"speculative_response\": true,\n      \"reengage\": {\n        \"enabled\": true,\n        \"steps\": [\n          {\n            \"after_seconds\": 301,\n            \"message\": \"\"\n          }\n        ],\n        \"exhausted_after_seconds\": 301,\n        \"schedule\": {\n          \"first_seconds\": 301,\n          \"interval_seconds\": 301,\n          \"count\": 5,\n          \"messages\": [\n            \"<string>\"\n          ]\n        }\n      },\n      \"hangup_after_seconds\": 1805,\n      \"hangup_farewell_message\": \"<string>\",\n      \"record_audio\": true,\n      \"timezone\": \"<string>\",\n      \"transfer_destinations\": [\n        {\n          \"type\": \"phone\",\n          \"label\": \"\",\n          \"phone_number\": \"<string>\",\n          \"sip_uri\": \"<string>\",\n          \"headers\": {},\n          \"description\": \"\",\n          \"mode\": \"cold\",\n          \"warm_connect\": \"confirm\",\n          \"warm_briefing_instructions\": \"\",\n          \"warm_briefing_speed\": 1.25,\n          \"warm_ring_timeout_seconds\": 30,\n          \"warm_confirm_timeout_seconds\": 60,\n          \"warm_human_detection\": false,\n          \"warm_consult_uses_agent_settings\": true,\n          \"on_failure\": {\n            \"action\": \"return_to_agent\",\n            \"message\": \"\"\n          },\n          \"announcement_mode\": \"generated\",\n          \"announcement_message\": \"\",\n          \"auth_username\": \"<string>\",\n          \"auth_password\": \"<string>\"\n        }\n      ],\n      \"transfer_refuse_questions\": true,\n      \"outbound\": {\n        \"amd_enabled\": true,\n        \"voicemail\": {\n          \"action\": \"hangup\",\n          \"message\": \"\"\n        }\n      },\n      \"keypad_menu\": {\n        \"enabled\": false,\n        \"prompt\": \"\",\n        \"options\": [],\n        \"accept_speech\": true,\n        \"variable\": \"menu_choice\",\n        \"no_input_timeout_seconds\": 5,\n        \"max_attempts\": 2,\n        \"retry_message\": \"\",\n        \"fallback_value\": \"\"\n      },\n      \"keypad_input\": {\n        \"enabled\": false,\n        \"terminator\": \"#\",\n        \"inter_digit_timeout_seconds\": 2\n      },\n      \"echo_guard\": {\n        \"web_voice\": true,\n        \"phone_inbound\": true,\n        \"phone_outbound\": true\n      },\n      \"turn_detector\": {}\n    },\n    \"tools\": {\n      \"enabled\": true,\n      \"tool_ids\": [\n        \"<string>\"\n      ],\n      \"system_tools\": {\n        \"hang_up_call\": true,\n        \"hang_up_call_farewell_message\": \"<string>\",\n        \"hang_up_call_refuse_questions\": true\n      }\n    },\n    \"webhooks\": {\n      \"conversation_init\": {\n        \"url\": \"<string>\",\n        \"secret\": \"<string>\",\n        \"keep_previous_secret_for_seconds\": 302400,\n        \"timeout_seconds\": 5\n      },\n      \"post_call\": [\n        {\n          \"url\": \"<string>\",\n          \"secret\": \"<string>\",\n          \"keep_previous_secret_for_seconds\": 302400\n        }\n      ]\n    },\n    \"knowledge_base\": {\n      \"enabled\": true,\n      \"knowledge_source_ids\": [\n        \"<string>\"\n      ]\n    },\n    \"analysis\": {\n      \"summary\": {\n        \"enabled\": true,\n        \"prompt\": \"<string>\",\n        \"language\": \"en\"\n      },\n      \"data_fields\": [\n        {\n          \"name\": \"<string>\",\n          \"type\": \"text\",\n          \"description\": \"\",\n          \"enum_options\": [\n            \"<string>\"\n          ]\n        }\n      ],\n      \"criteria\": [\n        {\n          \"name\": \"<string>\",\n          \"description\": \"\"\n        }\n      ]\n    },\n    \"guardrails\": {\n      \"focus\": true,\n      \"manipulation\": true,\n      \"pre_tool_speech\": true\n    },\n    \"context\": {\n      \"current_time\": true\n    },\n    \"llm\": {\n      \"custom\": {\n        \"base_url\": \"<string>\",\n        \"model\": \"<string>\",\n        \"api_key\": \"<string>\",\n        \"headers\": {}\n      },\n      \"fallback\": {\n        \"models\": [\n          {\n            \"custom\": {\n              \"base_url\": \"<string>\",\n              \"model\": \"<string>\",\n              \"api_key\": \"<string>\",\n              \"headers\": {}\n            },\n            \"ttft_timeout_ms\": 15250,\n            \"total_timeout_ms\": 60500,\n            \"parallel\": {\n              \"kick_in_ms\": 1500\n            }\n          }\n        ],\n        \"primary\": {\n          \"ttft_timeout_ms\": 15250,\n          \"total_timeout_ms\": 60500\n        }\n      }\n    },\n    \"variables\": {\n      \"defaults\": {}\n    }\n  }\n}"
    
    response = http.request(request)
    puts response.read_body

201

401

403

422

503
    
    
    {
      "agent_id": "<string>",
      "workspace_id": "<string>",
      "name": "<string>",
      "status": "active",
      "publication_state": "live",
      "created_at": "2023-11-07T05:31:56Z",
      "updated_at": "2023-11-07T05:31:56Z",
      "description": "",
      "public_enabled": false,
      "allowed_origins": [
        "<string>"
      ],
      "restrict_origins": false,
      "overrides_allowed": [
        "first_message"
      ]
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

#### Body

application/json

name

string

required

Required string length: `1 - 120`

description

string

default:""

Maximum string length: `2000`

config

PublicAgentConfigPatchPayload · object | null

Optional initial draft configuration, applied atop the platform defaults; one call provisions a fully configured agent.

Show child attributes

#### Response

201

application/json

Document created, URL follows

agent_id

string

required

workspace_id

string

required

name

string

required

status

enum<string>

required

Available options: 

`active`, 

`archived`

publication_state

enum<string>

required

`live` once at least one version is published; `draft` agents cannot take sessions yet.

Available options: 

`live`, 

`draft`

created_at

string<date-time>

required

updated_at

string<date-time>

required

description

string

default:""

public_enabled

boolean

default:false

allowed_origins

string[]

restrict_origins

boolean

default:false

Whether public access is limited to `allowed_origins`. When false, any origin can start a public session.

overrides_allowed

enum<string>[]

Available options: 

`first_message`, 

`system_prompt`, 

`voice_id`, 

`language`, 

`asr.model`, 

`llm.fallback`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/agent/create-agent.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/agent/create-agent)

[List Agents](https://docs.fish.audio/api-reference/endpoint/agent/list-agents)[Get Agent](https://docs.fish.audio/api-reference/endpoint/agent/get-agent)
