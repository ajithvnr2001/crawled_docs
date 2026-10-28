---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/list/
title: Method: projects.locations.instances.keyRings.keys.transactions.list \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:38.613584+00:00
---

# Method: projects.locations.instances.keyRings.keys.transactions.list  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.keyRings.keys.transactions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Transactions for a Key, or across Keys.

To list across Keys or KeyRings, use `-` as a wildcard in `parent` ([AIP-159](https://google.aip.dev/159)), for example `projects/p/locations/l/instances/i/keyRings/-/keys/-`. This powers the Signer Console's pending queue, for example with `filter = "state = PENDING_AUTHORIZATION"`.

Results are always scoped to the caller. If the caller's User (the User whose `principal` matches the caller's authenticated identity) has only the `SIGNER` role, only Transactions on Keys where that User holds a key share are returned. Transactions the caller cannot see are omitted rather than failing the request.

### HTTP request

`GET https://mpc.googleapis.com/v1beta/{parent=projects/*/locations/*/instances/*/keyRings/*/keys/*}/transactions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent Key. Use `-` for `{keyRing}` and `{key}` to list across all Keys in the instance ([AIP-159](https://google.aip.dev/159)). Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}/keys/{key} It takes the form `projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyring}/keys/{key}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of Transactions to return. The service may return fewer. If unspecified, at most 50 are returned. Values above 1000 are coerced to 1000.  
`pageToken` |  `string` Optional. A page token from a previous `transactions.list` call. When paginating, all other parameters must match the call that returned the token.  
`filter` |  `string` Optional. A filter expression ([AIP-160](https://google.aip.dev/160)). Supported fields:

  * `state`: equality, e.g. `state = PENDING_AUTHORIZATION`.
  * `createTime`: comparison against an RFC 3339 timestamp, e.g. `createTime > "2026-10-01T00:00:00Z"`.
  * `expireTime`: comparison against an RFC 3339 timestamp.

Expressions can be combined with `AND`. Unsupported fields or operators fail with INVALID_ARGUMENT.  
`orderBy` |  `string` Optional. The order of results ([AIP-132](https://google.aip.dev/132)). Supported fields: `createTime` and `expireTime`, each optionally followed by `desc`. Defaults to `createTime desc`.  
  
### Request body

The request body must be empty.

### Response body

Response message for TransactionService.ListTransactions.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transactions": [
        {
          object ([Transaction](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Transaction))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`transactions[]` |  `object (`[Transaction](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Transaction)`)` The Transactions visible to the caller.  
`nextPageToken` |  `string` A token to retrieve the next page. Empty if there are no more pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
