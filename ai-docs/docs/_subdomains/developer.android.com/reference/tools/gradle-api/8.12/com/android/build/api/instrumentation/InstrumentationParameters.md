---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters/
title: InstrumentationParameters \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:04:50.188459+00:00
---

# InstrumentationParameters  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# InstrumentationParameters

[View Source](https://cs.android.com/search?q=file:com/android/build/api/instrumentation/InstrumentationParameters.kt+class:com.android.build.api.instrumentation.InstrumentationParameters)

Added in 4.2.0
    
    
    interface [InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters) : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

Known direct subclasses 

[InstrumentationParameters.None](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters.None)

`[InstrumentationParameters.None](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters.None)` |   
---|---  
  
* * *

Parameters for a registered `[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/AsmClassVisitorFactory)`.

Build authors should extend this interface with any additional inputs needed for their ASM visitor, or use `[InstrumentationParameters.None](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters.None)` if no parameters are needed.

The parameters will be instantiated using `[ObjectFactory.newInstance](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#newInstance-java.lang.Class\[TypeParam\(bounds=\[kotlin.Any\]\)\]-kotlin.Array\[kotlin.Any\]-)`, configured using the given config when registering the visitor, and injected to the factory on instantiation.

The parameters will be used as Gradle inputs. Make sure to declare the inputs by annotating them using Gradle's input annotations so that it's compatible with Gradle's up-to-date checks.

Example:
    
    
    interface ParametersImpl : InstrumentationParameters {  
      @get:Input  
      val intValue: Property<Int>  
      
      @get:Internal  
      val listOfStrings: ListProperty<String>  
    }  
      
    androidComponents {  
        onVariants(selector().all(), {  
            instrumentation.transformClassesWith(AsmClassVisitorFactoryImpl.class,  
                                                 InstrumentationScope.Project) { params ->  
                 // parameters configuration  
                 params.intValue.set(1)  
                 params.listOfStrings.set(listOf("a", "b"))  
            }  
        })  
    }

## Summary

### Nested types  
  
---  
`class [InstrumentationParameters.None](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters.None) : [InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/instrumentation/InstrumentationParameters)`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
