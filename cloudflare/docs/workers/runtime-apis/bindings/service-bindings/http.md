---
url: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/
title: Service bindings - HTTP \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:11.347227+00:00
---

# Service bindings - HTTP · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)[Bindings (env)](https://developers.cloudflare.com/workers/runtime-apis/bindings/)

  4. /[Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)
  5. /HTTP



# HTTP

Last updated Nov 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHandle canceled requests Read or forward the response body Choose when work should stop Stop work when the client disconnects Find out why a request was canceled

Worker A that declares a Service binding to Worker B can forward a [`Request`](https://developers.cloudflare.com/workers/runtime-apis/request/) object to Worker B, by calling the `fetch()` method that is exposed on the binding object.

For example, consider the following Worker that implements a [`fetch()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/):
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "worker_b",
    	"main": "./src/workerB.js",
    	"upload_source_maps": true
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "worker_b"
    main = "./src/workerB.js"
    upload_source_maps = true
    
    
    export default {
      async fetch(request, env, ctx) {
        return new Response("Hello World!");
      }
    }

The following Worker declares a binding to the Worker above:
    
    
    {
    	"$schema": "./node_modules/wrangler/config-schema.json",
    	"name": "worker_a",
    	"main": "./src/workerA.js",
    	"upload_source_maps": true,
    	"services": [
    		{
    			"binding": "WORKER_B",
    			"service": "worker_b"
    		}
    	]
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "worker_a"
    main = "./src/workerA.js"
    upload_source_maps = true
    
    [[services]]
    binding = "WORKER_B"
    service = "worker_b"

And then can forward a request to it:
    
    
    export default {
    	async fetch(request, env) {
    		return await env.WORKER_B.fetch(request);
    	},
    };

Note

If you construct a new request manually, rather than forwarding an existing one, ensure that you provide a valid and fully-qualified URL with a hostname. For example:
    
    
    export default {
      async fetch(request, env) {
        // provide a valid URL
        let newRequest = new Request("https://valid-url.com", { method: "GET" });
        let response = await env.WORKER_B.fetch(newRequest);
        return response;
      }
    };

## Handle canceled requests

Cancellation can pass from a client through one Worker to another. This applies to both HTTP and RPC service bindings. Refer to [Request cancellation](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/#request-cancellation) for an explanation.

Both Workers can report [Client Disconnected](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/#invocation-statuses) for the same request. This can also happen if the calling Worker aborts the call or cancels the response body. The status alone does not tell you which Worker canceled first or why.

### Read or forward the response body

`await env.WORKER_B.fetch(request)` waits for response headers. The body may still be arriving when it returns.

Handle the body based on what your code needs:

  * **Send the response to your client:** Return the `Response`, as in the forwarding example.
  * **Read the response in your Worker:** Await the body reader, such as `await response.json()` for a JSON response.
  * **Discard the response body:** Run `await response.body?.cancel()` to release resources.



A recorded HTTP `200` does not mean the whole body arrived. Check whether the body finished as well as the HTTP status.

### Choose when work should stop

Follow [Choose when work should stop](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/#choose-when-work-should-stop) for guidance on request work, short background tasks, and jobs that must finish.

### Stop work when the client disconnects

To cancel an operation when the client disconnects, pass [`request.signal`](https://developers.cloudflare.com/workers/runtime-apis/request/#properties) to an API that accepts an `AbortSignal`. Check the [`enable_request_signal` compatibility setting](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests) first. If you forward the incoming `Request`, also check [`request_signal_passthrough`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#passthrough-abortsignal-of-incoming-request-to-subrequests).

For work that should continue after a disconnect, do not use that disconnect's abort signal. `waitUntil()` will not restart work canceled by a signal. Even without an abort signal, the runtime can still [stop work when the request ends](https://developers.cloudflare.com/workers/platform/limits/#duration).

### Find out why a request was canceled

Check both Workers for the same request:

  1. Log the same request ID in both Workers. If you create your own ID, pass it in a request header when calling the other Worker. Also log when the call starts, when response headers arrive, and when the body finishes or fails.
  2. Start [real-time logs](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/) for both Workers before testing. For a Pages caller, open [Pages Functions logs](https://developers.cloudflare.com/pages/functions/debugging-and-logging/) too. Note which deployments or versions you are testing.
  3. Send a request and let it finish. Then cancel a second request before it finishes, for example by closing the browser tab. Save the JSON logs from both tests.
  4. Match the requests by ID and UTC time. Compare `outcome`, HTTP status, and `exceptions`. Check your code for timeouts and `AbortController` calls. Check whether slow work in the called Worker makes the client give up.



Matching request IDs or cancellation counts do not tell you which Worker canceled first. If a log entry is missing, check logging settings, filters, sampling, and retention before assuming the request never arrived.

[PreviousOverview](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)[NextRPC (WorkerEntrypoint)](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/bindings/service-bindings/http.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
