---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode/
title: FramesComputationMode \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:33:29.422115+00:00
---

# FramesComputationMode  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# FramesComputationMode

[View Source](https://cs.android.com/search?q=file:com/android/build/api/instrumentation/FramesComputationMode.kt+class:com.android.build.api.instrumentation.FramesComputationMode)

Added in 4.2.0
    
    
    enum [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.instrumentation.FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)  
  
* * *

Indicates the frame computation mode that will be applied to the bytecode of the classes instrumented by ASM visitors registered through `[Component.transformClassesWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Component#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))`.

The default mode is to `[copy frames](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COPY_FRAMES)`.

## Summary

### Enum Values  
  
---  
`[COMPUTE_FRAMES_FOR_ALL_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COMPUTE_FRAMES_FOR_ALL_CLASSES)` |  Stack frames and the maximum stack sizes will be skipped when reading the original classes, and will **not** be computed by `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)`.  
`[COMPUTE_FRAMES_FOR_INSTRUMENTED_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COMPUTE_FRAMES_FOR_INSTRUMENTED_CLASSES)` |  Stack frames and the maximum stack sizes will be skipped when reading the original classes, and will be instead computed from scratch by `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)` based on the classpath of the original classes.  
`[COMPUTE_FRAMES_FOR_INSTRUMENTED_METHODS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COMPUTE_FRAMES_FOR_INSTRUMENTED_METHODS)` |  Stack frames and the maximum stack size will be computed by `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)` for any modified or added methods based on the classpath of the original classes.  
`[COPY_FRAMES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COPY_FRAMES)` |  Stack frames and the maximum stack sizes will be copied from the original classes to the instrumented ones, i.e. frames and maxs will be read and visited by the class visitors and then to the `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)` where they will be written without modification.  
  
### Public functions  
  
---  
`[FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### COMPUTE_FRAMES_FOR_ALL_CLASSES
    
    
    val [FramesComputationMode.COMPUTE_FRAMES_FOR_ALL_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COMPUTE_FRAMES_FOR_ALL_CLASSES): [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)

Stack frames and the maximum stack sizes will be skipped when reading the original classes, and will **not** be computed by `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)`. Instead, when the whole instrumentation process is finished for all the classes, there will be another pass where the frames are computed for all classes based on the classpath of the instrumented classes. This means that the frames will be computed for all classes non-incrementally regardless of which classes changed or which classes were instrumented.

Using this mode will have a large impact on the build speed, use only when it's absolutely necessary.

Use this mode if your instrumentation process requires recomputing frames and/or maxs, and there will be two classes A and B, where the lowest common superclass will **not** be the same before and after instrumentation.

For example, the instrumentation process could be

  * Changing the superclass of a subset of classes, that will result in changing the lowest common superclass of at least two classes.




### COMPUTE_FRAMES_FOR_INSTRUMENTED_CLASSES
    
    
    val [FramesComputationMode.COMPUTE_FRAMES_FOR_INSTRUMENTED_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COMPUTE_FRAMES_FOR_INSTRUMENTED_CLASSES): [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)

Stack frames and the maximum stack sizes will be skipped when reading the original classes, and will be instead computed from scratch by `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)` based on the classpath of the original classes.

Use this mode if your instrumentation process requires recomputing frames and/or maxs for all instrumented classes, and for any two classes A and B, the lowest common superclass will be the same before and after instrumentation.

For example, the instrumentation process could be

  * Injecting code without visiting the frames and/or maxs for the injected code.




### COMPUTE_FRAMES_FOR_INSTRUMENTED_METHODS
    
    
    val [FramesComputationMode.COMPUTE_FRAMES_FOR_INSTRUMENTED_METHODS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COMPUTE_FRAMES_FOR_INSTRUMENTED_METHODS): [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)

Stack frames and the maximum stack size will be computed by `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)` for any modified or added methods based on the classpath of the original classes. This means that neither the maximum stack size nor the stack frames will be computed for methods that are copied as is in the new class.

Use this mode if your instrumentation process requires recomputing frames and/or maxs only for the modified methods in each class.

For example, the instrumentation process could be

  * Injecting code without visiting the frames and/or maxs for the injected code.




### COPY_FRAMES
    
    
    val [FramesComputationMode.COPY_FRAMES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COPY_FRAMES): [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)

Stack frames and the maximum stack sizes will be copied from the original classes to the instrumented ones, i.e. frames and maxs will be read and visited by the class visitors and then to the `[ClassWriter](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassWriter.html)` where they will be written without modification.

This is the fastest mode as it doesn't require computing frames which can be an expensive operation.

Use this mode if your instrumentation process doesn't require recomputing frames or maxs.

For example, the instrumentation process could be

  * Adding an annotation to a method

  * Adding an interface to a class

  * Injecting code and also manually calculating and visiting the frames and maxs for the injected code.




## Public functions

### valueOf

Added in 4.2.0
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`kotlin.IllegalArgumentException` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
