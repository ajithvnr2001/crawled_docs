---
url: https://developer.android.com/training/cars/apps/library/start-screen/
title: Create your start screen \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:05.287693+00:00
---

# Create your start screen  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/start-screen/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Create your start screen Stay organized with collections  Save and categorize content based on your preferences. 

To create the screens displayed by your app, you define the classes that extend the `Screen` class and implement its [`onGetTemplate`](https://developer.android.com/reference/androidx/car/app/Screen#onGetTemplate\(\)) method to return the [`Template`](https://developer.android.com/reference/androidx/car/app/model/Template) instance that represents the state of the UI to display in the car screen.

This code snippet shows how to declare a `Screen` that uses a [`PaneTemplate`](https://developer.android.com/reference/androidx/car/app/model/PaneTemplate) template to display a "Hello world!" string:
    
    
    class MyStartScreen(carContext: CarContext) : Screen(carContext) {
        override fun onGetTemplate(): Template {
            val row = Row.Builder().setTitle("Hello world!").build()
            val pane = Pane.Builder().addRow(row).build()
            val header = Header.Builder()
                .setStartHeaderAction(Action.APP_ICON)
                .build()
            return PaneTemplate.Builder(pane)
                .setHeader(header)
                .build()
        }
    }
    
    [StartScreen.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/StartScreen.kt#L29-L40)

[ Previous arrow_back  Create your CarAppService and session  ](https://developer.android.com/training/cars/apps/library/carappservice-session)

[ Next Implement screen navigation  arrow_forward  ](https://developer.android.com/training/cars/apps/library/screen-navigation)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
