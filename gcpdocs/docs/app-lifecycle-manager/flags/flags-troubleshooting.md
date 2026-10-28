---
url: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/
title: Troubleshoot feature flags \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:37:51.555341+00:00
---

# Troubleshoot feature flags  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/

[ Skip to main content ](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/)
  * [Deutsch](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=es-419)
  * [Français](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=id)
  * [Italiano](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=ja)
  * [한국어](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fapp-lifecycle-manager%2Fflags%2Fflags-troubleshooting%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/operations-color.svg) ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [SDK and Runtime Evaluation](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#sdk_and_runtime_evaluation)
    * [Symptom: Flag returning safe default value](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#symptom_flag_returning_safe_default_value)
    * [Symptom: Unexpected evaluation results](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#symptom_unexpected_evaluation_results)
  * [Monitor Rollouts](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#monitor_rollouts)
    * [Rollout orchestration state](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#rollout_orchestration_state)
  * [Unit Missing Configs](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#unit_missing_configs)
    * [Understanding Unit Pinning](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#understanding_unit_pinning)
    * [Missing Config from Pinned Units](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#missing_config_from_pinned_units)
    * [Diagnostic Commands](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#diagnostic_commands)
    * [Manual Mitigation](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#manual_mitigation)


We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)


Was this helpful?
Send feedback 
#  Troubleshoot feature flags Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [SDK and Runtime Evaluation](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#sdk_and_runtime_evaluation)
    * [Symptom: Flag returning safe default value](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#symptom_flag_returning_safe_default_value)
    * [Symptom: Unexpected evaluation results](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#symptom_unexpected_evaluation_results)
  * [Monitor Rollouts](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#monitor_rollouts)
    * [Rollout orchestration state](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#rollout_orchestration_state)
  * [Unit Missing Configs](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#unit_missing_configs)
    * [Understanding Unit Pinning](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#understanding_unit_pinning)
    * [Missing Config from Pinned Units](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#missing_config_from_pinned_units)
    * [Diagnostic Commands](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#diagnostic_commands)
    * [Manual Mitigation](https://docs.cloud.google.com/app-lifecycle-manager/flags/flags-troubleshooting/#manual_mitigation)


This guide provides steps to diagnose and resolve common issues with App Lifecycle Manager feature flags.
## SDK and Runtime Evaluation
The OpenFeature API is designed for maximum safety and will never throw an error that crashes your application.
### Symptom: Flag returning safe default value
If the flag service is unreachable, the provider is unavailable, or the flag is misconfigured, the SDK returns the required default value provided in your code.
**Resolution:**
  1. Verify the connection between your OpenFeature provider and the `saasconfig.googleapis.com` endpoint.
  2. Check for authentication errors. Ensure the service account has `roles/saasconfig.viewer`.
  3. Verify `FLAGD_SOURCE_PROVIDER_ID` is correct.


### Symptom: Unexpected evaluation results
If a flag is not returning the expected variant:
**Resolution:**
  1. Check your CEL conditions and evaluation context.
  2. If a required attribute is missing from the context during a condition check, the evaluation engine skips that specific rule.
  3. If an attribute is missing during a percentage-based allocation, the evaluation returns `INVALID_CONTEXT`.


## Monitor Rollouts
Monitoring a feature flag rollout involves verifying both the orchestration state (did the rollout complete?) and the application health (did the binary pick up the flag?).
### Rollout orchestration state
The system monitors the success rate of operations in real-time.
#### Automatic pausing
To prevent a "broken" configuration from reaching your entire fleet, the system automatically pauses a rollout if the failure rate exceeds the Error Budget (default 10% per location).
#### Check summary stats
Use the `describe` command to see the aggregate failure count and determine if the rollout is `PAUSED` or `FAILED`.

```
gcloud beta app-lifecycle-manager rollouts describe ROLLOUT_ID --location=global

```

#### Filter failed unit updates
Once you confirm failures exist, you must find the specific units that missed the update. Use this filter to isolate only the failed flag updates in a specific region:

```
gcloud beta app-lifecycle-manager unit-operations list \
    --location=LOCATION \
    --filter="state:UNIT_OPERATION_STATE_FAILED AND flag_update:*"

```

#### Diagnose the Root Cause
For each failed operation, you can retrieve a detailed error message provided by the actuation engine. Read the `state_message` field.

```
gcloud beta app-lifecycle-manager unit-operations describe OPERATION_ID --location=LOCATION

```

## Unit Missing Configs
### Understanding Unit Pinning
Pinning freezes a unit at its current release, preventing it from being updated by any automated or manual rollouts. A pinned unit is explicitly excluded from rollout operations until its pinning period expires or it is manually unpinned.
### Missing Config from Pinned Units
A critical scenario occurs when a unit is pinned during a feature flag rollout. Pinning blocks all updates, meaning the unit skips the `FlagUpdate` operation required to receive its configuration.
**Symptom:** After the unit is unpinned and upgraded to a binary that requires feature flags, the application fails to initialize or enters an infinite retry loop, leading to failed readiness probes and continuous container restarts.
**Root Cause:** The UnitKind's `default_flag_revisions` were not updated while the unit was pinned, leaving the unit with no active configuration.
### Diagnostic Commands
#### 1. List Failed Flag Operations
To find units that missed an update, filter the unit operations for the `UNIT_OPERATION_STATE_FAILED` state and the `flag_update` type.

```
gcloud beta app-lifecycle-manager unit-operations list \
    --location="LOCATION" \
    --filter="state:UNIT_OPERATION_STATE_FAILED AND flag_update:*"

```

#### 2. Filter Specifically for Failed Flag Rollouts
To pinpoint failed flag updates across your fleet or for a specific unit, add a condition for the `UNIT_OPERATION_STATE_FAILED` state.

```
# Find all failed operations for a specific unit
gcloud beta app-lifecycle-manager unit-operations list \
    --location="LOCATION" \
    --filter="unit:UNIT_ID AND state:UNIT_OPERATION_STATE_FAILED"

```

#### 3. Inspect the Failure Reason
Use the `describe` command to read the `state_message`.

```
gcloud beta app-lifecycle-manager unit-operations describe "OPERATION_ID" --location="LOCATION"

```

#### 4. Check Unit Condition
You can also check the current state of a unit directly. If a flag rollout is currently failing or the last operation resulted in an error, it will be reflected in the status. Conditions with a type of `operationError`.

```
gcloud beta app-lifecycle-manager units describe "UNIT_ID" --location="LOCATION"

```

### Manual Mitigation
#### Applying UnitKind Default Flag Revisions
If a unit is missing its configuration because it was pinned during one or more rollouts, you can recover it by manually resetting the unit to the current baseline defined in its UnitKind.
  1. **Unpin the unit** (if pinned).
  2. **Retrieve default revisions** from parent UnitKind.
  3. **Create a new FlagRelease** containing those revisions.
  4. **Manually initiate a FlagUpdate** unit operation to apply the recovery release.


```
# 1. Unpin
gcloud beta app-lifecycle-manager units update "UNIT_ID" \
    --location="LOCATION" \
    --maintenance-pinned-until-time=""

# 2. Retrieve default revisions
gcloud beta app-lifecycle-manager unit-kinds describe "UNIT_KIND_ID" \
    --location="global" \
    --format="value(defaultFlagRevisions)"

# 3. Create recovery release
gcloud beta app-lifecycle-manager flags releases create "recovery-release-1" \
    --location="global" \
    --unit-kind="UNIT_KIND_ID" \
    --revisions="REVISIONS"

# 4. Initiate manual update
gcloud beta app-lifecycle-manager unit-operations create "recovery-op" \
    --unit="UNIT_ID" \
    --flag-release="recovery-release-1" \
    --location="global"

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
