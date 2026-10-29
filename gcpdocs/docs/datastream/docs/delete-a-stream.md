---
url: https://docs.cloud.google.com/datastream/docs/delete-a-stream/
title: Delete a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T11:06:05.084328+00:00
---

# Delete a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/delete-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Delete a stream Stay organized with collections  Save and categorize content based on your preferences. 

Deleting a stream that you no longer need in Datastream frees up your project quota and prevents further charges.

To ensure that all in-flight data transfers cleanly from your source to the destination, [pause the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#pause-a-stream) first. Wait for Datastream to confirm the paused status before you delete it.

## Delete a stream

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that you want to delete. 

  3. As a best practice, in the **Stream status** pane of the **Stream details** page, verify that the status of the stream isn't `Running`. If it is, then [pause the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#pause-a-stream).

  4. Click **DELETE**.

  5. In the dialog, enter `Delete` in the text field, and then click **DELETE**.




## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to modify a stream, see [Modify a stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream).
  * To learn how to recover a failed stream, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
