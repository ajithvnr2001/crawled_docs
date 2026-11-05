---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-five9/
title: Agent Assist for Salesforce voice integration with Five9 Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:46:09.753413+00:00
---

# Agent Assist for Salesforce voice integration with Five9 Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-five9/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist for Salesforce voice integration with Five9 Fusion Stay organized with collections  Save and categorize content based on your preferences. 

The integration of Five9 Fusion with Salesforce Voice (formerly Salesforce Service Cloud Voice) enables Salesforce representatives to make and receive calls in Salesforce using the capabilities of the Five9 platform.

![Five 9 Fusion integration architecture.](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/five9.png)**Figure 1.** Integration architecture for Salesforce voice with Agent Assist and Five9 Fusion.

Five9 sends call audio to both Google Cloud and your agent desktop with media streams. The media stream audio goes to the gRPC service in Google Cloud and Salesforce Voice on your agent desktop. Google Cloud processes the call audio with a variety of products, then sends messages and notifications from the Cloud Run UI connector to the Agent Assist UI modules on your agent desktop. Your agent desktop also sends call audio from Salesforce Voice to your Agent Assist UI modules.

## Before you begin

Follow these steps to set up the resources needed for your Salesforce Five9 Fusion integration.

  1. Set up your [access to resources](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-byb).
  2. Set up your [Agent Assist for Salesforce app](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup).
  3. Configure and deploy the following:

     * Instance of the [Five9 media stream integration services](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/main/aa-integration-backend/platforms/five9)
     * [Agent Assist integration services](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/main/aa-integration-backend)
     * Salesforce voice license
     * Five9 account



## Configure Five9

Follow these steps to send call media streams to Five9 integration services, and configure Five9 to pass the call ID to the voice call object in Salesforce.

### Media stream

Configure a [Five9 media stream](https://documentation.five9.com/bundle/voicestream-admin/page/voicestream-admin-guide/self-service/creating-ss-subscriptions.htm) to stream audio from a [campaign](https://documentation.five9.com/bundle/admin-console/page/admin-console/campaigns/_ch-campaigns.htm) to Agent Assist.

  1. From the administrator console, search _Media Stream_.
  2. Click **Media Stream** > **Create**.
  3. Enter the following details:

     * **Subscription Name** : Agent Assist for Salesforce
     * **Voice Streaming** : Voice Streaming
     * **Streaming Destination** : Other (Self Service)
     * **Streaming Protocol** : `gRPC`
     * **Primary Streaming Destination** : `https://your-five9-grpc-service:443`
     * **Stream Status Event Destination** : `https://your-five9-http-service/mediastream-event-destination/`
     * **CTI Call Event Destination** : `https://your-five9-http-service/cti-call-event-destination/`
     * **Five9 Trust Token** : Generate this token using code from the [Five9 integration services repository](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/main/aa-integration-backend/platforms/five9).
     * **Audio Streaming - > Enable third-party audio streaming**: Checked
     * **Audio Streaming - > Enable audio streaming for all agents in agent-only conference calls**: Checked
     * **Streaming Filter** : Use this to determine which calls are sent to Agent Assist with the media stream.
  4. Click **Save**.

  5. Five9 generates an API key. Attach this value to the environment variable `FIVE9_API_KEY` in your Cloud Run Five9 integration services, then redeploy them.




### Call variables

Follow these steps to implement [call variables](https://documentation.five9.com/bundle/byotadmins/page/crm-admins/SalesforceBYOT/installation/call-logging.htm).

  1. Login to Five9 as an administrator and search _Variables_ , then click the corresponding tile.
  2. Click **Create** on the **Variable Groups** page.
  3. Name the variable group `f9crm`.
  4. Click the `f9crm` variable group in the table.
  5. Click **Create Variable** in the variable group details panel.
  6. Name the variable `vcc_call_id`, and give it the `text` data type.



### Set variable in IVR flow

Follow these steps to set a variable in your interactive voice response (IVR) flow.

  1. On the Five9 administrator page, click **Apps**.
  2. Select **VCC Administrator via Web**.
  3. Create or select an IVR flow.
  4. After the **`IncomingCall`** step, add a **Set variable** step.
  5. Click **Add** in the **Set variable details** box.
  6. On the select menu, navigate to the **User CAV Variables** section > the variable `f9crm.vcc_call_id`.
  7. Select **Variable radio** > the variable `Call.call_id`.



### Contact center

Follow Five9's instructions to [set up a contact center](https://documentation.five9.com/bundle/byotadmins/page/crm-admins/SalesforceBYOT/installation/enable-scv-partner-technology.htm).

## Salesforce

Follow these steps to configure your integration from Salesforce.

### Create a custom field

The variable created and set in Five9 must match a field of the same name in Salesforce. Follow these steps to create the field in Salesforce

  1. Navigate to **Setup** and search _Object Manager_.
  2. In Object Manager, search _Voice Call_ and click the corresponding item.
  3. On the sidebar menu, click **Fields & Relationships** > **New**.
  4. Enter the following details:

     * **Field Label** : Five9 Call ID
     * **Field/API Name** : `F9_f9crm_vcc_call_id`.



### Map the Five9 call ID to an Agent Assist call ID

Follow these steps to map your call ID from Five9 onto an Agent Assist call ID.

  1. In Setup, click the **Quick Find** box and search _Flows_.
  2. Click **Flows** > **New Flow**.
  3. Select **Record-Triggered Flow** and click **Create**.



#### Create elements

Follow these steps to create elements that guide your flow.

  1. Click **Start** for your flow.
  2. In the **Object** field, select **Voice Call (VoiceCall)** and enter the following details:

     * **Trigger the flow when** : A record is created or updated.
     * **Condition requirements** : All Conditions Are Met (AND).
     * **Field** : Five9 call ID
     * **Operator** : Null.
     * **Value** : `$GlobalConstant.False`.
     * **When to Run the Flow for Updated Records** : Only when a record is updated to meet the condition requirements.
     * **Fast Field Updates** : This is a "Before-Save" flow. It is much faster and more efficient because it updates the record before it's saved to the database.



#### Create a formula

Five9 creates a numeric call ID then adds `five9-` and pads the call ID. Agent Assist must then transform the Five9 call ID into a conversation ID. Follow these steps to create a formula that maps the Five9 call ID to an Agent Assist conversation ID.

  1. On the **Flow** toolbar, click **Toggle Toolbox** > **New Resource**.
  2. For **Resource Type** , select **Formula**.
  3. Name the formula `Five9IDMapper`.
  4. In the **Data Type** field, select **Text**.
  5. In the **Formula field** , enter the following:
         
         IF(
           ISBLANK({!$Record.F9_f9crm_vcc_call_id__c}),
           NULL,
          "five9-" & 
           IF(
             LEN(TEXT(VALUE({!$Record.F9_f9crm_vcc_call_id__c}))) >= 10,
             TEXT(VALUE({!$Record.F9_f9crm_vcc_call_id__c})),
            LPAD(TEXT(VALUE({!$Record.F9_f9crm_vcc_call_id__c})), 10, "0")
           )
         )
         


**Note:** All custom fields in Salesforce end in `__c`.

#### Create an assignment

Follow these steps to create an assignment that maps the Five9 call ID to the formula you created.

  1. On the flow canvas, click the **+** after the **Start** element.
  2. Select the **Assignment** element and enter the following details:

     * **Label** : Copy Five9 call ID to Agent Assist conversation ID.
     * **Variable** : Search `VoiceCall` > `Conversation ID` and hover over the info icon to ensure it's `agent_assist__ConversationId__c`.
     * **Operator** : Equals.
     * **Value** : Search _Five9IDMapper_.
  3. Click **Save**.

  4. Provide a label if requested.

  5. Click **Activate**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
