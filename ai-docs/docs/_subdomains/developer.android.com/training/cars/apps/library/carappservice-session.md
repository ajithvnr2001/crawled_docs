---
url: https://developer.android.com/training/cars/apps/library/carappservice-session/
title: Create your CarAppService and Session \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:05.082080+00:00
---

# Create your CarAppService and Session  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/carappservice-session/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Create your CarAppService and Session Stay organized with collections  Save and categorize content based on your preferences. 

Your app must extend the [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService) class and implement its [`onCreateSession`](https://developer.android.com/reference/androidx/car/app/CarAppService#onCreateSession\(\)) method, which returns a [`Session`](https://developer.android.com/reference/androidx/car/app/Session) instance that corresponds to the current connection to the host:
    
    
    class HelloWorldService : CarAppService() {
        override fun onCreateSession(sessionInfo: SessionInfo): Session {
            return HelloWorldSession()
        }
        // ...
    }
    
    [CarAppServiceSession.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/CarAppServiceSession.kt#L30-L39)

The `Session` instance returns which [`Screen`](https://developer.android.com/reference/androidx/car/app/Screen) instance to use when the app is started for the first time:
    
    
    class HelloWorldSession : Session() {
        override fun onCreateScreen(intent: Intent): Screen {
            return HelloWorldScreen(carContext)
        }
    }
    
    [CarAppServiceSession.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/CarAppServiceSession.kt#L43-L47)

When your car app must start from a screen that isn't the **Home** or **Landing** screen, such as when handling deep links, you can use [`ScreenManager.push`](https://developer.android.com/reference/androidx/car/app/ScreenManager#push\(androidx.car.app.Screen\)) before returning from [`onCreateScreen`](https://developer.android.com/reference/androidx/car/app/Session#onCreateScreen\(android.content.Intent\)) to pre-seed a back stack of screens. Pre-seeding allows users to navigate back to previous screens from the first screen displayed by your app.

[ Previous arrow_back  Set up your project  ](https://developer.android.com/training/cars/apps/library/set-up-project)

[ Next Create your start screen  arrow_forward  ](https://developer.android.com/training/cars/apps/library/start-screen)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
