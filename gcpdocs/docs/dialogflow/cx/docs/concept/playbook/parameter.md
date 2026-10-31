---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter/
title: Playbook parameters \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:47:38.830540+00:00
---

# Playbook parameters  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbook parameters Stay organized with collections  Save and categorize content based on your preferences. 

Playbooks accept and emit context information using explicitly defined parameters. Parameters store conversation information, such as user selections and action results. You can pass the values of these parameters between playbooks and [flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow).

## Parameter declaration

You can define input (read) parameters and output (write) parameters.

Parameters have a name, description, and one of the following types:

  * String
  * Number
  * Boolean
  * Tool-specific parameter type



You can also specify whether a parameter is a list.

## Input (read) parameters

For each playbook, you can define _input parameters_ , also called _read parameters_ , that let playbooks use values passed from flows and other playbooks. For example, a playbook might receive a user's preferred name as a parameter and use it to thank the user personally, or it might receive an order identifier as a parameter and use it to retrieve order details using a [tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool).

Input parameters are defined per playbook, and playbooks don't have access to [other Dialogflow CX console parameter types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) by default. When a flow transitions to a playbook, page and session parameters are propagated to the playbook if the target playbook has an input parameter with the same name. To communicate information from a flow to a playbook during a transition, define playbook input parameters with the same name as a session or page parameter present before the transition.

**Note:** The default playbook doesn't accept input parameters because it serves as an entry point for user conversations and has no way to receive them.

Create examples to control how the input parameter value should affect actions. For example, if an input parameter should affect how the agent refers to the user, create examples that define a value for the parameter and then use the same value in utterance actions within the example. For more information, see passing parameters.

## Output (write, return) parameters

For each playbook, you can define _output parameters_ , also called _write parameters_ and _return parameters_ , that let playbooks emit information to be used by other flows or playbooks. For example, a playbook might collect an order number from a user and emit it through an output parameter, or a playbook might use a [tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) to book a flight and emit the confirmation number through an output parameter.

Create examples to control how playbooks determine the value for each output parameter. For example, if an output parameter representing a confirmation number derives its value from a tool use output, create examples where the tool output matches the value of the playbook output parameter.

## Passing parameters

**Note:** Because a task playbook can't call a routine playbook, that parameter passing scenario isn't described in the following sections.

Playbooks, unlike flows, **don't** support injecting parameter values with a particular syntax. Instead, playbooks rely on instructions and [few-shot prompt examples](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/learn/introduction-prompt-design#include-examples) to determine how parameter values should be used and decided.

### Routine playbook to flow

To pass parameters from a routine playbook to a flow:

  * Define write parameters for the routine playbook, which become session parameters when the routine playbook completes.
  * Use the session parameters in flows.
  * Include parameter usage in instructions and examples.



### Flow to routine playbook

To pass parameters from a flow to a routine playbook:

  * Write the session parameters from the flow.
  * Define read parameters for the routine playbook with the same names.
  * Include parameter usage in instructions and examples.



### Task playbook to flow

To pass parameters from a task playbook to a flow:

  * In the flow settings, define _input parameters_ of the same names.
  * Include parameter usage in instructions and examples.



### Flow to task playbook

To pass parameters from a flow to a parent task playbook:

  * In the flow settings, define _return parameters_.
  * Include parameter usage in instructions and examples.



To pass parameters from a flow to a child task playbook:

  * Define task input parameters in the task playbook that share the same name as session parameters in the flow.
  * Include parameter usage in instructions and examples.



### Routine playbook to task playbook

To pass parameters from a routine playbook to a task playbook:

  * Define input parameters for the task playbook using the same names.
  * Include parameter usage in instructions and examples.



### Sample involving tools

Suppose that an agent is designed for event ticket sales with the following task playbooks:

  * A playbook named `Ticket ordering` that places orders by using a tool named `Ticket sales API`. 
    * This playbook accepts an input parameter of type `number` named `event_id`.
    * The `Ticket sales API` tool expects a request including an `event_id`.
  * A playbook named `Event selection` that helps users select an event and then routes them to `Ticket ordering` with the parameter `event_id` to purchase tickets.



In this example, to ensure that `event_id` is reliably passed from `Event selection` to `Ticket ordering` and from `Ticket ordering` to `Ticket sales API`, you need several [examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example).

The `Ticket ordering` playbook should include multiple examples that:

  * Specify the input parameter `event_id` with a realistic value that differs in each example.
  * Include a tool use action with a request body that includes **the same** realistic `event_id` value as specified in the input parameter.



The `Event selection` playbook should include multiple examples that:

  * Include a user utterance where an event with a realistic `event_id` is selected, with a different ID in each example.
  * Include a playbook invocation of `Ticket ordering` that sets the `event_id` parameter to the same realistic `event_id` as determined by the selection.



Besides adding examples, add specific instructions to the [instructions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction), [goal](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/goal), or [tool details](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) explaining how parameters should be used.

For example, the `Ticket ordering` playbook can include the following instruction:
    
    
    - Use parameter event_id to send a buy_tickets request with ${TOOL: Ticket sales API}
    

With the described examples and instructions present, the `Event selection` playbook correctly decides an `event_id` based on the user's selection and passes it as an input parameter named `event_id` to the `Ticket ordering` playbook. Then, `Ticket ordering` passes the same `event_id` in the body of a request to the `Ticket sales API`. Playbooks depend on examples with distinct parameter values to help them infer how parameters are used.

[ Previous arrow_back  Playbook examples  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example)

[ Next Playbook tools  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
