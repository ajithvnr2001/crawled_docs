---
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/stylus/
title: Stylus \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:09.178086+00:00
---

# Stylus  |  App quality  |  Android Developers

> Source: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/stylus/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ User experience ](https://developer.android.com/quality/user-experience)



#  Stylus Stay organized with collections  Save and categorize content based on your preferences. 

A stylus enables artists, builders, and creators to express themselves using precise input and expansive canvases. Pressure sensitivity and low latency allow highly responsive interactions. Intuitive content management through drag and drop provides a premium usability experience.

## Guidelines

Build creative freedom into your app with stylus support.

### Stylus

Guideline ID | Test IDs | Description  
---|---|---  
Stylus_Draw_Write | T-Stylus_Draw_Write | App supports drawing and writing with a stylus. Drawings and writing can be erased with the stylus.  
Stylus_Drag_Drop | T-Stylus_Drag_Drop | App provides stylus support for dragging and dropping content between elements within the app and, in multi-window mode, to and from other apps. See [Enable drag and drop](https://developer.android.com/develop/ui/views/touch-and-input/drag-drop).  
Stylus_Enhanced | T-Stylus_Enhanced | App provides enhanced stylus support, including:

  * Low latency and motion prediction to improve responsiveness 
  * Pressure sensitivity for drawing strokes of varying width
  * Tilt detection for creating shading strokes
  * Palm and finger rejection to prevent stray marks

See [Advanced stylus features](https://developer.android.com/develop/ui/compose/touch-input/stylus-input/advanced-stylus-features#low-latency).   
  
## Tests

To verify that your stylus app provides a differentiated experience, complete the following tests.

### Stylus

Test ID | Guideline IDs | Description  
---|---|---  
T-Stylus_Draw_Write | Stylus_Draw_Write | Draw and write within the app using a stylus. Erase drawings and writing using the stylus.  
T-Stylus_Drag_Drop | Stylus_Drag_Drop | Using a stylus, drag and drop content on drop targets within the app. In multi-window mode, drag and drop content between the app and another app (to and from both apps).  
T-Stylus_Enhanced | T-Stylus_Enhanced | Interact with the app using a stylus as follows:

  * As you draw, observe the latency between the current stylus position and the last rendered stroke.
  * Draw with varying amounts of stylus pressure. Check whether the width of the strokes changes as the pressure changes. More pressure should produce thicker strokes.
  * Tilt the stylus as you draw; shading strokes should be produced. The more the stylus is tilted, the wider and lighter the shading strokes should be.
  * Let your fingers and palm touch the screen as you draw. The finger and palm touches shouldn't produce marks.

  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
