---
url: https://developers.cloudflare.com/changelog/post/2026-11-03-pi-harness-pi-1-5/
title: Agents SDK now supports Pi 1.5 with fewer storage writes and lower memory use \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.637030+00:00
---

# Agents SDK now supports Pi 1.5 with fewer storage writes and lower memory use · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-03-pi-harness-pi-1-5/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2026

## Agents SDK now supports Pi 1.5 with fewer storage writes and lower memory use

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Agents SDK v0.33.0 upgrades [`PiHarness`](https://developers.cloudflare.com/agents/harnesses/pi/) to [Pi 1.5 ↗︎](https://github.com/earendil-works/pi/blob/v1.5.0/packages/durable/CHANGELOG.md#150---2026-11-02). The release reduces storage transactions while streaming, improves throughput across many sessions, and reduces memory use when streaming large tool calls.

#### Performance improvements

  * **Far fewer storage writes while streaming.** Pi stores streamed answers and tool output in batches, within a second of each update, instead of on every update. Over SQLite, this cuts storage transactions by about 27x for long answers and 5.7x for turns with parallel tools, and CPU by about a quarter.
  * **Higher throughput across many sessions.** Pi's scheduler no longer rechecks every conversation on each commit. In a SQLite benchmark with 2,048 sessions, one Pi harness went from 88 to 459 agent runs per second.
  * **Less memory on large answers.** Streaming a 500 KB tool call used to take about 20 seconds of CPU and a 100 MB heap. Pi now appends new text instead of copying it on every update.



Streaming updates remain visible immediately, but are persisted in batches. With the default settings, a crash can lose up to about one second of streamed progress. Refer to [Recovery](https://developers.cloudflare.com/agents/harnesses/pi/#recovery) to configure this interval.

#### Session and tool updates

  * **A view of each session.** [`session.watch()`](https://developers.cloudflare.com/agents/harnesses/pi/#watch-sessions-from-clients) replaces `session.events()`. It returns the newest transcript entries and the session's live state, such as the answer being streamed, running tools, and why the last run ended without an answer.
  * **Continue without adding a message.** The new `session.continue()` API starts a new run using the existing transcript, for example after a model error or when a run reaches its turn limit.
  * **Turn limit.** `defaults.maxTurns` caps the tool rounds a run can take in new sessions.
  * **Tasks that keep crashing end.** Pi now ends a task cut off by its restart limit instead of parking it. `retry()` and the `parked` status are removed.
  * **Browser in Pi's code mode.** Scripts in [Pi's code mode](https://developers.cloudflare.com/agents/tools/browser/#use-it-in-pis-code-mode) can call `browserTool` and pass its screenshots to `image()`. `browserTool` also stops when the harness aborts its call.



#### Continue an unanswered conversation

For an existing session and submission `operationId`, check the result before offering a continuation. For example, after resolving a model error:
    
    
    const result = await session.wait(operationId);
    
    if (result.status === "unanswered" && result.reason === "model_error") {
    	const receipt = await session.continue({
    		operationId: `${operationId}:continue`,
    	});
    	const continued = await session.wait(receipt.operationId);
    	console.log(continued.status, continued.text);
    }
    
    
    const result = await session.wait(operationId);
    
    if (result.status === "unanswered" && result.reason === "model_error") {
    	const receipt = await session.continue({
    		operationId: `${operationId}:continue`,
    	});
    	const continued = await session.wait(receipt.operationId);
    	console.log(continued.status, continued.text);
    }

This starts a new run without appending a user message. The session must be idle. If the transcript already ends in an answer, the operation returns `unanswered` with reason `nothing_to_answer`. Refer to [Work with sessions](https://developers.cloudflare.com/agents/harnesses/pi/#work-with-sessions).

#### Upgrade

Once a conversation runs on Pi 1.5, Pi 1.4 cannot read it. After upgrading, roll forward to fix deployment issues rather than rolling back to Pi 1.4.

Update callers of `session.events()` to use `session.watch()`, and remove uses of `retry()` and the `parked` status. Refer to the [Pi Durable 1.5.0 changelog ↗︎](https://github.com/earendil-works/pi/blob/v1.5.0/packages/durable/CHANGELOG.md#150---2026-11-02) for the full list of breaking changes.

The [Agents SDK v0.33.0 changelog ↗︎](https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md#0330) has step-by-step upgrade instructions. Point your coding agent at them and upgrade today:

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!
