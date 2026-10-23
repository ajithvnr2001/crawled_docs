---
url: https://developer.android.com/training/app-links/faq/
title: App Links FAQ \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:04.289158+00:00
---

# App Links FAQ  |  App architecture  |  Android Developers

> Source: https://developer.android.com/training/app-links/faq/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  App Links FAQ Stay organized with collections  Save and categorize content based on your preferences. 

### What happens on devices running lower versions of Android?

Dynamic App Links on Android 15+ uses the same `handle_all_urls` relation type as App Links on earlier versions, but uses a new field, `dynamic_app_link_components`. Earlier versions will ignore the new `dynamic_app_link_components` field to allow for compatibility. If you need to support specific paths on older Android versions, you must declare them in the manifest as you traditionally would.

### Can I use both manifest-based path rules and dynamic rules at the same time?

Yes, the system will merge your dynamic rules with manifest-based rules. However, note that the rules defined in your manifest set the maximum allowed scope for your App Link paths, so all of your dynamic rules must be within that scope. The system does not allow dynamic rules to change or expand the static scope that you have declared in your manifest paths. A typical Dynamic App Links implementation would have a fairly broad scope set in the manifest configuration, with dynamic rules managed from the server that fine-tune the paths.

### What's the best way to get the SHA-256 fingerprint for the assetlinks.json file?

The most reliable way is to get it from the Google Play Console. Navigate to your app's **Protected with Play - > Play Store protection -> Manage Play app signing**. Under **App signing key certificate** , you will find the SHA-256 certificate fingerprint. This is the same key that Google Play uses to sign your app release. Alternatively, for local builds, you can use the `keytool` command-line utility on your keystore file.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
