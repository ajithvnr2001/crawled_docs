---
url: https://developer.android.com/stories/apps/monzo-camerax/
title: Monzo reduced over 9,000 lines of code and improved registration dropout by 5x with CameraX \u00a0|\u00a0 Developer stories \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:46.983200+00:00
---

# Monzo reduced over 9,000 lines of code and improved registration dropout by 5x with CameraX  |  Developer stories  |  Android Developers

> Source: https://developer.android.com/stories/apps/monzo-camerax/

  * [ Android Developers ](https://developer.android.com/)
  * [ Essentials ](https://developer.android.com/get-started)
  * [ Developer stories ](https://developer.android.com/stories)



#  Monzo reduced over 9,000 lines of code and improved registration dropout by 5x with CameraX Stay organized with collections  Save and categorize content based on your preferences. 

Monzo is a banking service and app offering digital and mobile-only financial services. Their mission is to make money work for everyone. To sign up new customers, the Monzo app captures images of an identification document (such as passport, driving license, or ID card) and takes a selfie video to prove that the identification documents are for the applicant.

## What they did

Early versions of the [Monzo](https://play.google.com/store/apps/details?id=co.uk.getmondo) app used camera2 APIs. Random crashes and odd behaviors on some devices led to 25% of potential customers not proceeding beyond the identification capture and selfie video steps.

To address these challenges, Monzo turned to CameraX, a Jetpack support library designed to make camera app development easier, to implement their image and video capture requirements. Using [`CameraController`](https://developer.android.com/reference/androidx/camera/view/CameraController), Monzo implemented the identification document image capture using the [`takePicture()`](https://developer.android.com/reference/androidx/camera/view/CameraController#takePicture\(androidx.camera.core.ImageCapture.OutputFileOptions,%20java.util.concurrent.Executor,%20androidx.camera.core.ImageCapture.OnImageSavedCallback\)) method. For the selfie video, they used the [`startRecording()`](https://developer.android.com/reference/androidx/camera/view/CameraController#startRecording\(androidx.camera.view.video.OutputFileOptions,%20java.util.concurrent.Executor,%20androidx.camera.view.video.OnVideoSavedCallback\)) and [`stopRecording()`](https://developer.android.com/reference/androidx/camera/view/CameraController#stopRecording\(\)) methods. They wanted to make design changes to the sign-up flow and wanted a more straightforward camera library that would give them more design flexibility.

## Results

Introducing CameraX enabled Monzo to simplify their code, making it more maintainable, and has helped simplify development. The move to CameraX has greatly reduced crashes and they are no longer seeing random activations of the camera flash. All of this has contributed to a reduction in the drop-off rate in the sign-up flow and has improved user feedback.

The simplification in code resulting from implementing CameraX reduced almost 9,000 lines of code, including 6,000 lines of UI code. In addition to making the code easier to maintain and simplifying development, CameraX also led to better code coverage in unit tests.

Importantly, the impact on the sign-up flow was significant. With the introduction of CameraX and the simplified flow design changes, the dropout rate from identification image capture and selfie video recording dropped from 25% to around 5%.

“For us, CameraX was all about stability and having an easy integration experience for our developers. It was the perfect library for us—we just wanted a simple way to take pictures and videos. CameraX has given us that, plus our code is simpler and the user experience better.” _Anastasios Morfopoulos—Android developer, Monzo_

## Get started

Check out the [CameraX documentation](https://developer.android.com/training/camerax) to learn how to introduce more robust and simplified image capture code to your app or game.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2022-01-25 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2022-01-25 UTC."],[],[]] 
