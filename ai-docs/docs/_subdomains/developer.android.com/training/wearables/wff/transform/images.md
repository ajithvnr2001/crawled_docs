---
url: https://developer.android.com/training/wearables/wff/transform/images/
title: Create animated images \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:32.044384+00:00
---

# Create animated images  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/transform/images/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Create animated images Stay organized with collections  Save and categorize content based on your preferences. 

In addition to static images on the watch face, animated images can bring a further dimension to the user experience.

Note that this section is specifically about using animated image files. It is possible to animate components on the watch face using the `Transform` element, which is covered on the [Dynamically changing the appearance of elements](https://developer.android.com/training/wearables/wff/transform) page.

Animations can consist of either an animated image file, such as an animated GIF, or a sequence of `Images`, which combine together to form an animation.

As well as specifying the files to use, you'll need to define how the animation should behave, for example, whether to loop the playback, or if not, what to do at the end, among other options. For this, use an [`AnimationController`](https://developer.android.com/training/wearables/wff/group/part/animated-image/animation-controller).

Finally, for all animations, include a [thumbnail image](https://developer.android.com/training/wearables/wff/group/part/animated-image/thumbnail) in all animations.

Putting this together, a basic animation can be implemented as follows:
    
    
    <PartAnimatedImage x="0" y="0" width="450" height="450">
        <AnimationController play="ON_VISIBLE"/>
        <AnimatedImage resource="animation" format="AGIF"/>
        <Thumbnail resource="animation_thumbnail" />
    </PartAnimatedImage>
    
    [watchface_dynamic_appearance.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_dynamic_appearance.xml#L46-L50)

Consult the [`PartAnimatedImage`](https://developer.android.com/training/wearables/wff/group/part/animated-image/part-animated-image) reference for more details on including a list of animated images and constructing an animation from still images.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
