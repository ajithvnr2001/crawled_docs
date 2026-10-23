---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/
title: Module: google.appengine.tools.queue_xml_parser \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:03:01.856403+00:00
---

# Module: google.appengine.tools.queue_xml_parser  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.tools.queue_xml_parser Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/tools/queue_xml_parser.py) Performs translation of `queue.xml` to `queue.yaml`.

## Classes

[`class Acl`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/Acl) [`class PullQueue`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/PullQueue) [`class PushQueue`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/PushQueue) [`class Queue`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/Queue) [`class QueueXml`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/QueueXml) [`class QueueXmlParser`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/QueueXmlParser): Provides logic for walking down XML tree and pulling data. [`class RetryParameters`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/RetryParameters)

## Functions

[`GetQueueYaml(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/GetQueueYaml) [`main(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/tools/queue_xml_parser/main) | 

## Other Members  
  
---  
  
BAD_MODE_ERROR_MESSAGE |  `('Mode, if specified, must be either push or pull (defaults to push) for queue ' "entries. Bad value '%s' in <queue> entry with name '%s'")`  
PULL_QUEUE_ERROR_MESSAGE |  `('The element <%s> is not defined for pull queues; bad <queue> entry with name ' "'%s'")`  
PUSH_QUEUE_RETRY_PARAMS |  `('task-age-limit', 'min-backoff-seconds', 'max-backoff-seconds', 'max-doublings')`  
PUSH_QUEUE_TAGS |  `('rate', 'bucket-size', 'max-concurrent-requests', 'target')`  
RETRY_PARAMETER_TAGS |  `('task-retry-limit', 'task-age-limit', 'min-backoff-seconds', 'max-backoff-seconds', 'max-doublings')`  
RETRY_PARAM_ERROR_MESSAGE |  `('The element <%s> in <retry-parameters> is not defined for pull queue with ' "name '%s'")`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
