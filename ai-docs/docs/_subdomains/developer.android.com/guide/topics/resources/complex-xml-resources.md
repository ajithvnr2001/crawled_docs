---
url: https://developer.android.com/guide/topics/resources/complex-xml-resources/
title: Inline complex XML resources \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:33.887590+00:00
---

# Inline complex XML resources  |  Views  |  Android Developers

> Source: https://developer.android.com/guide/topics/resources/complex-xml-resources/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



#  Inline complex XML resources Stay organized with collections  Save and categorize content based on your preferences. 

Certain resource types are a composition of multiple complex resources represented by XML files. One example is an animated vector drawable, which is a drawable resource encapsulating a vector drawable and an animation. This requires the use of at least three XML files, as shown in the following examples.

`res/drawable/avd.xml`
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/vectordrawable" >
        <target
            android:name="rotationGroup"
            android:animation="@anim/rotation" />
    </animated-vector>

`res/drawable/vectordrawable.xml`
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <vector xmlns:android="http://schemas.android.com/apk/res/android"
        android:height="64dp"
        android:width="64dp"
        android:viewportHeight="600"
        android:viewportWidth="600" >
        <group
            android:name="rotationGroup"
            android:pivotX="300.0"
            android:pivotY="300.0"
            android:rotation="45.0" >
            <path
                android:fillColor="#000000"
                android:pathData="M300,70 l 0,-70 70,70 0,0 -70,70z" />
        </group>
    </vector>

`res/anim/rotation.xml`
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <objectAnimator xmlns:android="http://schemas.android.com/apk/android"
        android:duration="6000"
        android:propertyName="rotation"
        android:valueFrom="0"
        android:valueTo="360" />

If the vector drawable and animations are re-used elsewhere, this is the best way to implement an animated vector drawable. But if these files are only used for this animated vector drawable, then there is a more compact way to implement them.

Using AAPT’s inline resource format, you can define all three resources in the same XML file, as shown in the following example. For an animated vector drawable, put the file under `res/drawable/`.

`res/drawable/avd.xml`
    
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
        **xmlns:aapt="http://schemas.android.com/aapt"** >
    
        **< aapt:attr name="android:drawable" >**
            <vector
                android:height="64dp"
                android:width="64dp"
                android:viewportHeight="600"
                android:viewportWidth="600" >
                <group
                    android:name="rotationGroup"
                    android:pivotX="300.0"
                    android:pivotY="300.0"
                    android:rotation="45.0" >
                    <path
                        android:fillColor="#000000"
                        android:pathData="M300,70 l 0,-70 70,70 0,0 -70,70z" />
                </group>
            </vector>
        **< /aapt:attr>**
    
        <target android:name="rotationGroup">
            **< aapt:attr name="android:animation" >**
                <objectAnimator
                    android:duration="6000"
                    android:propertyName="rotation"
                    android:valueFrom="0"
                    android:valueTo="360" />
            **< /aapt:attr>**
        </target>
    </animated-vector>

The XML tag `<aapt:attr >` tells AAPT to treat the tag’s child as a resource and extract it into its own resource file. The value in the attribute name specifies where to use the inline resource within the parent tag.

AAPT generates resource files and names for all the inline resources. Applications built using this inline format are compatible with all versions of Android.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
