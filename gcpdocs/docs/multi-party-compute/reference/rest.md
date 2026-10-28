---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/
title: Multi-party Compute API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:42.089241+00:00
---

# Multi-party Compute API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Multi-party Compute API Stay organized with collections  Save and categorize content based on your preferences. 

Multi-party Compute (MPC) API manages distributed cryptographic keys and signing operations.

  * REST Resource: v1beta.projects.locations.instances.keyLists
  * REST Resource: v1beta.projects.locations.instances.keyRings
  * REST Resource: v1beta.projects.locations.instances.keyRings.keys
  * REST Resource: v1beta.projects.locations.instances.keyRings.keys.transactions
  * REST Resource: v1beta.projects.locations.instances.teams
  * REST Resource: v1beta.projects.locations.instances.transactionPolicies
  * REST Resource: v1beta.projects.locations.instances.users
  * REST Resource: v1alpha1.projects.locations.instances.mpc.keyRings
  * REST Resource: v1alpha1.projects.locations.instances.mpc.keyRings.keys
  * REST Resource: v1alpha1.projects.locations.instances.mpc.keyRings.keys.proposals
  * REST Resource: v1alpha1.projects.locations.instances.mpc.signers
  * REST Resource: v1alpha1.projects.locations.instances.policyEngine
  * REST Resource: v1alpha1.projects.locations.instances.policyEngine.policies



## Service: mpc.googleapis.com

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api-service-endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints.

The Multi-party Compute (MPC) API is split across two distinct layers: the instance management API and the data plane API. Most of the services and methods documented here operate on the data plane to manage keys, key rings, and signing proposals. Data plane endpoints are hosted directly by your dedicated MPC instance, so you must connect to your specific instance's API hostname to access them.

### Data plane endpoints

The data plane API hostname resembles the following:

  * https://INSTANCE_MONIKER.LOCATION.mpc.goog



For example, the following hostname is for an instance moniker of `my-instance` in location `us-central1`:

  * `<https://my-instance.us-central1.mpc.goog>`



### Instance management endpoint

The instance management API manages the lifecycle of the instances themselves (such as creating or deleting instances) and is accessed via the shared multi-tenant endpoint:

  * `<https://mpc.googleapis.com>`



## REST Resource: [v1beta.projects.locations.instances.keyLists](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists)

Methods  
---  
`[addEntries](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/addEntries)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/keyLists/*}:addEntries`   
Adds entries to a KeyList and returns the updated KeyList.  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/create)` |  `POST /v1beta/{parent=projects/*/locations/*/instances/*}/keyLists`   
Creates a new KeyList in an instance.  
`[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/instances/*/keyLists/*}`   
Deletes a KeyList.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/keyLists/*}`   
Gets details of a single KeyList.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*}/keyLists`   
Lists KeyLists in an instance.  
`[removeEntries](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/removeEntries)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/keyLists/*}:removeEntries`   
Removes entries from a KeyList and returns the updated KeyList.  
  
## REST Resource: [v1beta.projects.locations.instances.keyRings](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/create)` |  `POST /v1beta/{parent=projects/*/locations/*/instances/*}/keyRings`   
Creates a new KeyRing in an instance.  
`[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/instances/*/keyRings/*}`   
Deletes a KeyRing and its KeyPolicy.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/keyRings/*}`   
Gets details of a single KeyRing.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*}/keyRings`   
Lists KeyRings in an instance.  
  
## REST Resource: [v1beta.projects.locations.instances.keyRings.keys](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/create)` |  `POST /v1beta/{parent=projects/*/locations/*/instances/*/keyRings/*}/keys`   
Creates a new Key in a KeyRing by running distributed key generation (DKG).  
`[disable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/disable)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/keyRings/*/keys/*}:disable`   
Disables a Key so it can no longer sign.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/keyRings/*/keys/*}`   
Gets details of a single Key.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*/keyRings/*}/keys`   
Lists Keys in a KeyRing.  
  
## REST Resource: [v1beta.projects.locations.instances.keyRings.keys.transactions](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/create)` |  `POST /v1beta/{parent=projects/*/locations/*/instances/*/keyRings/*/keys/*}/transactions`   
Creates a new Transaction for a Key.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/keyRings/*/keys/*/transactions/*}`   
Gets details of a single Transaction.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*/keyRings/*/keys/*}/transactions`   
Lists Transactions for a Key, or across Keys.  
`[recordSignerDecision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/recordSignerDecision)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/keyRings/*/keys/*/transactions/*}:recordSignerDecision`   
Records a signer's decision to authorize or deny a Transaction.  
  
## REST Resource: [v1beta.projects.locations.instances.teams](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/create)` |  `POST /v1beta/{parent=projects/*/locations/*/instances/*}/teams`   
Creates a new Team in an instance.  
`[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/instances/*/teams/*}`   
Deletes a Team.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/teams/*}`   
Gets details of a single Team.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.teams/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*}/teams`   
Lists Teams in an instance.  
  
## REST Resource: [v1beta.projects.locations.instances.transactionPolicies](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies)

Methods  
---  
`[approve](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/approve)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/transactionPolicies/*}:approve`   
Records a Policy Author's approval for a policy that is waiting to be activated or disabled.  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/create)` |  `POST /v1beta/{parent=projects/*/locations/*/instances/*}/transactionPolicies`   
Proposes a new TransactionPolicy in an instance.  
`[disable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/disable)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/transactionPolicies/*}:disable`   
Starts disabling a policy, or withdraws a policy that is still waiting for activation.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/transactionPolicies/*}`   
Gets details of a single TransactionPolicy, including its Cedar rule, current lifecycle state, and recorded Policy Author approvals.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*}/transactionPolicies`   
Lists TransactionPolicy resources in an instance, including disabled policies.  
  
## REST Resource: [v1beta.projects.locations.instances.users](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users)

Methods  
---  
`[approveRoleChange](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/approveRoleChange)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/users/*}:approveRoleChange`   
Records an Admin's approval of the User's pending role change: the roles in `PENDING_ACTIVE` or `PENDING_DISABLED` in `role_statuses`.  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/create)` |  `POST /v1beta/{parent=projects/*/locations/*/instances/*}/users`   
Creates a new User in an instance.  
`[disable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/disable)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/users/*}:disable`   
Disables a User and all of their roles at once.  
`[disableRole](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/disableRole)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/users/*}:disableRole`   
Disables one role of a User.  
`[enable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/enable)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/users/*}:enable`   
Re-enables a disabled User: sets `state` back to `ACTIVE`.  
`[enableRole](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/enableRole)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/users/*}:enableRole`   
Enables one role of a User: grants it, or re-enables it if it was disabled.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/users/*}`   
Gets details of a single User.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*}/users`   
Lists Users in an instance.  
`[patch](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/patch)` |  `PATCH /v1beta/{user.name=projects/*/locations/*/instances/*/users/*}`   
Updates a User's `display_name`.  
`[updateTeamAssignment](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/updateTeamAssignment)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*/users/*}:updateTeamAssignment`   
Moves a User to a different Team.  
  
## REST Resource: [v1alpha1.projects.locations.instances.mpc.keyRings](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/instances/*}/mpc/keyRings`   
Creates a new KeyRing in a given project and location.  
`[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/instances/*/mpc/keyRings/*}`   
Deletes a KeyRing.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/instances/*/mpc/keyRings/*}`   
Gets details of a single KeyRing.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/instances/*}/mpc/keyRings`   
Lists KeyRings in a given project and location.  
  
## REST Resource: [v1alpha1.projects.locations.instances.mpc.keyRings.keys](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/instances/*/mpc/keyRings/*}/keys`   
Initiates a Distributed Key Generation (DKG) ceremony.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*}`   
Gets details of a single Key.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/instances/*/mpc/keyRings/*}/keys`   
Lists Keys in a given KeyRing.  
`[patch](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/patch)` |  `PATCH /v1alpha1/{key.name=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*}`   
Updates a Key.  
  
## REST Resource: [v1alpha1.projects.locations.instances.mpc.keyRings.keys.proposals](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*}/proposals`   
Initiates a Signing Proposal for a given Key.  
`[fetchProposalSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/fetchProposalSignature)` |  `GET /v1alpha1/{name=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*/proposals/*}:fetchProposalSignature`   
Retrieves the final assembled signature for a completed Proposal.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*/proposals/*}`   
Gets details of a single Proposal.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*}/proposals`   
Lists Proposals for a given Key.  
`[recordParticipantDecision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/recordParticipantDecision)` |  `POST /v1alpha1/{name=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*/proposals/*}:recordParticipantDecision`   
Submits a cryptographic signature from a key participant, recording their assent (or rejection) for the proposal.  
  
## REST Resource: [v1alpha1.projects.locations.instances.mpc.signers](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers)

Methods  
---  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/instances/*}/mpc/signers`   
Registers a new participant entity capable of holding key shares.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/instances/*/mpc/signers/*}`   
Gets details of a single Participant.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/instances/*}/mpc/signers`   
Lists Participants in a given project and location.  
  
## REST Resource: [v1alpha1.projects.locations.instances.policyEngine](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine)

Methods  
---  
`[authorizePayload](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/authorizePayload)` |  `POST /v1alpha1/{instance=projects/*/locations/*/instances/*}/policyEngine:authorizePayload`   
Authorizes an operation proposal payload against active policies.  
`[getPolicyAuthorTrustBundle](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/getPolicyAuthorTrustBundle)` |  `GET /v1alpha1/{name=projects/*/locations/*/instances/*/policyEngine/policyAuthorTrustBundle}`   
Gets details of the PolicyAuthorTrustBundle singleton.  
`[updatePolicyAuthorTrustBundle](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine/updatePolicyAuthorTrustBundle)` |  `PATCH /v1alpha1/{policyAuthorTrustBundle.name=projects/*/locations/*/instances/*/policyEngine/policyAuthorTrustBundle}`   
Updates the PolicyAuthorTrustBundle singleton.  
  
## REST Resource: [v1alpha1.projects.locations.instances.policyEngine.policies](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies)

Methods  
---  
`[addQuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/addQuorumSignature)` |  `POST /v1alpha1/{name=projects/*/locations/*/instances/*/policyEngine/policies/*}:addQuorumSignature`   
Custom Method: Appends a software-backed author signature to a policy.  
`[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/instances/*}/policyEngine/policies`   
Creates a new policy in a given instance.  
`[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/instances/*/policyEngine/policies/*}`   
Gets details of a single policy.  
`[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/instances/*}/policyEngine/policies`   
Lists policies in a given instance.  
`[revoke](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/revoke)` |  `POST /v1alpha1/{name=projects/*/locations/*/instances/*/policyEngine/policies/*}:revoke`   
Custom Method: Revokes (deletes) a policy.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
