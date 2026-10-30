---
url: https://developers.cloudflare.com/agents/skills/sources/code/
title: Code \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:18.900497+00:00
---

# Code · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/skills/sources/code/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Agent Skills](https://developers.cloudflare.com/agents/skills/)

  4. /Sources
  5. /Code



# Code

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDefine skillsEntry fieldsCombine with other sources

`skills.manifest()` creates a source from [Agent Skills](https://developers.cloudflare.com/agents/skills/) defined in code. It needs no Workspace or bucket, which suits tests and small sets of skills that ship with your Worker.

## Define skills

Each entry holds the `SKILL.md` fields and, optionally, its resources:

src/server.jsjs
    
    
    import { Think, skills } from "@cloudflare/think";
    
    const handbook = skills.manifest({
    	id: "handbook",
    	skills: [
    		{
    			name: "release-notes",
    			description: "Turn a list of changes into release notes.",
    			body: "Read `references/style-guide.md`, then write one line per change.",
    			metadata: { author: "my-team" },
    			resources: [
    				{
    					path: "references/style-guide.md",
    					content: "Start each line with a past-tense verb.",
    				},
    			],
    		},
    	],
    });
    
    export class MyAgent extends Think {
    	getSkills() {
    		return [handbook];
    	}
    }

src/server.tsts
    
    
    import { Think, skills } from "@cloudflare/think";
    
    const handbook = skills.manifest({
    	id: "handbook",
    	skills: [
    		{
    			name: "release-notes",
    			description: "Turn a list of changes into release notes.",
    			body: "Read `references/style-guide.md`, then write one line per change.",
    			metadata: { author: "my-team" },
    			resources: [
    				{
    					path: "references/style-guide.md",
    					content: "Start each line with a past-tense verb.",
    				},
    			],
    		},
    	],
    });
    
    export class MyAgent extends Think<Env> {
    	getSkills() {
    		return [handbook];
    	}
    }

## Entry fields

Field | Required | Description  
---|---|---  
`name` | Yes | Skill name. Must follow the [naming rules](https://developers.cloudflare.com/agents/skills/#validation)  
`description` | Yes | What the skill does and when to use it  
`body` | Yes | Markdown instructions  
`license` | No | License name or bundled license file  
`compatibility` | No | Environment requirements  
`metadata` | No | String key-value metadata  
`allowedTools` | No | Space-separated list of pre-approved tools  
`resources` | No | Files as `{ path, content }`. Use `encoding: "base64"` for binary files  
  
Entries pass the same [checks](https://developers.cloudflare.com/agents/skills/#validation) as `SKILL.md` files: an entry that breaks a rule loads with a warning, and one with no `description` is skipped and logged.

`skills.fromManifest()` is a deprecated alias of `skills.manifest()`.

## Combine with other sources

A manifest works next to other sources. Sources are applied in order, so put the source you want to win first:
    
    
    export class MyAgent extends Think {
    	getSkills() {
    		return [skills.workspace(this.workspace), handbook];
    	}
    }
    
    
    export class MyAgent extends Think<Env> {
    	getSkills() {
    		return [skills.workspace(this.workspace), handbook];
    	}
    }

Here, a Workspace skill named `release-notes` replaces the manifest's version.

[PreviousR2](https://developers.cloudflare.com/agents/skills/sources/r2/)[NextExecution](https://developers.cloudflare.com/agents/skills/execution/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/skills/sources/code.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
