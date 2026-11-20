---
url: https://developers.cloudflare.com/spectrum/how-to/route-tcp-traffic-to-a-worker/
title: Route TCP traffic to a Worker \u00b7 Cloudflare Spectrum docs
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.872701+00:00
---

# Route TCP traffic to a Worker · Cloudflare Spectrum docs

> Source: https://developers.cloudflare.com/spectrum/how-to/route-tcp-traffic-to-a-worker/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Spectrum](https://developers.cloudflare.com/spectrum/)
  3. /How to
  4. /Route TCP traffic to a Worker



# Route TCP traffic to a Worker

Last updated Nov 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCreate the Spectrum applicationConfiguration constraintsVerify the connectionTerminate TLS with Spectrum Enterprise

You can use a Cloudflare Worker as the origin of a Spectrum TCP application. Spectrum accepts the public TCP connection and invokes the Worker's [`connect()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/) with a bidirectional socket.

Public beta

Spectrum applications with Worker origins are in public beta.

Worker origins support use cases such as:

  * Routing bidirectional protocols, including gRPC, to a [Cloudflare Container](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/).
  * Exposing existing TCP applications in Containers without rewriting them as HTTP services.
  * Running MQTT, multiplayer game, and custom binary protocol servers in Containers.
  * Receiving device, telemetry, or syslog data over TCP and sending it to Cloudflare storage or queues.
  * Implementing lightweight TCP services directly in Workers.



## Prerequisites

Before creating the Spectrum application:

  * Add a domain to Cloudflare and ensure Cloudflare is authoritative for its DNS.
  * Use a Pro or Business zone, or a zone with Spectrum Enterprise enabled. Free zones are not supported. Spectrum Enterprise access is separate from a zone's Enterprise plan.
  * In the same account as the zone, deploy a Worker that exports a [`connect()` handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/).
  * For API and CLI configuration, find the Worker's immutable 32-character tag. The tag is different from the Worker name.



Without Spectrum Enterprise, Pro and Business zones support one Worker-origin application per zone, on one TCP port. This application is in addition to existing plan-supported applications, such as SSH or Minecraft. Refer to [Protocols per plan](https://developers.cloudflare.com/spectrum/protocols-per-plan/) for availability.

Review your Spectrum subscription charges and [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/) before deploying. Workers usage is billed separately from Spectrum.

The setup in this guide passes TCP traffic through without terminating TLS. Requests without Spectrum Enterprise must omit the `tls` field. To encrypt the connection, terminate TLS in the service behind the Worker, or use Spectrum Enterprise TLS termination.

STARTTLS

Workers cannot upgrade inbound Spectrum sockets with `socket.startTls()`, including when `tls` is `off`. For STARTTLS protocols, proxy the connection to a backend that handles the TLS upgrade. Refer to the [connect handler TLS documentation](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/#tls).

## Create the Spectrum application

Choose the dashboard, Cloudflare CLI, or API procedure.

The dashboard steps depend on whether the zone has Spectrum Enterprise.

**Pro or Business zone without Spectrum Enterprise**

  1. In the Cloudflare dashboard, go to **Spectrum**.

[ Go to **Spectrum** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/spectrum)
  2. Select **Create an Application**.

  3. Under **Application Configuration** , select **Workers (tcp)** as the **Application Type**. This option is unavailable if the zone already has a Worker-origin application.

  4. In **Subdomain** , enter the subdomain that clients will connect to. The dashboard adds your zone name after it.

  5. In **Edge Port** , enter a single TCP port.

  6. In **Origin Worker** , select the Worker that will receive the connections. The list shows deployed Workers that export a `connect()` handler.

  7. Select **Add Application**.




These applications have no TLS or advanced options. Spectrum passes the TCP payload to the Worker without terminating TLS.

**Zone with Spectrum Enterprise**

  1. In the Cloudflare dashboard, go to **Spectrum**.

[ Go to **Spectrum** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/spectrum)
  2. Select **Create an Application**.

  3. Under **Application Configuration** , select **TCP** as the **Application Type**.

  4. In **Subdomain** , enter the subdomain that clients will connect to. The dashboard adds your zone name after it.

  5. In **Edge Port** , enter a single TCP port.

  6. Under **Origin Configuration** , select **Worker** as the **Origin type**.

  7. In **Origin Worker** , select the Worker that will receive the connections. The list shows deployed Workers that export a `connect()` handler.

  8. Leave **Edge TLS Termination** turned off to pass the TCP payload to the Worker without terminating TLS.

  9. Select **Add Application**.




  1. To find the Worker tag, search for the deployed Worker:

npmyarnpnpm
         
         npx cf@latest workers scripts search --name <WORKER_NAME>
         
         yarn dlx cf@latest workers scripts search --name <WORKER_NAME>
         
         pnpx cf@latest workers scripts search --name <WORKER_NAME>

Copy the Worker ID, also called the Worker tag, from the result.

  2. Create the Spectrum application:

npmyarnpnpm
         
         npx cf@latest spectrum apps create --zone example.com --body '{"dns":{"type":"CNAME","name":"tcp.example.com"},"protocol":"tcp/50051","traffic_type":"worker","origin_worker_id":"<WORKER_TAG>"}'
         
         yarn dlx cf@latest spectrum apps create --zone example.com --body '{"dns":{"type":"CNAME","name":"tcp.example.com"},"protocol":"tcp/50051","traffic_type":"worker","origin_worker_id":"<WORKER_TAG>"}'
         
         pnpx cf@latest spectrum apps create --zone example.com --body '{"dns":{"type":"CNAME","name":"tcp.example.com"},"protocol":"tcp/50051","traffic_type":"worker","origin_worker_id":"<WORKER_TAG>"}'

Replace the zone, hostname, port, and Worker tag with your values. The explicit `--body` sends only the fields supported without Spectrum Enterprise. Additional CLI defaults, such as `tls` or `proxy_protocol`, require Spectrum Enterprise.




  1. Find the Worker tag with the [List Workers endpoint](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/list/):

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Workers Tail Read`
     * `Workers Scripts Write`
     * `Workers Scripts Read`
     * `Workers Admin`
     * `Workers Editor`
     * `Workers Content Read-Only`
     * `Workers Metadata Read-Only`
     * `Individual Workers Admin`
     * `Individual Workers Editor`
     * `Individual Workers Content Read-Only`
     * `Individual Workers Metadata Read-Only`
List Worker Scriptsbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/scripts" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

In the response, find the Worker by its `id` and copy its `tag`.

  2. Create the Spectrum application:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Zone Settings Write`
Create Spectrum application using a name for the originbash
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/spectrum/apps" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"dns": {
    				"type": "CNAME",
    				"name": "tcp.example.com"
    		},
    		"protocol": "tcp/50051",
    		"traffic_type": "worker",
    		"origin_worker_id": "<WORKER_TAG>"
    	}'




## Configuration constraints

Spectrum applications with a Worker origin have the following constraints:

  * This TCP beta uses a single port per application. Port ranges are not supported.
  * `traffic_type` must be `worker`.
  * `origin_worker_id` must contain the target Worker's tag, not its name.
  * On Pro and Business zones without Spectrum Enterprise, omit `tls`. Spectrum does not terminate TLS for these applications.
  * With Spectrum Enterprise, `tls` can be `off` or `flexible`.
  * Do not set `origin_direct`, `origin_dns`, `origin_port`, `virtual_network_id`, Proxy Protocol, or Argo Smart Routing.



Refer to [Configuration options](https://developers.cloudflare.com/spectrum/reference/configuration-options/#worker-origin) for details.

## Verify the connection

To test the plaintext [echo handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/connect/#syntax), run:
    
    
    nc tcp.example.com 50051

Enter a message and confirm the Worker echoes it. If your service terminates TLS behind the Worker, use that service's TLS client instead.

The Spectrum application sends the connection to the Worker's `connect()` handler. Review the Worker's [real-time logs](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/) to confirm the handler ran.

## Terminate TLS with Spectrum Enterprise

Spectrum Enterprise applications can use `tls: "flexible"` to terminate TLS at Cloudflare. Spectrum sends the decrypted TCP payload to the Worker. This mode requires an active [advanced certificate](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/) or [custom certificate](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/) covering the Spectrum hostname. [Universal SSL is not supported](https://developers.cloudflare.com/spectrum/reference/limitations/#universal-ssl).

In the dashboard, turn on **Edge TLS termination** and select **Flexible** for **TLS mode**. For API or CLI configuration, add `"tls":"flexible"` to the request body. Do not include this field unless Spectrum Enterprise is enabled.

To test the echo handler with Spectrum TLS termination, run:
    
    
    openssl s_client -connect tcp.example.com:50051 -servername tcp.example.com -quiet

For an end-to-end bidirectional gRPC example, refer to [Bidirectional gRPC with Workers and Containers](https://developers.cloudflare.com/containers/examples/bidirectional-grpc/).

[PreviousGet started](https://developers.cloudflare.com/spectrum/get-started/)[NextEnable Proxy protocol](https://developers.cloudflare.com/spectrum/how-to/enable-proxy-protocol/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/spectrum/how-to/route-tcp-traffic-to-a-worker.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
