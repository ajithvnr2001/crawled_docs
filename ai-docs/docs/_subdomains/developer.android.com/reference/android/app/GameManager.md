---
url: https://developer.android.com/reference/android/app/GameManager/
title: GameManager \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:29.934398+00:00
---

# GameManager  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/android/app/GameManager/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

Summary: Constants | Methods | Inherited Methods

# GameManager

* * *

[Kotlin](https://developer.android.com/reference/kotlin/android/app/GameManager "View this page in Kotlin") |Java

` public final class GameManager `   
` extends [Object](https://developer.android.com/reference/java/lang/Object) ` ` `

[java.lang.Object](https://developer.android.com/reference/java/lang/Object)  
---  
↳ | android.app.GameManager   
  


* * *

The GameManager allows system apps to modify and query the game mode of apps. 

**Note:** After `[Build.VERSION_CODES.VANILLA_ICE_CREAM](https://developer.android.com/reference/android/os/Build.VERSION_CODES#VANILLA_ICE_CREAM)`, some devices that do not support the GameManager features _may_ not publish a GameManager instance. These device types include: 

  * Wear devices (`[PackageManager.FEATURE_WATCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WATCH)`) 



Therefore, you should always do a `null` check on the return value of `[Context.getSystemService(Class)](https://developer.android.com/reference/android/content/Context#getSystemService\(java.lang.Class<T>\))` and `[Context.getSystemService(String)](https://developer.android.com/reference/android/content/Context#getSystemService\(java.lang.String\))` when trying to obtain an instance of GameManager on the aforementioned device types.

## Summary

### Constants  
  
---  
`int` |  `[GAME_MODE_BATTERY](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_BATTERY)` Battery game mode will save battery and give longer game play time.   
`int` |  `[GAME_MODE_CUSTOM](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_CUSTOM)` Custom game mode that has user-provided configuration overrides.   
`int` |  `[GAME_MODE_PERFORMANCE](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_PERFORMANCE)` Performance game mode maximizes the game's performance.   
`int` |  `[GAME_MODE_STANDARD](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_STANDARD)` Standard game mode means the platform will use the game's default performance characteristics.   
`int` |  `[GAME_MODE_UNSUPPORTED](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_UNSUPPORTED)` Game mode is not supported for this application.   
  
### Public methods  
  
---  
` int` |  ` [getGameMode](https://developer.android.com/reference/android/app/GameManager#getGameMode\(\))() ` Return the user selected game mode for this application.   
` void` |  ` [setGameState](https://developer.android.com/reference/android/app/GameManager#setGameState\(android.app.GameState\))([GameState](https://developer.android.com/reference/android/app/GameState) gameState) ` Called by games to communicate the current state to the platform.   
  
### Inherited methods  
  
---  
From class ` [java.lang.Object](https://developer.android.com/reference/java/lang/Object) ` | ` [Object](https://developer.android.com/reference/java/lang/Object)` |  ` [clone](https://developer.android.com/reference/java/lang/Object#clone\(\))() ` Creates and returns a copy of this object.   
---|---  
` boolean` |  ` [equals](https://developer.android.com/reference/java/lang/Object#equals\(java.lang.Object\))([Object](https://developer.android.com/reference/java/lang/Object) obj) ` Indicates whether some other object is "equal to" this one.   
` void` |  ` [finalize](https://developer.android.com/reference/java/lang/Object#finalize\(\))() ` Called by the garbage collector on an object when garbage collection determines that there are no more references to the object.   
` final [Class](https://developer.android.com/reference/java/lang/Class)<?>` |  ` [getClass](https://developer.android.com/reference/java/lang/Object#getClass\(\))() ` Returns the runtime class of this `Object`.   
` int` |  ` [hashCode](https://developer.android.com/reference/java/lang/Object#hashCode\(\))() ` Returns a hash code value for the object.   
` final void` |  ` [notify](https://developer.android.com/reference/java/lang/Object#notify\(\))() ` Wakes up a single thread that is waiting on this object's monitor.   
` final void` |  ` [notifyAll](https://developer.android.com/reference/java/lang/Object#notifyAll\(\))() ` Wakes up all threads that are waiting on this object's monitor.   
` [String](https://developer.android.com/reference/java/lang/String)` |  ` [toString](https://developer.android.com/reference/java/lang/Object#toString\(\))() ` Returns a string representation of the object.   
` final void` |  ` [wait](https://developer.android.com/reference/java/lang/Object#wait\(long,%20int\))(long timeoutMillis, int nanos) ` Causes the current thread to wait until it is awakened, typically by being _notified_ or _interrupted_ , or until a certain amount of real time has elapsed.   
` final void` |  ` [wait](https://developer.android.com/reference/java/lang/Object#wait\(long\))(long timeoutMillis) ` Causes the current thread to wait until it is awakened, typically by being _notified_ or _interrupted_ , or until a certain amount of real time has elapsed.   
` final void` |  ` [wait](https://developer.android.com/reference/java/lang/Object#wait\(\))() ` Causes the current thread to wait until it is awakened, typically by being _notified_ or _interrupted_.   
  
## Constants

### GAME_MODE_BATTERY

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GAME_MODE_BATTERY

Battery game mode will save battery and give longer game play time.

Constant Value: 3 (0x00000003) 

### GAME_MODE_CUSTOM

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GAME_MODE_CUSTOM

Custom game mode that has user-provided configuration overrides. 

Custom game mode is expected to be handled only by the platform using users' preferred config. It is currently not allowed to opt in custom mode in game mode XML file nor expected to perform app-based optimizations when activated.

Constant Value: 4 (0x00000004) 

### GAME_MODE_PERFORMANCE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GAME_MODE_PERFORMANCE

Performance game mode maximizes the game's performance. 

This game mode is highly likely to increase battery consumption.

Constant Value: 2 (0x00000002) 

### GAME_MODE_STANDARD

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GAME_MODE_STANDARD

Standard game mode means the platform will use the game's default performance characteristics.

Constant Value: 1 (0x00000001) 

### GAME_MODE_UNSUPPORTED

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GAME_MODE_UNSUPPORTED

Game mode is not supported for this application.

Constant Value: 0 (0x00000000) 

## Public methods

### getGameMode

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public int getGameMode ()

Return the user selected game mode for this application. 

An application can use `android:isGame="true"` or `android:appCategory="game"` to indicate that the application is a game. If an application is not a game, always return `[GAME_MODE_UNSUPPORTED](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_UNSUPPORTED)`. 

Developers should call this API every time the application is resumed. 

If a game's `targetSdkVersion` is `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)` or lower, and when the game mode is set to `[GAME_MODE_CUSTOM](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_CUSTOM)` which is available in `[Build.VERSION_CODES.UPSIDE_DOWN_CAKE](https://developer.android.com/reference/android/os/Build.VERSION_CODES#UPSIDE_DOWN_CAKE)` or newer, this API will return `[GAME_MODE_STANDARD](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_STANDARD)` instead for backward compatibility.

Returns  
---  
`int` | Value is one of the following: 

  * `[GAME_MODE_UNSUPPORTED](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_UNSUPPORTED)`
  * `[GAME_MODE_STANDARD](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_STANDARD)`
  * `[GAME_MODE_PERFORMANCE](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_PERFORMANCE)`
  * `[GAME_MODE_BATTERY](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_BATTERY)`
  * `[GAME_MODE_CUSTOM](https://developer.android.com/reference/android/app/GameManager#GAME_MODE_CUSTOM)`

  
  
### setGameState

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public void setGameState ([GameState](https://developer.android.com/reference/android/app/GameState) gameState)

Called by games to communicate the current state to the platform.

Parameters  
---  
`gameState` |  `GameState`: An object set to the current state.   
This value cannot be `null`.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
