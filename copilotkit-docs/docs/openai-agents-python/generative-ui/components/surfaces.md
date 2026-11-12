---
url: https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/surfaces/
title: Surfaces
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:40.664593+00:00
---

# Surfaces

> Source: https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/surfaces/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/openai-agents-python/frontend-tools)

Generative UI

Controlled

Declarative

[Components and surfaces](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components)

[Surfaces](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/surfaces)[Catalogs](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/catalogs)[Standard catalog](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/standard-catalog)[State and actions](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/state-and-actions)[Theming](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/theming)[Transports](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/transports)[Markdown mode](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/markdown-mode)[Adopt from A2UI](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/from-a2ui)

[A2UI](https://docs.copilotkit.ai/openai-agents-python/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/openai-agents-python/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/openai-agents-python/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/openai-agents-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/openai-agents-python/learning)

[User Memories](https://docs.copilotkit.ai/openai-agents-python/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/openai-agents-python/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/openai-agents-python/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/openai-agents-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/openai-agents-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/openai-agents-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/openai-agents-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Surfaces

Generative UIDeclarativeComponents and surfaces

# Surfaces

Render generated UI in the chat, or in named areas of your page that the chat can change.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

The chat is a good place for an answer. It is a bad place for the product grid of your shop. When a user asks "show me cheap running shoes", the shoes belong in the product row of the page, not in a chat bubble.

A **surface** is one piece of generated UI. Each surface renders in a **target** , a place where generated UI can go:

  * **The chat.** Always there. The agent can use every component of the catalog. On React Native, you draw chat surfaces yourself, with `GenerativeUIActivity`; see Chat surfaces on React Native. The agent is offered the chat target even when the app shows no chat, so a React Native app that renders only `GenerativeUISurface` targets, or only the prebuilt `CopilotChat` (which does not draw surfaces yet), never shows a surface aimed at the chat.
  * **A page target.** An area of your page that you mark with `GenerativeUISurface`, or `<copilot-generative-ui-surface>` in Angular. The agent sees it only while it is mounted.



## Add a page target#

Wrap an area of your page in a target. Give it an id, and tell the agent what the area is for:

ReactAngularReact NativeVue

app/page.tsx
    
    
    import { GenerativeUISurface } from "@copilotkit/react-core/v2/generative-ui";
    import { shopUI } from "./catalog";
    
    export function FeaturedProducts({ products }: { products: Product[] }) {
      return (
        <GenerativeUISurface
          id="featured"
          ui={shopUI}
          description="The Featured Products row of the home page. When the customer asks to see products here, show them as a ProductGrid with one ProductCard for each product. When they ask for the featured products again, delete this surface."
          components={["ProductGrid", "ProductCard"]}
          fallback={<ProductRow products={products} />}
        />
      );
    }

src/app/featured-products.component.ts
    
    
    import { Component, input } from "@angular/core";
    import { CopilotGenerativeUISurface } from "@copilotkit/angular/generative-ui";
    import { ProductRow } from "./product-row.component";
    import { shopUI } from "./shop-ui";
    
    @Component({
      selector: "app-featured-products",
      imports: [CopilotGenerativeUISurface, ProductRow],
      template: `
        <copilot-generative-ui-surface
          id="featured"
          [ui]="shopUI"
          description="The Featured Products row of the home page. When the customer asks to see products here, show them as a ProductGrid with one ProductCard for each product. When they ask for the featured products again, delete this surface."
          [components]="['ProductGrid', 'ProductCard']"
        >
          <app-product-row [products]="products()" />
        </copilot-generative-ui-surface>
      `,
    })
    export class FeaturedProducts {
      readonly products = input.required<Product[]>();
      protected readonly shopUI = shopUI;
    }

The content of the element is the fallback.

src/FeaturedProducts.tsx
    
    
    import { GenerativeUISurface } from "@copilotkit/react-native/generative-ui";
    import { ProductRow } from "./ProductRow";
    import { shopUI } from "./shopUI";
    
    export function FeaturedProducts({ products }: { products: Product[] }) {
      return (
        <GenerativeUISurface
          id="featured"
          ui={shopUI}
          description="The Featured Products row of the home screen. When the customer asks to see products here, show them as a ProductGrid with one ProductCard for each product. When they ask for the featured products again, delete this surface."
          components={["ProductGrid", "ProductCard"]}
          fallback={<ProductRow products={products} />}
          style={{ marginVertical: 16 }}
        />
      );
    }

`style` applies to the `View` around the surface, which also holds the fallback, so the spacing stays the same when the agent's row replaces yours. `GenerativeUISurface` throws when no `GenerativeUIProvider` is above it, and shows its fallback under a provider that has no `ui`. A target follows the thread that is active in the provider, the thread of the last run that started on the core (of any agent), so it suits a screen that shares its agent with the chat. To show the output of one particular agent, such as a background run that composes a home screen, render that agent's activity message with `GenerativeUIActivity`; see Chat surfaces on React Native.

src/components/FeaturedProducts.vue
    
    
    <script setup lang="ts">
    import { GenerativeUISurface } from "@copilotkit/vue/v2/generative-ui";
    import type { Product } from "../product";
    import { shopUI } from "../shop-ui";
    import ProductRow from "./ProductRow.vue";
    
    defineProps<{ products: Product[] }>();
    </script>
    
    <template>
      <GenerativeUISurface
        id="featured"
        :ui="shopUI"
        description="The Featured Products row of the home page. When the customer asks to see products here, show them as a ProductGrid with one ProductCard for each product. When they ask for the featured products again, delete this surface."
        :components="['ProductGrid', 'ProductCard']"
      >
        <ProductRow :products="products" />
      </GenerativeUISurface>
    </template>

The default slot is the fallback.

What each prop does:

  * `id`: the target id. The agent names it when it renders here.
  * `description`: what the area is and what belongs in it. The agent reads it in each run that starts while the target is mounted, so write it like an instruction.
  * `fallback`: shows until the agent renders here, and again after the agent deletes its surface, unless an older surface of the same target and thread is still live: then that one shows. In Angular, the projected content is the fallback. In Vue, the default slot is the fallback.
  * `ui` and `components`: the only components the agent can use here. See Limit the components.



Now "show me cheap running shoes" swaps the row, and "show the featured products again" brings your own row back.

## Chat surfaces on React Native#

The prebuilt React Native `CopilotChat` does not draw surfaces yet. Every surface reaches the app as an **activity message** in `agent.messages`, though, and `GenerativeUIActivity` from `@copilotkit/react-native/generative-ui` draws one wherever you put it:

  * **In your own message list** , one per activity message. Like the web chat, `GenerativeUIActivity` shows only surfaces whose target is `"chat"`, so a surface aimed at a page target renders in its `GenerativeUISurface` and does not show twice. To show a surface of another target, pass that target id in its `target` prop.
  * **On a screen with no chat.** A home screen can start a run of its own agent and show the chat surfaces that run renders. This part renders them; the [React Native guide](https://docs.copilotkit.ai/openai-agents-python/react-native#compose-a-screen-with-no-chat) has the whole screen, which starts the run once, shows a spinner while it runs and a retry when it fails, and defines `isChatSurface`:



src/HomeSurfaces.tsx
    
    
    import { View } from "react-native";
    import { useAgent } from "@copilotkit/react-native/headless";
    import { GenerativeUIActivity } from "@copilotkit/react-native/generative-ui";
    import { isChatSurface } from "./agentTurns";
    
    export function HomeSurfaces() {
      const { agent } = useAgent({ agentId: "home" });
      // Every surface that renders here: aimed at the chat, and not deleted. Not only
      // the latest activity message, which can be a deleted surface or one aimed at a
      // page target, and render nothing.
      const surfaces = agent.messages.filter(isChatSurface);
      return (
        <View>
          {surfaces.map((message) => (
            <GenerativeUIActivity key={message.id} message={message} agent={agent} />
          ))}
        </View>
      );
    }

`GenerativeUIActivity` reads the surface from the thread of the agent you pass, so it shows that agent's output even when another agent ran last. It must be under `GenerativeUIProvider`: without one, or under a provider without `ui`, it renders nothing, and warns in development.

## Limit the components#

A product row must hold product cards, not a slider or a chart. `components` names the only components that the agent can use in this target, the root included:

ReactAngularReact NativeVue
    
    
    <GenerativeUISurface id="featured" ui={shopUI} components={["ProductGrid", "ProductCard"]} />
    
    
    <copilot-generative-ui-surface id="featured" [ui]="shopUI" [components]="['ProductGrid', 'ProductCard']" />
    
    
    <GenerativeUISurface id="featured" ui={shopUI} components={["ProductGrid", "ProductCard"]} />
    
    
    <GenerativeUISurface id="featured" :ui="shopUI" :components="['ProductGrid', 'ProductCard']" />

  * The agent gets the list, so it knows what fits.
  * An operation with another component is rejected, and the agent gets the reason.
  * `ui` types the names, so a typo is a type error. Pass the same catalog that you gave the provider.



Leave out `components` (and `ui`) to allow every component of the catalog. Names that are not in the catalog are dropped, with a warning in development. An empty list, or one with only unknown names, allows no component: the target is still offered to the agent, but every operation that places a component in it is rejected.

## Scroll to the surface#

When the agent starts to render into a target, the page scrolls to it, unless it is already on screen. Turn this off for one target:

ReactAngularReact NativeVue
    
    
    <GenerativeUISurface id="sidebar-notes" autoScroll={false} />
    
    
    <copilot-generative-ui-surface id="sidebar-notes" [autoScroll]="false" />

React Native has no `autoScroll`. Instead, `onGenerationStart` is called once each time the agent starts to render into the target (each `render_ui` call, for a new surface or an update), and when the target mounts, its `id` changes, or the active thread changes, while the agent is rendering into it. A re-render, `<React.StrictMode>` or a new callback does not call it again for the same start, and an error it throws is caught and logged with `console.error`. A call counts as new when the surface starts streaming again, or keeps streaming while the runtime resets its rejected operations; so when a reconnect delivers the next call already streaming and neither call had a rejected operation, the two calls count as one start. Scroll there yourself. The position you have may be out of date when the call comes: a target that mounts while the agent renders into it gets the call before its first layout, and content above the target can move as the generation starts. So for a short time after each call, scroll again whenever `onLayout` gives a new position:
    
    
    const scrollRef = useRef<ScrollView>(null);
    const notesY = useRef<number | undefined>(undefined);
    // Until this time, a new position of the target scrolls to it again.
    const followUntil = useRef(0);
    
    const scrollToNotes = () => {
      followUntil.current = Date.now() + 1000;
      // Undefined before the first layout: onLayout scrolls then.
      if (notesY.current !== undefined) {
        scrollRef.current?.scrollTo({ y: notesY.current, animated: true });
      }
    };
    
    <ScrollView ref={scrollRef}>
      {/* ... */}
      {/* A direct child of the ScrollView, so its layout y is its offset in the content. */}
      <View
        onLayout={(event) => {
          const { y } = event.nativeEvent.layout;
          if (y === notesY.current) return; // same position: nothing to correct
          notesY.current = y;
          if (Date.now() < followUntil.current) {
            scrollRef.current?.scrollTo({ y, animated: true });
          }
        }}
      >
        <GenerativeUISurface id="sidebar-notes" onGenerationStart={scrollToNotes} />
      </View>
    </ScrollView>;
    
    
    <GenerativeUISurface id="sidebar-notes" :auto-scroll="false" />

On the web, with a sticky header, give surfaces some room at the top in your CSS:
    
    
    [data-generative-ui-surface] {
      scroll-margin-top: 6rem;
    }

## One target for each item#

A target can be specific. A product page can give each product its own target, so its recommendations stay with it when the user moves between products:

ReactAngularReact NativeVue
    
    
    <GenerativeUISurface
      key={product.id}
      id={`recommendations-${product.id}`}
      description={`The "You might also like" row under ${product.name}. Show related products here. Never include ${product.name} itself.`}
    />
    
    
    @Component({
      selector: "app-product-page",
      imports: [CopilotGenerativeUISurface],
      template: `
        <copilot-generative-ui-surface
          [id]="'recommendations-' + product().id"
          [description]="recommendationsDescription(product())"
        />
      `,
    })
    export class ProductPage {
      readonly product = input.required<Product>();
    
      protected recommendationsDescription({ name }: Product) {
        return `The "You might also like" row under ${name}. Show related products here. Never include ${name} itself.`;
      }
    }

When the `id` input changes, the target is registered again under the new id, so no key is needed.
    
    
    <GenerativeUISurface
      key={product.id}
      id={`recommendations-${product.id}`}
      description={`The "You might also like" row under ${product.name}. Show related products here. Never include ${product.name} itself.`}
    />
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { GenerativeUISurface } from "@copilotkit/vue/v2/generative-ui";
    import type { Product } from "../product";
    
    const props = defineProps<{ product: Product }>();
    const description = computed(
      () =>
        `The "You might also like" row under ${props.product.name}. Show related products here. Never include ${props.product.name} itself.`,
    );
    </script>
    
    <template>
      <GenerativeUISurface :id="`recommendations-${product.id}`" :description="description" />
    </template>

When the `id` prop changes, the target is registered again under the new id, so no `key` is needed.

## When a component fails#

Each component renders inside its own error boundary. One broken component shows a small fallback, and the rest of the surface keeps working. To report errors, or to draw your own fallback:

ReactAngularReact NativeVue
    
    
    <CopilotKitProvider
      runtimeUrl="/api/copilotkit"
      generativeUI={{
        ui: shopUI,
        errorBoundary: {
          onError: (info) => console.warn(info.kind, info.surfaceId, info.error.message),
          fallback: ({ retry }) => <button onClick={retry}>Try again</button>,
        },
      }}
    >

src/app/app.config.ts
    
    
    provideGenerativeUI({
      ui: shopUI,
      onError: (info) => console.warn(info.kind, info.surfaceId, info.error.message),
      // A component with the inputs `message` and `componentId`, and
      // `retry` if it declares it.
      errorFallback: MyFallback,
    });

Angular has no per-component error boundary. A component that throws while it is created shows the fallback and reports to `onError`; an error in a later change detection goes to the `ErrorHandler` of the app. After a render error, the default fallback shows a Retry button that creates the component again with the current data. A custom `errorFallback` gets the same function in its `retry` input, if it declares one.
    
    
    <CopilotKitProvider runtimeUrl={runtimeUrl}>
      <GenerativeUIProvider
        ui={shopUI}
        errorBoundary={{
          onError: (info) => console.warn(info.kind, info.surfaceId, info.error.message),
          fallback: ({ retry }) => (
            <Pressable onPress={retry}>
              <Text>Try again</Text>
            </Pressable>
          ),
        }}
      >

The default fallback is the `NodeFallback` of the provider's `host`, `NativeNodeFallback` unless you pass your own `host`: the error, in native views, and a Retry button after a render error. A component whose props fail its schema shows it too, with the reason and no Retry button; your own `fallback` is not used for it. When your `fallback` throws, the host fallback with Retry shows in its place; when the host fallback throws, the node renders nothing. Either way the failure stays in its node, and it is reported to `onError`.

There is no Inspector on React Native. `onError` gets render failures, invalid props, failed events, failed functions that a component called and the operations that the app rejected; a render failure or invalid props that stay the same while the agent sends new content are reported once, and a failed event or function on every call. Operations that the runtime rejected never reach `onError`. They reach the `rejected` and `error` props of the `Wrapper`: the `Wrapper` of `GenerativeUIActivity` for a chat surface, and the `Wrapper` of `GenerativeUISurface` for a surface in a named target. Both default wrappers show a short error line. The exception is a rejected `createSurface`. A named target then keeps its fallback and renders no `Wrapper`; when the app rejected it, `onError` gets it and `<GenerativeUIActivity target="<id>">` shows it. When the runtime rejected it, no activity message is sent for it, so only the model learns of it, in the result of its `render_ui` call, and nothing on the device shows it. The one exception is a `createSurface` with the id of a live surface: the runtime adds that rejection to the live surface, whose `Wrapper` shows it. See [Errors on the device](https://docs.copilotkit.ai/openai-agents-python/react-native#errors-on-the-device).

The fallback is a Vue component. It gets `error`, `retry`, `surfaceId`, and `componentId` as props:

src/components/RetryFallback.vue
    
    
    <script setup lang="ts">
    import type { GenerativeUIErrorFallbackProps } from "@copilotkit/vue/v2/generative-ui";
    
    defineProps<GenerativeUIErrorFallbackProps>();
    </script>
    
    <template>
      <button @click="retry">Try again</button>
    </template>
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    import type { GenerativeUIErrorInfo } from "@copilotkit/vue/v2/generative-ui";
    import RetryFallback from "./components/RetryFallback.vue";
    import { shopUI } from "./shop-ui";
    
    function onError(info: GenerativeUIErrorInfo) {
      console.warn(info.kind, info.surfaceId, info.error.message);
    }
    </script>
    
    <template>
      <CopilotKitProvider
        runtime-url="/api/copilotkit"
        :generativeUI="{ ui: shopUI, errorBoundary: { onError, fallback: RetryFallback } }"
      >
        <slot />
      </CopilotKitProvider>
    </template>

When your `fallback` throws, the default fallback with Retry shows in its place. The failure stays in its node, and `onError` gets it. A render failure that stays the same while the agent sends new content is reported once.

## What the agent knows about surfaces#

On every run, the agent gets:

  * The targets that are mounted, with their descriptions and component limits, and the chat target.
  * The surfaces that already exist, so it can update one in place instead of building a new one.
  * The values the user typed into a surface. The agent cannot write over those values.
  * The operations that the runtime or the app (the browser, or the React Native app) rejected, with the reason, so the agent can fix them.



To see the same data, open the **Surfaces** tab of the Generative UI pane in Inspector. If a surface stays empty, see [When something does not render](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components#when-something-does-not-render).

Next: decide what the agent can render in a surface, with a [catalog](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components/catalogs).

### On this page

What is this?Add a page targetChat surfaces on React NativeLimit the componentsScroll to the surfaceOne target for each itemWhen a component failsWhat the agent knows about surfaces
