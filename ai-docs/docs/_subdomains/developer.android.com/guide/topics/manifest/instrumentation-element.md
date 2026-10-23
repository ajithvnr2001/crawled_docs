---
url: https://developer.android.com/guide/topics/manifest/instrumentation-element/
title: <instrumentation> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:21.078751+00:00
---

# <instrumentation>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/instrumentation-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <instrumentation> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <instrumentation android:functionalTest=["true" | "false"]
                     android:handleProfiling=["true" | "false"]
                     android:icon="_drawable resource_"
                     android:label="_string resource_"
                     android:name="_string_ "
                     android:targetPackage="_string_ "
                     android:targetProcesses="_string_ " />

contained in:
    `[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)`
description:
    Declares an `[Instrumentation](https://developer.android.com/reference/android/app/Instrumentation)` class that lets you monitor an application's interaction with the system. The `Instrumentation` object is instantiated before any of the application's components.
attributes:
    

`android:functionalTest`
    Whether the `Instrumentation` class runs as a functional test. This is `true` if it does and `false` if not. The default value is `false`.
`android:handleProfiling`
    Whether the `Instrumentation` object turns profiling on and off. This is `true` if it determines when profiling starts and stops and `false` if profiling continues the entire time it is running. A value of `true` enables the object to target profiling at a specific set of operations. The default value is `false`.
`android:icon`
    An icon that represents the `Instrumentation` class. This attribute must be set as a reference to a drawable resource.
`android:label`
    A user-readable label for the `Instrumentation` class. The label can be set as a raw string or a reference to a string resource.
`android:name`
    The name of the `Instrumentation` subclass. Use a fully qualified class name, such as `com.example.project.StringInstrumentation`. However, as a shorthand, if the first character of the name is a period, it is appended to the package name specified in the `[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)` element. 

There is no default. The name must be specified. 

`android:targetPackage`
    The application that the `Instrumentation` object runs against. An application is identified by the package name assigned in its manifest file by the `<manifest>` element.
`android:targetProcesses`
    

The processes that the `Instrumentation` object runs against. A comma-separated list indicates that the instrumentation runs against those specific processes. A value of `"*"` indicates that the instrumentation runs against all processes of the app defined in `android:targetPackage`.

If this value isn't provided in the manifest, the instrumentation runs only against the main process of the app defined in `android:targetPackage`.

This attribute was added in API level 26.

introduced in:
    API level 1

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
