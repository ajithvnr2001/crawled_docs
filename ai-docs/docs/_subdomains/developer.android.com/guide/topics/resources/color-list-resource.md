---
url: https://developer.android.com/guide/topics/resources/color-list-resource/
title: Color state list resource \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:36.592836+00:00
---

# Color state list resource  |  Views  |  Android Developers

> Source: https://developer.android.com/guide/topics/resources/color-list-resource/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



#  Color state list resource Stay organized with collections  Save and categorize content based on your preferences. 

A `[ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList)` is an object you can define in XML and apply as a color that actually changes colors depending on the state of the `[View](https://developer.android.com/reference/android/view/View)` object it is applied to. For example, a `[Button](https://developer.android.com/reference/android/widget/Button)` widget can exist in one of several states: pressed, focused, or neither. Using a color state list, you can provide a different color for each state.

You describe the state list in an XML file. Each color is defined in an `<item>` element inside a single `<selector>` element. Each `<item>` uses various attributes to describe the state in which it is used.

During each state change, the state list is traversed top to bottom, and the first item that matches the current state is used. The selection is _isn't_ based on the "best" match, but rather the first item that meets the minimum criteria of the state.

**Note:** If you want to provide a static color resource, use a simple [color](https://developer.android.com/guide/topics/resources/more-resources#Color) value.

file location:
    `res/color/_filename_.xml`  
The filename is used as the resource ID.
compiled resource datatype:
    Resource pointer to a `[ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList)`
resource reference:
     In Java: `R.color._filename_`  
In XML: `@[_package_ :]color/_filename_`
syntax:
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <selector xmlns:android="http://schemas.android.com/apk/res/android" >
        <item
            android:color="_hex_color_ "
            android:lStar="_floating_point_value_ "
            android:state_pressed=["true" | "false"]
            android:state_focused=["true" | "false"]
            android:state_selected=["true" | "false"]
            android:state_checkable=["true" | "false"]
            android:state_checked=["true" | "false"]
            android:state_enabled=["true" | "false"]
            android:state_window_focused=["true" | "false"] />
    </selector>

elements:
    

`<selector>`
    **Required.** This is the root element. Contains one or more `<item>` elements. 

Attributes:

`xmlns:android`
    _String_. **Required.** Defines the XML namespace, which is `"http://schemas.android.com/apk/res/android"`. 
`<item>`
    Defines a color to use during certain states, as described by its attributes. It is a child of a `<selector>` element. 

Attributes:

`android:color`
    _Hexadeximal color_. **Required**. The color is specified with an RGB value and optional alpha channel. 

The value always begins with a pound (`#`) character, followed by the Alpha-Red-Green-Blue information in one of the following formats:

  * #_RGB_
  * #_ARGB_
  * #_RRGGBB_
  * #_AARRGGBB_


`android:lStar`
    _Floating point_. **Optional**. This attribute modifies the base color's perceptual luminance. It takes either a floating-point value between 0 and 100 or a theme attribute that resolves as such. The item's overall color is calculated by converting the base color to an accessibility friendly color space and setting its L* to the value specified on the `lStar` attribute. 

Example: `android:lStar="50"`

`android:state_pressed`
    _Boolean_. `"true"` if this item is used when the object is tapped, such as when a button is touched or clicked. It's `"false"` if this item is used in the default, non-tapped state.
`android:state_focused`
    _Boolean_. `"true"` if this item is used when the object is focused, such as when a button is highlighted using the trackball or D-pad. It's `"false"` if this item is used in the default, non-focused state.
`android:state_selected`
    _Boolean_. `"true"` if this item is used when the object is selected, such as when a tab is opened. It's `"false"` if this item it used when the object isn't selected.
`android:state_checkable`
    _Boolean_. `"true"` if this item is used when the object is checkable. It's `"false"` if this item is used when the object isn't checkable. Only useful if the object can transition between a checkable and non-checkable widget.
`android:state_checked`
    _Boolean_. `"true"` if this item is used when the object is checked. It's `"false"` if it is used when the object is deselected.
`android:state_enabled`
    _Boolean_. `"true"` if this item is used when the object is enabled, capable of receiving touch or click events. It's `"false"` if it is used when the object is disabled.
`android:state_window_focused`
    _Boolean_. `"true"` if this item is used when the application window has focus, meaning the application is in the foreground. It's `"false"` if this item is used when the application window doesn't have focus, such as if the notification shade is pulled down or a dialog appears.

**Note:** The first item in the state list that matches the current state of the object is applied. So, if the first item in the list contains none of the preceding state attributes, then it applies every time. For this reason, place your default value last, as shown in the following example.

example:
    XML file saved at `res/color/button_text.xml`: 
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <selector xmlns:android="http://schemas.android.com/apk/res/android">
        <item android:state_pressed="true"
              android:color="#ffff0000"/> <!-- pressed -->
        <item android:state_focused="true"
              android:color="#ff0000ff"/> <!-- focused -->
        <item android:color="#ff000000"/> <!-- default -->
    </selector>

The following layout XML applies the color list to a `View`:
    
    
    <Button
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="@string/button_text"
        android:textColor="@color/button_text" />

see also:
    

  * [Color (simple value)](https://developer.android.com/guide/topics/resources/more-resources#Color)
  * `[ColorStateList](https://developer.android.com/reference/android/content/res/ColorStateList)`
  * [State list drawable](https://developer.android.com/guide/topics/resources/drawable-resource#StateList)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
