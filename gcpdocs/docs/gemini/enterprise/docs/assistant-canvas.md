---
url: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/
title: Create and edit documents and slides in Canvas \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:53:21.438201+00:00
---

# Create and edit documents and slides in Canvas  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/

[ Skip to main content ](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/)
  * [Deutsch](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-spark-blue-192px.svg) ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#before_you_begin)
  * [Create a document or a slide in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#create_a_document_or_a_slide_in_canvas)
    * [Source citations](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#source_citations)
  * [Edit a document in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#edit_a_document_in_canvas)
  * [Edit a slide in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#edit_a_slide_in_canvas)
  * [Export documents and slides from Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#export_documents_and_slides_from_canvas)
    * [Export a document](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#export_documents)
    * [Export a slide presentation](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#export_slides)
  * [Limitations](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#limitations)
  * [Best practices](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#best_practices)


**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)


Was this helpful?
Send feedback 
#  Create and edit documents and slides in Canvas Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#before_you_begin)
  * [Create a document or a slide in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#create_a_document_or_a_slide_in_canvas)
    * [Source citations](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#source_citations)
  * [Edit a document in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#edit_a_document_in_canvas)
  * [Edit a slide in Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#edit_a_slide_in_canvas)
  * [Export documents and slides from Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#export_documents_and_slides_from_canvas)
    * [Export a document](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#export_documents)
    * [Export a slide presentation](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#export_slides)
  * [Limitations](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#limitations)
  * [Best practices](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#best_practices)


Canvas is a dedicated, interactive tool within Gemini Enterprise that helps you create AI-generated documents and slide presentations from your conversations. You can work on your documents and slides side-by-side with your chat, without needing to switch between applications.
## Before you begin
Before you can use Canvas in Gemini Enterprise, an administrator must enable the feature toggle and configure any necessary permissions. For more information, see [Configure Canvas](https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas).
## Create a document or a slide in Canvas
To create a document or a slide in Canvas:
  1. Sign in to the Gemini Enterprise web app.
  2. Start a new chat.
  3. Click **Tools** in the chat box. A list of shortcuts appears.
  4. Select **Canvas** , or enter a prompt that implies creating a document or slide.
  5. Enter a prompt.
  6. (Optional) To upload files or an image with your prompt, click **+ Add files**.
  7. Click **Submit**. The document or the slide presentation opens in the Canvas editor on the right.


### Source citations
To view the references and search results used to generate documents, click **Sources** directly under the AI's response.
For slides, a final **Image Sources** slide is automatically included, containing all the metadata for the images used in your deck.
## Edit a document in Canvas
You can edit a document in the following ways:
  * **Direct edits** : In the Canvas space, you can manually add, edit, or delete text, change formatting like headings, bold, and italics, and create bulleted and numbered lists. Changes are auto-saved.
  * **AI-powered edits** : At the bottom right of the Canvas panel, use the **Change length** and **Change tone** sliders for global adjustments to tone and length, or provide detailed chat feedback for more specific edits.
  * **Highlight to edit** : To refine a specific section of text, highlight it and enter your instructions in one of two ways. You can type directly into the **Ask Gemini** box that appears next to your selection, or use the main prompt box to tell Gemini Enterprise how you want that section rewritten.


You can also use the undo and redo options on the toolbar to navigate between different saved versions of your document.
## Edit a slide in Canvas
To open and edit a slide presentation in Canvas:
  1. Go to the chat where you generated the slides.
  2. Click **Open**.
  3. In the chat box, enter your suggestions to update the slides.
  4. Click **Submit**.


## Export documents and slides from Canvas
You can export documents and slides from Canvas to download and edit it in your preferred application.
Export a document
To export a document from Canvas:
  1. Open the chat with the Canvas document that you want to export.
  2. At the top right of the Canvas panel, click **Export**. You can export to Google Docs, DOCX, or PDF.
  3. You can also copy all text to your clipboard. To copy all text, at the top right of the Canvas panel, click **Copy**.


Export a slide presentation
To export a slide presentation from Canvas:
  1. Open the chat with the Canvas slides that you want to export.
  2. At the top right of the Canvas panel, click **Export**. You can export to Google Slides, Microsoft PowerPoint, or PDF.


## Limitations
  * Canvas isn't supported on the mobile app. It's only available on the web app.
  * When you [share a conversation](https://docs.cloud.google.com/gemini/enterprise/docs/share-conversations), recipients can't open or edit documents or slide presentations created in Canvas. To share Canvas content with others, [export](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas/#export_documents_and_slides_from_canvas) the document or slide presentation to Google Docs, Google Slides, or another supported format, and then share the exported file.


## Best practices
When generating content in Canvas, follow these best practices:
  * For complex documents and presentations, provide clear and detailed prompts, with other Gemini Enterprise knowledge artifacts as sources and template references.
  * Always review and edit the AI-generated content to ensure that it meets your requirements.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
