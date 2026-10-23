---
url: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables/
title: Foldables \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:09.008415+00:00
---

# Foldables  |  App quality  |  Android Developers

> Source: https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ User experience ](https://developer.android.com/quality/user-experience)



#  Foldables Stay organized with collections  Save and categorize content based on your preferences. 

Foldable devices enable a unique user experiences, transitioning smoothly between compact phone-sized screens and expansive tablet-like displays. Foldables introduce unique physical states, or postures, such as tabletop and book posture, that apps can take advantage of to offer specialized layouts and enhanced multitasking capabilities.

## Guidelines

Create a premium user experience on premium foldable devices.

### Postures and states

Guideline ID | Test IDs | Description  
---|---|---  
Foldables_Postures | T-Foldables_Postures | App supports all foldable postures and related use cases:

  * Tabletop posture — Video calling and video or audio playback.
  * Book posture — Reading lengthy text content.

See [Learn about foldables](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables).   
Foldables_Camera | T-Foldables_Camera | Camera apps adjust their preview for folded and unfolded states and support front and back screen preview.  
  
### Multitasking and multi-instance

Guideline ID | Test IDs | Description  
---|---|---  
Foldables_Multitasking_Scenarios |  T-Foldables_PiP and  
T-Foldables_Attachments | App supports various multitasking scenarios, for example:

  * Picture-in-picture mode: With the device folded and unfolded,app is able to enter and exit picture‑in‑picture mode in portrait and landscape orientations and in multi‑window mode. See [Picture-in-picture (PiP) support](https://developer.android.com/guide/topics/ui/picture-in-picture).
  * Attachments: Messaging apps can open attachments (such as videos) in a separate window with the device folded and unfolded.

  
Foldables_PiP | T-Foldables_PiP | App supports interactive picture‑in‑picture functionality that enables custom controls and user interaction.  
Foldables_Multi-Instance | T-Foldables_Multi-Instance | In folded and unfolded device states, the app is able to launch multiple instances of itself in separate windows. See [Multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance) in [Support multi-window mode.](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode)  
  
## Tests

To verify that your app provides a differentiated experience on foldable devices, complete the following tests.

### Foldable postures and states

Test ID | Guideline IDs | Description  
---|---|---  
T-Foldables_Postures | Foldables_Postures | View the app in all foldable postures, including tabletop and book postures. Verify that UI elements transition to the optimal location (for example, media controllers move to the horizontal screen area in tabletop posture).  
T-Foldables_Camera | Foldables_Camera | Activate the camera from within the app. Verify that the camera preview is correct when the device is folded and unfolded and rotated to portrait and landscape orientations. With the device unfolded, verify that the preview is correct on front and back screens.  
  
### Multitasking and multi-instance

Test ID | Guideline IDs | Description  
---|---|---  
T-Foldables_PiP | Foldables_Multitasking_Scenarios | With the device folded and unfolded, enter and exit picture‑in‑picture mode in portrait and landscape orientations and in multi‑window mode. In multi‑window mode, change the window size while picture‑in‑picture mode is active. In picture-in-picture mode, interact with any custom controls and verify their functionality.  
T-Foldables_Attachments | Foldables_Multitasking_Scenarios | With the device folded and unfolded, open and close attachments and notifications in portrait and landscape orientations and in multi‑window mode.  
T-Foldables_Multi-Instance | T-Foldables_Multi-Instance | With the device folded and unfolded, launch multiple instances of the app in separate windows in portrait and landscape orientations and in multi‑window mode.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
