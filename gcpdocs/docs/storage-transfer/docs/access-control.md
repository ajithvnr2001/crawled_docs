---
url: https://docs.cloud.google.com/storage-transfer/docs/access-control/
title: Permissions and roles \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:05.864247+00:00
---

# Permissions and roles  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Permissions and roles Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service uses [Identity and Access Management (IAM)](https://cloud.google.com/iam/) permissions and roles to control who can access Storage Transfer Service resources. The main types of resources available in Storage Transfer Service are jobs, operations, and agent pools. In the [IAM policy hierarchy](https://docs.cloud.google.com/iam/docs/overview#policy_hierarchy), jobs are child resources of projects, and operations are child resources of jobs.

To grant access to a resource, you assign one or more [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions) or [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to a user, group, or a [service account](https://docs.cloud.google.com/iam/docs/overview#service_account).

## Permissions

You can grant the following Storage Transfer Service permissions:

### Transfer project permission

Permission | Description  
---|---  
`storagetransfer.projects.getServiceAccount` | Can read the GoogleServiceAccount used by the Storage Transfer Service to access Cloud Storage buckets.  
  
### Transfer job permissions

The following table describes permissions for Storage Transfer Service jobs:

Permission | Description  
---|---  
`storagetransfer.jobs.create` | Can create new transfer jobs.  
`storagetransfer.jobs.delete` | Can delete existing transfer jobs.  
  
Transfer jobs are deleted by calling the **patch** function. However, users must have this permission when deleting transfer jobs to avoid permission errors.   
`storagetransfer.jobs.get` | Can retrieve specific jobs.  
`storagetransfer.jobs.list` | Can list all transfer jobs.  
`storagetransfer.jobs.run` | Can run all transfer jobs.  
`storagetransfer.jobs.update` | Can update transfer job configurations without deleting them.  
  
### Transfer operations permissions

The following table describes permissions for Storage Transfer Service operations:

Permission | Description  
---|---  
`storagetransfer.operations.assign` | Used by transfer agents to assign operations. Not supported in custom roles; grant the predefined `roles/storagetransfer.transferAgent` role instead.  
`storagetransfer.operations.cancel` | Can cancel transfer operations.  
`storagetransfer.operations.get` | Can get details of transfer operations.  
`storagetransfer.operations.list` | Can list all transfer job operations.  
`storagetransfer.operations.pause` | Can pause transfer operations.  
`storagetransfer.operations.report` | Used by transfer agents to report operation status. Not supported in custom roles; grant the predefined `roles/storagetransfer.transferAgent` role instead.  
`storagetransfer.operations.resume` | Can resume paused transfer operations.  
  
### Transfer agent pool permissions

The following table describes permissions for transfer agent pools:

Permission | Description  
---|---  
`storagetransfer.agentpools.create` | Can create agent pools and configure bandwidth limits.  
`storagetransfer.agentpools.update` | Can update agent pools and bandwidth limits.  
`storagetransfer.agentpools.delete` | Can delete agent pools.  
`storagetransfer.agentpools.get` | Can get information and bandwidth limits for specific agent pools.  
`storagetransfer.agentpools.list` | Can list information and bandwidth limits for all agent pools in the project.  
`storagetransfer.agentpools.report` | Used by transfer agents to report status. Not supported in custom roles; grant the predefined `roles/storagetransfer.transferAgent` role instead.  
  
## Predefined roles

This section describes the predefined roles for Storage Transfer Service. Roles are the preferred way of setting IAM permissions.

### Role comparison

You can assign the following Storage Transfer Service predefined roles to principals:

Capability | Storage Transfer Admin  
(`roles/storagetransfer.admin`) | Storage Transfer User  
(`roles/storagetransfer.user`) | Storage Transfer Viewer  
(`roles/storagetransfer.viewer`)  
---|---|---|---  
List and get jobs |  |  |   
Create and configure jobs |  |  |   
Run and update jobs |  |  |   
Delete jobs |  |  |   
List and get transfer operations |  |  |   
Pause, resume, and cancel transfer operations |  |  |   
Read Storage Transfer Service service account details |  |  |   
List and get agent pools |  |  |   
Create and update agent pools |  |  |   
Delete agent pools |  |  |   
Set agent pool bandwidth limits |  |  |   
  
### Role details

The following table describes in detail the predefined roles for Storage Transfer Service:

Role | Description | Included Permissions  
---|---|---  
**Storage Transfer Admin  
(`roles/storagetransfer.admin`)** |  Provides full administrative access to all Storage Transfer Service resources, including creating, updating, running, and deleting transfer jobs and agent pools.  | 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `storagetransfer.*`

  
**Storage Transfer User  
(`roles/storagetransfer.user`)** |  Provides permissions to create, get, update, and run transfer jobs and agent pools within the project. Cannot delete transfer jobs or agent pools, preserving a complete audit record of past transfers.  | 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `storagetransfer.agentpools.create`
  * `storagetransfer.agentpools.get`
  * `storagetransfer.agentpools.list`
  * `storagetransfer.agentpools.report`
  * `storagetransfer.agentpools.update`
  * `storagetransfer.jobs.create`
  * `storagetransfer.jobs.get`
  * `storagetransfer.jobs.list`
  * `storagetransfer.jobs.run`
  * `storagetransfer.jobs.update`
  * `storagetransfer.operations.*`
  * `storagetransfer.projects.getServiceAccount`

  
**Storage Transfer Viewer  
(`roles/storagetransfer.viewer`)** |  Provides read-only access to view and list transfer jobs, operations, and agent pools within the project. Cannot create, run, update, or delete transfers.  | 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `storagetransfer.agentpools.get`
  * `storagetransfer.agentpools.list`
  * `storagetransfer.jobs.get`
  * `storagetransfer.jobs.list`
  * `storagetransfer.operations.get`
  * `storagetransfer.operations.list`
  * `storagetransfer.projects.getServiceAccount`

  
**Storage Transfer Agent (`roles/storagetransfer.transferAgent`) ** |  Gives transfer agents the Storage Transfer Service permissions required to complete a transfer. As of May 1, 2024, `pubsub` permissions are no longer required. Grant this role to the user or service account being used by agents.  | 

  * `logging.logEntries.create`
  * `monitoring.timeSeries.create`
  * `pubsub.subscriptions.consume`
  * `pubsub.subscriptions.create`
  * `pubsub.subscriptions.delete`
  * `pubsub.subscriptions.get`
  * `pubsub.topics.attachSubscription`
  * `pubsub.topics.create`
  * `pubsub.topics.get`
  * `pubsub.topics.list`
  * `pubsub.topics.publish`
  * `storagetransfer.agentpools.report`
  * `storagetransfer.operations.assign`
  * `storagetransfer.operations.get`
  * `storagetransfer.operations.report`

  
**Storage Transfer Service Agent (`roles/storagetransfer.serviceAgent`) ** |  Gives the [ Storage Transfer Service service agent](https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based#service-agent-permissions) the permissions required to create and modify Pub/Sub topics to communicate from Google Cloud to transfer agents. Grant this role to the [ Storage Transfer Service service agent](https://docs.cloud.google.com/storage-transfer/docs/iam-agent-based#service-agent-permissions).  | 

  * `pubsub.subscriptions.consume`
  * `pubsub.subscriptions.create`
  * `pubsub.subscriptions.delete`
  * `pubsub.subscriptions.get`
  * `pubsub.subscriptions.update`
  * `pubsub.topics.attachSubscription`
  * `pubsub.topics.create`
  * `pubsub.topics.delete`
  * `pubsub.topics.get`
  * `pubsub.topics.publish`
  * `pubsub.topics.update`

  
  
## Custom roles

You can create and apply [custom IAM roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) to meet your organization's access requirements.

When creating custom roles, we recommend using a combination of predefined roles to ensure that the correct permissions are included together.

The Google Cloud console will not work properly if the custom role is missing required permissions. For example, some parts of the Google Cloud console assume a role has read access to display an item before editing it, so a role with only write permissions may encounter Google Cloud console screens that don't work.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
