---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LintLifecycleExtension/
title: LintLifecycleExtension \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:37:33.317545+00:00
---

# LintLifecycleExtension  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LintLifecycleExtension/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LintLifecycleExtension

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/LintLifecycleExtension.kt+class:com.android.build.api.variant.LintLifecycleExtension)

Added in 7.1.0
    
    
    interface [LintLifecycleExtension](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/LintLifecycleExtension) : [DslLifecycle](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslLifecycle)

* * *

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.variant.DslLifecycle](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslLifecycle) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslLifecycle#finalizeDsl\(org.gradle.api.Action\))(callback: [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)<[Lint](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Lint)>)` `[Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html)` based version of `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))` above.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[finalizeDsl](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DslLifecycle#finalizeDsl\(kotlin.Function1\))(callback: ([Lint](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/Lint)) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` API to customize the DSL Objects programmatically after they have been evaluated from the build files and before used in the build process next steps like variant or tasks creation.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
