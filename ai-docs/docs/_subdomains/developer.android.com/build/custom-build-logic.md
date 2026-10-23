---
url: https://developer.android.com/build/custom-build-logic/
title: Apply custom build logic \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:20.029734+00:00
---

# Apply custom build logic  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/build/custom-build-logic/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Gradle build guides ](https://developer.android.com/build/gradle-build-overview)



#  Apply custom build logic Stay organized with collections  Save and categorize content based on your preferences. 

This section describes advanced topics that are useful when you want to extend the Android Gradle plugin or write your own plugin.

## Publish variant dependencies to custom logic

A library can have functionalities that other projects or sub-projects might want to use. Publishing a library is the process by which the library is made available to its consumers. Libraries can control which dependencies its consumers have access to at compile time and runtime.

There are two separate configurations that hold the transitive dependencies of each classpath which must be used by consumers to consume the library as described below:

  * `variant_nameApiElements`: This configuration holds the transitive dependencies that are available to consumers at compile time.
  * `variant_nameRuntimeElements`: This configuration holds the transitive dependencies that are available to consumers at runtime.



To learn more about the relationships between the different configurations, go to [The Java Library plugin configurations](https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_configurations_graph).

## Custom dependency resolution strategies

A project may include a dependency on two different versions of the same library which can lead to dependency conflicts. For example, if your project depends on version 1 of module A and version 2 of module B, and module A transitively depends on version 3 of module B, there arises a dependency version conflict.

To resolve this conflict, the Android Gradle plugin uses the following dependency resolution strategy: when the plugin detects that different versions of the same module are in the dependency graph, by default, it chooses the one with the highest version number.

However, this strategy might not always work as you intend. To customize the dependency resolution strategy, use the following configurations to resolve specific dependencies of a variant that are needed for your task:

  * `variant_nameCompileClasspath`: This configuration contains the resolution strategy for a given variant’s compile classpath.
  * `variant_nameRuntimeClasspath`: This configuration contains the resolution strategy for a given variant’s runtime classpath.



The Android Gradle plugin includes getters that you can use to access the configuration objects of each variant. Thus, you can use the variant API to query the dependency resolution as shown in the example below:

### Kotlin
    
    
    android {
        applicationVariants.all {
            // Return compile configuration objects of a variant.
            compileConfiguration.resolutionStrategy {
            // Use Gradle's [ResolutionStrategy API](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.ResolutionStrategy.html)
            // to customize how this variant resolves dependencies.
                ...
            }
            // Return runtime configuration objects of a variant.
            runtimeConfiguration.resolutionStrategy {
                ...
            }
            // Return annotation processor configuration of a variant.
            annotationProcessorConfiguration.resolutionStrategy {
                ...
            }
        }
    }

### Groovy
    
    
    android {
        applicationVariants.all { variant ->
            // Return compile configuration objects of a variant.
            variant.getCompileConfiguration().resolutionStrategy {
            // Use Gradle's [ResolutionStrategy API](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.ResolutionStrategy.html)
            // to customize how this variant resolves dependencies.
                ...
            }
            // Return runtime configuration objects of a variant.
            variant.getRuntimeConfiguration().resolutionStrategy {
                ...
            }
            // Return annotation processor configuration of a variant.
            variant.getAnnotationProcessorConfiguration().resolutionStrategy {
                ...
            }
        }
    }

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
