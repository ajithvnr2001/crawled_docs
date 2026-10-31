---
url: https://docs.cloud.google.com/developer-connect/docs/control-repository-access-with-tags/
title: Control repository access with tags and deny policies \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:00.586395+00:00
---

# Control repository access with tags and deny policies  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/control-repository-access-with-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Control repository access with tags and deny policies Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Identity and Access Management (IAM) deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) along with tags to block specific operations on the Git repository links in a Developer Connect connection.

You attach a tag to a connection, and then create a deny policy whose condition matches that tag. Every Git repository link in the connection inherits the tag, so the deny policy applies to all repositories that are linked through that connection.

## When to use tags and deny policies

IAM allow policies grant permissions. Deny policies let you set guardrails that take precedence over allow policies, regardless of which roles a principal has. Combining deny policies with tags lets you apply those guardrails to selected connections, instead of to every connection in a project.

For example, you can use this approach to do the following:

  * Let an AI agent or an automation service account read commits and pull requests through Developer Connect, but prevent it from opening, modifying, or commenting on pull requests in production repositories.
  * Block all repository operations for a group of principals on connections that link to sensitive repositories, while keeping their access to other connections in the same project.
  * Apply a consistent set of restrictions across many projects by creating the tag and the deny policy at the organization level.



## How tags apply to Git repository links

In Developer Connect, you can attach tags to connections, but not directly to Git repository links.

A Git repository link is a child resource of its connection. When IAM evaluates a deny policy for an operation on a Git repository link, the condition is evaluated against the link's effective tags. The effective tags include the tags that are attached to the parent connection, and the tags that [are inherited](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance) from the connection's project, folder, and organization.

Because Git repository links inherit tags from their connection, the controls in this document apply per connection. If you need different controls for different repositories, link those repositories through different connections, and then tag each connection separately.

## Before you begin

  * Make sure that you have a Developer Connect [connection](https://docs.cloud.google.com/developer-connect/docs/connect-repo) with at least one linked Git repository.
  * Make sure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) and the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project that contains the connection.
  * To use the command-line examples in this document, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).



### Required roles

To get the permissions that you need to create tags, attach tags to connections, and create deny policies, ask your administrator to grant you the following IAM roles on the organization: 

  * To create and manage tag keys and tag values: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) 
  * To attach a tag value to a connection: Tag User (`roles/resourcemanager.tagUser`) on the tag value, and Developer Connect Admin (`roles/developerconnect.admin`) on the connection 
  * To create, update, and delete deny policies: [Deny Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyAdmin) (`roles/iam.denyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** The Owner role (`roles/owner`) on a project doesn't include the permissions to create deny policies. The Deny Admin role can only be granted on an organization.

## Permissions that you can deny

You can deny the following permissions on Git repository links. In a deny policy, use the format `developerconnect.googleapis.com/gitRepositoryLinks.PERMISSION`.

### Read repository data

Permission | Lets a principal  
---|---  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchCommit` | Get a commit.  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchCommitList` | List commits.  
`developerconnect.googleapis.com/gitRepositoryLinks.diffCommit` | Get the diff between commits.  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchFileBlame` | Get blame information for a file.  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchPullRequest` | Get a pull request.  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchPullRequestList` | List pull requests.  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchGitRefs` | List branches and tags.  
  
### Change repository data

Permission | Lets a principal  
---|---  
`developerconnect.googleapis.com/gitRepositoryLinks.openPullRequest` | Open a pull request.  
`developerconnect.googleapis.com/gitRepositoryLinks.modifyPullRequest` | Modify a pull request, for example, its title, description, or state.  
`developerconnect.googleapis.com/gitRepositoryLinks.addPullRequestComment` | Add a comment to a pull request.  
`developerconnect.googleapis.com/gitRepositoryLinks.addPullRequestReviewComment` | Add a review comment to a pull request.  
  
### Access tokens and the Git proxy

Permission | Lets a principal  
---|---  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchReadToken` | Get a read-only access token for the repository.  
`developerconnect.googleapis.com/gitRepositoryLinks.fetchReadWriteToken` | Get a read-write access token for the repository.  
`developerconnect.googleapis.com/gitRepositoryLinks.gitProxyRead` | Read from the repository through the [Developer Connect proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy).  
`developerconnect.googleapis.com/gitRepositoryLinks.gitProxyWrite` | Write to the repository through the Developer Connect proxy.  
**Caution:** A principal that can get an access token or use the Developer Connect proxy can call your source code management system directly. If you deny a write permission such as `openPullRequest`, also deny `fetchReadWriteToken` and `gitProxyWrite` for the same principals. Otherwise, those principals might be able to make the same change outside of Developer Connect.

For the full list of permissions that deny policies support, see [Permissions supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).

## Create a tag and attach it to a connection

In this example, you create a tag key named `scm-agent-access` with a tag value named `read-only`, and then attach the tag value to a connection.

  1. Create the tag key. The following command creates the tag key in your organization, so that you can use it on connections in any project:
         
         gcloud resource-manager tags keys create scm-agent-access \
             --parent=organizations/ORGANIZATION_ID \
             --description="Controls agent access to Developer Connect repositories"

Replace ORGANIZATION_ID with your organization ID.

You can also create the tag key in a project by setting `--parent` to `projects/PROJECT_ID`. A project-level tag key can only be attached to resources in that project.

  2. Create the tag value:
         
         gcloud resource-manager tags values create read-only \
             --parent=ORGANIZATION_ID/scm-agent-access

  3. Attach the tag value to the connection:
         
         gcloud resource-manager tags bindings create \
             --tag-value=ORGANIZATION_ID/scm-agent-access/read-only \
             --parent=//developerconnect.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/connections/CONNECTION_ID \
             --location=LOCATION

Replace the following:

     * PROJECT_NUMBER: the project number of the project that contains the connection.
     * LOCATION: the region of the connection, for example, `us-central1`.
     * CONNECTION_ID: the ID of the connection.
  4. Verify that the tag is attached to the connection:
         
         gcloud resource-manager tags bindings list \
             --parent=//developerconnect.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/connections/CONNECTION_ID \
             --location=LOCATION




For more information about creating and attaching tags, see [Create and manage tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

## Create a deny policy

The following deny policy prevents a service account from opening, modifying, or commenting on pull requests, and from getting read-write tokens or writing through the Developer Connect proxy, in any Git repository link whose connection has the `scm-agent-access` tag set to `read-only`. The service account can still read commits and pull requests, if an allow policy grants it those permissions.

  1. Create a file named `policy.json` with the following content:
         
         {
           "displayName": "Read-only Developer Connect access for agents",
           "rules": [
             {
               "denyRule": {
                 "deniedPrincipals": [
                   "principal://iam.googleapis.com/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL"
                 ],
                 "deniedPermissions": [
                   "developerconnect.googleapis.com/gitRepositoryLinks.openPullRequest",
                   "developerconnect.googleapis.com/gitRepositoryLinks.modifyPullRequest",
                   "developerconnect.googleapis.com/gitRepositoryLinks.addPullRequestComment",
                   "developerconnect.googleapis.com/gitRepositoryLinks.addPullRequestReviewComment",
                   "developerconnect.googleapis.com/gitRepositoryLinks.fetchReadWriteToken",
                   "developerconnect.googleapis.com/gitRepositoryLinks.gitProxyWrite"
                 ],
                 "denialCondition": {
                   "title": "Connection is tagged scm-agent-access=read-only",
                   "expression": "resource.matchTag('ORGANIZATION_ID/scm-agent-access', 'read-only')"
                 }
               }
             }
           ]
         }

Replace SERVICE_ACCOUNT_EMAIL with the email address of the service account that you want to restrict. To restrict other types of principals, such as users or groups, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

  2. Create the deny policy and attach it to your organization:
         
         gcloud iam policies create scm-agent-read-only \
             --attachment-point=cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID \
             --kind=denypolicies \
             --policy-file=policy.json

You can also attach the deny policy to a folder or a project. A deny policy applies to all of the resources under its attachment point.




For more information about creating deny policies, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).

## Verify the deny policy

Changes to tags and deny policies are eventually consistent. It can take several minutes for a new tag binding or deny policy to take effect. For more information, see [Impact of tag changes](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#propagation) and [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

After the changes propagate, a request from the denied principal for a denied permission on a Git repository link in the tagged connection fails with an HTTP `403` `PERMISSION_DENIED` error. The error message names the permission and the Git repository link, and states that access was denied by an IAM deny policy. For example:
    
    
    Permission 'developerconnect.gitRepositoryLinks.openPullRequest' denied on resource '//developerconnect.googleapis.com/projects/my-project/locations/us-central1/connections/my-connection/gitRepositoryLinks/my-repo' due to an IAM deny policy.
    

Requests for permissions that the policy doesn't deny, and requests for Git repository links in connections that don't have the tag, aren't affected by the deny policy.

To check whether the deny policy applies to a principal and a Git repository link, use [Policy Troubleshooter](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access):
    
    
    gcloud policy-intelligence troubleshoot-policy iam \
        //developerconnect.googleapis.com/projects/PROJECT_ID/locations/LOCATION/connections/CONNECTION_ID/gitRepositoryLinks/GIT_REPOSITORY_LINK_ID \
        --principal-email=SERVICE_ACCOUNT_EMAIL \
        --permission=developerconnect.googleapis.com/gitRepositoryLinks.openPullRequest

## Remove the restriction

To remove the restriction from a single connection, delete the tag binding from the connection:
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=ORGANIZATION_ID/scm-agent-access/read-only \
        --parent=//developerconnect.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/connections/CONNECTION_ID \
        --location=LOCATION

To remove the restriction from all connections, delete the deny policy:
    
    
    gcloud iam policies delete scm-agent-read-only \
        --attachment-point=cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID \
        --kind=denypolicies

## Limitations

  * **Tags are attached per connection.** You can attach tags to connections, but not to Git repository links. All Git repository links in a connection share the connection's tags.
  * **Deny conditions only support tags.** The condition in a deny rule can only use tag functions, such as `resource.matchTag()` and `resource.hasTagKey()`. You can't write a deny condition based on the repository name or other resource attributes. For details, see [Denial conditions](https://docs.cloud.google.com/iam/docs/deny-overview#denial-conditions).
  * **Tag keys must be namespaced.** In `resource.matchTag()`, identify the tag key by its namespaced name, such as `ORGANIZATION_ID/scm-agent-access` or `PROJECT_ID/scm-agent-access`, not by its short name.
  * **Changes take time to propagate.** New tag bindings, changed tag values, and deny policies don't take effect immediately, and removing a tag doesn't restore access immediately. Allow several minutes for each change, and test your configuration before you rely on it.
  * **Effective tags are listed on connections.** To view the tags that apply to a Git repository link, list the effective tags of its parent connection.



## What's next

  * Learn more about [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).
  * Learn more about [tags and conditional access](https://docs.cloud.google.com/iam/docs/tags-access-control).
  * Learn about [Developer Connect roles and permissions](https://docs.cloud.google.com/developer-connect/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
