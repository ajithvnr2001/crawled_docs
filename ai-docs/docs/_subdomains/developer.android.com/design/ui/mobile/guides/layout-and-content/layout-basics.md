---
url: https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-basics/
title: Layout basics \u00a0|\u00a0 Mobile \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:39:34.917088+00:00
---

# Layout basics  |  Mobile  |  Android Developers

> Source: https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-basics/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ UI Design ](https://developer.android.com/design/ui)
  * [ Mobile ](https://developer.android.com/design/ui/mobile)
  * [ Guides ](https://developer.android.com/design/ui/mobile/guides/foundations/accessibility)



#  Layout basics Stay organized with collections  Save and categorize content based on your preferences. 

![Hero layout basics illustration](https://developer.android.com/static/images/design/ui/mobile/layout-basics-hero.png)

A layout defines the visual structure for a user to interface with your app, such as in a composable. Android provides a range of libraries, canonical starting points, and techniques to display and position content.

## Get Started

Start designing Android layouts by learning [app anatomy](https://developer.android.com/design/ui/mobile/guides/layout-and-content/app-anatomy) then how to [structure your app's content](https://developer.android.com/design/ui/mobile/guides/layout-and-content/content-structure).

## Takeaways

**Layout orientation**

Consider different aspect ratios, size classes, and resolutions that users might encounter. Verify that your app provides a good user experience on both landscape and portrait orientation as well as different screen sizes and form factors. 

For more information, see the guidance on [adapting your layout](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout) and [canonical layouts](https://developer.android.com/design/ui/mobile/guides/layout-and-content/common-layouts). 

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-orientation.webp)

**Device safe areas**

Honor device safe areas, which includes parts of the UI such as display cutouts, edge-to-edge insets, edge displays, software keyboards, and system bars. Provide a flexible layout for users to interact with the keyboard. 

Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/images/design/ui/mobile/layout-basics-video-1.mp4) and watch it with a video player. 

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics_alignment_do.webp)

check_circle 

### Do

Focus user inputs. If the keyboard is present, move the input up into a focused state or consider attaching the text input to the keyboard.

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics_alignment_dont.webp)

cancel 

### Don't

Hide inputs. Even on smaller screens, the user might not know or be able to scroll the screen.

**Interaction ergonomics**

Keep essential interactions, like primary navigation, in a reachable screen area. Floating action buttons (FABs) provide a prominent and reachable interaction point 

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-1-takeaways-key-essential-layout.webp)

**Containment groups**

Use containment to group related content to guide the user through content and actions. Cards using explicit containment to group content with related actions. 

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-2-takeways-explicit-containment.webp)

**Alignment**

Provide consistent alignment between similar content and UI elements.

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics_alignment_do.webp)

check_circle 

### Do

Establish consistent spacing between like elements.

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics_alignment_dont.webp)

cancel 

### Don't

Disrupt readability by inconsistently spacing like elements, which can make designs appear haphazard.

**Essential interactions**

Don't overwhelm your user with too many actions per view. 

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-1-takeaways-key-actions.webp)

**Notate layout specs**

When building custom layouts, notate how content should sit within the layout using alignment, constraints, or gravity terms. Include how images should respond to their container to display properly. 

![](https://developer.android.com/static/images/design/ui/mobile/layout-basics-2-takeways-notate.webp)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
