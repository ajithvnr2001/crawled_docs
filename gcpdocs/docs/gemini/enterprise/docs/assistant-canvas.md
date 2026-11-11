---
url: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/
title: Create documents, slides, and web apps in Canvas \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:24.796817+00:00
---

# Create documents, slides, and web apps in Canvas  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Create documents, slides, and web apps in Canvas Stay organized with collections  Save and categorize content based on your preferences. 

Canvas is a dedicated, interactive tool within Gemini Enterprise that helps you create AI-generated documents, slides, and interactive web apps from your conversations. You can work on your documents, slides, and apps side-by-side with your chat, without needing to switch between applications.

## Before you begin

Before you can use Canvas, an administrator must enable the [Canvas feature toggles](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features) and configure any necessary permissions. For more information, see [Configure Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas).

## Create a document or a slide in Canvas

To create a document or a slide in Canvas:

  1. Sign in to the Gemini Enterprise web app.

  2. Start a new chat.

  3. Click **Tools** in the chat box. A list of shortcuts appears.

  4. Select **Canvas** , or enter a prompt that implies creating a document or slide.

  5. Enter a prompt.

**Note:** Your chat conversation history, content from enabled connectors, and explicitly added sources are used as input.
  6. (Optional) To upload files or an image with your prompt, click **\+ Add files**.

  7. Click **Submit**. The document or the slide presentation opens in the Canvas editor on the right.




### Source citations

To view the references and search results used to generate documents, click **Sources** directly under the AI's response.

For slides, a final **Image Sources** slide is automatically included, containing all the metadata for the images used in your deck.

## Create a web app in Canvas

You can ask Gemini Enterprise to create interactive single-page HTML-based web apps. Describe an app, dashboard, or prototype in chat, and Canvas generates a working, interactive single-page app as a single self-contained HTML file, with no code required. You can preview, edit, share, and download the generated HTML file.

To create a single-page web app:

  1. Sign in to the Gemini Enterprise web app.

  2. Start a new chat.

  3. Click **Tools** or type `/` in the chat box. A list of shortcuts appears.

  4. Select **Canvas** , or enter a prompt that describes the web app you want to create (for example, `"Build an ROI calculator with sliders for headcount and hourly cost"`).

  5. Click **Submit**. Canvas generates the app and displays a live preview.




## Edit a document in Canvas

You can edit a document in the following ways:

  * **Direct edits** : In the Canvas space, you can manually add, edit, or delete text, change formatting like headings, bold, and italics, and create bulleted and numbered lists. Changes are auto-saved.

  * **AI-powered edits** : At the bottom right of the Canvas panel, use the **Change length** and **Change tone** sliders for global adjustments to tone and length, or provide detailed chat feedback for more specific edits.

  * **Highlight to edit** : To refine a specific section of text, highlight it and enter your instructions in one of two ways. You can type directly into the **Ask Gemini** box that appears next to your selection, or use the main prompt box to tell Gemini Enterprise how you want that section rewritten.




You can also use the undo and redo options on the toolbar to navigate between different saved versions of your document.

**Note:** You can edit a document in Canvas only during the session in which it was generated. To continue editing later, export the document to another app.

## Edit a slide in Canvas

To open and edit a slide presentation in Canvas:

  1. Go to the chat where you generated the slides.
  2. Click **Open**.
  3. In the chat box, enter your suggestions to update the slides.
  4. Click **Submit**.

**Note:** Each update generates a completely new Canvas artifact. The existing artifact is not modified or versioned.



## Edit an app in Canvas

You can review and edit an app in Canvas in the following ways:

  * **Interactive preview** : Test the app directly in the Canvas panel. You can click buttons, type in text fields, and switch tabs to see reactive updates in real time.
  * **Targeted chat edits** : Ask Gemini Enterprise to make specific changes globally or locally (for example, `"Make the chart a bar chart"` or `"Add a dark mode toggle"`). The app updates through search-and-replace edits without regenerating the entire file.
  * **Select and ask** : Highlight a specific element within the app preview to focus your edit request on just that component.
  * **Code and skill view** : View the underlying code and the skill configuration used to generate the app in a read-only view.



To edit your app:

  1. In the chat box next to the Canvas preview, enter instructions describing the changes or updates you want (for example, `"Change the chart to a stacked bar chart"` or `"Add a dark mode toggle"`).

  2. Click **Submit**. Canvas updates the app and refreshes the live preview.




### View previous app versions

You can use the version history controls on the toolbar to review and compare current and previous versions of your app.

![Create a single-page interactive app in Canvas](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/canvas-html-spas.png)A single-page interactive app in Canvas 

From the toolbar, you can also do the following:

  * Share the app with anyone in your organization.
  * Download the HTML file.
  * Expand to fullscreen.
  * Close the preview.



### Web app limitations

The following limitations apply when creating and running web apps in Canvas:

  * **Single-file** : Canvas web apps are generated as a single, self-contained HTML file (combining HTML, CSS, and JavaScript) that runs entirely in the browser.
  * **No persistent storage or database** : App state lives within the active browser session. There is no built-in database or server to persist data across users or sessions.
  * **No managed hosting or deployment** : You can preview the app in the Canvas panel or in a browser, but it isn't hosted at a managed URL or run as a public-facing web service.
  * **Limited external API calls** : Calls that require secret authentication keys or backend server processing aren't supported because there is no secure server-side component to store credentials.
  * **Client-side compute only** : Heavy processing, long-running jobs, or tasks requiring server-side execution aren't supported.
  * **Complexity and size ceilings** : Very large or highly complex apps might exceed generation or context limits. For best results, break large or complex workflows into smaller, targeted apps.
  * **File types and size limits** : Files and attachments must adhere to standard Gemini Enterprise file format and size limits. For more information, see [File formats and size limitations](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#file_formats_and_size_limitations).



## Export and download content from Canvas

You can export documents and slides, or download web apps, to view, share, or continue editing them outside Gemini Enterprise.

### Before you export to Google Docs or Google Slides

When you export to Google Docs or Google Slides, Gemini Enterprise creates the file in your own Google Drive by using your Google Account. The export doesn't use the Google Drive data store of the app, so it can fail even when the Google Drive connector works. Before you export, make sure that the following requirements are met:

  * **Authorize Google Drive access.** When you export a file for the first time, you are prompted to authorize Gemini Enterprise and allow access to your Google Drive. If you see **Export operation failed** , make sure that pop-ups are not blocked for Gemini Enterprise by enabling browser pop-ups for Gemini Enterprise and then try again. If you get a permission error after authorizing, remove Gemini Enterprise from your Google Account third-party apps and export again to reauthorize.

  * **Your Google Workspace administrator allows Drive SDK access.** Your Google Workspace administrator must allow users to access Google Drive with the Drive SDK API. In the Google Admin console, this setting is under **Apps > Google Workspace > Drive and Docs > Features and Applications > Drive SDK**. If the setting is turned off, the export fails with a permission denied error.

  * **You have the Canvas permissions on the Google Cloud project.** You need the Canvas permissions on the Google Cloud project of your Gemini Enterprise app, even if you access Gemini Enterprise with a Google Workspace license. If you can't open or export Canvas content, ask your administrator to review [Add Canvas permissions](https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas#add-canvas-permissions).




Gemini Enterprise saves the exported file in your My Drive. You can't export directly to a shared drive, to Microsoft OneDrive, or to Microsoft SharePoint. To store the file in another location, move the file in Google Drive after the export, or download the file and upload it to the other location.

### Export a document

To export a document from Canvas:

  1. Open the chat with the Canvas document that you want to export.
  2. At the top right of the Canvas panel, click **Export**. You can export to Google Docs, DOCX, or PDF.
  3. You can also copy all text to your clipboard. To copy all text, at the top right of the Canvas panel, click **Copy**.



### Export a slide presentation

To export a slide presentation from Canvas:

  1. Open the chat with the Canvas slides that you want to export.
  2. At the top right of the Canvas panel, click **Export**. You can export to Google Slides, Microsoft PowerPoint, or PDF.



### Download an app

To download your web app from Canvas:

  1. Open the chat with the Canvas app that you want to download.
  2. From the toolbar in the preview panel, click the **Download** button to save the self-contained `.html` file to your computer.



### Export to Google Docs and Google Slides

If you're a Google Workspace user, you can export your Canvas creations directly to Google Docs and Google Slides. For **Export to Google Docs** or **Export to Google Slides** options to appear and function correctly, your environment must meet specific configuration and licensing requirements as follows:

  * Your account must have an active Google Workspace license. The export feature isn't available for accounts without Google Workspace access.
  * A Google Drive data store must be successfully connected and tied to your Gemini Enterprise app.
  * Your Google Workspace administrator must have data access enabled for Gemini Enterprise. **Export to Google Docs** and **Export to Google Slides** are hidden if data access is turned off at the administrative level.



#### Troubleshooting export issues

  * **The Export button is missing** : This typically indicates your account is either BYOID or doesn't have access to Google Workspace, or that you haven't configured your Google Drive data store in Gemini Enterprise, or your Google Workspace administrator has turned off Google Workspace access by Gemini Enterprise.
  * **The Export fails after clicking** : This happens if there is an account mismatch between your account and the account with which the Google Drive data store is connected. Verify that you're logged in using the correct identity.



### Download a file

When you export to DOCX, PDF, or Microsoft PowerPoint, Gemini Enterprise generates the file and your browser downloads it. If the download fails, the message that you see indicates the cause:

  * **You are not allowed to perform this operation** : your organization's policies rejected the request, for example because you don't have the Canvas permissions on the Google Cloud project, or because of a Context-Aware Access or VPC Service Controls policy. Contact your administrator.
  * **Failed to download PDF** , **DOCX** , or **PPTX** : the request didn't complete. This usually means that it was blocked before it reached Gemini Enterprise, for example by endpoint security or data loss prevention software on your device, by a secure web gateway or proxy, or by a managed-device policy. Ask your IT administrator to check these controls.



If you can't download the file, export the content to Google Docs or Google Slides instead, and then download it from Google Drive in the format that you need.

## Limitations

  * Canvas isn't supported on the mobile app. It's only available on the web app. The mobile app also can't open or download documents, slide presentations, or PDF files that are generated in a chat. To open or download generated files, use the web app in a desktop or mobile browser.
  * When you [share a conversation](https://docs.cloud.google.com/gemini/enterprise/docs/share-conversations), recipients can't open or edit documents or slide presentations created in Canvas. To share Canvas content with others, export the document or slide presentation to Google Docs, Google Slides, or another supported format, and then share the exported file.
  * Canvas documents use Markdown formatting. Text colors, custom fonts, and other HTML styling aren't supported in the Canvas editor. To apply rich formatting, export the document to Google Docs and format it there.
  * Images in slide presentations come from web search with the **Google search** web grounding option. If web grounding is turned off for your Gemini Enterprise app, or if the app uses the **Enterprise web search** option, the generated slides don't contain images. For more information, see [Configure the assistant](https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant).
  * Canvas creates slide presentations (including Microsoft PowerPoint files) when you ask the assistant or a custom agent to generate them. If your administrator turns off Canvas for your app, you can't generate presentations. PDF and DOCX documents don't depend on Canvas. For more information, see [Configure Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas).



## Best practices

When generating content in Canvas, follow these best practices:

  * For complex documents and slides, provide clear and detailed prompts, with other Gemini Enterprise knowledge artifacts as sources and template references.

  * When updating apps and slides, request focused, incremental changes (for example, adjust one component or visual style at a time).

  * Always review and edit the AI-generated content to ensure that it meets your requirements.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
