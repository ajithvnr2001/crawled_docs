---
url: https://docs.cloud.google.com/eventarc/docs/event-format/
title: Event format \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:58:48.637601+00:00
---

# Event format  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/event-format/

[ Skip to main content ](https://docs.cloud.google.com/eventarc/docs/event-format/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/eventarc/docs/event-format/)
  * [Deutsch](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=de)
  * [Español](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=es-419)
  * [Français](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=id)
  * [Italiano](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=it)
  * [Português](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=ja)
  * [한국어](https://docs.cloud.google.com/eventarc/docs/event-format/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/eventarc/docs)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Define a message binding (Eventarc Advanced)](https://docs.cloud.google.com/eventarc/docs/event-format/#message-binding)
  * [Format received events (Eventarc Advanced)](https://docs.cloud.google.com/eventarc/docs/event-format/#format-events)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Reference ](https://docs.cloud.google.com/eventarc/docs/apis)


Was this helpful?
Send feedback 
#  Event format Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Define a message binding (Eventarc Advanced)](https://docs.cloud.google.com/eventarc/docs/event-format/#message-binding)
  * [Format received events (Eventarc Advanced)](https://docs.cloud.google.com/eventarc/docs/event-format/#format-events)


[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)
Eventarc delivers events, regardless of provider, to the target destination in a CloudEvents ([cloudevents.io](http://cloudevents.io/)) format in binary content mode.
CloudEvents is the Cloud Native Computing Foundation's [open standard specification](https://github.com/cloudevents/spec) for describing event metadata in a common way. Using a standard way to describe event metadata ensures consistency, accessibility, and portability.
A CloudEvent in binary content mode has its context attributes described as HTTP headers. The names of the HTTP headers are the context attribute names prefixed with `ce-`. The `Content-Type` header reflects the media type in which the event data is encoded.
Target destinations consume events using an [HTTP protocol binding](https://docs.cloud.google.com/eventarc/docs/cloudevents).
For Workflows destinations, the Workflows service converts the event to a [JSON object](https://docs.cloud.google.com/eventarc/docs/cloudevents-json), and passes the event into the workflow execution as a runtime argument.
## Define a message binding (Eventarc Advanced)
You can define a message binding and construct a new HTTP request. For more information, see [Define a message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding).
## Format received events (Eventarc Advanced)
You can configure a pipeline to expect event data in a specific format or, before events are delivered to a destination, you can convert event data from one supported format to another. For example, you might need to route events to an endpoint that only accepts Avro or Protobuf data. The following format conversions are supported:
  * Avro to JSON
  * Avro to Protobuf
  * JSON to Avro
  * JSON to Protobuf
  * Protobuf to Avro
  * Protobuf to JSON


For more information, see [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events). 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
