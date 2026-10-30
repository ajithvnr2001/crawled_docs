---
url: https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/
title: Scheduler \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:16.587022+00:00
---

# Scheduler · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Runtime](https://developers.cloudflare.com/agents/runtime/)

  4. /[Capabilities](https://developers.cloudflare.com/agents/runtime/capabilities/)
  5. /Scheduler



# Scheduler

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstall the capabilityOptionsSchedule work Per-schedule optionsManage schedulesFailures and retriesLimitsParse schedules from natural languageObservabilityOn the Agent class

`Scheduler` from `agents/schedules` runs registered callbacks in the future: after a delay, at a date, from a cron expression, or at a fixed interval. Schedules are stored as jobs in the [Lifecycle job queue](https://developers.cloudflare.com/agents/runtime/lifecycle/job-queue/), so they survive eviction and share the object's alarm with other capabilities.

## Install the capability

Register callbacks by name in the constructor, then install the scheduler on the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/):
    
    
    import { DurableObject } from "cloudflare:workers";
    import { getCurrentAgent, Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    export class ReminderAgent extends DurableObject {
    	scheduler = new Scheduler({
    		callbacks: {
    			sendReminder: (payload, schedule) => {
    				const { agent } = getCurrentAgent();
    				console.log(
    					`${agent?.lifecycle.name}: reminder ${schedule.id}: ${payload.message}`,
    				);
    			},
    		},
    	});
    	lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	async onStart() {
    		// Cron schedules are idempotent, so this adds one row, not one per wake.
    		await this.scheduler.set("0 8 * * 1-5", "sendReminder", {
    			message: "Good morning",
    		});
    	}
    
    	async onRequest() {
    		const schedule = await this.scheduler.set(300, "sendReminder", {
    			message: "Five minutes have passed",
    		});
    		return Response.json(schedule, { status: 201 });
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { getCurrentAgent, Lifecycle } from "agents/lifecycle";
    import { Scheduler, type Schedule } from "agents/schedules";
    
    type Reminder = { message: string };
    
    export class ReminderAgent extends DurableObject<Env> {
    	readonly scheduler = new Scheduler({
    		callbacks: {
    			sendReminder: (payload: Reminder, schedule: Schedule<Reminder>) => {
    				const { agent } = getCurrentAgent<ReminderAgent>();
    				console.log(
    					`${agent?.lifecycle.name}: reminder ${schedule.id}: ${payload.message}`,
    				);
    			},
    		},
    	});
    	readonly lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	async onStart(): Promise<void> {
    		// Cron schedules are idempotent, so this adds one row, not one per wake.
    		await this.scheduler.set("0 8 * * 1-5", "sendReminder", {
    			message: "Good morning",
    		});
    	}
    
    	async onRequest(): Promise<Response> {
    		const schedule = await this.scheduler.set(300, "sendReminder", {
    			message: "Five minutes have passed",
    		});
    		return Response.json(schedule, { status: 201 });
    	}
    }

Each schedule stores the callback's name, not the function. The callbacks map is rebuilt every time the object starts, so a schedule created before an eviction finds its callback after the object wakes. Register every callback unconditionally in the field initializer.

`set()` and `every()` check the callback name and the payload type against the map. A callback receives the payload and the `Schedule` that fired. It runs inside your object's invocation context, so [`getCurrentAgent()`](https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/) returns the object.

## Options

Option | Description  
---|---  
`callbacks` | Named callbacks `(payload, schedule) => unknown`  
`retry` | Default retry policy for callbacks: `{ maxAttempts, baseDelayMs, maxDelayMs }`. Defaults to `3`, `100`, and `3000`  
`hungScheduleTimeoutSeconds` | Seconds before a running interval schedule counts as abandoned. Defaults to `30`  
`onError` | `(error) => void`. Observes a callback's failure after its last retry  
  
## Schedule work

`set(when, callback, payload?, options?)` takes the time as its first argument. The type of `when` picks the mode:

`when` | Mode | Example  
---|---|---  
`number` | `delayed` | `set(60, "sendReminder", payload)` runs in 60 seconds  
`Date` | `scheduled` | `set(new Date("2026-12-25T09:00:00Z"), ...)`  
`string` | `cron` | `set("0 8 * * 1-5", ...)` runs at 08:00 UTC on weekdays  
  
`every(intervalSeconds, callback, payload?, options?)` creates an `interval` schedule:
    
    
    await this.scheduler.every(30, "sendReminder", { message: "Every 30 seconds" });

The first interval run happens after `intervalSeconds`, not immediately. If a run is still going when the next one is due, the scheduler skips that run.

Both methods return the stored `Schedule`. It has an `id`, the `callback` name, the `payload`, a `type`, and the next run `time` as a Unix timestamp in seconds. Depending on the type, it also has `delayInSeconds`, `cron`, or `intervalSeconds`.

### Per-schedule options

Pass options as the fourth argument:

Option | Description  
---|---  
`retry` | Overrides the scheduler's retry policy for this schedule  
`idempotent` | Returns an existing schedule with the same callback, timing, and payload instead of adding a row  
  
`idempotent` defaults to `true` for cron and interval schedules. You can create recurring schedules in `onStart()` without adding a row on every wake. It defaults to `false` for delayed and dated schedules, which add a row on every call unless you pass `{ idempotent: true }`.

## Manage schedules

Method | Description  
---|---  
`get(id)` | Returns one schedule, or `undefined`  
`list(criteria?)` | Returns schedules, filtered by `id`, `type`, or `timeRange: { start?, end? }`  
`cancel(id)` | Removes a schedule. Returns `true` if one was removed  
      
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    export class ReminderAgent extends DurableObject {
    	scheduler = new Scheduler({
    		callbacks: {
    			sendReminder: (payload) => console.log(payload.message),
    		},
    		retry: { maxAttempts: 5, baseDelayMs: 500, maxDelayMs: 10_000 },
    		onError: (error) => console.error("Reminder failed", error),
    	});
    	lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	// An RPC method, so it starts the Lifecycle itself.
    	async resetReminders() {
    		await this.lifecycle.start();
    		const crons = await this.scheduler.list({ type: "cron" });
    		for (const schedule of crons) {
    			await this.scheduler.cancel(schedule.id);
    		}
    		await this.scheduler.set(
    			60,
    			"sendReminder",
    			{ message: "Reminders reset" },
    			{ idempotent: true, retry: { maxAttempts: 1 } },
    		);
    		return crons.length;
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    type Reminder = { message: string };
    
    export class ReminderAgent extends DurableObject<Env> {
    	readonly scheduler = new Scheduler({
    		callbacks: {
    			sendReminder: (payload: Reminder) => console.log(payload.message),
    		},
    		retry: { maxAttempts: 5, baseDelayMs: 500, maxDelayMs: 10_000 },
    		onError: (error) => console.error("Reminder failed", error),
    	});
    	readonly lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	// An RPC method, so it starts the Lifecycle itself.
    	async resetReminders(): Promise<number> {
    		await this.lifecycle.start();
    		const crons = await this.scheduler.list({ type: "cron" });
    		for (const schedule of crons) {
    			await this.scheduler.cancel(schedule.id);
    		}
    		await this.scheduler.set(
    			60,
    			"sendReminder",
    			{ message: "Reminders reset" },
    			{ idempotent: true, retry: { maxAttempts: 1 } },
    		);
    		return crons.length;
    	}
    }

A one-time schedule is deleted after it runs. A cron or interval schedule moves to its next run time.

## Failures and retries

A callback that throws is retried with exponential backoff, up to `maxAttempts`. After the last attempt, `onError` runs. A one-time schedule is then removed, and a recurring schedule continues at its next run.

If the object is evicted while a callback runs, the Lifecycle alarm wakes it again and the callback runs again. Make external effects idempotent.

## Limits

  * Cron schedules have minute precision. Interval schedules have second precision.
  * Callbacks run one at a time with every other job on the object. Keep them short.
  * Payloads must be JSON-serializable.



## Parse schedules from natural language

`agents/schedules/parser` exports a prompt and a Zod schema that turn a request such as "remind me every Monday at 9" into a structured schedule. Use them with a model call that supports structured output:
    
    
    import { getSchedulePrompt, scheduleSchema } from "agents/schedules/parser";
    import { generateObject } from "ai";
    
    export async function parseRequest(input) {
    	const { object } = await generateObject({
    		model,
    		schema: scheduleSchema,
    		system: getSchedulePrompt({ date: new Date() }),
    		prompt: input,
    	});
    	return object; // { description, when: { type: "delayed", delayInSeconds } | ... }
    }
    
    
    import { getSchedulePrompt, scheduleSchema } from "agents/schedules/parser";
    import { generateObject, type LanguageModel } from "ai";
    
    declare const model: LanguageModel;
    
    export async function parseRequest(input: string) {
    	const { object } = await generateObject({
    		model,
    		schema: scheduleSchema,
    		system: getSchedulePrompt({ date: new Date() }),
    		prompt: input,
    	});
    	return object; // { description, when: { type: "delayed", delayInSeconds } | ... }
    }

`when.type` is `scheduled` with a `date`, `delayed` with `delayInSeconds`, `cron` with a `cron` expression, or `no-schedule`. The older `agents/schedule` import path still works but is deprecated.

## Observability

The scheduler publishes `schedule:create`, `schedule:execute`, `schedule:retry`, `schedule:error`, and `schedule:cancel` events to the `agents:schedule` [diagnostics channel](https://developers.cloudflare.com/agents/runtime/observability/diagnostics-channels/).

## On the Agent class

The [`Agent` class](https://developers.cloudflare.com/agents/agent-class/) installs a `Scheduler`. Its `this.schedule()`, `this.scheduleEvery()`, `this.getSchedule()`, `this.listSchedules()`, and `this.cancelSchedule()` methods call it, and callback names resolve to methods on the Agent. For more information, refer to [Schedule tasks](https://developers.cloudflare.com/agents/agent-class/schedule-tasks/).

[PreviousState](https://developers.cloudflare.com/agents/runtime/capabilities/state/)[NextMCPClientManager](https://developers.cloudflare.com/agents/runtime/capabilities/mcp-client-manager/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/capabilities/scheduler.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
