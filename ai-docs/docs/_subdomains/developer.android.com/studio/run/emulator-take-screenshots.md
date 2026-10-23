---
url: https://developer.android.com/studio/run/emulator-take-screenshots/
title: Take screenshots \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:44.832181+00:00
---

# Take screenshots  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/run/emulator-take-screenshots/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Take screenshots Stay organized with collections  Save and categorize content based on your preferences. 

To take a screenshot of the Android Emulator, click the **Take screenshot** ![Take Screenshot icon](https://developer.android.com/static/images/tools/e-itakescreenshot.png) button.

In the **Take Screenshot** dialog that appears, you can recapture, edit, or copy the captured image. Once you're satisfied with the image, click **Save**. The emulator creates a PNG file with the name `Screenshot_yyyymmdd-hhmmss.png`, using the year, month, day, hour, minute, and second of the capture. You can change the name, if you prefer, and choose where to save the file.

To take a [Play-compatible screenshot of a Wear OS emulator](https://developer.android.com/docs/quality-guidelines/wear-app-quality#google-play-screenshots-apps), set the drop-down to **Play Store Compatible**.

![Take screenshot dialog including Play Store Compatible drop-down.](https://developer.android.com/static/studio/images/wear-screenshot-play-compatible-dark.png)

You can also take screenshots from the command line with either of the following commands:

  * `screenrecord screenshot [destination-directory]`
  * `adb emu screenrecord screenshot [destination-directory]`



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
