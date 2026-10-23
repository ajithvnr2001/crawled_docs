---
url: https://developer.android.com/training/wearables/wff/personalization/photos/
title: Personalize with photos \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:34.894476+00:00
---

# Personalize with photos  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/personalization/photos/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Personalize with photos Stay organized with collections  Save and categorize content based on your preferences. 

**Note** : This feature is available on version 4 and higher of Watch Face Format.

Allowing the user to select photos for inclusion on the watch face can help bring a personal touch to your watch face experience.

The [working with images](https://developer.android.com/training/wearables/wff/images) section already covers how to display images in your watch face. If you want to allow the user to choose from a range of predefined images, then use a `ListConfiguration` as shown in the [define user configurations](https://developer.android.com/training/wearables/wff/personalization/user-configurations) section.

To use images in your watch face that the user can configure, use the `<PhotosConfiguration>` element, for example:
    
    
    <!-- Under WatchFace element -->
    <UserConfigurations>
        <PhotosConfiguration id="photoConfig" configType="SINGLE"/>
    </UserConfigurations>
    
    [watchface_photos.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_photos.xml#L19-L22)

The `configType` can be either `SINGLE` or `MULTIPLE` indicating whether the user will be able to select a single image within the companion or a collection of photos.

**Note:** Only one `PhotosConfiguration` can be defined within each watch face.

## Support a single photo

For the single image case, the photo can be used within a `PartImage` element as follows:
    
    
    <PartImage x="100" y="50" width="100" height="100">
        <Photos source="[CONFIGURATION.photoConfig]" defaultImageResource="default_image"/>
    </PartImage>
    
    [watchface_photos.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_photos.xml#L27-L29)

Note the `defaultImageResource`, which is shown when the user has not selected a photo in the companion and is a required attribute.

If the user wishes to select a different photo, then they must use the companion to replace the existing selection with another.

## Support multiple photos

Using `PhotosConfiguration` with `configType="MULTIPLE"` allows the watch face to display a photo from a collection, which can be cycled through either through tapping or automatically after so many views have taken place.
    
    
    <PartImage x="100" y="250" width="100" height="100">
        <Photos change="ON_VISIBLE TAP" changeAfterEvery="5"
            source="[CONFIGURATION.galleryConfig]" defaultImageResource="default_image"/>
    </PartImage>
    
    [watchface_photos_multi.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_photos_multi.xml#L24-L27)

The preceding example shows the two options that are introduced when using `MULTIPLE`:

  1. The `change` attribute allows the developer to specify what events should cause the photo to cycle through the available images.



In the preceding example, both `TAP` and `ON_VISIBLE` are specified, meaning that the photo changes in response _either_ to a user tapping the photo _or_ in response to the photo becoming visible.

  1. The `changeAfterEvery` attribute applies only to the `ON_VISIBLE` change event, specifing how many times the photo should have become visible before the photo is changed. For example, you may feel that changing the photo every time the user wakes their watch is too frequent. The default value here is 3.



For more details on working with `PhotosConfiguration`, see the samples on GitHub.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
