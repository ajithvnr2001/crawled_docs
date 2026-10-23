---
url: https://developer.android.com/training/cars/apps/library/text-string-variants/
title: Add text string variants \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:08.739267+00:00
---

# Add text string variants  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/text-string-variants/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Add text string variants Stay organized with collections  Save and categorize content based on your preferences. 

Different car screen sizes may show different amounts of text. With Car App API level 2 and later, you can specify multiple variants of a text string to best fit the screen. To see where text variants are accepted, look for templates and components that take a [`CarText`](https://developer.android.com/reference/androidx/car/app/model/CarText).

You can add text string variants to a `CarText` with the [`CarText.Builder.addVariant()`](https://developer.android.com/reference/androidx/car/app/model/CarText.Builder#addVariant\(java.lang.CharSequence\)) method:
    
    
    val itemTitle = CarText.Builder("This is a very long string")
        .addVariant("Shorter string")
        .build()
    
    [TextStringVariants.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/TextStringVariants.kt#L28-L30)

You can then use this `CarText`—for example, as the primary text of a [`GridItem`](https://developer.android.com/reference/androidx/car/app/model/GridItem).
    
    
    val gridItem = GridItem.Builder()
        .setTitle(itemTitle)
        .setImage(CarIcon.APP_ICON)
        .build()
    
    [TextStringVariants.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/TextStringVariants.kt#L34-L37)

Add strings in the order of from most to least preferred. For example, from longest to shortest. The host picks the appropriate-length string depending on the amount of space available on the car screen.

[ Next Add inline CarIcons for rows  arrow_forward  ](https://developer.android.com/training/cars/apps/library/inline-car-icons)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
