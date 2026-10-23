---
url: https://docs.comfy.org/specs/nodedef_json/
title: Node Definition JSON - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:12.968183+00:00
---

# Node Definition JSON - ComfyUI

> Source: https://docs.comfy.org/specs/nodedef_json/

## On this page

  * v2.0 (Latest)



Node Definitions

# Node Definition JSON

Copy pageCopy page

JSON schema for a ComfyUI Node.

Copy pageCopy page

The node definition JSON is defined using [JSON Schema](https://json-schema.org/). Changes to this schema will be discussed in the [rfcs repo](https://github.com/comfy-org/rfcs).

## 

​

v2.0 (Latest)

Node Definition v2.0
    
    
    {
      "$ref": "#/definitions/ComfyNodeDefV2",
      "definitions": {
        "ComfyNodeDefV2": {
          "type": "object",
          "properties": {
            "inputs": {
              "type": "object",
              "additionalProperties": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "default": {
                        "anyOf": [
                          {
                            "type": "number"
                          },
                          {
                            "type": "array",
                            "items": {
                              "type": "number"
                            }
                          }
                        ]
                      },
                      "defaultInput": {
                        "type": "boolean"
                      },
                      "forceInput": {
                        "type": "boolean"
                      },
                      "tooltip": {
                        "type": "string"
                      },
                      "hidden": {
                        "type": "boolean"
                      },
                      "advanced": {
                        "type": "boolean"
                      },
                      "rawLink": {
                        "type": "boolean"
                      },
                      "lazy": {
                        "type": "boolean"
                      },
                      "min": {
                        "type": "number"
                      },
                      "max": {
                        "type": "number"
                      },
                      "step": {
                        "type": "number"
                      },
                      "display": {
                        "type": "string",
                        "enum": [
                          "slider",
                          "number",
                          "knob"
                        ]
                      },
                      "control_after_generate": {
                        "type": "boolean"
                      },
                      "type": {
                        "type": "string",
                        "const": "INT"
                      },
                      "name": {
                        "type": "string"
                      },
                      "isOptional": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "name"
                    ],
                    "additionalProperties": true
                  },
                  {
                    "type": "object",
                    "properties": {
                      "default": {
                        "anyOf": [
                          {
                            "type": "number"
                          },
                          {
                            "type": "array",
                            "items": {
                              "type": "number"
                            }
                          }
                        ]
                      },
                      "defaultInput": {
                        "type": "boolean"
                      },
                      "forceInput": {
                        "type": "boolean"
                      },
                      "tooltip": {
                        "type": "string"
                      },
                      "hidden": {
                        "type": "boolean"
                      },
                      "advanced": {
                        "type": "boolean"
                      },
                      "rawLink": {
                        "type": "boolean"
                      },
                      "lazy": {
                        "type": "boolean"
                      },
                      "min": {
                        "type": "number"
                      },
                      "max": {
                        "type": "number"
                      },
                      "step": {
                        "type": "number"
                      },
                      "display": {
                        "type": "string",
                        "enum": [
                          "slider",
                          "number",
                          "knob"
                        ]
                      },
                      "round": {
                        "anyOf": [
                          {
                            "type": "number"
                          },
                          {
                            "type": "boolean",
                            "const": false
                          }
                        ]
                      },
                      "type": {
                        "type": "string",
                        "const": "FLOAT"
                      },
                      "name": {
                        "type": "string"
                      },
                      "isOptional": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "name"
                    ],
                    "additionalProperties": true
                  },
                  {
                    "type": "object",
                    "properties": {
                      "default": {
                        "type": "boolean"
                      },
                      "defaultInput": {
                        "type": "boolean"
                      },
                      "forceInput": {
                        "type": "boolean"
                      },
                      "tooltip": {
                        "type": "string"
                      },
                      "hidden": {
                        "type": "boolean"
                      },
                      "advanced": {
                        "type": "boolean"
                      },
                      "rawLink": {
                        "type": "boolean"
                      },
                      "lazy": {
                        "type": "boolean"
                      },
                      "label_on": {
                        "type": "string"
                      },
                      "label_off": {
                        "type": "string"
                      },
                      "type": {
                        "type": "string",
                        "const": "BOOLEAN"
                      },
                      "name": {
                        "type": "string"
                      },
                      "isOptional": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "name"
                    ],
                    "additionalProperties": true
                  },
                  {
                    "type": "object",
                    "properties": {
                      "default": {
                        "type": "string"
                      },
                      "defaultInput": {
                        "type": "boolean"
                      },
                      "forceInput": {
                        "type": "boolean"
                      },
                      "tooltip": {
                        "type": "string"
                      },
                      "hidden": {
                        "type": "boolean"
                      },
                      "advanced": {
                        "type": "boolean"
                      },
                      "rawLink": {
                        "type": "boolean"
                      },
                      "lazy": {
                        "type": "boolean"
                      },
                      "multiline": {
                        "type": "boolean"
                      },
                      "dynamicPrompts": {
                        "type": "boolean"
                      },
                      "defaultVal": {
                        "type": "string"
                      },
                      "placeholder": {
                        "type": "string"
                      },
                      "type": {
                        "type": "string",
                        "const": "STRING"
                      },
                      "name": {
                        "type": "string"
                      },
                      "isOptional": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "name"
                    ],
                    "additionalProperties": true
                  },
                  {
                    "type": "object",
                    "properties": {
                      "default": {},
                      "defaultInput": {
                        "type": "boolean"
                      },
                      "forceInput": {
                        "type": "boolean"
                      },
                      "tooltip": {
                        "type": "string"
                      },
                      "hidden": {
                        "type": "boolean"
                      },
                      "advanced": {
                        "type": "boolean"
                      },
                      "rawLink": {
                        "type": "boolean"
                      },
                      "lazy": {
                        "type": "boolean"
                      },
                      "control_after_generate": {
                        "type": "boolean"
                      },
                      "image_upload": {
                        "type": "boolean"
                      },
                      "image_folder": {
                        "type": "string",
                        "enum": [
                          "input",
                          "output",
                          "temp"
                        ]
                      },
                      "allow_batch": {
                        "type": "boolean"
                      },
                      "video_upload": {
                        "type": "boolean"
                      },
                      "remote": {
                        "type": "object",
                        "properties": {
                          "route": {
                            "anyOf": [
                              {
                                "type": "string",
                                "format": "uri"
                              },
                              {
                                "type": "string",
                                "pattern": "^\\/"
                              }
                            ]
                          },
                          "refresh": {
                            "anyOf": [
                              {
                                "type": "number",
                                "minimum": -9007199254740991,
                                "maximum": 9007199254740991
                              },
                              {
                                "type": "number",
                                "maximum": 9007199254740991,
                                "minimum": -9007199254740991
                              }
                            ]
                          },
                          "response_key": {
                            "type": "string"
                          },
                          "query_params": {
                            "type": "object",
                            "additionalProperties": {
                              "type": "string"
                            }
                          },
                          "refresh_button": {
                            "type": "boolean"
                          },
                          "control_after_refresh": {
                            "type": "string",
                            "enum": [
                              "first",
                              "last"
                            ]
                          },
                          "timeout": {
                            "type": "number",
                            "minimum": 0
                          },
                          "max_retries": {
                            "type": "number",
                            "minimum": 0
                          }
                        },
                        "required": [
                          "route"
                        ],
                        "additionalProperties": false
                      },
                      "options": {
                        "type": "array",
                        "items": {
                          "type": [
                            "string",
                            "number"
                          ]
                        }
                      },
                      "type": {
                        "type": "string",
                        "const": "COMBO"
                      },
                      "name": {
                        "type": "string"
                      },
                      "isOptional": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "name"
                    ],
                    "additionalProperties": true
                  },
                  {
                    "type": "object",
                    "properties": {
                      "default": {},
                      "defaultInput": {
                        "type": "boolean"
                      },
                      "forceInput": {
                        "type": "boolean"
                      },
                      "tooltip": {
                        "type": "string"
                      },
                      "hidden": {
                        "type": "boolean"
                      },
                      "advanced": {
                        "type": "boolean"
                      },
                      "rawLink": {
                        "type": "boolean"
                      },
                      "lazy": {
                        "type": "boolean"
                      },
                      "type": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "isOptional": {
                        "type": "boolean"
                      }
                    },
                    "required": [
                      "type",
                      "name"
                    ],
                    "additionalProperties": true
                  }
                ]
              }
            },
            "outputs": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "index": {
                    "type": "number"
                  },
                  "name": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string"
                  },
                  "is_list": {
                    "type": "boolean"
                  },
                  "options": {
                    "type": "array"
                  },
                  "tooltip": {
                    "type": "string"
                  }
                },
                "required": [
                  "index",
                  "name",
                  "type",
                  "is_list"
                ],
                "additionalProperties": false
              }
            },
            "hidden": {
              "type": "object",
              "additionalProperties": {}
            },
            "name": {
              "type": "string"
            },
            "display_name": {
              "type": "string"
            },
            "description": {
              "type": "string"
            },
            "category": {
              "type": "string"
            },
            "output_node": {
              "type": "boolean"
            },
            "python_module": {
              "type": "string"
            },
            "deprecated": {
              "type": "boolean"
            },
            "experimental": {
              "type": "boolean"
            }
          },
          "required": [
            "inputs",
            "outputs",
            "name",
            "display_name",
            "description",
            "category",
            "output_node",
            "python_module"
          ],
          "additionalProperties": false
        }
      },
      "$schema": "http://json-schema.org/draft-07/schema#"
    }
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/specs/nodedef_json.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/specs/nodedef_json)

[Workflow JSON 0.4Previous](https://docs.comfy.org/specs/workflow_json_0.4)[Node Definition JSON 1.0Next](https://docs.comfy.org/specs/nodedef_json_1_0)

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
