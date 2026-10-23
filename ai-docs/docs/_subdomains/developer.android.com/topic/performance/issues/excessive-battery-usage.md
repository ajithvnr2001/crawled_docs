---
url: https://developer.android.com/topic/performance/issues/excessive-battery-usage/
title: Excessive battery usage \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:21.653879+00:00
---

# Excessive battery usage  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/issues/excessive-battery-usage/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Excessive battery usage Stay organized with collections  Save and categorize content based on your preferences. 

When battery usage for a Wear OS watch face exceeds 4.44% per hour when devices aren't charging and no apps are in use, the watch won't last a full day on a single charge. This harms users and the Wear OS ecosystem.

To maximize battery life, aim for battery usage under 3.2% per hour for 80% of sessions and less than 1% excessive battery usage overall.

**Note:** For information on how Android Play Vitals tracks and reports this issue, see [Excessive battery usage in Android vitals](https://developer.android.com/google/play/vitals/excessive-battery-usage).

## Contributing factors

These are key factors affecting your app's battery usage:

  * **Excessive CPU usage:** Watch face sessions that use the CPU for 90 seconds or more per hour.
  * **Excessive partial wakelocks:** Watch face sessions that use wakelocks for 18.5 seconds or more per hour.



Use [Battery Historian](https://developer.android.com/topic/performance/power/battery-historian) to investigate further.

## Reduce battery usage

Use the following suggestions to reduce your app's battery usage.

### Use Watch Face Format

[Watch Face Format](https://developer.android.com/training/wearables/wff) uses declarative XML instead of executable code to simplify app creation and reduces battery usage.

### Handle Always on display (AoD) mode

When a watch isn't in use it switches to Always-on display (AoD), also called ambient mode. In AoD, your watch face should [illuminate no more than 15% of pixels](https://developer.android.com/docs/quality-guidelines/wear-app-quality#always-on-display).

### Optimize memory usage

Large images, fonts, and animations (like sweeping second hands) increase battery usage.

  * Use the lowest resolution resources needed
  * Crop resources to their minimum size (avoid transparent borders)
  * Remove or crop anything hidden by other elements to reduce overdraw

**Tip:** Use the [Watch Face Format Optimizer](https://github.com/google/watchface/tree/main/tools/wff-optimizer) to automatically apply some optimizations.

See [Optimize memory usage](https://developer.android.com/training/wearables/wff/memory-usage) for more suggestions.

### Limit animations

Animating elements makes watch faces visually appealing but uses more battery. To reduce their impact:

  * Avoid using high fps animations 
    * For most animations 15 fps is recommended
  * Limit usage of dynamic elements such as [Gyro](https://developer.android.com/training/wearables/wff/common/transform/gyro) and [ArithmeticExpression](https://developer.android.com/training/wearables/wff/common/attributes/arithmetic-expression)
    * `ArithmeticExpression` updates as frequently as its source data. High frequency sources such as `MILLISECOND` and `ACCELEROMETER` use more battery.
  * Avoid unnecessary animations in AoD mode



### Avoid wakelocks

Publish your app using [Watch Face Format](https://developer.android.com/training/wearables/wff) to avoid wakelocks.

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Watch Face Format](https://developer.android.com/training/wearables/wff)
  * [Power considerations](https://developer.android.com/design/ui/wear/guides/surfaces/watch-faces#power_considerations)
  * [Battery Historian](https://developer.android.com/topic/performance/power/battery-historian)



[ Previous arrow_back  Excessive Background Network Usage  ](https://developer.android.com/topic/performance/issues/bg-network-usage)

[ Next Permission Denials  arrow_forward  ](https://developer.android.com/topic/performance/issues/permissions)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
