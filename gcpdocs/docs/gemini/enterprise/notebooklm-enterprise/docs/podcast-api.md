---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/
title: Generate podcasts (API method) \u00a0|\u00a0 Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:55:46.005062+00:00
---

# Generate podcasts (API method)  |  Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/

[ Skip to main content ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/)
  * [Deutsch](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=de)
  * [Español](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=it)
  * [Português](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-spark-blue-192px.svg) ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Inputs](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#inputs)
  * [Output](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#output)
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#before-you-begin)
  * [Generate a podcast from context input](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#generate-podcast)
  * [Compliance](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#compliance)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)


Was this helpful?
Send feedback 
#  Generate podcasts (API method) Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Inputs](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#inputs)
  * [Output](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#output)
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#before-you-begin)
  * [Generate a podcast from context input](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#generate-podcast)
  * [Compliance](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#compliance)


Gemini Enterprise offers an API that lets you generate podcasts based on source documents. The output is very similar to the podcasts that end users can generate from within their notebooks.
Podcast generation through the API is well suited for batch jobs where you might have dozens or hundreds of books, articles, or courses, and you want to generate a podcast for each.
The [Podcast API](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.podcasts.operations) is a standalone API. That is, you don't need a Gemini Notebook Enterprise notebook, a Gemini Enterprise license, or a data store. All you need is an enabled Google Cloud project and the Podcast API User role.
## Inputs
The input for the API is an array of `context` elements. This is the source material that the podcast gets generated from. The input can be in the form of text, images, audio, and video. The total content of the context array must be less than 100,000 tokens.
For a list of supported types, see the technical specifications for images, documents, video, and audio on this page about [Gemini 2.5 Flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash).
## Output
The output from the API is the podcast, in MP3 format.
## Before you begin
Before you can generate a podcast using the API, you must have the following:
  * A Google Cloud project with the Discovery Engine API enabled. See [Create a project and enable the API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm#create-project-enable-api).
  * The [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) role of Podcast API User (`roles/discoveryengine.podcastApiUser`). For general information about granting roles, see [Set up Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm).


## Generate a podcast from context input
Use the following command to generate a podcast by calling the [podcast](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.podcasts.operations) method.
The input is an array of multimedia objects such as text, images, and audio and video clips.
[REST](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api/#rest) More
To generate and export a podcast, do the following:
  1. Run the following curl command:

```
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/podcasts" \
  -d '{
      "podcastConfig": {
        "focus": "FOCUS",
        "length": "LENGTH",
        "languageCode": "LANGUAGE_CODE"
      },
      "contexts": [
        {
          "text": "TEXT_CONTENT"
        },
        {
          "inlineData": {
            "mimeType": "MIME_TYPE",
            "data": "BASE64_ENCODED_DATA"
          }
        }
      ],
      "title": "PODCAST_TITLE",
      "description": "PODCAST_DESCRIPTION"
  }'

```

Replace the following:
     * `PROJECT_ID`: the ID of your project.
     * `FOCUS`: a prompt where you suggest the focus of the podcast. 
     * `LENGTH`: there are two options: 
       * `SHORT` (typically 4-5 minutes)
       * `STANDARD` (typically around 10 minutes but it can be shorter with smaller data sets)
     * `LANGUAGE_CODE`: optional. Specify the language code for the podcast. Use language tags defined by [BCP47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). If the language code isn't provided, then the podcast is generated in English. 
     * `TEXT_CONTENT`: The text content to be included.
     * `inlineData`: An object for non-text media.
     * `MIME_TYPE`: The MIME type of the blob data (for example, "image/png").
     * `BASE64_ENCODED_DATA`: The base64-encoded raw bytes of the media data.
     * `PODCAST_TITLE`: a title for the podcast. This can be for internal use, or you can choose to display it to your end users. 
     * `PODCAST_DESCRIPTION`: a description of the podcast. This can be for internal use, or you can choose to display it to your end users. 
Example command and result 
```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/podcasts" \
-d '{
    "podcastConfig": {
      "focus": "Can you talk about how to find a job in Google?",
      "length": "SHORT"
    },
    "contexts": [
      {
        "text": "Breaking into Google is a highly competitive endeavor, attracting millions of applicants globally due to its reputation as a top employer, its innovative work, and comprehensive perks. Success hinges on a multi-faceted approach, starting with meticulously tailored online applications that incorporate job description keywords for ATS and showcasing Googlyness—a blend of curiosity, collaborative spirit, and leadership potential. The rigorous, multi-stage interview process involves recruiter screens, behavioral interviews (often using the STAR method), and for technical roles, demanding coding challenges and system design questions that assess not just correct answers but also problem-solving thought processes and communication skills. Networking for referrals and informational interviews can significantly boost visibility, but ultimately, thorough preparation through mock interviews and platforms like LeetCode, combined with patience and resilience through the often lengthy process, are paramount for navigating this challenging but rewarding path."
      },
      {
        "inlineData": {
          "mimeType": "image/png",
          "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
        }
      }
    ],
    "title": "Find a job at Google ",
    "description": "This podcast is based on a plain text document and an image that describe various aspects of getting a job at Google."
}'

* * *

{
"name": "projects/123456/locations/global/operations/create-podcast-54321"
}

```

It takes a few minutes to generate a podcast.
  2. Make note of the operation name; you need it to download the podcast in step 4. In the example above, the operation name is `projects/123456/locations/global/operations/create-podcast-54321`.
  3. Optional. Poll the status of the podcast creation operation. See [Get details about a long-running operation](https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations#get-details).
  4. After the operation has finished, run the following curl command to download the podcast:

```
curl -v \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  "https://discoveryengine.googleapis.com/v1/OPERATION_NAME:download?alt=media" \
  --output FILENAME.mp3 -L

```

Replace the following:
     * `OPERATION_NAME`: the name of the operation that you noted down in step 2.
     * `FILENAME`: a filename for the podcast.
This command downloads the podcast to an MP3 file in your local directory.
Example command and result 
```
curl -v \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  "https://discoveryengine.googleapis.com/v1/projects/123456/locations/global/operations/create-podcast-54321:download?alt=media" \
  --output my-podcast.mp3 -L
  
* * *

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                               Dload  Upload   Total   Spent    Left  Speed
0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Host discoveryengine.googleapis.com:443 was resolved.
  ...
{ [42044 bytes data]
100 14.3M  100 14.3M    0     0  10.9M      0  0:00:01  0:00:01 --:--:-- 29.7M
* Connection #0 to host discoveryengine.googleapis.com left intact

```



## Compliance
The podcast API isn't in compliance with customer-managed encryption keys, [CMEK for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/cmek).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
