---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation/
title: TransformInvocation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:50.278279+00:00
---

# TransformInvocation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TransformInvocation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/TransformInvocation.java+class:com.android.build.api.transform.TransformInvocation)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [TransformInvocation](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation)

* * *

**This interface is deprecated.**  


An invocation object used to pass of pertinent information for a `[transform](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.TransformInvocation\))` call.

## Summary

### Public functions  
  
---  
`[Context](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Context)!` |  `[getContext](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getContext\(\))()` Returns the context in which the transform is run.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput)!>!` |  `[getInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getInputs\(\))()` Returns the inputs/outputs of the transform.  
`[TransformOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformOutputProvider)!` |  `[getOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getOutputProvider\(\))()` Returns the output provider allowing to create content.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput)!>!` |  `[getReferencedInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getReferencedInputs\(\))()` Returns the referenced-only inputs which are not consumed by this transformation.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[SecondaryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput)!>!` |  `[getSecondaryInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getSecondaryInputs\(\))()` Returns the list of secondary file changes since last.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIncremental](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#isIncremental\(\))()` Indicates whether the transform execution is incremental.  
  
## Public functions

### getContext

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getContext](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getContext\(\))(): [Context](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Context)!

Returns the context in which the transform is run.

Returns  
---  
`[Context](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Context)!` |  the context in which the transform is run.  
  
### getInputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getInputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput)!>!

Returns the inputs/outputs of the transform.

Returns  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput)!>!` |  the inputs/outputs of the transform.  
  
### getOutputProvider

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getOutputProvider\(\))(): [TransformOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformOutputProvider)!

Returns the output provider allowing to create content.

Returns  
---  
`[TransformOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformOutputProvider)!` |  he output provider allowing to create content.  
  
### getReferencedInputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getReferencedInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getReferencedInputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput)!>!

Returns the referenced-only inputs which are not consumed by this transformation.

Returns  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInput)!>!` |  the referenced-only inputs.  
  
### getSecondaryInputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getSecondaryInputs](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#getSecondaryInputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[SecondaryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput)!>!

Returns the list of secondary file changes since last. Only secondary files that this transform can handle incrementally will be part of this change set.

Returns  
---  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[SecondaryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput)!>!` |  the list of changes impacting a `[SecondaryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput)`  
  
### isIncremental

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [isIncremental](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformInvocation#isIncremental\(\))(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Indicates whether the transform execution is incremental.

Returns  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  true for an incremental invocation, false otherwise.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
