---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-deflection-links/
title: External deflection links \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:57.932601+00:00
---

# External deflection links  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-deflection-links/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  External deflection links Stay organized with collections  Save and categorize content based on your preferences. 

The aim of External Deflection Links is to provide another channel where information is readily available for consumers, like an FAQ page, and where they may be able to get an answer faster. It will also help contact centers reduce inbound requests to Agents.

When a consumer clicks on an external deflection link:

Consumers will also be able to return to the support experience after visiting a redirection link, so they can get more help from an agent if the redirect didn't resolve their request or question.

## Mobile experience

In the Mobile SDK, external deflection links will be displayed underneath the available call chat and email options. The icon, name, and call to action, are displayed as configured on the Deflection Links overview page.

### Visiting an external deflection link

When the consumer clicks on the external deflection link, the configured mobile deep link launches the associated app.

### Return to the support session

When returning to the support session after having visited an external deflection link, the consumer is presented with a alert asking _Did that resolve your issue?_

The option buttons available are **No** or **Yes**.

  * If a consumer clicks **No** : The alert is closed and the respective queue's contact options are displayed again.

  * If a consumer clicks **Yes** : The alert is closed and the support session is ended. The consumer is returned to the originating app's screen where they initiated the support session.




### External deflection links time limit

When returning to the support experience **after 5 minutes** of visiting an external deflection link, the alert is not presented, and the help session is terminated.

The user is returned to the originating screen where they initiated the support session.

## Web experience

The icon and name displayed here will be retrieved from your administrator configuration on the Deflection Links overview page in the CCAI Platform portal.

When there are **less than five alternatives** , the Web SDK displays external deflection links as follows:

When there are **more than five alternatives** , the Web SDK displays external deflection links as follows:

### Visit an external deflection link

When the consumer clicks on the external deflection link, the configured URL opens within a new tab in the user's active browser window.

### Return to the support session after visiting an external deflection link

When the consumer returns to the support session, within 5 minutes, after having visited an external deflection link, they're presented with a alert asking _Did that resolve your issue?_

The option buttons available are **No** or **Yes**.

  * When a consumer clicks **No** : The alert is closed and the respective queue's contact options are displayed again.

  * When the consumer clicks **Yes** : The alert is closed and the support session is ended.




The user is returned to the originating screen where they initiated the support session.

### External deflection links time limit

When returning to the support experience after 5 minutes of visiting an external deflection link, the alert is not presented, and the help session is terminated.

The user is returned to the originating screen where they initiated the support session.

## Configuration

External Deflection Links give you the ability to offer additional support options in addition to our standard chat, call and email options. For example, add a Billing FAQ link to your Billing queue or link to your social media channels. External Deflection links can be configured as the only support options.

The external deflection link appears in the UI based on how it is created in the Add Deflection Links configuration panel (for example: the name, a call to action, and the icon upload).

### Prerequisites

For Web: Web SDK version 2.2 or later

For Mobile: Mobile SDK version 0.41.0 or later

### Admin configuration

  1. Go to **Settings > Chat > Web & Mobile > External Deflection Links**.

  2. Select **View links**.

The **Deflection Links** overview page will load.

If deflection links are configured a list of links will appear.

This list will be empty if no deflection links are set.




#### Deflection links overview page

The **Deflection Links** overview page lists all configured external deflection links.

Further information displayed includes: if the link is enabled (**On** /**Off**), configuration details (display name, URL, icon) as well as assigned queues.

## Add a deflection link

  1. To add a deflection link, select **Add Deflection Link**.

A new window, the **Add Deflection Links** configuration panel will open.




### Add deflection links configuration panel

The identification, name, and URL are all **required** to be entered in this panel to add the deflection link. This is where you may add a call to action (optional and just for mobile). Icons will also be uploaded here.

The following fields are required:

  * **Identifier** : Enter the name used within the portal only (internal reference). For example, Spanish version FAQ.

  * **Displayed Name** : Enter the name to be displayed to the consumer. If using another language you will need to add the name here in that language.

  * **URL** : Enter the URL to where the deflection link will direct.


**Tip:** **Call to Action** (optional; only applicable to mobile): Enter a call to action, which appears like help text below the name of the link — for example, _Join our community support members here!_

### Upload icons

**Note:** If icon upload fields are left blank, the default deflection icon  will show for mobile and web.

#### Mobile icons

Enter the **Mobile Icon** name:

The icon name **must** match the icon's filename in the iOS asset catalog and/or the Android drawable folder. Check the iOS and Android README file for more details.

#### Web icon

By default, the default deflection link web icon is displayed.

If a web icon has been previously uploaded that icon will display.

To upload a web icon:

  1. Click the web icon ![Upload a web icon](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16331bc47671b9.jpg) to select a file from your file explorer.

**Recommendation** : For the best display experience, upload an SVG file.

The uploaded icon will now display.

  2. Select **Save**.

The **Add Deflection Links** panel will close.

The external deflection link you just set is now available as a new support option at the bottom of the **Deflection Links** overview page.

This new deflection link will start off without being assigned to any queues and will start in the **On** state.




## Assign an external deflection link to a queue

  1. Go to **Settings > Queue > Mobile** or **Web**.

  2. Click a leaf-queue. A panel on the side shows the queue **Settings**.

  3. Check the **External Deflection Links** checkbox. If that queue doesn't have an assigned external deflection link, then _No deflection links selected_ is displayed.

  4. Open the **Select Deflection Links** list.

  5. Select which external deflection links you would like to assign to the queue so that it appears to consumers in the UI.

  6. Select **Add**.

  7. Check the **External Deflection Links** checkbox.




## Set external deflection links as an option

Set an external deflection link as an after-hours deflection and/or an overcapacity deflection.

### After-hour deflection option (web and mobile only)

  1. Go to **Settings > Chat > Web & Mobile > Web & Mobile Deflection**. Under **Web & Mobile Chats**, find **After Hour Deflection Options**.

  2. Under **After Hour Deflection Options** , open the **Select Deflection Links** list. The drop-down component displays the list of options that are turned **On** in the **Deflection Links** overview page. By default, no custom deflection links are selected.

  3. Select which external deflection links you would like to assign as an after hour deflection option.

  4. Select **Add**.

  5. Select **Save Deflection**.




### Overcapacity deflection option

  1. Go to **Settings > Chat**.

  2. In **Web & Mobile Deflection**, under **Web & Mobile Chats**, find **Overcapacity Deflection Options**.

  3. Open the **Select Deflection Links** list. The drop-down component displays the list of options that are turned **On** in the **Deflection Links** overview page. By default, no custom deflection links are selected.

  4. Select which external deflection links you would like to assign as an overcapacity deflection option.

  5. Select **Add**.

  6. Select **Save Deflection**.




This globally applies the selected deflection links as after-hour / overcapacity deflection options.

### Mobile queue-specific custom after-hour deflection

External deflection links can be set for a custom after-hour deflection.

This is available only for mobile. Custom after-hours deflection isn't supported for web.

  1. Go to **Settings > Queue > Mobile > Custom After Hour Deflection > Deflection Options**.

  2. Under **Deflection Options** , check the **External Deflection Links** checkbox. The number beside **External Deflection Links** indicates how many deflection links are available.

  3. Select which external deflection link to apply.

  4. Select **Add**.

  5. Select **Save Custom After Hour Options**.




This applies the selected deflection link to the respective queues after-hour deflection options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
