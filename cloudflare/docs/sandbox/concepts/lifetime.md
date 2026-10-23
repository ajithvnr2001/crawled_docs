---
url: https://developers.cloudflare.com/sandbox/concepts/lifetime/
title: Sandbox lifetime \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:57.537408+00:00
---

# Sandbox lifetime · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/concepts/lifetime/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Concepts](https://developers.cloudflare.com/sandbox/concepts/)
  4. /Lifetime



# Sandbox lifetime

Last updated Oct 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/concepts/lifetime/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewActivity keeps an instance runningAn idle instance is still billedThe timeout does not survive a restartWhat stops an instanceDeploys keep instances runningSnapshots carry files to the next instanceMounted buckets outlive every instanceRelated resources

A Linux sandbox is a [Durable Object](https://developers.cloudflare.com/durable-objects/) that starts and stops a [container](https://developers.cloudflare.com/containers/). Your Worker reaches the Durable Object by name, for example a session ID, and the same name always reaches the same Durable Object. When work arrives, the Durable Object calls [`this.ctx.container.start()`](https://developers.cloudflare.com/containers/api/durable-object-container/#start), which starts a container instance: a Linux virtual machine that runs your image, with its own processes and its own disk.

The Durable Object and the instance last for different lengths of time. The Durable Object keeps its storage, such as session details or a snapshot ID, until your code deletes it. An instance runs only until something stops it, and its processes and the files on its disk end with it. The next `start()` creates a new instance.

This page follows a coding agent. The agent clones a repository, installs its dependencies, edits files, and starts a development server. Then it waits an hour for its next instruction and reaches the same sandbox by name. The files are still there if the instance kept running or the application saved a snapshot. The development server is still there only if the instance kept running.

Instance running

ResetStop instanceStart from snapshot

The Linux instance runs a development server and holds the repository and edits on its disk.

The sandbox of the coding agent, from top to bottom: the name, the Durable Object, the instance, and a mounted R2 bucket. Durable Object storage keeps a snapshot ID. The instance runs the development server and holds the repository and edits on its disk. When the instance stops, its processes and disk files end. The name, the Durable Object, and the objects in the bucket remain. A new instance started from the snapshot has the repository and edits on its disk, and no development server runs until the agent starts it again.

## Activity keeps an instance running

An instance keeps running while its Durable Object is active. The Durable Object is active while it handles a request, runs an alarm, streams a response, or holds open a WebSocket that it accepted with `accept()`. The [browser terminal](https://developers.cloudflare.com/sandbox/commands/open-a-terminal-in-the-browser/) keeps a sandbox running this way, even when nobody types.

After the Durable Object becomes inactive, the instance keeps running for the time set with [`setInactivityTimeout()`](https://developers.cloudflare.com/containers/api/durable-object-container/#setinactivitytimeout), up to 6 hours. A request that arrives within that time reaches the same instance, with its files and processes. Without a timeout, Cloudflare stops the instance shortly after the Durable Object becomes inactive.

Code that runs inside the instance does not count as activity. If no requests arrive, the instance stops when the inactivity timeout ends, even while a build, a test suite, or an agent task still runs inside it. A Durable Object [alarm](https://developers.cloudflare.com/durable-objects/api/alarms/) that runs more often than the timeout and checks the work keeps the instance running until the work ends. For an alarm that runs every minute, refer to [Run background processes](https://developers.cloudflare.com/sandbox/commands/run-background-processes/).

## An idle instance is still billed

While an instance runs, Containers bill its memory and disk, whether or not anything inside it does work. After the instance stops, it is not billed. For the rates, refer to [Containers pricing](https://developers.cloudflare.com/containers/platform/pricing/).

An inactivity timeout longer than the wait between requests keeps processes running through the wait, and you pay for the instance until the next request. A shorter timeout lets the instance stop. A snapshot then carries its files to the next instance, which starts its processes again. To keep its development server running through the hour, the coding agent needs a timeout longer than an hour, and pays for the instance for that hour.

## The timeout does not survive a restart

A Durable Object restarts when it leaves memory and later runs its constructor again, for example after a deploy or between two alarms. Its instance can keep running through the restart. The restarted Durable Object starts without an inactivity timeout, so the instance stops shortly after the Durable Object becomes inactive.

The sandbox examples set the timeout after `start()`, and set it again in the constructor of the Durable Object when the instance is already running. For an example, refer to [`setInactivityTimeout()`](https://developers.cloudflare.com/containers/api/durable-object-container/#setinactivitytimeout).

## What stops an instance

An instance stops when one of these happens:

  * The inactivity timeout ends.
  * Your Worker calls [`destroy()`](https://developers.cloudflare.com/containers/api/durable-object-container/#destroy).
  * The main process exits.
  * A platform event stops it, for example a server restart. Cloudflare does not guarantee that an instance runs for a set time.



The main process is the entrypoint passed to `start()`, or the default command of the image. When it exits, the instance stops, and every command started with `exec()` ends with it. The default command of `cloudflare/debian-trixie` exits right away, so the sandbox examples start that image with `sleep infinity` as the entrypoint, or run a web server as the main process.

When the inactivity timeout ends, every process in the instance receives `SIGTERM`, and Cloudflare stops the instance shortly after, whether or not the processes exit. `destroy()` stops the instance at once, with no time for processes to clean up. Do not rely on a `SIGTERM` handler to finish work. Save the files you need before the instance stops, for example in a snapshot.

Cloudflare does not wake the Durable Object when its instance stops. A pending [`monitor()`](https://developers.cloudflare.com/containers/api/durable-object-container/#monitor) call reports a stop only while the Durable Object is in memory. The call keeps the Durable Object in memory for up to 15 minutes from when the call starts. On compatibility dates before `2026-10-01`, the Durable Object leaves memory after its usual idle period instead, unless the Worker sets the [`durable_object_io_tasks_prevent_eviction`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#durable-object-io-tasks-prevent-eviction) flag. The inactivity timeout starts only after the Durable Object leaves memory, so the instance keeps running past the timeout and the Durable Object incurs duration charges until then. When the Durable Object leaves memory, the call ends without reporting the stop that follows.

To record each stop and its reason, refer to [Run code when a sandbox stops](https://developers.cloudflare.com/sandbox/manage/run-code-when-a-sandbox-stops/).

## Deploys keep instances running

Deploying a new version of your Worker restarts every Durable Object. A running instance keeps running, and the next request reaches the same instance, with its files and processes. Outbound handlers that the Durable Object set up with [`interceptOutboundHttp()`](https://developers.cloudflare.com/containers/api/durable-object-container/#interceptoutboundhttp) remain in place and run the code of the new version.

A running instance keeps the image, entrypoint, and environment variables that it started with. `start()` throws while an instance runs, so a new image or new startup options apply only to instances that start after the deploy. To move a sandbox to a new image, stop its instance, for example with `destroy()`, and start a new one. The files and processes of the old instance end with it.

Requests, streamed responses, and WebSockets that a sandbox is handling during a deploy can keep running on the previous version. Until that work ends, the previous version can also handle new requests for the sandbox, so new code reaches a busy sandbox late. A deploy is therefore not a way to cancel work. The runtime can still shut down a Durable Object, so make clients such as a browser terminal connect again when their connection closes. For more information, refer to [Shutdown behavior](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/#shutdown-behavior).

After the deploy, the instance keeps running for the inactivity timeout that the previous version set. The new version must set the timeout again, as described in The timeout does not survive a restart.

Container [rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/) replace instances only in Container applications that use the [default scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/), so no rollout replaces a sandbox.

## Snapshots carry files to the next instance

The disk of an instance holds the repository, installed packages, configuration files, and output written by commands. Its memory holds running processes, open terminals, and network connections. All of it ends when the instance stops, and the next instance starts from its image or from a snapshot.

Public beta

Container snapshots are in public beta. The API and behavior may change.

[`snapshotContainer()`](https://developers.cloudflare.com/containers/api/durable-object-container/#snapshotcontainer) saves the writable root filesystem of a running instance. It does not save separately mounted filesystems, memory, or processes. Starting with a snapshot creates a new instance with the saved files, and the new instance runs its entrypoint. The processes that were running do not continue. The new instance reuses the same process IDs, so a process ID saved in a file can belong to another process after a restore. Files in `/run` are in memory, and a snapshot does not save them.

Your application decides when to save a snapshot. It stores the snapshot, for example in Durable Object storage, and passes it to the next `start()`. Cloudflare does not restore a snapshot on its own. Changes made after the last snapshot exist only in the current instance, and an instance can stop without warning, so save a snapshot after work that you need to keep.

A snapshot expires 30 days after it is created or last restored. To keep files longer, copy them to a bucket.

The repository, dependencies, and edits of the coding agent return from a snapshot. The development server does not, so the agent starts it again. To save and restore a workspace, refer to [Save and restore a sandbox with snapshots](https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/). To save a sandbox each time it stops for inactivity, refer to [Save a sandbox automatically](https://developers.cloudflare.com/sandbox/files/save-a-sandbox-automatically/).

## Mounted buckets outlive every instance

Files in a mounted [R2](https://developers.cloudflare.com/r2/) bucket are objects in that bucket. They remain after every instance stops, and other sandboxes and Workers with access to the bucket can read them. A snapshot does not include mounted directories, and a mount ends with its instance, so each new instance mounts the bucket again.

Use a snapshot for files that belong to one continuing workspace. Use a bucket for files that other systems read, or that must outlive the workspace. To mount a bucket, refer to [Mount an R2 bucket](https://developers.cloudflare.com/sandbox/files/mount-an-r2-bucket/).

## Related resources

  * [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/)
  * [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/)
  * [Durable Object alarms](https://developers.cloudflare.com/durable-objects/api/alarms/)



[PreviousChoose an environment](https://developers.cloudflare.com/sandbox/concepts/)[NextSecurity](https://developers.cloudflare.com/sandbox/concepts/security/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/concepts/lifetime.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
