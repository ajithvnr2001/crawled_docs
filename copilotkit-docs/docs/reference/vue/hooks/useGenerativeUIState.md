---
url: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState/
title: useGenerativeUIState
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:17.860539+00:00
---

# useGenerativeUIState

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState/

Vue/Hooks

# useGenerativeUIState

Give generated components live app state, such as the cart, without sending it to the model

Copy MarkdownOpen

## OverviewCopy Anchor Link

A generated `ProductCard` must show how many of the product are in the cart. The agent does not know that number, and it must not guess. `useGenerativeUIState` gives one key of the declared app state its value. The props that read this key get the value. The model does not see it.

Generative UI is experimental. Call `useGenerativeUIState` in `setup()` (or `<script setup>`) of a component under a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) that has a `generativeUI` config. Outside such a provider, the composable throws an error.

For a full walkthrough, see [State and actions](https://docs.copilotkit.ai/generative-ui/components/state-and-actions).

## ImportCopy Anchor Link

Copy Text
    
    
    import { useGenerativeUIState } from "@copilotkit/vue/v2/generative-ui";

## SignatureCopy Anchor Link

Copy Text
    
    
    import type { MaybeRefOrGetter } from "vue";
    
    useGenerativeUIState<UI, Key>(
      ui: UI,
      key: Key,
      value: MaybeRefOrGetter<StateInput<UI, Key>>,
    ): void;

`StateInput<UI, Key>` is the input type of the schema of `key`. It is not exported. Let TypeScript infer it from `ui` and `key`.

## ParametersCopy Anchor Link

Prop

Type

`ui`GenerativeUI

`key`string

`value`MaybeRefOrGetter<StateInput<UI, Key>>

## Return valueCopy Anchor Link

None. The composable writes the value to the provider.

## ExampleCopy Anchor Link

`shopUI` declares the key in its state:

shop-ui.ts

Copy Text
    
    
    const cartSchema = z.object({
      items: z.array(z.object({ productId: z.string(), quantity: z.number() })),
    });
    
    export const shopUI = createGenerativeUI({
      id: "acme/shop@1",
      state: { cart: cartSchema },
      components: {
        /* ... */
      },
    });

Give the key its value from a component:

CartState.vue

Copy Text
    
    
    <script setup lang="ts">
    import { useGenerativeUIState } from "@copilotkit/vue/v2/generative-ui";
    import { useCartStore } from "./cart-store";
    import { shopUI } from "./shop-ui";
    
    const cart = useCartStore();
    
    useGenerativeUIState(shopUI, "cart", () => ({ items: cart.items }));
    </script>
    
    <template>
      <slot />
    </template>

## BehaviorCopy Anchor Link

  * The key is set at once. It is set again when the value changes. Values are compared as JSON.
  * The value goes through the schema of the key. Schema defaults and transforms apply.
  * An invalid value is not stored. The props that read the key show their fallback. In development, an error is logged.
  * The key is removed when the effect scope is disposed, for example when the component unmounts.
  * The model does not see the state. To let the agent answer questions about it, also give the data with [`useAgentContext`](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext).



## RelatedCopy Anchor Link

  * [`useGenerativeUIFunction`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction) \- run your code when generated UI calls a function
  * [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface) \- mark an area of your page for generated UI
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- give the provider the `generativeUI` config



How is this guide?

GoodBad

[Previous PageuseGenerativeUIFunction](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction)[Next PageuseHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)
