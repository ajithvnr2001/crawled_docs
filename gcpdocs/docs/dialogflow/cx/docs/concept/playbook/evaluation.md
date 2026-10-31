---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation/
title: Playbook evaluations \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:47:38.978243+00:00
---

# Playbook evaluations  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbook evaluations Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to use the built-in evaluations feature in the Dialogflow CX console to verify your agent's capabilities and prevent any regressions after updates. Dialogflow CX provides [out-of-the-box metrics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation#test_results) to help evaluate your agent's performance.

All metrics except for latency require at least one **test case** , a "golden response" that Dialogflow CX compares the agent's performance against to measure results. Each test case can be measured in the context of an **environment** , which lets you specify different versions of playbooks, flows, and tools to use in the agent's performance evaluation.

## (Optional) Create an environment

Creating an environment is optional. If you don't create one, the default value is **Draft**.

  1. Go to **Environments** and click **Create**.
  2. Choose the versions of the playbooks, flows, and tools that you want to use to measure agent performance.
  3. Click **Save** to save the environment.



## Create a test case

You can create a test case from an existing conversation in your conversation history, create a new conversation to save as a test case, or import test cases into Dialogflow CX.

### Create a test case in the console

  1. Go to **Conversation history** in the navigation menu.
  2. To create a new conversation, activate your agent, such as by calling the agent's phone number. When you have a conversation that you want to use as a test case, select it.
  3. View the conversation and verify the agent responses, tools invoked, and how each response sounds. When you're satisfied, select **Create test case**.
  4. Provide a display name for the test case and specify your expectations of events that must happen at the conversation level. This can include tools, playbooks, and flows that you expect to be called within the conversation. Select **+Add expectation** to add more expectations. To have the expectations evaluated in sequential order as listed from top to bottom, toggle **Sequential validation**.
  5. Click **Save** to save the test case.



### Upload test cases

  1. Test cases must be in [the following CSV format](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation#batch_import_test_cases_formatting).
  2. To upload test cases to the system, click **Import** at the top of the test cases menu.
  3. In the menu that appears, either select the locally stored file or enter the path to its Cloud Storage bucket.
  4. Your test cases should now appear in the test cases menu.



## Run a test case

  1. Go to **Test cases** in the navigation menu and select the test cases that you want to compare your agent against. You can select a single test case or multiple test cases.
  2. Click **Run selected test cases**.



## Test results

  1. **Access results:** The latest test run execution results appear for each test case in the _Test Case_ view after completion: 
     1. **Semantic similarity:** Measures how similar the agent's conversations were to the "golden response" (responses in the Test Case). Golden responses are required to receive this metric. Values can be 0 (inconsistent), 0.5 (somewhat consistent), or 1 (very consistent).
     2. **Tool call accuracy:** Reflects how faithfully the conversation includes the tools that are expected to be invoked during the conversation. Values range from 0 to 1. If no tools are used in the conversation, the accuracy appears as `--` (not applicable).
     3. **Latency:** The total time that the agent takes to process a user request and respond to the user, measured as the difference between the end of the user utterance and the beginning of the agent response in seconds.
  2. **Update golden test case:** If the latest run reflects expected changes due to an agent update, select **Save as golden** to overwrite the original Test Case.
  3. **Filter and sort results:** You can filter and sort evaluation results by any of the generated metrics or by a specific Environment to track changes in performance after each update.



## Batch import test case formatting

This section describes how to format a CSV file for importing batch test cases for your agent. The system reads this file to create a structured set of test cases, each containing one or more conversational turns.

A single test case can span multiple rows in the CSV file. The first row of a test case defines its overall properties, for example, its name and language. Each subsequent row for that test case defines a single back-and-forth turn in the conversation where the user says something and the agent replies.

### Header

The CSV file must have a header row as the very first line. This header defines the data in each column.

#### Required headers

The two required headers must appear in the order shown. Both are required for the first row of a new test case. You can start a new test case by providing new `DisplayName` and `LanguageCode` values.

  * `DisplayName`: The name of your test case. This is only filled in for the first row of a new test case.
  * `LanguageCode`: The language code for the test (for example, `en`, `en-US`, `es`).



#### Optional headers

You can include the following optional headers to provide more detail for your test cases. They can be in any order after the first two required columns.

Test case metadata:

  * Tags: Space-separated tags for organizing tests (for example, "payments onboarding").
  * Note: Free-text notes or a description of the test case purpose.
  * `TestCaseConfigV2.StartResource`: Specify the flow or playbook to start the test with.



User input:

  * `UserInput.Input.Text`: The text the user enters for a given turn.
  * `UserInput.InjectedParameters`: Parameters to inject into the conversation at the start of a turn, formatted as a JSON string.



Agent output:

  * `AgentOutput.QueryResult.ResponseMessages.Text`: The exact text that the agent replied with.
  * `AgentOutput.QueryResult.Parameters`: The parameters that were extracted by the agent, formatted as a JSON string.



Ordered expectations:

  * `OrderedExpectations.ExpectedFlow`: The flow you expect to be active after the turn.
  * `OrderedExpectations.ExpectedIntent`: The intent you expect to be matched for the turn.
  * `OrderedExpectations.ExpectedAgentReply`: The text you expect the agent to reply with, which can be a substring of the full reply.
  * `OrderedExpectations.ExpectedOutputParameter`: The parameters you expect to be set at the end of the turn, formatted as a JSON string.



Audio metadata:

  * `AudioTurnMetadata`: Metadata for audio-based tests, formatted as a JSON string.



### Build a test case

Test cases are organized by data rows.

  1. To start a new test case, fill out its metadata row: 
     * **Rule:** This row must have a value in the `DisplayName` column.
     * **Action:** Enter values for `DisplayName` and `LanguageCode`. Include tags, notes, or a `TestCaseConfigV2.StartResource` in this row as needed. Leave conversation-turn columns (such as `UserInput.Input.Text`) empty in this row. If you use tags, separate each tag with a space (for example, `tag1 tag2 tag3`). If you use `TestCaseConfigV2.StartResource`, prefix the resource name with `start_flow:` or `start_playbook:` (for example, `start_flow:projects/p/locations/l/agents/a/flows/f`).
  2. Add a conversational turn to the test case you just started by adding a new row immediately below it: 
     * **Rule:** The `DisplayName` column must be empty. This tells the parser that it's a turn belonging to the previous test case.
     * **Action:** Fill in the columns that describe the user's action and the expected agent response for this turn, such as `UserInput.Input.Text` and `OrderedExpectations.ExpectedAgentReply`. For columns requiring JSON, you must provide a valid JSON object as a string (for example, `{"param_name": "param_value", "number_param": 123}`).



[ Previous arrow_back  Playbook best practices  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/best-practices)

[ Next Data stores  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
