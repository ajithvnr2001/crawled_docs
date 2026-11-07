---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/connect-looker/
title: Connect to Looker \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:39:51.983342+00:00
---

# Connect to Looker  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/connect-looker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Connect to Looker Stay organized with collections  Save and categorize content based on your preferences. 

You can connect a data agent to Looker by using the Conversational Analytics API to let users query data in natural language and receive answers that are grounded in your curated LookML models and business logic.

You can use the Python SDK or HTTP to connect to Looker to define your connected Explores and configure authentication credentials.

Data agents that you create with the API are managed as Google Cloud resources and don't appear in the Looker UI. To create and manage data agents in Looker, see [Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents).

## Before you begin

Before you connect a data agent to Looker, complete the following tasks:

  1. [Enable the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api) in your Google Cloud project.
  2. Verify that you have the required Identity and Access Management (IAM) roles.
  3. Ensure that your Looker instance meets the [prerequisites for Conversational Analytics](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api#looker-and-looker-studio-requirements) and that you have access to the LookML models and Explores that you want to query.



### Required roles

To get the permissions that you need to connect a data agent to Looker and query Explores, ask your administrator to grant you the following IAM roles: 

  * Create a persistent data agent: [Gemini Data Analytics Data Agent Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentCreator) (`roles/geminidataanalytics.dataAgentCreator`) on your project 
  * Chat with a persistent data agent: [Gemini Data Analytics Data Agent User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentUser) (`roles/geminidataanalytics.dataAgentUser`) on your project or the data agent 
  * Chat by using inline context: [Gemini Data Analytics Stateless Chat User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentStatelessUser) (`roles/geminidataanalytics.dataAgentStatelessUser`) on your project 
  * Connect to a Looker (Google Cloud core) instance: [Looker Instance User ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.instanceUser) (`roles/looker.instanceUser`) on the project that hosts your Looker (Google Cloud core) instance 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

In addition to IAM roles, you must have appropriate permissions in Looker. To connect to and query Looker Explores, you must be assigned a [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) that contains the `gemini_in_looker` and `access_data` permissions for the LookML models that you interact with.

## Connect to Looker Explores

You can connect up to five Looker Explores at a time with the Conversational Analytics API.

A data agent queries one Explore at a time and can't join data across multiple Explores in a single query. However, an agent can query multiple Explores across a conversation to answer follow-up questions or multi-part prompts. For example, if a prompt requires data from both an `orders` Explore and an `inventory` Explore, the agent queries each one sequentially and combines the results in a single response.

To improve response accuracy, you can optionally define golden queries that guide how the agent queries your Explores. For more information, see [Define data agent context for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker).

The following code samples show how to define a connection to multiple Looker Explores:

### Python SDK
    
    
    looker_instance_uri = "INSTANCE_URI"
    
    looker_explore_reference_1 = geminidataanalytics.LookerExploreReference()
    looker_explore_reference_1.looker_instance_uri = looker_instance_uri
    looker_explore_reference_1.lookml_model = "MODEL"
    looker_explore_reference_1.explore = "EXPLORE"
    
    # Optional: Define additional Explores (up to 5 total)
    looker_explore_reference_2 = geminidataanalytics.LookerExploreReference()
    looker_explore_reference_2.looker_instance_uri = looker_instance_uri
    looker_explore_reference_2.lookml_model = "MODEL_2"
    looker_explore_reference_2.explore = "EXPLORE_2"
    
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.looker.explore_references = [
        looker_explore_reference_1,
        looker_explore_reference_2,
    ]
    

Replace the sample values as follows:

  * INSTANCE_URI: The complete URL of your Looker instance (for example, `https://mycompany.looker.com`).
  * MODEL: The name of the LookML model that includes the Explore that you want to connect to.
  * EXPLORE: The name of the Looker Explore that you want the data agent to query.
  * MODEL_2: An optional second LookML model name if you are connecting multiple Explores. You can repeat this variable for up to five Explores.
  * EXPLORE_2: An optional second Looker Explore name if you are connecting multiple Explores. You can repeat this variable for up to five Explores.



### HTTP
    
    
    looker_instance_uri = "INSTANCE_URI"
    looker_data_source = {
        "looker": {
            "explore_references": [
                {
                    "looker_instance_uri": looker_instance_uri,
                    "lookml_model": "MODEL",
                    "explore": "EXPLORE",
                },
                # Optional: Add up to 5 total Explore references
                {
                    "looker_instance_uri": looker_instance_uri,
                    "lookml_model": "MODEL_2",
                    "explore": "EXPLORE_2",
                },
            ],
        }
    }
    

Replace the sample values as follows:

  * INSTANCE_URI: The complete URL of your Looker instance (for example, `https://mycompany.looker.com`).
  * MODEL: The name of the LookML model that includes the Explore that you want to connect to.
  * EXPLORE: The name of the Looker Explore that you want the data agent to query.
  * MODEL_2: An optional second LookML model name if you are connecting multiple Explores. You can repeat this variable for up to five Explores.
  * EXPLORE_2: An optional second Looker Explore name if you are connecting multiple Explores. You can repeat this variable for up to five Explores.



## Authenticate to Looker

To run queries against your connected Explores, a data agent must authenticate to your Looker instance. Because credentials aren't stored with the data agent, you provide Looker credentials in each chat request, as described in [Build a data agent using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http) and [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).

You can format credentials by using either API keys or an OAuth access token.

### Authenticate with API keys

A Looker API key consists of a client ID and a client secret that are associated with a [Looker user account](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys). When you authenticate by using an API key, the data agent executes queries with the permissions that are assigned to that user account.

The following code samples show how to format credentials by using an API key:

### Python SDK
    
    
    credentials = geminidataanalytics.Credentials()
    credentials.oauth.secret.client_id = "CLIENT_ID"
    credentials.oauth.secret.client_secret = "CLIENT_SECRET"
    

Replace the sample values as follows:

  * CLIENT_ID: The client ID of your Looker API key.
  * CLIENT_SECRET: The client secret of your Looker API key.



### HTTP
    
    
    looker_credentials = {
        "oauth": {
            "secret": {
                "client_id": "CLIENT_ID",
                "client_secret": "CLIENT_SECRET",
            }
        }
    }
    

Replace the sample values as follows:

  * CLIENT_ID: The client ID of your Looker API key.
  * CLIENT_SECRET: The client secret of your Looker API key.



### Authenticate with an access token

If your application uses OAuth to authenticate to Looker, you can provide an access token in your credentials rather than an API key.

The following code samples show how to format credentials by using an access token:

### Python SDK
    
    
    credentials = geminidataanalytics.Credentials()
    credentials.oauth.token.access_token = "ACCESS_TOKEN"
    

Replace ACCESS_TOKEN with the [OAuth access token](https://docs.cloud.google.com/looker/docs/api-auth#authentication_without_an_sdk) that you generate to authenticate to Looker.

**Tip:** Store the Looker access token as an environment variable for improved security.

### HTTP
    
    
    looker_credentials = {
        "oauth": {
            "token": {
                "access_token": "ACCESS_TOKEN",
            }
        }
    }
    

Replace ACCESS_TOKEN with the [OAuth access token](https://docs.cloud.google.com/looker/docs/api-auth#authentication_without_an_sdk) that you generate to authenticate to Looker.

**Tip:** Store the Looker access token as an environment variable for improved security.

## What's next

  * [Define data agent context for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker) to add golden queries and improve response accuracy.
  * Create a data agent that queries your connected Looker Explores, or send stateless chat queries, as described in [Build a data agent using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http) or [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk).
  * [Configure customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek) to protect your data agent resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
