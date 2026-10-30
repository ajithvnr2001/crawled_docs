---
url: https://developers.cloudflare.com/agents/skills/sources/computer/
title: Computer \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:19.213805+00:00
---

# Computer · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/skills/sources/computer/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Agent Skills](https://developers.cloudflare.com/agents/skills/)

  4. /Sources
  5. /Computer



# Computer

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRead skills from the WorkspaceAdd skills to the WorkspaceRun skill scriptsExample

`skills.workspace()` reads [Agent Skills](https://developers.cloudflare.com/agents/skills/) from files in a Workspace from [`@cloudflare/computer` ↗︎](https://github.com/cloudflare/computer). A skill is a folder in the Workspace. Writing, editing, or deleting a `SKILL.md` changes the agent's skills on its next turn, with no deploy.

## Read skills from the Workspace

By default, every `/workspace/.agents/skills/<name>/SKILL.md` is a skill. The files beside it are its resources:
    
    
    /workspace/.agents/skills/
      release-notes/
        SKILL.md
        references/style-guide.md
        scripts/format-release-notes.js
      pirate-voice/
        SKILL.md

Return the source from `getSkills()`. In [Think](https://developers.cloudflare.com/agents/harnesses/think/), `this.workspace` is already a Computer Workspace:

src/server.jsjs
    
    
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think {
    	getSkills() {
    		return [skills.workspace(this.workspace)];
    	}
    }

src/server.tsts
    
    
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think<Env> {
    	getSkills() {
    		return [skills.workspace(this.workspace)];
    	}
    }

To read skills from another directory, pass an absolute `root`:
    
    
    skills.workspace(this.workspace, { root: "/workspace/skills" });

If the root directory does not exist, the source lists no skills. `.git`, `node_modules`, and `.DS_Store` inside a skill directory are ignored.

## Add skills to the Workspace

Skills are plain files, so anything that writes to the Workspace can add one: the agent's own `write` tool, a user upload, or your code. For example, write the starter skills the first time the agent starts:

src/server.jsjs
    
    
    import { Think, skills } from "@cloudflare/think";
    
    const ROOT = "/workspace/.agents/skills";
    
    const STARTER_SKILLS = {
    	"pirate-voice/SKILL.md": `---
    name: pirate-voice
    description: Answer in a pirate voice. Use when the user asks for a pirate tone.
    ---
    
    Answer accurately, then rewrite the answer in a light pirate voice.
    `,
    };
    
    export class MyAgent extends Think {
    	getSkills() {
    		return [skills.workspace(this.workspace)];
    	}
    
    	async onStart() {
    		for (const [path, content] of Object.entries(STARTER_SKILLS)) {
    			const file = `${ROOT}/${path}`;
    			await this.workspace.fs.mkdir(file.slice(0, file.lastIndexOf("/")), {
    				recursive: true,
    			});
    			await this.workspace.fs.writeFile(file, content);
    		}
    	}
    }

src/server.tsts
    
    
    import { Think, skills } from "@cloudflare/think";
    
    const ROOT = "/workspace/.agents/skills";
    
    const STARTER_SKILLS: Record<string, string> = {
    	"pirate-voice/SKILL.md": `---
    name: pirate-voice
    description: Answer in a pirate voice. Use when the user asks for a pirate tone.
    ---
    
    Answer accurately, then rewrite the answer in a light pirate voice.
    `,
    };
    
    export class MyAgent extends Think<Env> {
    	getSkills() {
    		return [skills.workspace(this.workspace)];
    	}
    
    	async onStart() {
    		for (const [path, content] of Object.entries(STARTER_SKILLS)) {
    			const file = `${ROOT}/${path}`;
    			await this.workspace.fs.mkdir(file.slice(0, file.lastIndexOf("/")), {
    				recursive: true,
    			});
    			await this.workspace.fs.writeFile(file, content);
    		}
    	}
    }

Each skill is checked against the [specification](https://developers.cloudflare.com/agents/skills/#validation) when it is listed. A skill whose `name` does not match its folder still loads with a warning. A skill with no `description` is skipped and logged. Use `skills.parseSkill()` to check a skill before you write it: it follows the specification when it parses with no warnings.

## Run skill scripts

Skill scripts are Workspace files too. Give the Workspace a backend, and the model runs scripts with the `exec` tool. Activating a skill tells the model where the skill's folder is, so it can run a script from there:

src/server.jsjs
    
    
    import { Workspace } from "@cloudflare/computer";
    import { WorkerJavaScriptBackend } from "@cloudflare/computer/backends/worker-javascript";
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think {
    	workspace = new Workspace({
    		storage: this.ctx.storage,
    		backends: [
    			new WorkerJavaScriptBackend({
    				id: "js",
    				loader: this.env.LOADER,
    				access: "read-write",
    			}),
    		],
    	});
    
    	getSkills() {
    		return [skills.workspace(this.workspace)];
    	}
    }

src/server.tsts
    
    
    import { Workspace } from "@cloudflare/computer";
    import { WorkerJavaScriptBackend } from "@cloudflare/computer/backends/worker-javascript";
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think<Env> {
    	workspace = new Workspace({
    		storage: this.ctx.storage,
    		backends: [
    			new WorkerJavaScriptBackend({
    				id: "js",
    				loader: this.env.LOADER,
    				access: "read-write",
    			}),
    		],
    	});
    
    	getSkills() {
    		return [skills.workspace(this.workspace)];
    	}
    }
    
    
    {
    	"worker_loaders": [{ "binding": "LOADER" }],
    }
    
    
    [[worker_loaders]]
    binding = "LOADER"

With the JavaScript backend, a skill can tell the model to run a script by re-exporting it, with `cwd` set to the skill's folder:
    
    
    export { default } from "./scripts/format-release-notes.js";

Refer to [Execution](https://developers.cloudflare.com/agents/skills/execution/) for the options.

## Example

The [`computer-skills` example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/computer-skills) stores skills in a Workspace, runs their scripts with `exec`, and lets you add and delete skills from the UI.

[PreviousSkills](https://developers.cloudflare.com/agents/skills/)[NextR2](https://developers.cloudflare.com/agents/skills/sources/r2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/skills/sources/computer.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
