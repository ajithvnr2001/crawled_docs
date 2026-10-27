---
url: https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes/
title: Support Voice Notes | Sarvam API Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-27T06:38:10.796402+00:00
---

# Support Voice Notes | Sarvam API Docs

> Source: https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes/

Skip to navigation

On this page

  * Overview
  * Business Value
  * How It Works
  * 1\. Prerequisites
  * 2\. Install the SDK and Dependencies
  * 3\. Set Environment Variables
  * 4\. The Full Bot Script
  * How it works
  * 5\. Run It
  * 6\. Tips & Best Practices
  * 7\. Error Handling
  * 8\. Additional Resources
  * 9\. Final Notes



Scroll to top

[Cookbook](https://docs.sarvam.ai/api/cookbook/guides/call-analytics-pipeline)[Guides](https://docs.sarvam.ai/api/cookbook/guides/call-analytics-pipeline)

# Support Voice Notes

Ask a question|Copy page|[View as Markdown](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes.md "View this page as plain text")|More actions

This page is for Model APIs.

Instant Voice Cloning is in **beta**. This cookbook uses it for the spoken reply; inbound transcription still uses Saaras.

## **Overview**

This cookbook builds a WhatsApp support bot whose spoken replies sound like a specific agent, not a stock speaker. It clones that agent once from a short reference clip, then on every inbound message it transcribes with **Saaras** , drafts a reply with a **Sarvam chat model** , and speaks the reply with **Instant Voice Cloning**.

The [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot) guide is the same channel with a Bulbul speaker. Use this page when the reply has to be a named person’s voice.

**What you’ll build:**

  * A saved cloned voice from a 10-15 second support-agent clip
  * A Flask webhook that receives WhatsApp text and voice notes via Twilio
  * Automatic transcription of inbound voice notes
  * A short support reply from a Sarvam chat model
  * A spoken reply in the cloned agent voice, attached as WhatsApp audio



### Business Value

  * Keep one familiar agent voice on a channel customers already have open
  * Reply in Hindi, Tamil, or any supported language from a single English (or other) reference clip
  * Avoid hiring per-language voice talent for routine status and FAQ replies



###### Customer Support

###### Collections & Reminders

###### Field Networks

A known agent’s voice confirms an order or walks through a refund, instead of a generic TTS speaker.

## **How It Works**

[1](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes#clone-the-agent-once)

### Clone the agent once

Send a clean reference clip to `voice_cloning.create_voice`. Keep the returned `voice_id` — every later reply uses it.

[2](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes#receive-the-message)

### Receive the message

Twilio POSTs every inbound WhatsApp message, text or voice note, to your Flask webhook.

[3](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes#transcribe-and-draft)

### Transcribe and draft

Voice notes go through **Saaras**. Typed or transcribed text goes to a **Sarvam chat model** with a short support persona.

[4](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes#speak-the-reply)

### Speak the reply

`voice_cloning.convert` synthesizes the reply with the saved `voice_id`. The bot attaches that audio to the WhatsApp response and still sends the text if synthesis fails.

**Voice cloning requires consent.** Only clone a voice you have the right to use. See [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing).

## **1\. Prerequisites**

  * Python 3.9 or higher
  * `sarvamai` ≥ `0.1.37`
  * A Sarvam API key from [Key Management](https://dashboard.sarvam.ai/key-management)
  * A 10-15 second, single-speaker clip of the support agent, saved as `reference.wav`. See [Prepare Reference Audio](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/prepare-reference-audio).
  * A [Twilio](https://console.twilio.com/) account with the WhatsApp Sandbox (or a WhatsApp-enabled Sender)
  * [ngrok](https://ngrok.com/download) to expose the local server



This cookbook uses the free **Twilio Sandbox for WhatsApp** for testing. Production needs a registered WhatsApp Sender. See [Twilio’s WhatsApp docs](https://www.twilio.com/docs/whatsapp). For Sandbox join-code and webhook setup, follow [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot#3-configure-twilio-for-whatsapp) — the Twilio side is the same.

## **2\. Install the SDK and Dependencies**
    
    
    pip install "sarvamai>=0.1.37" flask twilio python-dotenv requests

## **3\. Set Environment Variables**
    
    
    export SARVAM_API_KEY="your-sarvam-api-key"
    
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    
    export TWILIO_AUTH_TOKEN="your-twilio-auth-token"
    
    # Optional: reuse a voice created earlier instead of uploading the clip on every start
    
    # export VOICE_ID="svc-your-voice-id"

Load keys from the environment. If `VOICE_ID` is unset, the script clones `reference.wav` once at startup and prints the new id — save that value so later runs skip create.

## **4\. The Full Bot Script**

Copy this into `support_voice_notes.py`. It creates (or reuses) the agent voice, then handles every inbound WhatsApp message.
    
    
    import base64
    
    import logging
    
    import os
    
    import uuid
    
    from pathlib import Path
    
    import requests
    
    from dotenv import load_dotenv
    
    from flask import Flask, Response, request, send_from_directory
    
    from sarvamai import SarvamAI
    
    from twilio.twiml.messaging_response import MessagingResponse
    
    load_dotenv(override=True)
    
    logging.basicConfig(level=logging.INFO)
    
    logger = logging.getLogger(__name__)
    
    app = Flask(__name__)
    
    sarvam = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])
    
    AUDIO_DIR = Path("audio_replies")
    
    AUDIO_DIR.mkdir(exist_ok=True)
    
    SYSTEM_PROMPT = (
    
        "You are a support agent for a consumer app, chatting over WhatsApp. "
    
        "Reply in the customer's language. Keep replies to 2-3 sentences."
    
    )
    
    def resolve_voice_id() -> str:
    
        existing = os.getenv("VOICE_ID")
    
        if existing:
    
            return existing
    
        with open("reference.wav", "rb") as f:
    
            created = sarvam.voice_cloning.create_voice(
    
                file=f,
    
                name="support-agent",
    
                language="en-IN",
    
            )
    
        voice_id = created.data.voice_id
    
        logger.info("Created cloned voice %s — set VOICE_ID to reuse it", voice_id)
    
        return voice_id
    
    VOICE_ID = resolve_voice_id()
    
    @app.route("/audio/<filename>")
    
    def serve_audio(filename):
    
        return send_from_directory(AUDIO_DIR, filename, mimetype="audio/wav")
    
    @app.route("/whatsapp", methods=["POST"])
    
    def whatsapp_webhook():
    
        num_media = int(request.form.get("NumMedia", 0))
    
        twiml = MessagingResponse()
    
        try:
    
            if num_media > 0 and "audio" in request.form.get("MediaContentType0", ""):
    
                media_url = request.form["MediaUrl0"]
    
                media_response = requests.get(
    
                    media_url,
    
                    auth=(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")),
    
                    timeout=10,
    
                )
    
                media_response.raise_for_status()
    
                audio_file = Path("/tmp/voice_note.ogg")
    
                audio_file.write_bytes(media_response.content)
    
                transcript = sarvam.speech_to_text.transcribe(
    
                    file=open(audio_file, "rb"),
    
                    model="saaras:v4",
    
                    language_code="unknown",
    
                )
    
                user_text = transcript.transcript
    
            else:
    
                user_text = request.form.get("Body", "")
    
            completion = sarvam.chat.completions(
    
                model="sarvam-105b",
    
                messages=[
    
                    {"role": "system", "content": SYSTEM_PROMPT},
    
                    {"role": "user", "content": user_text},
    
                ],
    
            )
    
            reply_text = completion.choices[0].message.content
    
        except Exception:
    
            logger.exception("Failed to process incoming WhatsApp message")
    
            reply_text = "Sorry, I couldn't process that. Please try again in a moment."
    
        message = twiml.message(reply_text)
    
        try:
    
            spoken = sarvam.voice_cloning.convert(
    
                voice_id=VOICE_ID,
    
                text=reply_text,
    
            )
    
            filename = f"{uuid.uuid4().hex}.wav"
    
            (AUDIO_DIR / filename).write_bytes(
    
                base64.b64decode(spoken.audio_b64 or spoken.audio)
    
            )
    
            message.media(f"{request.host_url}audio/{filename}")
    
        except Exception:
    
            logger.exception("Cloned-voice synthesis failed, sending text-only reply")
    
        return Response(str(twiml), mimetype="application/xml")
    
    if __name__ == "__main__":
    
        app.run(port=7861)

### How it works

  * **`resolve_voice_id`** clones the agent from `reference.wav` once, unless `VOICE_ID` is already set. Create is not on the per-message path.
  * **Inbound voice notes** download from Twilio and go to **Saaras** with `language_code="unknown"`, so a Hindi note and a Tamil note work without a code change.
  * **`sarvam-105b`** drafts a short reply in the customer’s language.
  * **`voice_cloning.convert`** speaks that reply with the saved agent voice. Synthesis has its own `try`/`except`, so a cloning failure still leaves the customer with the text reply.
  * `language_code` is omitted on convert so the service detects the language from the reply. Pass the code when pronunciation has to be exact — see [Supported languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/supported-languages).



WhatsApp only renders a native voice-note bubble for OGG/Opus. A `.wav` reply still plays; it shows as a regular audio attachment.

This script trusts every request to `/whatsapp`. Before production, validate `X-Twilio-Signature` with `twilio.request_validator.RequestValidator`.

## **5\. Run It**

Put `reference.wav` next to the script, point the Twilio Sandbox webhook at `https://<ngrok-host>/whatsapp`, then:
    
    
    python support_voice_notes.py
    
    
    ngrok http 7861

Send a text or a voice note to the Sandbox number. You should get a text reply and an audio attachment in the cloned agent’s voice.

## **6\. Tips & Best Practices**

  * **Reference clip:** 10-15 seconds, one speaker, no music. The clone copies pace and emotion, not only timbre. See [Prepare Reference Audio](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/prepare-reference-audio).
  * **Create once:** Reuse `VOICE_ID`. Re-uploading the clip on every process start repeats transcription and can hit the free-plan voice cap.
  * **Reply length:** Keep the system prompt explicit. WhatsApp bodies are capped at 1600 characters, and short replies clone more cleanly.
  * **One-shot vs stream:** WhatsApp needs a finished file to attach, so this guide uses `convert`. For a live voice agent, use [HTTP streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/http-streaming) or [WebSocket](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/websocket-streaming).
  * **Sandbox opt-in:** Recipients must send the Sandbox join code first. See [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot#3-configure-twilio-for-whatsapp).



## **7\. Error Handling**

Retry `429`, `500`, `502`, `503`, and `504` with exponential backoff. Do not retry `400`, `401`, `402`, `403`, `404`, or `422`. Log `request_id` from failed Sarvam responses.

You may also see:

  * **400** on clone — both `voice_id` and `ref_audio` were sent, the clip is too long, or the reply is romanized Indic / Urdu. Keep native script in the chat prompt.
  * **402** — the subscription cannot generate this request.
  * **403** — invalid API key.
  * **Twilio 63015** — the sender has not joined the Sandbox.



For the full table, see [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting) and the [Instant Voice Cloning FAQ](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/faq).

## **8\. Additional Resources**

  * **API overview** : [Instant Voice Cloning](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/overview)
  * **Same channel, stock voice** : [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot)
  * **How-tos** : [Prepare Reference Audio](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/prepare-reference-audio) · [Clone Across Languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/clone-across-languages) · [HTTP Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/http-streaming)
  * **Related APIs** : [Speech-to-Text](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/overview) · [Chat Completion](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview)
  * **Twilio** : [Sandbox for WhatsApp](https://www.twilio.com/docs/whatsapp/sandbox)
  * **Community** : [Join the Discord Community](https://discord.com/invite/5rAsykttcs)



## **9\. Final Notes**

  * Keep API keys in environment variables.
  * Only clone a voice you have the right to use.
  * Create the agent voice once, then reuse `voice_id` on every reply.



**Keep Building!** 🚀

Was this page helpful?

YesNo

[Previous](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot)[Hindi collections voice agent with LiveKitNext](https://docs.sarvam.ai/api/cookbook/example-voice-agents/collection-agent)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=docs.sarvam.ai)

  * Getting Started

    * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
    * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
    * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
    * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
    * [Models](https://docs.sarvam.ai/api/getting-started/models)

    * [Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/ratelimits)
    * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
    * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
    * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
    * [Pricing](https://docs.sarvam.ai/api/getting-started/pricing)
    * Account & Billing

  * API Guides & Tutorials

    * Large Language Models

    * Speech to Text

    * Text to Speech

    * Text Processing

    * Document Intelligence

    * Document Translation

    * Dubbing

    * Instant Voice CloningBeta

  *     * Integration

    * Developer Tools

  * Cookbook

    * Guides
      * [Call Analytics Pipeline](https://docs.sarvam.ai/api/cookbook/guides/call-analytics-pipeline)
      * [Live Video Transcription](https://docs.sarvam.ai/api/cookbook/guides/live-video-transcription)
      * [Podcast Generator](https://docs.sarvam.ai/api/cookbook/guides/podcast-generator)
      * [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot)
      * [Support Voice Notes](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes)
      * [Example Projects on GitHub](https://github.com/sarvamai/sarvam-ai-cookbook/tree/main/examples "Example Projects on GitHub")

    * Example Voice Agents

  * Self-Hosted Deployments

    * Overview

    * AWS SageMaker

  *     * Migrations




  * [Welcome](https://docs.sarvam.ai/api/getting-started/welcome)
  * [Quickstart](https://docs.sarvam.ai/api/getting-started/quickstart)
  * [SDKs & Libraries](https://docs.sarvam.ai/api/getting-started/sdks)
  * [Building for Indian Languages](https://docs.sarvam.ai/api/getting-started/building-for-india)
  * [Models](https://docs.sarvam.ai/api/getting-started/models)
  * [Saaras](https://docs.sarvam.ai/api/getting-started/models/saaras)
  * [Bulbul](https://docs.sarvam.ai/api/getting-started/models/bulbul)
  * [Sarvam 105B](https://docs.sarvam.ai/api/getting-started/models/sarvam-105b)
  * [Open-Weight Models](https://docs.sarvam.ai/api/getting-started/models/openweight)
  * [GLM-5.3](https://docs.sarvam.ai/api/getting-started/models/openweight/glm-5-3)
  * [Gemma 4 31B](https://docs.sarvam.ai/api/getting-started/models/openweight/gemma-4-31b)
  * [DeepSeek V4.1 Flash](https://docs.sarvam.ai/api/getting-started/models/openweight/deepseek-v4.1-flash)
  * [Mayura](https://docs.sarvam.ai/api/getting-started/models/mayura)
  * [Sarvam Translate](https://docs.sarvam.ai/api/getting-started/models/sarvam-translate)
  * [Sarvam Vision](https://docs.sarvam.ai/api/getting-started/models/sarvam-vision)
  * [Sarvam 30B (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-30b)
  * [Sarvam M (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/sarvam-m)
  * [Saarika (Deprecated)](https://docs.sarvam.ai/api/getting-started/models/saarika)
  * [Credits & Rate Limits](https://docs.sarvam.ai/api/getting-started/ratelimits)
  * [Commercial Licensing](https://docs.sarvam.ai/api/getting-started/commercial-licensing)
  * [Errors & Troubleshooting](https://docs.sarvam.ai/api/getting-started/errors-troubleshooting)
  * [Talk to us](https://docs.sarvam.ai/api/getting-started/help)
  * [Pricing](https://docs.sarvam.ai/api/getting-started/pricing)
  * [Organisations & workspaces](https://docs.sarvam.ai/api/platform/organisations-and-workspaces)
  * [Create an organisation](https://docs.sarvam.ai/api/platform/create-an-organisation)
  * [Create a workspace](https://docs.sarvam.ai/api/platform/create-a-workspace)
  * [Invite your team](https://docs.sarvam.ai/api/platform/invite-your-team)
  * [Billing & payments](https://docs.sarvam.ai/api/platform/billing)
  * [Platform FAQ](https://docs.sarvam.ai/api/platform/faq)
  * [Chat Completion](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/overview)
  * [Responses API](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/responses-api)
  * [List your chat messages](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/list-your-chat-messages)
  * [Control response randomness](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-response-randomness)
  * [Control response diversity](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-response-diversity)
  * [Adjust the model's thinking level](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/adjust-the-models-thinking-level)
  * [Encourage new topics in response](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/encourage-new-topics-in-response)
  * [Reduce repetition words or phrases in response](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/reduce-repetition-words-or-phrases-in-response)
  * [Get repeatable results](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/get-repeatable-results)
  * [Control the response length](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-the-response-length)
  * [Control where the model stops](https://docs.sarvam.ai/api/api-guides-tutorials/chat-completion/how-to/control-where-the-model-stops)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/overview)
  * [Which API to Use](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/which-api-to-use)
  * [Rest API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/rest-api)
  * [Batch API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/batch-api)
  * [Realtime Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/realtime-streaming)
  * [Best Practices](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/best-practices)
  * [FAQs](https://docs.sarvam.ai/api/speech-to-text/faq)
  * [Select Output Mode](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/select-output-mode)
  * [Specify Language Codes](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/specify-language-codes)
  * [Enable Speaker Diarization](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/enable-speaker-diarization)
  * [Keyterm Prompting](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/how-to/keyterms)
  * [IVR & Contact Center](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/ivr-contact-center)
  * [BFSI Voice Bots](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/bfsi-voice-bots)
  * [EdTech](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/edtech)
  * [Government Services](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/government-services)
  * [Agri & Rural](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/agri-rural)
  * [Streaming API](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/streaming-api)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/overview)
  * [Voices](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/voices)
  * [Which API to Use](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/which-api-to-use)
  * [Rest API](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/rest-api)
  * [HTTP Stream](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/streaming-api/http-stream)
  * [WebSocket](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/streaming-api/web-socket)
  * [Pronunciation Dictionary](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/pronunciation-dictionary)
  * [Best Practice Guide for Bulbul v4 Flash](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/best-practices)
  * [Best Practices (Bulbul v3)](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/bulbul-v3-best-practices)
  * [Set the Language](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-the-language)
  * [Change the Speaker Voice](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/change-the-speaker-voice)
  * [Adjust the Tone](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-tone)
  * [Adjust the Speed](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-speed)
  * [Adjust the Loudness](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/adjust-the-loudness)
  * [Set the Sample rate](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-the-sample-rate)
  * [Enable Text Preprocessing](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/enable-text-preprocessing)
  * [Set audio format for output](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-audio-format-for-output)
  * [Set bitrate for output](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-bitrate-for-output)
  * [Set maximum length for sentence splitting](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-maximum-length-for-sentence-splitting)
  * [Set buffer size to start processing](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/set-buffer-size-to-start-processing)
  * [IVR & Contact Center](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/ivr-contact-center)
  * [BFSI Voice Bots](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/bfsi-voice-bots)
  * [EdTech](https://docs.sarvam.ai/api/api-guides-tutorials/speech-to-text/use-cases/edtech)
  * [Government Services](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/government-services)
  * [Agri & Rural](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/use-cases/agri-rural)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/overview)
  * [Text Translation](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/translation)
  * [Transliteration](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/transliteration)
  * [Language Detection](https://docs.sarvam.ai/api/api-guides-tutorials/text-processing/language-detection)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview)
  * [Get your config_id](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/get-your-config-id)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/overview)
  * [Set Style Guidelines](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/style-guidelines)
  * [Pick a Genre](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/genre-and-model-tier)
  * [Use Native Numerals](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/native-numerals)
  * [Poll Status and Export Results](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/how-to/poll-and-export)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/faq)
  * [Use Cases](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/use-cases)
  * [Translate a PDF](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/guides/translate-a-pdf)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/overview)
  * [Job Lifecycle](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/job-lifecycle)
  * [Specify Language Codes](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/specify-language-codes)
  * [Control Translation Tone](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/control-translation-tone)
  * [Choose a Voice](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/choose-a-voice)
  * [Choose Export Formats](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/how-to/choose-export-formats)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/faq)
  * [Overview](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/overview)
  * [Prepare Reference Audio](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/prepare-reference-audio)
  * [Clone Across Languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/clone-across-languages)
  * [Choose Audio Formats](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/choose-audio-formats)
  * [Use Quality Control](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/use-quality-control)
  * [HTTP Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/http-streaming)
  * [WebSocket Streaming](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/how-to/websocket-streaming)
  * [Supported Languages](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/supported-languages)
  * [FAQs](https://docs.sarvam.ai/api/api-guides-tutorials/voice-cloning/faq)
  * [LiveKit](https://docs.sarvam.ai/api/integration/build-voice-agent-with-live-kit)
  * [Pipecat](https://docs.sarvam.ai/api/integration/build-voice-agent-with-pipecat)
  * [Twilio](https://docs.sarvam.ai/api/integration/build-voice-agent-with-twilio)
  * [Exotel](https://docs.sarvam.ai/api/integration/build-voice-agent-with-exotel)
  * [Vobiz](https://docs.sarvam.ai/api/integration/build-voice-agent-with-vobiz)
  * [Vapi](https://docs.sarvam.ai/api/integration/build-voice-agent-with-vapi)
  * [n8n](https://docs.sarvam.ai/api/integration/n8n)
  * [Vercel AI SDK](https://docs.sarvam.ai/api/integration/vercel-ai-sdk)
  * [LangChain](https://docs.sarvam.ai/api/integration/langchain)
  * [LiveKit in Production](https://docs.sarvam.ai/api/integration/livekit-production-best-practices)
  * [Pipecat in Production](https://docs.sarvam.ai/api/integration/pipecat-production-guide)
  * [MCP Server](https://docs.sarvam.ai/api/developer-tools/mcp)
  * [Markdown & llms.txt](https://docs.sarvam.ai/api/developer-tools/llms-txt)
  * [Context7](https://docs.sarvam.ai/api/developer-tools/context7)
  * [Agent Skills](https://docs.sarvam.ai/api/developer-tools/agent-skills)
  * [Call Analytics Pipeline](https://docs.sarvam.ai/api/cookbook/guides/call-analytics-pipeline)
  * [Live Video Transcription](https://docs.sarvam.ai/api/cookbook/guides/live-video-transcription)
  * [Podcast Generator](https://docs.sarvam.ai/api/cookbook/guides/podcast-generator)
  * [WhatsApp Bot](https://docs.sarvam.ai/api/cookbook/guides/whats-app-bot)
  * [Support Voice Notes](https://docs.sarvam.ai/api/cookbook/guides/support-voice-notes)
  * [Collection Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/collection-agent)
  * [Government Scheme Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/government-scheme-agent)
  * [Tutor Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/tutor-agent)
  * [Loan Advisory Agent](https://docs.sarvam.ai/api/cookbook/example-voice-agents/loan-advisory-agent)
  * [Introduction](https://docs.sarvam.ai/api/self-hosted/introduction)
  * [Managed vs Self-Hosted](https://docs.sarvam.ai/api/self-hosted/hosted-vs-self-hosted)
  * [How it works](https://docs.sarvam.ai/api/self-hosted/architecture)
  * [Get started](https://docs.sarvam.ai/api/self-hosted/sagemaker/get-started)
  * [Speech-to-Text (Saaras v3)](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-saaras)
  * [Sarvam Vision](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-vision)
  * [Text-to-Speech (Bulbul v3)](https://docs.sarvam.ai/api/self-hosted/sagemaker/deploy-bulbul)
  * [Deploy with Terraform](https://docs.sarvam.ai/api/self-hosted/sagemaker/terraform)
  * [Speech-to-Text](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-saaras)
  * [Sarvam Vision](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-vision)
  * [Text-to-Speech](https://docs.sarvam.ai/api/self-hosted/sagemaker/api-bulbul)
  * [Error handling](https://docs.sarvam.ai/api/self-hosted/sagemaker/errors)
  * [Configure & tune](https://docs.sarvam.ai/api/self-hosted/sagemaker/configure)
  * [Operations](https://docs.sarvam.ai/api/self-hosted/sagemaker/operations)
  * [Limitations](https://docs.sarvam.ai/api/self-hosted/sagemaker/limitations)
  * [Troubleshooting](https://docs.sarvam.ai/api/self-hosted/sagemaker/troubleshooting)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-elevenlabs/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-elevenlabs/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-elevenlabs/speech-to-text)
  * [Instant Voice Cloning](https://docs.sarvam.ai/api/migrations/from-elevenlabs/voice-cloning)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-cartesia/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-cartesia/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-cartesia/speech-to-text)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-deepgram/overview)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-deepgram/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-deepgram/speech-to-text)
  * [Overview](https://docs.sarvam.ai/api/migrations/from-gemini/overview)
  * [Chat Completion](https://docs.sarvam.ai/api/migrations/from-gemini/chat-completion)
  * [Text to Speech](https://docs.sarvam.ai/api/migrations/from-gemini/text-to-speech)
  * [Speech to Text](https://docs.sarvam.ai/api/migrations/from-gemini/speech-to-text)



  * [Model APIs](https://docs.sarvam.ai/api)
  * [Voice Agents](https://docs.sarvam.ai/voice-agents)
  * [Doc Agents](https://docs.sarvam.ai/docai)
  * [Content Studio](https://docs.sarvam.ai/creative)
  * [Cowork](https://docs.sarvam.ai/cowork)
  * [API Reference](https://docs.sarvam.ai/api-reference)
  * [Changelog](https://docs.sarvam.ai/changelog)


