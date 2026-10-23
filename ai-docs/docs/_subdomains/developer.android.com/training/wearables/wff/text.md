---
url: https://developer.android.com/training/wearables/wff/text/
title: Work with text \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:30.014895+00:00
---

# Work with text  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/wff/text/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Work with text Stay organized with collections  Save and categorize content based on your preferences. 

For digital clocks, you should aim to use `DigitalClock` where possible. For all other text or clocks that cannot be represented using `DigitalClock`, `PartText` is the container for text-based rendering.

Depending on whether you want to show circular or regular text, the `PartText` should contain _either_ a `Text` or a `TextCircular` element.

### Work with fonts and bitmap fonts

Using custom fonts allows your watch face to stand out with its own style.

There are two ways to use custom fonts, both within `TimeText` and `PartText` containers.

  1. Specify a custom font `family` in the `Font` element. [A range of common formats](https://developer.android.com/training/wearables/wff/group/part/text/font?version=1) are supported, which must be placed in `res/font`

For example, using the Pacifico font from Google Fonts, and placing the asset as res/font/pacifico.ttf:
         
         <PartText x="0" y="50" width="450" height="250">
             <Text align="CENTER">
                 <Font family="pacifico" size="96">Hello!</Font>
             </Text>
         </PartText>
         
         [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L34-L38)

  2. Alternatively, define a `BitmapFont` supplying bitmap images in `res/drawable`:
         
         <BitmapFonts>
             <BitmapFont name="myhandwriting">
                 <Character name="1" resource="digit1" width="50" height="100" />
                 <Character name="2" resource="digit2" width="50" height="100" />
                 <Character name="3" resource="digit3" width="50" height="100" />
                 <Character name="4" resource="digit4" width="50" height="100" />
                 <!-- ... -->
                 <!-- Treat "12" specially, instead of a 1 followed by a 2-->
                 <Word name="12" resource="digit12" width="80" height="100" />
             </BitmapFont>
         </BitmapFonts>
         
         [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L19-L29)




Note how sequences of characters can be given a special treatment. For example, if "12" was to be represented with a joined 1 and 2, this could be achieved using a `Word` element.

To use the defined font:
    
    
    <DigitalClock x="125" y="120" width="200" height="50">
        <TimeText x="0" y="0" width="200" height="50" format="hh:mm">
            <BitmapFont family="myhandwriting" size="48" color="#FF00FF"/>
        </TimeText>
    </DigitalClock>
    
    [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L42-L46)

### Text effects

Watch Face Format provides several text effects which can be applied, such as [`OutGlow`](https://developer.android.com/training/wearables/wff/group/part/text/decoration/out-glow) and [`Shadow`](https://developer.android.com/training/wearables/wff/group/part/text/decoration/shadow). To use these, apply them as subelements of the `Font` element:
    
    
    <Font family="pacifico" size="96" color="#e2a0ff">
        <OutGlow color="#e8ffb7" radius="30">Hello!</OutGlow>
    </Font>
    
    [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L52-L54)

### Work with templates

Instead of static text, you may need to construct your text from data sources or expressions.

The `Template` element lets you do this:
    
    
    <Font family="pacifico" size="60" weight="BOLD" color="#ffffff">
        <Template>Day: %s<Parameter expression="[DAY_OF_WEEK_S]" /></Template>
    </Font>
    
    [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L62-L64)

### Work with resources

If your static text is instead defined in a resource, such as in `res/values/strings.xml`, then it can be referenced as follows:
    
    
    <!-- greeting defined in res/values/strings.xml -->
    <Font family="pacifico" size="60" weight="BOLD" color="#ffffff">greeting</Font>
    
    [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L72-L73)

This also lets you localize your watch face using different [resource qualifiers](https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources).

### Handle spacing

Working with text spacing in XML can be challenging. Extra spacing around text can cause formatting problems, such as incorrect centering, or prevent your app from finding Android string resources.

To avoid these situations, wrap your `Font` contents in a `CDATA` element:
    
    
    <Font family="pacifico" size="60" weight="BOLD" color="#ffffff">
        <![CDATA[Hello]]>
    </Font>
    
    [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L81-L83)

### Multiline text

To create multiline text, use the `maxLines` attribute on `Text`:
    
    
    <Text align="CENTER" maxLines="2">
        <Font family="pacifico" size="60" weight="BOLD" color="#ffffff">
            <![CDATA[Hello Wear OS world]]>
        </Font>
    </Text>
    
    [watchface_text.xml](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/watchface/src/main/res/raw/watchface_text.xml#L90-L94)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
