---
url: https://developer.android.com/studio/gemini/generate-compose-previews/
title: Generate Compose previews \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:21:51.733623+00:00
---

# Generate Compose previews  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/gemini/generate-compose-previews/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Android Studio AI agent ](https://developer.android.com/ai-in-android)



#  Generate Compose previews Stay organized with collections  Save and categorize content based on your preferences. 

[Compose previews](https://developer.android.com/develop/ui/compose/tooling/previews) are a powerful tool for visualizing composables at design time in Android Studio, but manually setting up mock data for the preview parameters can be time-consuming. Gemini in Android Studio includes a feature that solves this problem: automated Compose preview generation.

You can access this tool in two ways:

  * Within any composable, right-click and navigate to **Gemini > Generate "<composable>" Preview** or **Generate Compose Previews for this file**.

**Note:** You only see the option to generate Compose previews for the whole file if there are multiple composables in the file that don't have associated previews.

![Compose preview generation from context menu](https://developer.android.com/static/studio/gemini/images/compose-preview-menu.png)

  * If you don't have any previews set up yet, in the empty preview panel click **Auto-generate Compose Previews for this file**.

![Compose preview generation from preview panel](https://developer.android.com/static/studio/gemini/images/compose-preview-panel.png)




When you ask Gemini to generate Compose previews, you get a diff view with Gemini's suggested Compose preview code where you can accept or reject the proposed changes. Gemini's code should provide a valuable starting point to accelerate your development workflow.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
