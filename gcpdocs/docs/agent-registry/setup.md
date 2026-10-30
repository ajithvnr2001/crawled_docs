---
url: https://docs.cloud.google.com/agent-registry/setup/
title: Set up Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:40:09.335726+00:00
---

# Set up Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Set up Agent Registry Stay organized with collections  Save and categorize content based on your preferences. 

To register and discover your AI agents, Model Context Protocol (MCP) servers, standalone skills, and endpoints in Agent Registry, you must enable the Agent Registry API in your Google Cloud project. The project where you enable Agent Registry serves as your [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project).

You can set up Agent Registry in a single governance project or across multiple projects by configuring a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) where a central [management project](https://docs.cloud.google.com/agent-registry/boundaries-and-topology#management-project) serves as your governance project.

## Before you begin

Configure Agent Registry either in a single project or across multiple projects:

  * **Single project** : discover and manage agents, MCP servers, skills, and endpoints in a single Google Cloud governance project. Use an existing project or [create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), enable the Agent Registry API, and grant permissions.
  * **Multiple projects (management boundary)** : centralize discovery and governance across multiple member projects in your [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) by associating a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology) with a [management project](https://docs.cloud.google.com/agent-registry/boundaries-and-topology#management-project). Designate an existing Google Cloud project as your management project or let Resource Manager create one for you, enable the Resource Manager API, configure a management boundary, and grant permissions.



### Required roles

To get the permissions that you need to set up Agent Registry, ask your administrator to grant you the following IAM roles on your Google Cloud project: 

  * Enable the Agent Registry API: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 
  * Grant roles for using the Agent Registry API: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * Get full access to Agent Registry API resources: [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.admin) (`roles/agentregistry.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up your Google Cloud CLI environment

If you plan to use the gcloud CLI for Agent Registry, follow these steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Update the gcloud CLI to the most recent version with the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command:
         
         gcloud components update
         

  3. If you plan to use [Preview](https://cloud.google.com/products#product-launch-stages) features, install the `alpha` component with the [`gcloud components install`](https://docs.cloud.google.com/sdk/gcloud/reference/components/install) command:
         
         gcloud components install alpha
         




## Enable the Agent Registry API

  * **For a single project** : enable the Agent Registry API on your governance project. After you enable the API and grant permissions, you can begin registering and discovering agents in that project. You don't need to configure a management boundary.
  * **For multiple projects (management boundary)** : enable the Resource Manager API on the project that you use to run configuration commands. When you configure a management boundary for multiple projects and create the capability configuration, Resource Manager automatically enables the Agent Registry API on your [management project](https://docs.cloud.google.com/agent-registry/boundaries-and-topology#management-project).



Use [your project ID](https://support.google.com/googleapi/answer/7014113) to enable APIs:

###  Console 

For a single project, enable the Agent Registry API on your project:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=agentregistry.googleapis.com&redirect=https%3A//console.cloud.google.com)

For multiple projects (management boundary), enable the Resource Manager API on the project that you use for configuration:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

###  gcloud 

  * For a single project, enable the Agent Registry API on your project with the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command:
        
        gcloud services enable agentregistry.googleapis.com \
            --project=PROJECT_ID
        

  * For multiple projects (management boundary), enable the Resource Manager API on the project that you use for configuration:
        
        gcloud services enable cloudresourcemanager.googleapis.com \
            --project=PROJECT_ID
        




Replace `PROJECT_ID` with [the project ID](https://support.google.com/googleapi/answer/7014113) of your standalone governance project, or the project that you want to use as the management project for your management boundary.

**Note:** If you integrate Agent Registry with [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway) for policy enforcement, you must also enable the Identity-Aware Proxy API in your project. The gateway uses the Identity-Aware Proxy API to authenticate and authorize egress traffic from your agents to external destinations.

## Configure a management boundary for multiple projects

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use Agent Registry across multiple Google Cloud projects, configure a [management boundary](https://docs.cloud.google.com/agent-registry/boundaries-and-topology). A management boundary groups one or more Google Cloud member projects into a central [management project](https://docs.cloud.google.com/agent-registry/boundaries-and-topology#management-project) that serves as your governance project so that you can discover and govern AI agents, MCP servers, and tools across projects.

You define a management boundary in [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/boundaries-and-capabilities-overview). For step-by-step instructions, see [Configure management boundaries](https://docs.cloud.google.com/resource-manager/docs/manage-capability-configs) in the Resource Manager documentation.

For an architectural overview of how `BoundaryConfig`, `Boundary`, and `CapabilityConfig` resources work together, see [Cross-project boundaries](https://docs.cloud.google.com/agent-registry/boundaries-and-topology).

When you create a `CapabilityConfig` resource with `agent-management`, Resource Manager automatically enables `agentregistry.googleapis.com` on the management project. After establishing your management boundary:

  1. If needed for local operations within individual member projects, enable the Agent Registry API on those member projects.
  2. Grant the required [roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions#boundary-roles) to users and service accounts on the management project.



When you list or search for agents or MCP servers in a location on the management project, Agent Registry aggregates and returns auto-discovered resources in that location from all member projects in the boundary, alongside any registered `Service` resources created directly in that location on the management project. Each returned [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) preserves the component's ID and uses the project specified in the request.

## Grant permissions

To view and manage resources in Agent Registry, you must grant users the appropriate [Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

Grant your users one or more of the following Agent Registry roles:

  * **Agent Registry API Viewer** (`roles/agentregistry.viewer`): view and search agents, MCP servers, tools, standalone skills, skill revisions, publishers, endpoints, and bindings.
  * **Agent Registry API Editor** (`roles/agentregistry.editor`): view and edit Agent Registry resources, including registering, updating, and deleting agents, MCP servers, tools, endpoints, standalone skills, and skill revisions.
  * **Agent Registry API Admin** (`roles/agentregistry.admin`): perform all actions on Agent Registry resources, including registering and managing agents, MCP servers, tools, endpoints, standalone skills, skill revisions, bindings, and skill IAM policies.
  * **Agent Registry User** (`roles/agentregistry.user`): view all Agent Registry resources, and create, update, and delete standalone skills and skill revisions without edit access to agents, MCP servers, or endpoints.



To learn how to grant IAM roles on a project, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** Agent Registry and Agent Gateway have limited support for Workforce Identity Federation. If you encounter loading or authorization errors in the Google Cloud console, access the service with a standard Google Account managed through Cloud Identity or Google Workspace.

## Change your Agent Registry project

If you want to change the project where you use Agent Registry and remove dependencies from the old project, disable the Agent Registry API in the old project. After you have disabled the Agent Registry API in the old project, you can enable it in another project. Your data isn't migrated, and you must recreate your resources in this new project.

## Disable the Agent Registry API

If you no longer want to use Agent Registry, disable the Agent Registry API on the project:

###  Console 

  1. In the Google Cloud console, go to the Agent Registry API management page:

[Go to Agent Registry API](https://console.cloud.google.com/apis/api/agentregistry.googleapis.com/overview)

  2. From the project picker, select the Google Cloud project where you set up Agent Registry.

  3. Click **Disable API**.

  4. In the confirmation dialog, click **Disable**.




###  gcloud 

Disable the Agent Registry API in your project with the [`gcloud services disable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/disable) command:
    
    
    gcloud services disable agentregistry.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with [the ID of the project](https://support.google.com/googleapi/answer/7014113).

## What's next

  * [Learn about cross-project boundaries](https://docs.cloud.google.com/agent-registry/boundaries-and-topology)
  * [Quickstart: Register an agent](https://docs.cloud.google.com/agent-registry/quickstart-register-agent)
  * [Register MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers)
  * [Register skills](https://docs.cloud.google.com/agent-registry/register-skills)
  * [Search for agents, tools, and skills](https://docs.cloud.google.com/agent-registry/search-agents-and-tools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
