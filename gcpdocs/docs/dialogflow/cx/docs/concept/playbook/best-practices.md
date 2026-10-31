---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/best-practices/
title: Playbook best practices \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:47:40.101514+00:00
---

# Playbook best practices  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/best-practices/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbook best practices Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Generative AI App Builder still refers to playbooks as **agents**. This term is updated to **playbook** in the console.

These best practices can help you build robust agents.

## Playbook name in natural language

Playbook names should be clear, descriptive, and in natural English. This helps AI Generator performance at runtime. For example, "Customer Help Center Playbook" is better than "company_specialist".

Keep all names under 64 characters, including English letters and spaces.

## Concise goals

Goals must concisely describe the playbook's purpose.

## Provide quality instructions

Use instructions to:

  * Reflect the step-by-step approach to solving an end-user problem.
  * Provide concise natural language sentences of high-level instructions.
  * Specify the scenarios for tool uses straightforwardly.



## At least one example for each playbook

Include at least one [example](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/examples) for each playbook, and aim for at least four examples. Include happy path scenarios.

Without enough examples, a playbook can result in unpredictable behavior. If your playbook isn't responding or behaving as you expect, missing or poorly defined examples are likely the cause. Try improving your examples or adding new ones.

## Precision of instructions and examples

While it helps to write clear and descriptive instructions, it's really the quality and quantity of your examples that determine the accuracy of the playbook's behavior. In other words, spend more time writing thorough examples than writing perfectly precise instructions.

## Reference tools in examples

If the playbook is designed to provide responses using tools, reference the tools in the examples corresponding to this type of request.

## Tool schema `operationId` field

When you define schemas for your tools, the `operationId` value is important. Your playbook instructions will reference this value.

Use these naming recommendations for this field:

  * Use only letters, numbers, and underscores.
  * Ensure the name is unique among all `operationId`s described in the schema.
  * Choose a meaningful name that reflects the provided capability.



## Tool schema validation

Validate your tool schema. You can use the [Swagger Editor](https://editor.swagger.io/) to check your openAPI 3.0 schema syntax.

## Handle empty tool results

When your playbook relies on a tool to inform its response, an empty tool result can lead to unpredictable playbook behavior. Sometimes, the playbook AI Generator will hallucinate information in a response instead of a tool result. To help prevent unpredictable behavior, add specific instructions to help make sure that the playbook AI Generator doesn't attempt to answer on its own.

Some use cases require you to ground playbook responses in tool results or provided data and mitigate responses based only on the knowledge of the playbook AI Generator.

Examples of instructions to mitigate hallucinations include the following:

  * "You must use the tool to answer all user questions."
  * "If you don't get any data back from the tool, respond that you don't know the answer to the user's query."
  * "Don't make up an answer if you don't get any data back from the tool. Instead, ask the user to rephrase their query or ask for clarification."



## Generate a schema with Gemini

[Gemini](https://gemini.google.com/) can generate a schema for you. For example, try asking it to create an example OpenAPI 3.0 schema for Google Calendar.

## Focused playbooks

Don't create very large and complex playbooks. Each playbook should accomplish a specific and clear task. If you have a complex playbook, consider breaking it down into smaller sub-playbooks.

## Avoid loops and recursion

Don't create loops or recursion when linking agents in your instructions. A loop can occur if you try routing to an ancestor playbook that, directly or indirectly, called the current one.

## Provide routing information to examples

When a playbook routes to another playbook, provide this information to the examples. Provide this information to an example from the **End example with output information** field of the **Input & Output** example section.

For example, the final sentence of this field could be "Reroute back to the default playbook for further queries."

## Use Dialogflow CX Messenger JavaScript functions for personalization

When you use Dialogflow CX Messenger, the following JavaScript functions let you send user personalization information from the web interface to the playbook:

  * [setQueryParameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/javascript-functions#setqueryparameters)
  * [setContext](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/javascript-functions#setcontext)



## Planning for performance

Generative features typically require several seconds or even tens of seconds to generate a response. While playbooks enhance conversational naturalness, it's important to manage response times to maintain a positive end-user experience.

To optimize performance, use these strategies:

  * **Balance generative feature usage:** Carefully consider the trade-off between the time required to execute multiple generative features and the value they bring to the conversation. Avoid overusing these features if they don't significantly contribute to the user's goal.
  * **Minimize generative feature input:** Aim to gather and process the minimum amount of information required for an AI Generator to generate a useful response. This can reduce processing time significantly.
  * **Use context caching:** If you're using Gemini through a tool and have a large initial context, explore caching information using [Vertex AI Context Caching](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview) to avoid repetitive requests for the same data.
  * **Implement fixed responses for speed:** If your application doesn't require unique, dynamic content, consider storing frequently used responses in a traditional database like Firebase. Because they're predefined and readily available, these fixed responses provide much faster response times than a generative feature that needs to calculate an answer on the fly.
  * **Instruct the AI Generator to produce concise playbook responses:** For text input and output, the AI Generator response time is highly dependent on the model being used and the **output** length. Short responses can significantly improve performance. While input length also factors in, output length has a larger impact.



[ Previous arrow_back  Playbook settings  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/playbook-settings)

[ Next Playbook evaluations  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
