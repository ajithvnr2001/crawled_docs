---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-log-stackdriver/
title: Process Cloud Audit Logs with Cloud Functions \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:24:54.672189+00:00
---

# Process Cloud Audit Logs with Cloud Functions  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-log-stackdriver/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Process Cloud Audit Logs with Cloud Functions Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to process Cloud Audit Logs using Cloud Functions. It extracts and prints the method name, resource name, and initiator email from each log entry.

## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package log contains examples for handling Cloud Functions logs.
    package log
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    )
    
    func init() {
    	functions.CloudEvent("ProcessLogEntry", ProcessLogEntry)
    }
    
    // MessagePublishedData contains the full Pub/Sub message
    // See the documentation for more details:
    // https://cloud.google.com/eventarc/docs/cloudevents#pubsub
    type MessagePublishedData struct {
    	Message PubSubMessage
    }
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Data []byte `json:"data"`
    }
    
    // ProcessLogEntry processes a Pub/Sub message from Cloud Logging.
    func ProcessLogEntry(ctx context.Context, e event.Event) error {
    	var msg MessagePublishedData
    	if err := e.DataAs(&msg); err != nil {
    		return fmt.Errorf("event.DataAs: %w", err)
    	}
    
    	log.Printf("Log entry data: %s", string(msg.Message.Data)) // Automatically decoded from base64.
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonElement;
    import com.google.gson.JsonObject;
    import functions.eventpojos.PubSubBody;
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Logger;
    
    public class StackdriverLogging implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(StackdriverLogging.class.getName());
      // Use Gson (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(CloudEvent event) throws Exception {
        if (event.getData() == null) {
          logger.info("Hello, World!");
          return;
        }
    
        // Extract Cloud Event data and convert to PubSubBody
        String cloudEventData = new String(event.getData().toBytes(), StandardCharsets.UTF_8);
        PubSubBody body = gson.fromJson(cloudEventData, PubSubBody.class);
    
        String encodedData = body.getMessage().getData();
        String decodedData = new String(Base64
            .getDecoder().decode(encodedData), StandardCharsets.UTF_8);
    
        // Retrieve and decode PubSubMessage data into a JsonElement.
        // Function is expecting a user-supplied JSON message which contains what
        // name to log.
        JsonElement jsonPubSubMessageElement = gson.fromJson(decodedData, JsonElement.class);
    
        // Extract name if present or default to World
        String name = "World";
        if (jsonPubSubMessageElement != null && jsonPubSubMessageElement.isJsonObject()) {
          JsonObject jsonPubSubMessageObject = jsonPubSubMessageElement.getAsJsonObject();
    
          if (jsonPubSubMessageObject.has("name")
              && jsonPubSubMessageObject.get("name").isJsonPrimitive()
              && jsonPubSubMessageObject.get("name").getAsJsonPrimitive().isString()) {
            name = jsonPubSubMessageObject.get("name").getAsString();
          }
        }
    
        String res = String.format("Hello, %s!", name);
        logger.info(res);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.cloudEvent('processLogEntry', async event => {
      const dataBuffer = Buffer.from(event.data.message.data, 'base64');
    
      const logEntry = JSON.parse(dataBuffer.toString()).protoPayload;
      console.log(`Method: ${logEntry.methodName}`);
      console.log(`Resource: ${logEntry.resourceName}`);
      console.log(`Initiator: ${logEntry.authenticationInfo.principalEmail}`);
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import json
    
    import functions_framework
    
    
    @functions_framework.cloud_event
    def process_log_entry(event):
        data_buffer = base64.b64decode(event.data["message"]["data"])
        log_entry = json.loads(data_buffer)["protoPayload"]
    
        print(f"Method: {log_entry['methodName']}")
        print(f"Resource: {log_entry['resourceName']}")
        print(f"Initiator: {log_entry['authenticationInfo']['principalEmail']}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
