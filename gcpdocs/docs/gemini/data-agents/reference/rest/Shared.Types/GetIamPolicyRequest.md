---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/GetIamPolicyRequest/
title: GetIamPolicyRequest \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:27:35.277418+00:00
---

# GetIamPolicyRequest  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/GetIamPolicyRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  GetIamPolicyRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * GetPolicyOptions
    * JSON representation



Request message for `GetIamPolicy` method.

JSON representation  
---  
      
    
    {
      "resource": string,
      "options": {
        object ([GetPolicyOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions))
      }
    }  
  
Fields  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being requested. The only format that is supported is `projects/<>/locations/<>/dataAgents/<>`  
`options` |  `object (`[GetPolicyOptions](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions)`)` OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`.  
  
## GetPolicyOptions

Encapsulates settings provided to GetIamPolicy.

JSON representation  
---  
      
    
    {
      "requestedPolicyVersion": integer
    }  
  
Fields  
---  
`requestedPolicyVersion` |  `integer` Optional. The maximum policy version that will be used to format the policy.Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset.The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1.To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
