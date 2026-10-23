---
url: https://developer.android.com/training/wearables/complications/
title: About complications \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:36.881638+00:00
---

# About complications  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/complications/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  About complications Stay organized with collections  Save and categorize content based on your preferences. 

A [complication](https://en.wikipedia.org/wiki/Complication_\(horology\)) is any feature that is displayed on a watch face in addition to the time. For example, a battery indicator is a complication. The [Complications API](https://developer.android.com/reference/kotlin/androidx/wear/watchface/complications/package-summary) is for both watch faces and data source apps.

The rest of this document describes data sources, watch faces, and complication types. 

## Complication data source

Apps that provide data such as battery level, weather, or step counts to watch faces for complications are called _complication data sources_. These data sources supply raw data and are not responsible for controlling how their data is rendered on a watch face. To learn about writing apps that provide data to watch faces, see [Expose data to complications](https://developer.android.com/training/wearables/exposing-data-complications). 

The following diagram shows how Wear OS by Google mediates the flow of data from sources to watch faces.

![Complications data flow](https://developer.android.com/static/wear/images/complications-data-flow.png)**Figure 1.** The flow of complication data.

## Complications on watch faces

Watch faces receive data from complication data sources, which lets them include complications without needing code for getting the underlying data. Watch faces retain control over how the data is rendered, so they can integrate data naturally with their design. For more information, see the design guide about [Complications](https://developer.android.com/training/wearables/design/complications).

To learn how to add complications to a watch face, see [ Add complications to a watch face](https://developer.android.com/training/wearables/watch-faces/adding-complications).

## Complication types

Complication types define what kinds of data can be shown in a complication or supplied by a data source. For example, use the `SHORT_TEXT` type when the data consists primarily of a short string. A [ `ComplicationData`](https://developer.android.com/reference/androidx/wear/watchface/complications/data/ComplicationData) object always has a single complication type that defines required and optional fields. A required field represents the primary piece of data; most types take their name from the required field.

Data sources use complication types differently from watch faces:

  * A data source chooses the types of complication data to supply, including which optional fields of those types to supply, and how many different types can be supported. For example, a step-count source might support the `RANGED_VALUE` and `SHORT_TEXT` types, and a next-meeting source might support the `SHORT_TEXT` and `LONG_TEXT` types.
  * You can choose how many complications to include in your watch face and the complication types to support. For example, a dial complication on a watch face might support the `SHORT_TEXT`, `SMALL_IMAGE`, and `RANGED_VALUE` types. A gauge on the watch face might support only the `RANGED_VALUE` type. 



To learn more about different complication types and fields supported by each type, see [ Complication types](https://developer.android.com/training/wearables/watch-faces/adding-complications#types-fields). 

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
