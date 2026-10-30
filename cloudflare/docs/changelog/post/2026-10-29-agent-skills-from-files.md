---
url: https://developers.cloudflare.com/changelog/post/2026-10-29-agent-skills-from-files/
title: Agents SDK: Agent Skills are files in your agent's Workspace \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:18.834904+00:00
---

# Agents SDK: Agent Skills are files in your agent's Workspace · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-29-agent-skills-from-files/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 29, 2026

## Agents SDK: Agent Skills are files in your agent's Workspace

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Agent Skills](https://developers.cloudflare.com/agents/skills/) in the [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) are now files. Write a folder with a `SKILL.md` into your agent's [Computer ↗︎](https://github.com/cloudflare/computer) Workspace, under `/workspace/.agents/skills/`, and the agent can use it on its next turn. You do not need a build step or a deploy, and the agent can write its own skills.

src/server.jsjs
    
    
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think {
    	getSkills() {
    		return [
    			skills.workspace(this.workspace), // /workspace/.agents/skills
    			skills.r2(this.env.SKILLS_BUCKET, { prefix: "skills/" }),
    		];
    	}
    }

src/server.tsts
    
    
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think<Env> {
    	getSkills() {
    		return [
    			skills.workspace(this.workspace), // /workspace/.agents/skills
    			skills.r2(this.env.SKILLS_BUCKET, { prefix: "skills/" }),
    		];
    	}
    }

This release includes:

  * **Three sources.** Load skills from a [Computer Workspace](https://developers.cloudflare.com/agents/skills/sources/computer/), an [R2 bucket](https://developers.cloudflare.com/agents/skills/sources/r2/), or [code](https://developers.cloudflare.com/agents/skills/sources/code/). Think lists every source again before each turn.
  * **The open format.** Every `SKILL.md` is checked against the [Agent Skills specification ↗︎](https://agentskills.io/specification). As the specification's guide for agents recommends, a skill that breaks a rule still loads, with a logged warning. Use `parseSkill()` to check a skill before you write it.
  * **Scripts in the Workspace.** Skill scripts are Workspace files, and the model runs them with the Workspace `exec` tool. Refer to [Execution](https://developers.cloudflare.com/agents/skills/execution/).
  * **Skill tools for any harness.** Use the same `activate_skill` and `read_skill_resource` tools in Think, Pi Durable, or the AI SDK. Refer to [Skills tools](https://developers.cloudflare.com/agents/tools/skills/).
  * **Warm prompt caches.** When a skill changes mid-conversation, Think sends the new catalog as a reminder instead of rebuilding the cached system prompt. An overridden `getSystemPrompt()` now stays at the top of the system prompt, above context blocks.



This is a breaking change for code that uses `agents/skills` directly. The `agents:skills` Vite import, `agents/skills/compile`, `SkillRegistry`, and Think's `skillWorkspace` are removed, and `runner()` moved to `agents/skills/runner`. Install [Agents SDK v0.32.0 ↗︎](https://github.com/cloudflare/agents/releases/tag/agents%400.32.0) and [Think v0.23.0 ↗︎](https://github.com/cloudflare/agents/releases/tag/%40cloudflare%2Fthink%400.23.0) or later. Refer to the [`computer-skills` ↗︎](https://github.com/cloudflare/agents/tree/main/examples/computer-skills) and [`r2-skills` ↗︎](https://github.com/cloudflare/agents/tree/main/examples/r2-skills) examples.
