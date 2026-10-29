---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/clickhouse-managed-postgres/
title: ClickHouse Managed Postgres \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.849976+00:00
---

# ClickHouse Managed Postgres · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/clickhouse-managed-postgres/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to PostgreSQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/)

  4. /Database Providers
  5. /ClickHouse Managed Postgres



# ClickHouse Managed Postgres

Connect Hyperdrive to ClickHouse Managed Postgres.

Last updated Oct 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Get your connection details2\. Create a database configuration3\. Use Hyperdrive from your WorkerNext steps

This example connects Hyperdrive to a [ClickHouse Managed Postgres ↗︎](https://clickhouse.com/cloud/postgres) database in ClickHouse Cloud. ClickHouse Managed Postgres is a managed PostgreSQL service with local NVMe storage and built-in ClickHouse integration for analytics.

Note

ClickHouse documents the platform availability and current product status of ClickHouse Managed Postgres. For details, refer to the [ClickHouse Managed Postgres documentation ↗︎](https://clickhouse.com/docs/products/managed-postgres/).

## Prerequisites

Before you begin, you need:

  * An existing ClickHouse Managed Postgres instance.
  * A Workers project. Refer to [Get started](https://developers.cloudflare.com/workers/get-started/guide/) to create one.
  * [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/) version `4.9.0` or later, authenticated with your Cloudflare account.



## 1\. Get your connection details

  1. In the [ClickHouse Cloud console ↗︎](https://console.clickhouse.cloud/), select your Postgres instance and open the **Connect** menu.
  2. Select **Directly** to use the direct PostgreSQL endpoint. Hyperdrive provides [connection pooling](https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/).
  3. Copy the hostname, port, database name, username, and password. Use a database role with the permissions your application needs.
  4. In **Settings** , download the certificate authority (CA) certificate for this instance. Save it locally as `postgres-ca.pem`.



For more information, refer to [ClickHouse Managed Postgres connection details ↗︎](https://clickhouse.com/docs/products/managed-postgres/connection).

Your database must accept connections from Hyperdrive. If you restrict inbound connections by IP address, allow the [Cloudflare IP address ranges](https://developers.cloudflare.com/hyperdrive/configuration/firewall-and-networking-configuration/).

## 2\. Create a database configuration

Use the instance CA to verify the database server with Transport Layer Security (TLS). The CA certificate is specific to your Postgres instance.

  1. Upload the CA certificate to your Cloudflare account:

npmyarnpnpm
         
         npx wrangler cert upload certificate-authority --ca-cert postgres-ca.pem --name clickhouse-postgres-ca
         
         yarn wrangler cert upload certificate-authority --ca-cert postgres-ca.pem --name clickhouse-postgres-ca
         
         pnpm wrangler cert upload certificate-authority --ca-cert postgres-ca.pem --name clickhouse-postgres-ca

  2. Copy the certificate ID from the command output. Create a Hyperdrive configuration using that ID and your database connection details:

npmyarnpnpm
         
         npx wrangler hyperdrive create clickhouse-postgres --origin-host '<HOSTNAME>' --origin-port '<PORT>' --database '<DATABASE_NAME>' --origin-scheme postgres --origin-user '<USERNAME>' --origin-password '<PASSWORD>' --ca-certificate-id '<CA_CERTIFICATE_ID>' --sslmode verify-full --caching-disabled
         
         yarn wrangler hyperdrive create clickhouse-postgres --origin-host '<HOSTNAME>' --origin-port '<PORT>' --database '<DATABASE_NAME>' --origin-scheme postgres --origin-user '<USERNAME>' --origin-password '<PASSWORD>' --ca-certificate-id '<CA_CERTIFICATE_ID>' --sslmode verify-full --caching-disabled
         
         pnpm wrangler hyperdrive create clickhouse-postgres --origin-host '<HOSTNAME>' --origin-port '<PORT>' --database '<DATABASE_NAME>' --origin-scheme postgres --origin-user '<USERNAME>' --origin-password '<PASSWORD>' --ca-certificate-id '<CA_CERTIFICATE_ID>' --sslmode verify-full --caching-disabled

Replace each placeholder with your values. Use the direct endpoint port, which defaults to `5432`. Keep the password and command output private.

  3. Copy the Hyperdrive configuration ID from the output. Use this ID for the Worker binding in the next section.




The `verify-full` mode validates the certificate and database hostname. Hyperdrive checks the connection when you create the configuration. For certificate configuration details, refer to [SSL/TLS certificates](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/).

This example turns off query caching so reads reach Postgres. Connection pooling still applies. For workloads that can tolerate cached results, refer to [Query caching](https://developers.cloudflare.com/hyperdrive/concepts/query-caching/).

## 3\. Use Hyperdrive from your Worker

Install the `node-postgres` driver:

npmyarnpnpmbun
    
    
    npm i pg@>8.16.3
    
    
    yarn add pg@>8.16.3
    
    
    pnpm add pg@>8.16.3
    
    
    bun add pg@>8.16.3

Note

The minimum version of `node-postgres` required for Hyperdrive is `8.16.3`.

If using TypeScript, install the types package:

npmyarnpnpmbun
    
    
    npm i -D @types/pg
    
    
    yarn add -D @types/pg
    
    
    pnpm add -D @types/pg
    
    
    bun add -d @types/pg

Add the required Node.js compatibility flags and Hyperdrive binding to your `wrangler.jsonc` file:
    
    
    {
    	// required for database drivers to function
    	"compatibility_flags": [
    		"nodejs_compat"
    	],
    	// Set this to today's date
    	"compatibility_date": "2026-10-29",
    	"hyperdrive": [
    		{
    			"binding": "HYPERDRIVE",
    			"id": "<your-hyperdrive-id-here>"
    		}
    	]
    }
    
    
    compatibility_flags = [ "nodejs_compat" ]
    # Set this to today's date
    compatibility_date = "2026-10-29"
    
    [[hyperdrive]]
    binding = "HYPERDRIVE"
    id = "<your-hyperdrive-id-here>"

Create a new `Client` instance and pass the Hyperdrive `connectionString`:
    
    
    // filepath: src/index.ts
    import { Client } from "pg";
    
    export default {
    	async fetch(
    		request: Request,
    		env: Env,
    		ctx: ExecutionContext,
    	): Promise<Response> {
    		// Create a new client instance for each request. Hyperdrive maintains the
    		// underlying database connection pool, so creating a new client is fast.
    		const client = new Client({
    			connectionString: env.HYPERDRIVE.connectionString,
    		});
    
    		try {
    			// Connect to the database
    			await client.connect();
    
    			// Perform a simple query
    			const result = await client.query("SELECT * FROM pg_tables");
    
    			return Response.json({
    				success: true,
    				result: result.rows,
    			});
    		} catch (error: any) {
    			console.error("Database error:", error.message);
    
    			return new Response("Internal error occurred", { status: 500 });
    		}
    	},
    };

To test the connection through Hyperdrive, [deploy your Worker](https://developers.cloudflare.com/workers/get-started/guide/) and request its URL. A successful response contains `success: true` and the query results.

## Next steps

  * Configure [local development](https://developers.cloudflare.com/hyperdrive/configuration/local-development/).
  * Review [supported PostgreSQL features](https://developers.cloudflare.com/hyperdrive/reference/supported-databases-and-features/).
  * Diagnose connection errors with [Troubleshoot and debug](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/).



[PreviousSupabase](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/supabase/)[NextTimescale](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/timescale/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-postgres/postgres-database-providers/clickhouse-managed-postgres.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
