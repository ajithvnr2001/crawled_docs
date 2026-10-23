---
url: https://developer.android.com/security/fraud-prevention/activities/
title: Secure sensitive activities \u00a0|\u00a0 Fraud prevention \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:40.120483+00:00
---

# Secure sensitive activities  |  Fraud prevention  |  Android Developers

> Source: https://developer.android.com/security/fraud-prevention/activities/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ Security ](https://developer.android.com/security)
  * [ Fraud prevention ](https://developer.android.com/security/fraud-prevention)
  * [ Guides ](https://developer.android.com/security/fraud-prevention/environment)



#  Secure sensitive activities Stay organized with collections  Save and categorize content based on your preferences. 

This document details ways to monitor sensitive activities, such as user logins and online purchases.

## FLAG_SECURE

`FLAG_SECURE` is a [Window flag](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE) that tells Android not to allow screenshots or to display the window view on a non-secure display (such as Casting the screen). This is useful for applications that need to protect sensitive information, like banking apps or password managers. When a window is flagged with `FLAG_SECURE`, Android prevents screenshots from being taken and prevents the window from being displayed on a non-secure display, such as a TV or projector. This helps to protect the information that is being displayed in the window from being accessed by unauthorized people.

### How this helps mitigate fraud

A malicious app or entity might retrieve background screenshots. When the state of your app changes to the background, `FLAG_SECURE` can be used. When the screenshot is taken the resulting image is blank.

`FLAG_SECURE` also helps with remote screen sharing use cases. It isn't always a malicious app that will retrieve screenshots, legitimate screen sharing apps are also commonly found used in fraudulent situations.

### Implementation

For views with the information you want protected, add the following:

### Kotlin
    
    
    window?.setFlags(
        WindowManager.LayoutParams.FLAG_SECURE,
        WindowManager.LayoutParams.FLAG_SECURE
    )

### Java
    
    
    window.setFlags(
      WindowManager.LayoutParams.FLAG_SECURE,
      WindowManager.LayoutParams.FLAG_SECURE
    );

### Best practices

It is important to note that this approach isn't reliable in preventing overlay attacks. In some cases it does not correctly predict if screen recording is active, however it does cover most use cases. To mitigate overlay attacks, read the next section about `HIDE_OVERLAY_WINDOWS` permissions.

**Note:** For Android 11 (API 30) and lower `FLAG_SECURE` is able to help around 70% of the devices reliably. This is because on certain devices keyboard taps can be recorded.

## HIDE_OVERLAY_WINDOWS

`HIDE_OVERLAY_WINDOWS` is a permission added in Android 12 where your app can opt-out of having application overlays drawn over it. In Android 12 we have made it harder to acquire the [`SYSTEM_ALERT_WINDOW`](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW) permission, essentially allowing your app to block overlays from third-party apps.

### How this helps mitigate fraud

When you enable the `HIDE_OVERLAY_WINDOWS` permission you are opting out of having application overlays drawn on top of your app. This permission provides a protection mechanism against [cloak and dagger](https://cloak-and-dagger.org/) attacks.

### Implementation

To enable this permission, add [`HIDE_OVERLAY_WINDOWS`](https://developer.android.com/reference/android/Manifest.permission#HIDE_OVERLAY_WINDOWS) to your project's manifest.

### Best practices

As with any permission, you should trust any overlay app at least as much as you trust any other app on the device. In other words, your app shouldn't allow other apps to draw overlays over it unless you know the other app is trustworthy. Allowing an app to draw over other apps can be dangerous because it can steal passwords or read messages.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
