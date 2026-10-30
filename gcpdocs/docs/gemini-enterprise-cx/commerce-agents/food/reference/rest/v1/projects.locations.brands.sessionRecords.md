---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords
title: REST Resource: projects.locations.brands.sessionRecords \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:18.274971+00:00
---

# REST Resource: projects.locations.brands.sessionRecords  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  REST Resource: projects.locations.brands.sessionRecords Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SessionRecord
    * JSON representation
  * Interaction
    * JSON representation
  * UserUtterance
    * JSON representation
  * AgentUtterance
    * JSON representation
  * ResolveOrder
    * JSON representation
  * ResolveOrderInput
    * JSON representation
  * ResolveOrderOutput
    * JSON representation
  * SubmitOrder
  * MatchIntent
    * JSON representation
  * MatchIntentInput
    * JSON representation
  * MatchIntentOutput
    * JSON representation
  * ClientExecution
    * JSON representation
  * ClientExecutionInput
    * JSON representation
  * ClientExecutionOutput
    * JSON representation
  * ClientOrderUpdate
    * JSON representation
  * SuggestedOptions
    * JSON representation
  * SuggestedItems
    * JSON representation
  * SuggestedItem
    * JSON representation
  * NutritionalInfo
    * JSON representation
  * SuggestedModifiers
    * JSON representation
  * SuggestedModifier
    * JSON representation
  * SuggestedModGroup
    * JSON representation
  * SuggestedStores
    * JSON representation
  * SuggestedStore
    * JSON representation
  * SuggestedModifierGroups
    * JSON representation
  * SuggestedActions
    * JSON representation
  * SuggestedAction
    * JSON representation
  * TextInputAction
    * JSON representation
  * UpsellAttemptRecord
    * JSON representation
  * TrafficType
  * ExperimentMetadata
    * JSON representation
  * ExperimentStudy
    * JSON representation
  * Methods



## Resource: SessionRecord

Represents a single session record.

JSON representation  
---  
      
    
    {
      "name": string,
      "sessionStartTime": string,
      "storeId": string,
      "laneId": string,
      "interactions": [
        {
          object ([Interaction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#Interaction))
        }
      ],
      "outcomeLabel": string,
      "outcomeGroupLabel": string,
      "audioRecordingPath": string,
      "order": {
        object ([Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order))
      },
      "sessionDuration": string,
      "upsellAttemptRecords": [
        {
          object ([UpsellAttemptRecord](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#UpsellAttemptRecord))
        }
      ],
      "audioRecording": string,
      "trafficType": enum ([TrafficType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#TrafficType)),
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ChannelType)),
      "environment": string,
      "experimentMetadata": {
        object ([ExperimentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ExperimentMetadata))
      },
      "menu": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the SessionRecord. Format: projects/{project}/locations/{location}/brands/{brand}/sessionRecords/{sessionRecord}  
`sessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the session started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`storeId` |  `string` Immutable. The ID of the store where the order was placed.  
`laneId` |  `string` Immutable. The lane ID of the order session.  
`interactions[]` |  `object (`[Interaction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#Interaction)`)` Output only. The conversation turns.  
`outcomeLabel` |  `string` Output only. The final outcome label of the order.  
`outcomeGroupLabel` |  `string` Output only. The group label for the outcome.  
`audioRecordingPath  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated: Use storagePath instead. Path to the full audio recording.  
`order` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order)`)` Output only. The order associated with the session record.  
`sessionDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Total duration of the session.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`upsellAttemptRecords[]` |  `object (`[UpsellAttemptRecord](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#UpsellAttemptRecord)`)` Output only. Upsells performed during the session.  
`audioRecording` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Audio recording for the session. This field is only populated when calling sessionRecords.get.A base64-encoded string.  
`trafficType` |  `enum (`[TrafficType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#TrafficType)`)` Output only. The traffic type for the session.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ChannelType)`)` Output only. The type of channel used for the session (e.g. drive-through, mobile app, phone call).  
`environment` |  `string` Output only. The execution environment of the session (e.g. prod, preprod, preprod-au).  
`experimentMetadata` |  `object (`[ExperimentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ExperimentMetadata)`)` Output only. The metadata associated with the experiment.  
`menu` |  `string` Output only. The resource name of the menu active during the session. Format: `projects/{project}/locations/{location}/menus/{menu}`  
  
## Interaction

Represents a single interaction in a turn in the conversation.

JSON representation  
---  
      
    
    {
      "turnPosition": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userUtterance": {
        object ([UserUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#UserUtterance))
      },
      "agentUtterance": {
        object ([AgentUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#AgentUtterance))
      },
      "resolveOrder": {
        object ([ResolveOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrder))
      },
      "submitOrder": {
        object ([SubmitOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SubmitOrder))
      },
      "matchIntent": {
        object ([MatchIntent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntent))
      },
      "clientExecution": {
        object ([ClientExecution](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecution))
      },
      "clientOrderUpdate": {
        object ([ClientOrderUpdate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientOrderUpdate))
      },
      "suggestedOptions": {
        object ([SuggestedOptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedOptions))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`turnPosition` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Turn position in the conversation.  
The type of interaction. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userUtterance` |  `object (`[UserUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#UserUtterance)`)` User utterance.  
`agentUtterance` |  `object (`[AgentUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#AgentUtterance)`)` Agent utterance.  
`resolveOrder` |  `object (`[ResolveOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrder)`)` ResolveOrder call performed by the agent  
`submitOrder` |  `object (`[SubmitOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SubmitOrder)`)` SubmitOrder call performed by the agent  
`matchIntent` |  `object (`[MatchIntent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntent)`)` MatchIntent call performed by the agent  
`clientExecution` |  `object (`[ClientExecution](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecution)`)` ClientExecution call performed by the agent  
`clientOrderUpdate` |  `object (`[ClientOrderUpdate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientOrderUpdate)`)` Client-initiated order state update  
`suggestedOptions` |  `object (`[SuggestedOptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedOptions)`)` Suggested options surfaced to the customer during the turn.  
End of mutually exclusive fields.  
  
## UserUtterance

The user utterance.

JSON representation  
---  
      
    
    {
      "text": string,
      "createTime": string
    }  
  
Fields  
---  
`text` |  `string` The text of the user utterance.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the user utterance occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## AgentUtterance

The agent utterance.

JSON representation  
---  
      
    
    {
      "text": string,
      "createTime": string
    }  
  
Fields  
---  
`text` |  `string` The text of the agent utterance.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the agent utterance occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ResolveOrder

The resolve order interaction.

JSON representation  
---  
      
    
    {
      "input": {
        object ([ResolveOrderInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderInput))
      },
      "output": {
        object ([ResolveOrderOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderOutput))
      }
    }  
  
Fields  
---  
`input` |  `object (`[ResolveOrderInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderInput)`)` The input for the resolve order action.  
`output` |  `object (`[ResolveOrderOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderOutput)`)` The output for the resolve order action.  
  
## ResolveOrderInput

The input for the resolve order interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the resolve order interaction.  
  
## ResolveOrderOutput

The output for the resolve order interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the resolve order interaction output.  
  
## SubmitOrder

This type has no fields.

The submit order interaction.

## MatchIntent

The match intent interaction.

JSON representation  
---  
      
    
    {
      "input": {
        object ([MatchIntentInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentInput))
      },
      "output": {
        object ([MatchIntentOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentOutput))
      }
    }  
  
Fields  
---  
`input` |  `object (`[MatchIntentInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentInput)`)` The input for the match intent interaction.  
`output` |  `object (`[MatchIntentOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentOutput)`)` The output for the match intent interaction.  
  
## MatchIntentInput

The input for the match intent interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the match intent interaction input.  
  
## MatchIntentOutput

The output for the match intent interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the match intent interaction output.  
  
## ClientExecution

The client execution interaction.

JSON representation  
---  
      
    
    {
      "toolName": string,
      "input": {
        object ([ClientExecutionInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionInput))
      },
      "output": {
        object ([ClientExecutionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionOutput))
      }
    }  
  
Fields  
---  
`toolName` |  `string` The tool name for the client execution interaction.  
`input` |  `object (`[ClientExecutionInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionInput)`)` The input for the client execution interaction.  
`output` |  `object (`[ClientExecutionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionOutput)`)` The output for the client execution interaction.  
  
## ClientExecutionInput

The input for the client execution interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the client execution interaction input.  
  
## ClientExecutionOutput

The output for the client execution interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the client execution interaction output.  
  
## ClientOrderUpdate

Client-initiated order state update.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order))
      }
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Order)`)` An order state update sent by the client.  
  
## SuggestedOptions

Options to suggest to the customer.

JSON representation  
---  
      
    
    {
      "suggestedModifierGroups": {
        object ([SuggestedModifierGroups](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifierGroups))
      },
      "customIntegrationAttributes": {
        object
      },
      "suggestedActions": {
        object ([SuggestedActions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedActions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "suggestedItems": {
        object ([SuggestedItems](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedItems))
      },
      "suggestedModifiers": {
        object ([SuggestedModifiers](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifiers))
      },
      "suggestedStores": {
        object ([SuggestedStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedStores))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`suggestedModifierGroups` |  `object (`[SuggestedModifierGroups](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifierGroups)`)` A group of suggested modifiers.  
`customIntegrationAttributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
`suggestedActions` |  `object (`[SuggestedActions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedActions)`)` Optional. Generic contextual action pills.  
The suggested options. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`suggestedItems` |  `object (`[SuggestedItems](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedItems)`)` A list of items to suggest to the customer.  
`suggestedModifiers` |  `object (`[SuggestedModifiers](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifiers)`)` A list of modifiers to suggest to the customer.  
`suggestedStores` |  `object (`[SuggestedStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedStores)`)` A list of stores to suggest to the customer.  
End of mutually exclusive fields.  
  
## SuggestedItems

A list of items to suggest to the customer.

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([SuggestedItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedItem))
        }
      ]
    }  
  
Fields  
---  
`items[]` |  `object (`[SuggestedItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedItem)`)` The items to suggest to the customer.  
  
## SuggestedItem

An item to suggest to the customer.

JSON representation  
---  
      
    
    {
      "itemId": string,
      "displayName": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Image))
      },
      "basePrice": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "integrationAttributes": {
        object ([ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ItemIntegrationAttributes))
      },
      "nutritionalInfo": {
        object ([NutritionalInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#NutritionalInfo))
      },
      "description": string
    }  
  
Fields  
---  
`itemId` |  `string` ID of the item in the menu.  
`displayName` |  `string` Human-readable name for this tem to be shown on user interfaces.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Image)`)` Image to display for this item in the UI.  
`basePrice` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` The base price of the item. This may be affected by the selected modifiers. This is the price per unit of the item.  
`integrationAttributes` |  `object (`[ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ItemIntegrationAttributes)`)` Metadata associated with this entity used for downstream integrations.  
`nutritionalInfo` |  `object (`[NutritionalInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#NutritionalInfo)`)` Nutritional information for this item.  
`description` |  `string` Description for this item.  
  
## NutritionalInfo

Nutritional information for an item or modifier.

JSON representation  
---  
      
    
    {
      "calories": string
    }  
  
Fields  
---  
`calories` |  `string` Calorie count or calorie range string (e.g. "290", "250-300 Cal").  
  
## SuggestedModifiers

A list of modifiers to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifiers": [
        {
          object ([SuggestedModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifier))
        }
      ],
      "parentUid": string
    }  
  
Fields  
---  
`modifiers[]` |  `object (`[SuggestedModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifier)`)` The modifiers to suggest to the customer.  
`parentUid` |  `string` The unique identifier of the parent item/modifier to apply the modifiers to.  
  
## SuggestedModifier

A modifier to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifierId": string,
      "modifierGroupId": string,
      "modifierGroupDisplayName": string,
      "displayName": string,
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Image))
      },
      "priceAdjustment": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "integrationAttributes": {
        object ([ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ModifierIntegrationAttributes))
      },
      "alreadyIncluded": boolean,
      "suggestedModifierGroups": [
        {
          object ([SuggestedModGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModGroup))
        }
      ],
      "nutritionalInfo": {
        object ([NutritionalInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#NutritionalInfo))
      }
    }  
  
Fields  
---  
`modifierId` |  `string` ID of the modifier in the menu.  
`modifierGroupId` |  `string` ID of the modifier group that this modifier should be added to if the suggestion is accepted.  
`modifierGroupDisplayName` |  `string` Display name of the modifier group that this modifier belongs to.  
`displayName` |  `string` Human-readable name for this tem to be shown on user interfaces.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Image)`)` Image to display for this item in the UI.  
`priceAdjustment` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` The price adjustment associated with this modifier, if any. This is the price per unit of the modifier.  
`integrationAttributes` |  `object (`[ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ModifierIntegrationAttributes)`)` Metadata associated with this entity used for downstream integrations.  
`alreadyIncluded` |  `boolean` Whether this modifier is already included in the order.  
`suggestedModifierGroups[]` |  `object (`[SuggestedModGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModGroup)`)` The nested modifier groups suggested for this modifier.  
`nutritionalInfo` |  `object (`[NutritionalInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#NutritionalInfo)`)` Nutritional information for this modifier.  
  
## SuggestedModGroup

A modifier group to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifierGroupId": string,
      "displayName": string,
      "modifiers": [
        {
          object ([SuggestedModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifier))
        }
      ],
      "maxSelectionCount": integer,
      "minSelectionCount": integer,
      "maxSelectionCountPerModifier": integer,
      "minSelectionNotMatched": boolean
    }  
  
Fields  
---  
`modifierGroupId` |  `string` ID of the modifier group in the menu.  
`displayName` |  `string` The display name of the modifier group.  
`modifiers[]` |  `object (`[SuggestedModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModifier)`)` The modifiers in this group.  
`maxSelectionCount` |  `integer` The maximum number of modifiers that can be selected from this group.  
`minSelectionCount` |  `integer` The minimum number of modifiers that must be selected from this group.  
`maxSelectionCountPerModifier` |  `integer` Limits the number of times each modifier can be applied within this group.  
`minSelectionNotMatched` |  `boolean` Whether the minimum selection count is not matched.  
  
## SuggestedStores

A list of stores to suggest to the customer.

JSON representation  
---  
      
    
    {
      "stores": [
        {
          object ([SuggestedStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedStore))
        }
      ]
    }  
  
Fields  
---  
`stores[]` |  `object (`[SuggestedStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedStore)`)` The stores to suggest to the customer.  
  
## SuggestedStore

A store to suggest to the customer.

JSON representation  
---  
      
    
    {
      "store": {
        object ([Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.stores#Store))
      },
      "distance": number,
      "address": {
        object ([Address](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Address))
      },
      "storeHours": [
        {
          object ([StoreHours](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/StoreHours))
        }
      ],
      "phoneNumber": string,
      "storeName": string,
      "open": boolean,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeZone))
      }
    }  
  
Fields  
---  
`store  
**(deprecated)**` |  `object (`[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.stores#Store)`)` This item is deprecated!The suggested store.  
`distance` |  `number` The distance from the customer to the store in miles.  
`address` |  `object (`[Address](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Address)`)` The address of the store.  
`storeHours[]` |  `object (`[StoreHours](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/StoreHours)`)` The store hours.  
`phoneNumber` |  `string` The phone number of the store.  
`storeName` |  `string` The store resource name. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`open` |  `boolean` Whether the store is currently open.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeZone)`)` The timezone of the store.  
  
## SuggestedModifierGroups

A list of modifier groups to suggest to the customer.

JSON representation  
---  
      
    
    {
      "modifierGroups": [
        {
          object ([SuggestedModGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModGroup))
        }
      ]
    }  
  
Fields  
---  
`modifierGroups[]` |  `object (`[SuggestedModGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedModGroup)`)` The modifier groups to suggest to the customer.  
  
## SuggestedActions

A collection of action pills.

JSON representation  
---  
      
    
    {
      "actions": [
        {
          object ([SuggestedAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedAction))
        }
      ]
    }  
  
Fields  
---  
`actions[]` |  `object (`[SuggestedAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#SuggestedAction)`)` The list of suggested actions to display as pills.  
  
## SuggestedAction

A single action pill / chip.

JSON representation  
---  
      
    
    {
      "displayName": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "textInput": {
        object ([TextInputAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#TextInputAction))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`displayName` |  `string` The user-facing label rendered on the pill (e.g. "Edit Pizza", "Sign in").  
The typed action triggered when the pill is tapped. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`textInput` |  `object (`[TextInputAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#TextInputAction)`)` Sends back the text input through the textInput event.  
End of mutually exclusive fields.  
  
## TextInputAction

Action that sends a text query back to FoodAI via TextInput event.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` For sending back the text input through textInput event.  
  
## UpsellAttemptRecord

Represents an upsell attempt during an ordering session. This data is used to display upsell information in the console order history, namely upsell type, turn id, item names, price increase, and acceptance status.

JSON representation  
---  
      
    
    {
      "turnId": integer,
      "upsellType": string,
      "accepted": boolean,
      "originalItemDisplayName": string,
      "targetItemDisplayName": string,
      "priceIncrease": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      }
    }  
  
Fields  
---  
`turnId` |  `integer` Output only. ID of the turn in which the upsell opportunity occurred. Example: 2.  
`upsellType` |  `string` Output only. The type or configured display name of the upsell event. Example: "COMBO", "UP_SIZE", or "Add fries".  
`accepted` |  `boolean` Output only. Whether the upsell was accepted by the customer.  
`originalItemDisplayName` |  `string` Output only. The display name of the original item in the order that triggered the upsell. Example: "Cheeseburger".  
`targetItemDisplayName` |  `string` Output only. The display name of the target item offered or accepted in the upsell. Example: "French Fries" or "Cheeseburger Combo Meal".  
`priceIncrease` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. The additional monetary price increase for the upsold item. Example: {currencyCode: "USD", units: 1, nanos: 500000000} ($1.50).  
  
## TrafficType

The traffic type for the session. This is used to label the monitoring, logging, and observability metrics.

Enums  
---  
`TRAFFIC_TYPE_UNSPECIFIED` | The traffic type is not specified.  
`EXTERNAL` | The traffic is from an external client.  
`INTEGRATION_TEST` | The traffic is from an integration test.  
`EVAL` | The traffic is from the eval tool.  
`PROBER` | The traffic is from the prober.  
`MANUAL_TEST` | The traffic is from manual testing.  
`INTERNAL_TOOL` | The traffic is from an internal tool.  
`CONSOLE` | The traffic is from the food AI console.  
`QA` | Traffic from QA testing.  
  
## ExperimentMetadata

The metadata associated with the experiment.

JSON representation  
---  
      
    
    {
      "publicStudies": [
        {
          object ([ExperimentStudy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ExperimentStudy))
        }
      ]
    }  
  
Fields  
---  
`publicStudies[]` |  `object (`[ExperimentStudy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords#ExperimentStudy)`)` Output only. The public studies active during the session.  
  
## ExperimentStudy

The metadata associated with the study.

JSON representation  
---  
      
    
    {
      "studyName": string,
      "armName": string
    }  
  
Fields  
---  
`studyName` |  `string` Optional. The name of the study.  
`armName` |  `string` Optional. The name of the experiment arm.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords/delete)`

|  Deletes an SessionRecord.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords/get)`

|  Gets a specific SessionRecord.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.sessionRecords/list)`

|  Lists SessionRecords for a given brand.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
