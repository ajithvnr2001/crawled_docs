---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice/
title: ManagedVirtualDevice \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:54:31.117823+00:00
---

# ManagedVirtualDevice  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ManagedVirtualDevice

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/ManagedVirtualDevice.kt+class:com.android.build.api.dsl.ManagedVirtualDevice)

Added in 4.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [ManagedVirtualDevice](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice) : [Device](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Device)

* * *

Device type for emulators to be managed by the Android Gradle Plugin.

When a device group containing this device is run for tests, Gradle will:

  1. Automatically start up an emulator matching the device definition. Including downloading any and all required system image files and creating the avd.

  2. Run the tests on this device.

  3. Close the emulator upon completion.




These APIs are experimental and may change without notice.

## Summary

### Nested types  
  
---  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
enum [ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)` Defines possible system image selection strategies based on the requested Page Alignment  
  
### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[apiLevel](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#apiLevel\(\))` The api level of Android to be run on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[apiPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#apiPreview\(\))` The sdk version code of Android to be run on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[device](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#device\(\))` The hardware profile of the device to be emulated.  
`[ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)` |  `[pageAlignment](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#pageAlignment\(\))` What size pages the device should be aligned to.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[require64Bit](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#require64Bit\(\))` Whether the image must be a 64 bit image.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[sdkExtensionVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkExtensionVersion\(\))` The extension version of the system image to be run on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))` The SDK version code of Android to be run on the device.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))` The SDK version of Android to be run on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[systemImageSource](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#systemImageSource\(\))` Which source the system image should come from.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[testedAbi](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#testedAbi\(\))` What abi the apk should be built with to test against.  
  
### Inherited functions  
  
---  
From [com.android.build.api.dsl.Device](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Device) | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
@[Internal](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/Internal.html)  
[getName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Device#getName\(\))()`  
---|---  
  
## Public properties

### apiLevel

Added in 4.2.0
    
    
    var [apiLevel](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#apiLevel\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The api level of Android to be run on the device. This annotation is deprecated, use `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))` instead.

This specifies the sdk version of the device. Setting this value will override previous calls of `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))`, `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))`, and `[apiPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#apiPreview\(\))`.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html) for a list of valid values.

### apiPreview

Added in 8.0.2
    
    
    var [apiPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#apiPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The sdk version code of Android to be run on the device. This annotation is deprecated, use `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))` instead.

Setting this it will override previous calls of `[apiLevel](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#apiLevel\(\))`, `[apiPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#apiPreview\(\))`, `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))`, and `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))` setters.

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html) for a list of valid values.

### device

Added in 4.2.0
    
    
    var [device](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#device\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The hardware profile of the device to be emulated.

### pageAlignment

Added in 8.9.0
    
    
    var [pageAlignment](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#pageAlignment\(\)): [ManagedVirtualDevice.PageAlignment](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment)

What size pages the device should be aligned to.

By default, the system image that is validated against Google apis will be chosen. At present (api 35 or below) that is the 4KB page size system image. Newer apis will emit a warning when `[PageAlignment.DEFAULT_FOR_SDK_VERSION](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice.PageAlignment#DEFAULT_FOR_SDK_VERSION)` is chosen (as we will not be able to properly determine the validated image when offline.)

### require64Bit

Added in 7.2.0
    
    
    var [require64Bit](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#require64Bit\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether the image must be a 64 bit image. Defaults to false.

On x86_64 machines: When false, the managed device will use the 32 bit image if available with the given api level and source, otherwise the 64 bit image will be used. When true, the 64 image must be used and setup will fail if an appropriate image does not exist. On arm machines: The value of this parameter has no effect. An arm64 image is always selected.

### sdkExtensionVersion

Added in 8.9.0
    
    
    var [sdkExtensionVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkExtensionVersion\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The extension version of the system image to be run on the device.

By default, the basic system image will be chosen for the given `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))`.

### sdkPreview

Added in 8.9.0
    
    
    var [sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The SDK version code of Android to be run on the device.

Setting this value will override previous calls of `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))` or `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))` setters. Only one of `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))` and `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))` should be set

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html) for a list of valid values.

### sdkVersion

Added in 8.9.0
    
    
    var [sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The SDK version of Android to be run on the device.

Setting this value will override previous calls of `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))` or `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))` setters. Only one of `[sdkVersion](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkVersion\(\))` and `[sdkPreview](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#sdkPreview\(\))` should be set

See [uses-sdk element documentation](http://developer.android.com/guide/topics/manifest/uses-sdk-element.html) for a list of valid values.

### systemImageSource

Added in 4.2.0
    
    
    var [systemImageSource](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#systemImageSource\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Which source the system image should come from. Either "google", "google-atd", "aosp", or "aosp-atd". You can also specify an explicit source such as "google_apis_playstore".

"google", the default, will select Google APIs images for the device. "google-atd" will use automated test device images from Google APIs. "aosp" will use the Android Open Source Project images for the device. "aosp-atd" will use automated test device image from the Android Open Source Project.

### testedAbi

Added in 8.11.0
    
    
    var [testedAbi](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/ManagedVirtualDevice#testedAbi\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

What abi the apk should be built with to test against.

This changes the abi of the testedApk to be installed on the given managed device. This should be changed to test native code. If the abi is not compatible with the system image, this will result in a failure.

The default is for the abi to match the abi of the system image (which is selected based on the abi of the host system). Certain system image sources, such as "google" or "google_apis_playstore" support NDK translation. This allows for the "arm64-v8a" apks to be installed and run on an "x86_64" system image.

Valid values include "x86", "x86_64", and "arm64-v8a"

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
