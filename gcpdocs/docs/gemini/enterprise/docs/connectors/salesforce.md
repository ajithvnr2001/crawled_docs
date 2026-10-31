---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T06:00:25.235915+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Salesforce connector for Gemini Enterprise lets you search and act on your Salesforce records using natural language. End users can query accounts, contacts, opportunities, cases, leads, and custom objects, and create, update, and delete records without leaving Gemini Enterprise.

To connect Salesforce, your Salesforce administrator enables the **SObject All** MCP server in your organization and configures one of two OAuth 2.0 authentication methods:

  * **Google-managed OAuth (default)** : Install the [Gemini Enterprise - Salesforce Connector](https://appexchange.salesforce.com/appxListingDetail?listingId=ee18ab11-351b-4178-b6af-3573d35e2d29) managed package from Salesforce AppExchange. You don't create your own OAuth application or provide a client ID and client secret.
  * **Bring your own app** : Create and configure your own external client app in Salesforce, and provide its client ID and client secret when you set up the data store.



For more information, see [Salesforce configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration).

## Supported actions

When the Salesforce data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

The following actions read Salesforce data and are enabled by default:

Action | Description  
---|---  
Soql Query | Runs a SOQL query against standard and custom objects in your Salesforce organization.  
Find | Runs a full-text search across Salesforce records.  
Get Object Schema | Returns an index of the objects in your organization, or the fields and picklist values of a specific object.  
Get Related Records | Returns the records reached from a record through a relationship.  
List Recent Sobject Records | Returns the records of an object that were viewed or modified most recently.  
Get User Info | Returns the identity, role, and preferences of the current user.  
  
The following actions change Salesforce data and are turned off by default until an administrator enables them:

Action | Description  
---|---  
Create Sobject Record | Creates a record of any object type in Salesforce.  
Update Sobject Record | Updates the fields of an existing record.  
Update Related Record | Updates the record reached from a record through a to-one relationship.  
Delete Sobject Record | Deletes a record. Deleted records go to the Salesforce Recycle Bin.  
Delete Related Record | Deletes the record reached from a record through a to-one relationship.  
  
Actions run with the permissions of the user who authorized the connector. A user can only read and change the records that they can already read and change in Salesforce.

## Limitations

The Salesforce data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Salesforce data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * Static IP addresses aren't supported for the Salesforce data store. Instead, login IP policy for authentication and token refresh requests is configured on the app in Salesforce, and data requests are authorized using the user's valid access token. For more information, see [Set the login IP policy for the app](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration#ip-policy).



## What's next

  * To enable the MCP server and configure OAuth authentication in Salesforce before anyone can authorize the connector, see [Salesforce configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration).

  * To create and configure a data store with Salesforce, see [Set up a Salesforce data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
