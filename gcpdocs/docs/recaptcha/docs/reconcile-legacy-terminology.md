---
url: https://docs.cloud.google.com/recaptcha/docs/reconcile-legacy-terminology/
title: Reconcile Admin Console and Google Cloud console terminology \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:45:06.679000+00:00
---

# Reconcile Admin Console and Google Cloud console terminology  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/reconcile-legacy-terminology/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Reconcile Admin Console and Google Cloud console terminology Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to identify your reCAPTCHA key version (`v2` or `v3`), map legacy [reCAPTCHA Admin console](https://www.google.com/recaptcha/admin) terminology to the Google Cloud console, and retrieve the site keys and secret keys required by content management system (CMS) platforms and third-party plugins, such as WordPress or Shopify integrations.

## Map legacy terminology to the Google Cloud console

If you manage your keys only in the [reCAPTCHA Admin console](https://www.google.com/recaptcha/admin), you're using reCAPTCHA Classic. If you manage your keys on the **Google Cloud Fraud Defense** page in the Google Cloud console, you're using Fraud Defense. Both consoles support `v2` and `v3` website keys.

Many CMS platforms and plugins refer to reCAPTCHA keys using legacy version numbers, such as `v2 Checkbox`, `v2 Invisible`, and `v3`. The Google Cloud console uses platform-based descriptors instead of version numbers.

The following table maps legacy CMS and Admin Console terminology to the Google Cloud console terminology:

CMS or Admin Console terminology | Google Cloud console (**Platform details**) | **Edit key** (**Type** field) | Verification mechanism and CMS compatibility  
---|---|---|---  
Score based (v3) | `Website • score` | `Website • Score` | Frictionless, score-based verification. Use for CMS plugins that require **reCAPTCHA v3**.  
Challenge (v2) | `Website • checkbox` | `Website • Checkbox challenge` | Requires the user to select an "I'm not a robot" checkbox. Use for CMS plugins that require **reCAPTCHA v2 Checkbox**.  
Invisible (v2) | `Website • invisible` | `Website • Invisible integration` | Analyzes risk in the background and might show a challenge. Use for CMS plugins that require **reCAPTCHA v2 Invisible**.  
N/A | `Website • policy-based challenge` | `Website • Policy-based challenge` | Triggers challenges based on a configured score threshold. Requires a custom `CreateAssessment` integration.  
N/A | `iOS` | `iOS app` | iOS mobile key without challenge.  
N/A | `Android` | `Android app` | Android mobile key without challenge.  
**Note:** You can't create new Invisible (v2) keys using the Google Cloud console. Create a score-based (`v3`) or checkbox (`v2`) web key instead.

### View your key version in the Google Cloud console

To view the version of your key in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Select the **Keys** tab.

  3. If your keys are in **Cards** view, switch to **Table** view.

  4. Check the **Platform details** column for your key. For example, `Website • score` corresponds to `v3`, and `Website • checkbox` corresponds to `v2 Checkbox`.

  5. Optional. In **Cards** view, click **Key details** on a key card, and then select **Edit key**. The **Type** field shows the key configuration, such as `Website • Score` for `v3` or `Website • Checkbox challenge` for `v2 Checkbox`.




## Find the site key and secret key

Third-party plugins and CMS platforms often require a site key and a secret key for reCAPTCHA integration:

  * **Site key** : In the Google Cloud console, the **Key ID** corresponds to the site key.
  * **Secret key** : The Google Cloud console doesn't display the secret key by default because Google Cloud authentication typically uses API keys or Identity and Access Management roles. However, you can retrieve the legacy secret key for plugins that require it. Some third-party libraries or documentation might refer to the legacy secret key as a **private key**.



### Retrieve the secret key in the Google Cloud console

To retrieve the site key and secret key, do the following:

  1. In the Google Cloud console, go to the **Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Select the **Keys** tab.

  3. In the **reCAPTCHA Keys** section, go to the key that you need the secret key for:

     * If you're in the **Cards** view, click **Key details** on the key card. The **Key ID** is displayed at the top of the page.
     * If you're in the **Table** view, the **Key ID** is visible in the table. Click the key to go to its details page.
  4. Copy the **Key ID** displayed at the top of the page. This value is your **site key**.

  5. Go to the **Integration** tab.

  6. Depending on the key's status, do one of the following:

     * If the key is configured for legacy use, click **Use legacy key**.
     * If the key isn't integrated with a legacy service, click **Integrate with a third-party service or plugin**.
  7. A dialog appears with your **secret key**. Copy this value securely. Treat this secret as sensitive data.

Alternatively, on the **Key details** page, click **Edit key** , and then click **Reveal** next to the **Secret key** field.




## Integrate with WordPress, Shopify, or other CMS platforms

If you use a website builder, ecommerce platform, or CMS plugin, the platform or plugin loads the reCAPTCHA script and verifies user tokens automatically. You don't need to install [reCAPTCHA client libraries](https://docs.cloud.google.com/recaptcha/docs/libraries) or write custom backend code.

To configure reCAPTCHA in a CMS or third-party plugin, do the following:

  1. **Check the reCAPTCHA version required by your CMS or plugin** : Open the reCAPTCHA integration settings in your CMS or plugin and check which key type it supports (typically **reCAPTCHA v3** or **reCAPTCHA v2 Checkbox**).
  2. **Select or create a matching key** :

     * If you already have a key, view your key version to confirm that it matches the version selected in your plugin (`Website • score` for `v3`, or `Website • checkbox` for `v2 Checkbox`).
     * If you need a new key, [create a key for your website](https://docs.cloud.google.com/recaptcha/docs/create-key-website) that matches the required version, and add your website domain (for example, `example.com`) to the key's **Domain list**.
**Note:** Using a `v3` score-based key in a plugin configured for `v2 Checkbox` (or the reverse) causes an `Invalid key type` error on your website.
  3. **Copy your site key and legacy secret key** : Follow the steps in Retrieve the secret key in the Google Cloud console to get your **Key ID** (site key) and **secret key**.

  4. **Enter the keys in your CMS or plugin settings** :

     * Paste the **Key ID** into the **Site key** field.
     * Paste the **secret key** into the **Secret key** (or **Private key**) field, and then save your settings.
**Note:** Some plugins also offer a built-in **reCAPTCHA Enterprise** mode that requests a **Project ID** and an **API key** instead of a legacy secret key. For those plugins, provide your Google Cloud project ID, **Key ID** , and a restricted [Google Cloud API key](https://docs.cloud.google.com/docs/authentication/api-keys).



## Integrate custom websites using assessments

**Important:** For custom integrations that don't use third-party plugins, use the `CreateAssessment` method instead of the legacy `SiteVerify` method. 

The `CreateAssessment` method provides detailed risk analysis and reason codes, and enables access to advanced Fraud Defense features. You can call the `CreateAssessment` method using the [reCAPTCHA client libraries](https://docs.cloud.google.com/recaptcha/docs/libraries) or the REST API.

For more information, see [Create an assessment for your website](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).

### Legacy `SiteVerify` method

Although we recommend the `CreateAssessment` method for new and custom integrations, some existing systems or third-party plugins still rely on the legacy `SiteVerify` method. This method requires a **secret key** associated with your reCAPTCHA key.

If you need to integrate with a system that requires the legacy `SiteVerify` API, see [Verify user response tokens with legacy SiteVerify](https://docs.cloud.google.com/recaptcha/docs/verify).

## What's next

  * [Create keys for websites](https://docs.cloud.google.com/recaptcha/docs/create-key-website)
  * [Troubleshoot reCAPTCHA integration issues](https://docs.cloud.google.com/recaptcha/docs/troubleshoot-recaptcha-issues)
  * [Create an assessment for websites](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
