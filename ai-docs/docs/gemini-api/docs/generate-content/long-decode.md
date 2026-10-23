---
url: https://ai.google.dev/gemini-api/docs/generate-content/long-decode/
title: Long decode
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:43:37.220172+00:00
---

# Long decode

> Source: https://ai.google.dev/gemini-api/docs/generate-content/long-decode/

Long decode lets Gemini 4 Argon generate past the single-request output limit for deep reasoning tasks, up to the unified 1M-token context window (1,048,576 tokens shared across input, thinking, and output).

Changing the model ID alone doesn't enable long decode. Without additional setup, output stops at 64K tokens for streaming calls and 32K tokens for non-streaming calls. The fastest way to turn on long decode is to upgrade the Google GenAI SDK and set `max_output_tokens` greater than 65,536. This guide explains how long decode works, when to use it, and how to turn it on with `generateContent`.

## How long decode works

A single streaming or SDK request generates up to 64K tokens, and a non-streaming REST request generates up to 32K tokens. When a response needs more tokens, the model generates it across multiple request-and-response hops that each continue from where the previous hop stopped.

  * **Unified input and output token limit:** Input, thinking, function calls, and the final response share one 1M-token window. Output can use up to 1,048,576 minus your input tokens.
  * **A cap on each hop:** One hop returns up to 65,536 output tokens. Non-streaming REST requests return up to 32,768.
  * **A continuation signal:** If the model reaches the cap and has tokens left, the response ends with `finish_reason: CONTINUATION` and a `continuation_token`.
  * **The next hop:** The client sends the same request again with the token. The model continues from where it stopped.
  * **One total for all hops:** `max_output_tokens` sets the total thinking and output tokens for all hops together.
  * **A stop signal:** When the model uses all of `max_output_tokens`, the response ends with `finish_reason: MAX_TOKENS`.



On hard problems, a hop can spend all of its tokens on internal thinking and return empty text with a `continuation_token`. This is normal, and the final answer arrives in later hops.

## Default output limits

Without long decode, a single request stops at these per-request limits:

  * **Streaming requests and non-streaming requests through the Google GenAI SDK (`generate_content`):** Default to 64K output tokens.
  * **Direct non-streaming REST calls (`generateContent`):** Default to 32K output tokens. Setting `max_output_tokens` greater than 32,768 on a non-streaming REST call without a `continuation_token` returns a `400` error.

How you call the model | Output limit without long decode | Long decode at launch | What to do  
---|---|---|---  
Google GenAI SDK, latest version | 64K | Yes, the SDK continues for you | Set `max_output_tokens`.  
Google GenAI SDK, older version, non-streaming | 64K | No | Upgrade the SDK.  
REST `streamGenerateContent` | 64K | Yes, with your own loop | Write a loop. See Option 2.  
REST `generateContent` | 32K | Yes, with your own loop | Write a loop. See Option 2.  
  
## When to use long decode

Most requests finish within the single-request limit (64K tokens for streaming and SDK calls, or 32K tokens for non-streaming REST calls). Use long decode when a response needs more combined thinking and output tokens than a single request allows. Raising `max_output_tokens` gives the model a higher ceiling to reason through hard problems, rather than making standard answers longer.

Workload | Use long decode? | Why  
---|---|---  
Hard math, science, research, and formal proofs | Yes | The model can spend more than 64K tokens to explore and check its reasoning.  
The hardest coding and agentic tasks | Yes | Some tasks need more than 64K tokens of thinking and code in one response. Most coding and agentic tasks finish under 64K.  
Evaluation harnesses that stop at the output limit | Yes | Long decode prevents cut-off answers when the model spends a whole 64K or 32K request on thinking.  
Chat, Q&A, summarization, classification, and extraction | No | These tasks finish well under 32K tokens.  
Requests for a fixed length, such as "write a 700,000-word book" | No | The model does not follow length targets.  
Agents that call tools in many short turns | No | Each turn is short. Large outputs on each turn fill the unified 1M input and output window fast.  
Prompts near the 1M input limit | No | Output can use only 1M minus your input.  
Latency-sensitive requests | No | Long decode can run for several minutes.  
  
Setting a high `max_output_tokens` gives the model room to think longer on hard problems, but the model still decides how much to write. To control how much reasoning effort the model uses, set [`thinking_level`](https://ai.google.dev/gemini-api/docs/generate-content/thinking).

## Turn on long decode

You can run long decode automatically with the Google GenAI SDK (Option 1, recommended for most apps) or write your own continuation loop (Option 2). Both options support the full 1M-token context window.

| Option 1: Google GenAI SDK (recommended) | Option 2: Your own streaming loop | Option 2: Your own non-streaming loop  
---|---|---|---  
**Who starts each hop** | The SDK. You set `max_output_tokens`. | Your code, at each checkpoint or after a dropped stream | Your code, every 32K tokens  
**Tokens per request** | 64K per hop | 64K per stream, with a checkpoint every 5K tokens after 32K | 32K per request  
**Time limit per request** | 20 minutes | 20 minutes | 20 minutes  
**Storage** | No server storage | No server storage | No server storage  
**Best for** | Most applications | REST callers and custom harnesses that stream | Simple evaluation harnesses  
  
The encrypted `continuation_token` carries the model's state between requests, so nothing is stored on the server.

### Option 1: Use the Google GenAI SDK (recommended)

In the latest Google GenAI SDK, `automatic_continuation` is enabled by default for both streaming and non-streaming calls, so you do not need to set it. When you set `max_output_tokens` above the per-request cap, the SDK automatically runs the continuation hops and returns one combined response.

  1. Upgrade the SDK.

### Python
         
         pip install -U "google-genai>=2.30.1"
         

### JavaScript
         
         npm install "@google/genai@>=2.29.1"
         

  2. Set `max_output_tokens` greater than 65,536.

### Python
         
         from google import genai
         from google.genai import types
         
         client = genai.Client()  # Reads GEMINI_API_KEY
         
         response = client.models.generate_content(
             model="gemini-4-argon",
             contents="Write a complete, rigorous proof of the prime number theorem.",
             config=types.GenerateContentConfig(
                 max_output_tokens=262_144,  # Total thinking and output for all hops
                 thinking_config=types.ThinkingConfig(thinking_level="high"),
                 automatic_continuation=True,  # Default. Shown for clarity.
             ),
         )
         
         print(response.text)
         print("Finish reason:", response.candidates[0].finish_reason)
         print("Prompt size:", response.usage_metadata.initial_prompt_token_count)
         print("Billed tokens:", response.usage_metadata.total_token_count)
         

### JavaScript
         
         import { GoogleGenAI, ThinkingLevel } from "@google/genai";
         
         const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
         
         const response = await ai.models.generateContent({
           model: "gemini-4-argon",
           contents: "Write a complete, rigorous proof of the prime number theorem.",
           config: {
             maxOutputTokens: 262144, // Total thinking and output for all hops
             thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
             automaticContinuation: true, // Default. Shown for clarity.
           },
         });
         
         console.log(response.text);
         console.log("Finish reason:", response.candidates?.[0]?.finishReason);
         console.log("Prompt size:", response.usageMetadata?.initialPromptTokenCount);
         console.log("Billed tokens:", response.usageMetadata?.totalTokenCount);
         




Keep these points in mind:

  * **Streaming:** `generate_content_stream` (Python) and `generateContentStream` (JavaScript) also continue for you. If a stream drops after a checkpoint, the SDK resumes from that checkpoint.
  * **Timeouts:** Timeouts and retries apply to each hop, not to the full run.
  * **Manual control:** To run the loop yourself, set `automatic_continuation=False` (Python) or `automaticContinuation: false` (JavaScript). Then follow Option 2.
  * **Usage:** The usage fields show the sum of all hops. To get the size of your prompt, read `initial_prompt_token_count`. See Count tokens.



### Option 2: Write your own loop

Write your own loop if you call REST directly, use a language without the latest SDK, or need full control. You can also refer to our Google GenAI SDK implementations in [Python](https://github.com/googleapis/python-genai/blob/v2.30.1/google/genai/models.py#L6111) and [JavaScript/TypeScript](https://github.com/googleapis/js-genai/blob/v2.29.1/src/models.ts#L88) as a reference.

Follow these rules:

  1. **Send the same request on every hop.** Send the original `contents`, `system_instruction`, `tools`, and `generation_config`. Keep `max_output_tokens` the same.
  2. **Do not add partial output to`contents`.** The `continuation_token` carries the model's state, including its thinking.
  3. **Send only the latest token.** Each token contains all earlier progress.
  4. **Continue while`finish_reason` is `CONTINUATION`.** Stop on any other finish reason.
  5. **Join the parts after the last hop.** Combine the parts from all hops into one model turn for the conversation history.



### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()  # Reads GEMINI_API_KEY
    PROMPT = "Write a complete, rigorous proof of the prime number theorem."
    parts = []
    token = None
    
    while True:
        response = client.models.generate_content(
            model="gemini-4-argon",
            contents=PROMPT,  # The original contents on every request
            config=types.GenerateContentConfig(
                max_output_tokens=262_144,  # The same total on every request
                thinking_config=types.ThinkingConfig(thinking_level="high"),
                automatic_continuation=False,  # You run the loop
                continuation_token=token,
            ),
        )
        candidate = response.candidates[0]
        if candidate.content and candidate.content.parts:
            parts.extend(candidate.content.parts)
        token = candidate.continuation_token
        if candidate.finish_reason != types.FinishReason.CONTINUATION or not token:
            break
    
    print("".join(p.text for p in parts if p.text and not p.thought))
    print("Finish reason:", candidate.finish_reason)
    

### JavaScript
    
    
    import { GoogleGenAI, ThinkingLevel } from "@google/genai";
    
    const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
    const PROMPT = "Write a complete, rigorous proof of the prime number theorem.";
    const parts = [];
    let token = undefined;
    let candidate = undefined;
    
    while (true) {
      const response = await ai.models.generateContent({
        model: "gemini-4-argon",
        contents: PROMPT, // The original contents on every request
        config: {
          maxOutputTokens: 262144, // The same total on every request
          thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
          automaticContinuation: false, // You run the loop
          continuationToken: token,
        },
      });
      candidate = response.candidates?.[0];
      if (candidate?.content?.parts) {
        parts.push(...candidate.content.parts);
      }
      token = candidate?.continuationToken;
      if (candidate?.finishReason !== "CONTINUATION" || !token) {
        break;
      }
    }
    
    console.log(parts.filter((p) => p.text && !p.thought).map((p) => p.text).join(""));
    console.log("Finish reason:", candidate?.finishReason);
    

### REST
    
    
    # Hop 1: send the request with max_output_tokens.
    curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
        "generationConfig": {
          "maxOutputTokens": 262144,
          "thinkingConfig": {"thinkingLevel": "high"}
        }
      }'
    
    # Hop 2: if finishReason is CONTINUATION, send the same request plus the token.
    curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
        "generationConfig": {
          "maxOutputTokens": 262144,
          "thinkingConfig": {"thinkingLevel": "high"}
        },
        "continuationToken": "TOKEN_FROM_HOP_1"
      }'
    

A hop spent entirely on thinking returns empty `text` with `finishReason: "CONTINUATION"`. Treat this as normal progress and request the next hop:
    
    
    {
      "candidates": [{
        "content": {"role": "model", "parts": [{"text": ""}]},
        "finishReason": "CONTINUATION",
        "continuationToken": "CiQ4ZmQ3..."
      }],
      "usageMetadata": {
        "promptTokenCount": 142,
        "candidatesTokenCount": 0,
        "thoughtsTokenCount": 32768,
        "totalTokenCount": 32910
      }
    }
    

**Streaming loops** need one more rule. After the first 32,768 tokens, the stream sends a checkpoint token every 5,000 tokens. Keep new chunks in a pending list. When a chunk has a `continuation_token`, move the pending chunks to your committed output and save the token. If the stream drops, discard the pending chunks and resume from the last token. If the stream drops before the first checkpoint, send the original request again.

## Set `max_output_tokens`

`max_output_tokens` sets the combined limit for thinking and output across all hops. Lowering it doesn't make the model think more concisely, and instead cuts the response off sooner.

Your workload | Recommended `max_output_tokens`  
---|---  
Existing apps with a limit lower than 32K | Raise it to 32,768.  
Long coding and agentic tasks | Start at 65,536.  
Hard math, science, research, and proofs | Test values from 262,144 up to 1,048,576 minus your input tokens.  
  
To use fewer tokens, lower `thinking_level`. Use `high` for the hardest reasoning tasks. Use `medium` (the default) for most coding and agentic work. Use `low` for less complex tasks.

## Handle long-running requests

Because Gemini 4 Argon thinks longer than Gemini 3.x models on hard problems, you should increase your client timeouts so long requests don't disconnect early.

  * **Non-streaming calls:** The server closes the connection after 10 minutes.
  * **Streaming calls:** The server closes the stream after 20 minutes.
  * **Client timeouts:** Set your HTTP read timeout to 20 minutes. A 3-minute or 5-minute timeout stops the request early.



In Python, set the timeout on the client in milliseconds:
    
    
    client = genai.Client(http_options=types.HttpOptions(timeout=1_200_000))  # 20 minutes
    

For jobs that your client polls, the Interactions API runs long decode on the server. See [background execution](https://ai.google.dev/gemini-api/docs/background-execution).

## Resume when the model uses all output tokens

When a response ends with `MAX_TOKENS`, it still includes a `continuation_token`. You have two choices:

  * **Continue:** Send the same request with the token and a higher `max_output_tokens`. The value must be above the tokens used so far. Otherwise, the API returns a 400 error.
  * **Start again:** Send the original request with a higher `max_output_tokens` and no token. You pay for both runs.



## Count tokens

With automatic continuation, `usage_metadata` reports the totals across all hops. The SDK adds up every count field: `prompt_token_count`, `cached_content_token_count`, `candidates_token_count`, `thoughts_token_count`, and `total_token_count`.

`prompt_token_count` adds up the input tokens of every hop. Each hop sends your prompt plus everything generated so far back to the model as input, so the same tokens are counted again in every later hop. For example, with the Google GenAI SDK, a 1,000-token prompt that produces 200,000 tokens of thinking and output takes four hops:

Hop | Input sent to the model | Input tokens  
---|---|---  
1 | Prompt | 1,000  
2 | Prompt + hop 1 | 66,536  
3 | Prompt + hops 1 and 2 | 132,072  
4 | Prompt + hops 1 to 3 | 197,608  
**Total** |  | **397,216**  
  
`prompt_token_count` reports about 397,000 tokens (with repeated hop inputs automatically discounted 95% by implicit caching), and `total_token_count` reports about 597,000 tokens, even though the actual context size is only about 201,000 tokens: the 1,000-token prompt plus 200,000 tokens of thinking and output. A non-streaming REST loop uses 32K hops, so it takes seven hops for the same output and reports 695,128 input tokens.

How you call the model | What `usage_metadata` shows | For cost | For the prompt size  
---|---|---|---  
Google GenAI SDK, automatic continuation (the default) | Totals across all hops | Read the usage fields as is. | Read `usage_metadata.initial_prompt_token_count` (Python) or `usageMetadata.initialPromptTokenCount` (JavaScript).  
SDK with `automatic_continuation=False`, or REST | One hop per response | Add each field across hops. | Read `prompt_token_count` from the first hop.  
  
`prompt_token_count` and `total_token_count` are the sum of every hop, not the size of your context. Don't use them to decide when to summarize or trim your conversation history (context compaction), or to enforce a context limit. To estimate the context size, add your prompt size from the table to `candidates_token_count` and `thoughts_token_count`.

Update your agent framework, evaluation tool, or proxy before you run long decode:

  * **Agents and evaluation tools:** If your code compacts context or stops a run at a token limit, use `initial_prompt_token_count` (or the first hop's `prompt_token_count` in REST) instead of the summed `prompt_token_count`. Responses that finish in one hop report the same value in both fields, so short tests don't show the problem.
  * **Proxies and gateways that call REST:** Each REST response reports only its own hop. Add each field across hops for cost, and keep the first hop's `promptTokenCount` as the prompt size. Otherwise, your users see different numbers than SDK users see for the same request.
  * **Logs and serialized responses:** The SDK calculates `initial_prompt_token_count` on the client. It isn't in the REST response or in the SDK's JSON output, such as `model_dump()`. Save it as a separate value if you need it later.



If you stream in your own loop, `usage_metadata` is cumulative within each stream. Keep only the last value of each stream, then add the values across hops.

## Understand billing

You pay for every token in every hop, including hops that contain only thinking.

  * **Cache discount:** Implicit caching discounts the repeated input in each hop by 95%. Cached input costs $0.10 per 1M tokens instead of $2.00 during the introductory period.
  * **Cache expiry:** The cache expires after 15 to 20 minutes without use. A long pause between hops charges the full input rate again.
  * **Failed non-streaming hops:** You pay only when a response completes. A failed or dropped request costs $0.
  * **Dropped streams:** A stream that drops before 32K tokens costs $0. After that, you pay up to the last checkpoint token, because you can resume from it.



## Troubleshooting

Symptom | Cause and fix  
---|---  
Output stops at 64K or 32K with `CONTINUATION` | The model has tokens left, but nothing continued the request. Upgrade the SDK or add a loop.  
Output stops at 64K or 32K with `MAX_TOKENS` | `max_output_tokens` is not set or is too low. Set it to more than 65,536.  
Empty text with `MAX_TOKENS` | The model used all tokens on thinking. Raise `max_output_tokens` or lower `thinking_level`.  
400: "Continuation token has already used output tokens..." | `max_output_tokens` is not above the tokens used so far. Raise it.  
Error for `thinking_level: "minimal"`, or for `thinking_budget` with `thinking_level` | Gemini 4 Argon does not support `minimal`. Use `low`, `medium`, or `high`. Set `thinking_level` or `thinking_budget`, not both.  
Warning for `thinking_budget`, `temperature`, `top_p`, or `top_k` | Gemini 4 Argon ignores or maps these fields. Use `thinking_level`, and remove the sampling parameters.  
Request ends after 3 or 5 minutes | The client timeout is too short. Set it to 20 minutes.  
Context compaction starts too early | The harness reads summed input. Read `initial_prompt_token_count` instead.  
  
## Limitations

  * **OpenAI compatibility endpoint:** Long decode is not available. Output stops at the per-request cap.
  * **Older SDKs:** Versions below the minimums in the note do not continue automatically.
  * **Length:** The model does not follow token-length or word-count targets.



## Checklist

  * Upgrade the Google GenAI SDK to the minimum version.
  * Set `max_output_tokens` greater than 65,536.
  * Use `thinking_level` (`low`, `medium`, or `high`), not `thinking_budget`.
  * Set HTTP read timeouts to 20 minutes.
  * Use `initial_prompt_token_count` for context size and compaction.
  * Run one prompt as a test before a large evaluation.



## Next steps

  * [What's new in Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/generate-content/latest-model)
  * [Thinking](https://ai.google.dev/gemini-api/docs/generate-content/thinking)
  * [Token counting](https://ai.google.dev/gemini-api/docs/generate-content/tokens)


