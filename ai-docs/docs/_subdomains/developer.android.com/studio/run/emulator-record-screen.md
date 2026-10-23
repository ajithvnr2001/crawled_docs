---
url: https://developer.android.com/studio/run/emulator-record-screen/
title: Record the screen \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:45.013522+00:00
---

# Record the screen  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/run/emulator-record-screen/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Record the screen Stay organized with collections  Save and categorize content based on your preferences. 

You can record video and audio from the Android Emulator and save the recording to a WebM or animated GIF file.

The screen recording controls are in the **Record and Playback** tab of the [**Extended Controls**](https://developer.android.com/studio/run/emulator-extended-controls) window.

**Tip:** You can open the screen recording controls by pressing `Control`+`Shift`+`R` (`Command`+`Shift`+`R` on macOS).

  * To begin screen recording, click the **Start recording** button in the **Record and Playback** tab.
  * To stop recording, click **Stop recording**.



To save the recorded video:

  1. Controls for playing and saving the recorded video are at the bottom of the **Record and Playback** tab.
  2. Choose **WebM** or **GIF** from the menu at the bottom of the tab.
  3. Click **Save**.



You can also record and save a screen recording from the emulator using the following command on the command line:

`adb emu screenrecord start --time-limit 10 [path to save video]/sample_video.webm`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
