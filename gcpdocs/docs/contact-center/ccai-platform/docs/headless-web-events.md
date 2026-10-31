---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-events/
title: Headless web SDK events \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T06:00:18.303280+00:00
---

# Headless web SDK events  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless web SDK events Stay organized with collections  Save and categorize content based on your preferences. 

The headless web SDK provides events that you can listen to in order to handle specific actions or updates within your application.
    
    
    const handleReady = () => {
      console.log("**** client is ready")
    }
    
    client.on("ready", handleReady)
    
    // client.off("ready", handleReady)
    

## General events

The following are general events for the SDK

### `ready`

Emitted when the client is ready for communication.
    
    
    client.on("ready", () => {
    })
    

### `authenticated`

Emitted when the client has authenticated with the user's token.
    
    
    client.on("authenticated", () => {
    })
    

## All available events

The SDK provides various events that you can listen to in order to handle specific actions or updates within your application.

You can add and remove event listeners using the `.on` and `.off` methods.
    
    
    const handleReady = () => {
      console.log(" client is ready")
    }
    client.on("ready", handleReady)
    // client.off("ready", handleReady)
    

Here is a comprehensive list of all available events:

### Global events

Event name | Description  
---|---  
`ready` | Emitted when client is ready for communication  
  
### Deprecated events

The SDK continues to emit the following events for backward compatibility. Don't use them in new integrations.

Event name | Description | Guidance  
---|---|---  
`authenticated` | Emitted when client has authenticated with the user's token | Deprecated and scheduled for removal. Existing integrations can continue to receive it until removal.  
`chat.connected` | Emitted when the chat is connected with provider. | Deprecated. Use `chat.connectedMessages`, which also provides the initial messages payload.  
  
### Chat events

Event name | Description  
---|---  
`chat.ongoing` | Emitted when there is an ongoing chat.  
`chat.updated` | Emitted when the chat instance has updated.  
`chat.message` | Emitted when there is a new message.  
`chat.memberJoined` | Emitted when a new member joined the conversation.  
`chat.memberLeft` | Emitted when a member left the conversation.  
`chat.typingStarted` | Emitted when a member started typing.  
`chat.typingEnded` | Emitted when a member ended typing.  
`chat.connectedMessages` | Emitted when the SDK is connected to a conversation with provider.  
`chat.disconnected` | Emitted when the chat is disconnected from the provider.  
`chat.dismissed` | Emitted when the chat's status is changed to `dismissed`.  
`chat.timeout` | Emitted when the chat is ended due to "timeout".  
`chat.ended` | Emitted when the chat is ended.  
`chat.destroyed` | Emitted when `destroyChat` is called.  
`chat.checkInRequested` | Emitted when chat is able to be checked in.  
`chat.checkInTimedOut` | Emitted when chat check-in has timed out  
  
### Cobrowse events

Event name | Description  
---|---  
`cobrowse.request` | Emitted when end user or agent requests cobrowse  
`cobrowse.loaded` | Emitted when cobrowse session is loaded  
`cobrowse.updated` | Emitted when cobrowse session is updated  
`cobrowse.ended` | Emitted when cobrowse session is ended  
  
#### Usage examples
    
    
    client.on("ready", () => {
      // Client is ready
    })
    client.on("chat.message", message => {
      console.log(message)
    })
    client.on("chat.connectedMessages", async ({ chat, messages }) => {
      // Handle chat and messages
    })
    client.on("cobrowse.request", ({ from }) => {
      console.log("Cobrowse requested by", from)
    })
    

## Custom data configuration

The `custom_data` option lets you pass arbitrary key-value pair data to the web SDK.

### Usage

You can provide custom data as either an object (unsigned) or a string (signed) when creating a chat:
    
    
    interface ChatRequest {
      lang?: string;
      trigger_id?: string;
      ticket_id?: string;
      email?: string;
      greeting?: string;
      cobrowsable?: boolean;
      custom_data?: {
        signed?: string;
        unsigned?: Record<string, any>;
      };
    }
    

#### Example

See the following example:
    
    
    const custom_data = {
      unsigned: {
        version: {
          label: 'Version',
          value: '1.0.0'
        }
      },
      signed: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' // JWT or other signed payload
    }
    
    try {
      const chat: Chat = await client.createChat(123, { custom_data })
    } catch (error) {
      // handle error
    }
    

**Note:** Custom data is typically sent with session-creation requests for backend processing.

## External chatbot transfer

There are some cases where you might want to maintain history and interactions from other chat providers. You can do this by using the `custom_data object`.

See the following example:
    
    
    cconst custom_data = {
      unsigned: {
        external_chat_transfer: {
          greeting_override: "Please hold while we connect you with a human agent.",
          agent: {
            name: "Agent Name",
            avatar: "https://ujet.s3.amazonaws.com/default-virtual-agent-avatar-1.png"
          },
          transcript: [
            {
              sender: "agent",
              timestamp: "2021-03-15 12:00:00Z",
              content: [
                {
                  type: "text",
                  text: "Hello! How can I help you today?"
                },
                {
                  type: "buttons",
                  buttons: [
                    {
                      label: "Create New Order",
                      selected: false
                    },
                    {
                      label: "Check Order Status",
                      selected: true
                    },
                    {
                      label: "Check Account Balance",
                      selected: false
                    },
                  ]
                }
              ]
            },
            {
              sender: "end_user",
              timestamp: "2021-03-15 12:00:15Z",
              content: [
                {
                  type: "text",
                  text: "Check Order Status"
                }
              ]
            },
            {
              sender: "agent",
              timestamp: "2021-03-15 12:00:16Z",
              content: [
                {
                  type: "text",
                  text: "I can help you with that, what's your order number?"
                }
              ]
            },
            {
              sender: "end_user",
              timestamp: "2021-03-15 12:00:20Z",
              content: [
                {
                  type: "media",
                  media: {
                    type: "image",
                    url: "https://ujet.s3.amazonaws.com/default-virtual-agent-avatar-1.png"
                  }
                }
              ]
            }
          ]
        }
      },
      signed: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' // JWT or other signed payload
    }
    
    try {
      const chat: Chat = await client.createChat(123, { custom_data })
    } catch (error) {
      // handle error
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
