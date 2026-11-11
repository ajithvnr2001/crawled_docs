---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection/
title: Credit card expiration date collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:32:46.859750+00:00
---

# Credit card expiration date collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Credit card expiration date collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) captures a credit card expiration date from the user.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Payment gateway integration is not included in this component.



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to let users input numeric values using the telephone keypad.

## Additional features

This prebuilt component provides the following additional features:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The sample dialogs show common scenarios that this prebuilt component handles. They demonstrate behavior when the user calls the component using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Successful input

  1. The user provides the expiration date in the first attempt.
  2. The agent successfully accepts it.

User Input | Agent Response  
---|---  
| Say or enter the credit card's expiration date, starting with the month followed by the year.  
01/27 |   
| I have received the credit card's expiration date as January 2027. Is that correct?  
yes |   
| Great, I'm done with collecting the credit card's expiration date.  
  
### Retries

  1. The user provides the expiration date on the first attempt.
  2. When the agent reconfirms the collected expiration date, the user says "it's wrong."
  3. The agent asks the user to confirm which part of the expiration date is incorrect—the entire date, month, or year—and re-prompts the user to provide those details again.

User Input | Agent Response  
---|---  
| Say or enter the credit card's expiration date, starting with the month followed by the year.  
01/27 |   
| I have received the credit card's expiration date as January 2027. Is that correct?  
It's wrong |   
| Sorry I didn't get that right. Let me know if you want to change the entire date or if you want to change the month or year instead?  
month |   
| Sorry about that. Say or enter your credit card's expiration month.  
feb |   
| I have received the credit card's expiration month as February. Is that correct?  
yes |   
| I have received the credit card's expiration date as February 2027. Is that correct?  
yes |   
| Great, I'm done with collecting the credit card's expiration date.  
  
### Partial input

  1. The user cannot provide the expiration date on the first attempt.
  2. The agent splits the expiration date and asks for the month followed by the year.
  3. The user provides the input correctly this time, and the agent successfully accepts it.

User Input | Agent Response  
---|---  
| Say or enter the credit card's expiration date, starting with the month followed by the year.  
13 |   
| Sorry, the expiration date doesn't look quite right. Try capturing the month again.  
  
Say or enter your credit card's expiration month.  
1 |   
| I have received the credit card's expiration month as January. Is that correct?  
Yes, right |   
| Say or enter your credit card's expiration year.  
26 |   
| I have received the credit card's expiration year as 2026. Is that correct?  
yes |   
| I have received the credit card's expiration date as January 2026. Is that correct?  
yes |   
| Great, I'm done with collecting the credit card's expiration date.  
  
### Unrecognized input

The component exits the flow after the user provides unrecognized input three times.

User Input | Agent Response  
---|---  
| Say or enter the credit card's expiration date, starting with the month followed by the year.  
It's fine |   
| Sorry, I did not get that. Can you say or enter the credit card's expiration date again?  
nice |   
| Hmm, I was still not able to get that. Make sure you are saying the credit card's expiration date. You can also use the keypad to enter the credit card's expiration date.  
good |   
| Sorry, I'm having difficulty understanding your response.  
  
## Credit card expiration date validation

The user can enter the credit card expiration date months as an integer between '01' and '12' or as a string representing a month between 'January' and 'December'.

The credit card expiration date year must be four digits long. If the user enters two digits, the system converts them to a four-digit year; for example, '25' becomes '2025'. Additionally, the year can't be more than 10 years in the future from the current year.

The credit card expiration date, including month and year, must be a future date compared to the current month and year.

## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Credit Card Expiration Date Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_credit_card_expiration_date_collection_collect_date  
Entity Type | prebuilt_components_[component_name]_[entity_type_name] | prebuilt_components_credit_card_expiration_date_collection_month  
Parameter | [param_name] | expiration_date  
  
## Output parameters

Output parameters are session parameters that remain active after exiting the component. These parameters contain important information collected by the component.

This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
credit_card_expiration_date_collection_credit_card_expiration_date | This parameter returns the object of expiration element types that will be captured during the conversation flow session | 
    
    
    {  
      "year": integer,  
      "month": integer  
    }  
  
## Basic setup

To set up this prebuilt component, you can [import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).

### Complete

The prebuilt component should now be set up and ready to test.

[ Previous arrow_back  Credit card enrollment  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment)

[ Next Credit card number collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-number-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
