---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-custom-field-mapping/
title: Custom CRM field mapping (Salesforce, Zendesk, Kustomer) \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:23:48.574379+00:00
---

# Custom CRM field mapping (Salesforce, Zendesk, Kustomer)  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-custom-field-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Custom CRM field mapping (Salesforce, Zendesk, Kustomer) Stay organized with collections  Save and categorize content based on your preferences. 

In order to allow metadata from CRM records to be analyzed quickly, the CCAI Platform Web and Mobile SDKs — and Apps API (Chat) — can push data into CRM custom fields.

**Custom field mapping** lets you map **CCAI Platform custom data keys** (Portal UI: **Custom Data Field Label**) to CRM fields or properties so the mapped values are automatically written to the appropriate CRM record.

Custom data keys can be provided by:

  * CCAI Platform Web and Mobile SDKs, or

  * Apps API (chat) using the [Send custom data in a chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-endpoints#send-custom-data-chat) endpoint.

**Note:** This document only documents Apps API support for chats. While the Apps API also exposes custom data endpoints for calls, the behavior of CRM custom field mapping for calls isn't covered here unless explicitly confirmed.



## Mobile SDK API example

The following sections outline an example specific to the mobile SDK.

### Data from SDK to server
    
    
    {
        custom_data: { # same format with previous custom data from SDK
            data_name: {
                value: value,
                type: string,
                label: "Data Name",
            },
            device: { # example
                value: "iOS",
                type: "string",
                label: "Device Type"}
        }
    }
    

### Data from server to CRM adaptor
    
    
    {
        key: {
            crm_field: "crm custom field name",
            type: "text", # text / checkbox ...,
            value: "value"
        },
        device: { # example
            crm_field: "device",
            type: "text", 
            value: "iOS"
        }
    }
    

## API endpoint

The CRM custom field mapping can be accessed using an API. The following endpoints are available:

  * **Retrieve all fields** : HTTP POST or GET: `/crm_custom_fields`

  * **Update or delete a specific field** : HTTP PUT or DELETE `/crm_custom_fields/:id`




## Apps API (chat) example (no SDK)

Customers using the **Apps API** directly (without CCAI Platform Web or Mobile SDKs) can still use **custom field mapping** for **chat** interactions by sending custom data for an existing chat session.

  * Endpoint: `POST /apps/api/v1/chats/:id/custom_data`



### Request body (unsecured / unsigned)
    
    
    {
      "signed": false,
      "data": {
        "orderId": {
          "label": "Order ID",
          "value": "12345"
        },
        "customerTier": {
          "label": "Customer Tier",
          "value": "gold"
        }
      }
    }
    

### Request body (secured / signed JWT)
    
    
    {
      "signed": true,
      "signed_data": "<JWT>"
    }
    

**Note:** In signed mode, the HTTP request body contains `signed_data`, and the JWT payload contains `custom_data`.

### JWT payload shape (example)
    
    
    {
      "custom_data": {
        "orderId": { "label": "Order ID", "value": "12345" },
        "customerTier": { "label": "Customer Tier", "value": "gold" }
      },
      "exp": 1734567890,
      "iat": 1734560000
    }
    

## Apply custom field mapping to Apps API payloads

In the CCAI Platform Portal, set **Custom Data Field Label** (custom data key) to the **top-level key** under the Apps API payload `data` object (for example, `orderId` or `customerTier`) and map it to the selected CRM field or property.

Here are two examples:

  * Maps by key: `orderId`, `customerTier`
  * Doesn't map by nested label: `"label": "Order ID"` is display text and isn't used for mapping.

**Tip:** The mapping is driven by the key name and the associated value. If a `label` is present, treat it as descriptive text only.

### Reserved keys (customer flags)

You may see reserved keys such as:

  * `reserved_verified_customer`

  * `reserved_bad_actor`

  * `reserved_repeat_customer`




These keys are primarily used for customer-flag behavior. To avoid confusion, don't map `reserved_*` keys as CRM custom fields unless you have a specific reporting need. Prefer mapping business-specific keys (like `orderId`, `customerTier`, etc.) for CRM custom field mapping.

## Steps to configure custom CRM field mapping

  1. Create the custom field and values in your CRM.

  2. Assign the new values to contacts in your CRM.

  3. Configure the setting in the CCAI Platform portal.

  4. Test.




### Zendesk configuration

The following sections outline the process to configure field mappings for the Zendesk CRM.

#### Create a custom field for User (Contact)

  1. Sign in to Zendesk as an Admin.

  2. Click the  settings  to access the Admin options.

  3. Select **User Fields**.

  4. Select the field type that you want to create.

![Select field type](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/select-field-type.png)

  5. Add a field title and name within an agent's view.

**Note:** We recommend using the same value as the `crm_field` from the API.

**Field key** is filled automatically.

  6. Click **Create field**.




You can now see this new field in the **Active fields** list, and this new field appears in the left-side column when viewing a user.

![Active fields display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23da0486.png)

#### Create a custom field for Ticket

  1. Sign in to Zendesk as an Admin.

  2. Click the  settings  icon to access the Admin options.

  3. Select **Ticket Fields**.

  4. Click the **add custom field** button.

  5. Select a field type that you want to create by clicking **select**.

  6. Add a **Field Title**. The **Field Title** will appear in your Agent's view.

We recommend using the same value as the **crm_field** from the API.

![Field title display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23da700b.png)

  7. Click the **Add field** button.




You can now see this new field in the **Active fields** list, and this new field appears in the left side column when viewing a ticket.

### Salesforce configuration

  1. Go to **Setup**.

  2. Select **Object Manager**.

  3. Choose the object on which you want to append custom fields (Case or CCAI Platform Session).

  4. Click **Fields & Relationships**.

  5. Click **New**.

  6. Select **Text** as the Data Type.

  7. In **Field Label** , enter a name for the field.

  8. In **Length** , enter **255**.

**Field Name** should automatically populate after you enter **Field Label**.

![Field label display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23daa480.png)

You may leave the rest of the variables at their default value.

  9. Click **Next**.

  10. Check the **Visible** box for any of the profiles that access the object (Case or CCAI Platform Session).

  11. Click **Next**.

  12. Click **Save**.

  13. This will take you back to the **Fields & Relationships** view. Find the field that you just created, and take note of the **Field Name**.

![Fields and relationship view](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23dad8b7.png)

  14. The **Field Name** is what you will enter in **CRM Field Label** in the CCAI Platform Custom Field Mapping page.




The following example shows what a **New field** will look like when correctly set up and used on the case object:

![New field display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23db13cf.png)

### Kustomer configuration

See the Kustomer Help Center for details and information regarding setting up Custom Fields.

### CCAI Platform configuration

The following sections outline the changes needed in the CCAI Platform portal to configure the Kustomer CRM field mapping:

  1. In the CCAI Platform portal, go to **Settings > Operation Management**.

  2. Go to the **CRM Custom Field Mapping** section and click **View All**.

  3. Click the + **Add CRM Field Mapping** link.

     * **Field mapping title** : CCAI Platform name for this custom field mapping used in the CCAI Platform Portal.

     * **CRM field label** : Label within your CRM of the CRM field to which you are mapping.

     * **Custom data field label** : Custom data field label from which you are mapping.

     * **SDK examples** : `data_name`, `device` (from the `custom_data object` )

     * **Apps API (Chat) examples** : `orderId`, `customerTier` (from the Apps API request data object).

  4. Click **Save**.

**Tip:** The nested label field — `"label": "Order ID"` — is descriptive text only and is not used for mapping. Always use the top-level key name, such as `orderId`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 
