---
url: https://developer.android.com/build/publish-library/configure-test-fixtures/
title: Configure test fixtures for publication \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:29.657753+00:00
---

# Configure test fixtures for publication  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/build/publish-library/configure-test-fixtures/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Gradle build guides ](https://developer.android.com/build/gradle-build-overview)



#  Configure test fixtures for publication Stay organized with collections  Save and categorize content based on your preferences. 

While publishing test fixtures doesn't require any particular configuration of the publication, the [capability mechanism](https://docs.gradle.org/current/userguide/component_capabilities.html) used to handle fixtures does require an additional configuration.

For a given artifact with coordinates `groupId:artifactId:version`, Gradle expects that the test fixtures artifact declares a capability with coordinates `groupId:artifactId-test-fixtures:version`. This is not currently done automatically by either the test fixture support or the Maven Publish Plugin, and therefore must be done manually.

Gradle creates the capability from the project’s name, group, and version. All three must be set up to match the `artifactId`, `groupId`, and `version` set in the publication.

The project’s name is the last segment of its path by default, so the default name of a project with the path `:path:to:mylibrary` is `mylibrary`. If this is not what you want to use for `artifactId`, then you need to change your project name.

There are two options for renaming your project:

  * Rename the folder of the project. This changes the project name, or the Gradle path of the project, so all dependencies on the project need to be updated. While keeping the project name and folder the same might create more reorganization work initially, it reduces confusion.
  * Rename the project in Gradle without renaming the folder of the project. This avoids the impact on source versioning, but it splits the project location and name.



To rename the project in Gradle, insert the following code in the `settings.gradle` file:

### Groovy
    
    
    include ':path:to:mylibrary'
    project(':path:to:mylibrary').name = 'my-library'

### Kotlin
    
    
    include(":path:to:mylibrary")
    project(":path:to:mylibrary").name = "my-library"

This code assigns the new path of the project to `:path:to:my-library`.

The value `groupId` defaults to the build name, which is generally the name of the root folder, and the value `version` is by default unspecified. To change the values of the group ID or version, set the `group` and `version` properties, respectively, in your project-level `build.gradle` file (for Groovy) or `build.gradle.kts` (for Kotlin script):

### Groovy
    
    
    group = 'com.my-company'
    version = '1.0'

### Kotlin
    
    
    group = "com.my-company"
    version = "1.0"

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
