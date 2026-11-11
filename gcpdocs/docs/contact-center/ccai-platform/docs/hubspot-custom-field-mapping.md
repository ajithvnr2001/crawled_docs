---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-custom-field-mapping/
title: HubSpot custom field mapping \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:09:07.382586+00:00
---

# HubSpot custom field mapping  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-custom-field-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  HubSpot custom field mapping Stay organized with collections  Save and categorize content based on your preferences. 

HubSpot Custom Field Mapping extends existing [Custom Field Mapping](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-custom-field-mapping) functionality (previously available for Salesforce, Zendesk, and Kustomer) of CCAI Platform session data to HubSpot.

Use this feature to:

  * Map custom data sent from CCAI Platform SDKs (mobile or web) or the [Apps API (Chat)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-endpoints#send-custom-data-chat) `Send custom data in a chat` endpoint to HubSpot custom properties.

  * Automatically populate HubSpot Ticket or Deal fields with CCAI Platform session data (for example, customer ID, queue name, or any other custom parameter you pass using the SDK or Apps API).

  * Maintain CRM parity across platforms by using the same Custom Field Mapping workflow you may already use for other CRMs.




This guide covers how to:

  * Access the Custom Field Mapping page for HubSpot.

  * Create, edit, and delete custom field mappings.

  * Understand how mappings behave at runtime and how to verify they are working.




## Before you begin

Before you begin, ensure these requirements are met.

### Account and licensing

  * You must have a HubSpot account connected to CCAI Platform as the CRM Agent Platform.

  * HubSpot Ticket or Deal objects must have any required custom properties already created in HubSpot (this feature does not create properties in HubSpot for you).




### System and user setup

The following system and user setup is required to configure custom field mappings:

  * **Administrator permissions**. You must be logged into CCAI Platform with an account that has Administrator permissions.


  1. Access: **Settings > Operation Management**.

  2. Manage CRM configuration.



  * **HubSpot configured as CRM**.


  1. In your CCAI Platform Admin Portal, HubSpot must be selected as the CRM Agent Platform.

  2. The HubSpot integration must be fully authorized and connected.



  * **Configure the data source**.

  * Your web or mobile SDK implementation or Apps API (Chat) integration must send custom data fields that you want to map into HubSpot.

  * You must know the custom data key (top-level key name in the payload) for each field you plan to map (for example, `customer_id`, `plan_type`).




### Content and assets (optional)

You need a list of HubSpot custom properties (Ticket or Deal) that you want to populate with CCAI Platform data.

## Create a HubSpot custom field mapping

To create a HubSpot custom field mapping, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Custom Field Mapping** pane, and then click **View all**. The **Custom Field Mapping** page appears.

  3. Click **Add CRM Field Mapping**. The **Add CRM custom field** dialog appears.

  4. In the **Field Mapping Title** field, enter a descriptive name for the custom field. See the following examples:

     * For a customer ID: `HubSpot ticket customer ID`

     * For a queue name: `HubSpot deal queue name`

  5. In the **Custom Field Name** field, enter the name of the HubSpot custom field that you want the SDK custom field data to be written to.

  6. Click the **Custom Data Field Label** field. A list of SDK custom data field labels appears.

  7. Select the name of the SDK custom data field to map to the HubSpot custom field. At runtime, when the SDK sends this custom data, the system writes it to the mapped HubSpot custom field.

  8. Click **Save**. The new mapping appears on the **Custom Field Mapping** page.




## Edit a HubSpot custom field mapping

To edit a HubSpot custom field mapping, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Custom Field Mapping** pane, and then click **View all**.

  3. Click edit **Edit** for the mapping that you want to edit. The **Edit CRM custom field** dialog appears.

  4. Edit the mapping, and then click **Save**.




## Delete a HubSpot custom field mapping

To delete a HubSpot custom field mapping, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Custom Field Mapping** pane, and then click **View all**.

  3. Click close **Delete** for the mapping that you want to delete.

  4. Confirm the deletion.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
