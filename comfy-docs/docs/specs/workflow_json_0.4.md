---
url: https://docs.comfy.org/specs/workflow_json_0.4
title: Workflow JSON 0.4 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:13.835789+00:00
---

# Workflow JSON 0.4 - ComfyUI

> Source: https://docs.comfy.org/specs/workflow_json_0.4

## On this page

  * v0.4



Workflow JSON

# Workflow JSON 0.4

Copy pageCopy page

JSON schema for a ComfyUI workflow.

Copy pageCopy page

## 

​

v0.4
    
    
    {
      "$ref": "#/definitions/ComfyWorkflow0_4",
      "definitions": {
        "ComfyWorkflow0_4": {
          "type": "object",
          "properties": {
            "last_node_id": {
              "anyOf": [
                {
                  "type": "integer"
                },
                {
                  "type": "string"
                }
              ]
            },
            "last_link_id": {
              "type": "number"
            },
            "nodes": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "type": {
                    "type": "string"
                  },
                  "pos": {
                    "anyOf": [
                      {
                        "type": "object",
                        "properties": {
                          "0": {
                            "type": "number"
                          },
                          "1": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "0",
                          "1"
                        ],
                        "additionalProperties": true
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "number"
                          },
                          {
                            "type": "number"
                          }
                        ]
                      }
                    ]
                  },
                  "size": {
                    "anyOf": [
                      {
                        "type": "object",
                        "properties": {
                          "0": {
                            "type": "number"
                          },
                          "1": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "0",
                          "1"
                        ],
                        "additionalProperties": true
                      },
                      {
                        "type": "array",
                        "minItems": 2,
                        "maxItems": 2,
                        "items": [
                          {
                            "type": "number"
                          },
                          {
                            "type": "number"
                          }
                        ]
                      }
                    ]
                  },
                  "flags": {
                    "type": "object",
                    "properties": {
                      "collapsed": {
                        "type": "boolean"
                      },
                      "pinned": {
                        "type": "boolean"
                      },
                      "allow_interaction": {
                        "type": "boolean"
                      },
                      "horizontal": {
                        "type": "boolean"
                      },
                      "skip_repeated_outputs": {
                        "type": "boolean"
                      }
                    },
                    "additionalProperties": true
                  },
                  "order": {
                    "type": "number"
                  },
                  "mode": {
                    "type": "number"
                  },
                  "inputs": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "type": {
                          "anyOf": [
                            {
                              "type": "string"
                            },
                            {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            {
                              "type": "number"
                            }
                          ]
                        },
                        "link": {
                          "type": [
                            "number",
                            "null"
                          ]
                        },
                        "slot_index": {
                          "anyOf": [
                            {
                              "type": "integer"
                            },
                            {
                              "type": "string"
                            }
                          ]
                        }
                      },
                      "required": [
                        "name",
                        "type"
                      ],
                      "additionalProperties": true
                    }
                  },
                  "outputs": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "type": {
                          "anyOf": [
                            {
                              "type": "string"
                            },
                            {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            {
                              "type": "number"
                            }
                          ]
                        },
                        "links": {
                          "anyOf": [
                            {
                              "type": "array",
                              "items": {
                                "type": "number"
                              }
                            },
                            {
                              "type": "null"
                            }
                          ]
                        },
                        "slot_index": {
                          "anyOf": [
                            {
                              "type": "integer"
                            },
                            {
                              "type": "string"
                            }
                          ]
                        }
                      },
                      "required": [
                        "name",
                        "type"
                      ],
                      "additionalProperties": true
                    }
                  },
                  "properties": {
                    "type": "object",
                    "properties": {
                      "Node name for S&R": {
                        "type": "string"
                      }
                    },
                    "additionalProperties": true
                  },
                  "widgets_values": {
                    "anyOf": [
                      {
                        "type": "array"
                      },
                      {
                        "type": "object",
                        "additionalProperties": {}
                      }
                    ]
                  },
                  "color": {
                    "type": "string"
                  },
                  "bgcolor": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "type",
                  "pos",
                  "size",
                  "flags",
                  "order",
                  "mode",
                  "properties"
                ],
                "additionalProperties": true
              }
            },
            "links": {
              "type": "array",
              "items": {
                "type": "array",
                "minItems": 6,
                "maxItems": 6,
                "items": [
                  {
                    "type": "number"
                  },
                  {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  {
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "number"
                      }
                    ]
                  }
                ]
              }
            },
            "groups": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "string"
                  },
                  "bounding": {
                    "type": "array",
                    "minItems": 4,
                    "maxItems": 4,
                    "items": [
                      {
                        "type": "number"
                      },
                      {
                        "type": "number"
                      },
                      {
                        "type": "number"
                      },
                      {
                        "type": "number"
                      }
                    ]
                  },
                  "color": {
                    "type": "string"
                  },
                  "font_size": {
                    "type": "number"
                  },
                  "locked": {
                    "type": "boolean"
                  }
                },
                "required": [
                  "title",
                  "bounding"
                ],
                "additionalProperties": true
              }
            },
            "config": {
              "anyOf": [
                {
                  "anyOf": [
                    {
                      "not": {}
                    },
                    {
                      "type": "object",
                      "properties": {
                        "links_ontop": {
                          "type": "boolean"
                        },
                        "align_to_grid": {
                          "type": "boolean"
                        }
                      },
                      "additionalProperties": true
                    }
                  ]
                },
                {
                  "type": "null"
                }
              ]
            },
            "extra": {
              "anyOf": [
                {
                  "anyOf": [
                    {
                      "not": {}
                    },
                    {
                      "type": "object",
                      "properties": {
                        "ds": {
                          "type": "object",
                          "properties": {
                            "scale": {
                              "type": "number"
                            },
                            "offset": {
                              "anyOf": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "0": {
                                      "type": "number"
                                    },
                                    "1": {
                                      "type": "number"
                                    }
                                  },
                                  "required": [
                                    "0",
                                    "1"
                                  ],
                                  "additionalProperties": true
                                },
                                {
                                  "type": "array",
                                  "minItems": 2,
                                  "maxItems": 2,
                                  "items": [
                                    {
                                      "type": "number"
                                    },
                                    {
                                      "type": "number"
                                    }
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "scale",
                            "offset"
                          ],
                          "additionalProperties": true
                        },
                        "info": {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "string"
                            },
                            "author": {
                              "type": "string"
                            },
                            "description": {
                              "type": "string"
                            },
                            "version": {
                              "type": "string"
                            },
                            "created": {
                              "type": "string"
                            },
                            "modified": {
                              "type": "string"
                            },
                            "software": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "name",
                            "author",
                            "description",
                            "version",
                            "created",
                            "modified",
                            "software"
                          ],
                          "additionalProperties": true
                        },
                        "linkExtensions": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "number"
                              },
                              "parentId": {
                                "type": "number"
                              }
                            },
                            "required": [
                              "id",
                              "parentId"
                            ],
                            "additionalProperties": true
                          }
                        },
                        "reroutes": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "number"
                              },
                              "parentId": {
                                "type": "number"
                              },
                              "pos": {
                                "anyOf": [
                                  {
                                    "type": "object",
                                    "properties": {
                                      "0": {
                                        "type": "number"
                                      },
                                      "1": {
                                        "type": "number"
                                      }
                                    },
                                    "required": [
                                      "0",
                                      "1"
                                    ],
                                    "additionalProperties": true
                                  },
                                  {
                                    "type": "array",
                                    "minItems": 2,
                                    "maxItems": 2,
                                    "items": [
                                      {
                                        "type": "number"
                                      },
                                      {
                                        "type": "number"
                                      }
                                    ]
                                  }
                                ]
                              },
                              "linkIds": {
                                "anyOf": [
                                  {
                                    "type": "array",
                                    "items": {
                                      "type": "number"
                                    }
                                  },
                                  {
                                    "type": "null"
                                  }
                                ]
                              }
                            },
                            "required": [
                              "id",
                              "pos"
                            ],
                            "additionalProperties": true
                          }
                        }
                      },
                      "additionalProperties": true
                    }
                  ]
                },
                {
                  "type": "null"
                }
              ]
            },
            "version": {
              "type": "number"
            },
            "models": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "url": {
                    "type": "string",
                    "format": "uri"
                  },
                  "hash": {
                    "type": "string"
                  },
                  "hash_type": {
                    "type": "string"
                  },
                  "directory": {
                    "type": "string"
                  }
                },
                "required": [
                  "name",
                  "url",
                  "directory"
                ],
                "additionalProperties": false
              }
            }
          },
          "required": [
            "last_node_id",
            "last_link_id",
            "nodes",
            "links",
            "version"
          ],
          "additionalProperties": true
        }
      },
      "$schema": "http://json-schema.org/draft-07/schema#"
    }
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/specs/workflow_json_0.4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/specs/workflow_json_0.4)

[Workflow JSONPrevious](https://docs.comfy.org/specs/workflow_json)[Node Definition JSONNext](https://docs.comfy.org/specs/nodedef_json)

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
