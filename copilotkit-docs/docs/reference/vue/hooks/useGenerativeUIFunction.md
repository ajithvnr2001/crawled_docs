---
url: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction/
title: useGenerativeUIFunction
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:51.510090+00:00
---

# useGenerativeUIFunction

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁VueSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)[CopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)[CopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer)[GenerativeUISurface](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)[useGenerativeUIFunction](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction)[useGenerativeUIState](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/vue/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Hooks

# useGenerativeUIFunction

Run your own code when a generated component calls a declared function, such as add to cart

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

A user clicks "Add to cart" on a generated `ProductCard`. That click must add to the cart, with no message to the agent. `useGenerativeUIFunction` mounts the handler of a function that you declare in `createGenerativeUI({ functions })`. When generated UI calls the function, your handler runs.

Generative UI is experimental. Call `useGenerativeUIFunction` in `setup()` (or `<script setup>`) of a component under a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) that has a `generativeUI` config. Outside such a provider, the composable throws an error.

For a full walkthrough, see [State and actions](https://docs.copilotkit.ai/generative-ui/components/state-and-actions).

## Import
    
    
    import { useGenerativeUIFunction } from "@copilotkit/vue/v2/generative-ui";

## Signature
    
    
    import type { GenerativeUIFunctionArgs } from "@copilotkit/vue/v2/generative-ui";
    
    useGenerativeUIFunction<UI, Name>(
      ui: UI,
      name: Name,
      handler: (args: GenerativeUIFunctionArgs<UI, Name>) => unknown,
    ): void;

## Parameters

Prop

Type

`ui`GenerativeUI

Prop

Type

`name`string

Prop

Type

`handler`(args: GenerativeUIFunctionArgs<UI, Name>) => unknown

## Return value

None. The handler stays mounted until the effect scope is disposed.

## Example

`shopUI` declares the function:

shop-ui.ts
    
    
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

## Behavior

  * Generated UI can call the function only while exactly one handler for it is mounted. Mount one handler for each function.
  * The handler is registered once. It reads refs, props, and stores when it runs, so it sees their current values.
  * The handler is unregistered when the effect scope is disposed, for example when the component unmounts.
  * Failures go to `errorBoundary.onError` of the provider's `generativeUI` config.



## Related

  * [`useGenerativeUIState`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState) \- give generated components live app state
  * [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface) \- mark an area of your page for generated UI
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- give the provider the `generativeUI` config


