---
url: https://developer.android.com/topic/performance/baselineprofiles/confirm-startup-profiles/
title: Confirm Startup Profiles optimization \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:05.462026+00:00
---

# Confirm Startup Profiles optimization  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/baselineprofiles/confirm-startup-profiles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Confirm Startup Profiles optimization Stay organized with collections  Save and categorize content based on your preferences. 

You can check that your Startup Profiles are working using either Android Studio or looking at the R8 build metadata.

## Confirm with Android Studio

To confirm DEX layout optimization, use Android Studio to open the APK and verify the classes in the DEX files. Make sure the primary `classes.dex` isn't completely filled. If your app consists of a single DEX file, you can check whether the app contains two DEX files after enabling the Startup Profile.

Android Studio warns you if the startup classes don't fit in a single DEX file. To get diagnostic information that includes the amount of non-startup methods in the startup classes, make sure the R8 compiler is updated to at least version 8.3.21 by making the following changes to the `settings.gradle` file when you apply the Startup Profile:

### Kotlin
    
    
    pluginManagement {
        buildscript {
            repositories {
                mavenCentral()
                maven {
                    url = uri("https://storage.googleapis.com/r8-releases/raw")
                }
            }
            dependencies {
                classpath("com.android.tools:r8:8.3.21")
            }
        }
    }

### Groovy
    
    
    pluginManagement {
        buildscript {
            repositories {
                mavenCentral()
                maven {
                    url uri('https://storage.googleapis.com/r8-releases/raw')
                }
            }
            dependencies {
                classpath 'com.android.tools:r8:8.3.6-dev"
            }
        }
    }

Make sure you add `--info` after `assembleRelease` in the following command when building with Gradle.
    
    
    ./gradlew assembleRelease --info
    

The diagnostic is then printed to the terminal.

If your app or any libraries reference any [desugared APIs](https://developer.android.com/studio/write/java8-support#library-desugaring), the bundled compatibility implementations of these classes are always contained in the last DEX file. This desugared last DEX file doesn't participate in DEX layout optimizations.

## Confirm with bundle metadata

**Note:** This workflow has only been tested on Linux.

Starting with AGP 8.8, R8 outputs metadata in your Android App Bundle (AAB) that you can use to check if the DEX layout optimization was successful. To check if the optimization worked, do the following:

  1. Build your app's AAB:
         
         ./gradlew app:bundleRelease
         

  2. Check that there's at least one DEX file that contains the text `"startup": true`.

     1. Open the metadata:
            
            unzip -j -o path-to-aab BUNDLE-METADATA/com.android.tools/r8.json && jq .dexFiles r8.json
            

The path to your AAB might be something like `app/build/outputs/bundle/release/app-release.aab`.

     2. Check the output, which should look something like this:
            
            inflating: r8.json
            [
              {
                "checksum": "f0b4b0ddb295812607f44efe03cf7a830056ccfddbdb81db3760d2281940e951",
                "startup": true
              }
            ]
            

If you only see `"startup": false` in the metadata, you need to [enable startup profiles](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations#create-startup) and ensure that your startup profile isn't obfuscated.

  3. Check that the SHA-256 values from the metadata match those from the AAB. To get the SHA-256 values for all your DEX files run the following:
         
         unzip -o path-to-aab */dex/*.dex && sha256sum */dex/*
         

The output should look something like this:
         
         Archive: app/build/outputs/bundle/release/myapp-release.aab
           inflating: base/dex/classes.dex
         f0b4b0ddb295812607f44efe03cf7a830056ccfddbdb81db3760d2281940e951  base/dex/classes.dex
         

Compare the hash values to the "checksum" values from step 1. If the SHA-256 values don't match, there might be a compilation step interfering with R8's ability to output DEX files.




[ Previous arrow_back  Create Startup Profiles  ](https://developer.android.com/topic/performance/startupprofiles/dex-layout-optimizations)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
