---
url: https://developer.android.com/build/remote-repositories/
title: Manage remote repositories \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:23.457429+00:00
---

# Manage remote repositories  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/build/remote-repositories/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Gradle build guides ](https://developer.android.com/build/gradle-build-overview)



#  Manage remote repositories Stay organized with collections  Save and categorize content based on your preferences. 

When your dependency is something other than a local library or file tree, Gradle looks for the files in whichever online repositories are specified in the `dependencyResolutionManagement { repositories {...} }` block of your `settings.gradle` file. The order in which you list each repository determines the order in which Gradle searches the repositories for each project dependency. For example, if a dependency is available from both repository A and B, and you list A first, Gradle downloads the dependency from repository A.

By default, new Android Studio projects specify Google's Maven repository, and the [Maven central repository](https://search.maven.org/) as repository locations in the project's `settings.gradle` file, as shown below:

### Kotlin
    
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
        }
    }

### Groovy
    
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
        }
    }

**Warning:** The JCenter repository, which was included by default in the past, became read-only on March 31st, 2021. For more information, see [JCenter service update](https://developer.android.com/studio/build/jcenter-migration).

If you want something from a local repository use `mavenLocal()`:

### Kotlin
    
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
            mavenLocal()
        }
    }

### Groovy
    
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
            mavenLocal()
        }
    }

Or you can declare specific Maven or Ivy repositories as follows:

### Kotlin
    
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            maven(url = "https://repo.example.com/maven2")
            maven(url = "file://local/repo/")
            ivy(url = "https://repo.example.com/ivy")
        }
    }

### Groovy
    
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            maven {
                url 'https://repo.example.com/maven2'
            }
            maven {
                url 'file://local/repo/'
            }
            ivy {
                url 'https://repo.example.com/ivy'
            }
        }
    }

For more information, see the [Gradle Repositories guide](https://docs.gradle.org/current/userguide/dependency_management.html#sec:repositories).

## Google's Maven repository

The most recent versions of the following Android libraries are available from Google's Maven repository:

  * [AndroidX Libraries](https://developer.android.com/jetpack/androidx)
  * [Architecture Components Library](https://developer.android.com/topic/libraries/architecture)
  * [Constraint Layout Library](https://developer.android.com/training/constraint-layout)
  * [AndroidX Test](https://developer.android.com/training/testing)
  * [Databinding Library](https://developer.android.com/topic/libraries/data-binding)
  * [Android Instant App Library](https://developer.android.com/topic/instant-apps)
  * [Wear OS](https://developer.android.com/training/building-wearables)
  * [Google Play services](https://developers.google.com/android/guides/setup)
  * [Google Play Billing Library](https://developer.android.com/google/play/billing)
  * [Firebase](https://firebase.google.com/docs/android/setup)



You can see all available artifacts at [Google's Maven repository index](https://maven.google.com) (see below for programmatic access).

To add one of these libraries to your build, include Google's Maven repository in your top-level `build.gradle.kts` file:

### Kotlin
    
    
    dependencyResolutionManagement {
    
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
    
            // If you're using a version of Gradle lower than 4.1, you must instead use:
            // maven {
            //     url = "https://maven.google.com"
            // }
            // An alternative URL is "https://dl.google.com/dl/android/maven2/".
        }
    }

### Groovy
    
    
    dependencyResolutionManagement {
    
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
    
            // If you're using a version of Gradle lower than 4.1, you must instead use:
            // maven {
            //     url 'https://maven.google.com'
            // }
            // An alternative URL is 'https://dl.google.com/dl/android/maven2/'.
        }
    }

Then add the desired library to your module's `dependencies` block. For example,the [appcompat library](https://developer.android.com/jetpack/androidx/releases/appcompat) looks like this:

### Kotlin
    
    
    dependencies {
        implementation("com.android.support:appcompat-v7:28.0.0")
    }

### Groovy
    
    
    dependencies {
        implementation 'androidx.appcompat:appcompat:1.7.0'
    }

However, if you're trying to use an older version of the above libraries and your dependency fails, then it's not available in the Maven repository and you must instead get the library from the offline repository.

### Programmatic access

For programmatic access to Google's Maven artifacts, you can get an XML list of artifact groups from [maven.google.com/master-index.xml](https://maven.google.com/master-index.xml). Then, for any group, you can view its library names and versions at:

_maven.google.com/ group_path/group-index.xml_

For example, libraries in the android.arch.lifecycle group are listed at [maven.google.com/android/arch/lifecycle/group-index.xml](https://maven.google.com/android/arch/lifecycle/group-index.xml).

You can also download the POM and JAR files at:

_maven.google.com/ group_path/library/version /library-version.ext_

For example: [maven.google.com/android/arch/lifecycle/compiler/1.0.0/compiler-1. 0.0.pom](https://maven.google.com/android/arch/lifecycle/compiler/1.0.0/compiler-1.0.0.pom).

### Offline repository from SDK Manager

For libraries not available from the Google Maven repository (usually older library versions), you must download the offline **Google Repository** package from the [SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager).

Then you can add these libraries to your `dependencies` block as usual.

The offline libraries are saved in `android_sdk/extras/`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
