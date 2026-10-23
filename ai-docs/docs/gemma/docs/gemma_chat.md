---
url: https://ai.google.dev/gemma/docs/gemma_chat/
title: Building a chatbot with Gemma
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:45:54.642152+00:00
---

# Building a chatbot with Gemma

> Source: https://ai.google.dev/gemma/docs/gemma_chat/

[![](https://ai.google.dev/static/site-assets/images/docs/notebook-site-button.png)View on ai.google.dev](https://ai.google.dev/gemma/docs/gemma_chat) |  [![](https://www.tensorflow.org/images/colab_logo_32px.png)Run in Google Colab](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/docs/gemma_chat.ipynb) |  [![](https://www.kaggle.com/static/images/logos/kaggle-logo-transparent-300.png)Run in Kaggle](https://kaggle.com/kernels/welcome?src=https://github.com/google-gemma/cookbook/blob/main/docs/gemma_chat.ipynb) |  [![](https://ai.google.dev/images/cloud-icon.svg)Open in Vertex AI](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2Fgoogle-gemma%2Fcookbook%2Fmain%2Fdocs%2Fgemma_chat.ipynb) |  [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://github.com/google-gemma/cookbook/blob/main/docs/gemma_chat.ipynb) Large Language Models (LLMs) such as Gemma excel at generating informative responses, making them ideal for building virtual assistants and chatbots. Conventionally, LLMs operate in a stateless manner, meaning they lack an inherent memory to store past conversations. Each prompt or question is processed independently, disregarding prior interactions. However, a crucial aspect of natural conversation is the ability to retain context from prior interactions. To overcome this limitation and enable LLMs to maintain conversation context, they must be explicitly provided with relevant information such as the conversation history (or pertinent parts) into each new prompt presented to the LLM. This tutorial shows you how to develop a chatbot using the instruction-tuned model variant of Gemma.

## Setup

### Gemma setup

To complete this tutorial, you'll first need to complete the setup instructions at [Gemma setup](https://ai.google.dev/gemma/docs/setup). The Gemma setup instructions show you how to do the following:

  * Get access to Gemma on kaggle.com.
  * Select a Colab runtime with sufficient resources to run the Gemma 2B model.
  * Generate and configure a Kaggle username and API key.

After you've completed the Gemma setup, move on to the next section, where you'll set environment variables for your Colab environment.

### Set environment variables

Set environment variables for `KAGGLE_USERNAME` and `KAGGLE_KEY`.
    
    
    import os
    from google.colab import userdata
    
    # Note: `userdata.get` is a Colab API. If you're not using Colab, set the env
    # vars as appropriate for your system.
    os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME')
    os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY')
    

### Install dependencies

Install Keras and KerasNLP.
    
    
    # Install Keras 3 last. See https://keras.io/getting_started/ for more details.
    pip install -q tensorflow-cpu
    pip install -q -U keras-nlp tensorflow-hub
    pip install -q -U "keras>=3"
    pip install -q -U tensorflow-text

### Select a backend

Keras is a high-level, multi-framework deep learning API designed for simplicity and ease of use. [Keras 3](https://keras.io/keras_3) lets you choose the backend: TensorFlow, JAX, or PyTorch. All three will work for this tutorial.
    
    
    import os
    
    # Select JAX as the backend
    os.environ["KERAS_BACKEND"] = "jax"
    
    # Pre-allocate 100% of TPU memory to minimize memory fragmentation
    os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"] = "1.0"
    

### Import packages

Import Keras and KerasNLP.
    
    
    import keras
    import keras_nlp
    
    # for reproducibility
    keras.utils.set_random_seed(42)
    

### Instantiate the model

KerasNLP provides implementations of many popular [model architectures](https://keras.io/api/keras_nlp/models/). In this tutorial, you'll instantiate the model using `GemmaCausalLM`, an end-to-end Gemma model for causal language modeling. A causal language model predicts the next token based on previous tokens. Instantiate the model using the `from_preset` method:
    
    
    gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma2_instruct_2b_en")
    

The `GemmaCausalLM.from_preset()` function instantiates the model from a preset architecture and weights. In the code above, the string `"gemma2_instruct_2b_en"` specifies the preset the Gemma 2 2B model with 2 billion parameters. Gemma models with [7B, 9B, and 27B parameters](https://ai.google.com/gemma/docs/get_started#models-list) are also available. You can find the code strings for Gemma models in their **Model Variation** listings on [Kaggle](https://www.kaggle.com/models/google/gemma). Use the `summary` method to get more info about the model:
    
    
    gemma_lm.summary()
    

As you can see from the summary, the model has 2.6 billion trainable parameters.

### Define formatting helper functions
    
    
    from IPython.display import Markdown
    import textwrap
    
    def display_chat(prompt, text):
      formatted_prompt = "<font size='+1' color='brown'>🙋‍♂️<blockquote>" + prompt + "</blockquote></font>"
      text = text.replace('•', '  *')
      text = textwrap.indent(text, '> ', predicate=lambda _: True)
      formatted_text = "<font size='+1' color='teal'>🤖\n\n" + text + "\n</font>"
      return Markdown(formatted_prompt+formatted_text)
    
    def to_markdown(text):
      text = text.replace('•', '  *')
      return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    

## Building the chatbot

The Gemma instruction-tuned model `gemma2_instruct_2b_en` is fine-tuned to understand the following turn tokens:
    
    
    <start_of_turn>user\n  ... <end_of_turn>\n
    <start_of_turn>model\n ... <end_of_turn>\n
    

This tutorial uses these tokens to build the chatbot. Refer to [Formatting and system instructions](https://ai.google.dev/gemma/docs/formatting) for more information on Gemma control tokens.

### Create a chat helper to manage the conversation state
    
    
    class ChatState():
      """
      Manages the conversation history for a turn-based chatbot
      Follows the turn-based conversation guidelines for the Gemma family of models
      documented at https://ai.google.dev/gemma/docs/formatting
      """
    
      __START_TURN_USER__ = "<start_of_turn>user\n"
      __START_TURN_MODEL__ = "<start_of_turn>model\n"
      __END_TURN__ = "<end_of_turn>\n"
    
      def __init__(self, model, system=""):
        """
        Initializes the chat state.
    
        Args:
            model: The language model to use for generating responses.
            system: (Optional) System instructions or bot description.
        """
        self.model = model
        self.system = system
        self.history = []
    
      def add_to_history_as_user(self, message):
          """
          Adds a user message to the history with start/end turn markers.
          """
          self.history.append(self.__START_TURN_USER__ + message + self.__END_TURN__)
    
      def add_to_history_as_model(self, message):
          """
          Adds a model response to the history with start/end turn markers.
          """
          self.history.append(self.__START_TURN_MODEL__ + message)
    
      def get_history(self):
          """
          Returns the entire chat history as a single string.
          """
          return "".join([*self.history])
    
      def get_full_prompt(self):
        """
        Builds the prompt for the language model, including history and system description.
        """
        prompt = self.get_history() + self.__START_TURN_MODEL__
        if len(self.system)>0:
          prompt = self.system + "\n" + prompt
        return prompt
    
      def send_message(self, message):
        """
        Handles sending a user message and getting a model response.
    
        Args:
            message: The user's message.
    
        Returns:
            The model's response.
        """
        self.add_to_history_as_user(message)
        prompt = self.get_full_prompt()
        response = self.model.generate(prompt, max_length=2048)
        result = response.replace(prompt, "")  # Extract only the new response
        self.add_to_history_as_model(result)
        return result
    

### Chat with the model

Start chatting with the model.
    
    
    chat = ChatState(gemma_lm)
    message = "Tell me, in a few words,  how to compute all prime numbers up to 1000?"
    display_chat(message, chat.send_message(message))
    

🙋‍♂️

> Tell me, in a few words, how to compute all prime numbers up to 1000?

🤖

> **Sieve of Eratosthenes.**

Continue the conversation.
    
    
    message = "Now in Python! No numpy, please!"
    display_chat(message, chat.send_message(message))
    

🙋‍♂️

> Now in Python! No numpy, please!

🤖

> 
>     def sieve_of_eratosthenes(n):
>       """Returns a list of prime numbers up to n."""
>       primes = [True] * (n + 1)
>       primes[0] = primes[1] = False
>       for i in range(2, int(n**0.5) + 1):
>         if primes[i]:
>           for j in range(i * i, n + 1, i):
>             primes[j] = False
>       return [i for i, is_prime in enumerate(primes) if is_prime]
>     
>     primes = sieve_of_eratosthenes(1000)
>     print(primes)
>     
> 
> **Explanation:**
> 
>   1. **Initialization:**
>      * `primes = [True] * (n + 1)`: Creates a list `primes` of boolean values, initially assuming all numbers are prime.
>      * `primes[0] = primes[1] = False`: Sets 0 and 1 as non-prime.
>   2. **Iteration:**
>      * `for i in range(2, int(n**0.5) + 1):`: Iterates from 2 to the square root of `n`. We only need to check up to the square root because any composite number must have a prime factor less than or equal to its square root.
>      * `if primes[i]:`: If `i` is marked as prime: 
>        * `for j in range(i * i, n + 1, i):`: Marks all multiples of `i` as non-prime.
>   3. **Result:**
>      * `return [i for i, is_prime in enumerate(primes) if is_prime]`: Creates a list of indices where `primes[i]` is True, representing the prime numbers.
> 
Let me know if you'd like a more detailed explanation of any part! 
    
    
    message = "Thank you, it works! Can you explain the code in French?"
    display_chat(message, chat.send_message(message))
    

🙋‍♂️

> Thank you, it works! Can you explain the code in French?

🤖

> Bien sûr ! Voici une explication du code en français :
>     
>     
>     def sieve_of_eratosthenes(n):
>       """Retourne une liste de nombres premiers jusqu'à n."""
>       primes = [True] * (n + 1)
>       primes[0] = primes[1] = False
>       for i in range(2, int(n**0.5) + 1):
>         if primes[i]:
>           for j in range(i * i, n + 1, i):
>             primes[j] = False
>       return [i for i, is_prime in enumerate(primes) if is_prime]
>     
>     primes = sieve_of_eratosthenes(1000)
>     print(primes)
>     
> 
> **Explication:**
> 
>   1. **Initialisation:**
>      * `primes = [True] * (n + 1)`: Crée une liste `primes` de valeurs booléennes, initialement supposant que tous les nombres sont premiers.
>      * `primes[0] = primes[1] = False`: Définit 0 et 1 comme non-premiers.
>   2. **Itération:**
>      * `for i in range(2, int(n**0.5) + 1):`: Itère de 2 jusqu'à la racine carrée de `n`. Nous ne devons vérifier que jusqu'à la racine carrée car tout nombre composite doit avoir un facteur premier inférieur ou égal à sa racine carrée.
>      * `if primes[i]:`: Si `i` est considéré comme premier: 
>        * `for j in range(i * i, n + 1, i):`: Marquer tous les multiples de `i` comme non-premiers.
>   3. **Resultat:**
>      * `return [i for i, is_prime in enumerate(primes) if is_prime]`: Crée une liste des indices où `primes[i]` est vrai, représentant les nombres premiers.
> 
N'hésitez pas à me demander si vous avez besoin d'une explication plus détaillée de quelque chose! 
    
    
    message = "Great! Now add those explanations as comments in the code."
    display_chat(message, chat.send_message(message))
    

🙋‍♂️

> Great! Now add those explanations as comments in the code.

🤖

> 
>     def sieve_of_eratosthenes(n):
>       """Retourne une liste de nombres premiers jusqu'à n."""
>       # Initialise une liste de boolean avec True pour tous les nombres de 0 à n
>       primes = [True] * (n + 1)
>       # Définit 0 et 1 comme non-premiers
>       primes[0] = primes[1] = False
>       # Itère de 2 à la racine carrée de n
>       for i in range(2, int(n**0.5) + 1):
>         # Si i est considéré comme premier
>         if primes[i]:
>           # Itère sur tous les multiples de i
>           for j in range(i * i, n + 1, i):
>             # Définit les multiples de i comme non-premiers
>             primes[j] = False
>       # Retourne la liste des indices des nombres premiers
>       return [i for i, is_prime in enumerate(primes) if is_prime]
>     
>     primes = sieve_of_eratosthenes(1000)
>     print(primes)
>     
> 
> **Explication:**
> 
>   * **Initialisation:**
>     * `primes = [True] * (n + 1)`: Crée une liste `primes` de valeurs booléennes, initialement supposant que tous les nombres sont premiers.
>     * `primes[0] = primes[1] = False`: Définit 0 et 1 comme non-premiers.
>   * **Itération:**
>     * `for i in range(2, int(n**0.5) + 1):`: Itère de 2 jusqu'à la racine carrée de `n`. Nous ne devons vérifier que jusqu'à la racine carrée car tout nombre composite doit avoir un facteur premier inférieur ou égal à sa racine carrée.
>     * `if primes[i]:`: Si `i` est considéré comme premier: 
>       * `for j in range(i * i, n + 1, i):`: Marquer tous les multiples de `i` comme non-premiers.
>   * **Resultat:**
>     * `return [i for i, is_prime in enumerate(primes) if is_prime]`: Crée une liste des indices où `primes[i]` est vrai, représentant les nombres premiers. 
> 


Test the generated response by running the generated code:
    
    
    def sieve_of_eratosthenes(n):
      """Retourne une liste de nombres premiers jusqu'à n."""
      # Initialise une liste de boolean avec True pour tous les nombres de 0 à n
      primes = [True] * (n + 1)
      # Définit 0 et 1 comme non-premiers
      primes[0] = primes[1] = False
      # Itère de 2 à la racine carrée de n
      for i in range(2, int(n**0.5) + 1):
        # Si i est considéré comme premier
        if primes[i]:
          # Itère sur tous les multiples de i
          for j in range(i * i, n + 1, i):
            # Définit les multiples de i comme non-premiers
            primes[j] = False
      # Retourne la liste des indices des nombres premiers
      return [i for i, is_prime in enumerate(primes) if is_prime]
    
    primes = sieve_of_eratosthenes(1000)
    print(primes)
    
    
    
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    

Use the `get_history` method to see how all the context was retained by the `Chat` class.
    
    
    print(chat.get_history())
    
    
    
    <start_of_turn>user
    Tell me, in a few words,  how to compute all prime numbers up to 1000?<end_of_turn>
    <start_of_turn>model
    **Sieve of Eratosthenes.** 
    <end_of_turn><start_of_turn>user
    Now in Python! No numpy, please!<end_of_turn>
    <start_of_turn>model
    
    ```python
    def sieve_of_eratosthenes(n):
      """Returns a list of prime numbers up to n."""
      primes = [True] * (n + 1)
      primes[0] = primes[1] = False
      for i in range(2, int(n**0.5) + 1):
        if primes[i]:
          for j in range(i * i, n + 1, i):
            primes[j] = False
      return [i for i, is_prime in enumerate(primes) if is_prime]
    
    primes = sieve_of_eratosthenes(1000)
    print(primes)
    ```
    
    **Explanation:**
    
    1. **Initialization:**
       - `primes = [True] * (n + 1)`: Creates a list `primes` of boolean values, initially assuming all numbers are prime.
       - `primes[0] = primes[1] = False`: Sets 0 and 1 as non-prime.
    
    2. **Iteration:**
       - `for i in range(2, int(n**0.5) + 1):`: Iterates from 2 to the square root of `n`. We only need to check up to the square root because any composite number must have a prime factor less than or equal to its square root.
       - `if primes[i]:`: If `i` is marked as prime:
         - `for j in range(i * i, n + 1, i):`: Marks all multiples of `i` as non-prime.
    
    3. **Result:**
       - `return [i for i, is_prime in enumerate(primes) if is_prime]`: Creates a list of indices where `primes[i]` is True, representing the prime numbers.
    
    
    Let me know if you'd like a more detailed explanation of any part! 
    <end_of_turn><start_of_turn>user
    Thank you, it works! Can you explain the code in French?<end_of_turn>
    <start_of_turn>model
    Bien sûr ! Voici une explication du code en français :
    
    ```python
    def sieve_of_eratosthenes(n):
      """Retourne une liste de nombres premiers jusqu'à n."""
      primes = [True] * (n + 1)
      primes[0] = primes[1] = False
      for i in range(2, int(n**0.5) + 1):
        if primes[i]:
          for j in range(i * i, n + 1, i):
            primes[j] = False
      return [i for i, is_prime in enumerate(primes) if is_prime]
    
    primes = sieve_of_eratosthenes(1000)
    print(primes)
    ```
    
    **Explication:**
    
    1. **Initialisation:**
       - `primes = [True] * (n + 1)`: Crée une liste `primes` de valeurs booléennes, initialement supposant que tous les nombres sont premiers.
       - `primes[0] = primes[1] = False`: Définit 0 et 1 comme non-premiers.
    
    2. **Itération:**
       - `for i in range(2, int(n**0.5) + 1):`: Itère de 2 jusqu'à la racine carrée de `n`. Nous ne devons vérifier que jusqu'à la racine carrée car tout nombre composite doit avoir un facteur premier inférieur ou égal à sa racine carrée.
       - `if primes[i]:`: Si `i` est considéré comme premier:
         - `for j in range(i * i, n + 1, i):`:  Marquer tous les multiples de `i` comme non-premiers.
    
    3. **Resultat:**
       - `return [i for i, is_prime in enumerate(primes) if is_prime]`: Crée une liste des indices où `primes[i]` est vrai, représentant les nombres premiers.
    
    
    N'hésitez pas à me demander si vous avez besoin d'une explication plus détaillée de quelque chose! 
    <end_of_turn><start_of_turn>user
    Great! Now add those explanations as comments in the code.<end_of_turn>
    <start_of_turn>model
    
    ```python
    def sieve_of_eratosthenes(n):
      """Retourne une liste de nombres premiers jusqu'à n."""
      # Initialise une liste de boolean avec True pour tous les nombres de 0 à n
      primes = [True] * (n + 1)
      # Définit 0 et 1 comme non-premiers
      primes[0] = primes[1] = False
      # Itère de 2 à la racine carrée de n
      for i in range(2, int(n**0.5) + 1):
        # Si i est considéré comme premier
        if primes[i]:
          # Itère sur tous les multiples de i
          for j in range(i * i, n + 1, i):
            # Définit les multiples de i comme non-premiers
            primes[j] = False
      # Retourne la liste des indices des nombres premiers
      return [i for i, is_prime in enumerate(primes) if is_prime]
    
    primes = sieve_of_eratosthenes(1000)
    print(primes)
    ```
    
    **Explication:**
    
    * **Initialisation:**
        * `primes = [True] * (n + 1)`:  Crée une liste `primes` de valeurs booléennes, initialement supposant que tous les nombres sont premiers.
        * `primes[0] = primes[1] = False`: Définit 0 et 1 comme non-premiers.
    * **Itération:**
        * `for i in range(2, int(n**0.5) + 1):`: Itère de 2 jusqu'à la racine carrée de `n`. Nous ne devons vérifier que jusqu'à la racine carrée car tout nombre composite doit avoir un facteur premier inférieur ou égal à sa racine carrée.
        * `if primes[i]:`: Si `i` est considéré comme premier:
            * `for j in range(i * i, n + 1, i):`:  Marquer tous les multiples de `i` comme non-premiers.
    * **Resultat:**
        * `return [i for i, is_prime in enumerate(primes) if is_prime]`: Crée une liste des indices où `primes[i]` est vrai, représentant les nombres premiers. 
    
    
    
    <end_of_turn>
    

## Summary and further reading

In this tutorial, you learned how to chat with the Gemma 2B Instruction tuned model using Keras on JAX. Check out these guides and tutorials to learn more about Gemma:

  * [Get started with Keras Gemma](https://ai.google.dev/gemma/docs/get_started).
  * [Finetune the Gemma model on GPU](https://ai.google.dev/gemma/docs/lora_tuning).
  * Learn about [Gemma integration with Vertex AI](https://ai.google.dev/gemma/docs/integrations/vertex)
  * Learn how to [use Gemma models with Vertex AI](https://cloud.google.com/vertex-ai/docs/generative-ai/open-models/use-gemma).


