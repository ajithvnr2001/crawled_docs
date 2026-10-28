---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/generate-agent/
title: Create agents with Arc \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:35:05.634787+00:00
---

# Create agents with Arc  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/generate-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Create agents with Arc Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

As an alternative to defining instructions manually for agents, you can use [Arc](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc). This is a quick way to use AI to generate an agent application for you.

With this approach you provide:

  * A clear prompt describing what you want your agent application to do.
  * Optional knowledge documents that provide technical details for the agent application, which can include technical details for external services to utilize.



## Steps to generate agents

To generate agents:

  1. Using the agent builder, create an agent application.
  2. Click the **Start with AI** button in the root agent or click the **Arc** button at the top of the builder.
  3. Provide a clear goal for your agent application.
  4. Optionally add knowledge documents using the **Upload** button. These documents help teach your agent how to handle a variety of scenarios. You can upload files like tool catalog, requirements, transcripts, external services, and FAQs. These files can be used to provide specifications for tools and back end integrations (PRD, PDF, Markdown, OpenAPI). You do not need to attach any files; a clear natural language prompt works well on its own in many cases.
  5. Submit your prompt and upload files. Arc will start streaming its chain of thought. Once complete, agents are created with instructions, tools, and callbacks as necessary.



Example prompt for customer support and flight rebooking:
    
    
    Create a customer service agent for an airline that can check flight status,
    assist passengers with rebooking flights, and answer questions about baggage
    policies.
    

Example prompt for customer order status (uploaded files: `return_policy.md`, `orders_api.json`):
    
    
    Create an e-commerce assistant based on the attached return policy
    and OpenAPI catalog. The agent should answer customer shipping FAQs,
    check order delivery status using the orders tool, and route return
    requests to a live agent if the item was purchased more than 30 days ago.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
