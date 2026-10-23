---
url: https://docs.comfy.org/development/api-development/sdks/
title: Comfy SDKs: Python and TypeScript Clients for ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:42.402730+00:00
---

# Comfy SDKs: Python and TypeScript Clients for ComfyUI - ComfyUI

> Source: https://docs.comfy.org/development/api-development/sdks/

## On this page

  * Install
  * Quickstart
  * Choosing a base URL
    * Comfy Cloud
    * Comfy API deployment
    * Your own ComfyUI
  * Retrying a submit: the idempotency key
  * Watching a job run
    * events() is not subscribe()
  * Tracing an output back to its workflow
  * Label jobs and find them later
    * Over HTTP
  * What the SDKs cover today
  * Reference
  * Feedback



Run Workflows

# Comfy SDKs: Python and TypeScript Clients for ComfyUI

Copy pageCopy page

Run ComfyUI workflows from Python or TypeScript against Comfy Cloud, a deployment or your own ComfyUI: assets, jobs, live events and idempotent retries.

Copy pageCopy page

Comfy API v2 is versioned. Changes within v2 are additive; breaking changes ship as v3. Report problems through Feedback.

**One package, two surfaces.** `comfy-sdk` (PyPI) and `@comfyorg/sdk` (npm) ship two clients that talk to two different services. Method names repeat across them (`run`, `submit`, `events`) and mean different things in each, so check which client a snippet builds before you copy it.

Surface| What it does| How you reach it| Base URL| Auth  
---|---|---|---|---  
**[Comfy Router](https://docs.comfy.org/development/comfy-router/quickstart)**|  Calls a partner model (FLUX, Veo, Gemini, Kling) with that provider’s own request body and hands back its native response| Python: `client.models` on a `Comfy()`. TypeScript: `comfy.models` on the module-level `comfy` namespace| `https://api.comfy.org`, route `/v2/models/{provider}/{model}`| `COMFY_API_KEY`, or `comfy.config({ credentials })`  
**[Comfy Cloud and Comfy API v2](https://docs.comfy.org/development/api-development/sdks)**|  Runs an API-format ComfyUI workflow end to end: upload assets, submit the graph, follow the job, download outputs| `Comfy(api_key=...)` / `new Comfy({ apiKey })`, then `client.workflows`, `client.assets`, `client.jobs`| `https://cloud.comfy.org` by default, or whatever `COMFY_BASE_URL` names| `api_key` / `apiKey` on the constructor  
  
Neither surface wraps the other, and one API key created in [your Comfy workspace](https://platform.comfy.org/profile/api-keys) works for both.

The two languages expose the Router surface differently. In Python, `Comfy()` carries both: `client.models.run(...)` for Router and `client.workflows` / `client.assets` / `client.jobs` for Cloud. In TypeScript they are separate exports with deliberately similar names: `comfy` (lowercase, the module-level namespace) holds `comfy.models`, while `Comfy` (the class) is the Cloud client and has no `.models`.

This page documents the second row: the Comfy Cloud and Comfy API v2 client. For the model router, start at the [Comfy Router quickstart](https://docs.comfy.org/development/comfy-router/quickstart). The Comfy SDKs let your application run ComfyUI workflows and get the results back. You submit a workflow, ComfyUI executes it, and you download the outputs. The same code runs against Comfy Cloud or against a ComfyUI instance you host yourself. Only the base URL changes, except for job labels, which work only on a Comfy API deployment, and the job list, which Comfy Cloud does not offer yet. The SDKs are clients for the [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview), a versioned HTTP API that we intend to support long term. New releases of ComfyUI will not break integrations built on it. Things people build this way:

  * Plugins that generate content inside another application, such as Blender or Krita
  * Consumer apps that run generation on behalf of their users
  * Batch pipelines, for example running one workflow over every frame of a video
  * Backend services that need many workflows in flight at once



These SDKs drive ComfyUI **from the outside**. If you are writing custom nodes or frontend extensions that run **inside** ComfyUI, you want [Develop Custom Nodes](https://docs.comfy.org/custom-nodes/overview) instead. Those are a separate set of APIs.

## 

​

Install

Python

TypeScript
    
    
    pip install comfy-sdk
    
    
    
    npm i @comfyorg/sdk
    

Python 3.10 or newer. Node 22 or newer.

**Current release: 0.5.0.** [`comfy-sdk`](https://pypi.org/project/comfy-sdk/) on PyPI and [`@comfyorg/sdk`](https://www.npmjs.com/package/@comfyorg/sdk) on npm are released together and share a version number. Install the latest (`pip install comfy-sdk`, `npm install @comfyorg/sdk`) or state a range rather than an exact pin. The two ecosystems spell that differently: `comfy-sdk>=0.5` is a floor and accepts later minors, while `@comfyorg/sdk@^0.5` is npm’s compatible range for `0.5.x` and stops short of `0.6.0`, so a caret range needs raising when a new minor ships. Use `@comfyorg/sdk@>=0.5.0` if you want the npm side to track later minors too. The registry pages are authoritative if this note is behind.

## 

​

Quickstart

Upload an input image, run a workflow, and write the results to disk.

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    # Comfy Cloud
    client = Comfy(api_key="comfyui-...")
    
    wf = client.workflows.from_file("workflow_api.json")
    
    asset = client.assets.from_file("photo.png")
    wf.set_input("10", "image", asset)
    
    job = client.run(wf)
    for output in job.get_outputs("9"):
        output.to_file(output.name)
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    // Comfy Cloud
    const client = new Comfy({ apiKey: "comfyui-..." });
    
    const wf = await client.workflows.fromFile("workflow_api.json");
    
    const asset = client.assets.fromFile("photo.png");
    wf.setInput("10", "image", asset);
    
    const job = await client.run(wf);
    await job.getOutputs("9")[0].toFile("out.png");
    

`workflow_api.json` is a workflow saved in [API format](https://docs.comfy.org/development/api-development/workflow-api-format). `"10"` and `"9"` are node IDs from that file: the node the input image feeds into, and the output node whose results you want. Asset handles are lazy. `photo.png` is hashed locally and only uploaded if the server does not already have those bytes, so re-running with the same input costs nothing. `run()` submits the job and waits for it to reach a terminal state. To do work while it executes, use `submit()` instead and watch the event stream. To run against your own ComfyUI instead, set `COMFY_BASE_URL` and drop the key. See below.

## 

​

Choosing a base URL

Surface| Base URL| API key  
---|---|---  
**Comfy Cloud**| `https://cloud.comfy.org` (the default)| Required  
**Comfy API deployment**| `https://<deployment>.run.comfy.app`| Required  
**Your own ComfyUI**| `http://127.0.0.1:8189` (the local proxy)| None by default. Optional static bearer token  
  
The base URL comes from the `COMFY_BASE_URL` environment variable, not a constructor argument:
    
    
    export COMFY_BASE_URL="https://<deployment>.run.comfy.app"  # Comfy API deployment
    export COMFY_BASE_URL="http://127.0.0.1:8189"               # self-hosted proxy
    

It is read each time a client is constructed, must be an `http(s)` URL, and unset or blank means Comfy Cloud. So the client itself is the same everywhere:

Python

TypeScript
    
    
    client = Comfy(api_key="comfyui-...")
    
    
    
    const client = new Comfy({ apiKey: "comfyui-..." });
    

Upgrading from an early build? `Comfy("<url>", "<key>")` is now `Comfy(api_key="<key>")` with `COMFY_BASE_URL` set. `api_key` is keyword-only, so the old positional call raises `TypeError` rather than quietly reading a URL as a key.

### 

​

Comfy Cloud

Works out of the box. Create an [API key](https://docs.comfy.org/development/api-development/getting-an-api-key) and pass it to the client.

API access requires a paid Comfy Cloud subscription. The free tier does not include it. How many jobs you can run at once depends on your tier. See [Concurrent jobs](https://docs.comfy.org/development/deploy/cloud-usage#concurrent-jobs).

### 

​

Comfy API deployment

A workflow you deployed through the [developer platform](https://platform.comfy.org) gets its own endpoint. Point `COMFY_BASE_URL` at it and use your API key, exactly as with Comfy Cloud. Everything in this guide works the same way, except job labels and the job list, which Comfy Cloud does not support yet. A Comfy API deployment can run multiple workflows with the models and custom nodes included in its Build. For each job, `get_workflow()` returns a workflow response with `format: "api"` and the executed graph in its `.graph` property.

### 

​

Your own ComfyUI

The v2 API is served on self-hosted ComfyUI by [comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy), a small open-source service that runs alongside your ComfyUI. Install it, run it, and set `COMFY_BASE_URL="http://127.0.0.1:8189"`:
    
    
    pip install comfy-api-proxy
    comfy-api-proxy
    export COMFY_BASE_URL="http://127.0.0.1:8189"
    

See [API Proxy for Self-Hosted ComfyUI](https://docs.comfy.org/development/comfyui-server/api-proxy) for configuration and authentication details.

## 

​

Retrying a submit: the idempotency key

`submit()` and `run()` send an `Idempotency-Key` with every submission, and the Comfy API v2 contract for that key is **reject-on-duplicate, not record-and-replay**. Read this before you wrap a submit in a retry loop.

  * **Each call mints a fresh key.** Calling `submit()` twice with the same workflow is two submissions, two jobs and two charges. A naive `for attempt in range(3)` around `submit()` is a double-bill, not a retry.
  * **A reused key is rejected, not replayed.** Pass your own `idempotency_key` (`idempotencyKey` in TypeScript) to make a retry idempotent, and the second request with that key fails `422 idempotency_key_reuse` instead of returning the first job. The SDKs raise `IdempotencyKeyReuse`. That is the opposite of what “idempotent retry” usually means, so handle it explicitly.
  * **Recovery is to go and find the job, not to resubmit.** On `IdempotencyKeyReuse` the first attempt may well have created a job. Fetch it with `client.jobs.get(job_id)`. That lookup needs an id you already stored, so it only recovers the case where the submit returned and you persisted the id before the failure. If the connection dropped before the id was recorded there is nothing to look up and no automatic recovery: the examples below re-raise for manual handling rather than resubmitting under a claimed key.
  * **The key is released when the submission definitively failed.** A validation error, an out-of-credits reject or a queue-full reject creates no job and frees the key, so resubmitting under it is fine. After an _ambiguous_ failure (a read timeout, a connection dropped mid-request) the key stays claimed: look for the job rather than resubmitting.
  * **Keys expire after 24 hours** and must be non-empty, printable ASCII and within the length bound. An invalid key raises `ValueError` before any request is made, so an explicit `""` never silently falls back to a minted key.

A retry that is safe to run more than once therefore has to carry two things across attempts: the key, so the server can tell a retry from a new submission, and the job id, so you can find the job a claimed key already created.

Python

TypeScript
    
    
    import uuid
    from comfy_sdk import IdempotencyKeyReuse
    
    # Both values belong in your own store, keyed by whatever the request means to
    # you. `key` is minted once, on the first attempt; `job_id` is filled in as soon
    # as a submit returns.
    state = load_submission_state()  # {"key": ..., "job_id": ...} or {}
    key = state.get("key") or str(uuid.uuid4())
    save_submission_state(key=key)
    
    try:
        job = client.submit(wf, idempotency_key=key)
        save_submission_state(key=key, job_id=job.id)
    except IdempotencyKeyReuse:
        # An earlier attempt under this key already reached submission, so a job
        # may exist. Do not resubmit: go and find it.
        job_id = state.get("job_id")
        if job_id is None:
            raise  # nothing recorded to look up; this needs a human
        job = client.jobs.get(job_id)
    
    
    
    import { IdempotencyKeyReuse } from "@comfyorg/sdk";
    
    // Both values belong in your own store, keyed by whatever the request means to
    // you. `key` is minted once, on the first attempt; `jobId` is filled in as soon
    // as a submit returns.
    const state = await loadSubmissionState(); // { key?, jobId? }
    const key = state.key ?? crypto.randomUUID();
    await saveSubmissionState({ key });
    
    let job;
    try {
      job = await client.submit(wf, { idempotencyKey: key });
      await saveSubmissionState({ key, jobId: job.id });
    } catch (err) {
      // An earlier attempt under this key already reached submission, so a job
      // may exist. Do not resubmit: go and find it.
      if (!(err instanceof IdempotencyKeyReuse) || !state.jobId) throw err;
      job = await client.jobs.get(state.jobId);
    }
    

`client.jobs.get(job_id)` is the SDK’s rehydration path, and it needs an id, which is why recording the id the moment a submit returns is what makes this recoverable at all. See [Comfy API v2](https://docs.comfy.org/api-reference/v2/overview) for the full key contract on `POST /api/v2/jobs`.

Comfy Router’s `Idempotency-Key` behaves **differently**. On Router the key is a replay handle rather than a single-use token: re-sending a queued submit under the same key returns the original request instead of queueing a second one. See [queued idempotency and billing](https://docs.comfy.org/development/comfy-router/queue#idempotency-and-billing) and [Router retry outcomes](https://docs.comfy.org/development/comfy-router/errors#retry-outcomes). The two surfaces share a header name, not a contract.

## 

​

Watching a job run

`job.events()` gives you a live stream of the job’s state: node and step progress, preview frames, and each output the moment it is committed. It reconnects on its own if the connection drops.

Python

TypeScript
    
    
    from comfy_sdk import Progress, Preview, OutputReady, StatusChange
    
    job = client.submit(wf)
    
    for event in job.events():
        match event:
            case Progress() as p:
                print(f"{p.value:.0%} {p.message}")
            case Preview() as pv:
                image = pv.to_pil()
            case OutputReady() as o:
                o.output.to_file(f"partial/{o.output.name}")
            case StatusChange(status="succeeded"):
                break
    
    result = job.result()
    
    
    
    const job = await client.submit(wf);
    
    // The label is required: a bare `break` inside a switch leaves the switch,
    // not the loop.
    eventLoop: for await (const event of job.events()) {
      switch (event.kind) {
        case "progress":
          console.log(event.value);
          break;
        case "outputReady":
          await event.output.toFile(`${event.output.name}`);
          break;
        case "statusChange":
          if (event.status === "succeeded") break eventLoop;
      }
    }
    

`Preview.to_pil()` requires the optional Pillow extra: `pip install "comfy-sdk[pil]"`. `result()` returns the finished job, or raises `JobFailed` with the node-level detail if execution failed. See the SDK README for your language for the full event catalog.

### 

​

`events()` is not `subscribe()`

Three similarly named things exist across the two surfaces, and only one of them is on this page:

Call| Surface| What it yields  
---|---|---  
`job.events()`| Comfy Cloud (this page)| A live SSE stream of one workflow job: `Progress`, `Preview`, `OutputReady`, `StatusChange`. Auto-reconnects, falls back to polling.  
`handle.events()` (TypeScript) / `handle.iter_events()` (Python)| [Comfy Router queued delivery](https://docs.comfy.org/development/comfy-router/queue)| Queue observations for one Router request: status and queue position. It polls the status route; there is no stream and there are no progress or preview events.  
`comfy.models.subscribe(...)`| [Comfy Router queued delivery](https://docs.comfy.org/development/comfy-router/queue)| Not an iterator. Submit, poll and collect in one call, with an `on_queue_update` / `onQueueUpdate` callback, resolving to the result.  
  
There is no `subscribe()` on the Comfy Cloud client, and no `job.subscribe()` anywhere. The Cloud equivalent of `subscribe` is `run()`: submit and wait for a terminal state. The stream is a live feed, not a replayable log. It exists so you can render progress, not so you can rely on it for results. Polling the job is what is authoritative, and `run()`, `wait()`, and `result()` fall back to polling automatically. See [Design Notes](https://docs.comfy.org/development/api-development/sdks-design#poll-first-stream-for-progress) for why.

## 

​

Tracing an output back to its workflow

Outputs carry the id of the job that produced them, so you can start from a file and work backwards without keeping a side table.

Python

TypeScript
    
    
    output = job.outputs[0]
    output.job_id          # the job that produced this file
    
    
    
    const output = job.outputs[0];
    output.jobId; // the job that produced this file
    

The same id is on an asset fetched on its own, so a file you found later still leads back to its job. It is `None` (TypeScript: `undefined`) for an asset you uploaded, which has no producing job. From the job you can ask for the workflow behind it. This works for a job you did not submit in this process, rehydrated by id:

Python

TypeScript
    
    
    wf = job.get_workflow()
    
    if wf.format == "save":
        ...  # the workflow as authored, canvas layout and Note nodes intact
    else:
        ...  # the executed API-format graph
    
    
    
    const wf = await job.getWorkflow();
    
    if (wf.format === "save") {
      // the workflow as authored, canvas layout and Note nodes intact
    } else {
      // the executed API-format graph
    }
    

**Always branch on`format`.** Which shape comes back depends on how the job was submitted, not on anything you control per request:

`format`| What you get| When  
---|---|---  
`save`| The authoring workflow at the version the job ran, with canvas layout and editor-only nodes such as Note| Jobs submitted from the Comfy Cloud editor, which pins a workflow version  
`api`| The executed graph. Editor-only constructs are gone and Get/Set nodes are expanded| Everything else, including every job submitted through these SDKs today  
  
Jobs you submit through the SDK always return `api`, because v2 submission has no version-pinning fields yet. That will change; the discriminator is there so your code does not have to.

## 

​

Label jobs and find them later

A label is a key and a value you attach to a job when you submit it, such as `client: acme` or `project: spring`. Use labels to record which of your clients or projects a job ran for. You can then list the jobs for one client without keeping your own table of job ids. Labels and the job list need the current SDK release, the one named in the version note under Install. Labels work on jobs sent to a Comfy API deployment, so set `COMFY_BASE_URL` to the deployment’s address as shown in Choosing a base URL. Comfy Cloud refuses them for now, and answers the job list with `501` and code `not_implemented`. A self-hosted comfy-api-proxy does not keep them either: its own `metadata` field is a single text string, so it refuses a label map. Its job list ignores label filters, so an SDK list call with labels returns no jobs there, and the same filters over HTTP return every job. The limits:

  * Up to 16 labels on a job.
  * A key is 1 to 40 characters: letters, digits, `_`, `-` and `.`.
  * A value is a string of up to 256 bytes (UTF-8).
  * Labels are set when you submit the job and cannot be changed later.

A submit that breaks a limit fails with `422` and code `metadata_invalid`, and no job is created. The error message names the key that broke the rule, or gives the count when there are more than 16 labels. The SDKs do not check the limits themselves. They raise an error that carries the server’s code and message.

Anyone in your workspace who can see a job can see its labels. Do not put secrets or personal data in them.

Pass `metadata` when you submit. The job carries the labels when you read it back:

Python

TypeScript
    
    
    job = client.submit(wf, metadata={"client": "acme", "project": "spring"})
    job.metadata  # {"client": "acme", "project": "spring"}
    
    
    
    const job = await client.submit(wf, {
      metadata: { client: "acme", project: "spring" },
    });
    job.metadata; // { client: "acme", project: "spring" }
    

A job submitted without labels has an empty `metadata`. To find the jobs for one client, list jobs filtered by label. The list covers only the jobs sent to the deployment at your base URL. Results come newest first, and the SDK fetches the next page for you as you iterate:

Python

TypeScript
    
    
    for job in client.list_jobs(metadata={"client": "acme"}):
        print(job.id, job.status)
    
    
    
    for await (const job of client.listJobs({ metadata: { client: "acme" } })) {
      console.log(job.id, job.status);
    }
    

You can filter on up to 3 labels at once, and a job must match all of them exactly. List items do not include outputs. To get a job’s outputs, read the job by its id with `client.jobs.get(job.id)`.

### 

​

Over HTTP

Send `metadata` in the body of `POST /api/v2/jobs`:
    
    
    curl -X POST "https://<deployment>.run.comfy.app/api/v2/jobs" \
      -H "Authorization: Bearer $COMFY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "workflow": { ... },
        "metadata": { "client": "acme", "project": "spring" }
      }'
    

Filter `GET /api/v2/jobs` with one `metadata[<key>]=<value>` query parameter per label. The `-g` flag stops curl from reading the square brackets as a pattern:
    
    
    curl -g "https://<deployment>.run.comfy.app/api/v2/jobs?metadata[client]=acme" \
      -H "Authorization: Bearer $COMFY_API_KEY"
    

The response holds a page of jobs and, when more pages exist, a `next_cursor`. Pass it back as `cursor`, together with the same `metadata[...]` filters, to get the next page. A cursor sent without its filters returns unfiltered jobs. Use `limit` to set the page size (at most 500).
    
    
    {
      "jobs": [
        {
          "id": "6f1c2b9e-...",
          "status": "succeeded",
          "metadata": { "client": "acme", "project": "spring" }
        }
      ],
      "next_cursor": "eyJ..."
    }
    

More than 3 label filters, or a key that breaks the key rule, fails with `400` and code `invalid_metadata_filter`. See the [Comfy API v2 reference](https://docs.comfy.org/api-reference/v2/overview) for every field on the job and the list.

## 

​

What the SDKs cover today

The first version does one thing properly: run a workflow and get the results back.

  * **Assets.** Create input handles from a file, bytes, a stream, or a URL. Handles are lazy and content addressed, so re-running with the same input does not re-upload it.
  * **Submission.** Submit an API-format graph. Submission is idempotent, and a full queue is retried for you within a bounded budget.
  * **Execution.** Poll with `wait()`, or follow `events()` for live progress.
  * **Outputs.** Write to disk, buffer into memory, fetch a byte range, or get a short-lived download URL. `getDownloadUrl()` hands back a signed URL that anyone can read without an API key, valid for roughly 6 hours. Read [Output URLs and How Long They Last](https://docs.comfy.org/api-reference/v2/overview#output-urls-and-how-long-they-last) before you store one: to keep showing an output later, re-host the bytes or re-mint the URL on demand.
  * **Traceability.** Every output carries the id of the job that produced it, and a job can hand back the workflow behind it.
  * **Deleting assets.** Remove an asset you uploaded, by handle or by id.
  * **Errors.** Typed exceptions such as `JobFailed`, `Unauthorized`, `InsufficientCredits`, and `QueueFull`, rather than raw status codes.
  * **Cancellation.** Jobs can be canceled while running. TypeScript additionally accepts an `AbortSignal` on any call.

Python ships both a synchronous `Comfy` client and an `AsyncComfy` client with the same surface. TypeScript is async only. Not in this version: managing saved workflows, the model library, node introspection, and named workflow parameters. [Design Notes](https://docs.comfy.org/development/api-development/sdks-design#scope-of-the-first-version) explains why the surface starts this small.

## 

​

Reference

The SDK READMEs are the full reference for each language, including auth, assets, errors, and the low-level escape hatches.

## Python SDK

`comfy-sdk` on PyPI. Sync and async clients.

## TypeScript SDK

`@comfyorg/sdk` on npm. Typed, async, with a low-level client.

## Comfy API v2 Reference

The HTTP API underneath both SDKs. Use it directly from any language.

## Design Notes

Why this API exists, how it relates to the existing ComfyUI APIs, and what comes next.

## Comfy Router

The other surface in the same package: `comfy.models.run` against partner models such as Flux, Veo and Gemini.

## 

​

Feedback

Report what is awkward, what you expected to find and did not, and what you had to work around. The `#developer-platform` channel in [our Discord](https://discord.com/invite/comfyorg) is the place for it. If you want a first-party SDK in another language, say so there. Both SDKs sit on the same documented HTTP contract, so any language can talk to the API today, but we would rather know where the demand is.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/api-development/sdks.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/api-development/sdks)

[Run your first workflowPrevious](https://docs.comfy.org/development/api-development/quickstart)[API Proxy for Self-Hosted ComfyUINext](https://docs.comfy.org/development/comfyui-server/api-proxy)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
