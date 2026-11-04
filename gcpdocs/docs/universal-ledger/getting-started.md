---
url: https://docs.cloud.google.com/universal-ledger/getting-started/
title: Getting started with the Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:21.598081+00:00
---

# Getting started with the Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Getting started with the Universal Ledger Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to onboard to a Universal Ledger network and enable the Universal Ledger API in your Google Cloud projects.

## Onboarding request

Before submitting transactions to a network, you must first create a Universal Ledger account. Review the [Product overview](https://docs.cloud.google.com/universal-ledger/overview) page to familiarize yourself with the various manager and operator account types.

Ledger accounts must be created by a privileged administrator account on the ledger. Check the guide to [Identify who can create your account](https://docs.cloud.google.com/universal-ledger/how-to/request-account#identify-creator) so you can send them the required onboarding details.

To set up a Currency Operator account, or to discuss your use case, contact us at [gcul-help@google.com](mailto:gcul-help@google.com).

## Enabling the API

You can enable the Universal Ledger API using `gcloud`, and assign granular access to your team members using specific IAM roles.

  1. **Enable the API using gcloud**

To enable the API, use the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable):
         
         gcloud services enable universalledger.googleapis.com \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project where you want to enable the API.

If you are a project owner, you should now be able to send requests to the API.

  2. **Set up granular access using IAM roles**

To manage granular access to the Universal Ledger API for other members of your organization, you may assign them IAM roles. The API has three IAM roles configured, each providing different layers of access:

     * `roles/universalledger.viewer`: Read-only access to available endpoints and networks. Grants the ability to view the endpoints, and query the network using an endpoint.
     * `roles/universalledger.editor`: Full access to available endpoints and networks. Grants access to query the networks and submit transactions.
     * `roles/universalledger.admin`: Full access to available endpoints and networks. Grants the access to query the networks and submit transactions. This role has the same permissions as the Universal Ledger Editor role, subject to change in the future.

To add a new IAM role to a user, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="PRINCIPAL" \
        --role="ROLE"
    

Replace the following:

     * `PROJECT_ID`: the project where to add the IAM policy binding
     * `PRINCIPAL`: the principal to whom the role is added, for example: `user:test-user@gmail.com` or `serviceAccount:test123@example.domain.com`.
     * `ROLE`: one of the previously described roles to assign to the principal



## Sending your first request

Now you can start using the API!

To validate that the previous configuration is working correctly, first authenticate using the [`gcloud auth application-default login` command](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login):
    
    
    gcloud auth application-default login
    

Then try sending an [`endpoints.list` request](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/list):
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -X GET "https://universalledger.us-central1.rep.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/endpoints"
    

Requests to a given Universal Ledger network are sent using API endpoints, which will have the form
    
    
    https://universalledger.REGION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/endpoints/NETWORK_NAME
    

Completing these steps validates your access to the Universal Ledger API.

## What's next

  * Review the list of available [Universal Ledger networks and regions](https://docs.cloud.google.com/universal-ledger/locations).
  * Request the [creation of an account on the ledger](https://docs.cloud.google.com/universal-ledger/how-to/request-account).
  * Learn how to [send RPC requests with Python](https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
