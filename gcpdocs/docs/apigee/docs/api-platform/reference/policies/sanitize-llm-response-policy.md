---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy/
title: SanitizeModelResponse policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:51:20.682356+00:00
---

# SanitizeModelResponse policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SanitizeModelResponse policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This policy is supported on Apigee, and on Apigee hybrid **version 1.15.1 and later**.

The SanitizeModelResponse policy protects AI clients from harmful or offensive content by sanitizing responses from generative AI models. The policy uses [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) to evaluate model responses for harmful or offensive content, enabling native protection for AI clients and workloads using Apigee. Model Armor is a Google Cloud service offering AI security and safety measures to mitigate the risks associated with large language models (LLMs).

This policy is used in conjunction with the [SanitizeUserPrompt policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy).

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** If you have configured a forward proxy for your environment, the outbound calls this policy makes to Model Armor are routed through the proxy. No policy-level configuration is required. This is applicable for Apigee and Apigee Hybrid 1.16.10 and later, and 1.17.0 and later. For more information, see [Configure forward proxying](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#forward-proxying) (Apigee) or [Configure forward proxying for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/forward-proxy) (Apigee Hybrid).

## Before you begin

Before you use the SanitizeModelResponse policy, you must complete the following tasks:

  * Create a Model Armor template. This step must be completed before you create a SanitizeModelResponse policy.
  * Set the API endpoint for the Model Armor service.



### Required roles

To get the permissions that you need to apply and use the SanitizeModelResponse policy, ask your administrator to grant you the following IAM roles on the service account you use to deploy Apigee proxies: 

  * [Model Armor User ](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.user) (`roles/modelarmor.user`)
  * [Model Armor Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.viewer) (`roles/modelarmor.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

Enable the Model Armor APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,modelarmor.googleapis.com)

## `<SanitizeModelResponse>` element

Defines a SanitizeModelResponse policy.

**Default Value** | See **Default Policy** tab, below  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#displayname)  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#ignoreunresolvedvariables)  
[`<ModelArmor>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#modelarmor)  
[`<UserPromptSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#userpromptsource)  
[`<LLMResponseSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#llmresponsesource)  
[`<FunctionCallSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#functioncallsource)  
`<ContinuousScan>`  
  
  
The [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name) element uses the following syntax:

### Syntax
    
    
    <SanitizeModelResponse async="false" continueOnError="false" enabled="true" name="sanitize-response">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <DisplayName>sanitize-response-sample</DisplayName>
      <ModelArmor>
        <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
      </ModelArmor>
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content)}</UserPromptSource>
      <LLMResponseSource>{jsonPath('$.candidates[-1].content.parts',response.content)}</LLMResponseSource>
      <FunctionCallSource>{jsonPath('$.candidates[-1].content.parts[-1].functionCall.args',response.content)}</FunctionCallSource>
      <ContinuousScan>false</ContinuousScan>
    </SanitizeModelResponse>

### Default Policy

The following example shows the default settings when you add a SanitizeModelResponse policy to your request flow in the Apigee UI:
    
    
    <SanitizeModelResponse async="false" continueOnError="false" enabled="true" name="sanitize-response">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <DisplayName>sanitize-response-sample</DisplayName>
      <ModelArmor>
        <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
      </ModelArmor>
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content)}</UserPromptSource>
      <LLMResponseSource>{jsonPath('$.candidates[-1].content.parts',response.content)}</LLMResponseSource>
      <FunctionCallSource>{jsonPath('$.candidates[-1].content.parts[-1].functionCall.args',response.content)}</FunctionCallSource>
    </SanitizeModelResponse>

When you insert a new SanitizeModelResponse policy using the Apigee UI, the template contains stubs for all possible operations. See below for information on required elements.

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
The following table provides a high level description of the child elements of [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name):

Child Element | Required? | Description  
---|---|---  
[`<DisplayName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#displayname) | Optional | The name of the policy.   
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#ignoreunresolvedvariables) | Optional | Specifies whether processing stops if the variable used for the template name or Model Armor payload is unresolved.  
[`<ModelArmor>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#modelarmor) | Required | Contains the required information for specifying the Model Armor template.  
[`<UserPromptSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#userpromptsource) | Optional | The payload location from which to extract the user prompt text. The policy sends this text to Model Armor as context for response sanitization. If you omit this element, the policy sends only the LLM response to Model Armor for sanitization, and the policy deploys and runs successfully. Supports only string text values. This field supports Apigee message template syntax, including the use of [ variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#use-curly-braces-to-denote-variables) or [JSON Path functions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#json-path-function). For example: 
    
    
    {jsonpath('$.contents[-1].parts[-1].text',request.content,false)}  
  
[`<LLMResponseSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#llmresponsesource) | Optional | The location of the payload for the LLM response text to be extracted. When omitted, the default Agent Platform `generateContent` JSON path is applied: `{jsonPath('$.candidates[-1].content.parts',response.content)}`. Only string text values are supported. This field supports Apigee message template syntax, including the use of [ variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#use-curly-braces-to-denote-variables) or [JSON Path functions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#json-path-function). For example: 
    
    
    {jsonpath('$.input.prompt.text',request.content,false)}  
  
[`<FunctionCallSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#functioncallsource) | Optional | The location of the function call arguments to extract from model responses. The policy uses this element as a fallback when [`<LLMResponseSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#llmresponsesource) returns empty on function-calling turns. Default: `{jsonPath('$.candidates[-1].content.parts[-1].functionCall.args',response.content)}`  
`<ContinuousScan>` | Optional | Specifies whether to check the entire streaming (SSE) response, delivering each event to the client only after Model Armor checks it. Applies only when the policy runs in an SSE `EventFlow`. Default: `false`  
  
## Sanitize streaming Server-Sent Events (SSE) responses

In an SSE `EventFlow`, use `<ContinuousScan>` to choose one of two options: check each event separately (`false`, the default), or check the whole stream using Model Armor [streaming sanitization](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#sanitize-streaming) (`true`). With `true`, the complete response usually finishes sooner, because the policy checks the stream over one connection while the model is still generating, instead of making a separate request for each event. However, time to first token can be longer. To add the policy to an `EventFlow`, see [Use an Apigee Model Armor policy in an EventFlow](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events#model-armor-policy).

The following table compares the two options:

Behavior | `false` (default): each event separately | `true`: whole stream  
---|---|---  
How text is checked | Each event on its own, without the text of earlier events. | The whole stream, with the text of earlier events as context.  
When the client receives an event | After that event's own check. | After Model Armor has checked it.  
Model Armor requests | One per event. | One per response.  
Token limit | Per request. | No limit on the total tokens in a response.  
**Note:** With `<ContinuousScan>true</ContinuousScan>`, Apigee delivers each SSE event whole, unchanged, and in order, only after Model Armor checks it, so events can arrive slightly later than in the original stream.

The `<ContinuousScan>` element exists only on the SanitizeModelResponse policy, not on the [SanitizeUserPrompt policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy).

### Configure continuous scan

Set `<ContinuousScan>true</ContinuousScan>` and point `<LLMResponseSource>` at the text in the current event, `response.event.current.data`:
    
    
    <SanitizeModelResponse async="false" continueOnError="false"
        enabled="true" name="SMR-ContinuousScan">
      <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
      <DisplayName>SMR-ContinuousScan</DisplayName>
      <ModelArmor>
        <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
      </ModelArmor>
      <LLMResponseSource>{jsonPath('$.candidates[-1].content.parts[-1].text',response.event.current.data,true)}</LLMResponseSource>
      <ContinuousScan>true</ContinuousScan>
    </SanitizeModelResponse>

Use the `<LLMResponseSource>` expression that matches your model's streaming format:

Streaming format | `<LLMResponseSource>`  
---|---  
Gemini (`streamGenerateContent?alt=sse`) | `{jsonPath('$.candidates[-1].content.parts[-1].text',response.event.current.data,true)}`  
OpenAI-compatible chat completions | `{jsonPath('$.choices[-1].delta.content',response.event.current.data,true)}`  
Anthropic Claude | `{jsonPath('$.delta.text',response.event.current.data,true)}`  
  
### Matches and errors

With `<ContinuousScan>` set to `true`, errors are either transient or terminal:

Type | Examples | How it's handled  
---|---|---  
Transient | A dropped connection to Model Armor, or Model Armor temporarily unavailable. | Retried. Apigee reconnects and checks the not-yet-delivered text again, so no event is skipped or delivered unchecked. This happens up to two times per response, regardless of `continueOnError`. If it keeps failing, the error becomes terminal.  
Terminal | A filter match, an authentication or permission error, an exceeded Model Armor quota, or no response from Model Armor within the 60-second timeout. | Not retried. The check ends, and `continueOnError` determines what the client receives, as described in the next table.  
  
With `<ContinuousScan>` set to `true`, the policy doesn't deliver the Sensitive Data Protection (SDP) de-identified (redacted) text from Model Armor. Apigee releases events unchanged and handles a de-identification match like any other match.

On a terminal error, the `continueOnError` attribute determines what the client receives:

`continueOnError` | What the client receives  
---|---  
`false` (default) | The client receives the events that passed the check and then an SSE event with the fault, such as `steps.sanitize.model.response.FilterMatched`, `steps.sanitize.modelarmor.ModelArmorAPIFailed`, or `steps.sanitize.modelarmor.AuthenticationFailure`. The stream then ends. The client receives no unchecked or matching text.  
`true` | The client receives the complete response, including the matching text and anything after it. Terminal errors don't raise a fault, and the rest of the response passes through unchecked. The policy sets `SanitizeModelResponse.POLICY_NAME.failed` to `true` so that a later step in the `EventFlow` can act on it.  
  
With `<ContinuousScan>` set to `false`, each event is a separate request, and there are no reconnect retries. With `continueOnError="true"`, a match affects only that event, and the policy still checks later events.

### Quotas and limits

  * With `<ContinuousScan>true</ContinuousScan>`, a whole streamed response counts as one request against your project's [Model Armor quota](https://docs.cloud.google.com/model-armor/quotas#quotas), plus one for each reconnect. With `false`, every SSE event is a separate request.
  * With `<ContinuousScan>true</ContinuousScan>`, there is [no limit on the total tokens](https://docs.cloud.google.com/model-armor/quotas#unlimited-tokens-real-time-streaming) in a response. Otherwise, each request is subject to the Model Armor [token limits](https://docs.cloud.google.com/model-armor/quotas#token-limits).



## Child element reference

This section describes the child elements of [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name).

### `<DisplayName>`

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, more natural-sounding name.

The `<DisplayName>` element is common to all policies.

**Default Value** | N/A  
---|---  
**Required?** | Optional. If you omit `<DisplayName>`, the value of the policy's `name` attribute is used.  
**Type** | String  
**Parent Element** |  <PolicyElement>  
**Child Elements** |  None   
  
The `<DisplayName>` element uses the following syntax:

### Syntax
    
    
    <_PolicyElement_ >
      **< DisplayName>POLICY_DISPLAY_NAME</DisplayName>**
      ...
    </_PolicyElement_ >

### Example
    
    
    <_PolicyElement_ >
      **< DisplayName>My Validation Policy</DisplayName>**
    </_PolicyElement_ >

The `<DisplayName>` element has no attributes or child elements.

### `<IgnoreUnresolvedVariables>`

Determines whether processing stops when a variable is unresolved. Set to `true` to ignore unresolved variables and continue processing.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name)  
**Child Elements** |  None   
  
### `<ModelArmor>`

Contains the Model Armor template configuration. The [`<TemplateName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#templatename) child element specifies which Model Armor template is used to sanitize the LLM response.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name)  
**Child Elements** |  [`<TemplateName>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#templatename)  
  
The `<ModelArmor>` element uses the following syntax:
    
    
    <ModelArmor>
      <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
    </ModelArmor>

### `<TemplateName>`

The Model Armor template.

**Default Value** | N/A  
---|---  
**Required?** | Required  
**Type** | String  
**Parent Element** |  [`<ModelArmor>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#modelarmor)  
**Child Elements** |  None   
  
The `<TemplateName>` element uses the following syntax:

### Syntax
    
    
    <ModelArmor>
      <TemplateName>projects/{project}/locations/{location}/templates/{template-name}</TemplateName>
    </ModelArmor>

### Example

This example uses Apigee flow variables to populate the required information.
    
    
    <ModelArmor>
      <TemplateName>projects/**{ organization.name}**/locations/**{ system.region.name}**/templates/**{ id}**</TemplateName>
    </ModelArmor>

### `<UserPromptSource>`

The payload location from which to extract the user prompt text. If you provide this element, the policy sends the user prompt to Model Armor alongside the model response for context-aware sanitization. If you omit this element, the policy sanitizes only the model response, and the policy deploys and runs successfully. Supports only string text values.

This field supports Apigee message template syntax, including the use of [ variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#use-curly-braces-to-denote-variables) or [JSON Path functions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#json-path-function). For example: 
    
    
    {jsonpath('$.input.prompt.text',request.content,false)}

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name)  
**Child Elements** |  None   
  
### `<LLMResponseSource>`

The location of the payload for the LLM response to be extracted. Only string text values are supported. 

This field supports Apigee message template syntax, including the use of [ variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#use-curly-braces-to-denote-variables) or [JSON Path functions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#json-path-function). For example: 
    
    
    {jsonpath('$.input.prompt.text',request.content,false)}

**Default Value** | {jsonPath('$.candidates[-1].content.parts',response.content)}  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name)  
**Child Elements** |  None   
  
### `<FunctionCallSource>`

The location of the function call arguments to extract from the model response. The policy uses this element as a fallback when [`<LLMResponseSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#llmresponsesource) returns empty, which occurs when the model returns a function call invocation instead of text content.

This field supports message template syntax, including JSON Path functions.

**Default Value** | {jsonPath('$.candidates[-1].content.parts[-1].functionCall.args',response.content)}  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name)  
**Child Elements** |  None   
  
### <ContinuousScan>

Set to `true` to check the entire streaming (SSE) response as one stream, using Model Armor [streaming sanitization](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#sanitize-streaming). The policy checks each event together with the text of all earlier events, and the client receives each event whole and unchanged, only after Model Armor checks it. The policy doesn't deliver the Sensitive Data Protection (SDP) de-identified (redacted) text from Model Armor.

When `false` or omitted, the policy checks each event separately. The element applies only when the policy runs in an SSE `EventFlow`, and has no effect elsewhere. For more information, see Sanitize streaming Server-Sent Events (SSE) responses.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name)  
**Child Elements** |  None   
  
The `<ContinuousScan>` element uses the following syntax:
    
    
    <ContinuousScan>true</ContinuousScan>

## Flow variables

Flow variables can be used to configure dynamic runtime behavior for policies and flows, based on HTTP headers or message content, or the context available in the Flow. For more information about flow variables, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

This policy provides the following set of _read-only_ flow variables during execution. You can use these flow variables with the [DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) to create custom analytics reports. For more information, see [Collecting customer data with the Data Capture policy](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture).

Variable name | Description  
---|---  
`SanitizeModelResponse.POLICY_NAME.templateUsed` | Specifies which model armor template is used. For example: `projects/myproject/locations/us-west1/templates/mytemplate`  
`SanitizeModelResponse.POLICY_NAME.userPrompt` | Specifies the prompt content used for the call to Model Armor to sanitize the content.  
`SanitizeModelResponse.POLICY_NAME.modelResponse` | Specifies the LLM response content used for the call to Model Armor to sanitize the content.  
`SanitizeModelResponse.POLICY_NAME.responseFromModelArmor` | Specifies the JSON response from Model Armor. When `<ContinuousScan>` is set to `true`, contains the most recent response.  
`SanitizeModelResponse.POLICY_NAME.filterMatchState` | Specifies whether the filter was matched. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeModelResponse.POLICY_NAME.invocationResult` | A field indicating the outcome of the invocation, irrespective of match status. It can have the following: 

  * SUCCESS: All filters executed successfully.
  * PARTIAL: Some filters were skipped or failed execution.
  * FAILURE: All filters were skipped or failed execution.

  
`SanitizeModelResponse.POLICY_NAME.raiFilterResult.executionState` | Rai filter execution result. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeModelResponse.POLICY_NAME.raiFilterResult.matchState` | Rai filter match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeModelResponse.POLICY_NAME.sdpFilterResult.inspectResult.executionState` | Sdp filter inspect result execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeModelResponse.POLICY_NAME.sdpFilterResult.inspectResult.matchState` | Sdp filter inspect result match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeModelResponse.POLICY_NAME.sdpFilterResult.deidentifyResult.executionState` | Sdp filter de identify result execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeModelResponse.POLICY_NAME.sdpFilterResult.deidentifyResult.matchState` | Sdp filter de identify result match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeModelResponse.POLICY_NAME.piAndJailbreakFilterResult.executionState` | Prompt injection and Jailbreak filter results execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeModelResponse.POLICY_NAME.piAndJailbreakFilterResult.matchState` | Prompt injection and Jailbreak filter results match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeModelResponse.POLICY_NAME.csamFilterFilterResult.executionState` | CSAM filter execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeModelResponse.POLICY_NAME.csamFilterFilterResult.matchState` | CSAM filter match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeModelResponse.POLICY_NAME.maliciousUriFilterResult.executionState` | Malicious URI filter execution state. Valid values include `EXECUTION_SUCCESS` and `EXECUTION_SKIPPED`.  
`SanitizeModelResponse.POLICY_NAME.maliciousUriFilterResult.matchState` | Malicious URI filter match state. Valid values include `MATCH_FOUND` and `NO_MATCH_FOUND`.  
`SanitizeModelResponse.POLICY_NAME.sanitizationMetadata.errorCode` | Custom overridden Error code if present in Model Armor response.  
`SanitizeModelResponse.POLICY_NAME.sanitizationMetadata.errorMessage` | Custom overridden Error code if present in Model Armor response.  
`SanitizeModelResponse.POLICY_NAME.csamFilterMatched` | Boolean value indicating whether the CSAM filter matched.  
`SanitizeModelResponse.POLICY_NAME.maliciousURIs` | Appended list of malicious URIs detected by the malicious URI filter.  
`SanitizeModelResponse.POLICY_NAME.maliciousURIsDetected` | Boolean value indicating whether the malicious URI filter matched.  
`SanitizeModelResponse.POLICY_NAME.matchesFound` | Boolean value indicating whether any of the filters matched.  
`SanitizeModelResponse.POLICY_NAME.promptInjectionDetected` | Boolean value indicating whether the prompt injection filter matched.  
`SanitizeModelResponse.POLICY_NAME.promptInjectionConfidence` | Confidence level of prompt injection detection.  
`SanitizeModelResponse.POLICY_NAME.raiMatchesFound` | Boolean value indicating whether the RAI filter matched.  
`SanitizeModelResponse.POLICY_NAME.requestSentToModelArmor` | Specifies the JSON request sent to Model Armor. When `<ContinuousScan>` is set to `true`, contains the most recent request.  
`SanitizeModelResponse.POLICY_NAME.sanitizeOperation` | Specifies the operation performed by the policy. Valid values include `SANITIZE_USER_PROMPT` and `SANITIZE_MODEL_RESPONSE`.  
`SanitizeModelResponse.POLICY_NAME.streamReplacements` | Specifies the number of times the policy reconnected to Model Armor during the response when `<ContinuousScan>` is set to `true`. Set only if the policy reconnected.  
`SanitizeModelResponse.POLICY_NAME.lastStreamReplacementCause` | Specifies the error that caused the most recent reconnect when `<ContinuousScan>` is set to `true`. Set only if the policy reconnected.  
  
## Error reference

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee specific to the [`<SanitizeModelResponse>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#name) policy. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

Fault code | HTTP status | Cause  
---|---|---  
`steps.sanitize.model.response.FilterMatched` | `400` | This error occurs if the user prompt does not pass the Model Armor template check.  
`steps.sanitize.model.response.SanitizationResponseParsingFailed` | `500` | This error occurs if the Model Armor response cannot be parsed.  
`steps.sanitize.model.response.FailedToExtractUserPrompt` | `500` | This error occurs if the automatic user prompt extraction for the default value failed.  
`steps.sanitize.model.response.FailedToExtractLLMResponse` | `500` | This error occurs if the automatic model response extraction for the default value failed.  
`steps.sanitize.model.response.InternalError` | `500` | This error occurs if there is an internal server error.  
`steps.sanitize.model.response.ModelArmorTemplateNameExtractionFailed` | `500` | This error occurs if the template name cannot be resolved.  
`steps.sanitize.model.response.AuthenticationFailure` | `500` | This error occurs if the service account does not have permission to call the Model Armor API.  
`steps.sanitize.model.response.ModelArmorAPIFailed` | `500` | This error occurs if the Model Armor API throws an error.  
`steps.sanitize.model.response.ModelArmorCalloutError` | `500` | This error occurs if the Model Armor API call fails.  
`steps.sanitize.modelarmor.ServiceUnavailable` | `500` | This error occurs if the Model Armor service is unavailable.  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

Error name | Cause  
---|---  
`The ModelArmor/TemplateName element is required.` | Occurs if the <TemplateName> element in <ModelArmor> is not present.  
`The TemplateName element value is required.` | Occurs if the <TemplateName> value is empty.  
  
### Fault variables

These variables are set when this policy triggers an error at runtime. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="FAULT_NAME"` | FAULT_NAME is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "UnresolvedVariable"`  
`SanitizeModelResponse.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `SanitizeModelResponse.sanitize-response.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
      "fault": {
        "faultstring": "SanitizeModelResponse[sanitize-response]: unable to resolve variable [variable_name]",
        "detail": {
          "errorcode": "steps.sanitizemodelresponse.UnresolvedVariable"
        }
      }
    }

### Example fault rule
    
    
    <FaultRule name="SanitizeModelResponse Faults">
        <Step>
            <Name>SMR-CustomSetVariableErrorResponse</Name>
            <Condition>(fault.name = "SetVariableFailed")</Condition>
        </Step>
        <Condition>(sanitizemodelresponse.failed = true)</Condition>
    </FaultRule>

### Model Armor template error code and error messages

The Model Armor template supports overriding error codes and error messages thrown by the SanitizeModelResponse policy's API requests. If the user sets the overrides, then the Model Armor error codes and error messages will populate the flow variables.

For example, a response with Model Armor error codes and messages could look like the following: 
    
    
    {
    "sanitizationResult": {
      "filterMatchState": "MATCH_FOUND",
      "filterResults": {...},
      "sanitizationMetadata": {
        "errorCode": "890",
        "errorMessage": "get out"
      },
      "invocationResult": "SUCCESS"
      }
    }

## Schemas

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
