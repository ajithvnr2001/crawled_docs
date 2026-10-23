---
url: https://developer.android.com/training/wearables/wff/images/
title: Work with images \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:30.733689+00:00
---

# Work with images  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/images/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Work with images Stay organized with collections  Save and categorize content based on your preferences. 

Using images in your watch face can really help bring it to life, from a full-screen background image to individual detail images to add interest.

Place your image resources in the `res/drawable` folder, for example `res/drawable/face.png`, and then reference the image as follows:
    
    
    <PartImage x="0" y="0" width="450" height="450">
        <Image resource="watch_face_dial"/>
    </PartImage>
    
    [watchface_images.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_images.xml#L20-L22)

The `PartImage` element, as with other containers in Watch Face Format, can be modified in many ways, including being scaled, rotated, transformed, tinted, or masked. See the [`PartImage`](https://developer.android.com/training/wearables/wff/group/part/image/part-image) reference for more information.

### Vary the background

One effect that can provide interest is to change the background every hour. This can be achieved through the use of the `Images` element, for example:
    
    
    <PartImage x="150" y="150" width="150" height="150">
        <Images change="ON_NEXT_HOUR">
            <Image resource="red"/>
            <Image resource="orange"/>
            <Image resource="green"/>
        </Images>
    </PartImage>
    
    [watchface_images.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_images.xml#L26-L32)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
