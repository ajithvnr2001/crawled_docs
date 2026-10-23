---
url: https://developer.android.com/training/wearables/wff/expressions/
title: Build expressions \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:31.258483+00:00
---

# Build expressions  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/expressions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Build expressions Stay organized with collections  Save and categorize content based on your preferences. 

WFF uses an expression language to enable:

  * Transforming the appearance using `Transform` or `Gyro`
  * Conditional behavior through `Condition` statements
  * String formatting in `Template` elements



The expression language is a scripting language which contains your typical operators and a range of functions that can be used.

Expressions can use [data sources](https://developer.android.com/training/wearables/wff/common/attributes/source-type)—represented using square brackets—to let you react to external inputs such as the current date and time, health and fitness metrics, or even the weather.

When using expressions, the primary difference between `Transform`, `Template`, and `Condition` usage is that `Transform` and `Template` require the expression to result in a _value_ (for example, the new position of the enclosing element) while `Condition` requires the expression to result in a _boolean_.

When used in a `Condition` element, specify the expression as a text element. Wrap the expression in a `CDATA` element to avoid the need to use entity references, such as `&quot;` and `&amp;`.
    
    
    <![CDATA[[DAY_OF_WEEK] == 6 || [DAY_OF_WEEK] == 7]]>
    
    [watchface_expressions.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_expressions.xml#L28-L28)

This evaluates to a boolean and determines whether it is a weekend or not, using the `DAY_OF_WEEK` data source.

[Functions](https://developer.android.com/training/wearables/wff/common/attributes/arithmetic-expression#functions) are also supported—for example, an expression for rotating a value up to 5 degrees in either direction—based on the `x-value` of the Wear OS device's accelerometer:
    
    
    (5.0/90.0)*clamp([ACCELEROMETER_ANGLE_X],0,90) +
    (-5.0/90.0)*clamp([ACCELEROMETER_ANGLE_X],-90,0)
    
    [watchface_expressions.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_expressions.xml#L33-L34)

The `clamp()` function constrains a value within two bounds.

### Expression re-evaluation

The frequency with which expressions are re-evaluated depends on the data sources used in them. For example, the `[DAY_OF_WEEK] == 6 || [DAY_OF_WEEK] == 7` expression only re-evaluates when a new day starts. However, an expression that uses the `[SECOND]` data source re-evaluates every second.

Re-evaluation may result in scene recalculations and re-rendering, based on the change in the result of the expression. Therefore it is important to always use data sources that re-evaluate as infrequently as possible. For example, to determine whether it is afternoon:
    
    
    <!-- BAD: Re-evaluates every second -->
    [SECONDS_IN_DAY] > 43200
    
    [watchface_expressions.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_expressions.xml#L39-L40)
    
    
    <!-- Good: Minimizes re-evaluation (1 = PM, 0 = AM) -->
    [AMPM_STATE] == 1
    
    [watchface_expressions.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_expressions.xml#L45-L46)

### Configuration values in expressions

In addition to functions and data sources, configuration values can be used. For example, if in the [UserConfigurations](https://developer.android.com/training/wearables/wff/user-configuration/user-configurations) a `BooleanConfiguration` named `showBackgroundInAfternoon` has been defined, this can be used in an expression:
    
    
    <![CDATA[[CONFIGURATION.showBackgroundInAfternoon] == "TRUE" && [AMPM_STATE] == 1]]>
    
    [watchface_expressions.xml](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/watchface/src/main/res/raw/watchface_expressions.xml#L51-L51)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
