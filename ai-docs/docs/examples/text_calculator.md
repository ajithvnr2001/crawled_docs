---
url: https://ai.google.dev/examples/text_calculator/
title: Use external tools with generate_text
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:35.671906+00:00
---

# Use external tools with generate_text

> Source: https://ai.google.dev/examples/text_calculator/

[![](https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png)View on ai.google.dev](https://ai.google.dev/examples/text_calculator) |  [![](https://www.tensorflow.org/images/colab_logo_32px.png)Try a Colab notebook](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/examples/text_calculator.ipynb) |  [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View notebook on GitHub](https://github.com/google/generative-ai-docs/blob/main/site/en/examples/text_calculator.ipynb) For some use cases, you may want to stop the generation from a model to insert specific results. For example, language models may have trouble with complicated arithmetic problems like word problems. This tutorial shows an example of using an external tool with the `genai.generate_text` method to output the correct answer to a word problem. This particular example uses the [`numexpr`](https://github.com/pydata/numexpr) tool to perform the arithmetic but you can use this same procedure to integrate other tools specific to your use case. The following is an outline of the steps:

  1. Determine a `start` and `end` tag to demarcate the text to send the tool.
  2. Create a prompt instructing the model how to use the tags in its result.
  3. Include the `end` tag in the of `stop_sequences` passed to `generate_text`.
  4. From the model result, take the text between the `start` and `end` tags as input to the tool.
  5. Run the tool and add its output to the prompt.
  6. Call `generate_text` again, to have the model continue with the tool's output.



## Setup
    
    
    pip install -q google.generativeai
    
    
    import google.generativeai as genai
    genai.configure(api_key='YOUR API KEY')
    
    from google.api_core import retry
    
    @retry.Retry()
    def generate_text(*args, **kwargs):
      return genai.generate_text(*args, **kwargs)
    
    
    
    models = [m for m in genai.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)
    
    
    
    models/text-bison-001
    

## Try to solve the problem directly

Here's the word problem you're going to solve:
    
    
    question = """
    I have 77 houses, each with 31 cats.
    Each cat owns 14 mittens, and 6 hats.
    Each mitten was knit from 141m of yarn, each hat from 55m.
    How much yarn was needed to make all the items?
    """
    
    
    
    prompt_template = """
    You are an expert at solving word problems. Here's one:
    
    {question}
    
    Work through it step by step, and show your work.
    One step per line.
    
    Your solution:
    """
    

Try it as is:
    
    
    completion = generate_text(
        model=model,
        prompt=prompt_template.format(question=question),
        # The maximum length of the response
        max_output_tokens=800,
    )
    
    print(completion.result)
    
    
    
    In the houses there are 77 * 31 = 2387 cats.
    So they need 2387 * 14 = 33418 mittens.
    And they need 2387 * 6 = 14322 hats.
    In total they need 33418 * 141 + 14322 * 55 = 5554525m of yarn.
    The answer: 5554525.
    

The prompt as is usually returns an incorrect result. It generally gets the steps right but the arithmetic wrong. The answer should be:
    
    
    answer = 77*31*14*141 + 77*31*6*55
    answer
    
    
    
    5499648
    

## Tell the model to use a calculator

In this next attempt, give the model instructions on how to access the calculator. You can do that by specifying a `start` and `end` tag the model can use to indicate where a calculation is needed. Add something like the following to the prompt:
    
    
    calc_prompt_template = """
    You are an expert at solving word problems. Here's a question:
    
    {question}
    
    -------------------
    
    When solving this problem, use the calculator for any arithmetic.
    
    To use the calculator, put an expression between <calc></calc> tags.
    The answer will be printed after the </calc> tag.
    
    For example: 2 houses  * 8 cats/house = <calc>2 * 8</calc> = 16 cats
    
    -------------------
    
    Work through it step by step, and show your work.
    One step per line.
    
    Your solution:
    """
    
    calc_prompt = calc_prompt_template.format(question=question)
    

To give the model access to the output of this "calculator", you'll have to pause generation and insert the result. Use the `stop_sequences` argument to stop at the `</calc>` tag:
    
    
    completion = generate_text(
        model=model,
        prompt=calc_prompt,
        stop_sequences=["</calc>"],
        # The maximum length of the response
        max_output_tokens=800,
        candidate_count=1,
    )
    
    result = completion.result
    print(result)
    
    
    
    In each house, there are <calc>31 * 14
    

The `stop_sequence` is not included in the result. Split off the expression and run it through the calculator, and add it back to the result:
    
    
    # Use re to clear units from the calculator expressions
    import re
    # Use numexpr since `eval` is unsafe.
    import numexpr
    
    
    def calculator(result):
      result, expression = result.rsplit('<calc>', 1)
    
      # Strip any units like "cats / house"
      clean_expression = re.sub("[a-zA-Z]([ /a-zA-Z]*[a-zA-Z])?",'', expression)
    
      # `eval` is unsafe use numexpr
      result = f"{result}<calc>{expression}</calc> = {str(numexpr.evaluate(clean_expression))}"
      return result
    
    
    
    print(calculator(result))
    
    
    
    In each house, there are <calc>31 * 14</calc> = 434
    

Now append that to the prompt, and run the model again, so it can continue where it left off:
    
    
    continue_prompt=calc_prompt +"\n"+ "-"*80 + "\n" + calculator(result)
    
    completion = generate_text(
        model=model,
        prompt=continue_prompt,
        stop_sequences=["</calc>"],
        # The maximum length of the response
        max_output_tokens=800,
        candidate_count=1,
    )
    
    print(completion.result)
    
    
    
    mittens.
    In each house, there are <calc>31 * 6
    

This time, the model continued the text from the last calculation and moved on to the next. Now run it in a loop to fully solve the word problem:
    
    
    def solve(question=question):
      results = []
    
      for n in range(10):
        prompt = calc_prompt_template.format(question=question)
    
        prompt += " ".join(results)
    
        completion = generate_text(
            model=model,
            prompt=prompt,
            stop_sequences=["</calc>"],
            # The maximum length of the response
            max_output_tokens=800,
        )
    
        result = completion.result
        if '<calc>' in result:
          result = calculator(result)
    
        results.append(result)
        print('-'*40)
        print(result)
        if str(answer) in result:
          break
        if "<calc>" not in  result:
          break
    
      is_good = any(str(answer) in r for r in results)
    
      print("*"*100)
      if is_good:
        print("Success!")
      else:
        print("Failure!")
      print("*"*100)
    
      return is_good
    
    
    
    solve(question);
    
    
    
    ----------------------------------------
    The total number of cats is <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    The total number of mittens is <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens.
    The total amount of yarn needed for the mittens is <calc>33418 * 141</calc> = 4711938
    ----------------------------------------
    m.
    The total number of hats is <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats.
     The total amount of yarn needed for the hats is <calc>14322 * 55</calc> = 787710
    ----------------------------------------
    m.
    In total, <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    

You can run that a few times to estimate the solve rate:
    
    
    good = []
    
    for n in range(10):
      good.append(solve(question))
    
    
    
    ----------------------------------------
    There are <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    They need <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens.
    The mittens need <calc>33418 * 141</calc> = 4711938
    ----------------------------------------
    m of yarn.
    They need <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats.
    The hats need <calc>14322 * 55</calc> = 787710
    ----------------------------------------
    m of yarn.
     They need a total of <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    There are <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    So for the mittens, we need <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens.
    That means we need <calc>33418 * 141</calc> = 4711938
    ----------------------------------------
    m of yarn for mittens.
    For the hats, we need <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats.
    That means we need <calc>14322 * 55</calc> = 787710
    ----------------------------------------
    m of yarn for hats.
     In total we need <calc>787710 + 4711938</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    In the 77 houses I have <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    They need <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens.
    The mittens need <calc>33418 * 141</calc> = 4711938
    ----------------------------------------
    m of yarn.
    They need <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats.
    The hats need <calc>14322 * 55</calc> = 787710
    ----------------------------------------
    m of yarn.
     So, in total I need <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    The number of cats is <calc>77 * 31</calc> = 2387
    ----------------------------------------
    . Each cat needs <calc>14 * 141</calc> = 1974
    ----------------------------------------
    m of yarn for mittens. So we need <calc>1974 * 2387</calc> = 4711938
    ----------------------------------------
    m of yarn for mittens. Each cat needs <calc>6 * 55</calc> = 330
    ----------------------------------------
    m of yarn for hats. So we need <calc>330 * 2387</calc> = 787710
    ----------------------------------------
    m of yarn for hats. So in total we need <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    There are <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    Each cat needs <calc>14 * 141</calc> = 1974
    ----------------------------------------
    yarn for mittens.
    All cats need <calc>2387 * 1974</calc> = 4711938
    ----------------------------------------
    yarn for mittens.
    Each cat needs <calc>6 * 55</calc> = 330
    ----------------------------------------
    yarn for hats.
    All cats need <calc>2387 * 330</calc> = 787710
    ----------------------------------------
    yarn for hats.
     All in all, you need <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    There are <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    Each cat needs <calc>14 + 6</calc> = 20
    ----------------------------------------
    items.
    So we need <calc>20 * 2387</calc> = 47740
    ----------------------------------------
    items in total.
    Each mitten needs <calc>141</calc> = 141
    ----------------------------------------
    m of yarn.
    So all the mittens need <calc>141 * 47740</calc> = 6731340
    ----------------------------------------
    m of yarn.
     Each hat needs <calc>55</calc> = 55
    ----------------------------------------
    m of yarn.
    So all the hats need <calc>55 * 47740</calc> = 2625700
    ----------------------------------------
    m of yarn.
     In total, we need <calc>6731340 + 2625700</calc> = 9357040
    ----------------------------------------
    m of yarn. There are <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    Each cat needs <calc>14 + 6</calc> = 20
    ********************************************************************************
    Failure!
    ----------------------------------------
    There are <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    There are <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens.
    There are <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats.
    There was <calc>141 * 33418</calc> = 4711938
    ----------------------------------------
    m of yarn needed for mittens.
    There was <calc>55 * 14322</calc> = 787710
    ----------------------------------------
    m of yarn needed for hats.
     So there was <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    There are <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats in total. 
    They need <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens. 
    That's <calc>33418 * 141</calc> = 4711938
    ----------------------------------------
    meters of yarn for mittens. 
    They need <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats. 
    That's <calc>14322 * 55</calc> = 787710
    ----------------------------------------
    meters of yarn for hats. 
    So, they need <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    There are 77 houses * 31 cats / house = <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats.
    So we need <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens.
    So we need <calc>33418 * 141</calc> = 4711938
    ----------------------------------------
    m of yarn for mittens.
    So we need <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats.
     So we need <calc>14322 * 55</calc> = 787710
    ----------------------------------------
    m of yarn for hats.
    In total, we need <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    ----------------------------------------
    In total there are 77 houses * 31 cats / house = <calc>77 * 31</calc> = 2387
    ----------------------------------------
    cats. In total 2387 cats * 14 mittens / cat = <calc>2387 * 14</calc> = 33418
    ----------------------------------------
    mittens. In total 33418 mittens * 141m / mitten = <calc>33418 * 141</calc> = 4711938
    ----------------------------------------
    m of yarn for mittens. In total 2387 cats * 6 hats / cat = <calc>2387 * 6</calc> = 14322
    ----------------------------------------
    hats. In total 14322 hats * 55m / hat = <calc>14322 * 55</calc> = 787710
    ----------------------------------------
    m of yarn for hats. In total we need 4711938 m of yarn for mittens + 787710 m of yarn for hats = <calc>4711938 + 787710</calc> = 5499648
    ********************************************************************************
    Success!
    
    
    
    import numpy as np
    np.mean(good)
    
    
    
    0.9
    
