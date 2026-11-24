---
url: https://developers.cloudflare.com/containers/faq/
title: Frequently Asked Questions \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:03.198644+00:00
---

# Frequently Asked Questions · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/faq/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Frequently Asked Questions



# Frequently Asked Questions

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow do Container logs work?How are container instance locations selected?How do container updates and rollouts work?How do Workers Builds work with Containers?How does scaling work? Is built-in autoscaling for stateless applications available?Can a Container receive inbound TCP or gRPC traffic?What are cold starts? How fast are they?How do I use an existing container image?Is disk persistent? What happens to my disk when my container sleeps?What happens if I run out of memory?How long can instances run for? What happens when a host server is shut down?How can I pass secrets to my container?Can I run Docker inside a container (Docker-in-Docker)?How do I allow or disallow egress from my container?

## How do Container logs work?

To get logs in the Dashboard, including live tailing of logs, turn on observability in your Wrangler config.

You can turn it on at the Worker level, which applies to containers by default:
    
    
    {
    	"observability": {
    		"enabled": true
    	}
    }
    
    
    [observability]
    enabled = true

You can also configure observability per container:
    
    
    {
    	"containers": [
    		{
    			"class_name": "MyContainer",
    			"image": "./Dockerfile",
    			"observability": {
    				"enabled": true
    			}
    		}
    	]
    }
    
    
    [[containers]]
    class_name = "MyContainer"
    image = "./Dockerfile"
    
      [containers.observability]
      enabled = true

If a container sets `observability` in its container entry, it overrides the top-level `observability` setting for that container.

Logs are subject to the same [limits as Workers Logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/#limits) and are retained for seven days.

Beginning December 1, 2026, Container logs use [Cloudflare Observability pricing](https://developers.cloudflare.com/observability/pricing/).

You can export container logs via [Logpush](https://developers.cloudflare.com/logs/logpush/) to your preferred destination.

## How are container instance locations selected?

With the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy), Cloudflare selects a suitable location when your Durable Object calls `this.ctx.container.start()`. Placement takes into account the Durable Object's jurisdiction, available capacity, and cached images.

While the container is running, requests through its Durable Object reach that same instance. After it stops, a later start may select a different location. For more information, refer to [Placement](https://developers.cloudflare.com/containers/concepts/placement/).

## How do container updates and rollouts work?

On `wrangler deploy`, the Worker goes live first. Container instances update with a gradual rollout by default. Refer to [Rollouts](https://developers.cloudflare.com/containers/configuration/rollouts/) for steps, grace periods, and modes. Refer to [Deploy Containers](https://developers.cloudflare.com/containers/guides/deploy/) to run a deploy.

## How do Workers Builds work with Containers?

On the production branch, Workers Builds should run `wrangler deploy` so images and container instances can update. Non-production Workers Builds defaults to `wrangler versions upload`, which does not update images. Containers Workers implement Durable Objects, so preview URLs are not generated for them. Refer to [Deploy Containers](https://developers.cloudflare.com/containers/guides/deploy/#before-production).

## How does scaling work?

Containers scale by creating or addressing specific instances. For stateless routing across a fixed number of interchangeable instances, choose an instance name at random from a fixed pool.

Refer to [scaling and routing](https://developers.cloudflare.com/containers/configuration/scaling-and-routing/) for details.

### Is built-in autoscaling for stateless applications available?

Not today, though Cloudflare plans to add built-in autoscaling in a future release.

Until then, route to a random instance from a fixed pool for simple stateless routing, and use specific instance names when you need explicit control over container lifecycle.

## Can a Container receive inbound TCP or gRPC traffic?

Yes. Inbound TCP connections to Workers are in public beta. A Spectrum application sends the connection to a Worker's [`connect()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/), which can forward the raw socket to a process running in a Container.

Refer to [Bidirectional gRPC with Workers and Containers](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/) for a complete example.

## What are cold starts? How fast are they?

A cold start is when a container instance is started from a completely stopped state.

If you call `env.MY_CONTAINER.get(id)` with a completely novel ID and launch this instance for the first time, it will result in a cold start.

This will start the container image from its entrypoint for the first time. Depending on what this entrypoint does, it will take a variable amount of time to start.

Container cold starts can often be in the 1-3 second range, but this is dependent on image size and code execution time, among other factors.

## How do I use an existing container image?

Refer to [image management](https://developers.cloudflare.com/containers/guides/image-management/#use-pre-built-container-images).

## Is disk persistent? What happens to my disk when my container sleeps?

All disk is ephemeral by default. When a Container instance goes to sleep, the next time it starts, it uses a fresh disk from the container image.

If you need point-in-time filesystem state, Container applications that use the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy) can create and restore a snapshot. Snapshots are immutable, so later file changes require a new snapshot. For more information, refer to [Snapshots](https://developers.cloudflare.com/containers/guides/snapshots/).

You can also use [FUSE](https://developers.cloudflare.com/containers/examples/r2-fuse-mount/) to persist disk to R2 or other object storage backends. Though you should not expect native SSD-like performance while using FUSE.

## What happens if I run out of memory?

If an out-of-memory (OOM) condition stops an instance that uses the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy), its Durable Object must start it again.

Containers do not use swap memory.

## How long can instances run for? What happens when a host server is shut down?

Cloudflare does not stop a container instance after a fixed maximum runtime. Call [`setInactivityTimeout()`](https://developers.cloudflare.com/containers/api/durable-object-container/#setinactivitytimeout) to stop an inactive container.

Another platform event can stop an active container. For example, a host server restart happens on an irregular cadence. Cloudflare does not guarantee that any container instance will run for a set period.

After a host stop, a new container instance may start on a different server. For cleanup guidance, refer to [Container shutdown](https://developers.cloudflare.com/containers/concepts/architecture/#container-shutdown).

## How can I pass secrets to my container?

You can use [Worker Secrets](https://developers.cloudflare.com/workers/configuration/secrets/) or the [Secrets Store](https://developers.cloudflare.com/secrets-store/integrations/workers/) to define secrets for your Workers.

For implementation details, refer to [Environment variables and secrets](https://developers.cloudflare.com/containers/examples/env-vars-and-secrets/).

## Can I run Docker inside a container (Docker-in-Docker)?

Yes. With the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy), Docker can use bridge networking, iptables, and IP forwarding. Use the `docker:dind` image:

Dockerfiledockerfile
    
    
    FROM docker:dind
    
    # Start dockerd, then run your app
    ENTRYPOINT ["sh", "-c", "dockerd-entrypoint.sh dockerd & exec /path/to/your-app"]

Run the Docker daemon as `root` for this setup.

If your application uses Docker or writes to `/tmp` during startup, wait for the daemon before starting the application. The `docker:dind` entrypoint can mount a new filesystem over `/tmp` during startup. Use an entrypoint script that waits for Docker:

entrypoint.shsh
    
    
    #!/bin/sh
    set -eu
    
    dockerd-entrypoint.sh dockerd &
    
    # Wait for dockerd to be ready
    until docker version >/dev/null 2>&1; do
      sleep 0.2
    done
    
    exec /path/to/your-app

## How do I allow or disallow egress from my container?

Refer to [Handle outbound traffic](https://developers.cloudflare.com/containers/configuration/outbound-traffic/) for how to control outbound traffic and internet access.

[PreviousWrangler Commands ↗︎](https://developers.cloudflare.com/workers/wrangler/commands/containers/)[NextLimits and Instance Types](https://developers.cloudflare.com/containers/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/faq.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
