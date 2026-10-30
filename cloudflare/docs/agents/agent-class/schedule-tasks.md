---
url: https://developers.cloudflare.com/agents/agent-class/schedule-tasks/
title: Schedule tasks \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:24.610600+00:00
---

# Schedule tasks · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/agent-class/schedule-tasks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent class](https://developers.cloudflare.com/agents/agent-class/)
  4. /Schedule tasks



# Schedule tasks

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSchedule a callbackAgent methodsKeeping the agent aliveNext steps

The `Agent` class installs the [`Scheduler` capability](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/). Its scheduling methods call the scheduler, and a callback name is the name of a method on your Agent. Schedules are stored in SQLite and run from the Lifecycle's job queue, so they survive restarts and evictions. For schedule options, retries, limits, and natural-language parsing, refer to the [`Scheduler` capability](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/).

## Schedule a callback
    
    
    import { Agent } from "agents";
    
    export class ReminderAgent extends Agent {
    	async onStart() {
    		// Recurring schedules are idempotent, so this adds one row however often the Agent starts.
    		await this.schedule("0 8 * * *", "dailyDigest");
    	}
    
    	async remindLater(message) {
    		await this.schedule(30, "sendReminder", { message }); // in 30 seconds
    		await this.schedule(new Date("2026-12-01T09:00:00Z"), "sendReminder", {
    			message,
    		});
    		await this.scheduleEvery(300, "checkInbox"); // every 5 minutes
    	}
    
    	async sendReminder(payload) {
    		console.log(payload.message);
    	}
    
    	async dailyDigest() {}
    
    	async checkInbox() {}
    }
    
    
    import { Agent } from "agents";
    
    export class ReminderAgent extends Agent<Env> {
    	async onStart() {
    		// Recurring schedules are idempotent, so this adds one row however often the Agent starts.
    		await this.schedule("0 8 * * *", "dailyDigest");
    	}
    
    	async remindLater(message: string) {
    		await this.schedule(30, "sendReminder", { message }); // in 30 seconds
    		await this.schedule(new Date("2026-12-01T09:00:00Z"), "sendReminder", {
    			message,
    		});
    		await this.scheduleEvery(300, "checkInbox"); // every 5 minutes
    	}
    
    	async sendReminder(payload: { message: string }) {
    		console.log(payload.message);
    	}
    
    	async dailyDigest() {}
    
    	async checkInbox() {}
    }

## Agent methods

Agent method | Scheduler equivalent  
---|---  
`schedule(when, callback, payload?, options?)` | `scheduler.set()`  
`scheduleEvery(intervalSeconds, callback, payload?, options?)` | `scheduler.every()`  
`getScheduleById(id)` | `scheduler.get()`  
`listSchedules(criteria?)` | `scheduler.list()`  
`cancelSchedule(id)` | `scheduler.cancel()`  
  
`when` is a delay in seconds, a `Date`, or a cron string. `callback` must name a method on the Agent. `getSchedule()` and `getSchedules()` are deprecated synchronous versions of `getScheduleById()` and `listSchedules()`.

## Keeping the agent alive

An idle Durable Object is evicted after about 70 to 140 seconds without requests, messages, or alarms. Work in flight at that moment stops. `keepAliveWhile()` holds a heartbeat on the shared alarm while a function runs, and releases it when the function settles:
    
    
    import { Agent } from "agents";
    
    export class ReportAgent extends Agent {
    	async buildReport() {
    		return this.keepAliveWhile(async () => {
    			// Long work that must not be interrupted by idle eviction.
    			return "done";
    		});
    	}
    }
    
    
    import { Agent } from "agents";
    
    export class ReportAgent extends Agent<Env> {
    	async buildReport() {
    		return this.keepAliveWhile(async () => {
    			// Long work that must not be interrupted by idle eviction.
    			return "done";
    		});
    	}
    }

`keepAlive()` returns a disposer instead, for work that does not fit one function. Always call the disposer. `AIChatAgent` keeps itself alive while it streams a reply. Scheduled callbacks and Workflows do not need it.

A heartbeat only prevents idle eviction. A deploy or crash still stops the work, so schedule a job or use a [Workflow](https://developers.cloudflare.com/agents/agent-class/run-workflows/) for work that must finish.

## Next steps

### [Scheduler capability](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/)

Schedule options, retries, limits, and parsing schedules from natural language.

### [Queue tasks](https://developers.cloudflare.com/agents/agent-class/queue-tasks/)

Run background work one item at a time.

### [Run Workflows](https://developers.cloudflare.com/agents/agent-class/run-workflows/)

Durable multi-step work with retries.

[PreviousProtocol messages](https://developers.cloudflare.com/agents/agent-class/protocol-messages/)[NextQueue tasks](https://developers.cloudflare.com/agents/agent-class/queue-tasks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/agent-class/schedule-tasks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
