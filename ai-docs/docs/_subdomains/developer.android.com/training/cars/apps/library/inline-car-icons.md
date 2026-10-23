---
url: https://developer.android.com/training/cars/apps/library/inline-car-icons/
title: Add inline CarIcons for rows \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:09.282722+00:00
---

# Add inline CarIcons for rows  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/inline-car-icons/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Add inline CarIcons for rows Stay organized with collections  Save and categorize content based on your preferences. 

You can add icons inline with text to enrich your app's visual appeal using [`CarIconSpan`](https://developer.android.com/reference/kotlin/androidx/car/app/model/CarIconSpan). See the documentation for [`CarIconSpan.create`](https://developer.android.com/reference/kotlin/androidx/car/app/model/CarIconSpan#create) for more information on creating these spans. See [Spantastic text styling with Spans](https://medium.com/androiddevelopers/spantastic-text-styling-with-spans-17b0c16b4568) for an overview of how text styling with spans work.

**Note:** On hosts that support a Car App API level of less than five, raw text is rendered instead of the `CarIcon`.
    
    
    val rating = SpannableString("Rating: 4.5 stars")
    rating.setSpan(
        CarIconSpan.create(
            // Create a CarIcon with an image of four and a half stars
            CarIcon.Builder(
                IconCompat.createWithResource(carContext, R.drawable.ic_star)
            ).build(),
            // Align the CarIcon to the baseline of the text
            CarIconSpan.ALIGN_BASELINE
        ),
        // The start index of the span (index of the character '4')
        8,
        // The end index of the span (exclusive, length of the string)
        17,
        Spanned.SPAN_INCLUSIVE_INCLUSIVE
    )
    
    val row = Row.Builder()
        .setTitle("Rating Row")
        .addText(rating)
        .build()
    
    [InlineCarIcons.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/InlineCarIcons.kt#L32-L52)

[ Previous arrow_back  Add text string variants  ](https://developer.android.com/training/cars/apps/library/text-string-variants)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
