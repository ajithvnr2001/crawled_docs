---
url: https://developer.android.com/training/wearables/tiles/screen-size/
title: Develop tiles for different screen sizes \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:22.267184+00:00
---

# Develop tiles for different screen sizes  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/tiles/screen-size/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Develop tiles for different screen sizes Stay organized with collections  Save and categorize content based on your preferences. 

Your app's tiles should work well on Wear OS devices of all sizes, taking advantage of additional space where available, and still look great on smaller screens too. This guide provides recommendations for achieving this user experience.

To learn more about the design principles for adaptive layouts, read the [design guidance](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design).

## Provide differentiated experiences through breakpoints

Layouts from the [ProtoLayout Material](https://developer.android.com/reference/androidx/wear/protolayout/material/layouts/package-summary) library are responsive and take care of correct element placement and visibility. However, in some cases you might want to vary the number of visible elements for best results. For example, you might want 3 buttons on a smaller display, and 5 on a larger display.

To implement this sort of differentiated experience, use _screen size breakpoints_. To show a different layout when the screen size exceeds 225 dp:
    
    
    materialScope(this, requestParams.deviceConfiguration) {
        // ...
        val isLargeScreen = deviceConfiguration.screenWidthDp >= 225
        primaryLayout(
            mainSlot = {
                buttonGroup {
                    buttonGroupItem { button1 }
                    buttonGroupItem { button2 }
                    buttonGroupItem { button3 }
                    if (isLargeScreen) {
                        buttonGroupItem { button4 }
                        buttonGroupItem { button5 }
                    }
                }
            }
        )
    }
    
    [Tile.kt](https://github.com/android/snippets/blob/cf6066f995732d4217d67d3853eae3eb0d4e5071/wear/src/main/java/com/example/wear/snippets/m3/tile/Tile.kt#L92-L134)

The [design guidance](https://developer.android.com/design/ui/wear/guides/foundations/adaptive-design) illustrates additional opportunities.

## Test tiles on different screen sizes using Previews

It is important to test your layouts on different screen sizes. Use the Tile Preview annotations, along with the [`TilePreviewHelper`](https://developer.android.com/reference/androidx/wear/tiles/tooling/preview/TilePreviewHelper) and [`TilePreviewData`](https://developer.android.com/reference/androidx/wear/tiles/tooling/preview/TilePreviewData) classes:
    
    
    @Preview(device = WearDevices.LARGE_ROUND)
    fun smallPreview(context: Context) = TilePreviewData {
        TilePreviewHelper.singleTimelineEntryTileBuilder(
            materialScope(context, it.deviceConfiguration) {
                myAdaptiveLayout() // varies the layout depending on the size of the screen
            }
        )
            .build()
    }
    
    [Tile.kt](https://github.com/android/snippets/blob/cf6066f995732d4217d67d3853eae3eb0d4e5071/wear/src/main/java/com/example/wear/snippets/m3/tile/Tile.kt#L146-L154)

This lets you preview your Tile layouts directly within Android Studio.

For a full example, see the [timer tiles sample](https://github.com/android/wear-os-samples/blob/main/WearTilesKotlin/app/src/debug/java/com/example/wear/tiles/golden/Timer.kt) on GitHub.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
