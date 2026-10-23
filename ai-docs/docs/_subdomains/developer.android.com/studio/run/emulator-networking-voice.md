---
url: https://developer.android.com/studio/run/emulator-networking-voice/
title: Send a voice call or SMS to another emulator instance \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:50.944658+00:00
---

# Send a voice call or SMS to another emulator instance  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/run/emulator-networking-voice/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Send a voice call or SMS to another emulator instance Stay organized with collections  Save and categorize content based on your preferences. 

The emulator automatically forwards simulated voice calls and SMS messages from one instance to another. To send a voice call or SMS, use the dialer app or SMS app, respectively, from one of the emulators.

To initiate a simulated voice call to another emulator instance:

  1. Launch the dialer app on the originating emulator instance.
  2. As the number to dial, enter the console port number of the target instance.



You can determine the console port number of the target instance by checking its window title, if it is running in a separate window, but not if it is running in a tool window. The console port number is reported as "Android Emulator (<port>)".

Alternatively, the `adb devices` command prints a list of running virtual devices and their console port numbers. For more information, see [Query for devices](https://developer.android.com/studio/command-line/adb#devicestatus).

  1. Click the dial button. A new inbound call appears in the target emulator instance.



To send an SMS message to another emulator instance:

  1. If an SMS app is available, launch it.
  2. Specify the console port number of the target emulator instance as the SMS address.
  3. Enter the message text.
  4. Send the message. The message is delivered to the target emulator instance.



You can also connect to an emulator console to simulate an incoming voice call or SMS. For more information, see [Telephony emulation](https://developer.android.com/studio/run/emulator-console#telephony) and [SMS emulation](https://developer.android.com/studio/run/emulator-console#sms).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-12 UTC."],[],[]] 
