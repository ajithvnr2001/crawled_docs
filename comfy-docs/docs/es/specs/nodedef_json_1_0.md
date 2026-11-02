---
url: https://docs.comfy.org/es/specs/nodedef_json_1_0/
title: JSON de definici\u00f3n de nodo 1.0 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.358109+00:00
---

# JSON de definición de nodo 1.0 - ComfyUI

> Source: https://docs.comfy.org/es/specs/nodedef_json_1_0/

## En esta página

Volver arriba

  * v1.0



Node Definitions

# JSON de definición de nodo 1.0

Copiar páginaCopiar página

Esquema JSON de la definición de un nodo de ComfyUI.

Copiar páginaCopiar página

## 

​

v1.0

Node Definition v1.0
    
    
    {
      "$ref": "#/definitions/ComfyNodeDefV1",
      "definitions": {
        "ComfyNodeDefV1": {
          "type": "object",
          "properties": {
            "input": {
              "type": "object",
              "properties": {
                "required": {
                  "type": "object",
                  "additionalProperties": {
                    "anyOf": [
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "INT"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  "control_after_generate": {
                                    "type": "boolean"
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "FLOAT"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "BOOLEAN"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "STRING"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "array",
                            "items": {
                              "type": [
                                "string",
                                "number"
                              ]
                            }
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "COMBO"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                },
                "optional": {
                  "type": "object",
                  "additionalProperties": {
                    "anyOf": [
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "INT"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  "control_after_generate": {
                                    "type": "boolean"
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "FLOAT"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "BOOLEAN"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "STRING"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "array",
                            "items": {
                              "type": [
                                "string",
                                "number"
                              ]
                            }
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string",
                            "const": "COMBO"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "string"
                          },
                          {
                            "anyOf": [
                              {
                                "not": {}
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
                                  }
                                },
                                "additionalProperties": true
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                },
                "hidden": {
                  "type": "object",
                  "additionalProperties": {}
                }
              },
              "additionalProperties": false
            },
            "output": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "array",
                    "items": {
                      "type": [
                        "string",
                        "number"
                      ]
                    }
                  }
                ]
              }
            },
            "output_is_list": {
              "type": "array",
              "items": {
                "type": "boolean"
              }
            },
            "output_name": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "output_tooltips": {
              "type": "array",
              "items": {
                "type": "string"
              }
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/specs/nodedef_json_1_0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/specs/nodedef_json_1_0)

[JSON de definición de nodo](https://docs.comfy.org/es/specs/nodedef_json)[Descripción general](https://docs.comfy.org/es/custom-nodes/intro)
