---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/package-summary/
title: com.android.build.api.instrumentation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:03.742506+00:00
---

# com.android.build.api.instrumentation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/package-summary/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# com.android.build.api.instrumentation

## Interfaces

`[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/AsmClassVisitorFactory)` |  A factory to create class visitor objects to instrument classes.  
---|---  
`[ClassContext](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/ClassContext)` |   
`[ClassData](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/ClassData)` |  Data about the class to be instrumented.  
`[InstrumentationContext](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/InstrumentationContext)` |  Instrumentation context data that will be injected to `[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/AsmClassVisitorFactory)` on instantiation.  
`[InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/InstrumentationParameters)` |  Parameters for a registered `[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/AsmClassVisitorFactory)`.  
  
## Classes

`[InstrumentationParameters.None](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/InstrumentationParameters.None)` |   
---|---  
  
## Enums

`[FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/FramesComputationMode)` |  Indicates the frame computation mode that will be applied to the bytecode of the classes instrumented by ASM visitors registered through `[Component.transformClassesWith](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Component#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))`.  
---|---  
`[InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/instrumentation/InstrumentationScope)` |   
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
