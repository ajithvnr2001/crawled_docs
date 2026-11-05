---
url: https://docs.cloud.google.com/pubsub/docs/publish-hedging/
title: Publish hedging \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:17:21.646713+00:00
---

# Publish hedging  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/publish-hedging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Publish hedging Stay organized with collections  Save and categorize content based on your preferences. 

High tail latency when publishing messages can be caused by transient network delays or temporary server-side slowness. Publish hedging lets a Pub/Sub publisher client send a backup (hedged) publish request in parallel if an in-flight request does not complete within a configured delay, using whichever response returns first.

This document provides information about using publish hedging with messages published to a topic.

## Before you begin

Before configuring the publish workflow, ensure you have completed the following tasks:

  * Learn about [topics and the publishing workflow](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).
  * [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic).



### Required roles

To get the permissions that you need to send hedged publish requests to a topic, ask your administrator to grant you the [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role on the topic. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You need [additional permissions](https://docs.cloud.google.com/pubsub/docs/access-control) to create or update topics and subscriptions.

## About publish hedging

Hedging settings control how and when the Pub/Sub client libraries send hedged publish requests. Publish hedging is disabled by default. When enabled, the client libraries have the following hedging settings:

  * **Hedge delay** : the amount of time that a client library waits before sending an additional publish request in parallel if the previous request has not completed. The default value is 1 second, and the configured value must be between 100 milliseconds and 10 seconds.
  * **Maximum tokens** : the maximum number of tokens that a client library can accumulate for sending hedged publish requests. Each hedged publish request consumes 1 token. The default value is 50, and the configured value must be between 1 and 250.
  * **Refill ratio** : the number of tokens added for each successful publish request. This value controls the maximum fraction of publish requests that can be hedged over time. For example, a refill ratio of 0.1 allows up to 10% of publish requests to be hedged. The default value is 0.1, and the configured value must be between 0.001 and 0.2.



To hedge publish requests, the hedge delay must be shorter than both the initial request timeout and the total timeout in the publisher's [retry settings](https://docs.cloud.google.com/pubsub/docs/retry-requests). If not, the publisher client will fail to initialize. When publish hedging is enabled, the client library sends publish requests as follows:

  * If an in-flight publish request doesn't complete within the hedge delay and at least one token is available, the client library consumes one token and sends an additional publish request for the same batch of messages in parallel while keeping the initial request outstanding.
  * If none of the in-flight requests complete after another hedge delay, the client library continues sending additional hedged requests at intervals of the hedge delay while tokens remain available and the total timeout has not expired.
  * As soon as any in-flight publish request for the batch succeeds, the client library completes the publish operation, cancels any remaining in-flight attempts for that batch, and increases the available tokens by the refill ratio, up to the maximum tokens.



## Hedge a publish request

Unlike [retry requests](https://docs.cloud.google.com/pubsub/docs/retry-requests), which wait for an in-flight publish request to fail or time out, publish hedging keeps the initial request outstanding while sending a concurrent hedged request. This reduces tail latency without prematurely canceling requests that are about to succeed.

Because multiple requests for the same batch of messages can be in flight concurrently, more than one attempt might succeed before the remaining attempts are canceled, as publish request cancellation is best-effort. As a result, you might receive duplicate messages with different message IDs, which can increase client network traffic and Pub/Sub costs for publishing and delivering those duplicates. See ["Troubleshoot duplicate, redelivered, or missing messages"](https://docs.cloud.google.com/pubsub/docs/troubleshooting#troubleshoot-duplicates-redeliveries) for tips on handling duplicate messages.

If a service degradation causes a sustained increase in latency or errors, the maximum tokens and refill ratio settings prevent hedged publish rates from becoming too high. Because tokens are only added when publish requests succeed, sustained slowness or errors quickly deplete the available tokens and automatically throttle hedged requests.

This sample code demonstrates creating a publisher with custom hedging settings. Not all client libraries support publish hedging; see the [API Reference documentation](https://docs.cloud.google.com/pubsub/docs/reference/libraries#additional_resources) for your chosen language.

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.pubsub.v1.[HedgingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.HedgingSettings.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.time.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    
    public class PublishWithHedgingSettingsExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
    
        publishWithHedgingSettingsExample(projectId, topicId);
      }
    
      public static void publishWithHedgingSettingsExample(String projectId, String topicId)
          throws IOException, ExecutionException, InterruptedException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null;
    
        try {
          // Hedging settings configures how and when the publisher sends multiple concurrent publish
          // requests to reduce tail latency.
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) hedgeDelay = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).ofMillis(500); // default: 1000 ms (1 second)
          int maxTokens = 100; // default: 50
          float refillRatio = 0.05f; // default: 0.1
    
          [HedgingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.HedgingSettings.html) hedgingSettings =
              [HedgingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.HedgingSettings.html).newBuilder()
                  .[setHedgeDelay](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.HedgingSettings.Builder.html#com_google_cloud_pubsub_v1_HedgingSettings_Builder_setHedgeDelay_java_time_Duration_)(hedgeDelay)
                  .[setMaxTokens](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.HedgingSettings.Builder.html#com_google_cloud_pubsub_v1_HedgingSettings_Builder_setMaxTokens_int_)(maxTokens)
                  .[setRefillRatio](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.HedgingSettings.Builder.html#com_google_cloud_pubsub_v1_HedgingSettings_Builder_setRefillRatio_float_)(refillRatio)
                  .build();
    
          // Create a publisher instance with hedging settings bound to the topic
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName).[setHedgingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.Builder.html#com_google_cloud_pubsub_v1_Publisher_Builder_setHedgingSettings_com_google_cloud_pubsub_v1_HedgingSettings_)(hedgingSettings).build();
    
          String message = "Hello world!";
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(data).build();
    
          // Once published, returns a server-assigned message id (unique within the topic)
          ApiFuture<String> messageIdFuture = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(pubsubMessage);
          String messageId = messageIdFuture.get();
          System.out.println("Published a message with hedging settings: " + messageId);
    
        } finally {
          if (publisher != null) {
            // When finished with the publisher, shutdown to free up resources.
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
        }
      }
    }

## Publish hedging with ordering keys

Publish hedging cannot be used with [message ordering](https://docs.cloud.google.com/pubsub/docs/ordering). Because publish hedging sends concurrent publish requests for the same batch of messages, the Pub/Sub service might receive and process those requests out of order. If you enable both message ordering and publish hedging on a publisher client, creating the publisher fails with an error.

## Tips and best practices

Consider the following best practices when configuring publish hedging:

  * **Use hedging for transient tail latency** : Publish hedging is designed to smooth out short-lived latency spikes caused by temporary network delays or brief server-side slowness. Don't rely on hedging to mitigate sustained outages or persistent errors.
  * **Hedging with retry policies** : Set a larger initial request timeout in your [retry settings](https://docs.cloud.google.com/pubsub/docs/retry-requests) alongside a shorter hedge delay. Short, aggressive timeouts cancel requests prematurely and trigger full retries, discarding work already underway on the server. A larger timeout allows the original request to complete if it is only slightly delayed.
  * **Client-side flow control and hedging** : Publish hedging does not resolve client-side delays, such as CPU contention or thread starvation. If high publish latency is caused by messages queuing in client memory, using [flow control](https://docs.cloud.google.com/pubsub/docs/flow-control-messages) to manage queue sizes may help, though host resource constraints should be addressed as well.
  * **Monitor publish latency and throughput metrics** : Use Monitoring metric graphs such as [`topic/send_request_latencies`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/send_request_latencies) to identify tail latency spikes and determine whether hedging may help. High rates of `CANCELLED` errors might indicate that your request deadlines are configured too low. When tuned effectively, publish hedging keeps message throughput and [topic byte cost](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/byte_cost) approximately constant even during publish tail latency.



## What's next

To learn how to configure advanced publishing options, see the following:

  * [Retry requests](https://docs.cloud.google.com/pubsub/docs/retry-requests)

  * [Compress messages](https://docs.cloud.google.com/pubsub/docs/compress-messages)

  * [Flow control](https://docs.cloud.google.com/pubsub/docs/flow-control-messages)

  * [Concurrency control](https://docs.cloud.google.com/pubsub/docs/concurrency-control-messages)

  * [Batch messaging](https://docs.cloud.google.com/pubsub/docs/batch-messaging)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
