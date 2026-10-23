---
url: https://developer.android.com/studio/gemini/features/
title: Gemini in Android Studio features \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:21:52.097438+00:00
---

# Gemini in Android Studio features  |  Android Developers

> Source: https://developer.android.com/studio/gemini/features/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ Android Studio AI agent ](https://developer.android.com/ai-in-android)



#  Gemini in Android Studio features Stay organized with collections  Save and categorize content based on your preferences. 

Gemini in Android Studio includes features for every step of the development process. The following table lists some of the key features available to help power your workflow. Gemini is a rapidly developing space, so also check Android Studio's [stable release notes](https://developer.android.com/studio/releases) and [preview release notes](https://developer.android.com/studio/preview/features) for the latest updates.

Category | Feature | Description | Docs  
---|---|---|---  
Agent Mode | Create a new project | Go from an idea to an app prototype quickly with the help of AI. | [Create a new project with AI](https://developer.android.com/studio/gemini/create-a-new-project-with-ai)  
Parallel conversations | Run multiple Agent Mode conversations in parallel to multitask effectively inside the IDE. | [Agent Mode](https://developer.android.com/studio/gemini/agent-mode#parallel-conversations)  
Add an API key | Add an API key to expand the context window and get even higher quality responses.   
  
Only applicable to users on the default model of the no-cost tier. | [Add your own Gemini API key](https://developer.android.com/studio/gemini/add-api-key)  
Add an MCP server | Interact with external tools and extend knowledge and capabilities using the Model Context Protocol (MCP). | [Add an MCP server](https://developer.android.com/studio/gemini/add-mcp-server)  
Add a remote MCP server | Connect to an MCP server without having to install and maintain it yourself. | [Add an MCP server](https://developer.android.com/studio/gemini/add-mcp-server)  
`AGENTS.md` file support | Define preferences for Gemini's responses to your queries in one or more Markdown files that are part of your codebase. Instructions defined in `AGENTS.md` files are IDE-independent. | [Customize Gemini using `AGENTS.md` files](https://developer.android.com/studio/gemini/agent-files)  
Manage permissions | You can manage specific permissions for the agent, giving you granular control over your workspace. | [Manage permissions in Agent Mode](https://developer.android.com/studio/gemini/permissions)  
Access the Android Knowledge Base | Access fresh, authoritative documentation to help you develop high-quality apps. | [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources#android-knowledge-base)  
Agent Web Search | Conduct real-time web searches to access fresh information. | [Agent Web Search](https://developer.android.com/studio/gemini/access-helpful-resources#agent-web-search)  
Extend Agent Mode with skills | Skills let you enhance Agent Mode's capabilities with specialized expertise and custom workflows. | [Extend Agent Mode with skills](https://developer.android.com/studio/gemini/skills)  
Interact with the connected device | The AI agent in Android Studio has access to tools to deploy an app to the connected device, inspect what is currently shown on the screen, take screenshots, check Logcat for errors, and interact with the running app. | [Test and verify changes on a device](https://developer.android.com/studio/gemini/agent-mode#use-cases)  
Local third-party models | Choose an LLM locally installed on your computer to power the AI functionality in Android Studio. | [Use a local LLM](https://developer.android.com/studio/gemini/use-a-local-model)  
Remote third-party models | Choose an LLM from a remote model provider to power the AI functionality in Android Studio. | [Use a remote LLM](https://developer.android.com/studio/gemini/use-a-remote-model)  
Code | Next Edit Prediction | Proactively suggests edits elsewhere in your codebase based on your recent changes. | [Next Edit Prediction](https://developer.android.com/studio/gemini/next-edit-prediction)  
Update dependencies | Update dependencies and iteratively resolve build errors along the way. | [Update dependencies with the Gemini agent](https://developer.android.com/studio/releases#update-dependencies)  
Generate unit tests | Gemini can generate comprehensive, compilable unit tests for your Kotlin and Java code, including `setUp` methods, mock initialization, and individual test cases. | [Generate unit tests](https://developer.android.com/studio/gemini/generate-unit-tests)  
Journeys with Gemini | Write end-to-end functional tests, called journeys, by describing the steps and assertions using natural language. Gemini converts your steps into actions that Gemini performs on your app.   
  
Enable through [Studio Labs](https://developer.android.com/studio/gemini/labs). | [Journeys for Android Studio](https://developer.android.com/studio/gemini/journeys)  
Compose | Compose preview generation | Gemini can automatically generate Compose previews, including mock data for preview parameters, for a specific composable or all composables in a file. | [Generate Compose previews](https://developer.android.com/studio/gemini/generate-compose-previews)  
Transform UI | Use natural language to update your app UI directly from the Compose preview panel. | [Transform UI](https://developer.android.com/studio/gemini/transform-ui)  
New UI from a design mock | Generate Compose code directly from a design mock. | [Generate UI with image attachment](https://developer.android.com/studio/gemini/generate-ui-with-images)  
Match UI to a target image | Make your UI match a reference design, when you already have an initial UI created. | [Generate UI with image attachment](https://developer.android.com/studio/gemini/generate-ui-with-images)  
Fix UI quality issues | Find and fix issues to improve your UI quality and accessibility. | [Find and fix UI quality issues](https://developer.android.com/studio/gemini/generate-ui-with-images#fix-ui-quality)  
Android-powered integrations | Analyze crashes with App Quality Insights | Use Gemini to analyze your App Quality Insights crash reports, generate insights, provide a crash summary, and (when possible) recommend next steps, including sample code and links to relevant documentation. | [Analyze crashes with App Quality Insights and Gemini](https://developer.android.com/studio/gemini/analyze-crashes-with-aqi)  
Analyze runtime errors with Logcat | Gemini in Android Studio helps you understand and resolve errors from the Logcat window, streamlining your debugging process. When your app throws an error or exception, click "Ask Gemini" to get immediate explanations and actionable suggestions without leaving the IDE. | [Analyze runtime errors with Logcat and Gemini](https://developer.android.com/studio/gemini/analyze-runtime-errors-with-logcat)  
Get help with build and sync errors | Gemini understands Gradle build and sync errors. When errors occur, click the "Ask Gemini" link in the build output to help you diagnose and fix the problems. |   
Privacy and security | Configure context sharing | Configure which files specifically are shared with Gemini using `.aiexclude` files. | [Configure context sharing](https://developer.android.com/studio/gemini/aiexclude)  
Logging | Collect Gemini activity in Cloud Logging, including prompts and responses and metadata such as lines of code accepted by the user.   
  
Business tier subscribers only. | [Access Gemini Enterprise usage audit logs with Cloud Logging](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs)  
VPC service controls | Establish a secure and controlled environment for coding to protect sensitive data and intellectual property.   
  
Business tier subscribers only. | [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls)  
Productivity metrics | Track your team's usage of Gemini in Android Studio and the impact it's had on your work, including metrics such as the rate of acceptance of code recommendations.   
  
Business tier subscribers only. | [View and export analytics data](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics)  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
