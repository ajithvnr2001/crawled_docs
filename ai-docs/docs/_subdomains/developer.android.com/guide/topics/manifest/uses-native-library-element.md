---
url: https://developer.android.com/guide/topics/manifest/uses-native-library-element/
title: <uses-native-library> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:28.665853+00:00
---

# <uses-native-library>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/uses-native-library-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <uses-native-library> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <uses-native-library
      android:name="string"
      android:required=["true" | "false"] />

contained in:
     ` [<application>](https://developer.android.com/guide/topics/manifest/application-element) `
description:
    

Specifies a [vendor-provided shared native library](https://source.android.com/devices/tech/config/namespaces_libraries#adding-additional-native-libraries) that the application must be linked against. This element tells the system to make the native library accessible for the package. 

NDK libraries are by default accessible and therefore don't require the `<uses-native-library>` tag. 

Non-NDK native shared libraries that are provided by silicon vendors or device manufacturers aren't accessible by default if the app targets Android 12 (API level 31) or higher. The libraries are accessible only when they are explicitly requested using the `<uses-native-library>` tag. 

If the app targets Android 11 (API level 30) or lower, the `<uses-native-library>` tag isn't required. In that case, any native shared library is accessible regardless of whether it is an NDK library. 

This element also affects the installation of the application on a particular device. If this element is present and its `android:required` attribute is set to `true`, the `[PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)` framework won't let a user install the application unless the library is present on the user's device. 

The `android:required` attribute is described in detail in the following section. 

attributes:
    

`android:name`
     The name of the library file. 
`android:required`
     Boolean value that indicates whether the application requires the library specified by `android:name`. 

  * `"true"`: the application doesn't function without this library. The system doesn't let the application install on a device that doesn't have the library. 
  * `"false"`: the application uses the library if present, but is designed to function without it if necessary. The system lets the application install, even if the library isn't present. If you use `"false"`, you are responsible for gracefully handling the absence of the library. 



The default is `"true"`. 

introduced in:
    API level 31
see also:
    

  * `[PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)`
  * `[<uses-library>](https://developer.android.com/guide/topics/manifest/uses-library-element)`



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
