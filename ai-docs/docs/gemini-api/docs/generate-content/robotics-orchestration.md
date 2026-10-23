---
url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration/
title: Task orchestration
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:43:45.591937+00:00
---

# Task orchestration

> Source: https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration/

Gemini Robotics ER models can plan tasks and reason about space, inferring which actions to take and which objects to move to complete a goal. This page shows an example for driving a pick-and-place operation through a custom robot API to orchestrate the task of placing an item into a bowl.

For full runnable code, see the [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Using a custom robot API

This example demonstrates task orchestration with a custom robot API. It introduces a mock API designed for a pick-and-place operation. The task is to pick up a blue block and place it in an orange bowl:

![An image of the block and bowl](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png)

This example uses the following mock robot API and tool definitions:

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    def move(x, y, high):
        print(f"Mock Robot: Moving to coordinates: {x}, {y}, {'high above table' if high else 'down at table level'}")
    
    def setGripperState(opened):
        print(f"Mock Robot: {'Opening gripper' if opened else 'Closing gripper'}")
    
    robot_origin_y = 300
    robot_origin_x = 500
    
    move_declaration = types.FunctionDeclaration(
        name="move",
        description="Moves the arm to the given coordinates.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "x": types.Schema(type=types.Type.INTEGER, description="X coordinate relative to the origin"),
                "y": types.Schema(type=types.Type.INTEGER, description="Y coordinate relative to the origin"),
                "high": types.Schema(type=types.Type.BOOLEAN, description="Set to True to lift the robot arm above the scene. Set to False to place the gripper on the surface."),
            },
            required=["x", "y", "high"],
        ),
    )
    
    set_gripper_state_declaration = types.FunctionDeclaration(
        name="setGripperState",
        description="Opens or closes the robot's gripper.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "opened": types.Schema(type=types.Type.BOOLEAN, description="True opens the gripper, False closes the gripper."),
            },
            required=["opened"],
        ),
    )
    
    robot_tools = types.Tool(function_declarations=[move_declaration, set_gripper_state_declaration])
    

The following example sends the prompt and image to the model with the tool definitions. It then runs an agentic loop: after each model response, it executes any requested function calls (`move`, `setGripperState`), returns the results back to the model, and repeats until the model stops calling functions or the step limit is reached.

### Python
    
    
    with open("robot-api-example.png", "rb") as f:
        img_bytes = f.read()
    
    prompt = (
        "You are a robotic arm with six degrees-of-freedom. "
        f"The origin point for calculating the moves is at normalized point y={robot_origin_y}, x={robot_origin_x}. "
        "Use this as the new (0,0) for calculating moves, allowing x and y to be negative.\n\n"
        "Find the blue block and the orange bowl. Calculate their coordinates relative to the origin.\n"
        "Perform a pick and place operation where you pick up the blue block and place it into the orange bowl. "
        "Call the appropriate sequence of functions to complete this operation."
    )
    
    contents = [
        types.Content(role="user", parts=[
            types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
            types.Part(text=prompt),
        ])
    ]
    
    print("\n--- Executing Orchestrated Plan ---")
    
    max_steps = 15  # Safety limit to prevent infinite loops
    step_count = 0
    
    # The Agentic Loop
    while step_count < max_steps:
        step_count += 1
    
        response = client.models.generate_content(
            model="gemini-robotics-er-2-preview",
            contents=contents,
            config=types.GenerateContentConfig(
                tools=[robot_tools],
                thinking_config=types.ThinkingConfig(thinking_level="low"),
            ),
        )
    
        # Add model response to conversation history
        contents.append(response.candidates[0].content)
    
        # Check for function calls
        function_calls = [part for part in response.candidates[0].content.parts if part.function_call]
    
        if not function_calls:
            # Model is done calling functions
            print("Sequence complete.")
            print(f"Model Summary: {response.text}")
            break
    
        # Execute function calls and collect results
        function_response_parts = []
        for part in function_calls:
            fc = part.function_call
            if fc.name == "move":
                move(**fc.args)
            elif fc.name == "setGripperState":
                setGripperState(**fc.args)
    
            function_response_parts.append(
                types.Part.from_function_response(
                    name=fc.name,
                    response={"status": "success"},
                )
            )
    
        # Send function results back to model
        contents.append(types.Content(role="user", parts=function_response_parts))
    

The following shows a possible output of the model based on the prompt and the mock robot API. The output includes the output of the robot function calls that the model sequenced together.
    
    
    --- Executing Orchestrated Plan ---
    Mock Robot: Opening gripper
    Mock Robot: Moving to coordinates: 160, 440, high above table
    Mock Robot: Moving to coordinates: 160, 440, down at table level
    Mock Robot: Closing gripper
    Mock Robot: Moving to coordinates: 160, 440, high above table
    Mock Robot: Moving to coordinates: -250, 60, high above table
    Mock Robot: Moving to coordinates: -250, 60, down at table level
    Mock Robot: Opening gripper
    Mock Robot: Moving to coordinates: -250, 60, high above table
    Sequence complete.
    Model Summary: I have completed the task of picking up the blue block and placing it into the orange bowl.
    

## What's next

  * [Robotics with streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming) — real-time streaming with function calling (Gemini Robotics ER 2 only).
  * [Video understanding](https://ai.google.dev/gemini-api/docs/robotics-video-progress) — track task progress from video (ER 2 only).
  * [Spatial reasoning](https://ai.google.dev/gemini-api/docs/robotics-spatial) — pointing, tracking, and bounding box examples.


