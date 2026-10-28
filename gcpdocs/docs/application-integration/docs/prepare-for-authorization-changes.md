---
url: https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes/
title: Prepare for upcoming authorization changes \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T09:50:58.789844+00:00
---

# Prepare for upcoming authorization changes  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare for upcoming authorization changes

Application Integration is updating how it authorizes integrations. These changes took effect for new integrations on October 15, 2026. Existing integrations keep their current behavior until a later date. Most integrations continue to run without changes, but some require a configuration update to keep running. You can make the changes described on this page now because they use configurations you already control. 

## Upcoming authorization changes

Application Integration is updating how it handles identities for integration runs. Every run must now have an explicit identity, acting as one of the following:

  * The user who triggered the run. The called systems apply that user's access permissions.
  * A run-as service account. You control, scope, and audit this account like any other service account in your Google Cloud project.



Because of this update:

  * To publish or test an integration that has a run-as service account, you must have permission to act as that account. Running the integration, approving its suspended runs, and calling it from another integration will require the same permission as the rollout proceeds.
  * You can't publish or test a new integration with a scheduled or event trigger without a run-as service account. Runs that reach a task without an identity, and asynchronous runs of any integration without a run-as service account, are planned to fail in a later release.



## When these updates take effect

Integration | When the updates apply  
---|---  
Created **on or after October 15, 2026** | From the first version you create. Every version you publish afterward retains the new behavior.  
Created **before October 15, 2026** | These integrations keep their current behavior until a later date, which Application Integration announces separately.  
**Note:** Editing an integration doesn't change its stage, and a sub-integration runs in its own stage, not in the stage of the integration that calls it. The following conditions do not depend on the stage: 

  * Service Account User checks apply to every integration, regardless of its creation date.
  * Every test uses the new behavior, including tests started from the Google Cloud console and tests of integrations created before October 15, 2026.



## What to do

Make these changes now, whichever stage your integrations are in. They take effect as soon as you make them.

  1. **[Find integrations that need a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-find-affected)** : integrations that run asynchronously, on a schedule, or from an event, and don't have one.
  2. **[Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access)** on each run-as service account and each authentication profile's service account, to everyone who runs, tests, publishes, or approves the integration, and to the service accounts your triggers and automation use.
  3. **[Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as)** on each integration you found, and publish it.

**Warning:** Complete step 2 before step 3. Publishing an integration with a run-as service account requires Service Account User on that account, so if you set the service account first, the publish can be rejected.

## Try the new behavior before it applies

Integrations created on or after October 15, 2026 already use the new behavior. Your existing integrations keep their current behavior until a later date, but you don't have to wait to find out how they will be affected. There are two ways to try the change while you still control the timing.

### Turn on end user credentials for a region

This applies the new behavior to every integration in one region.

  1. In the Google Cloud console, go to the region's settings.
  2. Turn on **Run integrations with end user credentials**.
  3. Save the settings.



Tasks in that region then call downstream services as the user who triggered the integration, instead of as a shared platform identity. Runs with no triggering user fall back to an identity that has no permissions.

**Warning:** This setting applies to every integration in the region, including ones created before October 15, 2026. A task that touches a resource the triggering user can't access starts failing with a permission error. Work through What to do first, then turn the setting on.

### Test a single integration asynchronously

If you would rather try one integration than a whole region, run it asynchronously from the test panel. This takes the same credential path as a scheduled or event-driven run, without changing any settings.

  1. Open the integration and click **Test integration**.
  2. Under **Execution mode** , turn on **Run asynchronously**.
  3. Enter your input values and run the test.



The run is enqueued the way a real trigger fires, with no caller credentials, so it exercises the credential path a scheduled or event trigger would use. The test runs the version you have open with the inputs you entered, and reports an execution ID rather than the output.

**Note:** If any configuration value differs from the saved version, the run is refused and nothing is queued. Save the integration before you test it asynchronously.

If something fails after the change, see [Troubleshoot authorization errors](https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
