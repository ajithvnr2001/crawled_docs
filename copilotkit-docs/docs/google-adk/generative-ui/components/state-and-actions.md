---
url: https://docs.copilotkit.ai/google-adk/generative-ui/components/state-and-actions/
title: State and actions
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:49.310199+00:00
---

# State and actions

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/components/state-and-actions/

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

State and actions

Generative UIDeclarativeComponents and surfaces

# State and actions

Show live app data in generated UI, run your code when users click, and keep what they type.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

You want a product card that the agent rendered to act like the rest of your app. It must show how many of the product are in the cart, add to the cart when the user clicks, and keep what the user types into a form.

Three tools connect generated UI to your app:

  * **App state** fills props with live values from your app.
  * **Functions** run your code when a component calls an event.
  * **Writable props** keep what the user types.



## Show live app state#

The agent does not know how many items are in the cart, and it must not guess. Declare the state in the catalog, and the library fills the prop:

app/catalog.tsx
    
    
    const cartSchema = z.object({
      items: z.array(z.object({ productId: z.string(), quantity: z.number() })),
    });
    
    export const shopUI = createGenerativeUI({
      id: "acme/shop@1",
      state: { cart: cartSchema },
      components: {
        ProductCard: {
          component: ProductCard,
          props: z.object({ productId: z.string(), name: z.string(), inCart: z.number() }),
          bind: {
            inCart: (state, { productId }) =>
              state.cart.items.find((item) => item.productId === productId)?.quantity ?? 0,
          },
        },
      },
    });

Then give the state its value from your app:
    
    
    import { useGenerativeUIState } from "@copilotkit/react-core/v2/generative-ui";
    
    function CartState({ cart }: { cart: Cart }) {
      useGenerativeUIState(shopUI, "cart", { items: cart.items });
      return null;
    }

How props get their values:

  * A prop with the name of a state key reads that key. A prop named `cart` gets `state.cart`.
  * `bind` gives a prop a selector. The selector gets the state and the props that the agent set.
  * The agent never sets a bound prop and does not see it.



The agent does not see the state either. To let it answer "what is in my cart?", also give it the data with [`useAgentContext`](https://docs.copilotkit.ai/reference/hooks/useAgentContext).

## Run your code on a click#

"Add to cart" must add to the cart, with no message to the agent. Declare a function, give the component an event with a matching name, and mount a handler:

app/catalog.tsx
    
    
    export const shopUI = createGenerativeUI({
      id: "acme/shop@1",
      functions: {
        addToCart: {
          description: "Add a product to the cart",
          parameters: z.object({ productId: z.string(), quantity: z.number().default(1) }),
        },
      },
      components: {
        ProductCard: {
          component: ProductCard,
          props: z.object({ productId: z.string(), name: z.string() }),
          events: { onAddToCart: {} },
        },
      },
    });
    
    
    import { useGenerativeUIFunction } from "@copilotkit/react-core/v2/generative-ui";
    
    function CartActions({ cart }: { cart: Cart }) {
      useGenerativeUIFunction(shopUI, "addToCart", ({ productId, quantity }) => {
        cart.addItem(productId, quantity);
        return { added: productId };
      });
      return null;
    }

In the component, the event is a typed prop. It gives back a result, so you can show progress and errors:
    
    
    import { useState } from "react";
    import type { GenerativeUIComponentProps } from "@copilotkit/react-core/v2/generative-ui";
    
    function ProductCard({ productId, name, onAddToCart }: GenerativeUIComponentProps<typeof shopUI, "ProductCard">) {
      const [error, setError] = useState<string>();
      return (
        <article>
          <h4>{name}</h4>
          <button
            onClick={async () => {
              const result = await onAddToCart?.({ productId });
              if (result && !result.ok) setError(result.error.message);
            }}
          >
            Add to cart
          </button>
          {error ? <p role="alert">{error}</p> : null}
        </article>
      );
    }

An event matches the function with its name, or the name without `on`: `onAddToCart` calls `addToCart`.

### Who may call a function#

A declaration can carry the A2UI 1.0 interface fields. `allowedCallers` is `"rendererOnly"` (event bindings and prop values), `"agentOnly"` (`callRendererFunction`) or `"rendererOrAgent"`. `requiresUserActivation: true` limits a function to a user gesture, like `openUrl`, which makes it `rendererOnly`. `returnType` names what the handler gives back, with the A2UI names (`"string"`, `"number"`, `"boolean"`, `"array"`, `"object"`, `"validationResult"`, `"any"`, `"void"`).
    
    
    functions: {
      addToCart: { parameters: z.object({ productId: z.string() }), allowedCallers: "rendererOrAgent", returnType: "object" },
      track: { parameters: z.object({ event: z.string() }), returnType: "void" },
      reload: { parameters: z.object({}), allowedCallers: "agentOnly" },
    },

Left out, only the UI may call the function, as in A2UI 1.0. The manifest and the exported catalog always write the value out, so a 1.0 reader sees the same thing. An event cannot match an `"agentOnly"` function, and the built-in functions are value functions of the UI.

In this version the agent cannot call renderer functions at all, whatever `allowedCallers` says: a `callRendererFunction` operation is rejected and never mentioned to the model, because its result would travel back as a developer message, and not every backend keeps that message where the model reads it in order. The declaration fields are kept for the catalog export and for when the path is on.

## Send a click to the agent#

Some clicks need the agent. For example, "Show me the Team plan" needs a new answer. An event that matches no function does that. Give it `parameters`:
    
    
    events: {
      onChoose: {
        description: "The user picked a plan",
        parameters: z.object({ plan: z.string() }),
      },
    },

When the user clicks, the click becomes a visible user message, and the agent answers it. The agent can also choose the text of that message (its `userMessage`), for example "Show me the Team plan".

The run that the click starts also carries the structured A2UI 1.0 action message, in `forwardedProps.copilotkit.ui.metadata.extensions.copilotkit_action`: `{ "version": "v1.0", "action": { "name": "choose", "surfaceId": "plans", "sourceComponentId": "team-button", "timestamp": "2026-10-20T10:00:00.000Z", "userMessage": "Show me the Team plan", "context": { "plan": "team" } } }`. An agent that wants the structured event reads it from there instead of parsing the message; `envelopeToManifest` from `@copilotkit/shared` gives it back as `action`.

## Compute values in the browser#

A prop can be a function value as well as a literal or a binding, at any depth: `{ "@call": "formatCurrency", "args": { "value": { "@path": "/total" }, "currency": "EUR" } }`. It recomputes when the data it reads changes, with no round trip to the agent. The functions of the A2UI 1.0 basic catalog are built in: `formatString` (with `${/path}` and `${fn(arg: value)}` interpolation), `formatNumber`, `formatCurrency`, `formatDate`, `pluralize`, `and`, `or`, `not`, the validators `required`, `regex`, `length`, `numeric` and `email`, `@index` in a template, and `openUrl`, which runs only as the `functionCall` of an event.

A2UI 1.0 has no arithmetic, so CopilotKit adds two catalog functions. `calc` evaluates an expression over named args: `{ "@call": "calc", "args": { "expression": "seats * 29 * (annual ? 0.8 : 1)", "seats": { "@path": "/seats" }, "annual": { "@path": "/annual" } } }`, with `+ - * / %`, comparisons, `&& || !`, `?:`, `min`, `max`, `round`, `floor`, `ceil`, `abs` and text concatenation. `series` builds a list of `count` items from an item template with `${...}` expressions over a loop variable, for chart data. Both appear to the model as regular catalog functions; a renderer without them rejects the call. The built-ins run only in the browser: the agent cannot call them with `callRendererFunction`.

## Keep what the user types#

A checkout form that the agent filled in must keep the user's edits. List the props that the component can change in `writable`. Each one gets a setter:
    
    
    CheckoutForm: {
      component: CheckoutForm,
      props: z.object({ email: z.string().optional() }),
      writable: ["email"],
    },
    
    
    function CheckoutForm({ email, setEmail }: GenerativeUIComponentProps<typeof shopUI, "CheckoutForm">) {
      return <input value={email ?? ""} onChange={(event) => setEmail(event.target.value)} />;
    }

When the agent binds `email` to a value of the surface, what the user types is written there. From then on, that value belongs to the user: a later agent update cannot write over it. The agent still sees the value on its next run.

Now the card shows live cart data, its button runs your code, and the form keeps the user's input.

### On this page

What is this?Show live app stateRun your code on a clickWho may call a functionSend a click to the agentCompute values in the browserKeep what the user types
