---
url: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction/
title: useGenerativeUIFunction
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:21.929420+00:00
---

# useGenerativeUIFunction

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction/

Vue/Hooks

# useGenerativeUIFunction

Run your own code when a generated component calls a declared function, such as add to cart

Copy MarkdownOpen

## OverviewCopy Anchor Link

A user clicks "Add to cart" on a generated `ProductCard`. That click must add to the cart, with no message to the agent. `useGenerativeUIFunction` mounts the handler of a function that you declare in `createGenerativeUI({ functions })`. When generated UI calls the function, your handler runs.

Generative UI is experimental. Call `useGenerativeUIFunction` in `setup()` (or `<script setup>`) of a component under a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) that has a `generativeUI` config. Outside such a provider, the composable throws an error.

For a full walkthrough, see [State and actions](https://docs.copilotkit.ai/generative-ui/components/state-and-actions).

## ImportCopy Anchor Link

Copy Text
    
    
    import { useGenerativeUIFunction } from "@copilotkit/vue/v2/generative-ui";

## SignatureCopy Anchor Link

Copy Text
    
    
    import type { GenerativeUIFunctionArgs } from "@copilotkit/vue/v2/generative-ui";
    
    useGenerativeUIFunction<UI, Name>(
      ui: UI,
      name: Name,
      handler: (args: GenerativeUIFunctionArgs<UI, Name>) => unknown,
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`ui`GenerativeUI

`name`string

`handler`(args: GenerativeUIFunctionArgs<UI, Name>) => unknown

## Return valueCopy Anchor Link

None. The handler stays mounted until the effect scope is disposed.

## ExampleCopy Anchor Link

`shopUI` declares the function:

shop-ui.ts

Copy Text
    
    
    export const shopUI = createGenerativeUI({
      id: "acme/shop@1",
      functions: {
        addToCart: {
          description: "Add a product to the cart",
          parameters: z.object({ productId: z.string(), quantity: z.number().default(1) }),
        },
      },
      components: {
        /* ... */
      },
    });

Mount the handler from a component:

CartActions.vue

Copy Text
    
    
    <script setup lang="ts">
    import { useGenerativeUIFunction } from "@copilotkit/vue/v2/generative-ui";
    import { useCartStore } from "./cart-store";
    import { shopUI } from "./shop-ui";
    
    const cart = useCartStore();
    
    useGenerativeUIFunction(shopUI, "addToCart", ({ productId, quantity }) => {
      cart.addItem(productId, quantity);
      return { added: productId };
    });
    </script>
    
    <template>
      <slot />
    </template>

## BehaviorCopy Anchor Link

  * Generated UI can call the function only while exactly one handler for it is mounted. Mount one handler for each function.
  * The handler is registered once. It reads refs, props, and stores when it runs, so it sees their current values.
  * The handler is unregistered when the effect scope is disposed, for example when the component unmounts.
  * Failures go to `errorBoundary.onError` of the provider's `generativeUI` config.



## RelatedCopy Anchor Link

  * [`useGenerativeUIState`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState) \- give generated components live app state
  * [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface) \- mark an area of your page for generated UI
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- give the provider the `generativeUI` config



How is this guide?

GoodBad

[Previous PageuseFrontendTool](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)[Next PageuseGenerativeUIState](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState)
