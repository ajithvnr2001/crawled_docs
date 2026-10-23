---
url: https://ai.google.dev/gemma/docs/meme-generator/
title: Meme Generator
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:55.700046+00:00
---

# Meme Generator

> Source: https://ai.google.dev/gemma/docs/meme-generator/

This guide offers a practical approach to implementing an application using function calling with Gemma. This technique can be applied to various Gemma model versions through careful prompt engineering. You can find more information in [Beyond the Chatbot: Agentic AI with Gemma](https://developers.googleblog.com/beyond-the-chatbot-agentic-ai-with-gemma/).

## Function Calls Explained

The common structure for function calling involves a few key components, designed to allow Gemma to interact with external tools or APIs.

  1. **Describe the tools**  
You tell the model about the "tools" (functions) it can use. This includes:

     * What the tool does (description)
     * What information the tool needs (parameters)
  2. **User asks a question**  
You ask the model a question or give it a task

  3. **Gemma decides**  
The model figures out if it needs a tool to answer your question.

  4. **Gemma requests a tool**  
If a tool is needed, Gemma will generate a code wrapped with ```tool_code```

  5. **Tool does its job**  
The tool (function) takes the information from the model and does what it's supposed to do.

  6. **Tool gives back results**  
Gemma is expecting to get its result back wrapped with ```tool_output```

  7. **Gemma gives final answer**  
The model uses the tool's results to create a complete and accurate answer for you.




**Helpful Hints**

  * **JSON Schema** : Using JSON Schema for parameter definitions, though not mandatory, offers the advantages of consistent structure and automated validation.
  * **Clear Understanding** : The quality of the function's description is critical for the model to correctly identify when to use it.
  * **Error Handling** : Robust error handling is essential to manage cases where the function call fails or returns unexpected results.
  * **Iterative Process** : Sometimes there are multiple turns of conversation between the model, and the function calls.



## Example Prompts and Outputs

You can find the code for this application in the [Gemma Cookbook code repository](https://github.com/google-gemini/gemma-cookbook/tree/main/Gemma/%5BGemma_3%5DMeme_Generator.ipynb).

Step 1 and 2: Describe the tool and give a task

![A funny image of a cat](https://ai.google.dev/gemma/docs/capabilities/vision/images/surprise.png)

Input: A funny image of a cat  
Text Input:
    
    
    If you decide to invoke any of the function(s), it should be wrapped with ```tool_code```.
    
    You have access to the following tools.
    
    * `generate_meme(image, top_text, middle_text, bottom_text)`: Generate a meme with the given parameters
    
    Make a funny meme with this. "meme.jpg"
    

Step 3: Gemma decides and requests a tool

This prompt would produce the following response:
    
    
    Okay, here's a funny meme based on the image of the surprised cat:
    
    ```tool_code
    generate_meme(image="meme.jpg", top_text="Me when I hear a creak", middle_text="Is it safe?", bottom_text="Probably not.")
    ```
    

Step 4: Tool does its job

You will process the model's output by locating the code blocks, parse function arguments, and execute the functions.

![Final Output from the Meme Generator](https://ai.google.dev/gemma/docs/images/meme-generator.png)
