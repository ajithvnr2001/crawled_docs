---
url: https://docs.comfy.org/specs/workflow_json/
title: Workflow JSON - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:13.453574+00:00
---

# Workflow JSON - ComfyUI

> Source: https://docs.comfy.org/specs/workflow_json/

## On this page

  * Version 1.0 (Latest)
  * Older versions



Workflow JSON

# Workflow JSON

Copy pageCopy page

Workflow JSON schema for the ComfyUI workflow file format (v1.0 plus legacy v0.4), covering nodes, links, groups, and version fields.

Copy pageCopy page

The workflow JSON is defined using [JSON Schema](https://json-schema.org/). Changes to this schema will be discussed in the [rfcs repo](https://github.com/comfy-org/rfcs).

## 

​

Version 1.0 (Latest)

ComfyUI Workflow v1.0
    
    
    {
      "$ref": "#/definitions/ComfyWorkflow1_0",
      "definitions": {
        "ComfyWorkflow1_0": {
          "type": "object",
          "properties": {
            "version": {
              "type": "number",
              "const": 1
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
            "state": {
              "type": "object",
              "properties": {
                "lastGroupid": {
                  "type": "number"
                },
                "lastNodeId": {
                  "type": "number"
                },
                "lastLinkId": {
                  "type": "number"
                },
                "lastRerouteId": {
                  "type": "number"
                }
              },
              "additionalProperties": true
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
                "type": "object",
                "properties": {
                  "id": {
                    "type": "number"
                  },
                  "origin_id": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "origin_slot": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "target_id": {
                    "anyOf": [
                      {
                        "type": "integer"
                      },
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "target_slot": {
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
                  "parentId": {
                    "type": "number"
                  }
                },
                "required": [
                  "id",
                  "origin_id",
                  "origin_slot",
                  "target_id",
                  "target_slot",
                  "type"
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
            "version",
            "state",
            "nodes"
          ],
          "additionalProperties": true
        }
      },
      "$schema": "http://json-schema.org/draft-07/schema#"
    }
    

## 

​

Older versions

  * [0.4](https://docs.comfy.org/specs/workflow_json/workflow_json_0.4)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/specs/workflow_json.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/specs/workflow_json)

[Comfy CLI Troubleshooting GuidePrevious](https://docs.comfy.org/comfy-cli/troubleshooting)[Workflow JSON 0.4Next](https://docs.comfy.org/specs/workflow_json_0.4)

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
