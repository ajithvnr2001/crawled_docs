---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection/
title: Alphanumeric collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:32:48.112495+00:00
---

# Alphanumeric collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Alphanumeric collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The alphanumeric collection [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) collects alphanumeric sequences from the user. Input parameters let you configure the minimum and maximum length accepted.

The component captures chunks of characters from the user on each conversational turn and concatenates them to form the final sequence. Input parameters let you configure the minimum and maximum length accepted per chunk.

The sequence capture continues until the user indicates that they're done with the sequence by providing input that matches the [`prebuilt_components_confirmation_done intent`](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#common-intents).

## Phonetic alphabet

This component supports the use of phonetic alphabets, such as the [NATO Phonetic Alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet).

User Input | Captured Sequence  
---|---  
alpha bravo charlie 123 | abc123  
A B Cat 1 2 3 | ABC123  
A as in apple, B as in banana, C for chili, one fifteen | ABC115  
  
## Additional capabilities

The following additional capabilities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

These sample dialogs show common scenarios that this prebuilt component handles. They show behavior when you call the component using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Single chunk

  1. The user provides an alphanumeric sequence in one chunk and says "I'm done."
  2. The agent successfully accepts it.

User Input | Agent Response  
---|---  
| Please start by saying the first 1 to 8 characters of the alphanumeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
fvfd3433 |   
| Alright. I got fvfd3433, is that correct?  
yes |   
| Okay. Tell me the next 1 to 8 characters in the sequence.  
I'm done |   
| Thank you for confirming. The final alphanumeric sequence I got is fvfd3433, is that correct?  
yes |   
| Fantastic, I've collected the alphanumeric sequence.  
  
### Multiple chunks

  1. The user provides an alphanumeric sequence in two chunks.
  2. The agent successfully accepts it.

User Input | Agent Response  
---|---  
| Please start by saying the first 1 to 8 characters of the alphanumeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
fvfd3433 |   
| Alright. I got fvfd3433, is that correct?  
yes |   
| Okay. Tell me the next 1 to 8 characters in the sequence.  
gh67 |   
| Alright. I got gh67, is that correct?  
yes |   
| Okay. Tell me the next 1 to 8 characters in the sequence.  
I'm done |   
| Thank you for confirming. The final alphanumeric sequence I got is fvfd3433gh67, is that correct?  
yes |   
| Fantastic, I've collected the alphanumeric sequence.  
  
### Successful retry

  1. The user provides an alphanumeric sequence.
  2. The agent re-prompts the user to confirm it.
  3. The user says "No" to the confirmation and provides an alphanumeric sequence again.
  4. The agent successfully accepts the second sequence.

User Input | Agent Response  
---|---  
| Please start by saying the first 1 to 8 characters of the alphanumeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
fvfd3433 |   
| Alright. I got fd3433, is that correct?  
no |   
| Sorry about that, can you please provide the first 1 to 8 characters again?  
fvfd3433 |   
| Alright. I got fvfd3433, is that correct?  
yes |   
| Okay. Tell me the next 1 to 8 characters in the sequence.  
I'm done |   
| Thank you for confirming. The final alphanumeric sequence I got is fvfd3433, is that correct?  
yes |   
| Fantastic, I've collected the alphanumeric sequence.  
  
### Unsuccessful retries

The user cannot provide an alphanumeric sequence of 1 to 8 characters within three attempts, so the component exits the flow.

User Input | Agent Response  
---|---  
| Please start by saying the first 1 to 8 characters of the alphanumeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
123N |   
| Alright. I got 123M, is that correct?  
no |   
| Sorry about that, can you please provide the first 1 to 8 characters again?  
123N |   
| Alright. I got 123M, is that correct?  
no |   
| Sorry about that, can you please provide the first 1 to 8 characters again?  
  
Please spell out each letter of your sequence with a word starting with each letter. For example, if your sequence is AB123, say "Apple Baby 123".  
123 Nest |   
| Alright. I got 123N, is that correct?  
no |   
| Sorry, I've used too many attempts and failed to collect the alphanumeric sequence.  
  
### Phonetic alphabet

  1. The user provides an alphanumeric sequence.
  2. The agent re-prompts the user to confirm it.
  3. The user says "No" to the confirmation, and the agent re-prompts the user again.
  4. The user says "No" to the confirmation again, and the agent enables phonetic conversion.
  5. The user provides an alphanumeric sequence using phonetic conversion.
  6. The agent successfully accepts the alphanumeric sequence.

User Input | Agent Response  
---|---  
| Please start by saying the first 1 to 8 characters of the alphanumeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
123N |   
| Alright. I got 123M, is that correct?  
no |   
| Sorry about that, can you please provide the first 1 to 8 characters again?  
123N |   
| Alright. I got 123M, is that correct?  
no |   
| Sorry about that, can you please provide the first 1 to 8 characters again?  
  
Please spell out each letter of your sequence with a word starting with each letter. For example, if your sequence is AB123, say "Apple Baby 123".  
123 N as in Nancy |   
| Alright. I got 123N, is that correct?  
yes |   
| Okay. Tell me the next 1 to 8 characters in the sequence.  
567BC |   
| Alright. I got 567BC, is that correct?  
that's all |   
| Thank you for confirming. The final alphanumeric sequence I got is 123N56BC. Is that correct?  
yep |   
| Fantastic, I've collected the alphanumeric sequence.  
  
### Invalid sequence length

  1. The user provides an alphanumeric sequence with a length that is outside the predefined minimum and maximum length of the alphanumeric sequence.
  2. The agent prompts the user to start over.
  3. The user declines, and the component exits the flow.

User Input | Agent Response  
---|---  
| Please start by saying the first 1 to 8 characters of the alphanumeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
123M |   
| Alright. I got 123M, is that correct?  
done |   
| Sorry, you provided an alphanumeric sequence that is outside the required length of 5 to 30 characters. Do you want to start over?  
no |   
| Sorry, I've used too many tries and failed to collect the alphanumeric sequence.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Alphanumeric Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_alphanumeric_collection_support_continue  
Parameter | [param_name] | alphanumeric_max_length  
  
## Input parameters

Input parameters configure certain behaviors of the component. The parameters are used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described in the following table. Session-scoped parameters can be set either by a calling flow or on the start page of this component.

You can configure the minimum and maximum lengths accepted per capture and for the final collected sequence by modifying [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) in the [flow's start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#data).

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$flow.alphanumeric_min_length | Minimum length of the final alphanumeric sequence. The default value is `1`. | integer  
$flow.alphanumeric_max_length | Maximum length of the final alphanumeric sequence. The default value is `30`. | integer  
$flow.lower_limit | Minimum length of the chunk a user can provide each turn. The default value is `1`. | integer  
$flow.upper_limit | Maximum length of the chunk a user can provide each turn. The default value is `8`. | integer  
  
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

Output parameters are session parameters that remain active after you exit the component. These parameters contain information that the component collects. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
alphanumeric_collection_alphanumeric_sequence | This parameter returns the alphanumeric sequence captured by the component. | string  
  
## Basic setup

To set up this prebuilt component:

[Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).

### Complete

The prebuilt component is now set up and ready to test.

[ Previous arrow_back  Address collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/address-collection)

[ Next Arrange appointment  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
