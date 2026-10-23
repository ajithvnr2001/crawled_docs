---
url: https://developer.android.com/guide/topics/resources/style-resource/
title: Style resource \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:37.853573+00:00
---

# Style resource  |  Views  |  Android Developers

> Source: https://developer.android.com/guide/topics/resources/style-resource/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



#  Style resource Stay organized with collections  Save and categorize content based on your preferences. 

A style resource defines the format and look for a UI. A style can be applied to an individual `[View](https://developer.android.com/reference/android/view/View)` (from within a layout file) or to an entire `[Activity](https://developer.android.com/reference/android/app/Activity)` or application (from within the manifest file).

For more information about creating and applying styles, please read [Styles and Themes](https://developer.android.com/guide/topics/ui/themes).

**Note:** A style is a simple resource that is referenced using the value provided in the `name` attribute (not the name of the XML file). As such, you can combine style resources with other simple resources in the one XML file, under one `<resources>` element.

file location:
    `res/values/_filename_.xml`  
The filename is arbitrary. The element's `name` will be used as the resource ID.
resource reference:
     In XML: `@[package:]style/_style_name_`
syntax:
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <style
            name="_style_name_ "
            parent="@[package:]style/_style_to_inherit_ ">
            <item
                name="_[package:]style_property_name_ "
                >_style_value_ </item>
        </style>
    </resources>

elements:
    

`<resources>`
    **Required.** This must be the root node. 

No attributes.

`<style>`
    Defines a single style. Contains `<item>` elements. 

attributes:

`name`
    _String_. **Required**. A name for the style, which is used as the resource ID to apply the style to a View, Activity, or application. 
`parent`
    _Style resource_. Reference to a style from which this style should inherit style properties. 
`<item>`
    Defines a single property for the style. Must be a child of a `<style>` element. 

attributes:

`name`
    _Attribute resource_. **Required**. The name of the style property to be defined, with a package prefix if necessary (for example `android:textColor`). 
example:
    

XML file for the style (saved in `res/values/`):
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <style name="CustomText" parent="@style/Text">
            <item name="android:textSize">20sp</item>
            <item name="android:textColor">#008</item>
        </style>
    </resources>

XML file that applies the style to a `[TextView](https://developer.android.com/reference/android/widget/TextView)` (saved in `res/layout/`):
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <EditText
        style="@style/CustomText"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Hello, World!" />

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
