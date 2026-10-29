---
url: https://docs.copilotkit.ai/ag2/generative-ui/components/theming/
title: Theming
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:36.399587+00:00
---

# Theming

> Source: https://docs.copilotkit.ai/ag2/generative-ui/components/theming/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

[Components and surfaces](https://docs.copilotkit.ai/ag2/generative-ui/components)

[Surfaces](https://docs.copilotkit.ai/ag2/generative-ui/components/surfaces)[Catalogs](https://docs.copilotkit.ai/ag2/generative-ui/components/catalogs)[Standard catalog](https://docs.copilotkit.ai/ag2/generative-ui/components/standard-catalog)[State and actions](https://docs.copilotkit.ai/ag2/generative-ui/components/state-and-actions)[Theming](https://docs.copilotkit.ai/ag2/generative-ui/components/theming)[Transports](https://docs.copilotkit.ai/ag2/generative-ui/components/transports)[Markdown mode](https://docs.copilotkit.ai/ag2/generative-ui/components/markdown-mode)[Adopt from A2UI](https://docs.copilotkit.ai/ag2/generative-ui/components/from-a2ui)

[A2UI](https://docs.copilotkit.ai/ag2/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/ag2/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/ag2/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/ag2/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Theming

Generative UIDeclarativeComponents and surfaces

# Theming

Give the standard components your colors and fonts, and turn on dark mode.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

The standard components look neutral by default. You want them to use your accent color, your font, and your dark mode.

Every color, radius, shadow, and font of the standard components is a CSS variable. Set the variables with the `theme` option:
    
    
    <CopilotKitProvider
      runtimeUrl="/api/copilotkit"
      generativeUI={{
        ui: standardUI,
        theme: {
          "--a2ui-color-accent": "#d97706",
          "--a2ui-font-family": "Inter, sans-serif",
          "--a2ui-radius-md": "10px",
        },
      }}
    >

The keys are typed. A name that the components do not read, such as `"--a2ui-color-acent"`, is a type error.

## The variables#

Group| Variables  
---|---  
Accent and controls| `--a2ui-color-accent`, `--a2ui-color-on-accent`, `--a2ui-color-control`, `--a2ui-color-focus`  
Surfaces| `--a2ui-color-surface`, `--a2ui-color-surface-secondary`, `--a2ui-color-surface-elevated`, `--a2ui-color-panel`, and more `--a2ui-color-surface-*`  
Text| `--a2ui-color-text-default`, `--a2ui-color-text-secondary`, `--a2ui-color-text-tertiary`, and the `--a2ui-color-text-*` status colors  
Borders| `--a2ui-color-border-default`, `--a2ui-color-border-subtle`, `--a2ui-color-border-strong`, `--a2ui-color-border-control`  
Shape and type| `--a2ui-radius-*`, `--a2ui-shadow-xs` to `--a2ui-shadow-md`, `--a2ui-font-family`  
Charts| `--a2ui-chart-1` to `--a2ui-chart-6`  
  
Your editor lists all of them when you type a key in `theme`. To type a theme in its own file, use `GenerativeUITheme`:
    
    
    import type { GenerativeUITheme } from "@copilotkit/react-core/v2/generative-ui";
    
    export const theme: GenerativeUITheme = { "--a2ui-color-accent": "#d97706" };

## Dark mode#

Dark mode is built in. The standard components switch to dark colors when an ancestor has the `dark` class, the same rule as the CopilotKit chat:
    
    
    <html class="dark">

If your app already switches dark mode with a `dark` class, there is nothing to do. To follow the system setting, set the class with a small script in the `<head>`, so the page does not flash:
    
    
    const colorSchemeScript = `(() => {
      const media = matchMedia("(prefers-color-scheme: dark)");
      const apply = () => document.documentElement.classList.toggle("dark", media.matches);
      apply();
      media.addEventListener("change", apply);
    })();`;
    
    <head>
      <script dangerouslySetInnerHTML={{ __html: colorSchemeScript }} />
    </head>;

## Colors for each mode#

Values at the top level of `theme` apply in light and in dark mode. Values in `dark` replace them in dark mode only:
    
    
    theme: {
      "--a2ui-color-accent": "#d97706",
      dark: {
        "--a2ui-color-panel": "#1f2937",
        "--a2ui-color-surface": "#111827",
      },
    },

So a brand accent goes at the top level once, and only the colors that differ in dark mode go in `dark`.

## The map#

The `Map` component draws a light basemap, and a dark one in dark mode. Set your own [MapLibre style](https://maplibre.org/maplibre-style-spec/) for each mode:
    
    
    theme: {
      mapStyle: "https://tiles.example.com/light.json",
      dark: { mapStyle: "https://tiles.example.com/dark.json" },
    },

## Set variables in CSS#

You can also set the variables in your stylesheet, on the `.a2ui-surface` element that wraps every surface:
    
    
    .a2ui-surface {
      --a2ui-color-accent: #d97706;
    }

A value in `theme` wins over the same variable in your CSS.

Your accent, font, and dark colors now apply to every standard component, in the chat and on the page.

### On this page

What is this?The variablesDark modeColors for each modeThe mapSet variables in CSS
