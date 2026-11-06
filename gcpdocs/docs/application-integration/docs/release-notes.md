---
url: https://docs.cloud.google.com/application-integration/docs/release-notes/
title: Application Integration release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:52:29.307772+00:00
---

# Application Integration release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Resources ](https://docs.cloud.google.com/application-integration/docs/release-notes)



Send feedback 

#  Application Integration release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Application Integration. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/application-integration-release-notes.xml) directly. 

## October 28, 2026

Security

A Deserialization of Untrusted Data vulnerability was discovered in the `SubWorkflow` task in Application Integration versions prior to September 11, 2026. For more information, see the [GCP-2026-074](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-074) security bulletin.

Feature

**Application Integration agent skills**

Application Integration agent skills are available in the public [`google/skills`](https://github.com/google/skills) repository: `application-integration-basics`, `application-integration-authoring`, and `application-integration-troubleshooting`. AI coding agents that use these skills can help you set up Application Integration; build, publish, and run integrations through the REST API; and troubleshoot failed runs. For more information, see [Application Integration agent skills](https://docs.cloud.google.com/application-integration/docs/agent-skills-overview) and [Build an integration with an AI agent](https://docs.cloud.google.com/application-integration/docs/build-integration-ai-agent).

## October 14, 2026

Security

An Incorrect Authorization vulnerability in the `AuthConfig` validation and integration execution runtime in Application Integration versions prior to August 27, 2026. For more information, see the [GCP-2026-068](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-068) security bulletin.

## October 12, 2026

Announcement

Starting October 15, 2026, Application Integration enforces security fixes for IAM, run-as service accounts, and `iam.serviceAccounts.actAs` checks, requiring the correct permissions for the test feature and any new integrations. For more information, see the [GCP-2026-068](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-068) security bulletin and [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes).

## September 28, 2026

Security

A Confused Deputy vulnerability was discovered in the Email Task component in Application Integration versions prior to June 30, 2026. For more information, see the [GCP-2026-066](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-066) security bulletin.

Security

A Deserialization of Untrusted Data vulnerability was discovered in the JavaScript Task in Application Integration versions prior to June 28, 2026. For more information, see the [GCP-2026-065](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-065) security bulletin.

Security

An Incorrect Authorization vulnerability was discovered in the task configuration in Application Integration versions prior to June 17, 2026. For more information, see the [GCP-2026-064](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-064) security bulletin.

## August 28, 2026

Announcement

**Upcoming authorization changes for integration runs**

Application Integration is updating how identities are handled for integration runs. Every run will act as either the person who triggered it or a run-as service account that you configure, and running an integration will require permission to act as that service account. Integrations that run without a person, such as those started by a schedule or an event, will need an explicitly configured run-as service account.

Action might be required before the change takes effect. For guidance on identifying affected integrations and updating them, see [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes).

## February 02, 2026

Feature

**FIFO message processing with Pub/Sub ordering keys**

Application Integration now supports publishing messages to Google Cloud Pub/Sub topics using ordering keys, enabling First-In, First-Out (FIFO) message processing. By setting an ordering key in the Pub/Sub trigger's `Publish Message` action, you can ensure messages are received in the correct order, enhancing reliability for integrations requiring ordered message processing. For more information on how to use ordering keys to publish messages, see [Using ordering keys](https://cloud.google.com/pubsub/docs/publisher#using-ordering-keys).

## May 05, 2025

Change

**Cloud Function Task adds support for Cloud Functions v2 API**

The Cloud Function task in Application Integration now lets you create, link, and run the latest generation of serverless functions, called Cloud Run functions, using the Cloud Functions v2 API.

For more information, see [Cloud Function Task](https://cloud.google.com/application-integration/docs/configure-cloud-function-task).

Change

**Control HTTP call access by region in Application Integration**

Application Integration now offers a new control within the **Regions** page to enable or disable HTTP calls for integrations on a per-region basis. 

For more information, see [Manage regions](https://cloud.google.com/application-integration/docs/enable-new-region).

## April 21, 2025

Change

**New Canvas View is enabled by default in the Integration Editor**

The new Canvas View is now enabled by default in the integration editor. This change is a default setting and no manual enablement is required. You can switch to the old canvas view by disabling the **New canvas view** toggle.

For more information, see [Use the new canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view).

## April 02, 2025

Feature

**Build Conversational Agents with Dialogflow CX** ([Preview](https://cloud.google.com/products#product-launch-stages))

Application Integration now simplifies the creation of conversational experiences with direct integration with Conversational Agents (Dialogflow CX). Using API triggers, you can now build intelligent chatbots and automated tools directly within your integration workflows, enhancing user interactions and automating tasks.

For more information, see [Build conversational agents with Application Integration](https://docs.cloud.google.com/application-integration/docs/conversational-agents).

Change

**Enhancements to Replay Execution**

Application Integration Replay Execution now provides the following enhancements:

  * **Modify input parameters on replay:** You can now modify the input parameters of an integration execution when initiating a replay. This provides greater flexibility in fixing failed executions.
  * **Continue execution from point of failure:** When replaying an integration, you can now choose to continue the execution from the point of the last failure. This will retry the failed task and, upon success, continue the execution from that point, saving time and effort.



For more information, see [Introduction to replay executions](https://docs.cloud.google.com/application-integration/docs/replay-executions).

## September 25, 2024

Feature

**View logs in Cloud Logging**

Viewing integration execution logs in Cloud Logging is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [View logs in Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging)

## September 24, 2024

Feature

The [Resolve JSON Path ](https://docs.cloud.google.com/application-integration/docs/reference/data-transformer-reference/json-functions-reference#resolve-json-path) data transformer function is now available. This function resolves a JSON path on a given JSON object by using the `JSONPath` reference.

## September 12, 2024

Feature

The [XSLT Transform](https://docs.cloud.google.com/application-integration/docs/reference/data-transformer-reference/xml-functions-reference#xslt-transform) data transformer function is now available. This function transforms the specified XML string using the specified XSL string.

## August 22, 2024

Feature

**New canvas view**

In the integration editor layout, you can try the [new canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view) to create integration flows. This feature is in [preview](https://cloud.google.com/products#product-launch-stages). The canvas view offers the following benefits:

  * Improved responsiveness of the canvas interaction
  * Clearer view of your integration
  * Minimap view
  * Easier to build integrations



## August 18, 2024

Feature

In the Application Integration editor, you can now search, browse, and select tasks and connectors in the **[Tasks](https://docs.cloud.google.com/application-integration/docs/tasks)** list. For more information, see [Add a Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task).

## July 22, 2024

Feature

The [Solace trigger](https://docs.cloud.google.com/application-integration/docs/configure-solace-trigger) is now available in [preview](https://cloud.google.com/products#product-launch-stages).

## July 15, 2024

Feature

You can now share custom connectors between different Google Cloud projects by [exporting and importing the connector specification](https://docs.cloud.google.com/application-integration/docs/manage-custom-connector-versions#export-import). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## July 11, 2024

Feature

The following [Connector Event triggers](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) are [generally available](https://cloud.google.com/products#product-launch-stages):

  * [SAP ERP trigger](https://docs.cloud.google.com/application-integration/docs/configure-sap-erp-trigger)
  * [SAP Gateway trigger](https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger)



## May 26, 2024

Feature

The [TIBCO EMS trigger](https://docs.cloud.google.com/application-integration/docs/configure-tibcoems-trigger) is now available in [preview](https://cloud.google.com/products#product-launch-stages).

## May 21, 2024

Announcement

Application Integration is now available in Milan (`europe-west8`). For a list of supported regions, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).

## May 20, 2024

Feature

**Terraform support**

You can now use Terraform to [provision new regions](https://docs.cloud.google.com/application-integration/docs/enable-new-region#provision-new-region) and [create authentication profiles](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#createAuthProfile). For a detailed reference document about terraform resources, see [`google_integrations_client`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integrations_client) and [`google_integrations_auth_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integrations_auth_config).

## May 03, 2024

Issue

**Loop Metadata variables are changing**

In the [For each loop](https://cloud.google.com/application-integration/docs/configure-for-each-loop-task) and [While loop](https://cloud.google.com/application-integration/docs/configure-while-loop-task) tasks, there's a `Loop metadata` variable in which you will find duplicate keys for the output variable–for example, `Current Iteration Count` and `current_iteration_count`. We recommend you to use the variables that contain the underscore (`_`) symbol because the other keys are being deprecated. 

For more information, see [Known issue: Duplicate keys in the Loop metadata](https://docs.cloud.google.com/application-integration/docs/known-issue#duplicate_keys_in_the_loop_metadata).

## April 29, 2024

Feature

With Gemini, you can now [build integrations in Application Integration](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini):

  * [Create and build integrations](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#create-and-build-integrations)
  * [Configure connector tasks in an integration](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#configure-connector-tasks)
  * [Add edge conditions and append additional tasks to an integration](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#append)
  * [Generate integration description](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#generate-integration-description)



This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## April 28, 2024

Feature

While configuring a [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger#configure-a-cloud-pubsub-trigger), you can now add a config variable for your service account. [Config variables](https://docs.cloud.google.com/application-integration/docs/variables#config_var) let you externalize configuration for integrations.

## April 24, 2024

Change

For [Cloud Pub/Sub triggers](https://cloud.google.com/application-integration/docs/configure-pubsub-trigger), the default value of the [expiration period option](https://cloud.google.com/pubsub/docs/subscription-properties#expiration_period) for subscriptions is changed from `31 days` to `never expire`. If you want to change the value of the expiration period, then you must update the Cloud Pub/Sub subscription in the Google Cloud console.

## April 21, 2024

Feature

[Apache Kafka trigger](https://docs.cloud.google.com/application-integration/docs/configure-apache-kafka-trigger) is now in [preview](https://cloud.google.com/products#product-launch-stages).

## March 06, 2024

Feature

Application Integration now supports [config variables](https://docs.cloud.google.com/application-integration/docs/variables#config_var). Config variables let you to [build CICD for your integration](https://docs.cloud.google.com/application-integration/docs/build-cicd). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## February 23, 2024

Feature

Application Integration now supports [private triggers](https://docs.cloud.google.com/application-integration/docs/configure-private-trigger) that enable you to break large flows into various subflows. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## February 19, 2024

Feature

**Data masking in logs**

You can now prevent sensitive data from appearing the integration execution logs. For more information, see [Mask sensitive data in logs](https://docs.cloud.google.com/application-integration/docs/mask-sensitive-data-logs).

## February 12, 2024

Feature

You can now also view the integration execution logs in Cloud Logging. For more information, see [View logs in Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging).

## January 24, 2024

Feature

**Custom connectors [Preview]**

Application Integration now supports custom connectors. The custom connectors feature (based on the Open API specification) lets you create your own connectors that aren't a part of the standard connectors provided by Integration Connectors. You can use these connectors in your integrations. For more information, see [Custom connectors](https://docs.cloud.google.com/integration-connectors/docs/custom-connectors).

## January 23, 2024

Feature

The following new [data transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) are available:

  * [`getIntegrationVersionId ()`](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#integration-version-id): Get the integration version ID of the current integration.

  * [`getIntegrationVersionNumber()`](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#integration-version-number): Get the version number of the current integration.




## January 16, 2024

Feature

[Webhook triggers](https://docs.cloud.google.com/application-integration/docs/configure-webhook-trigger) are now supported in [preview](https://cloud.google.com/products#product-launch-stages). With webhook triggers, you can build integrations for your data sources that don't have specific triggers but support webhook for event listening.

## December 13, 2023

Announcement

Application Integration is now available in the following regions:

  * `asia-east2` (Taiwan)
  * `asia-northeast2` (Osaka)
  * `asia-northeast3` (Seoul)
  * `asia-south2` (Delhi)
  * `asia-southeast2` (Jakarta)
  * `europe-central2` (Warsaw)
  * `europe-west10` (Berlin)
  * `europe-west12` (Turin)
  * `northamerica-northeast2` (Toronto)
  * `southamerica-west1` (Santiago)
  * `us-east5` (Columbus)
  * `us-west3` (Salt Lake City)
  * `us-west4` (Las Vegas)
  * `us-south1` (Dallas)



For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/application-integration/docs/locations).

## December 01, 2023

Feature

**Cloud Pub/Sub trigger supports cross-project topics**

You can now configure your [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger) for a Pub/Sub topic that isn't in the same Google Cloud project as your integration. The Pub/Sub topic can be in any Google Cloud project.

Starting with this release, you must specify a service account when configuring the Cloud Pub/Sub trigger. Your existing Cloud Pub/Sub triggers, that don't have any service account associated with them, will continue to work as before. However, if you want to modify the Pub/Sub topic in any of the existing Cloud Pub/Sub triggers, you must also configure a service account for those triggers to continue using them.

## November 29, 2023

Change

The **Database persistence** feature is now renamed to **Local logging** , which also supports logging in **ASYNC** mode. For more information, see [Local logging](https://docs.cloud.google.com/application-integration/docs/local-logging).

Announcement

Application Integration is now available in the Dammam (`me-central2`) region. For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/application-integration/docs/locations).

## November 23, 2023

Feature

[HubSpot trigger](https://docs.cloud.google.com/application-integration/docs/configure-hubspot-trigger) is now available in [preview](https://cloud.google.com/products#product-launch-stages).

## November 21, 2023

Feature

The following [Connector Event triggers](https://docs.cloud.google.com/application-integration/docs/triggers#connector-event-triggers-preview) are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [IBM MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-ibmmq-trigger)
  * [Rabbit MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-rabbitmq-trigger)



## October 19, 2023

Announcement

The maximum memory available for script evaluation in the [Data Transformer Script task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task) is 300 MB. For the list of all the applicable limits, see [Quotas and Limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## October 10, 2023

Feature

The following new [data transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) are available:

  * [Manifest XML](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#manifest-xml) \- Converts the specified input JSON object into an XML string.

  * [Parse XML](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#parse-xml) \- Parses the specified input XML string into a JSON object.




Feature

**IAM Conditions for fine-grained access**

[IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) lets you define and enforce conditional, attribute-based access control for Google Cloud resources, including Application Integration resources. For more information, see [Add IAM conditions](https://docs.cloud.google.com/application-integration/docs/add-iam-conditions).

Feature

You can now view the detailed summary of an integration from the Integration designer. For more information, see [View integration details](https://docs.cloud.google.com/application-integration/docs/view-integration-details).

Change

**Support for user-defined service account**

You can now configure a service account of your choice for an integration. The option to select a service account is displayed to you during the integration creation step.

## September 22, 2023

Feature

**Vertex AI - Predict task**

Starting with this release, Application Integration provides the [Vertex AI - Predict task](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task) that lets you perform online predictions on your ML models.

## September 06, 2023

Feature

**Application Integration Quick setup ([GA](https://cloud.google.com/products/#product-launch-stages))**

Application Integration **Quick setup** is now generally available in all the supported [Google Cloud locations](https://docs.cloud.google.com/application-integration/docs/locations). 

**Quick setup** is a single-click operation that automatically provisions Application Integration with the default configurations needed to get you started with the product.

For more information, see [Set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration#quick).

## July 20, 2023

Feature

**Connector Event triggers** ([Preview](https://cloud.google.com/products#product-launch-stages))

Application Integration introduces **Connector Event triggers** ; specialized triggers that let you invoke an integration based on the [event subscriptions](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) created in various business applications using [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs).

The following Connector Event triggers are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [Jira Cloud trigger](https://docs.cloud.google.com/application-integration/docs/configure-jira-cloud-trigger)
  * [ServiceNow trigger](https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger)
  * [Zendesk trigger](https://docs.cloud.google.com/application-integration/docs/configure-zendesk-trigger)



For more information, see [Connector Event triggers](https://docs.cloud.google.com/application-integration/docs/triggers#connector-event-triggers-preview).

Issue

**Known issues**

  * [Integration fails to publish when duplicate Connector Event triggers are configured](https://docs.cloud.google.com/application-integration/docs/known-issue#integration_fails_to_publish_when_duplicate_connector_event_triggers_are_configured)
  * [Event subscription error when an integration containing Connector Event triggers is uploaded](https://docs.cloud.google.com/application-integration/docs/known-issue#event_subscription_error_when_an_integration_containing_connector_event_triggers_is_uploaded)



For more information, see [Application Integration known issues](https://docs.cloud.google.com/application-integration/docs/known-issue).

## July 05, 2023

Fixed

The issue relating to [Application Integration setup failure in a new Google Cloud project](https://docs.cloud.google.com/application-integration/docs/known-issue#application_integration_fails_to_set_up_in_a_new_google_cloud_project) has been resolved.

## December 26, 2022

Feature

**Test without publishing an integration**

You can now test your integration without the need to publish or create a new integration version. Testing an integration lets you experiment with the integration input variable values, and helps in identifying any faults in the integration connection flow before you finalize and publish the integration.

For more information, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
