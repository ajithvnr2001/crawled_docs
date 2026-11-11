---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-level-wrap-up-settings/
title: Queue-level wrap-up settings \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:08:55.006403+00:00
---

# Queue-level wrap-up settings  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-level-wrap-up-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue-level wrap-up settings Stay organized with collections  Save and categorize content based on your preferences. 

Queue-level wrap-up settings allow you to customize communication wrap-up times for different queues within a contact center, to ensure that agents have adequate time to complete their tasks without compromising service level agreements or taking another call or chat before they are ready. This is particularly useful for queues that handle different types of issues, such as escalations or complex issues, which may require more time to handle.

Queue wrap-up settings can be defined explicitly for a leaf-queue or defined at a parent level to allow for the settings to be shared and reduce the overhead of defining the settings for each leaf menu.

## Define wrap-up queue level settings

Wrap-up settings are inherited by all queues globally by default, unless they are overridden (redefined) at the queue level or at the parent queue level. Global settings are defined in Operations Management.

To adjust the wrap-up settings for a queue:

  1. Open the settings for the queue you want to configure.

  2. Go to **Wrap-up Settings**.

  3. Select **Configure**.




The **Wrap-up Settings** panel for that queue opens.

## Wrap-up settings

When you open the **Wrap-up Settings** panel, you can see if the settings are inherited or have been previously defined for the queue.

### Wrap-up exceeded

This setting transitions agents into **Wrap-up Exceeded** status once they have gone beyond a wrap-up threshold time and have cleared all ongoing sessions. When an agent transitions to **Wrap-up Exceeded** status, an agent-level notification appears.

**Note:** **Wrap-up Exceeded** requires **Automatic wrap-up** to be enabled for the applicable channel (inbound calls, outbound calls, or chats). Disposition codes and notes are not required.

For more information, see [Wrap-up Exceeded Status](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status#wrap-up_exceeded_status) and [Agent Statuses](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status).

### Automatic wrap-up for calls

This setting automatically ends a call or chat session after a set period of time. This feature is typically used to help agents manage their time more efficiently, and to ensure that all calls or chats are properly documented and closed out.

If unconfigured, then manual wrap-up activity will automatically be assigned to the agent's last completed call or chat session.

#### Disposition codes and notes

Once **Automatic wrap-up for calls** is toggled on, the settings for disposition notes and codes become available. This includes applying a disposition code list which contains the set of all available disposition codes for a specific queue.

Disposition codes and notes are tools that allow agents to document the final outcome of a customer interaction.

The codes are used to classify and label inbound and outbound sessions, while the notes provide additional context about the session outcome. This feature helps to inform the team of the context of the session and streamline the follow-up process for efficiency.

For more information, see [About Disposition Codes, Notes, and Lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-note).

#### Exceptions

There are certain situations where wrap-up is bypassed:

  * Forced logout using the Apps API while in-call
  * In wrap-up but got force logged out by administrator or manager
  * Origin call of a callback
  * Call never reached agent
  * Call never reached end user
  * Call connected but dropped shortly, call duration is too short



For these scenarios, there is no wrap-up or disposition input data if checking in reports.

#### Set automatic wrap-up for calls

To set automatic wrap-up for calls, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to **Wrap-up settings** , and then click **Configure**. The **Wrap-up** pane appears.

  5. Do one of the following, or both, depending on your requirements:

     * To set automatic wrap-up for inbound calls, do the following:

       1. Click the **Automatic wrap-up for inbound calls** toggle to the on position.

       2. Set the number of seconds after which the agent's status switches to **Available**.

     * To set automatic wrap-up for outbound calls, do the following:

       1. Click the **Automatic wrap-up for outbound calls** toggle to the on position.

       2. Set the number of seconds after which the agent's status switches to **Available**.

  6. Click **Save**.




### Manual wrap-up

If an agent manually changes their status to **Wrap-up** in the agent adapter, by default, wrap-up activities are assigned to the agent's last completed call or chat session. You can also [configure manual wrap-up attribution](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-disposition-timing#configure-manual-wrap-up)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
