---
url: https://developer.android.com/training/cars/apps/library/template-restrictions/
title: Template restrictions \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:03.213447+00:00
---

# Template restrictions  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/template-restrictions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Template restrictions Stay organized with collections  Save and categorize content based on your preferences. 

The host limits the number of templates to display for a given task to a maximum of five, of which the last template must be one of the following types:

  * [`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate)
  * [`PaneTemplate`](https://developer.android.com/reference/androidx/car/app/model/PaneTemplate)
  * [`MessageTemplate`](https://developer.android.com/reference/androidx/car/app/model/MessageTemplate)
  * [`MediaPlaybackTemplate`](https://developer.android.com/reference/kotlin/androidx/car/app/media/model/MediaPlaybackTemplate)
  * [`SignInTemplate`](https://developer.android.com/reference/androidx/car/app/model/signin/SignInTemplate)
  * [`LongMessageTemplate`](https://developer.android.com/reference/androidx/car/app/model/LongMessageTemplate)



Note that this limit applies to the number of templates and not the number of `Screen` instances in the stack. For example, if an app sends two templates while in screen A and then pushes screen B, it can now send three more templates.

Alternatively, if each screen is structured to send a single template, then the app can push five screen instances onto the `ScreenManager` stack.

**Caution:** If the template quota is exhausted and the app attempts to send a new template, the host displays an error message to the user before closing the app.**Note:** During development with Android Auto, you can see the current number of steps overlaid on the screen by first enabling [Developer Mode](https://developer.android.com/training/cars/testing#developer-mode) and then checking **Enable debug overlay** in the **Developer Settings** screen. On Android Automotive OS, you can see the current number of steps in the logcat output after running `adb shell setprop log.tag.CarApp.H.Dis VERBOSE`.

There are special cases to these restrictions: template refreshes and back and reset operations.

### Template refreshes

Certain content updates are not counted toward the template limit. In general, if an app pushes a new template that is of the same type and contains the same main content as the previous template, the new template is not counted against the quota. For example, updating the toggle state of a row in a [`ListTemplate`](https://developer.android.com/reference/androidx/car/app/model/ListTemplate) does not count against the quota. See the documentation of individual templates to learn more about what types of content updates can be considered a refresh.

### Back operations

To enable sub-flows within a task, the host detects when an app is popping a `Screen` from the `ScreenManager` stack and updates the remaining quota based on the number of templates that the app is going backward by.

For example, if the app sends two templates while in screen A, then pushes screen B and sends two more templates, the app has one quota remaining. If the app then pops back to screen A, the host resets the quota to three, because the app has gone backward by two templates.

Note that, when popping back to a screen, an app must send a template that is of the same type as the one last sent by that screen. Sending any other template type causes an error. However, as long as the type remains the same during a back operation, an app can freely modify the contents of the template without affecting the quota.

### Reset operations

Certain templates have special semantics that signify the end of a task. For example, the [`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate) is a view that's expected to remain on the screen and be refreshed with new turn-by-turn instructions for the user.

When a task reaches one of these templates, the host resets the template quota, treating that template as though it's the first step of a new task. This allows the app to start a new task. To learn more, see the documentation for individual templates to learn which trigger a reset on the host.

If the host receives an intent to start the app from a notification action or from the launcher, the quota is also reset. This mechanism lets an app begin a new task flow from notifications, and it holds true even if an app is already bound and in the foreground.

[ Previous arrow_back  Glossary and concepts  ](https://developer.android.com/training/cars/apps/library/glossary-concepts)

[ Next CarContext class  arrow_forward  ](https://developer.android.com/training/cars/apps/library/carcontext-class)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
