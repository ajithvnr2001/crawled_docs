---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/authorizePayload/
title: Method: projects.locations.instances.policyEngine.authorizePayload \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:51.355607+00:00
---

# Method: projects.locations.instances.policyEngine.authorizePayload  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/authorizePayload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.policyEngine.authorizePayload Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * PayloadSchema
  * Decision
  * Try it!



Authorizes an operation proposal payload against active policies.

### HTTP request

`POST https://mpc.googleapis.com/v1alpha1/{instance=projects/*/locations/*/instances/*}/policyEngine:authorizePayload`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The unique resource name of the MPC instance evaluating the policies. Format: projects/{project}/locations/{location}/instances/{instance} It takes the form `projects/{project}/locations/{location}/instances/{instance}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "principal": string,
      "action": string,
      "resource": string,
      "schema": enum ([PayloadSchema](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/authorizePayload#PayloadSchema)),
      "payload": string
    }  
  
Fields  
---  
`principal` |  `string` Required. The entity requesting authorization (e.g., `User::"alice"`).  
`action` |  `string` Required. The specific Cedar action being authorized. Since Cedar actions are dynamic and user-defined in custom policy sets, they are represented as strings (e.g., `Action::"dkg_genesis"`, `Action::"Transfer"`).  
`resource` |  `string` Required. The target asset or context of the operation, formatted as a Cedar entity reference (e.g., `Token::"USDC"` or `Vault::"vault_123"`).  
`schema` |  `enum (`[PayloadSchema](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/authorizePayload#PayloadSchema)`)` Required. The schema identifier of the payload.  
`payload` |  `string` Required. The representation of the operation proposal (e.g. hex-encoded or raw JSON string) to parse and verify.  
  
### Response body

Response from authorizing an operation proposal payload.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "decision": enum ([Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/authorizePayload#Decision)),
      "token": string,
      "digest": string,
      "evaluatedPolicyIds": [
        string
      ]
    }  
  
Fields  
---  
`decision` |  `enum (`[Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/authorizePayload#Decision)`)` The outcome of the policy evaluation.  
`token` |  `string` The JWS signature policy token (only populated on PERMIT).  
`digest` |  `string` The hex-encoded SHA-256 digest computed from the raw transaction payload.  
`evaluatedPolicyIds[]` |  `string` The list of active Cedar policy IDs that authorized or triggered the decision.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## PayloadSchema

PayloadSchema identifies the parser needed to decode the raw bytes. This enum is not frozen; new payload schemas may be added in the future.

Enums  
---  
`PAYLOAD_SCHEMA_UNSPECIFIED` | Unspecified payload schema.  
`DKG_INTENT_V1` | DKG Key Generation Intent V1.  
`ETHEREUM_TX_V1` | Ethereum Transaction V1.  
`BITCOIN_TX_V1` | Deprecated: Use `BITCOIN_TX_V2` instead.Bitcoin Transaction V1.This item is deprecated!  
`BITCOIN_TX_V2` | Bitcoin Transaction V2 (BIP 174 PSBT v0).  
`ETHEREUM_TX_V2` | Ethereum Transaction V2 (Protocol-Agnostic).  
  
## Decision

Decision represents the result of the policy evaluation. This enum is frozen; no new decisions are expected to be added.

Enums  
---  
`DECISION_UNSPECIFIED` | Unspecified decision.  
`PERMIT` | The operation is explicitly permitted.  
`DENY` | The operation is explicitly denied.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
