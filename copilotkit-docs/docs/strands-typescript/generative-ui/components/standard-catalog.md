---
url: https://docs.copilotkit.ai/strands-typescript/generative-ui/components/standard-catalog/
title: Standard catalog
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:11.480305+00:00
---

# Standard catalog

> Source: https://docs.copilotkit.ai/strands-typescript/generative-ui/components/standard-catalog/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands-typescript)[Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands-typescript/frontend-tools)

Generative UI

Controlled

Declarative

[Components and surfaces](https://docs.copilotkit.ai/strands-typescript/generative-ui/components)

[Surfaces](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/surfaces)[Catalogs](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/catalogs)[Standard catalog](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/standard-catalog)[State and actions](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/state-and-actions)[Theming](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/theming)[Transports](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/transports)[Markdown mode](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/markdown-mode)[Adopt from A2UI](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/from-a2ui)

[A2UI](https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/strands-typescript/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/strands-typescript/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands-typescript/webmcp)

Agent capabilities

AWS Strands (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands-typescript/learning)

[User Memories](https://docs.copilotkit.ai/strands-typescript/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/strands-typescript/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/strands-typescript/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/strands-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Standard catalog

Generative UIDeclarativeComponents and surfaces

# Standard catalog

Use the 69 standard components, drop the ones you do not want, and replace any of them with your own.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

You want the agent to answer with tables, charts, and forms today, not after you build a component library. `standardUI` is a catalog of 69 ready-made components that the agent already knows how to use. The 18 components of the A2UI 1.0 basic catalog are in it under their A2UI names and props (`Image.url`, `CheckBox.value`, `Row.justify: "spaceBetween"`, `weight` for flex-grow); the rest extend the catalog.

Use it as it is:
    
    
    import { standardUI } from "@copilotkit/react-core/v2/generative-ui";
    
    <CopilotKitProvider runtimeUrl="/api/copilotkit" generativeUI={{ ui: standardUI }}>

## What is in it#

Group| Components  
---|---  
Layout| `Box`, `Column`, `Row`, `Grid`, `GridItem`, `Card`, `Flow`, `FlowItem`, `Carousel`, `CarouselItem`, `CarouselMediaItem`, `Spacer`, `Divider`, `Tabs`  
Text| `Title`, `Text`, `Caption`, `Label`, `Bold`, `Italic`, `Underline`, `Strikethrough`, `Badge`, `Blockquote`, `Code`, `Markdown`, `Math`, `ShimmerText`, `Link`, `Tooltip`  
Inputs| `Button`, `Pressable`, `Form`, `TextField`, `TextArea`, `Select`, `CheckBox`, `Radio`, `RadioGroup`, `Slider`, `SegmentedControl`, `ChoicePicker`, `DateTimeInput`  
Data| `Table`, `TableSection`, `TableRow`, `TableCell`, `List`, `ListItem`, `Chart`, `Map`  
Media| `Image`, `Icon`, `Favicon`, `Svg`, `Video`, `AudioPlayer`, `HtmlView`  
Feedback and overlay| `PulseIndicator`, `FlashcardFlip`, `Popover`, `PopoverTrigger`, `PopoverContent`, `Modal`  
Composites| `LinkCard`, `Citation`, `FollowUp`, `EntityCard`, `ImageGrid`  
  
A few things to know:

  * **Every input validates.** `checks` holds the `Checkable` rules of A2UI 1.0: `[{ "condition": { "@call": "email", "args": { "value": { "@path": "/form/email" } } }, "message": "Enter a valid email" }]`. An input shows the first failed message once the user has been in it, and a `Button` with the same checks is disabled while one fails. A result carries the A2UI `ValidationResult` fields: the built-in validators set a `code` (`required`, `pattern`, `tooShort`, `tooLong`, `notANumber`, `tooSmall`, `tooLarge`, `email`), and a `severity` of `"warning"` or `"info"` (from a bound result or your own validator) shows the message in its own colour without making the input invalid or holding the `Button` back.
  * **`Video` takes any URL.** A video file plays in the native player, with `captions` as WebVTT tracks; a YouTube link shows a poster until the user presses play, then loads the privacy-enhanced embed. A page on another video site (Vimeo, Loom, TikTok, …) and a file that fails to load show a link card instead of a dead player. YouTube is the only provider that embeds; to embed another one, replace the component. `Tabs` takes `tabs: [{ "title", "child" }]` with the id of each panel.
  * **Inputs keep what users type.** When the agent binds an input to a value, what the user types stays. A later agent update cannot write over it.
  * **`Button` and `Pressable` can act in the browser.** `href` opens a URL, and `Button` with `copy` copies text, with no message to the agent.
  * **`Map` needs one package.** Run `npm install maplibre-gl` if your agent draws maps. Without it, the map shows a list of the places.
  * **`Chart` works out of the box.** It uses `recharts`, which comes with CopilotKit.



To see every component with sample data, run [`examples/v2/a2ui-markdown`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/v2/a2ui-markdown) and open `/catalog`.

## Express calling conventions#

The standard catalog exports content, children, labels/values and common actions before presentation parameters. For example, the short prefixes are `Text(text?, children?)`, `Column(children?)`, `Button(label?, onClick?)`, `TextField(label?, value?)` and `Chart(data?, xKey?, series?, chartType?)`. Other component-specific fields follow, then shared layout and typography fields. Optional styling is easiest to pass by name.

This is CopilotKit's catalog design, not a prescribed list of signatures from A2UI. The official Express specification defines how JSON property order becomes argument order. The standard catalog applies that rule through [`exportA2UICatalog`](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/catalogs#positional-parameter-order), so agents consuming the exported catalog receive the same calling convention regardless of framework.

Compared with the initial experimental style-first catalog, this changes positional meanings. Start a fresh conversation when moving to this catalog and regenerate saved positional Express source against its signatures. Named arguments and JSON property values keep their meaning.

## Add your own components#

Put your components on top of the standard ones with `extends`:
    
    
    import { createGenerativeUI, standardUI } from "@copilotkit/react-core/v2/generative-ui";
    
    export const appUI = createGenerativeUI({
      id: "acme/app@1",
      extends: [standardUI],
      components: {
        ProductCard: { component: ProductCard, props: productSchema },
      },
    });

See [Catalogs](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/catalogs) for how to declare a component.

## Drop components#

Every component makes the prompt a little longer. If your app never needs a map or a video, remove them. `omit` returns a copy of the catalog without them, and the agent no longer sees them:
    
    
    export const appUI = createGenerativeUI({
      id: "acme/app@1",
      extends: [standardUI.omit(["Map", "Video", "HtmlView"])],
      components: {},
    });

The names are typed, so a typo is a type error. Call `omit` once, at module level.

## Replace a component#

Your app has its own card, with your shadows and spacing. `overrides` swaps the React component of a standard component. The agent sees the same component as before, with the same props:
    
    
    import {
      createGenerativeUI,
      standardUI,
      type GenerativeUIComponentProps,
    } from "@copilotkit/react-core/v2/generative-ui";
    
    function MyCard({ children }: GenerativeUIComponentProps<typeof standardUI, "Card">) {
      return <div className="rounded-2xl border p-6 shadow-sm">{children}</div>;
    }
    
    export const appUI = createGenerativeUI({
      id: "acme/app@1",
      extends: [standardUI],
      overrides: { Card: { component: MyCard } },
      components: {},
    });

  * Your component gets the props of the component it replaces. The types check this.
  * Only components of the catalogs in `extends` can be overridden. An unknown name is a type error.
  * You can combine both: `extends: [standardUI.omit(["Map"])]` with `overrides: { Card: ... }`.



Next: make the standard components match your brand with a [theme](https://docs.copilotkit.ai/strands-typescript/generative-ui/components/theming).

### On this page

What is this?What is in itExpress calling conventionsAdd your own componentsDrop componentsReplace a component
