---
url: https://developer.android.com/build/android-settings-plugin/
title: Configure project-wide build properties with the settings plugin \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:23.206018+00:00
---

# Configure project-wide build properties with the settings plugin  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/build/android-settings-plugin/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Gradle build guides ](https://developer.android.com/build/gradle-build-overview)



#  Configure project-wide build properties with the settings plugin Stay organized with collections  Save and categorize content based on your preferences. 

The settings plugin lets you centralize common build properties that apply to all modules in one place so you don't need to copy and paste the configurations across multiple modules.

### Apply the settings plugin

Apply the settings plugin in the `settings.gradle` file. The version must be the same as the AGP version declared in the `libs.versions.toml` file:

### Kotlin
    
    
    pluginManagement {
        // Add the following.
        plugins {
           id("com.android.settings") version "9.4.0" apply false
        }
    }
    
    plugins {
        id("com.android.settings")
    }

### Groovy
    
    
    pluginManagement {
        // Add the following.
        plugins {
           id("com.android.settings") version "9.4.0" apply false
        }
    }
    
    plugins {
        id("com.android.settings")
    }

### Apply build properties

Apply the `android` block in the `settings.gradle` file. Unlike in module-level `build.gradle` files, apply the `minSdk` and `targetSdk` to the top-level `android` block:

### Kotlin
    
    
    android {
        compileSdk {
            version = release(36) {
                minorApiLevel = 1
            }
        }
        minSdk {
            version = release(23)
        }
        targetSdk {
            version = release(36)
        }
    }

### Groovy
    
    
    android {
        compileSdk {
            version = release(36) {
                minorApiLevel = 1
            }
        }
        minSdk {
            version = release(23)
        }
        targetSdk {
            version = release(36)
        }
    }

You should remove these build properties from the module-level `build.gradle` files if you want the versions defined in the `settings.gradle` file to be applied. Keeping these properties in the module-level `build.gradle` files overrides those set in the `settings.gradle` file for that particular module.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
