---
url: https://developer.android.com/quality/core-value/sdk-eligibility/
title: Inline Install API eligibility criteria for SDKs \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:06.337490+00:00
---

# Inline Install API eligibility criteria for SDKs  |  App quality  |  Android Developers

> Source: https://developer.android.com/quality/core-value/sdk-eligibility/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Core value ](https://developer.android.com/quality/core-value)



#  Inline Install API eligibility criteria for SDKs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the eligibility criteria for using the Inline Install API for Advertising SDKs. These criteria are subject to change.

In addition to meeting these eligibility criteria, advertising SDKs must accept the Terms of Service for the API. To accept the Terms of Service, fill out the [interest form](https://docs.google.com/forms/d/e/1FAIpQLSdq7OVNxAA8NDtMyVWXN5189uwiFi9b_aOJKMeXzOFGTkao1w/viewform). After your application has been reviewed and deemed eligible for the API, we will provide you with the Terms of Service for you to accept. After you accept the Terms of Service and meet all eligibility criteria, we will notify you that you can [integrate the API](https://developer.android.com/distribute/marketing-tools/inline-installs-sdk).

**Note:** Even if your SDK has successfully passed the review process and been allowlisted for the Inline Install API, the Inline Install experience may not be available because of [app eligibility criteria](https://developer.android.com/quality/core-value/app-eligibility). In that case, the call redirects to the standard Play Store App deep link page. More information is provided in the technical onboarding.

## SDK eligibility criteria

To qualify for access to this premium growth tool, you must provide a high-quality and trustworthy user experience, and you must be a developer in good standing on Google Play. In addition, the app that is to be installed must be of sufficiently high quality.

The following table describes all of the criteria to be met:

Criteria | Definition  
---|---  
The ad SDK is categorized appropriately in Play SDK Console. | Your SDK must offer display or video ads monetization for app publishers. This corresponds to an SDK category of _Advertising Platform_ or _Rewarded Videos_ in Play SDK Console.  
The ad SDK promotes a safe, secure, and high-quality user experience. |  You must meet the following criteria:

  * You must register on [Play SDK Console](https://play.google.com/sdk-console/about/), which includes a commitment that your SDK will not cause apps to violate [Play Developer Policies](https://play.google/developer-content-policy/).
  * You must provide publicly accessible documentation of your SDK's Data Safety Labels and Privacy Policy, and you must provide links to them on your _SDK Details_ page in Play SDK Console.
  * Your SDK must have no outstanding Play Developer Policy violations.
  * Your SDK must comply with the Ad UI Requirements.

  
The ad SDK accepts the API Terms of Service. | You must accept the legally binding Google Play Inline Install (Ad SDK Version) Terms of Service that are shared with you after initial eligibility checks.  
**Warning:** Ad SDKs must only use the Inline Install API according to the API Terms of Service. Google Play wants to provide users with contextual and seamless journeys. If we see that the Inline Install API is inappropriately used, we may revoke access. It's your responsibility as the SDK provider to ensure that the implementation of your SDK is aligned with the criteria in the table.

## Ad UI requirements

In accordance with the [Play Ads Policy](https://support.google.com/googleplay/android-developer/answer/9857753) and [App Promotion Policy](https://support.google.com/googleplay/android-developer/answer/9899004), all redirection to Inline Installs or to the Play Store app must require an informed user action. The following table lists some examples of guidelines which must be met to be eligible to use the Inline Install API. These guidelines may be updated on an ongoing basis to ensure a good user experience.

Predictable ad dismiss experience | 

  * Ads must comply with [Play Ads policies](https://support.google.com/googleplay/android-developer/answer/9857753), including requirements around Deceptive Ads and Disruptive Ads.
  * There are additional requirements for the size and position of the dismiss button, inspired by the [IAB New Ad Experience Guidelines](https://www.iab.com/wp-content/uploads/2019/04/IABNewAdPortfolio_AdExperience_CBA_Guide.pdf) (aligned with CBA Better Ads Standards): the dismiss button must be presented clearly in the top right or top left corner (locale specific) with a minimum clickable area of 50x50 dp. For more information about IAB creative guidelines, see the [IAB New Ad Portfolio](https://iabtechlab.com/standards/iab-new-ad-portfolio-guidelines/).

  
---|---  
No automatic redirection to Play Inline Install AP or the Play Store app | 

  * Ads that don't have a dismiss button can't automatically redirect to the Play Inline Install API or the Play Store app without an additional click to action. Ads with a dismiss button can automatically redirect to the Play Inline Install API or the Play Store app only if the user has watched the ad fully to the end and didn't click the dismiss button.
  * If the ad can be mistaken for a playable ad (for example, a linear video depicting a playable ad experience), a separate click to action is required before redirecting to the Play Inline Install API or the Play Store app.

  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
