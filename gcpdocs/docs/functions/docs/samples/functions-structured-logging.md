---
url: https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/
title: Write structured Logging in Cloud Functions \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:53:59.516014+00:00
---

# Write structured Logging in Cloud Functions  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/

[ Skip to main content ](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/)
  * [Deutsch](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=de)
  * [Español](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=es-419)
  * [Français](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=id)
  * [Italiano](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=it)
  * [Português](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=ja)
  * [한국어](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffunctions%2Fdocs%2Fsamples%2Ffunctions-structured-logging%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/run-color.svg) ](https://docs.cloud.google.com/functions/docs)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Code sample](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/#code-sample)
  * [What's next](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/#whats-next)


If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)


Was this helpful?
#  Write structured Logging in Cloud Functions Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Code sample](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/#code-sample)
  * [What's next](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/#whats-next)


This sample demonstrates how to write structured logs in Cloud Functions using the Google Cloud logging client. Structured logs provide a more detailed and organized way to record information about your application, making it easier to troubleshoot and analyze issues.
## Code sample
[Node.js](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/#node.js)[Python](https://docs.cloud.google.com/functions/docs/samples/functions-structured-logging/#python) More
To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
const {Logging} = require('@google-cloud/logging[](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/overview.html)');
const functions = require('@google-cloud/functions-framework');
const pkg = require('./package.json');

functions.http('structuredLogging', async (req, res) => {
  // Initialize the logging client
  const logging = new [Logging](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/logging/logging.html)();
  // Required to capture your project id
  await logging.[setProjectId](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/logging/logging.html)();
  // Create a LogSync transport, defaulting to process.stdout
  const log = logging.[logSync](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest/logging/logging.html)(pkg.name);
  const text = 'Hello, world!';
  // Create a structured log entry with severity,
  // additional component fields, and HTTP request.
  // Appending the httpRequest enables log correlation.
  const metadata = {
    severity: 'NOTICE',
    component: 'arbitrary-property',
    httpRequest: req,
  };
  // Prepares a log entry
  const entry = log.entry(metadata, text);
  log.write(entry);
  res.status(200).send('Success: A log message was written');
});
```

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
import logging

import functions_framework
from google.cloud.logging import [Client](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html)


@functions_framework.http
def structured_logging(request):
    # Initialize the Google Cloud logging client
    cloud_logging_client = Client()
    # Set up a Log Handler that exports logs in JSON format to stdout
    # when running in a serverless environment.
    # To manually set up a Structured Log Handler, see
    # https://googleapis.dev/python/logging/latest/handlers-structured-log.html
    cloud_logging_client.[setup_logging](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_setup_logging)()

    # Construct log message and additional metadata
    # https://cloud.google.com/run/docs/logging#using-json
    msg = "Hello, world!"
    metadata = {"component": "arbitrary-property"}

    # Write structured log with additional component fields
    # HTTP request data is attached automatically for request-log correlation
    logging.info(msg, extra={"json_fields": metadata})

    return "Success: A log message was written"


```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
