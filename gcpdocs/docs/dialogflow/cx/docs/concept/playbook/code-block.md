---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block/
title: Code blocks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:47:39.847679+00:00
---

# Code blocks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Code blocks Stay organized with collections  Save and categorize content based on your preferences. 

When defining a playbook, you can optionally provide _code blocks_ , which are inline Python code that lets you better control agent behavior. This code consists of functions with special decorators and any utility functions that you require.

When writing your code, you can use the [code block system library](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library) to control agent behavior.

## Limitations

The following limitations apply:

  * Code blocks can't contain any objects that persist data. However, you can use tools to persist data and maintain state.
  * Code blocks can't make remote calls directly. For example, you can't use the Python requests library. However, you can use tools to make remote calls indirectly.
  * Resource names that are converted to Python names must be [legal Python names](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#naming).
  * Code blocks can't write session parameters, unless a flow transition takes place.



## Inline actions

Inline actions behave similarly to [tool actions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example#tool-use). They have a defined input and output schema, which is determined by the Python function signature, including type annotations and docstring. Like tool calls, the LLM is unaware of the code that implements the action.

For example:
    
    
    @Action
    def is_prime(n: int) -> bool:
      """Returns true if n is prime."""
      if not isinstance(n, int) or n < 2:
        return False
    
      for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
          return False
    
      return True
    

For this function, the LLM receives information about the action, its input, and its output.

To reference an inline action in your playbook instructions, reference the action name in backticks and describe how to use it.

Here's an example for a `place_order` inline action:
    
    
    Take the customer's order, and then call the `place_order` action when the
    order is ready.
    

To create examples that use inline actions, use the **inline-action** tool type in the **Input & Output** section.

For more information, see the [@Action](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-action) reference documentation.

## Trigger functions

Trigger functions are used to define [conditional actions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions) in code.

You declare trigger functions by using decorators.

You can use the following trigger function decorators:

Decorator | Decorator Parameters | Description  
---|---|---  
[@EventTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-eventtrigger) | `event: str, condition: str`, where condition is optional | Triggered by an event  
[@BeforeModelTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-beforemodeltrigger) | `condition: str`, where condition is optional | Triggered every time before the LLM predicts the next action.  
[@BeforeActionTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-beforeactiontrigger) | `condition: str`, where condition is optional | Triggered every time before the LLM executes an action.  
[@BeforePlaybookTrigger](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#decorator-beforeplaybooktrigger) | `condition: str`, where condition is optional | Triggered the first time a playbook is started.  
  
For example, these functions show how to use these decorators and decorator parameters, and also how to use the [respond](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-respond) code block system library function.
    
    
    # No decorator parameter
    @PlaybookStartTrigger
    def my_playbook_conditional_action():
      respond("How can I help?")
    
    # With a condition decorator parameter
    @BeforeActionTrigger('$next-action.name = "search"')
    def my_before_action_conditional_action():
      respond("One moment please")
    
    # Event
    @EventTrigger(event="welcome")
    def my_welcome_event():
      respond("hi")
    
    # Event with a condition:
    @EventTrigger(event="welcome",
                  condition="$sys.func.NOW().hours < 10")
    def my_good_morning_event():
      respond("Good morning ☕")
    

## Referencing flows, playbooks, and tools

In your code block, you can reference specific flows, playbooks, and tools using the [flows](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#variable-flows), [playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#variable-playbooks), and [tools](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#variable-tools) global variables.

Each of these objects has members that match the names of the corresponding resources. These names need to be [legal Python names](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#naming).

For example:
    
    
      add_override(playbooks.troubleshooting, {})
      add_override(flows.billing)
      add_override(tools.weather_api.get_weather, {"location": "San Francisco"})
    

When you reference flows and playbooks in a code block, you must also reference them in the playbook instructions using the following syntax:
    
    
    ${RESOURCE_TYPE: my_resource_name}
    

For example, if your code block contains `flows.myflow` and `playbooks.myplaybook`, your playbook instructions should include:
    
    
    ${FLOW: myflow}
    ${PLAYBOOK: myplaybook}
    

## Action overrides

Use code blocks to create a queue of actions that will take place before any further actions determined by the LLM, and potentially override them. Create action overrides by using the [add_override](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-add_override) global function.

All queued override actions execute sequentially, and the action output is available to the LLM. Once the queue is empty, operation returns to the LLM for action and input selection, unless an override finishes the turn with [respond](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-respond) or another function that completes the turn.

Function arguments:

  * **Action:** Specify the action to take place. For an inline action, use `my_function_name`. For a tool action, use `tools.my_tool_name.my_tool_action`. For a flow action, use `flows.my_flow_name`.
  * **Inputs:** Specify optional inputs for the action, such as `{"location": "Omaha"}`.



For example:
    
    
    # Assuming remote tool named "dmv" with operationId "search_offices"
    # remote tool with only requestBody
    add_override(tools.dmv.search_offices,{"address": "95030"})
    
    # remote tool with only parameters
    add_override(tools.pets.get_pet, {"id": "123"})
    
    # remote tool with requestBody + parameters:
    add_override(tools.pets.create_pet, {"requestBody": {"arg1":"foo"}, "param1": "bar"})
    
    # datastore. Assumes existing datastore tool named "Menu".
    add_override(tools.menu.Menu, {"query": "what is the menu"})
    
    # code block action. Assumes another code block @Action my_action.
    add_override(my_action)
    

## Response overrides

You can use the [respond](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#function-respond) global function to force the agent to respond to the user with specific content, similar to action overrides, but specifically for agent responses.

For example:
    
    
    respond("Hello")
    

## Calling tools

You can call the tools that are defined for your agent in your code block functions. Unlike when you override a tool action, when you call a tool directly, the LLM cannot access the results of the tool execution.

For example:
    
    
    # Assumes existing tool named "DMV" with operationId "search_offices"
    # remote tool with only request body.
    offices = tools.dmv.search_offices({"address": "95030"})
    
    # remote tool with parameters and request body
    offices = tools.dmv.search_offices({"requestBody": {"address":"95030"}, "param1":"foo"})
    
    # datastore actions. Assumes existing datastore tool named "Menu".
    data = tools.menu.Menu({"query": "get the menu"})["snippets"]
    

## Match intent

Code blocks can programmatically match an intent for a given flow using the [Flow.match_intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library#class-flow-match_intent) function.

For example:
    
    
    matches = flows.flow1.match_intent(history.last_user_utterance).matches
    if matches and matches[0].intent == "some_intent":
      to_country = matches[0].parameters.get("to_country")
      if to_country:
        respond(f"To confirm, you're going to {to_country}, right?")
    

## Read session parameters

Code blocks can read [parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) that are available at the time of execution.

For example:
    
    
    state["$session.params.my-param"]
    state["$request.session-id"]
    

## Debugging

Use the simulator to debug your code block functions. These functions appear as actions in the simulator and provide debugging details as needed.

## Additional control

This document covers some common uses of the [code block system library](https://docs.cloud.google.com/dialogflow/cx/docs/reference/code-block-system-library). For additional types of control, see the library documentation.

[ Previous arrow_back  Playbook instructions  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction)

[ Next Playbook conditional actions  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
