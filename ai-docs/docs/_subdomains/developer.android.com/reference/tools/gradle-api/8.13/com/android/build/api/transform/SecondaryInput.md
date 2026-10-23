---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput/
title: SecondaryInput \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:36:46.300717+00:00
---

# SecondaryInput  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SecondaryInput

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/SecondaryInput.java+class:com.android.build.api.transform.SecondaryInput)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    interface [SecondaryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput)

* * *

**This interface is deprecated.**  


Represents a change event for a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryFile)` transform input.

## Summary

### Public functions  
  
---  
`[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryFile)!` |  `[getSecondaryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput#getSecondaryInput\(\))()` The change event subject.  
`[Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!` |  `[getStatus](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput#getStatus\(\))()` The change status.  
  
## Public functions

### getSecondaryInput

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getSecondaryInput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput#getSecondaryInput\(\))(): [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryFile)!

The change event subject.

Returns  
---  
`[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryFile)!` |  an instance of `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryFile)` that represent a transform input file.  
  
### getStatus

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getStatus](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/SecondaryInput#getStatus\(\))(): [Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!

The change status.

Returns  
---  
`[Status](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/Status)!` |  the change status.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
