---
url: https://developers.cloudflare.com/cf/agent-feedback/
title: Agent feedback \u00b7 Cloudflare CLI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:00.136200+00:00
---

# Agent feedback · Cloudflare CLI docs

> Source: https://developers.cloudflare.com/cf/agent-feedback/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare CLI](https://developers.cloudflare.com/cf/)
  3. /Agent feedback



# Agent feedback

Last updated Nov 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSend a noteSend an agent reportDiagnostic context

Use `cf feedback` to send bug reports, feature requests, and feedback about where you or your coding agent got stuck. Sign in with `cf auth login` or set `CLOUDFLARE_API_TOKEN` before running the command.

## Send a note

A short note is enough to submit feedback.
    
    
    cf feedback "The deploy output did not identify the selected environment"

Add details with repeatable `--field key=value` flags.
    
    
    cf feedback --field type=friction --field command="cf deploy" --field expected="Show the selected environment" --field actual="The output only showed the Worker name"

## Send an agent report

An agent can send a JSON report from a file or through standard input. Describe the task, the expected and actual results, and any workaround. Use the optional `agent` object for details such as the agent name or commands it ran.

feedback.jsonjson
    
    
    {
    	"type": "friction",
    	"task": "Find the command to list Worker deployments",
    	"expected": "A search result for listing Worker deployments",
    	"actual": "The first result was a command to create a deployment",
    	"impact": "worked_around",
    	"agent": {
    		"name": "claude-code",
    		"commands": ["cf cli search \"list Worker deployments\""]
    	}
    }

Send the file with `cf feedback --input-json feedback.json`. To read the JSON from standard input, set `--input-json=-`. If a `--field` flag and the JSON report supply the same field, the flag takes precedence. Run `cf feedback --help` for supported fields.

The command prints a JSON receipt with a `submission_id` after Cloudflare accepts the report. If you send feedback as an agent through the CLI or MCP tool, tell the user at the next natural break, such as the end of the current turn. Include the submission ID.

## Diagnostic context

Every feedback report includes diagnostic details such as the CLI version, operating system, and detected agent and model, regardless of your CLI telemetry settings. The complete JSON report, including diagnostic context, can be up to 16 KiB.

Feedback requests include the CLI version and execution mode in their headers, along with the agent name when detected. With `DO_NOT_TRACK` enabled, `cf feedback --help` reminds you that sending feedback includes diagnostic context.

[PreviousCoding agents](https://developers.cloudflare.com/cf/agents/)[NextCI and automation](https://developers.cloudflare.com/cf/ci/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cf/agent-feedback.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
