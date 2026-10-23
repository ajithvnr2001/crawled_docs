---
url: https://developer.android.com/design/ui/tv/guides/components/lists/
title: Lists \u00a0|\u00a0 TV \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:39:59.245836+00:00
---

# Lists  |  TV  |  Android Developers

> Source: https://developer.android.com/design/ui/tv/guides/components/lists/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ UI Design ](https://developer.android.com/design/ui)
  * [ TV ](https://developer.android.com/design/ui/tv)
  * [ Guides ](https://developer.android.com/design/ui/tv/guides/foundations/design-for-tv)



#  Lists Stay organized with collections  Save and categorize content based on your preferences. 

Lists are a visual representation of one or more related items. They are commonly used to display a collection of options.

![Lists Cover](https://developer.android.com/static/design/ui/tv/guides/components/images/covers/cover-lists.webp)

## Resources

Type | Link | Status  
---|---|---  
Design | [Design source (Figma)](https://goo.gle/tv-desing-kit) | Available  
Implementation | [Jetpack Compose](https://developer.android.com/reference/kotlin/androidx/tv/material3/ListItem.composable#ListItem\(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.ui.unit.Dp,androidx.tv.material3.ListItemShape,androidx.tv.material3.ListItemColors,androidx.tv.material3.ListItemScale,androidx.tv.material3.ListItemBorder,androidx.tv.material3.ListItemGlow,androidx.compose.foundation.interaction.MutableInteractionSource\)) | Available  
  
## Highlights

  * Lists are a continuous collection of text or images.
  * Lists should feel natural and be scannable.
  * Lists are made up of items containing primary and supplemental actions represented by icons and text.



## Variants

There are three types of lists: one-line list, two-line list, and three-line list.

![Lists Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/list-types.webp)

  1. **One-line list** : A single line to communicate each item. This simple design ensures each item is clearly distinct from the other.
  2. **Two-line list** : Uses two parallel lines to communicate each item. This structured design ensures natural readability and avoids cognitive overload.
  3. **Three-line list** : Uses three parallel lines to represent each item. This decorative design creates a high level of visual prominence.



## Anatomy

![Lists Anatomy](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/list-item-anatomy.webp)

  1. **Icon** : A small graphic that represents a specific object or action, often used to visually communicate an idea or concept.
  2. **Overline** : A short line of text that appears above title or subtitle, often used to provide additional context or emphasis.
  3. **Title** : A large, bold line of text that serves as the main heading of a design element or page.
  4. **Subtitle** : A smaller line of text that provides additional information or context below a main title.
  5. **Control** : An interactive element that allows the user to input a decision.



## States

![List States](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/list-item-states.webp)

## Spec

![List Specs](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/list-item-spec.webp)

![List Height Suggestion](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/list-item-height.webp)

![List Spacing](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/list-item-spacing.webp)

## Usage

Lists are vertically organized groups of text and images. Optimized for reading comprehension, a list consists of a single continuous column of items. List items can contain primary and supplemental actions represented by icons and text.

![](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/container-do.webp)

check_circle 

### Do

List items are not buttons. The items don't have containers. List items are, by default, unselected and unfocused.

![](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/container-dont.webp)

warning 

### Caution

Use container background for list items only when necessary.

### Selection controls

Controls display information and actions for list items. They can be aligned to the leading or trailing edge of the list item.

![Selection checkbox](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/selection-checkbox.webp)

![Selection radio](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/selection-radio.webp)

![Selection switch](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/selection-switch.webp)

  1. **Checkboxes** : Select one or more list items.
  2. **Radio buttons** : Select exactly one item in the list.
  3. **Switches** : Toggle a control on or off.



![](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/selection-do.webp)

check_circle 

### Do

Use an icon selection indicator to clearly show the selected item in a list. This will help users easily identify which item they have selected and improve the overall user experience.

![](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/selection-dont.webp)

cancel 

### Don't

Avoid relying solely on the background color to indicate selection in a list.

![](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/action-dont.webp)

cancel 

### Don't

Avoid placing buttons inside a list item as it can cause confusion about which element is currently in focus.

### Icons

![](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/icon-do.webp)

check_circle 

### Do

If you're showing the same type of content in the list, omit icons to reduce visual noise and improve the user experience. Avoid using icons in a list when they serve no purpose and don't provide additional information. 

![](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/icon-dont.webp)

cancel 

### Don't

Avoid using the same icon for all items in a list. This can be visually overwhelming and confusing for users. Instead, use icons only when they add value or provide additional information.

### Avatars and images

List items can include images in a circular crop to represent a person or entity.

![Avatars & Images](https://developer.android.com/static/design/ui/tv/guides/components/images/lists/avatar-do.webp)

[ Previous arrow_back  Featured carousel  ](https://developer.android.com/design/ui/tv/guides/components/featured-carousel)

[ Next Tabs  arrow_forward  ](https://developer.android.com/design/ui/tv/guides/components/tabs)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
