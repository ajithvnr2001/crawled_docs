---
url: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/
title: Prisma ORM \u00b7 Cloudflare Hyperdrive docs
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:01:02.956346+00:00
---

# Prisma ORM · Cloudflare Hyperdrive docs

> Source: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)
  3. /…

Examples[Connect to PostgreSQL](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/)

  4. /Libraries and Drivers
  5. /Prisma ORM



# Prisma ORM

Last updated Nov 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Install Prisma ORM2\. Configure Prisma ORM 2.1. Define a data model 2.2. Set up environment variables 2.3. Emit the contract and create the tables3\. Connect Prisma ORM to Hyperdrive4\. Deploy your WorkerNext steps

[Prisma ORM ↗︎](https://www.prisma.io/docs/orm) is a Node.js and TypeScript ORM with a focus on type safety and developer experience. This example demonstrates how to use Prisma ORM with PostgreSQL via Cloudflare Hyperdrive in a Workers application.

## Prerequisites

  * A Cloudflare account with Workers access
  * A PostgreSQL database (such as [Prisma Postgres ↗︎](https://www.prisma.io/postgres))
  * A [Hyperdrive configuration to your PostgreSQL database](https://developers.cloudflare.com/hyperdrive/get-started/#3-connect-hyperdrive-to-a-database)
  * An existing [Worker project](https://developers.cloudflare.com/workers/get-started/guide/)



## 1\. Install Prisma ORM

Initialize Prisma ORM in your Worker project:

npmyarnpnpm
    
    
    npx prisma@latest orm init --yes --target postgres --authoring psl --write-env
    
    
    yarn dlx prisma@latest orm init --yes --target postgres --authoring psl --write-env
    
    
    pnpx prisma@latest orm init --yes --target postgres --authoring psl --write-env

The command installs `@prisma/orm-postgres`, which includes the `pg` driver, and the Prisma CLI. It also creates `src/prisma/contract.prisma` for your data model, `prisma.config.ts`, which reads `DATABASE_URL` from `.env`, and a `.env` file with a placeholder `DATABASE_URL`.

Add the required Node.js compatibility flags and Hyperdrive binding to your Wrangler configuration file:
    
    
    {
    	// required for database drivers to function
    	"compatibility_flags": [
    		"nodejs_compat"
    	],
    	// Set this to today's date
    	"compatibility_date": "2026-11-10",
    	"hyperdrive": [
    		{
    			"binding": "HYPERDRIVE",
    			"id": "<your-hyperdrive-id-here>"
    		}
    	]
    }
    
    
    compatibility_flags = [ "nodejs_compat" ]
    # Set this to today's date
    compatibility_date = "2026-11-10"
    
    [[hyperdrive]]
    binding = "HYPERDRIVE"
    id = "<your-hyperdrive-id-here>"

## 2\. Configure Prisma ORM

### 2.1. Define a data model

Define your data model in the `src/prisma/contract.prisma` file:

src/prisma/contract.prismaprisma
    
    
    // use prisma-8
    
    model User {
      id        Int      @id @default(autoincrement())
      name      String
      email     String   @unique
      createdAt DateTime @default(now()) @onCreate(now())
    }

### 2.2. Set up environment variables

Replace the placeholder `DATABASE_URL` in the `.env` file with your database connection string. The Prisma CLI uses it to create and update tables, connecting to the database directly rather than through Hyperdrive:

.envtxt
    
    
    DATABASE_URL="postgres://user:password@host:port/database"

### 2.3. Emit the contract and create the tables

Emit the contract files that the Worker imports, then create the tables in your database:
    
    
    npx prisma contract emit
    npx prisma db init

`contract emit` writes `src/prisma/contract.json` and `src/prisma/contract.d.ts` next to your contract. Run it again whenever you change the model, followed by `npx prisma db update` to apply the change to the database.

## 3\. Connect Prisma ORM to Hyperdrive

Use your Hyperdrive configuration when using Prisma ORM. Update your `src/index.ts` file:

src/index.tsts
    
    
    import postgres from "@prisma/orm-postgres/runtime";
    import { contractFromJson } from "@prisma/orm-postgres/static";
    import type { Contract } from "./prisma/contract.d";
    import contractJson from "./prisma/contract.json" with { type: "json" };
    
    const contract = contractFromJson<Contract>(contractJson);
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		// Create a Prisma ORM client with the Hyperdrive connection string
    		const db = postgres({ contract, url: env.HYPERDRIVE.connectionString });
    
    		try {
    			// Sample query to create and fetch users
    			const user = await db.orm.public.User.create({
    				name: "John Doe",
    				email: `john.doe.${Date.now()}@example.com`,
    			});
    
    			const allUsers = await db.orm.public.User.all();
    
    			return Response.json({
    				newUser: user,
    				allUsers: allUsers,
    			});
    		} finally {
    			// Close the connection after the response is sent
    			ctx.waitUntil(db.close());
    		}
    	},
    } satisfies ExportedHandler<Env>;

Run `npx wrangler types` so that the generated `Env` type includes the `HYPERDRIVE` binding.

Note

The client is created inside `fetch` with the Hyperdrive connection string and closed after the response with `ctx.waitUntil(db.close())`. Workers do not allow a socket opened during one request to be reused by another, so do not share a module-level client across requests. Hyperdrive pools the connections at the network level, so no Prisma-specific pooling is needed.

To run the Worker locally with `wrangler dev`, set a [`localConnectionString`](https://developers.cloudflare.com/hyperdrive/configuration/local-development/) for the binding so that the Worker connects directly to your database.

## 4\. Deploy your Worker

Deploy your Worker:
    
    
    npx wrangler deploy

## Next steps

  * Learn more about [How Hyperdrive Works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/).
  * Refer to the [troubleshooting guide](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/) to debug common issues.
  * Understand more about other [storage options](https://developers.cloudflare.com/workers/platform/storage-options/) available to Cloudflare Workers.



[PreviousDrizzle ORM](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/)[NextOverview](https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
