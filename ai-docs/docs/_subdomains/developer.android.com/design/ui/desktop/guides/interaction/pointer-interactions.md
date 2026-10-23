---
url: https://developer.android.com/design/ui/desktop/guides/interaction/pointer-interactions/
title: Pointer interactions \u00a0|\u00a0 Desktop experience \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:39:45.477918+00:00
---

# Pointer interactions  |  Desktop experience  |  Android Developers

> Source: https://developer.android.com/design/ui/desktop/guides/interaction/pointer-interactions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ UI Design ](https://developer.android.com/design/ui)
  * [ Desktop experience ](https://developer.android.com/design/ui/desktop)
  * [ Guides ](https://developer.android.com/design/ui/desktop/guides/foundations/design-principles)



#  Pointer interactions Stay organized with collections  Save and categorize content based on your preferences. 

Desktop users rely on pointer devices, such as a mouse or touchpad, to interact with your app. For an optimal desktop experience, support key pointer events such as hover, scroll, primary click, and secondary click.

## Takeaways when adapting to desktop inputs

  1. Add hover states and interactions to your existing system.
  2. Account for right-click interaction for added efficiency.
  3. Targets should have more precise sizing.



## Primary click

Primary click, or in most cases left-click, is the main cursor interaction a desktop user relies on. The rule of thumb is that a user should be able to accomplish all the primary user journeys with primary clicks alone. Not hiding functionality from primary clicks is not only good for discoverability but also critical to assistive technologies like [Switch Access](https://support.google.com/accessibility/android/answer/6122836).

## Secondary click

While touch interactions rely on a long-press, desktop users expect context menus to appear on a secondary click, such as a right-click on a mouse or a two-finger tap on a touchpad. For an optimal desktop experience, configure your app to trigger context menus on a secondary click, rather than requiring a long click.

![Right-clicking a card to show a context menu for more options](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_secondary.webp)Right-clicking a card to show a context menu for more options.

## Hover

In addition to cursor icon change, interactivity can also be indicated by changing an element's visual state on hover. For design guidance, learn more at [states](https://m3.material.io/foundations/interaction/states/overview).

Hover can also reveal supplementary information or actions, such as tooltips or list actions nested in context menus or overflow menus.

![Here hover is used to show additional information in a tooltip and more interactions](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_supplement.webp)Here hover is used to show additional information in a tooltip and more interactions.

## Drag-and-drop

On touchscreens, dragging requires a long-press because a one-finger swipe is reserved for scrolling. Click-and-drag should be instantaneous with pointer devices with dedicated scroll methods, such as a scroll wheel or two-finger swipe on a touchpad.

![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_drag.webp)Draggable cards as an alternative interaction.

## Selection

Streamline selection interactions for the desktop experience by providing a dedicated click target.

![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_pointer_selection.webp)Instead of touch & hold to reveal selection options, desktop allows for checkboxes on hover.

## Target size

When sizing UI elements for cursor interactions, avoid buttons that are overly large or have intrinsic touch targets beyond the element's visual boundaries.

![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_target.webp)

![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_target_adapt_do.webp)

check_circle 

### Do

Set a max width for buttons and their targets when using a pointer device.

![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop_ixd_target_adapt_dont.webp)

cancel 

### Don't

Allow buttons to expand full width or maintain intrinsic touch targets.

Pointer targets can be smaller than the standard 48 x 48 dp touch target, for alternative cursor interactions, such as an archive on hover that appears primarily after the item is selected.

![](https://developer.android.com/static/images/design/ui/desktop/guides/desktop-ixd-target-size.webp)

For more on designing for inputs, learn more on [Material Design inputs](https://m3.material.io/foundations/interaction/inputs). Learn how to [implement with Mouse and touchpad support](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens#mouse_and_touchpad).

[ Previous arrow_back  Across form factors  ](https://developer.android.com/design/ui/desktop/guides/foundations/across-form-factors)

[ Next Cursors  arrow_forward  ](https://developer.android.com/design/ui/desktop/guides/interaction/cursors)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-03 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-03 UTC."],[],[]] 
