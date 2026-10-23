---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/QueueXmlParser/
title: google.appengine.tools.queue_xml_parser.QueueXmlParser \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:17:43.955860+00:00
---

# google.appengine.tools.queue_xml_parser.QueueXmlParser  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/QueueXmlParser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.tools.queue_xml_parser.QueueXmlParser Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/tools/queue_xml_parser.py#L61-L201) Provides logic for walking down XML tree and pulling data. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

## Methods

### `ProcessQueueNode`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/tools/queue_xml_parser.py#L98-L147)
    
    
    ProcessQueueNode(
        node
    )
    

Processes XML `<queue>` nodes into Queue objects. The following information is parsed out:

  * name
  * mode: can be either push or pull
  * retry-parameters: task-retry-limit



#### For push queues only:

  * task-age-limit
  * min-backoff-seconds
  * max-back-off-seconds
  * max-doubling
  * bucket-size
  * max-concurrent-requests
  * rate: how often tasks are processed on this queue.
  * target: version of application on which tasks on this queue will be invoked.



#### For pull queues only:

  * acl: access control list - lists user and writer email addresses.

| Args  
---  
  
`node` |  Current `<queue>` XML node being processed.   
  
### `ProcessXml`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/tools/queue_xml_parser.py#L64-L96)
    
    
    ProcessXml(
        xml_str
    )
    

Parses XML string and returns object representation of relevant info.

Args  
---  
  
`xml_str` |  The XML string.   
  
Returns  
---  
A `QueueXml` object containing information about task queue specifications from the XML.   
  
Raises  
---  
  
`AppEngineConfigException` |  In case of malformed XML or illegal inputs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
