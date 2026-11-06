---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/address-collection/
title: Address collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:53:36.951721+00:00
---

# Address collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/address-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Address collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The address collection [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) collects an address from a customer and validates the address using the [Google Address Validation API](https://mapsplatform.google.com/maps-products/address-validation/).

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component includes the following limitations:

  * Supports addresses only from countries listed in the [Address Validation API coverage details](https://developers.google.com/maps/documentation/address-validation/coverage).



## Additional functionalities

The following additional functionalities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. They demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Full address validation

The user provides a complete address, and the address collection component verifies it.

User Input | Agent Response  
---|---  
| Please tell me your full address to start.  
1600 Amphitheatre Parkway, Mountain View, CA 94043-1351, USA |   
| I have collected the final address; the street number is 1600, the route is Amphitheatre Parkway, the city is Mountain View, the administrative area is CA, the postal code is 94043, the country is USA. Is that correct? Please say yes or no.  
yes |   
| Fantastic, I've collected the address.  
  
### Partial valid address with inferred elements

  1. The user provides a partial address.
  2. The agent guesses the missing part and verifies it after confirmation from the user.

User Input | Agent Response  
---|---  
| Please tell me your full address to start.  
1600 Amphitheatre Parkway |   
| I have guessed some part of the address, the city is Mountain View, postal code is 94043, administrative area is CA, country is USA.  
  
I have collected the final address; the street number is 1600, the route is Amphitheatre Parkway, the city is Mountain View, the administrative area is CA, the postal code is 94043, the country is USA. Is that correct? Please say yes or no.  
Yes |   
| Fantastic, I've collected the address.  
  
### Partial valid address with user-provided elements

  1. The user provides a partial address.
  2. The user rejects the guessed part and provides their own input.
  3. The agent accepts the user-provided input and re-prompts for confirmation.
  4. The user accepts the final address.

User Input | Agent Response  
---|---  
| Please tell me your full address to start.  
1600 Amphitheatre Parkway |   
| I have guessed some part of the address, the city is Mountain View, postal code is 94043, administrative area is CA, country is USA.  
  
I have collected the final address; the street number is 1600, the route is Amphitheatre Parkway, the city is Mountain View, the administrative area is CA, the postal code is 94043, the country is USA. Is that correct? Please say yes or no.  
No |   
| Okay. Please tell me which part of the address needs to be changed.  
Postal code |   
| Can you please share the postal code?  
94044 |   
| I'm done with this update. Is there anything else to be changed? Please say yes or no.  
no |   
| After validation I have replaced the postal code as 94043.  
  
I have collected the final address; the street number is 1600, the route is Amphitheatre Parkway, the city is Mountain View, the administrative area is CA, the postal code is 94043, the country is USA. Is that correct? Please say yes or no.  
yes |   
| Fantastic, I've collected the address.  
  
### Unrecognized input

Component exits the flow after the user provides unrecognized input three times.

User Input | Agent Response  
---|---  
| Please tell me your full address to start.  
It's fine |   
| Sorry, I didn't get that. Please tell me your full address to start.  
nice |   
| Hmm, I still wasn't able to get that. Please tell me your full address to start.  
great |   
| Sorry, I'm having difficulty understanding your response.  
  
### Unsupported address

Component exits the flow after the user provides an address that isn't supported by the Address Validation API.

User Input | Agent Response  
---|---  
| Please tell me your full address to start.  
India |   
| I'm sorry, but I'm unable to validate addresses in that region.  
  
## Address validation

For more information about how the address collection component validates addresses, see [Address Validation API Overview](https://developers.google.com/maps/documentation/address-validation).

The address collection component captures user input by using the [@sys.address system entity](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities) and sends the captured address to the Address Validation API to extract address elements for further processing.

The Address Validation API returns the following address elements, which you can use to collect and validate a complete address:

  * `administrative_area_level_1`
  * `archipelago`
  * `country`
  * `locality`
  * `postal_code`
  * `route`
  * `street_number`



You can try the [Google Address Validation Demo](https://developers.google.com/maps/documentation/address-validation/demo) with any address from a [supported region](https://developers.google.com/maps/documentation/address-validation/coverage).

## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Address Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_address_collection_locality  
Parameter | [param_name] | user_provided_address  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_address_collection:address_validation  
  
## Input parameters

Input parameters configure certain behaviors of the component. One or more conditions within the flow use the parameters to determine how the component should behave. The user must set flow-scoped parameters on the start page of the component as described in the following table. The user can set session-scoped parameters either by a calling flow or on the start page of this component.

The user can configure which address elements are required by this component by modifying [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) on the [flow's start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#data).

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$flow.zip_code | If the zip code address element is required, then set it to `true`; otherwise, set it to `false`. | boolean  
$flow.city | If the city address element is required, then set it to `true`; otherwise, set it to `false`. | boolean  
$flow.admin_area | If the administrative area address element is required, then set it to `true`; otherwise, set it to `false`. | boolean  
$flow.street_number | If the street number address element is required, then set it to `true`; otherwise, set it to `false`. | boolean  
$flow.route | If the route address element is required, then set it to `true`; otherwise, set it to `false`. | boolean  
$flow.country | If the country address element is required, then set it to `true`; otherwise, set it to `false`. | boolean  
$flow.island | If the island address element is required, then set it to `true`; otherwise, set it to `false`. | boolean  
$flow.retry_num | Sets the maximum retry limit for Maps Address Validation API webhook calls. | integer  
  
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

The prebuilt component provides the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
address_collection_address | This parameter returns the address object if an address was captured by the component | 
    
    
    {  
      "admin-area": string,  
      "city": string,  
      "country": string,  
      "island": string,  
      "route": string,  
      "zip-code": string,  
      "street-number": string  
    }  
  
address_collection_status | This parameter returns the status of the collected address. The returned value is one of the following:  
  
`VALID_ADDRESS`: address was collected and validated by the Address Validation API.  
  
`INVALID_ADDRESS`: address was confirmed by the user but one or more elements were not validated or marked as `UNCONFIRMED_BUT_PLAUSIBLE` by the Address Validation API.  
  
`MAPS_API_ERROR`: address was not collected due to Address Validation API error.  
  
`COUNTRY_NOT_SUPPORTED`: address was not collected because the Address Validation API doesn't support that region.  
  
`NO_USER_CONFIRMATION`: address was not confirmed because the user didn't confirm an address. | 
    
    
    string  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).
  2. [Enable](https://docs.cloud.google.com/service-usage/docs/enable-disable) the Address Validation API.
  3. Configure the provided [flexible webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with your Maps API key. For more information, see Webhook setup.



## Webhook setup

To validate addresses with the Address Validation API, configure the provided flexible webhook with the correct credentials.

### Address Validation webhook

This webhook performs the following actions:

  1. Processes captured Dialogflow CX parameters, forms the request, and verifies the address using the [Address Validation API](https://developers.google.com/maps/documentation/address-validation).
  2. Extracts confirmed, unconfirmed, missing, and inferred address elements from the [Address Validation API response](https://developers.google.com/maps/documentation/address-validation/demo).



Update the webhook settings with the correct Maps API key to configure the webhook for this component.

To retrieve your API key, go to [Google Cloud **Console** > **APIs & Services** > **Credentials**](https://console.cloud.google.com/apis/credentials), select your Maps API key, and copy the API key field.

To configure the webhook:

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Webhooks**.
  6. Select the `prebuilt_components_address_collection:address_validation` webhook.
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the URL including your Maps API key: `https://addressvalidation.googleapis.com/v1:validateAddress?key=<var>MAPS_API_KEY</var>`.
  8. In the **Authentication** settings, configure the Username as `key`, and set the password for your Maps API key.
  9. Click **Save**.



### Complete

The prebuilt component and its webhook are now set up and ready to test.

[ Previous arrow_back  Account statement  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-statement)

[ Next Alphanumeric collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
