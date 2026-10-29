---
url: https://docs.copilotkit.ai/google-adk/generative-ui/components/catalogs/
title: Catalogs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:49.236324+00:00
---

# Catalogs

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/components/catalogs/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

[Components and surfaces](https://docs.copilotkit.ai/google-adk/generative-ui/components)

[Surfaces](https://docs.copilotkit.ai/google-adk/generative-ui/components/surfaces)[Catalogs](https://docs.copilotkit.ai/google-adk/generative-ui/components/catalogs)[Standard catalog](https://docs.copilotkit.ai/google-adk/generative-ui/components/standard-catalog)[State and actions](https://docs.copilotkit.ai/google-adk/generative-ui/components/state-and-actions)[Theming](https://docs.copilotkit.ai/google-adk/generative-ui/components/theming)[Transports](https://docs.copilotkit.ai/google-adk/generative-ui/components/transports)[Markdown mode](https://docs.copilotkit.ai/google-adk/generative-ui/components/markdown-mode)[Adopt from A2UI](https://docs.copilotkit.ai/google-adk/generative-ui/components/from-a2ui)

[A2UI](https://docs.copilotkit.ai/google-adk/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/google-adk/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/google-adk/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/google-adk/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Catalogs

Generative UIDeclarativeComponents and surfaces

# Catalogs

Declare the components the agent can render, with typed props, in one catalog.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

The agent cannot render a component it does not know about. It also needs to know the props of each one, or it guesses, and a guessed price or a wrong prop breaks the page.

A **catalog** lists the components that the agent can use. For each component it holds the React component, a description, and a schema of its props. The agent gets the descriptions and the schemas. Your app gets typed props.

## Create a catalog#

Declare the catalog once, at module level, with `createGenerativeUI`:

app/catalog.tsx
    
    
    import { z } from "zod";
    import {
      createGenerativeUI,
      type GenerativeUIComponentProps,
    } from "@copilotkit/react-core/v2/generative-ui";
    
    function ProductGrid({ title, children }: GenerativeUIComponentProps<typeof shopUI, "ProductGrid">) {
      return (
        <section>
          {title ? <h3>{title}</h3> : null}
          <div className="grid grid-cols-2 gap-4">{children}</div>
        </section>
      );
    }
    
    function ProductCard({ name, price, imageUrl }: GenerativeUIComponentProps<typeof shopUI, "ProductCard">) {
      return (
        <article>
          <img src={imageUrl} alt={name} />
          <h4>{name}</h4>
          <p>${price}</p>
        </article>
      );
    }
    
    export const shopUI = createGenerativeUI({
      id: "acme/shop@1",
      components: {
        ProductGrid: {
          component: ProductGrid,
          description: "A grid of products. Put the ids of ProductCard components in children.",
          props: z.object({ title: z.string().optional() }),
          slots: { children: "multiple" },
        },
        ProductCard: {
          component: ProductCard,
          description: "One product. Copy every value from a product of a tool result.",
          props: z.object({ name: z.string(), price: z.number(), imageUrl: z.string() }),
        },
      },
    });

Then give it to the provider:
    
    
    <CopilotKitProvider runtimeUrl="/api/copilotkit" generativeUI={{ ui: shopUI }}>

The `id` names the catalog. Use a versioned id, for example `acme/shop@1`.

## What a component can declare#

  * `component`: the React component that renders.
  * `description`: what the component is and when to use it. The agent reads it, so be specific.
  * `props`: the schema of the props that the agent sets.
  * `slots`: props that hold child components. `"single"` takes one child, and `"multiple"` takes a list.
  * A child reference inside the props schema: mark a prop with `child()` or `childList()` from `@copilotkit/react-core/v2/generative-ui`, anywhere in the schema, for example `tabs: z.array(z.object({ title: z.string(), child: child() }))`. The engine renders the referenced components and your component receives them as React nodes in place of the ids. This is how A2UI 1.0 marks references (`ComponentId`, `ChildList`); `slots` stays for the plain top-level case.
  * `events`, `bind`, and `writable`: actions, app state, and inputs. See [Connect app state and actions](https://docs.copilotkit.ai/google-adk/generative-ui/components/state-and-actions).



Next to `id` and `component`, every component the agent writes may carry the A2UI 1.0 envelope: `catalogId` (must be the id of your UI), `metadata` (`{ "extensions": { ... } }`, kept for your own tooling) and `accessibility` (`label`, `description`, `live`, `hidden`; `label`, `description` and `hidden` may be bindings or function values). The engine resolves `accessibility` and keeps all three out of your props. `hidden` and `live` apply to every component: the engine wraps the component in an element with `aria-hidden` and `aria-live`. A `label` or a `description` needs an element with a role, so the standard components set them on their root or on their control. In your own component, call `useGenerativeUIAccessibility()` and spread the result on the root element. A component that must not be wrapped (a table row or cell) declares `accessibility: "self"` and applies the attributes itself.

## Type your components#

`GenerativeUIComponentProps<typeof ui, "Name">` gives a component the exact props that the renderer passes. It reads them from the schema, so the component and the catalog cannot drift apart:
    
    
    function ProductCard(props: GenerativeUIComponentProps<typeof shopUI, "ProductCard">) {
      props.price; // number
      props.color; // type error: not a prop of ProductCard
    }

## Pick a schema library#

`props` takes any [Standard Schema](https://standardschema.dev) of an object. The agent gets the props as JSON Schema, so the schema must be able to give one:

zodValibot
    
    
    import { z } from "zod";
    
    props: z.object({ name: z.string(), price: z.number() }),
    
    
    import * as v from "valibot";
    import { toStandardJsonSchema } from "@valibot/to-json-schema";
    
    props: toStandardJsonSchema(v.object({ name: v.string(), price: v.number() })),

These work: zod 3, zod 4.2 or later, ArkType, and Valibot with `@valibot/to-json-schema`. The schema must validate synchronously, because props are checked while a surface renders.

## Combine catalogs#

`extends` merges other catalogs into yours. The result has the types of every component:
    
    
    import { createGenerativeUI, standardUI } from "@copilotkit/react-core/v2/generative-ui";
    
    export const appUI = createGenerativeUI({
      id: "acme/app@1",
      extends: [standardUI, cartUI],
      components: { Hero: { component: Hero, props: z.object({ title: z.string() }) } },
    });

A name can come from one catalog only. Two components named `Card` throw an error when the app loads. To replace a standard component, use [overrides](https://docs.copilotkit.ai/google-adk/generative-ui/components/standard-catalog#replace-a-component).

## Export the catalog for other A2UI tools#

`exportA2UICatalog(ui)` writes your UI as an A2UI 1.0 catalog definition (the `catalog_definition.json` shape), for a validator, another renderer or a prompt builder:
    
    
    import { exportA2UICatalog } from "@copilotkit/react-core/v2/generative-ui";
    
    const catalog = exportA2UICatalog(appUI, { title: "Acme app" });
    fs.writeFileSync("acme-catalog.json", JSON.stringify(catalog, null, 2));

Every component is an entry with `component` as a `const`, its model-set props, its events as `Action` references and its slots as `ComponentId` or `ChildList` references. A prop takes its literal schema, a `DataBinding` or a `FunctionCall`, because the renderer resolves dynamic values in any prop. Every function, built-in or declared, states `returnType` and `allowedCallers`; `calc` and `series` are listed like the others, so a reader without them knows what it cannot run.

## Positional parameter order#

A2UI Express maps positional arguments using the order of properties in the catalog's JSON Schema. Its [schema-driven key mapping specification](https://a2ui.org/specification/proposals/express/a2ui_express/#schema-driven-key-mapping) defines that behavior. The choice of which parameters come first belongs to the catalog author.

Declare `parameterOrder` to put a component's main content, children or actions first, across `props`, `slots` and `events`:
    
    
    const ui = createGenerativeUI({
      id: "acme/panel@1",
      components: {
        Panel: {
          component: Panel,
          props: z.object({ title: z.string(), color: z.string().optional() }),
          slots: { children: "multiple" },
          parameterOrder: ["title", "children"],
        },
      },
    });

`exportA2UICatalog(ui)` emits `Panel.properties` in the order `component`, `title`, `children`, `color`. Express ignores the structural `component` discriminator, so the first positional argument is the title. `parameterOrder` is CopilotKit authoring/manifest metadata, **not an A2UI JSON Schema keyword** : the portable export applies it to the actual JSON property order.

Names must be unique declared props, slots or events. An ordered component cannot declare canonical integer-index names (`"0"` through `"4294967294"`): JavaScript sorts those keys numerically before other keys regardless of the requested order. Unlisted names follow in their existing declaration order: props, then slots, then events. Bound props and matched events are omitted from the model-facing signature. Catalogs without `parameterOrder` retain their existing export order. `extends`, `omit` and React-component `overrides` preserve the declared convention.

Treat positional order as an API contract. Changing it can change the meaning of existing Express programs; named arguments keep their meaning. Keep short prefixes stable and use named arguments for optional styling. Preserve property order when serializing or transforming a catalog for Express.

## What the agent sees#

The agent gets each component with its description and the props that it can set. It does not see:

  * Props that come from app state (`bind`).
  * Events that your own code handles.



To see this list, open the **Catalog** tab of the Generative UI pane in Inspector. It groups the components by the catalog that declared them, so you can see what `extends` added.

Next: start from the [standard catalog](https://docs.copilotkit.ai/google-adk/generative-ui/components/standard-catalog), then add your own components on top.

### On this page

What is this?Create a catalogWhat a component can declareType your componentsPick a schema libraryCombine catalogsExport the catalog for other A2UI toolsPositional parameter orderWhat the agent sees
