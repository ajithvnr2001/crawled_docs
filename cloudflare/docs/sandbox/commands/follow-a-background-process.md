---
url: https://developers.cloudflare.com/sandbox/commands/follow-a-background-process/
title: Follow a background process \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:49.656982+00:00
---

# Follow a background process · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/commands/follow-a-background-process/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Run commands](https://developers.cloudflare.com/sandbox/commands/)
  4. /Follow a background process



# Follow a background process

Last updated Oct 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/commands/follow-a-background-process/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesFollow the outputWait for a log lineRelated resources

Read the output of a background process while it runs, from a request other than the one that started it. A page can show each line as the process prints it, and your Worker can wait until a process prints a line, such as `ready` from a development server.

## Prerequisites

  * A Worker that runs background processes, with the scripts, `run()`, `status()`, and the routes from [Run background processes](https://developers.cloudflare.com/sandbox/commands/run-background-processes/).



## Follow the output

  1. Add a method that sends the output of a process as server-sent events while the process runs:

src/index.tsts
         
         export class MyContainer extends DurableObject<Env> {
         	// ...
         
         	async follow(id: string, stream: "stdout" | "stderr"): Promise<Response | undefined> {
         		const status = await this.status(id);
         
         		if (!status) {
         			return undefined;
         		}
         
         		const path = `${ROOT}/${id}/${stream}.log`;
         		const argv =
         			status.state === "running"
         				? ["tail", "-n", "+1", "-F", "--pid", `${status.pid}`, path]
         				: ["cat", path];
         		const process = await this.ctx.container!.exec(argv, { stderr: "ignore" });
         		const { readable, writable } = new TransformStream<Uint8Array, Uint8Array>();
         		const writer = writable.getWriter();
         		const encoder = new TextEncoder();
         
         		const send = (event: string, data: unknown) =>
         			writer.write(
         				encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`),
         			);
         
         		let exited = false;
         		const markExited = () => {
         			exited = true;
         		};
         		process.exitCode.then(markExited, markExited);
         
         		// Signaling a process that has exited records an internal error.
         		const stop = () => {
         			if (!exited) process.kill();
         		};
         
         		// Stop following when the client disconnects.
         		writer.closed.catch(stop);
         
         		// Detect a disconnected client while the log is quiet.
         		const heartbeat = setInterval(() => {
         			writer.write(encoder.encode(": keep-alive\n\n")).catch(() => {});
         		}, 5_000);
         
         		const pump = async () => {
         			try {
         				for await (const text of process.stdout!.pipeThrough(
         					new TextDecoderStream(),
         				)) {
         					await send(stream, text);
         				}
         				const ended = await this.status(id);
         				const exitCode = ended?.state === "exited" ? ended.exitCode : null;
         				await send("exit", { exitCode });
         				await writer.close();
         			} catch (error) {
         				stop();
         				// End the response, so a connected client does not wait forever.
         				await writer.abort(error).catch(() => {});
         			} finally {
         				clearInterval(heartbeat);
         			}
         		};
         
         		void pump();
         
         		return new Response(readable, {
         			headers: {
         				"Content-Type": "text/event-stream",
         				"Cache-Control": "no-cache",
         			},
         		});
         	}
         }

`follow()` sends the output so far, then new output until the process exits and `tail --pid` stops. Each event is named after the stream, and holds a JSON-encoded chunk of output, which can be part of a line or several lines. When the output ends, `follow()` sends an `exit` event with the exit code, or `null` when the process recorded none. A page can read the stream with `EventSource`, as in [Stream command output](https://developers.cloudflare.com/sandbox/commands/stream-command-output/#read-the-stream-in-a-browser).

`follow()` notices a disconnected client only when a write fails. The keep-alive comment every five seconds makes that write happen while the log is quiet, so `follow()` stops `tail`. Without the comment, `tail` keeps running until the process exits.

  2. In the `logs` branch of your Worker route, follow the output when the query has `follow`. Add this before the call to `sandbox.logs()`:

src/index.tsts
         
         if (url.searchParams.has("follow")) {
         	const response = await sandbox.follow(id, stream);
         	return response ?? new Response("Not found", { status: 404 });
         }

  3. Deploy your Worker:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  4. Start a process named `ticker`, then follow its output. Replace the example hostname with the `workers.dev` URL that Wrangler prints:
         
         curl https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/processes/ticker --request POST
         curl "https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/processes/ticker/logs?follow" --no-buffer

The second request prints the lines so far as one event, then a new event each second:
         
         event: stdout
         data: "ready\ntick 1\ntick 2\ntick 3\ntick 4\n"
         
         event: stdout
         data: "tick 5\n"
         
         event: stdout
         data: "tick 6\n"

Add `stream=stderr` to the query to follow standard error.

  5. In another terminal, stop the process:
         
         curl https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/processes/ticker --request DELETE

The followed output ends with an `exit` event:
         
         event: exit
         data: {"exitCode":143}




## Wait for a log line

A development server prints a line, such as `ready`, when it accepts requests. To wait for that line before you use the server, check the log files until a line matches or the process exits:

  1. Add a script that checks the logs of a process:

src/index.jsjs
         
         // Prints the first matching line and exits with 0. Exits with 3 when the
         // process ends without printing one, 4 when there is no such process, and
         // 5 when the process was lost, for example in an earlier instance.
         const WAIT = `${CURRENT}
         dir=$1; pattern=$2
         [ -d "$dir" ] || exit 4
         while :; do
           exited=false; [ -e "$dir/exit-code" ] && exited=true
           if ! $exited && [ -e "$dir/pid" ] && ! { current "$dir" && kill -0 "$pid" 2>/dev/null; }; then
             sleep 0.1; [ -e "$dir/exit-code" ] || exit 5; exited=true
           fi
           line=$(grep -h -m 1 -E -e "$pattern" "$dir/stdout.log" "$dir/stderr.log" 2>/dev/null | head -n 1)
           [ -n "$line" ] && { printf '%s\\n' "$line"; exit 0; }
           $exited && exit 3
           sleep 0.2
         done`;

src/index.tsts
         
         // Prints the first matching line and exits with 0. Exits with 3 when the
         // process ends without printing one, 4 when there is no such process, and
         // 5 when the process was lost, for example in an earlier instance.
         const WAIT = `${CURRENT}
         dir=$1; pattern=$2
         [ -d "$dir" ] || exit 4
         while :; do
           exited=false; [ -e "$dir/exit-code" ] && exited=true
           if ! $exited && [ -e "$dir/pid" ] && ! { current "$dir" && kill -0 "$pid" 2>/dev/null; }; then
             sleep 0.1; [ -e "$dir/exit-code" ] || exit 5; exited=true
           fi
           line=$(grep -h -m 1 -E -e "$pattern" "$dir/stdout.log" "$dir/stderr.log" 2>/dev/null | head -n 1)
           [ -n "$line" ] && { printf '%s\\n' "$line"; exit 0; }
           $exited && exit 3
           sleep 0.2
         done`;

Do not pipe `tail -F` into `grep -m 1` instead: `tail` keeps running after `grep` exits, until the next line arrives.

  2. Add a method that runs the script with a time limit:

src/index.tsts
         
         export class MyContainer extends DurableObject<Env> {
         	// ...
         
         	async waitForLog(id: string, pattern: string, timeoutMs: number) {
         		const container = this.ctx.container;
         
         		if (!container?.running) {
         			return undefined;
         		}
         
         		const result = await run(container, [
         			"timeout",
         			"--kill-after=5",
         			`${timeoutMs / 1000}`,
         			"sh",
         			"-c",
         			WAIT,
         			"sh",
         			`${ROOT}/${id}`,
         			pattern,
         		]);
         
         		if (result.exitCode === 0) {
         			return { state: "matched", line: result.stdout.trimEnd() };
         		}
         
         		if (result.exitCode === 3) {
         			return { state: "exited" };
         		}
         
         		if (result.exitCode === 4) {
         			return undefined;
         		}
         
         		if (result.exitCode === 5) {
         			return { state: "lost" };
         		}
         
         		// 124 when the time limit passes, or 137 if timeout also sends SIGKILL.
         		if (result.exitCode === 124 || result.exitCode === 137) {
         			return { state: "timed-out" };
         		}
         
         		throw new Error(`The log check failed with exit code ${result.exitCode}`);
         	}
         }

`timeout` stops the script when the time limit passes. If the script is still running five seconds later, `--kill-after=5` stops it with `SIGKILL`.

  3. Call it after `startProcess()`, for example with the pattern `^ready`:

src/index.tsts
         
         const ready = await sandbox.waitForLog(id, "^ready", 30_000);
         
         { "state": "matched", "line": "ready" }

The pattern is an extended regular expression. The state is `exited` when the process ends without printing a matching line, `lost` when it ended without recording an exit code, and `timed-out` when the time limit passes first. The method returns `undefined` when no process uses the ID. A process that was still running when an earlier instance stopped is `lost`, even when its log matches, because `current()` checks the boot ID.




## Related resources

  * [Run background processes](https://developers.cloudflare.com/sandbox/commands/run-background-processes/): start, check, and stop the processes that this page follows.
  * [Stream command output](https://developers.cloudflare.com/sandbox/commands/stream-command-output/): stream the output of a command that finishes while the request is open.
  * [Run a server in the background](https://developers.cloudflare.com/sandbox/commands/run-a-server-in-the-background/): processes that run until the container stops.



[PreviousRun background processes](https://developers.cloudflare.com/sandbox/commands/run-background-processes/)[NextRun a server in the background](https://developers.cloudflare.com/sandbox/commands/run-a-server-in-the-background/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/commands/follow-a-background-process.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
