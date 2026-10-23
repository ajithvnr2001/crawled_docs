---
url: https://developer.android.com/studio/projects/continuous-integration/
title: Set up continuous integration \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:36.033536+00:00
---

# Set up continuous integration  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/projects/continuous-integration/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Set up continuous integration Stay organized with collections  Save and categorize content based on your preferences. 

Continuous integration systems let you automatically build and test your app every time you check in updates to your source control system. You can use any continuous integration tool that can initiate a Gradle build to build your Android Studio projects.

To run tests as part of the build, you need to either configure your continuous integration server to use the [Android Emulator](https://developer.android.com/studio/run/emulator-commandline) or use [Firebase Test Lab](https://firebase.google.com/docs/test-lab/) to run your tests.

For specific information about configuring continuous integration for your Android project using Jenkins and Firebase Test Lab, see [Start testing with continuous integration (CI) systems](https://firebase.google.com/docs/test-lab/continuous).

**Note:** You must accept the license agreements for any packages your app requires on each machine where you build your app. If you have not installed Android Studio on your continuous integration server, you can [accept licenses from the command line using `sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager#accept-licenses).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
