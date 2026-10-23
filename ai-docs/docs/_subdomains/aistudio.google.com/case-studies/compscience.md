---
url: https://aistudio.google.com/case-studies/compscience/
title: CompScience | Google AI Studio
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (86 chars), fallback to crawl4ai)
fetched_at: 2026-10-15T19:34:25.086863+00:00
---

# CompScience | Google AI Studio

> Source: https://aistudio.google.com/case-studies/compscience/

Jan 7, 2025

# CompScience improves industrial worksite safety with on-demand image and video analysis

CompScience uses Gemini 2.5 Pro and 2.5 Flash to analyze worksite footage and mitigate realtime hazards. Through their Safe Work Plan, Safety Pulse, and Safety Search products, they scale expert knowledge to help workers stay safe on the job.

### MODEL USED

Gemini 2.5 Pro

Gemini 2.5 Flash

### IMPACT

400%

Adoption of Safe Work Plan vs. standard techniques

15K+

Hours of video footage processed

60

Detailed risk reports deployed to industry

CompScience is on a mission to eliminate workplace accidents by using AI to provide Safe Work Plans, real-time alerts, and comprehensive safety reports derived from worksite video footage. Partnering with professional risk experts like the National Safety Council, CompScience serves over 100 industrial customers across a variety of sectors, helping them identify risks before they become injuries. 

The core challenge for CompScience is the sheer volume of data. Industrial worksites generate hundreds of hours of video every day. Manually reviewing this footage for potential hazards is impossible at scale. To turn this massive unstructured dataset into concise, actionable safety information, CompScience turned to the Gemini API. 

## Scaling expert safety knowledge with Gemini 2.5 Pro

CompScience utilizes Gemini 2.5 Pro to build their Safe Work Plan application. When maintenance workers encounter unplanned work in a factory, they can use their cellphones to take photos of the situation. 

![Phone screen allowing users to input job details to conduct a quick Risk Prediction.](https://www.gstatic.com/aistudio/case_studies/compScience/CompScience_inline_01.jpg)

Workers can submit photos from job sites to generate a Safe Work Plan detailing hazards and proposed safeguards.

2.5 Pro processes these images, reasons through complex safety assessment rubrics, and provides expert-informed advice and guidance. These recommendations can then be saved as standard safe company procedures, effectively digitizing and scaling expert safety knowledge. 

## Processing over 15 thousand hours of video with Gemini 2.5 Flash

Beyond static images, CompScience needs to process continuous video streams for their Safety Pulse and Safety Search products. They utilize Gemini 2.5 Flash to periodically assess worksite cameras for immediate issues and to rapidly search through hundreds of hours of archived video in minutes to generate impact reports. 

According to Daniel Walton, Principal Engineer at CompScience, 2.5 Flash’s native video processing capabilities are a key differentiator, noting that “video processing just isn’t available” at the same level with other AI providers they tested. To manage the high throughput of video data, CompScience leverages the Files API, using multiple threads to upload video and generate insights efficiently. 

A recent development for CompScience is utilizing Gemini 2.5 Flash’s ability to generate bounding boxes around identified hazards within continuous video or images. This visual grounding allows them to help identify unsafe behaviors or conditions in their reports, a feature Walton notes is “only possible with Gemini 2.5 Flash” for their specific use case. 

![Two screenshots of the CompScience SafetyPulse interface. The left screen shows a video feed from a construction site with a green bounding box around a crane, alongside an "Alert" log identifying a suspended load hazard. A "Take Action" pop-up menu allows users to select corrective measures. The right screen displays a "Safety Overview" dashboard with camera activity thumbnails, alert summaries, and a generated report listing potential safety hazards and recommendations for improvement.](https://www.gstatic.com/aistudio/case_studies/compScience/CompScience_inline_02.jpg)

Gemini 2.5 Flash processes job site security photos for safety managers to review, then generates actionable daily reports.

## Proactively improving safety and mitigating hazards

By integrating Gemini models, CompScience currently delivers video-driven safety reports to hundreds of customers. The effectiveness of their AI-driven approach has led the National Safety Council to include the CompScience Safe Work Plan system for their own members, scaling these safety benefits to a broader industrial audience. 

### AUTHORS

Dan Walton

Vishal Dharmadhikari

### MODEL USED

Gemini 2.5 Pro

Gemini 2.5 Flash

### IMPACT

400%

Adoption of Safe Work Plan vs. standard techniques

15K+

Hours of video footage processed

60

Detailed risk reports deployed to industry

## More stories

  * ![Case study image](https://www.gstatic.com/aistudio/case_studies/Pascal_AI_thumbnail.jpg)Read casePascal AIGemini 2.5 Pro
  * ![Case study image](https://www.gstatic.com/aistudio/case_studies/ava/Ava_thumbnail.jpg)Read caseAvaGemini 2.5 Flash
  * ![Case study image](https://www.gstatic.com/aistudio/case_studies/Raindrop_thumbnail.jpg)Read caseRaindropGemini 2.5 Flash


