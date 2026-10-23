---
url: https://developer.android.com/guide/topics/resources/font-resource/
title: Font resources \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:37.466365+00:00
---

# Font resources  |  Views  |  Android Developers

> Source: https://developer.android.com/guide/topics/resources/font-resource/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



#  Font resources Stay organized with collections  Save and categorize content based on your preferences. 

A font resource defines a custom font that you can use in your app. Fonts can be individual font files or a collection of font files, known as a font family and defined in XML.

Also see how to define [fonts in XML](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml) or instead use [Downloadable Fonts](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts).

## Bundled font

You can bundle fonts as resources in an app. Fonts are compiled in the `R` file and are automatically available in the system as a resource. You can then access these fonts with the help of the `font` resource type. 

file location:
    `res/font/_filename_.ttf` (`.ttf`, `.ttc`, `.otf`, or `.xml`)  
The filename is used as the resource ID. 
resource reference:
    In XML: `@[package:]font/_font_name_`
syntax:
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <font-family>
      <font
        android:font="@[package:]font/font_to_include"
        android:fontStyle=["normal" | "italic"]
        android:fontWeight="weight_value" />
    </font-family>

elements:
    

`<font-family>`
    **Required.** This must be the root node. 

No attributes.

`<font>`
    Defines a single font within a family. Contains no child nodes. 

Attributes:

`android:fontStyle`
    _Keyword_. Defines the font style. This attribute is used when the font is loaded into the font stack and overrides any style information in the font's header tables. If you don't specify the attribute, the app uses the value from the font's header tables. The constant value is either `normal` or `italic`. 
`android:fontWeight`
    _Integer_. The weight of the font. This attribute is used when the font is loaded into the font stack and overrides any weight information in the font's header tables. The attribute value must be a multiple of 100 between 100 and 900, inclusive. If you don't specify the attribute, the app uses the value from the font's header tables. The most common values are 400 for regular weight and 700 for bold weight. 
example:
    XML file saved at `res/font/lobster.xml`: 
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <font-family xmlns:android="http://schemas.android.com/apk/res/android">
        <font
            android:fontStyle="normal"
            android:fontWeight="400"
            android:font="@font/lobster_regular" />
        <font
            android:fontStyle="italic"
            android:fontWeight="400"
            android:font="@font/lobster_italic" />
    </font-family>

XML file saved in `res/layout/` that applies the font to a `[TextView](https://developer.android.com/reference/android/widget/TextView)`:
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <EditText
        android:fontFamily="@font/lobster"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Hello, World!" />

## Downloadable font

A downloadable font resource defines a custom font that you can use in an app. This font isn't available in the app itself. Instead, the font is retrieved from a font provider. 

file location:
    `res/font/_filename_.xml` The filename is the resource ID. 
resource reference:
    In XML:`@[package:]font/_font_name_`
syntax:
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <font-family
        android:fontProviderAuthority="authority"
        android:fontProviderPackage="package"
        android:fontProviderQuery="query"
        android:fontProviderCerts="@[package:]array/array_resource" />

elements:
    

`<font-family>`
    **Required.** This must be the root node. 

attributes:

`android:fontProviderAuthority`
    _String_. **Required**. The authority of the font provider that defines the font request. 
`android:fontProviderPackage`
    _String_. **Required**. The package name of the font provider to be used for the request. This is used to verify the identity of the provider. 
`android:fontProviderQuery`
    _String_. **Required**. The string query of the font. Refer to your font provider's documentation on the format of this string. 
`android:fontProviderCerts`
    _Array resource_. **Required**. Defines the sets of hashes for the certificates used to sign this provider. This is used to verify the identity of the provider and is only required if the provider isn't part of the system image. The value can point to a single list (a string array resource) or a list of lists (an array resource), where each individual list represents one collection of signature hashes. Refer to your font provider's documentation for these values. 
example:
    XML file saved at `res/font/lobster.xml`: 
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <font-family xmlns:android="http://schemas.android.com/apk/res/android"
        android:fontProviderAuthority="com.example.fontprovider.authority"
        android:fontProviderPackage="com.example.fontprovider"
        android:fontProviderQuery="Lobster"
        android:fontProviderCerts="@array/certs">
    </font-family>

XML file saved in `res/values/` that defines the cert array:
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <string-array name="certs">
          <item>MIIEqDCCA5CgAwIBAgIJA071MA0GCSqGSIb3DQEBBAUAMIGUMQsww...</item>
        </string-array>
    </resources>

XML file saved in `res/layout/` that applies the font to a `[TextView](https://developer.android.com/reference/android/widget/TextView)`:
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <EditText
        android:fontFamily="@font/lobster"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Hello, World!" />

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
