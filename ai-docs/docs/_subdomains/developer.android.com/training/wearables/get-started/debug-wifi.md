---
url: https://developer.android.com/training/wearables/get-started/debug-wifi/
title: Debug Wear OS over Wi-Fi \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:04.295315+00:00
---

# Debug Wear OS over Wi-Fi  |  Android Developers

> Source: https://developer.android.com/training/wearables/get-started/debug-wifi/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Debug Wear OS over Wi-Fi Stay organized with collections  Save and categorize content based on your preferences. 

Wear OS supports wireless debugging, which lets you debug your app over a Wi-Fi network.

## Prerequisites

Before you begin, verify that you have the following:

  * **Android Debug Bridge (ADB):** Use [`adb`](https://developer.android.com/tools/adb) version 30.0.0 or higher.
  * **Same Wi-Fi network:** Your development computer and the Wear OS watch must be connected to the same Wi-Fi network.

**Note:** Many enterprise Wi-Fi networks enable access point isolation, which prevents devices from communicating with each other. If you encounter issues, try connecting both devices to a mobile hotspot.



## Enable wireless debugging

  1. [Enable developer options](https://developer.android.com/studio/debug/dev-options#enable) on your watch.
  2. On the watch, open **Settings** and navigate to **Developer options**.
  3. Enable **ADB debugging**.
  4. Enable **Wireless debugging**.

In the dialog that appears, select **Allow** or **Always allow on this network** to confirm.




## Pair your computer with the watch

You only need to pair your computer with the watch once.

  1. On the watch, navigate to **Settings > Developer options > Wireless debugging**.
  2. Select **Pair new device**.
  3. The watch displays a **Wi-Fi pairing code** , an **IP address** , and a **Port** for pairing. Note these values.
  4. On your computer, open a terminal and run the following command, replacing `ip-address` and `pairing-port` with the values shown on the watch:
         
         adb pair ip-address:pairing-port
         

  5. When prompted, enter the Wi-Fi pairing code shown on the watch. If pairing succeeds, you see a message similar to:
         
         Successfully paired to ip-address:pairing-port
         




## Connect to the watch

After the watch and computer pair, you can connect to the watch. You need to reconnect each time you restart wireless debugging or change Wi-Fi networks.

  1. On the watch, navigate to **Settings > Developer options > Wireless debugging**.
  2. Find the **IP address** and **Port** for the connection under **Wireless debugging** (not under "Pair new device").

**Note:** The connection port is usually different from the pairing port.
  3. On your computer, run the following command:
         
         adb connect ip-address:connection-port
         

  4. Verify the connection by running:
         
         adb devices
         

Your watch should appear in the list of connected devices.

If this command returns more than one device, preface your `adb` commands with the IP address of the device:
         
         adb -s ip-address:connection-port
         




## Troubleshooting

If you are unable to connect, do the following:

  * **Check network connection:** Check that both devices are on the same Wi-Fi network and that the network allows peer-to-peer traffic.
  * **Restart ADB:** On your computer, run `adb kill-server` and then `adb start-server`, then try connecting again.
  * **Toggle debugging:** Turn **Wireless debugging** off and back on on the watch.



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
