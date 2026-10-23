---
url: https://developer.android.com/training/wearables/wff/release-notes/
title: Release notes for Watch Face Format \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:36.288947+00:00
---

# Release notes for Watch Face Format  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/release-notes/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Release notes for Watch Face Format Stay organized with collections  Save and categorize content based on your preferences. 

All versions of the Watch Face Format offer the following capabilities:

  * **Style editing:** Customize the watch face, including its color, background image, and font.

  * **Groups and complications:** Group components so that you can control or move those components with a single action. You can also handle an entire [complication](https://developer.android.com/training/wearables/design/complications) as one group.

  * **Tag expressions:** Add tags with date, time, battery, step count information, and more.




## Version 5

Version 5 of the Watch Face Format adds several capabilities, including the following:

  * Support for [blend mode](https://developer.android.com/reference/wear-os/wff/common/attributes/blend-mode) on [`Group`](https://developer.android.com/reference/wear-os/wff/group/group) and [`ComplicationSlot`](https://developer.android.com/reference/wear-os/wff/complication/complication-slot) elements.
  * Support for line spacing and vertical alignment on [`Text`](https://developer.android.com/reference/wear-os/wff/group/part/text/text) elements.
  * Support for auto-sizing and vertical alignment on [`TextCircular`](https://developer.android.com/reference/wear-os/wff/group/part/text/text-circular) elements.
  * Support for a minimum font size ([`minSize`](https://developer.android.com/reference/wear-os/wff/group/part/text/font)) on [`Font`](https://developer.android.com/reference/wear-os/wff/group/part/text/font) elements when auto-sizing is enabled.
  * Support for corner rendering control (`join` attribute) on [`Stroke`](https://developer.android.com/reference/wear-os/wff/group/part/draw/style/stroke) and [`WeightedStroke`](https://developer.android.com/reference/wear-os/wff/group/part/draw/style/weighted-stroke) elements.
  * Support for nested settings and dynamic complications on [`ListOption`](https://developer.android.com/reference/wear-os/wff/group/configuration/list-configuration) elements.



To view features from version 5 in the [XML reference](https://developer.android.com/reference/wear-os/wff/watch-face), check that the **Version 5** button is selected at the top of the documentation page.

## Version 4

Version 4 of the Watch Face Format adds several capabilities, including the following:

  * Support for [user-selected photos](https://developer.android.com/training/wearables/wff/personalization/photos).
  * [Transitions](https://developer.android.com/training/wearables/wff/transform) when entering and exiting ambient mode.
  * Support for [color transformations](https://developer.android.com/reference/wear-os/wff/common/transform/transform#transformable) on most elements and [color tinting](https://developer.android.com/reference/wear-os/wff/user-configuration/color-configuration) on grouped elements.
  * A new [`Reference`](https://developer.android.com/reference/wear-os/wff/common/reference/reference) element that lets you single-source your transform configurations.



To view features from version 4 in the [XML reference](https://developer.android.com/reference/wear-os/wff/watch-face), check that the **Version 4** button is selected at the top of the documentation page.

## Version 3

Version 3 of the Watch Face Format adds several capabilities, including the following:

  * [Auto-sizing text](https://developer.android.com/reference/wear-os/wff/group/part/text/text).
  * More capabilities for combining graphical objects, including [blend mode](https://developer.android.com/reference/wear-os/wff/common/attributes/blend-mode).
  * Support for weighted constraints on [line elements](https://developer.android.com/reference/wear-os/wff/group/part/draw/shape/line).
  * Several additional [data sources](https://developer.android.com/reference/wear-os/wff/common/attributes/source-type), primarily related to time zones.



To view features from version 3 in the [XML reference](https://developer.android.com/reference/wear-os/wff/watch-face), check that the **Version 3** button is selected at the top of the documentation page.

## Version 2

Version 2 of the Watch Face Format adds several capabilities related to data visualization, weather forecasts, and system data source types.

Highlights include the following:

  * [Flavors](https://developer.android.com/reference/wear-os/wff/user-configuration/flavor): Preset configurations for your watch face that users can browse in a companion app.
  * **Goal progress complication type:** Useful when users can exceed a goal such as step count.
  * **Weighted elements complication type:** Useful for showing discrete subsets of data.
  * **Weather conditions:** Show the current weather, as well as forecast conditions for hours or days into the future.
  * A new **heart rate** system data source for complications.



To view features from version 2 in the [XML reference](https://developer.android.com/reference/wear-os/wff/watch-face), check that the **Version 2** button is selected at the top of the documentation page.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-22 UTC."],[],[]] 
