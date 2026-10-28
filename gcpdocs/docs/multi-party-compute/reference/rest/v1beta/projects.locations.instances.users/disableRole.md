---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/disableRole/
title: Method: projects.locations.instances.users.disableRole \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:40.384436+00:00
---

# Method: projects.locations.instances.users.disableRole  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/disableRole/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.users.disableRole Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Disables one role of a User. The role stays in `roleStatuses` as `DISABLED`, and the User's other roles are not affected.

`SIGNER` is disabled immediately and the User leaves their Team; it fails with FAILED_PRECONDITION while the User holds key shares, until resharing is supported. `ADMIN` and `POLICY_AUTHOR` need `authorizationInfo`. An `ACTIVE` role becomes `PENDING_DISABLED`, still usable, until enough Admins approve with `users.approveRoleChange`. A `PENDING_ACTIVE` role is canceled: it becomes `DISABLED` at once, without Admin approval.

Disabling `ADMIN` fails with FAILED_PRECONDITION if it would leave too few active Admins (see the service rules). Fails with FAILED_PRECONDITION if the role is already `DISABLED` or `PENDING_DISABLED`.

### HTTP request

`POST https://mpc.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*/users/*}:disableRole`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the User. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "role": enum ([Role](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#Role)),
      "authorizationInfo": {
        object ([AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo))
      }
    }  
  
Fields  
---  
`role` |  `enum (`[Role](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#Role)`)` Required. The role to disable.  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Optional. The calling Admin's signature over a UserSigningPayload with the User's role changes that are pending after this request: the DISABLE change for `role` plus any other pending changes. Not needed when the request only cancels a pending enable of `role`. Otherwise required if `role` is `ADMIN` or `POLICY_AUTHOR`; must be empty for other roles.  
  
### Response body

If successful, the response body contains an instance of `[User](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#User)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
