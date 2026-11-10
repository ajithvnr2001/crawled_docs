---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/adobe/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:46:28.562528+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/adobe/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The Adobe data store for Gemini Enterprise lets you search, share, and manage your Adobe Creative Cloud assets, customize Adobe Express templates, apply Lightroom presets, perform Photoshop-style image edits, and create, compress, OCR, or convert PDFs with Adobe Acrobat using natural language.

## Supported actions

When you enable the Adobe data store, you can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Asset add file | Open the file picker so user can select an image/video/document to edit or process.  
Asset create folders | Create one or more folders in Adobe Creative Cloud Files storage for organizing assets.  
Asset finalize file upload | Completes a block upload after all file chunks have been transferred to Adobe Creative Cloud storage.  
Asset initialize file upload | Initiates a block upload for a file to Adobe Creative Cloud storage.  
Asset invite collaborators | Adds one or more collaborators to an Adobe asset or project at a specified role: Viewer, Commenter, Editor, or Consumer.  
Change background color | Update the background color of an Express design.  
Fill text | Fill placeholder text fields in an Adobe Express design template with specific content.  
Image apply adjustments | Adobe Photoshop and Lightroom professional image adjustments.  
Image apply auto tone | Automatically corrects the tonal balance of the images in one step by adjusting exposure, contrast, highlights, shadows, whites, and blacks.  
Image apply effects | Applies a single Photoshop filter or style effect to the image or an area.  
Image apply preset | Applies a named Lightroom preset to the image, transforming its look in one step.  
Image crop and resize | Smart crop and resize with subject-aware positioning.  
Image crop to bounds | Crop images to exact geometric bounds using normalized coordinates (0-1).  
Image fill area | Fills a masked area of the image with a solid color at a specified opacity.  
Image generate | Generates a brand-new image from a text prompt using generative AI.  
Image generative expand | Expand images by generating new content around their edges.  
Image get task status | Waits for an operation that a previous tool call started but did not finish, and returns its result once ready.  
Image instruct edit | Applies generative edits to an image using plain-language instructions about what to change.  
Image invert selection | Invert the current selection mask. This selects everything that wasn't selected and deselects everything that was.  
Image remove background | Detects the main subject and creates a cutout.  
Image remove blemishes | Removes skin blemishes, spots, and surface imperfections from an image using AI healing.  
Image select by prompt | Select specific objects in the image so you can apply effects or adjustments to those objects only.  
Image select subject | Selects the main subject or subjects in an image and creates a selection mask.  
Replace image | Replace or change a visual element in the Express Design with a different image or appearance.  
  
The following Adobe Acrobat actions are read-only and always available, so you don't need to enable them.

Action | Description  
---|---  
Markdown to PDF | Converts Markdown or plain text from the conversation into a PDF document.  
PDF compress | Compresses a PDF file to reduce its size while maintaining quality.  
PDF create | Creates a PDF from documents such as Word, PowerPoint, Excel, images, or text.  
PDF export | Exports a PDF to other formats, such as Word, PowerPoint, Excel, or RTF.  
PDF OCR | Applies optical character recognition (OCR) to a scanned PDF so that its text is searchable and selectable.  
PDF operation status | Checks the status of an asynchronous PDF operation and returns its result once ready.  
PDF to image | Converts PDF pages to JPEG or PNG images.  
PDF to Markdown | Converts PDF documents to Markdown for text extraction.  
**Note:** Additional read-only actions are also available.

## Limitations

The Adobe data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Adobe data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Adobe data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a data store with Adobe, see [Set up a Adobe data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/adobe/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
