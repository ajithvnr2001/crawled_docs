---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion/
title: AndroidPluginVersion \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:40:59.660976+00:00
---

# AndroidPluginVersion  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AndroidPluginVersion

[View Source](https://cs.android.com/search?q=file:com/android/build/api/AndroidPluginVersion.kt+class:com.android.build.api.AndroidPluginVersion)

Added in 7.0.0
    
    
    class [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion) : [Comparable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-comparable/index.html)

* * *

Represents a version of the Android Gradle Plugin

Designed for plugin authors to compare the currently running plugin version, so implements comparable.

For example `AndroidPluginVersion(7, 0)` refers to Android Gradle Plugin version 7.0.0, and `AndroidPluginVersion(7, 0, 1)` refers to Android Gradle Plugin version 7.0.1.

The internal representation is normalized, so that `AndroidPluginVersion(7, 0)` equals `AndroidPluginVersion(7, 0, 0)`

Also supports preview versions through methods `[alpha](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#alpha\(kotlin.Int\))`, `[beta](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#beta\(kotlin.Int\))` and `[rc](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#rc\(kotlin.Int\))` that return the more specific version. For example `AndroidPluginVersion(7, 0).alpha(5)` refers to Android Gradle Plugin version 7.0.0-alpha05. This is for use when developing using incubating APIs that have changed between preview releases of the Android Gradle Plugin. Once those APIs are stable in a stable version of Android Gradle Plugin, it's recommended to drop support for the preview versions. For example, if a new API was introduced in 7.0.0-alpha05, you can test for that using

```if (androidComponents.pluginVersion >= AndroidPluginVersion(7, 0).alpha(5)) { ... }```

If that API is marked as stable in 7.0.0, drop support for the preview versions before it by updating your condition to:

```if (androidComponents.pluginVersion >= AndroidPluginVersion(7, 0)) { ... }```

Take care with maximum version checks to avoid excluding point releases. For example, if a behavior is only applicable for AGP 8.7 series, and you have a different code path for the following version, don't check for 8.7.0 as the maximum, as your plugin will break on point releases of 8.7.0, instead compare with an exclusive bound with the first alpha of the subsequent major-minor version. (This applies even if the alpha is never released as it turned out to be a major version)

```if (androidComponents.pluginVersion < AndroidPluginVersion(8, 8).alpha(1)) { ... }```

## Summary

### Public companion functions  
  
---  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` |  `[getCurrent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#getCurrent\(\))()` Returns the current version of the Android Gradle Plugin.  
  
### Public constructors  
  
---  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#AndroidPluginVersion\(kotlin.Int,kotlin.Int\))(major: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), minor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Create an AndroidPluginVersion with the given major and minor version.  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#AndroidPluginVersion\(kotlin.Int,kotlin.Int,kotlin.Int\))(major: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), minor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), micro: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Create an AndroidPluginVersion with the given major, minor and micro version.  
  
### Public functions  
  
---  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` |  `[alpha](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#alpha\(kotlin.Int\))(alpha: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` returns an alpha version.  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` |  `[beta](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#beta\(kotlin.Int\))(beta: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` returns a beta version.  
`open operator [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[compareTo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#compareTo\(com.android.build.api.AndroidPluginVersion\))(other: [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion))`  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` |  `[dev](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#dev\(\))()` From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` specify an internal development version.  
`open operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[equals](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#equals\(kotlin.Any\))(other: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?)`  
`open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[hashCode](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#hashCode\(\))()`  
`[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` |  `[rc](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#rc\(kotlin.Int\))(rc: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` returns a release candidate version.  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[toString](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#toString\(\))()`  
  
### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[major](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#major\(\))` The major version.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[micro](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#micro\(\))` The micro, or patch version.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[minor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#minor\(\))` The minor version.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[preview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#preview\(\))` The preview version.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[previewType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#previewType\(\))` The type of preview version.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[version](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#version\(\))` Returns the string representing this AGP version in maven version form.  
  
## Public companion functions

### getCurrent

Added in 8.3.1
    
    
    fun [getCurrent](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#getCurrent\(\))(): [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)

Returns the current version of the Android Gradle Plugin.

## Public constructors

### AndroidPluginVersion

Added in 7.0.0
    
    
    [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#AndroidPluginVersion\(kotlin.Int,kotlin.Int\))(major: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), minor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))

Create an AndroidPluginVersion with the given major and minor version.

For example `AndroidPluginVersion(7, 0)` refers to Android Gradle Plugin version 7.0.0.

### AndroidPluginVersion

Added in 7.0.0
    
    
    [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#AndroidPluginVersion\(kotlin.Int,kotlin.Int,kotlin.Int\))(major: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), minor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), micro: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))

Create an AndroidPluginVersion with the given major, minor and micro version.

For example `AndroidPluginVersion(7, 0, 1)` refers to Android Gradle Plugin version 7.0.1.

## Public functions

### alpha

Added in 7.0.0
    
    
    fun [alpha](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#alpha\(kotlin.Int\))(alpha: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)

From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` returns an alpha version.

For example `AndroidPluginVersion(7, 0).alpha(5)` refers to Android Gradle Plugin version 7.0.0-alpha05.

### beta

Added in 7.0.0
    
    
    fun [beta](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#beta\(kotlin.Int\))(beta: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)

From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` returns a beta version.

For example `AndroidPluginVersion(7, 0).beta(2)` refers to Android Gradle Plugin version 7.0.0-beta02.

### compareTo

Added in 7.0.0
    
    
    open operator fun [compareTo](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#compareTo\(com.android.build.api.AndroidPluginVersion\))(other: [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### dev

Added in 7.0.0
    
    
    fun [dev](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#dev\(\))(): [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)

From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` specify an internal development version.

`-dev` versions are never publicly released, but this can be useful if you are building the Android Gradle Plugin from source.

For example `AndroidPluginVersion(7, 0).dev()` refers to Android Gradle Plugin version 7.0.0-dev.

### equals
    
    
    open operator fun [equals](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#equals\(kotlin.Any\))(other: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### hashCode
    
    
    open fun [hashCode](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#hashCode\(\))(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### rc

Added in 7.0.0
    
    
    fun [rc](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#rc\(kotlin.Int\))(rc: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)

From a stable `[AndroidPluginVersion](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion)` returns a release candidate version.

For example `AndroidPluginVersion(7, 0).rc(1)` refers to Android Gradle Plugin version 7.0.0-rc01.

### toString
    
    
    open fun [toString](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#toString\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

## Public properties

### major

Added in 7.0.0
    
    
    val [major](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#major\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The major version.

e.g. 7 for Android Gradle Plugin Version 7.0.1

### micro

Added in 7.0.0
    
    
    val [micro](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#micro\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The micro, or patch version.

e.g. 1 for Android Gradle Plugin Version 7.0.1

### minor

Added in 7.0.0
    
    
    val [minor](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#minor\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The minor version.

e.g. 0 for Android Gradle Plugin Version 7.0.1

### preview

Added in 7.0.0
    
    
    val [preview](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#preview\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

The preview version.

e.g. 5 for Android Gradle Plugin Version 7.0.0-alpha05

### previewType

Added in 7.0.0
    
    
    val [previewType](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#previewType\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The type of preview version.

Null in the case of a stable version. One of 'alpha', 'beta', 'rc', 'dev' for preview versions.

e.g. 'alpha' for Android Gradle Plugin Version 7.0.0-alpha05

### version

Added in 8.4.0
    
    
    val [version](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/AndroidPluginVersion#version\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns the string representing this AGP version in maven version form.

This corresponds exactly to the format of the version of the Android Gradle plugin artifacts published in the Google maven repository.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
