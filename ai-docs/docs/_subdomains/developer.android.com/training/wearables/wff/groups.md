---
url: https://developer.android.com/training/wearables/wff/groups/
title: Arrange elements into groups \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:33.346344+00:00
---

# Arrange elements into groups  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/groups/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Arrange elements into groups Stay organized with collections  Save and categorize content based on your preferences. 

Groups allow you to separate your watch face design into a logical structure.

This can be useful to help you organize components. You can give each group a `name` to indicate what it is for.

A further reason that groups are very useful is that you can then treat everything within that group as a single entity for the purpose of adjusting its appearance, even dynamically adjusting to changing data sources.

Here are some examples of how this can be useful. The following `Group` contains various `PartText, PartImage` and `PartDraw` elements that make up a single logical part of the watch face:
    
    
    <Group name="decorations" x="100" y="100" width="200" height="200">
        <!-- PartText, PartImage, PartDraw elements go here -->
    </Group>
    
    [watchface_groups.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_groups.xml#L20-L22)

## Change ambient behavior

Having defined the `Group`, the visibility of the whole `Group` can be adjusted for Ambient mode, for example, to hide the `Group`:
    
    
    <Group name="decorations" x="100" y="100" width="200" height="200">
        <Variant mode="AMBIENT" target="alpha" value="0" />
        <!-- PartText, PartImage, PartDraw elements go here -->
    </Group>
    
    [watchface_groups.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_groups.xml#L26-L29)

This avoids the need to add a `Variant` element individually to each child element.

### Transform a group

Similar to adjusting the ambient behavior, using `Variant`, many of the properties of `Group` can be adjusted using one or more `Transform` elements.

In this example, the `Group` is rotated based on the second. By specifying `pivotX` and `pivotY` as `0.5`, the rotation occurs around the center of the `Group`, irrespective of where each element, such as `PartText` or `PartImage` sits within that `Group`:
    
    
    <Group name="decorations" x="100" y="100" width="200" height="200">
        <!-- One full rotation per minute -->
        <Transform target="angle" value="[SECOND] * 6" />
        <!-- PartText, PartImage, PartDraw elements go here -->
    </Group>
    
    [watchface_groups.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_groups.xml#L33-L37)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
