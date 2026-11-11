---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection/
title: Credit card CVV collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:32:47.135982+00:00
---

# Credit card CVV collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Credit card CVV collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The credit card CVV collection [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) captures a three- or four-digit CVV (Card Verification Value) code.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not include payment gateway integration.
  * This component does not accept CVVs shorter than three or longer than four digits.



## Additional features

This prebuilt component provides the following additional features:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to let users input numeric values using the telephone keypad.

## Sample dialogs

The sample dialogs show common scenarios that this prebuilt component handles. They demonstrate behavior when the user calls the component using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Valid CVV

The user provides a three- to four-digit CVV, and the component accepts it.

User Input | Agent Response  
---|---  
| Say or enter the 3 or 4 digit CVV present on your card.  
3434 |   
| You mentioned the CVV is 3434, is that correct?  
yes |   
| Great, I'm done with collecting the CVV.  
  
### Retries

The user provides a three- to four-digit CVV in the third attempt, and the component accepts it.

User Input | Agent Response  
---|---  
| Say or enter the 3 or 4 digit CVV present on your card.  
45 |   
| I heard 45, which isn't a valid 3 or 4 digit CVV code.  
  
Say or enter the 3 or 4 digit CVV present on your card.  
34 |   
| I heard 34, which isn't a valid 3 or 4 digit CVV code.  
  
Say or enter the 3 or 4 digit CVV present on your card.  
3434 |   
| You mentioned the CVV is 3434, is that correct?  
yes |   
| Great, I'm done with collecting the CVV.  
  
### Unrecognized input

The component ends the flow when the user provides unrecognized input three times.

User Input | Agent Response  
---|---  
| Say or enter the 3 or 4 digit CVV present on your card.  
It's fine |   
| Sorry, I didn't get that. Can you say or enter the 3 or 4 digit CVV present on your card again?  
It's fine |   
| Hmm, I still wasn't able to get that. Make sure you're saying or using your keypad to enter the 3 or 4 digit CVV present on your card.  
It's fine |   
| Sorry, I'm having difficulty understanding your response.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | CVV Collection  
Component Specific Intent | prebuilt _components_[component _name]_[intent_name] | prebuilt_components_cvv_collect_cvv  
Parameter | [param_name] | cvv_code  
  
## Output parameters

Output parameters are session parameters that remain active after you exit the component. These parameters contain important information that the component collects.

This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
cvv_collection_cvv | This parameter returns the CVV captured by the component. | string  
  
## Basic setup

To set up this prebuilt component, you can [import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).

### Complete

The credit card CVV collection prebuilt component is now set up and ready to test.

[ Previous arrow_back  Cancel order  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order)

[ Next Credit card enrollment  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
