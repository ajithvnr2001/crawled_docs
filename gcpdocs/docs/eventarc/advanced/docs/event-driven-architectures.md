---
url: https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/
title: Event-driven architectures \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:54:18.868527+00:00
---

# Event-driven architectures  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/

[ Skip to main content ](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/)
  * [Deutsch](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=de)
  * [Español](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=es-419)
  * [Français](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=id)
  * [Italiano](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=it)
  * [Português](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=ja)
  * [한국어](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Architecture overview](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#architecture_overview)
    * [Core components](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#core_components)
  * [When to use event-driven architectures](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#when_to_use_event-driven_architectures)
  * [Benefits of event-driven architectures](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#benefits_of_event-driven_architectures)
    * [Loose coupling and improved developer agility](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#loose_coupling_and_improved_developer_agility)
    * [Asynchronous eventing and resiliency](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#asynchronous_eventing_and_resiliency)
    * [Push-based messaging, real-time event streams, and lower costs](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#push-based_messaging_real-time_event_streams_and_lower_costs)
    * [Simplified auditing and event sourcing](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#simplified_auditing_and_event_sourcing)
  * [Architectural considerations](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#architectural_considerations)
  * [What's next](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)


Send feedback 
#  Event-driven architectures Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Architecture overview](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#architecture_overview)
    * [Core components](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#core_components)
  * [When to use event-driven architectures](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#when_to_use_event-driven_architectures)
  * [Benefits of event-driven architectures](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#benefits_of_event-driven_architectures)
    * [Loose coupling and improved developer agility](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#loose_coupling_and_improved_developer_agility)
    * [Asynchronous eventing and resiliency](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#asynchronous_eventing_and_resiliency)
    * [Push-based messaging, real-time event streams, and lower costs](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#push-based_messaging_real-time_event_streams_and_lower_costs)
    * [Simplified auditing and event sourcing](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#simplified_auditing_and_event_sourcing)
  * [Architectural considerations](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#architectural_considerations)
  * [What's next](https://docs.cloud.google.com/eventarc/advanced/docs/event-driven-architectures/#whats_next)


[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)
Decoupling microservices through asynchronous event routing lets you build distributed systems that react to state changes independently. Instead of relying on direct service-to-service calls, **event producers** publish immutable notifications, while an **event router** (or broker) filters and fans out messages to downstream **event consumers** (or sinks). This separation helps you deploy, scale, and update components in isolation without breaking dependent services.
You can manage event delivery by defining _enrollments_ when using [Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/overview) or by defining _triggers_ when using [Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs/overview).
## Architecture overview
An _event-driven architecture_ is a software design pattern in which microservices react to changes in state, called _events_. Events can either carry a state (such as the price of an item or a delivery address) or events can be identifiers (a notification that an order was received or shipped, for example). The events trigger microservices that work together to achieve a common goal, but don't have to know anything about each other except the event format. Although operating together, each microservice can apply a different business logic, and emit its own output events.
An event has the following characteristics:
  * It is a record of something that has happened.
  * It captures an immutable fact that cannot be changed or deleted.
  * It occurs whether or not a service applies any logic upon consuming it.
  * It can be persisted indefinitely, at a large scale, and consumed as many times as necessary.


### Core components
In an event-driven system, three components—event producers, event router, event consumers—are decoupled and can be independently deployed, updated, and scaled:
![Event brokers and subscribers](https://docs.cloud.google.com/static/eventarc/images/broker-subscriber.svg)
The event router links the different services and is the medium through which messages are sent and received. It executes a response to the original event generated by an event producer and sends this response downstream to the appropriate consumers. Events are handled asynchronously and their outcomes are decided when a service reacts to an event or is impacted by it, as in the following diagram of a very simplified event flow: 
![Event-driven architecture](https://docs.cloud.google.com/static/eventarc/images/event-driven-architecture.svg)
## When to use event-driven architectures
Consider the following usages when designing your system.
  * **To monitor and receive alerts** for any anomalies or changes to storage buckets, database tables, virtual machines, or other resources.
  * **To fan out a single event** to multiple consumers. The event router will push the event to all the appropriate consumers, without you having to write customized code. Each service can then process the event in parallel, yet differently.
  * **To provide interoperability between different technology stacks** while maintaining the independence of each stack.
  * **To coordinate systems and teams** operating in and deploying across different regions and accounts. You can reorganize the ownership of microservices. There are fewer cross-team dependencies and you can react more quickly to changes that would otherwise be impeded by barriers to data access.


## Benefits of event-driven architectures
These are some of the advantages when building an event-driven architecture.
### Loose coupling and improved developer agility
Event producers are logically separated from event consumers. This decoupling between the production and consumption of events means that services are interoperable but can be scaled, updated, and deployed independently of each other.
Loose coupling reduces dependencies and lets you implement services in different languages and frameworks. You can add or remove event producers and receivers without having to change the logic in any one service. You don't need to write custom code to poll, filter, and route events.
### Asynchronous eventing and resiliency
In an event-driven system, events are generated asynchronously, and can be issued as they happen without waiting for a response. Loosely coupled components means that if one service fails, the others are unaffected. If necessary, you can log events so that the receiving service can resume from the point of failure, or replay past events.
### Push-based messaging, real-time event streams, and lower costs
Event-driven systems allow for push-based messaging and clients can receive updates without needing to continuously poll remote services for state changes. These pushed messages can be used for on-the-fly data processing and transformation, and real-time analysis. Moreover, with less polling, there is a reduction in network I/O, and decreased costs.
### Simplified auditing and event sourcing
The centralized location of the event router simplifies auditing, and lets you control who can interact with a router, and which users and resources have access to your data. You can also encrypt your data both in transit and at rest.
Additionally, you can make use of event sourcing, an architectural pattern that records all changes made to an application's state, in the same sequence that they were originally applied. Event sourcing provides a log of immutable events which can be kept for auditing purposes, to recreate historic states, or as a canonical narrative to explain a business-driven decision.
## Architectural considerations
An event-driven architecture might require that you approach your application design in a new way. Although well suited for applications that make use of microservices or decoupled components, you should also consider the following:
  * _Can your event source guarantee delivery if you need to process every single event?_
It should be a durable and reliable event source.
  * _Can your application handle multiple asynchronous requests?_
Your system performance shouldn't rely on global scope or inelastic databases.
  * _How do you want to track your event flow?_
An event-driven architecture supports dynamic tracking using monitoring services, but not static tracking using code analysis.
  * _Do you want to use the data in your event source to rebuild state?_
You should consider how to ensure that your data is deduplicated and ordered.


## What's next
  * To understand how Eventarc Advanced handles events, see the [Eventarc Advanced overview](https://docs.cloud.google.com/eventarc/advanced/docs/overview).
  * To understand how Eventarc Standard handles events, see the [Eventarc Standard overview](https://docs.cloud.google.com/eventarc/standard/docs/overview).


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
