---
url: https://developers.cloudflare.com/containers/configuration/scaling-and-routing/
title: Scaling and Routing \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:48.319991+00:00
---

# Scaling and Routing · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/configuration/scaling-and-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Configuration
  4. /Scaling and Routing



# Scaling and Routing

Last updated Nov 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewScale container instances with explicit names Route across a fixed pool of instances

## Scale container instances with explicit names

Each container instance belongs to one Durable Object. To run more container instances, address more Durable Objects by name with [`getByName()`](https://developers.cloudflare.com/durable-objects/api/namespace/#getbyname). Getting a Durable Object does not start its container. The container starts when the Durable Object calls [`ctx.container.start()`](https://developers.cloudflare.com/containers/api/durable-object-container/#start).
    
    
    // Get two Durable Objects. Each one starts its own container instance.
    const containerOne = env.MY_CONTAINER.getByName(nameOne);
    const containerTwo = env.MY_CONTAINER.getByName(nameTwo);
    
    // The Durable Object starts its container when it handles a request.
    const response = await containerOne.fetch(request);

Each instance runs until the Durable Object stops it, or until the [inactivity timeout](https://developers.cloudflare.com/containers/api/durable-object-container/#setinactivitytimeout) that the Durable Object sets elapses. Without a timeout, Cloudflare stops the container shortly after the Durable Object becomes inactive.

This behavior is very useful when you want explicit control over the lifecycle of container instances. For instance, you may want to spin up a container backend instance for a specific user, or you may briefly run a code sandbox to isolate AI-generated code, or you may want to run a short-lived batch job.

### Route across a fixed pool of instances

To run multiple instances of a container and route requests between them, choose a name at random from a fixed pool:
    
    
    const INSTANCE_COUNT = 3;
    
    export default {
    	async fetch(request, env) {
    		const index = Math.floor(Math.random() * INSTANCE_COUNT);
    		return env.BACKEND.getByName(`instance-${index}`).fetch(request);
    	},
    };
    
    
    const INSTANCE_COUNT = 3;
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const index = Math.floor(Math.random() * INSTANCE_COUNT);
    		return env.BACKEND.getByName(`instance-${index}`).fetch(request);
    	},
    } satisfies ExportedHandler<Env>;

Random selection from a fixed pool means:

  * You set a fixed number of instances to route to.
  * Each request goes to a random instance, regardless of location.



For the Durable Object that starts the container, waits for its port, and forwards the request, refer to [Stateless instances](https://developers.cloudflare.com/containers/examples/stateless/).

[PreviousEnvironment Variables](https://developers.cloudflare.com/containers/configuration/environment-variables/)[NextRollouts](https://developers.cloudflare.com/containers/configuration/rollouts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/configuration/scaling-and-routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
