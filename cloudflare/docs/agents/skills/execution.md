---
url: https://developers.cloudflare.com/agents/skills/execution/
title: Execution \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:18.689622+00:00
---

# Execution · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/skills/execution/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent Skills](https://developers.cloudflare.com/agents/skills/)
  4. /Execution



# Execution

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRun scripts in the WorkspaceScript runner JavaScript scripts Python and Bash scripts Runner optionsRelated

[Agent Skills](https://developers.cloudflare.com/agents/skills/) can bundle scripts under `scripts/`. An agent runs them in one of two ways:

Where the skill lives | How scripts run  
---|---  
[Computer Workspace](https://developers.cloudflare.com/agents/skills/sources/computer/) | The model runs the file with the Workspace `exec` tool  
[R2](https://developers.cloudflare.com/agents/skills/sources/r2/) or a [manifest](https://developers.cloudflare.com/agents/skills/sources/code/) | The experimental script runner, through `run_skill_script`  
  
## Run scripts in the Workspace

When skills are files in a Workspace, a script is a file the agent can run like any other. Give the Workspace a backend, and Think adds the `exec` tool. Refer to [Computer](https://developers.cloudflare.com/agents/skills/sources/computer/#run-skill-scripts) for the setup.

Activating a skill returns its folder as `location`, for example `/workspace/.agents/skills/release-notes`. With the JavaScript backend, the skill's instructions can tell the model to run a script from that folder:
    
    
    export { default } from "./scripts/format-release-notes.js";

The script exports a default async function. It receives the `input` that the model passes to `exec`, and can use `node:fs` to read the Workspace:
    
    
    import { readdir } from "node:fs/promises";
    
    export default async function (input) {
    	const entries = await readdir(input.root ?? "/workspace");
    	return { count: entries.length };
    }

## Script runner

Caution

The script runner is experimental, and its options may change. Prefer storing skills in a Computer Workspace and running scripts with `exec`.

For skills that do not live in a Workspace, `skills.runner()` runs bundled scripts in a Dynamic Worker and adds the `run_skill_script` tool. It needs a Worker Loader binding:
    
    
    {
    	"worker_loaders": [{ "binding": "LOADER" }],
    }
    
    
    [[worker_loaders]]
    binding = "LOADER"

Return the runner from `getSkillScriptRunner()`:

src/server.jsjs
    
    
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think {
    	getSkills() {
    		return [skills.r2(this.env.SKILLS_BUCKET, { prefix: "skills/" })];
    	}
    
    	getSkillScriptRunner() {
    		return skills.runner({ loader: this.env.LOADER });
    	}
    }

src/server.tsts
    
    
    import { Think, skills } from "@cloudflare/think";
    
    export class MyAgent extends Think<Env> {
    	getSkills() {
    		return [skills.r2(this.env.SKILLS_BUCKET, { prefix: "skills/" })];
    	}
    
    	getSkillScriptRunner() {
    		return skills.runner({ loader: this.env.LOADER });
    	}
    }

Outside Think, import the runner from `agents/skills/runner`. It is a separate entry point because it loads `just-bash` and Code Mode:
    
    
    import { runner } from "agents/skills/runner";
    
    const scriptRunner = runner({ loader: env.LOADER });
    
    
    import { runner } from "agents/skills/runner";
    
    const scriptRunner = runner({ loader: env.LOADER });

The runner runs JavaScript, Python, and Bash scripts under `scripts/`. Python runs as a Python Dynamic Worker, and Bash runs through `just-bash`. There is no bundler at runtime: a JavaScript script must be one self-contained module. Compile TypeScript and multi-file scripts, for example with esbuild, before you store the skill.

### JavaScript scripts

JavaScript scripts export a default function that takes the input and a context object:
    
    
    export default async function run(input, ctx) {
    	const guide = ctx.files["references/style-guide.md"]; // bundled text resources
    	const docs = await ctx.workspace.readFile("README.md"); // gated by permission
    	const summary = await ctx.tools.call("summarize", { input }); // explicit tools
    	await ctx.output.writeFile("notes.md", summary); // scratch artifact
    	return { ok: true };
    }

`ctx` is typed as `SkillRunContext` and contains:

Field | Description  
---|---  
`skill` | The skill's name, description, and metadata  
`files` | The skill's text resources, by relative path  
`workspace` | Workspace reads and writes, gated by the `workspace` option  
`tools` | Only the tools passed to the runner, as `tools.call(name, input)` or `tools.name(input)`  
`output` | `writeFile(name, content)` returns scratch files to the model without changing the Workspace  
  
### Python and Bash scripts

Python and Bash scripts use files instead of a context object:

  * `/input.json` holds the input.
  * `/context.json` holds the skill metadata.
  * `/skill` holds `SKILL.md` and the skill's resources.
  * Files written to `/output` are returned to the model.



Python scripts can also define `def run(input, ctx)`.

### Runner options

Option | Default | Description  
---|---|---  
`loader` | Required | Worker Loader binding  
`workspaceInstance` | None | A Computer Workspace that scripts can access  
`workspace` | `"read"` with `workspaceInstance`, else `"none"` | `"none"`, `"read"`, or `"read-write"`  
`tools` | None | Tools scripts can call  
`network` | `false` | Allow outbound network access  
`timeout` | `30000` | Timeout in milliseconds  
  
Scripts get no network access and no tools unless you grant them. Relative paths in `ctx.workspace` resolve against `/workspace`.

## Related

  * [Think tools](https://developers.cloudflare.com/agents/harnesses/think/tools/): how skill tools merge with workspace, custom, MCP, and client tools
  * [Sandbox](https://developers.cloudflare.com/agents/tools/sandbox/): run code in a container



[PreviousCode](https://developers.cloudflare.com/agents/skills/sources/code/)[NextOverview](https://developers.cloudflare.com/agents/harnesses/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/skills/execution.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
