---
url: https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface/
title: GenerativeUISurface
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:06.059778+00:00
---

# GenerativeUISurface

> Source: https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface/

Vue/Components

# GenerativeUISurface

Vue 3 component that marks a named area of your page where the agent can render generated UI.

Copy MarkdownOpen

## OverviewCopy Anchor Link

The chat is not always the right place for generated UI. A product grid belongs in the product area of your page. `GenerativeUISurface` marks that area as a target. The agent can then render your components into it.

Until the agent renders into the target, the component shows its default slot.

Generative UI is experimental. Use `GenerativeUISurface` under a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) that has a [`generativeUI`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) config. Outside such a provider, the component throws an error.

For a full walkthrough, see [Surfaces](https://docs.copilotkit.ai/generative-ui/components/surfaces).

## ImportCopy Anchor Link

Copy Text
    
    
    import { GenerativeUISurface } from "@copilotkit/vue/v2/generative-ui";

## PropsCopy Anchor Link

Prop

Type

`id`string

`description?`string

`ui?`GenerativeUI

`components?`readonly GenerativeUIComponentName<UI>[]

`autoScroll?`boolean

Other attributes, such as `class` and `style`, go to the element around the rendered surface. That element has a `data-generative-ui-surface` attribute with the `id`.

## SlotsCopy Anchor Link

Prop

Type

`default?`slot

## ExampleCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { GenerativeUISurface } from "@copilotkit/vue/v2/generative-ui";
    import { shopUI } from "./shop-ui";
    import ProductRow from "./ProductRow.vue";
    
    defineProps<{ products: { id: string; name: string }[] }>();
    </script>
    
    <template>
      <GenerativeUISurface
        id="featured"
        :ui="shopUI"
        description="The Featured Products row. Show products here as a ProductGrid with one ProductCard for each product."
        :components="['ProductGrid', 'ProductCard']"
        class="featured-row"
      >
        <ProductRow :products="products" />
      </GenerativeUISurface>
    </template>

`shopUI` is the object from `createGenerativeUI`. The provider gets the same object:

Copy Text
    
    
    <CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: shopUI }">
      <App />
    </CopilotKitProvider>

## BehaviorCopy Anchor Link

  * The target registers after mount, so server rendering registers nothing.
  * The agent knows about the target only while it is mounted. When it unmounts, the agent cannot render into it.
  * If `components` names a component that the UI does not have, the name is dropped. In development, a warning is logged.
  * A change to `id`, `description`, or `components` registers the target again. A new array with the same names does not.



## RelatedCopy Anchor Link

  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- give the provider the `generativeUI` config
  * [`useGenerativeUIState`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState) \- give generated components live app state
  * [`useGenerativeUIFunction`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction) \- run your code when generated UI calls a function
  * [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) \- change the card around surfaces in the chat



How is this guide?

GoodBad

[Previous PageCopilotThreadsDrawer](https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer)[Next PageuseAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)
