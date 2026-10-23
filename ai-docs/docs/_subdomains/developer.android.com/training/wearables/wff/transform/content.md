---
url: https://developer.android.com/training/wearables/wff/transform/content/
title: Dynamically change element content \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:32.216168+00:00
---

# Dynamically change element content  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/transform/content/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Dynamically change element content Stay organized with collections  Save and categorize content based on your preferences. 

While `Transform` lets you change the appearance of elements or groups of elements, there might be occasions where you want to switch between a list of behaviors based on some condition. This is analogous to a `switch` statement or `if…else` statement in other languages.

For example, you might want to show a different background for early morning, morning, lunch, afternoon, evening, and night.

`Condition` statements in Watch Face Format let you include different parts of your watch face scene depending on the evaluation of [expressions](https://developer.android.com/training/wearables/wff/expressions), for example:
    
    
    <Condition>
        <Expressions>
            <Expression name="is_early_morning">
                <![CDATA[[HOUR_0_23] >= 6 && [HOUR_0_23] < 8]]
            </Expression>
            <Expression name="is_morning">
                <![CDATA[[HOUR_0_23] < 12]]
            </Expression>
            <!-- Further expressions -->
        </Expressions>
        <Compare expression="is_early_morning">
            <!-- Early morning content here -->
        </Compare>
        <Compare expression="is_morning">
            <!-- Morning content here -->
        </Compare>
        <!-- Further Compare elements -->
        <!-- The "else" case -->
        <Default>
            <!-- content -->
        </Default>
    </Condition>
    
    [watchface_dynamic_content.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_dynamic_content.xml#L20-L55)

A few things to note about conditions:

  1. The first `Compare` element where the `expression` is `true` is used, and others are ignored.
  2. Owing to the XML format, it can often be easiest to wrap the expression definition in a `CDATA` element as shown here, as this avoids the need for XML escaping using entity elements such as `&gt;` and `&amp;`.
  3. `Condition` structures can be nested.



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
