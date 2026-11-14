---
url: https://developers.cloudflare.com/realtime/sfu/concepts/negotiation/
title: Negotiation and session lifecycle \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:55.501925+00:00
---

# Negotiation and session lifecycle · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/sfu/concepts/negotiation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[Realtime SFU](https://developers.cloudflare.com/realtime/sfu/)

  4. /[Concepts](https://developers.cloudflare.com/realtime/sfu/concepts/)
  5. /Negotiation and session lifecycle



# Negotiation and session lifecycle

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOffer and answerSerialize mutations per session Example: simultaneous meeting joinsRetry and reconnectTeardownLearn with an example

A Realtime SFU session has one WebRTC PeerConnection and one offer/answer state machine. Session Description Protocol (SDP) is the setup text that describes the connection's media and transport settings. It does not carry the media itself.

Your endpoint creates or applies SDP. Your backend carries the descriptions between the endpoint and the [SFU API](https://developers.cloudflare.com/realtime/sfu/api/).

## Offer and answer

An offer proposes connection settings, and an answer completes that negotiation. An endpoint can send an offer describing the tracks it wants to publish. The SFU returns an answer for the endpoint to apply.

An SFU operation can also return an offer that the endpoint must answer. When a response sets `requiresImmediateRenegotiation: true`, complete that exchange before starting another mutation on the session.

Apply the SFU offer, create and set the endpoint's answer, and submit that answer through `PUT /sessions/{sessionId}/renegotiate`. Refer to [Complete an SFU offer](https://developers.cloudflare.com/realtime/sfu/get-started/connection-patterns/#complete-an-sfu-offer) for the exact sequence.

Check the response and each resource result before advancing your application's state. An HTTP `200` response alone does not establish that every requested resource succeeded.

## Serialize mutations per session

Serialize mutations that target the same SFU session, including track and DataChannel creation, updates, closure, and renegotiation. Independent operations on different sessions can run concurrently. Application dependencies still apply: a publication must exist before another session can subscribe to it.

Each mutation finishes only after its API request and required SDP exchange succeed. For an endpoint offer, wait until the returned SFU answer is applied. For an SFU offer, wait until the endpoint's answer is accepted through `/renegotiate`. Returning an offer to the browser, or reaching `signalingState: "stable"` there, does not finish the backend's work.

Sequential `await` calls are sufficient when one execution path owns all mutations for a session, and each awaited operation includes that full exchange. When event handlers, timers, or UI actions can overlap, use one shared queue per session. An `await` inside one handler does not prevent another handler from starting a request.

Separate publishing and receiving sessions can simplify an application's ownership model. A single bidirectional session is also valid when all its mutations share the same queue.

### Example: simultaneous meeting joins

In a conferencing application, participant B may join while participant A is still joining. A's initial room snapshot triggers subscriptions to existing participants, while B's join notification triggers another subscription. Both handlers update **A's receiving session**.

If the handlers submit requests independently, the second `tracks/new` can arrive before the first offer/answer exchange finishes. The SFU can reject the conflicting request with HTTP `406`. A `406` can also indicate other invalid requests. Inspect the public `errorCode`, `errorDescription`, and endpoint state when diagnosing it.

Route the initial snapshot and later participant updates through A's receiving-session queue:

**Initial room snapshot**

**Participant-joined handler**

**A's receiving-session queue**

**Realtime SFU**

Subscribe to existing participants

Subscribe to B

tracks/new for existing publications

Offer requiring an answer

A applies the offer and creates an answer

renegotiate with A's answer

Answer accepted

tracks/new for B's publications

Complete the next offer/answer exchange

Queue the subscription work before creating SDP or issuing its API request. When it runs, reconcile it with the current publications and connection. Deduplicate repeated publication locators and discard subscriptions that are no longer wanted. Other sessions can continue while A completes this exchange.

## Retry and reconnect

A lost response leaves the request's outcome unknown. Pause later mutations on that session while recovering. Application-level duplicate detection does not make an SFU request safe to repeat.

Use the interrupted operation to choose the next step:

Interrupted operation | Next step  
---|---  
`sessions/new` | Create a replacement session.  
`tracks/new` | Inspect allocations before creating more tracks. Repeated subscriptions can allocate duplicates. If the SDP response is lost, replace the connection.  
`datachannels/new` | Recover visible allocations through session inspection. An empty snapshot cannot resolve an uncertain request. Retain successful allocations from partial responses.  
`datachannels/establish` | Complete the transport's SDP exchange. If its response is lost, replace the connection. Repeating establish is not a state check.  
`/renegotiate` | A repeated answer can fail after the first succeeds. If acceptance remains unknown, replace the connection. A retry error cannot resolve that uncertainty.  
Forced media close or `datachannels/close` | While the session is live, retry unresolved IDs in order. Process each result.  
Negotiated media close | Apply the original answer if available. Otherwise, close the PeerConnection and discard the session.  
  
[Session inspection](https://developers.cloudflare.com/realtime/sfu/api/#inspect-a-session) can recover resource identifiers, but not lost SDP or request history. [`correlationId`](https://developers.cloudflare.com/realtime/sfu/api/#correlate-session-creation) labels diagnostics. It does not recover or deduplicate a session.

Give a replacement connection a new application attempt ID. Ignore old responses when updating it. Republish and rebuild subscriptions using the new session identifiers.

## Teardown

Stop accepting new mutations, withdraw ended publications from discovery, and close the PeerConnection. [Discard the session](https://developers.cloudflare.com/realtime/sfu/concepts/sessions-tracks/#resource-lifetime) and cancel its queued work.

## Learn with an example

The [video-room negotiation queues ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/video-room/ARCHITECTURE.md#sdp-serialization) hold a session operation open across the browser answer. The [DataChannel example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/echo-datachannels#api-and-lifecycle) demonstrates transport setup and teardown through a local Node.js backend.

For a native endpoint, follow the [embedded firmware/SFU walkthrough ↗︎](https://github.com/cloudflare/realtime-examples/blob/main/esp32-radio/firmware/docs/sfu.md).

[PreviousApplication architecture](https://developers.cloudflare.com/realtime/sfu/concepts/architecture/)[NextOverview](https://developers.cloudflare.com/realtime/sfu/features/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/sfu/concepts/negotiation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
