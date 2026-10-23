---
url: https://ai.google.dev/gemma/docs/codegemma/prompt-structure/
title: CodeGemma formatting and system instructions
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:39.358588+00:00
---

# CodeGemma formatting and system instructions

> Source: https://ai.google.dev/gemma/docs/codegemma/prompt-structure/

Gemma instruction-tuned (IT) models are trained with a specific _formatter_ that annotates all instruction tuning examples with extra information, both at training and inference time. CodeGemma uses the Gemma general prompt structure as described in [Gemma formatting and system instructions](https://ai.google.dev/gemma/docs/core/prompt-structure).

The CodeGemma 2B and 7B variants are specially tuned for code infilling tasks. Specifically, they are trained on four formatting control tokens that you can use to help construct model prompts for fill-in-the-middle (FIM) coding tasks.

Context| Token  
---|---  
FIM prefix | `<|fim_prefix|>`  
FIM suffix | `<|fim_suffix|>`  
FIM middle | `<|fim_middle|>`  
File separator | `<|file_separator|>`  
  
Use the FIM tokens to define the cursor location and surrounding context around it for CodeGemma to perform code infilling. Use the file separator token for multi-file contexts.

## Fill in task example

Consider the following code:
    
    
    import |⏎ # Line 1
    if __name__ == '__main__':⏎ # Line 2
       sys.exit(0) # Line 3
    

The `|` indicates the location of the cursor which is where the code needs to be completed. Note that there is a space before the cursor and that lines 1 and 2 have carriage returns at the end.

The prefix is then,
    
    
    import
    

with one space at the end.

The suffix is:
    
    
    ⏎
    if __name__ == '__main__':⏎
       sys.exit(0)
    

with a new line at the start.

The prompt should be constructed as:
    
    
    <|fim_prefix|>import <|fim_suffix|>⏎
    if __name == '__main__':⏎
       sys.exit(0)<|fim_middle|>
    

Note that:

  * There should be no extra white spaces between any FIM tokens and the prefix and suffix
  * The FIM middle token should be at the end to prime the model to continue filling in
  * The prefix or the suffix could be empty depending on where the cursor currently is in the file, or how much context you want to provide the model with



You can see a more complete version of this example in the [Keras CodeGemma quickstart](https://ai.google.dev/gemma/docs/codegemma/keras_quickstart).

## Understanding model output

The model response for the example above would be:
    
    
    <|fim_prefix|>import <|fim_suffix|>⏎
    if __name__ == "__main__":\n    sys.exit(0)<|fim_middle|>sys\n<|file_separator|>
    

The model repeats the input prompt and provides `sys` as the code completion.

When using the CodeGemma models for FIM tasks, stream response tokens and use the FIM or file separator tokens as delimiters to stop streaming and get the resulting code completion.
