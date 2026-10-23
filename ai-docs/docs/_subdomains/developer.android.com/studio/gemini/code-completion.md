---
url: https://developer.android.com/studio/gemini/code-completion/
title: Accelerate coding with AI code completion \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:13.870307+00:00
---

# Accelerate coding with AI code completion  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/gemini/code-completion/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Android Studio AI agent ](https://developer.android.com/ai-in-android)



#  Accelerate coding with AI code completion Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** [Next Edit Prediction](https://developer.android.com/studio/gemini/next-edit-prediction) is now the default experience for users on some Gemini flash models. We encourage you to try it out. You can toggle between Next Edit Prediction and traditional AI code completion at **File** (**Android Studio** on macOS) > **Settings > Tools > AI > Editor**.

Gemini offers AI-enabled autocompletion of code in Android Studio that appears as gray italicized text as you type. This feature saves you time and lets you complete coding projects faster by suggesting full functions. When AI code completion is enabled, Gemini might send additional information from your codebase such as surrounding pieces of your code, file types, and other necessary information to provide context to the LLM and provide more relevant suggestions.

To use AI code completion, follow these steps:

  1. Enable context sharing by selecting **Use all Gemini features** in the [Gemini settings](https://developer.android.com/studio/gemini/configure-gemini). AI code completion only works when Gemini can access context from your codebase.
  2. Open a file and start typing. Suggestions only trigger when the cursor is at the end of a line or anywhere on a blank line.
  3. Press `Tab` to accept a suggestion and `Esc` to clear a suggestion.



Keep in mind that the system won't always generate code completions. It's possible that the model doesn't have enough information to generate a response with high confidence.

You can toggle AI code completion on and off at any time by clicking the Gemini icon at the bottom of the Studio IDE ![](https://developer.android.com/static/studio/gemini/images/gemini-active.png) and clicking **Enable AI code completion**.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
