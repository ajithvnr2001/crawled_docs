---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/after-hour-deflection/
title: After hour deflection for calls and chats \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:52.220940+00:00
---

# After hour deflection for calls and chats  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/after-hour-deflection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  After hour deflection for calls and chats Stay organized with collections  Save and categorize content based on your preferences. 

Customize your consumer's experience by configuring specific deflection paths for consumers who try to contact you outside your hours of operation. Configure your hours of operation first, then enable and configure deflection at the global level on the Call Settings and Chat Settings pages. Deflection after hours of operation can be further customized for each leaf-queue in **Settings > Queue**.

The global Languages and Messages settings includes the setup for the voice recordings or Text-to-speech prompts needed once certain settings are enabled.

Add the appropriate messages once announcements or deflections are enabled.

## Details

When After Hour deflection is enabled, calls and chats will be deflected based on the specific operation hours for the queue, language, or channel the consumer has selected or has been routed to. While deflection options and configuration is done on the Call settings and Queue Settings pages, the actual hours are set on the **Support Center Details** settings page. There are multiple options you can offer callers once this setting is enabled.

After-hours deflection applies to contacts that arrive outside your hours of operation. Overcapacity deflection, which applies when wait times are high rather than when you are closed, is configured in the same Portal sections — Caller Announcements for calls and Web & Mobile Deflection for chats. For those options, including the overcapacity options for chats, see [Call settings: Overcapacity deflection and caller announcements](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#call-settings-overcapacity-deflection).

### Steps to fully enable and configure After Hour deflection

  1. Configure hours of operation for your environment - global and custom hours for each queue, channel, and language as needed.

  2. Enable and configure After Hour deflection for calls.

  3. Enable and configure After Hour deflection for chats.

  4. Configure per-queue deflection options (optional).

  5. Configure and upload appropriate greetings at **Settings > Languages and Messages**.




## CCAI Platform configuration

To configure after-hours, follow these steps.

### Enable and configure After Hour deflection for calls

  1. Go to **Settings** > **Call** > **Caller Announcements**.

  2. Toggle **Enable After Hour Deflection** to **On** to deflect callers when dialing in after scheduled hours of operation (set at **Settings > Support Center Details**).

  3. Select **Allow transfers to queues outside of hours of operation** for the following behavior:

Agents will be able to see the following queues as options to transfer to in the Agent Adapter:

All queues within operating hours

All queues that are outside of operation hours with after hour deflection enabled

All queues that are outside of hours of operation with no deflection enabled and active, logged-in agents

All queues that are after-hours with an assigned virtual agent in 24-hour availability mode

Agents won't be able to see the following types of queues:

All queues that are outside of operating hours with an assigned virtual agent limited to queue hours of operation




### Select Web & Mobile call deflection options

Under **Web & Mobile Calls**, in the **After-Hours Deflection** block, select the options to offer consumers outside your hours of operation. The regular call and chat options don't appear, and only the options you select are available.

  * **After-Hours Deflection** : Deflects consumers by presenting alternative options.

    * **Scheduled Call** : Shows a set of available times within the hours of operation for the queue to request a call.

    * **Email** : If after-hour deflection is enabled for email, a message is presented to end-users after-hours asking them to contact the email address listed. The email address listed is always the email listed in support center details.

      * Web: gives the consumer the email address to contact.

      * Mobile: default email app is launched with an email address in the "To" field, and data like app version and device type can be added to the email body by default.

      * Email address is set in **Settings > Support Center Details:**

    * **Phone number or Outbound SIP transfer** : _Only for Mobile SDK._ Deflects consumers to a phone number or SIP URI that you enter, or to a destination you select from a contact list. When a phone number is configured, the option appears as **Call now** and displays the number to dial.

    * **Voicemail** : _Only for Mobile SDK._ Allows consumers to leave a voicemail. Shows as "Leave a callback message." Voicemails will be delivered to agents assigned to the selected queue for calls.




#### Example deflection UI

Example Mobile SDK that is set to deflect to all options after-hours.

### Select IVR call deflection options

Under **IVR Calls** , in the **After-Hours Deflection** block, select the option to offer callers. Outside the hours of operation set in **Settings > Support Center Details**, calls deflect to the option you select.

**Queue:** If you have a 24-hour queue or just one with longer hours set, all calls will be sent to this queue.

**Phone number or Outbound SIP transfer** : Deflects the caller to a phone number or SIP URI that you enter, or to a destination you select from a contact list.

**Voicemail** : Allows caller to leave a voicemail.

Agents assigned to the queue that was called when operating hours were reached will be alerted of voicemails left as a result of this deflection setting. If this is applied to a top-level queue with no assignments, voicemails will be available in your CRM.

The message can be customized in **Settings** > **Languages & Messages** > **Voicemail** message.

Additional Voicemail message options are available under **Custom Callbacks**.

Voicemail - Phone Number Blocked

Voicemail - Request Phone Number

Voicemail - Phone Number Input Success

**Message Only:** "After Hour Deflection" message plays and the call ends. The message can be customized in **Settings** > **Languages & Messages** > **After Hour Deflection** message.

Click **Save Caller Announcements** to save the settings.

### Enable and configure After-Hour deflection for chats

  1. Go to **Settings** > **Chat** > **Web & Mobile** > **Web & Mobile Deflection**.

  2. **Enable After-Hour Deflection** : Enable to deflect chat requests outside of operating hours.

  3. Under **General** , select **Allow transfers to queues outside of hours of operation** for the following behavior:

This setting is optional and applies whether **Enable After Hour Deflection** is on or off. When After Hour Deflection is enabled for the destination queue, the consumer receives that queue's after-hours deflection experience after the transfer.

Agents will be able to see the following queues as options to transfer to in the Agent Adapter:

     1. All queues within operating hours

     2. All queues that are outside of hours of operation with no deflection enabled and active, logged-in agents

     3. All queues that are after-hours with after hour deflection enabled

     4. All queues that are after-hours with an assigned virtual agent in 24-hour availability mode

Agents won't be able to see the following types of queues:

All queues that are outside of operating hours with an assigned virtual agent limited to queue hours of operation

  4. Under **After Hour Deflection Options** , select **Email** , **External Deflection Links** , or both:

     1. **Email** : Deflects a consumer to email when they request chat support outside operating hours. The consumer is presented with the email address set in **Settings** > **Support Center Details** , within the body of the chat interaction.

     2. **External Deflection Links** : Presents the consumer with the external links you select. For more information, see [External deflection links](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-deflection-links).

  5. Click **Save Deflection**.




## Configure queue-specific settings

Available for IVR, Mobile, and SMS channels. Not available for Web.

### IVR

  1. Go to **Settings** > **Queue** > **IVR**.

  2. Click the queue you want to edit.

  3. Under **Custom After Hour Deflection** , turn on the switch.

**Message** : A message will play, then end the call. Default message set in **Settings** > **Call** or a Custom Greeting can be used.

**Queue** : Deflects the caller to another queue.

**Phone number** : Redirect callers after-hours to a phone number. Additional charges for call time apply.

**Voicemail** : directs the caller to voicemail with an option to customize the voicemail greeting.

  4. Click **Save After Hour Deflection**.




### Mobile

Mobile configuration allows for either deflecting to a queue, or a combination of other deflection options. If you are deflecting to a queue, the consumer cannot also have another option like leaving a voicemail.

  1. Go to **Settings** > **Queue** > **Mobile**.

  2. Click the queue you want to edit.

  3. Under **Custom After Hour Deflection** , turn on the switch.

Deflect to Queue: deflects the consumer to another queue

**OR**

Deflection Options (select one or more):

**Scheduled Call** : When scheduled calls are enabled in the Channel Settings for this queue, you can select this option to present consumers with timeslots for a scheduled call during operating hours.

**Email** : If after-hour deflection is enabled for email, a message will be presented to end-users after-hours asking them to contact the email address listed. The email address listed will always be the email listed in support center details. Default email app is launched with an email address in the "To" field, and data like app version and device type can be added to the email body by default. Email address is set in **Settings** > **Support Center Details**.

**Phone Number** : Deflects consumers to another phone number. Shows "Call now" and displays the number the phone will be dialing.

**Voicemail** : Allows consumers to leave a voicemail. Shows as "Leave a callback message." Voicemails will be delivered to agents assigned to the selected queue for calls.

**External Deflection Links** : Presents the consumer with the external links you select. For more information, see [External deflection links](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-deflection-links).

  4. Select **Save Custom After Hour Options**.




### SMS

  1. Go to **Settings** > **Queue** > **SMS**.

  2. Click the queue you want to edit.

  3. Scroll to SMS Chat System Messages section and mark the checkbox next to **Enable after hour message**.

  4. Enter the text message to send to consumers.

  5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
