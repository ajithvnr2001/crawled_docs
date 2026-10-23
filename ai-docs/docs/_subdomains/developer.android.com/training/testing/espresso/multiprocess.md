---
url: https://developer.android.com/training/testing/espresso/multiprocess/
title: Multiprocess Espresso \u00a0|\u00a0 Test your app on Android \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:58.953307+00:00
---

# Multiprocess Espresso  |  Test your app on Android  |  Android Developers

> Source: https://developer.android.com/training/testing/espresso/multiprocess/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Test your app on Android ](https://developer.android.com/training/testing)



#  Multiprocess Espresso Stay organized with collections  Save and categorize content based on your preferences. 

As your app grows, you might find it useful to place some of your app components in a process other than your app's main process. To test app components in these _non-default processes_ , you can use the functionality of Multiprocess Espresso. This tool, available on Android 8.0 (API level 26) and higher, allows you to seamlessly test your app's UI interactions that cross your app's process boundaries while maintaining Espresso's synchronization guarantees.

When using Multiprocess Espresso, keep the following versioning and scope considerations in mind:

  * Your app must target Android 8.0 (API level 26) or higher.
  * The tool can only test app components that you include in processes within your app's package. It cannot test external processes.



## Use the tool

To test a process within your app using Multiprocess Espresso, add a reference to the **espresso-remote** artifact in your app's `build.gradle` file:

app/build.gradle

### Groovy
    
    
    dependencies {
        ...
        androidTestImplementation 'androidx.test.espresso:espresso-remote:3.6.1'
    }

### Kotlin
    
    
    dependencies {
        ...
        androidTestImplementation('androidx.test.espresso:espresso-remote:3.6.1')
    }

You also need to add the following to your app's `androidTest` manifest:

  * An `<instrumentation>` element that defines the process.
  * A `<meta-data>` element indicating that you want to use Multiprocess Espresso.



The following code snippet shows how to add these elements:

src/androidTest/AndroidManifest.xml
    
    
    <manifest ... package="androidx.test.mytestapp.tests">
      <uses-sdk android:targetSdkVersion="27" android:minSdkVersion="14" />
      <instrumentation
        android:name="androidx.test.runner.AndroidJUnitRunner"
        android:targetPackage="androidx.test.mytestapp"
        **android:targetProcesses="*"** >
        **< meta-data
          android:name="remoteMethod"
          android:value="androidx.test.espresso.remote.EspressoRemote#remoteInit" />**
      </instrumentation>
    </manifest>

The previous snippet indicates to the Android framework that you want it to test every process in your app's package. If you want to test only a subset of your app's processes, you can specify a comma-separated list within the `[targetProcesses](https://developer.android.com/reference/android/content/pm/InstrumentationInfo#targetProcesses)` element instead:
    
    
    <instrumentation
        ...
        android:targetProcesses=
                "androidx.test.mytestapp:myFirstAppProcessToTest,
                 androidx.test.mytestapp:mySecondAppProcessToTest" ... />
    

**Note:** Multiprocess Espresso ignores the value of `[targetProcesses](https://developer.android.com/reference/android/content/pm/InstrumentationInfo#targetProcesses)` if you set it to your app package's main process.

## Understand the tool's architecture

When you test your app and launch its default process, you might perform a UI interaction, such as a button press, that starts an activity in a secondary process. The system then completes the following steps to enable cross-process testing using Espresso:

  1. The Android Framework creates and starts a new process to follow your app's navigational structure. Each `[Instrumentation](https://developer.android.com/reference/android/app/Instrumentation)` process includes a new instance of [`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner). At this stage, the 2 instrumentation processes cannot communicate with each other.
  2. Each [`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) instance registers Espresso as its testing framework.
  3. The 2 instances of [`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) perform a handshake to establish a connection between each other. At the same time, each [`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) instance connects all registered clients like Espresso with their respective counterparts in other processes so that these clients can form a direct communication channel between themselves.
  4. Each [`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) instance continues to look for newly-added instrumentation instances and testing framework clients, establishing additional communication channels as needed.



Figure 1 illustrates the result of this process:

![](https://developer.android.com/static/images/training/testing/multiprocess_espresso.png)**Figure 1.** Establishing communication between multiple instrumentation processes using Multiprocess Espresso

## Additional resources

For further information on this topic, consult the following resources.

  * [Test-Driven Development on Android with the Android Testing Support Library](https://www.youtube.com/watch?v=pK7W5npkhho&start=2201) session video from Google I/O 2017, beginning at 36:41.



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
