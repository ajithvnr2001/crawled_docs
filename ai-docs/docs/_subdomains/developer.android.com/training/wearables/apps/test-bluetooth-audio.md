---
url: https://developer.android.com/training/wearables/apps/test-bluetooth-audio/
title: Test Bluetooth audio on emulators \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:14.453568+00:00
---

# Test Bluetooth audio on emulators  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/apps/test-bluetooth-audio/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Test Bluetooth audio on emulators Stay organized with collections  Save and categorize content based on your preferences. 

On the Wear OS emulator, system images that run Wear OS 4 or higher include support for emulated Bluetooth. This support lets you test several use cases related to Bluetooth audio.

## Pair with an emulated phone

Using the emulator's Bluetooth support, you can pair with an emulated phone. To do so, enable the setup wizard from the command line:
    
    
    -append-userspace-opt androidboot.setupwizard_mode=REQUIRED
    

## Play audio through an emulated output device

Using the emulator's Bluetooth support, you can also play audio through an emulated Bluetooth output device. To test audio output switching in the emulator, connect to an emulated Bluetooth output device using the open source [Bumble project](https://www.github.com/google/bumble).

### Prepare your environment

To prepare your development machine for using Bumble, complete the following steps:

  1. Fetch the Bumble source code:
         
         git clone https://github.com/google/bumble
         

  2. Navigate to the `bumble` directory, then build and install Bumble modules:
         
         cd bumble && python3 -m pip install "."
         




### Launch emulated Bluetooth speaker

To launch the emulated speaker, complete the following steps:

  1. Launch a version of the emulator that supports Wear OS 4 or higher.

**Note:** If you're using an emulator version lower than 33.1.10, launch the emulator from the command line using the `-packet-streamer-endpoint default` parameter.
  2. To discover and connect to the emulated speaker, run the following command in the `bumble` directory:
         
         python3 examples/run_a2dp_sink.py examples/a2dp_sink1.json \
           android-netsim stdout | ffplay -i
         

The audio output is played through your computer's speakers.

You can also redirect output to a file:
         
         python3 examples/run_a2dp_sink.py examples/a2dp_sink1.json \
           android-netsim output.sbc
         




Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
