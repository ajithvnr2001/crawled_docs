---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild/
title: NdkBuild \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:13:31.857041+00:00
---

# NdkBuild  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# NdkBuild

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/NdkBuild.kt+class:com.android.build.api.dsl.NdkBuild)

Added in 4.2.0
    
    
    interface [NdkBuild](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild)

* * *

DSL object for per-module ndk-build configurations, such as the path to your `Android.mk` build script and external native build output directory.

To include ndk-build projects in your Gradle build, you need to use Android Studio 2.2 and higher with Android plugin for Gradle 2.2.0 and higher. To learn more about Android Studio's support for external native builds, read [Add C and C++ Code to Your Project](https://developer.android.com/studio/projects/add-native-code.html)

If you want to instead build your native libraries using CMake, see `[Cmake](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Cmake)`

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[buildStagingDirectory](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#buildStagingDirectory\(kotlin.Any\))(any: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Specifies the path to your external native build output directory.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[path](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#path\(kotlin.Any\))(any: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html))` Specifies the relative path to your `Android.mk` build script.  
  
### Public properties  
  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[buildStagingDirectory](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#buildStagingDirectory\(\))` Specifies the path to your external native build output directory.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[path](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#path\(\))` Specifies the relative path to your `Android.mk` build script.  
  
## Public functions

### buildStagingDirectory

Added in 4.2.0
    
    
    fun [buildStagingDirectory](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#buildStagingDirectory\(kotlin.Any\))(any: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies the path to your external native build output directory.

If you do not specify a value for this property, the Android plugin uses the `<project_dir>/.cxx/` directory by default.

If you specify a path that does not exist, the Android plugin creates it for you. Relative paths are relative to the `build.gradle` file, as shown below:
    
    
    android {  
        externalNativeBuild {  
            ndkBuild {  
                // Tells Gradle to put outputs from external native  
                // builds in the path specified below.  
                buildStagingDirectory "./outputs/ndk-build"  
            }  
        }  
    }

If you specify a path that's a subdirectory of your project's temporary `build` directory, you get a build error. That's because files in this directory do not persist through clean builds. So, you should either keep using the default `<project_dir>/.cxx/` directory or specify a path outside the temporary build directory.

since 4.0.0

### path

Added in 4.2.0
    
    
    fun [path](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#path\(kotlin.Any\))(any: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies the relative path to your `Android.mk` build script.

For example, if your ndk-build script is in the same folder as your project-level `build.gradle` file, you simply pass the following:
    
    
    android {  
        externalNativeBuild {  
            ndkBuild {  
                // Tells Gradle to find the root ndk-build script in the same  
                // directory as the project's build.gradle file. Gradle requires this  
                // build script to add your ndk-build project as a build dependency and  
                // pull your native sources into your Android project.  
                path "Android.mk"  
            }  
        }  
    }

since 4.0.0

## Public properties

### buildStagingDirectory

Added in 4.2.0
    
    
    var [buildStagingDirectory](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#buildStagingDirectory\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

Specifies the path to your external native build output directory.

If you do not specify a value for this property, the Android plugin uses the `<project_dir>/.cxx/` directory by default.

If you specify a path that does not exist, the Android plugin creates it for you. Relative paths are relative to the `build.gradle` file, as shown below:
    
    
    android {  
        externalNativeBuild {  
            ndkBuild {  
                // Tells Gradle to put outputs from external native  
                // builds in the path specified below.  
                buildStagingDirectory "./outputs/ndk-build"  
            }  
        }  
    }

If you specify a path that's a subdirectory of your project's temporary `build` directory, you get a build error. That's because files in this directory do not persist through clean builds. So, you should either keep using the default `<project_dir>/.cxx/` directory or specify a path outside the temporary build directory.

since 3.0.0

### path

Added in 4.2.0
    
    
    var [path](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/NdkBuild#path\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

Specifies the relative path to your `Android.mk` build script.

For example, if your ndk-build script is in the same folder as your project-level `build.gradle` file, you simply pass the following:
    
    
    android {  
        externalNativeBuild {  
            ndkBuild {  
                // Tells Gradle to find the root ndk-build script in the same  
                // directory as the project's build.gradle file. Gradle requires this  
                // build script to add your ndk-build project as a build dependency and  
                // pull your native sources into your Android project.  
                path "Android.mk"  
            }  
        }  
    }

since 2.2.0

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
