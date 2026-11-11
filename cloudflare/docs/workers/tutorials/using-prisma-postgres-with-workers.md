---
url: https://developers.cloudflare.com/workers/tutorials/using-prisma-postgres-with-workers/
title: Set up and use a Prisma Postgres database \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:01:03.009019+00:00
---

# Set up and use a Prisma Postgres database · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/tutorials/using-prisma-postgres-with-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Tutorials](https://developers.cloudflare.com/workers/tutorials/)
  4. /Set up and use a Prisma Postgres database



# Set up and use a Prisma Postgres database

Last updated Nov 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create a new Worker project2\. Set up Prisma ORM in your project 2.1. Initialize Prisma ORM 2.2. Enable Node.js compatibility 2.3. Create a Prisma Postgres database 2.4. Define the data model and create the tables3\. Develop the application4\. Deploy the application to CloudflareNext steps

[Prisma Postgres ↗︎](https://www.prisma.io/postgres) is a managed PostgreSQL database with built-in connection pooling. In this tutorial, you query it from a Worker with [Prisma ORM ↗︎](https://www.prisma.io/docs/orm), which runs inside the Worker with the [`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) compatibility flag.

In this tutorial, you will learn how to:

  * Set up a Cloudflare Workers project with Prisma ORM.
  * Create a Prisma Postgres database from the command line.
  * Define a data model and create its tables in the database.
  * Query the database from Workers.
  * Deploy the Worker to Cloudflare.



## Prerequisites

To follow this guide, ensure you have the following:

  * Node.js `v22.18` or higher installed.
  * An active [Cloudflare account ↗︎](https://dash.cloudflare.com/).
  * A basic familiarity with installing and using command-line interface (CLI) applications.



## 1\. Create a new Worker project

Begin by using [C3](https://developers.cloudflare.com/pages/get-started/c3/) to create a Worker project in the command line:
    
    
    npm create cloudflare@latest prisma-postgres-worker -- --type=hello-world --lang=ts --git=true --deploy=false --agents=false

Then navigate into your project:
    
    
    cd ./prisma-postgres-worker

Your initial `src/index.ts` file currently contains a simple request handler:

src/index.tsts
    
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		return new Response("Hello World!");
    	},
    } satisfies ExportedHandler<Env>;

## 2\. Set up Prisma ORM in your project

In this step, you will add Prisma ORM to the project, create a Prisma Postgres database, and create the tables for your data model.

### 2.1. Initialize Prisma ORM

Run the Prisma CLI in the project directory:

npmyarnpnpm
    
    
    npx prisma@latest orm init --yes --target postgres --authoring psl
    
    
    yarn dlx prisma@latest orm init --yes --target postgres --authoring psl
    
    
    pnpx prisma@latest orm init --yes --target postgres --authoring psl

The command installs `@prisma/orm-postgres` and the Prisma CLI, and creates:

  * `src/prisma/contract.prisma`: the file where you define your data model. It starts with a `User` and a `Post` model.
  * `src/prisma/contract.json` and `src/prisma/contract.d.ts`: emitted from the contract. The Worker imports both, so there is no separate `prisma generate` step.
  * `prisma.config.ts`: tells the Prisma CLI where the contract is and reads the `DATABASE_URL` environment variable from `.env`.



### 2.2. Enable Node.js compatibility

Prisma ORM connects to PostgreSQL through the `pg` driver, which needs the `node:net` and `node:tls` modules. Add the `nodejs_compat` flag to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):
    
    
    {
    	"compatibility_flags": ["nodejs_compat"],
    }
    
    
    compatibility_flags = [ "nodejs_compat" ]

### 2.3. Create a Prisma Postgres database

Create a database and write its connection string to `.env`:

npmyarnpnpm
    
    
    npx create-db@latest --env .env
    
    
    yarn dlx create-db@latest --env .env
    
    
    pnpx create-db@latest --env .env

The command creates a temporary Prisma Postgres database and prints a claim URL. The database is deleted after 24 hours unless you open the claim URL and claim it with a free Prisma account. If you already have a Prisma Postgres database, put its connection string in `.env` instead:

.envtxt
    
    
    DATABASE_URL="postgres://USERNAME:PASSWORD@HOST:5432/postgres?sslmode=require"

Both the Prisma CLI (through `prisma.config.ts`) and `wrangler dev` read this file, so the Worker receives the value as `env.DATABASE_URL` during local development.

### 2.4. Define the data model and create the tables

Replace the contents of `src/prisma/contract.prisma` with the following `User` model:

src/prisma/contract.prismaprisma
    
    
    // use prisma-8
    
    model User {
      id    Int    @id @default(autoincrement())
      email String
      name  String
    }

Emit the contract files from the model, then create the table in the database:
    
    
    npx prisma contract emit
    npx prisma db init

`db init` creates the `User` table and records the contract version in the database. When you change the model later, run `npx prisma contract emit` again, followed by `npx prisma db update` to apply the change during development.

After these steps are complete, Prisma ORM is fully set up and connected to your Prisma Postgres database.

## 3\. Develop the application

Modify the `src/index.ts` file and replace its contents with the following code:

src/index.tsts
    
    
    import postgres from "@prisma/orm-postgres/runtime";
    import { contractFromJson } from "@prisma/orm-postgres/static";
    import type { Contract } from "./prisma/contract.d";
    import contractJson from "./prisma/contract.json" with { type: "json" };
    
    const contract = contractFromJson<Contract>(contractJson);
    
    export default {
    	async fetch(request, env, ctx): Promise<Response> {
    		const path = new URL(request.url).pathname;
    		if (path === "/favicon.ico")
    			return new Response("Resource not found", {
    				status: 404,
    				headers: {
    					"Content-Type": "text/plain",
    				},
    			});
    
    		const db = postgres({ contract, url: env.DATABASE_URL });
    
    		try {
    			const user = await db.orm.public.User.create({
    				email: `Jon${Math.ceil(Math.random() * 1000)}@gmail.com`,
    				name: "Jon Doe",
    			});
    
    			const { userCount } = await db.orm.public.User.aggregate((a) => ({
    				userCount: a.count(),
    			}));
    
    			return new Response(`\
    Created new user: ${user.name} (${user.email}).
    Number of users in the database: ${userCount}.
    		`);
    		} finally {
    			ctx.waitUntil(db.close());
    		}
    	},
    } satisfies ExportedHandler<Env>;

A few things to note about this handler:

  * The database client is created inside `fetch` and closed after the response with `ctx.waitUntil(db.close())`. Workers do not allow a socket opened during one request to be reused by another, so do not share a module-level client across requests.
  * `contract.json` is imported with `with { type: "json" }` and converted once with `contractFromJson`. Wrangler bundles it into the Worker.
  * On PostgreSQL, you reach a model through its schema: `db.orm.public.User`.



Generate the Worker types so that `Env` includes the `DATABASE_URL` variable from `.env`:
    
    
    npx wrangler types

Run the development server:
    
    
    npm run dev

Visit [`http://localhost:8787` ↗︎](http://localhost:8787) to see your app display the following output:
    
    
    Created new user: Jon Doe (Jon453@gmail.com).
    Number of users in the database: 1.

Every time you refresh the page, a new user is created. The number displayed will increment by `1` with each refresh as it returns the total number of users in your database.

## 4\. Deploy the application to Cloudflare

When the application is deployed to Cloudflare, it needs access to the `DATABASE_URL` environment variable that is defined locally in `.env`. You can use the [`npx wrangler secret put`](https://developers.cloudflare.com/workers/configuration/secrets/#adding-secrets-to-your-project) command to upload the `DATABASE_URL` to the deployment environment:
    
    
    npx wrangler secret put DATABASE_URL

When prompted, paste the `DATABASE_URL` value (from `.env`). If you are logged in via the Wrangler CLI, you will see a prompt asking if you'd like to create a new Worker. Confirm by choosing "yes":
    
    
    ✔ There doesn't seem to be a Worker called "prisma-postgres-worker". Do you want to create a new Worker with that name and add secrets to it? … yes

Then execute the following command to deploy your project to Cloudflare Workers:
    
    
    npm run deploy

The `wrangler` CLI will bundle and upload your application.

If you are not already logged in, the `wrangler` CLI will open a browser window prompting you to log in to the Cloudflare dashboard.

Note

If you belong to multiple accounts, select the account where you want to deploy the project.

Once the deployment completes, verify the deployment by visiting the live URL provided in the deployment output, such as `https://{PROJECT_NAME}.workers.dev`. If you encounter any issues, ensure the secrets were added correctly and check the deployment logs for errors.

## Next steps

Congratulations on building and deploying a simple application with Prisma Postgres and Cloudflare Workers!

To enhance your application further:

  * Learn how to [filter, sort, and paginate ↗︎](https://www.prisma.io/docs/orm/fundamentals/reading-data?utm_source=cloudflare&utm_medium=docs&utm_campaign=cloudflare_prisma_postgres_workers_tutorial&utm_content=next_steps_reading_data) with Prisma ORM.
  * Explore the [Prisma Postgres documentation ↗︎](https://www.prisma.io/docs/postgres?utm_source=cloudflare&utm_medium=docs&utm_campaign=cloudflare_prisma_postgres_workers_tutorial&utm_content=next_steps_prisma_postgres).
  * Connect to your database through [Hyperdrive](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/prisma-postgres/) to pool connections closer to your Worker.



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/tutorials/using-prisma-postgres-with-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
