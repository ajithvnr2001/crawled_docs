---
url: https://developer.android.com/training/cars/apps/library/connection-api/
title: Connection API \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:07.860255+00:00
---

# Connection API  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/connection-api/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Connection API Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** For apps that use the `CarConnection` API and [target](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) Android 14 (API level 34) and higher, use Car App Library version `1.3.0-beta01` or later. Earlier versions of the library throw an exception on devices running Android 14 or later due to the requirement for [context-registered receivers to specify export behavior](https://developer.android.com/about/versions/14/behavior-changes-14#runtime-receivers-exported).  
  
Regardless of the Car App Library version, for apps that target Android 13 (API level 33) or lower, `CarConnection` API doesn't encounter this issue, even on a device running Android 14 or higher.

To determine if your app is running on Android Auto or Android Automotive OS, use the [`CarConnection` API](https://developer.android.com/reference/androidx/car/app/connection/CarConnection) to retrieve connection information at runtime. For example:

  1. In your car app's `Session`, initialize a `CarConnection` and subscribe to `LiveData` updates:


    
    
    CarConnection(carContext).type.observe(this, ::onConnectionStateUpdated)
    
    [ConnectionApi.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/ConnectionApi.kt#L31-L31)

  1. In the observer, react to changes in the connection state:


    
    
    fun onConnectionStateUpdated(connectionState: Int) {
        val message = when (connectionState) {
            CarConnection.CONNECTION_TYPE_NOT_CONNECTED -> "Not connected to a head unit"
            CarConnection.CONNECTION_TYPE_NATIVE -> "Connected to Android Automotive OS"
            CarConnection.CONNECTION_TYPE_PROJECTION -> "Connected to Android Auto"
            else -> "Unknown car connection type"
        }
        CarToast.makeText(carContext, message, CarToast.LENGTH_SHORT).show()
    }
    
    [ConnectionApi.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/ConnectionApi.kt#L37-L45)

[ Previous arrow_back  Request permissions  ](https://developer.android.com/training/cars/apps/library/request-permissions)

[ Next Constraints API  arrow_forward  ](https://developer.android.com/training/cars/apps/library/constraints-api)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
