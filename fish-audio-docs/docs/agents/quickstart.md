---
url: https://docs.fish.audio/agents/quickstart/
title: Quickstart - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-20T16:17:52.515635+00:00
---

# Quickstart - Fish Audio

> Source: https://docs.fish.audio/agents/quickstart/

## On this page

Back to top

  * Build with a coding assistant
  * Build it step by step
  * Next steps



Get Started

# Quickstart

Copy pageCopy page

Create a voice agent and have your first conversation in minutes

Copy pageCopy page

Build a voice agent and talk to it in a few minutes. Use the console for a no-code path, or do everything over the API and reach your agent on the phone or on your own page. **Prerequisites**

  * A Fish Audio account.
  * Every account starts with a $5 trial balance. It pays for web, phone, and API sessions at the normal rates, including token-billed LLMs. After that, usage is billed per second against your API credit.



## Build with a coding assistant

Working in Claude Code, Codex, Cursor, or another coding assistant? Paste this prompt. The assistant asks what your agent should do, then follows the API path on this page and builds a demo you can talk to. Along the way it needs an API key from you.

Prompt
    
    
    Build a voice agent using Fish Audio Voice Agents. Give me a browser demo I can talk to. Ask me questions.
    
    Follow the API in https://docs.fish.audio/agents/quickstart.md.
    

Optionally, install the Fish Audio agents skill first. It also gives the assistant the error codes and the pages to read for tools, deployment, and telephony.

Install the skill (optional)
    
    
    npx skills add https://docs.fish.audio --skill fish-audio-agents
    

## Build it step by step

  * Console

  * API




1

Create an agent

Go to [Agents](https://fish.audio/app/agents) and click **New agent**. Give it a name. You land in the Builder immediately.

2

Write the system prompt

On the **Configuration** page, write the system prompt that defines who your agent is and how it should behave (up to 32,000 tokens). Optionally set a **First message** so the agent opens the conversation.Edits save automatically as a draft.

3

Pick a voice

Choose a voice and a speaking language for your agent. You can pick from the featured voices or browse the full library. See [Voice & language](https://docs.fish.audio/agents/build/voice-language) for details.

4

Test it with a preview call

Click **Test call** in the top bar. Your browser asks for microphone access, then you talk to the agent directly, with a live transcript, call timer, and mute and hang-up controls in the side panel.Preview calls always run against your current draft, so you can iterate on the prompt and immediately hear the difference. See [Preview calls](https://docs.fish.audio/agents/test/preview-calls).

5

Publish

Click **Publish** to turn the draft into an immutable version. Published versions are what real sessions connect to.You can keep editing the draft afterwards; nothing goes live until you publish again. See [Versions & publishing](https://docs.fish.audio/agents/deploy/versions-publishing).

Your agent is live. Choose how people reach it.

  * **Phone number.** Open **Phone numbers** in the console, click **Add number** , buy a number and bind it to your agent, then call it from your phone. See [Phone numbers](https://docs.fish.audio/agents/telephony/phone-numbers).
  * **Widget.** On the agent’s **Deploy** page, turn on **Public access** and paste the two-line embed into your site. See [Widget](https://docs.fish.audio/agents/deploy/widget).
  * **Your own backend.** Switch to the **API** tab above and start from **Get an API key**.



1

Get an API key

Create a key on the [API keys](https://fish.audio/app/agents/api-keys?new=1) page of the console and copy it. The key is shown once. Keep it on your server and out of browsers and apps.

Set the key
    
    
    export FISH_API_KEY="your_api_key"
    

Check the key by listing your agents. The list is empty on a new account.

Check the key
    
    
    curl https://api.fish.audio/v1/agent/agents \
      --header "Authorization: Bearer $FISH_API_KEY"
    

A `200` means the key works. A `401` means it is wrong or expired. This request creates nothing, so use it whenever you want to test your setup.

2

Create an agent

Create the agent and configure it in one call. The `config` section is optional at creation time, and you can update it later with `PATCH /v1/agent/agents/{agent_id}/config`. See [Configuration](https://docs.fish.audio/agents/build/configuration) for the opening line, the speaking language, and the other settings.

Create an agent
    
    
    curl --request POST https://api.fish.audio/v1/agent/agents \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Support agent",
        "config": {
          "prompt": {
            "system_prompt": "You are a friendly support agent for Acme. Keep answers short and conversational."
          },
          "voice": {
            "voice_id": "802e3bc2b27e49c2995d23ef70e6ac89"
          }
        }
      }'
    

The response includes the agent’s `agent_id`. Use it as `$AGENT_ID` below. `voice_id` accepts any voice model id from the [Voice Library](https://docs.fish.audio/features/manage-voices).

Save the agent ID
    
    
    export AGENT_ID="the agent_id from the response"
    

`system_prompt` is limited to 32,000 tokens; longer prompts return `422`. Keeping it under 2,000 tokens is recommended for latency and cost.

3

Publish it

Sessions only run **published** configuration. Creating a session for an agent that has never been published returns `409`.

Publish the draft
    
    
    curl --request POST https://api.fish.audio/v1/agent/agents/$AGENT_ID/publish \
      --header "Authorization: Bearer $FISH_API_KEY"
    

Each publish creates an immutable version with an auto-incremented `version_number`.

4

Talk to your agent

Your agent is published. Reach it on the phone with nothing but API requests, hear it in the console with a test call, or talk to it on your own page with a one-file demo.

  * Phone

  * Console

  * Your own page




Give your agent a phone number and call it. Every step is an API request and the conversation happens on your phone, with no browser and no SDK. The number is a US or Canada local number.**Find a number**

Search numbers
    
    
    curl "https://api.fish.audio/v1/agent/available-phone-numbers?country_code=US" \
      --header "Authorization: Bearer $FISH_API_KEY"
    

Pick a `phone_number` from the `available_phone_numbers` array.**Buy it and bind your agent**

Buy a number
    
    
    curl --request POST https://api.fish.audio/v1/agent/phone-numbers \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --data '{
        "provider": "twilio",
        "phone_number": "+14155550123",
        "agent_id": "'$AGENT_ID'"
      }'
    

Passing `agent_id` binds the number in the same request, so it answers calls right away. The response includes the `phone_number_id`.**Call it** Dial the number from your phone. Your agent picks up.If you are not in the US or Canada, have the agent call you instead. Outbound calls reach numbers in the US, Canada, Japan, the UK, Italy, Australia, and Mexico. See [allowed destinations](https://docs.fish.audio/agents/telephony/outbound-calls#allowed-destinations).

Have the agent call you
    
    
    curl --request POST https://api.fish.audio/v1/agent/phone-calls \
      --header "Authorization: Bearer $FISH_API_KEY" \
      --header "Content-Type: application/json" \
      --header "Idempotency-Key: quickstart-call-1" \
      --data '{
        "agent_id": "'$AGENT_ID'",
        "phone_number_id": "YOUR_PHONE_NUMBER_ID",
        "to_number": "+14155550123"
      }'
    

**Read the conversation back**

Find the call
    
    
    curl "https://api.fish.audio/v1/agent/sessions?agent_id=$AGENT_ID" \
      --header "Authorization: Bearer $FISH_API_KEY"
    

The newest session comes first. An outbound call also returns its `session_id` when you place it. Read the transcript with that id.

Read the transcript
    
    
    curl "https://api.fish.audio/v1/agent/sessions/SESSION_ID" \
      --header "Authorization: Bearer $FISH_API_KEY"
    

`items` holds the messages and tool calls in order. See [Conversation history](https://docs.fish.audio/agents/monitor/conversation-history).Keep the number as your agent’s line, or release it to stop the rental. See [Pricing](https://docs.fish.audio/agents/pricing#phone-number-rental).

Release the number
    
    
    curl --request DELETE https://api.fish.audio/v1/agent/phone-numbers/YOUR_PHONE_NUMBER_ID \
      --header "Authorization: Bearer $FISH_API_KEY"
    

Place a test call in the console. It takes no code and no phone number, so it is the quickest way to hear your agent.

Print the link to your agent
    
    
    echo "https://fish.audio/app/agents/$AGENT_ID"
    

Open the link. Agents created over the API appear in the console like any other. Click **Test call** in the top bar. Your browser asks for the microphone, then you are talking to your agent.A test call is a preview for you. It runs the agent’s draft, which right after publishing matches the published version. To put the agent in front of your users, use **Phone** or **Your own page**. See [Preview calls](https://docs.fish.audio/agents/test/preview-calls).

Run one file to get a browser demo on your own page. It serves a page with the call widget and a route that creates a session with your API key when a call starts. It has no dependencies and no build step, and needs Node.js 18 or later, or Python 3.8 or later.

server.mjs

server.py
    
    
    import { createServer } from "node:http";
    
    const page = `<!doctype html>
    <meta charset="utf-8">
    <title>Fish Agent demo</title>
    <fish-agent agent-name="My agent"></fish-agent>
    <script src="https://unpkg.com/@fishaudio/agent-widget-embed" async></script>
    <script>
      document.querySelector("fish-agent").sessionTokenProvider = async () => {
        const response = await fetch("/voice-session", { method: "POST" });
        if (!response.ok) throw new Error("backend answered " + response.status);
        return response.json();
      };
    </script>`;
    
    createServer(async (req, res) => {
      if (req.method !== "POST" || req.url !== "/voice-session") {
        res.writeHead(200, { "Content-Type": "text/html" });
        return res.end(page);
      }
      try {
        const upstream = await fetch("https://api.fish.audio/v1/agent/sessions", {
          method: "POST",
          headers: {
            Authorization: `Bearer ${process.env.FISH_API_KEY}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ agent_id: process.env.AGENT_ID }),
        });
        const body = await upstream.text();
        if (upstream.ok) console.log("session", JSON.parse(body).session_id);
        else console.log("failed", upstream.status, body);
        res.writeHead(upstream.status, { "Content-Type": "application/json" });
        res.end(body);
      } catch (error) {
        console.error(error);
        res.writeHead(502).end();
      }
    }).listen(3000, "localhost", () => console.log("open http://localhost:3000"));
    
    
    
    import json
    import os
    import urllib.error
    import urllib.request
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    
    PAGE = b"""<!doctype html>
    <meta charset="utf-8">
    <title>Fish Agent demo</title>
    <fish-agent agent-name="My agent"></fish-agent>
    <script src="https://unpkg.com/@fishaudio/agent-widget-embed" async></script>
    <script>
      document.querySelector("fish-agent").sessionTokenProvider = async () => {
        const response = await fetch("/voice-session", { method: "POST" });
        if (!response.ok) throw new Error("backend answered " + response.status);
        return response.json();
      };
    </script>"""
    
    
    class Handler(BaseHTTPRequestHandler):
        def reply(self, status, content_type, body):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    
        def do_GET(self):
            self.reply(200, "text/html", PAGE)
    
        def do_POST(self):
            if self.path != "/voice-session":
                return self.reply(404, "text/plain", b"not found")
            request = urllib.request.Request(
                "https://api.fish.audio/v1/agent/sessions",
                data=json.dumps({"agent_id": os.environ["AGENT_ID"]}).encode(),
                headers={
                    "Authorization": f"Bearer {os.environ['FISH_API_KEY']}",
                    "Content-Type": "application/json",
                },
            )
            try:
                with urllib.request.urlopen(request) as upstream:
                    status, body = upstream.status, upstream.read()
                print("session", json.loads(body)["session_id"], flush=True)
            except urllib.error.HTTPError as error:
                status, body = error.code, error.read()
                print("failed", status, body.decode(), flush=True)
            except urllib.error.URLError as error:
                status, body = 502, b""
                print("failed", error.reason, flush=True)
            self.reply(status, "application/json", body)
    
    
    print("open http://localhost:3000", flush=True)
    ThreadingHTTPServer(("localhost", 3000), Handler).serve_forever()
    

Start it in the terminal where you set `FISH_API_KEY` and `AGENT_ID`.

Node.js

Python
    
    
    node server.mjs
    
    
    
    python3 server.py
    

Open `http://localhost:3000`, click the launcher in the corner of the page, and start a voice chat. Your browser asks for the microphone, then you are talking to your agent.The terminal prints the `session_id` of each call. After you hang up, read the call back.

Read the call
    
    
    curl "https://api.fish.audio/v1/agent/sessions/SESSION_ID" \
      --header "Authorization: Bearer $FISH_API_KEY"
    

`status` is `completed` and `items` holds the transcript.

Open the page on `localhost` or over `https`. Browsers do not give a page the microphone on a plain `http` address such as a LAN IP.

What the file does.

  * The route calls `POST /v1/agent/sessions` with your API key and returns the response to the page unchanged. Your key never reaches the browser.
  * The response is a short-lived token for one conversation. Create a session when a user starts a call, one per call. Do not create sessions ahead of time or to test the API, because a session that no client joins ends as `failed`.
  * The widget receives the token through `sessionTokenProvider`. To build your own interface, pass the same token to the [Web SDK](https://docs.fish.audio/agents/deploy/web-sdk) or the [React SDK](https://docs.fish.audio/agents/deploy/react-sdk).

For production, keep the same shape. Your backend owns the API key and returns session tokens, and the page runs the widget or the SDK. See [Authenticated sessions](https://docs.fish.audio/agents/deploy/authenticated-sessions).

## Next steps

## Core concepts

Agents, drafts, versions, and sessions: how the pieces fit together.

## Web SDK

Events, transcripts, client tools, and audio controls in the browser.

## Agents API reference

Every endpoint with full request and response schemas.

## Knowledge base

Ground your agent in your own documents.

## Conversation history

Review transcripts, tool calls, and recordings.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/agents/quickstart.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/agents/quickstart)

[Overview](https://docs.fish.audio/agents/overview)[Concepts](https://docs.fish.audio/agents/concepts)
