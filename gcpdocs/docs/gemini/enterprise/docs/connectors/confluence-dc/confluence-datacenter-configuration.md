---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenter-configuration/
title: Confluence Data Center configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:31:30.247071+00:00
---

# Confluence Data Center configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenter-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Confluence Data Center configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

To connect Gemini Enterprise to your Confluence Data Center instance, complete the following configuration steps.

## Create a user and grant administrator access

To create a new user and add the user to the administrator group, do the following:

  1. Sign in to your Confluence Data Center instance at the base URL with administrator credentials. The base URL is typically in the format `https://confluence.yourcompany.com`.
  2. To create a new user, follow these steps: 
     1. Click the settings icon settings and select **User management** from the list.
     2. Enter the administrator credentials, if prompted.
     3. In the **Administration** page, click **Create user**.
     4. Enter the email address, full name, username, and password.
     5. Click **Create user**.
  3. To add the newly created user to the administrators group, follow these steps: 
     1. Click **Groups** from the navigation menu.
     2. Search for the `confluence-administrators` group and open it.
     3. Click **Add/Remove Users** and add the newly created user to this group.



## Set up OAuth 2.0 authentication and OAuth scopes

To set up an incoming external application link using OAuth 2.0 in Confluence Data Center and obtain the client ID and client secret, follow these steps. You must have administrator privilege or the help of a Confluence Data Center administrator to complete this step.

  1. Sign in to your Confluence Data Center instance at the base URL with administrator credentials. The base URL is typically in the format `https://confluence.yourcompany.com`.
  2. Click the settings icon and select **Applications** from the list.
  3. In the navigation menu, click **Application links**.
  4. On the **Application links** page, click **Create link**.
  5. In the **Create link** modal, configure the following: 
     * **Application type** : Select **External application**.
     * **Direction** : Select **Incoming**.
     * Click **Continue**.
  6. Configure the OAuth 2.0 details:

     * **Name** : Enter a name for the application link.
     * **Redirect URL** : Enter the following redirect URI:

       * `https://vertexaisearch.cloud.google.com/oauth-redirect`
     * **OAuth scopes** : Select `READ` or `WRITE` based on your specific connection mode:

Connection mode | Scope | Purpose  
---|---|---  
Data ingestion | `READ` | Required to ingest Confluence page content, attachments, and comments.  
Federated search and actions | `WRITE` | Required to search Confluence page content, attachments, and comments, and to upload attachments.  
  7. Click **Continue**. The client ID and client secret are automatically generated and displayed.

     * **Client ID (Consumer Key)** : Copy the unique ID provided.
     * **Client Secret (Shared Secret)** : Copy the client secret and store it securely, for example, in a password manager. The secret is displayed only once. If lost, you must create a new application link to generate new credentials.
  8. Click **Save**. The newly created application link will appear in the list on the **Application links** page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
