---
url: https://docs.comfy.org/es/specs/nodedef_json/
title: JSON de definici\u00f3n de nodo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.574664+00:00
---

# JSON de definición de nodo - ComfyUI

> Source: https://docs.comfy.org/es/specs/nodedef_json/

## En esta página

Volver arriba

  * v2.0 (más reciente)



Node Definitions

# JSON de definición de nodo

Copiar páginaCopiar página

Esquema JSON de la definición de un nodo de ComfyUI.

Copiar páginaCopiar página

El JSON de definición de nodo se define con [JSON Schema](https://json-schema.org/). Los cambios en este esquema se tratarán en el [repositorio de rfcs](https://github.com/comfy-org/rfcs).

## 

​

v2.0 (más reciente)

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
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/specs/nodedef_json.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/specs/nodedef_json)

[Workflow JSON 0.4](https://docs.comfy.org/es/specs/workflow_json_0.4)[JSON de definición de nodo 1.0](https://docs.comfy.org/es/specs/nodedef_json_1_0)
