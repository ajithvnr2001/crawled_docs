---
url: https://developer.android.com/reference/wear-os/wff/watch-face/
title: WatchFace \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:35.884538+00:00
---

# WatchFace  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/wear-os/wff/watch-face/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



#  WatchFace Stay organized with collections  Save and categorize content based on your preferences. 

Watch Face Format version Version 5 Version 4 Version 3 Version 2 Version 1

* * *

The root element of every `watchface.xml` file. It contains information about the elements that should appear in the watch face preview when users choose which watch face to use on their Wear OS devices.

Introduced in Wear OS 4.

## Syntax
    
    
    <WatchFace width="_positive-integer_ " height="_positive-integer_ "
               clipShape="NONE | **CIRCLE** | RECTANGLE" cornerRadiusX="_float_ "
               cornerRadiusY="_float_ ">
      <!-- Only the required inner element is shown here. -->
      <Scene>
      </Scene>
    </WatchFace>

## Attributes

The `WatchFace` element must contain the following attributes:

`width`
    Width of the visual screen on which watch face components are drawn, in pixels. All child geometric elements, such as shapes and complications, have their sizes and positions set relative to the visual screen size. Note that the visual screen might be a different size than the display resolution of a physical Wear OS device.
`height`
    Height of the visual screen on which watch face components are drawn, in pixels. All child geometric elements, such as shapes and complications, have their sizes and positions set relative to the visual screen size. Note that the visual screen might be a different size than the display resolution of a physical Wear OS device.

The `WatchFace` element can also contain the following attributes:

`clipShape`
    

The shape of the visual screen to use for the watch face preview. If you use a value of `CIRCLE`, it's likely that elements near the corners become partially cut off.

The default value is `CIRCLE`.

`cornerRadiusX`
    

The length of half of an ellipse's horizontal axis, which creates round corners. Use this value, along with `cornerRadiusY`, to create a rounded-rectangle effect.

This value has no effect unless you specify a `clipShape` of `RECTANGLE`.

`cornerRadiusY`
    

The length of half of an ellipse's vertical axis, which creates round corners. Use this value, along with `cornerRadiusY`, to create a rounded-rectangle effect.

This value has no effect unless you specify a `clipShape` of `RECTANGLE`.

## Inner elements

The `WatchFace` element must contain at least one [`Scene`](https://developer.android.com/training/wearables/wff/scene) inner element.

The `WatchFace` element can also contain the following inner elements:

  * [`BitmapFonts`](https://developer.android.com/training/wearables/wff/bitmap-fonts)
  * [`Metadata`](https://developer.android.com/training/wearables/wff/metadata)
  * [`UserConfigurations`](https://developer.android.com/training/wearables/wff/user-configuration/user-configurations)



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [RoundRectangle](https://developer.android.com/training/wearables/wff/group/part/draw/shape/round-rectangle)
  * [RoundRectangle](https://developer.android.com/training/wearables/wff/v2/group/part/draw/shape/round-rectangle)
  * [BitmapFonts](https://developer.android.com/training/wearables/wff/bitmap-fonts)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-20 UTC."],[],[]] 
