---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-statement/
title: Account statement prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:53:37.998339+00:00
---

# Account statement prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-statement/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Account statement prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The account statement [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) verifies a customer's [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) and sends the account statement for a specified period to an authenticated user. If the customer has multiple accounts, the component confirms the specific account that the user needs to retrieve an account statement for.

This component uses the [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component to authenticate customers and uses a customized version of [Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) to collect start and end dates for the statement period.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component doesn't encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. They show behavior when you call the component using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Single account

If the user has a single account, the agent collects the statement start and end dates, asks whether the user wants to encrypt the statement, and sends the account statement to them.

User Input | Agent Response  
---|---  
| _The agent authenticates the user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component._  
| Thank you, you have been successfully authenticated.  
| Please wait while we are fetching your account details.  
  
We have found an account number ending with 1001 associated with your number.  
  
Please provide the account statement start date, starting with the month, followed by day and then year. Note that the account statement period will be provided only for the last 90 days.  
| _The agent collects statement start date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component._  
| Great, we have collected your statement start date.  
  
Please provide the account statement end date, starting with the month, followed by day and then year. Note that the account statement period will be provided only for the last 90 days.  
| _The agent collects statement end date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component._  
| Thank you. Please confirm if you are looking for the account statement between 2023-07-12 to 2023-07-24?  
Yes |   
| Please wait while we are fetching your statement details.  
  
We found transactions from 2023-07-12 to 2023-07-24. Would you like to receive it by email, SMS or WhatsApp?  
SMS |   
| Do you want to encrypt the document before we share it with you?  
No thanks |   
| You will receive the statement within 15 minutes on your registered mobile.  
  
### Multiple accounts

If the user has multiple accounts, the agent confirms which account the user is requesting an account statement for. The agent then collects the statement start and end dates, asks whether the user wants to encrypt the statement, and sends the account statement to them.

User Input | Agent Response  
---|---  
| _The agent authenticates the user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component._  
| Thank you, you have been successfully authenticated.  
| Please wait while we are fetching your account details.  
  
We have found that there are 2 accounts associated with your number.  
  
Can you please help us with the last 4 digits of the account you are referring to?  
2002 |   
| The last four digits of the account number that we got are 2002, is that correct?  
yes |   
| Please provide the account statement start date, starting with the month, followed by day and then year. Please note that the account statement period will be provided only for the last 90 days.  
| _The agent collects statement start date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component._  
| Great, we have collected your statement start date.  
  
Please provide the account statement end date, starting with the month, followed by day and then year. Note that the account statement period will be provided only for the last 90 days.  
| _The agent collects statement end date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component._  
| Thank you. Please confirm if you are looking for the account statement between 2023-07-18 to 2023-07-22?  
Yes |   
| Please wait while we are fetching your statement details.  
  
We found transactions from 2023-07-18 to 2023-07-22. Would you like to receive it by email, SMS, or WhatsApp?  
WhatsApp |   
| Do you want to encrypt the document before we share it with you?  
Yes |   
| Password details will be shared on your registered WhatsApp.  
  
You will receive the statement within 15 minutes on your registered WhatsApp.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | Component Name | Account Statement  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_account_number_collection_four_digit_account_number  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_account_statement_channelall  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_account_statement:request_statement  
  
## Input parameters

Input parameters configure specific behaviors of the component. One or more conditions within the flow use the parameters to determine how the component behaves. The user must configure flow-scoped parameters on the start page of the component as described in the following table. The user can also set session-scoped parameters either by a calling flow or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level | (optional) Indicates the authentication level of the caller. | integer  
$session.params.auth_level_req | Indicates the [level of authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) needed before a user can access their account statement. This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `1`. | integer  
$session.params.account_auth_enabled | Indicates whether the user should be authenticated as an account holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `true`. | boolean  
$session.params.card_auth_enabled | Indicates whether the user should be authenticated as a card holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `false`. | boolean  
$session.params.phone_number | (optional) Customer's registered phone number used for authentication. | string  
$session.params.account_count | (optional) Number of accounts associated with the authenticated user. | integer  
$session.params.last_four_digit_of_account_number | (optional) Last four digits of the customer account number for which the statement needs to be provided. If the customer has a single account, this information is retrieved automatically post authentication. If the customer has multiple accounts, the specific account number is collected from the customer. | string  
$session.params.account_statement_max_days | Specifies the maximum number of days before the current date allowed for a statement start date. By default, this value is `-90`, indicating that statement start dates may start no more than 90 days before the current date. This parameter is configured in the start page `true` route. | integer  
$flow.max_retry_count | Specifies the number of retries allowed when prompting the user to provide a valid statement end date. The default value is `3`. | integer  
$flow.max_retry_confirm_period_counter | Specifies the number of retries allowed when confirming the statement period with the user. The default value is `3`. | integer  
$flow.max_retry_statement_counter | Specifies the number of retries allowed when the provided statement period does not retrieve any transactions. The default value is `3`. | integer  
  
####  To configure the input parameters for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Build** tab. 
  5. Click the imported component in the **Flows** section. 
  6. Click the Start Page in the **Pages** section. 
  7. Click the **true** Route in the Start Page. 
  8. In the Route window, edit the **Parameter Presets** values as needed. 
  9. Click **Save**. 



## Output parameters

Output parameters are session parameters that remain active after the user exits the component. These parameters contain important information that the component collects.

This prebuilt component provides the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
auth_level | Indicates the authentication level of the caller. | integer  
phone_number | The local phone number of the caller, without the country code, used to identify the user. | string  
account_count | The number of accounts associated with the user's registered telephone number. These accounts include self-accounts and accounts for which the user has power of attorney. | integer  
last_four_digit_of_account_number | The last four digits of the account number that the user selected to receive account statement information for. | string  
transfer_reason | This parameter indicates the reason the flow exited, if it was not successful. The returned value is one of:  
  
`agent`: the user requested a human agent at some point during the conversation.  
  
`denial_of_information`: the user declined to share information requested by the component.  
  
`max_no_input`: the conversation reached the maximum number of retries for no-input events. See [no-input built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).  
  
`max_no_match`: the conversation reached the maximum number of retries for no-match events. See [no-match built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).  
  
`webhook_error`: a webhook error occurred. See [webhook.error built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).   
  
`webhook_not_found`: a webhook URL was unreachable. See [webhook.error.not-found built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). | string  
  
## Basic setup

To set up the prebuilt component, complete the following steps:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).
  2. Configure the provided [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with settings describing your external services. For more information, see the Webhook setup section.



## Webhook setup

To use this component, you must configure the included [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to retrieve needed information from your external services.

### Authentication

If you haven't previously configured external services required for authentication, configure them to enable authentication of users for this component. For more information about webhook setup, see [Authentication webhook setup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#webhook-setup).

### Validate account

The `prebuilt_components_account_services:validate_account` webhook is used by the component to verify that an account exists based on the user's registered phone number and the last four digits of the account number provided. The webhook also returns the account balance, if an account exists.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | The local phone number of the caller, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user selected and confirmed to receive account statement information for. | string  
  
#### API response parameters

The component pulls the following parameters from the API response:

Parameter Name | Description | Output Format  
---|---|---  
account_found | Indicates whether an account with the provided last four digits exists for the user's registered account. | boolean  
balance | The amount of the current balance on the account, if it exists. | number  
  
####  To configure the Validate account webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_account_services:validate_account webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get transactions

The `prebuilt_components_account_statement:get_transactions` webhook is used by the component to retrieve the transactions for an account given the user's registered phone number, the last four digits of the account number, and the statement period.

#### API request parameters

The component provides the following parameters as inputs to the API request:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | The local phone number of the caller, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user selected and confirmed to receive account statement information for. | string  
$flow.statement_start_date | The requested statement start date in "YYYY-MM-DD" format. | string  
$flow.statement_end_date | (optional) The requested statement end date in "YYYY-MM-DD" format. If no value is provided by the user or caller declines to provide an end date, the value defaults to the current date. | string  
  
#### API response parameters

The component pulls the following parameters from the API response:

Parameter Name | Description | Output Format  
---|---|---  
transactions_count | The number of transactions found for the specified account in the given statement period. | integer  
  
####  To configure the Get transactions webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_account_statement:get_transactions webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Request statement

The `prebuilt_components_account_statement:request_statement` webhook sends a statement for an account to a selected channel based on the user's registered phone number, the last four digits of the account number, and the statement period.

#### API request parameters

The component provides the following parameters as inputs to the API request:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | The local phone number of the caller, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user selected and confirmed to receive account statement information for. | string  
$flow.statement_start_date | The requested statement start date in "YYYY-MM-DD" format. | string  
$flow.statement_end_date | (optional) The requested statement end date in "YYYY-MM-DD" format. If no value is provided by the user or caller declines to provide an end date, the value defaults to the current date. | string  
$flow.channel_medium | The channel the user has selected to receive the message on. Valid values are defined by the `prebuilt_components_account_statement_channelphn` and `prebuilt_components_account_statement_channelall` custom entities, depending on whether the user has a registered email. By default `email`, `mobile` and `WhatsApp` are supported. | string  
$flow.encryption_status | Indicates whether the user wants the document encrypted before sending to the specified channel. If no value is provided by the user or caller declines to provide an encryption preference, the value defaults to `true`. | boolean  
  
####  To configure the Request statement webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_account_statement:request_statement webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

The prebuilt component and its webhooks are now set up and ready to test.

[ Previous arrow_back  Account balance  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-balance)

[ Next Address collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/address-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
