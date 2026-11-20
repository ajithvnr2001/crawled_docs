---
url: https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea/
title: CopilotTextarea
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:28.094185+00:00
---

# CopilotTextarea

> Source: https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea/

React/v1

# CopilotTextarea

An AI-powered textarea component for your application, which serves as a drop-in replacement for any textarea.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`CopilotTextarea` has no direct v2 replacement. See the [v1 to v2 export map](https://docs.copilotkit.ai/reference/v1/export-map).

  
![](https://cdn.copilotkit.ai/docs/copilotkit/images/CopilotTextarea.gif)

`<CopilotTextarea>` is a React component that acts as a drop-in replacement for the standard `<textarea>`, offering enhanced autocomplete features powered by AI. It is context-aware, integrating with the [`useCopilotReadable`](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable) hook to provide intelligent suggestions based on the application context.

In addition, it provides a hovering editor window (available by default via `Cmd + K` on Mac and `Ctrl + K` on Windows) that allows the user to suggest changes to the text, for example providing a summary or rephrasing the text.

## ExampleCopy Anchor Link

Copy Text
    
    
    import { CopilotTextarea } from '@copilotkit/react-textarea';
    import "@copilotkit/react-textarea/styles.css";
    
    <CopilotTextarea
      autosuggestionsConfig={{
        textareaPurpose:
         "the body of an email message",
        chatApiConfigs: {},
      }}
    />

## UsageCopy Anchor Link

### Install DependenciesCopy Anchor Link

This component is part of the [@copilotkit/react-textarea](https://npmjs.com/package/@copilotkit/react-textarea) package.

Copy Text
    
    
    npm install @copilotkit/react-core @copilotkit/react-textarea

### UsageCopy Anchor Link

Use the CopilotTextarea component in your React application similarly to a standard `<textarea />`, with additional configurations for AI-powered features.

For example:

Copy Text
    
    
    import { useState } from "react";
    import { CopilotTextarea } from "@copilotkit/react-textarea";
    import "@copilotkit/react-textarea/styles.css";
    
    export function ExampleComponent() {
      const [text, setText] = useState("");
    
      return (
        <CopilotTextarea
          className="custom-textarea-class"
          value={text}
          onValueChange={(value: string) => setText(value)}
          placeholder="Enter your text here..."
          autosuggestionsConfig={{
            textareaPurpose: "Provide context or purpose of the textarea.",
            chatApiConfigs: {
              suggestionsApiConfig: {
                maxTokens: 20,
                stop: [".", "?", "!"],
              },
            },
          }}
        />
      );
    }

### Look & FeelCopy Anchor Link

By default, CopilotKit components do not have any styles. You can import CopilotKit's stylesheet at the root of your project:

YourRootComponent.tsx

Copy Text
    
    
    ...
    import "@copilotkit/react-textarea/styles.css";
    
    export function YourRootComponent() {
      return (
        <CopilotKit>
          ...
        </CopilotKit>
      );
    }

## PropertiesCopy Anchor Link

Prop

Type

`disableBranding?`boolean

`placeholderStyle?`React.CSSProperties

`suggestionsStyle?`React.CSSProperties

`hoverMenuClassname?`string

`value?`string

`onValueChange?`(value: string) => void

`onChange?`(event: React.ChangeEvent<HTMLTextAreaElement>) => void

`shortcut?`string

`autosuggestionsConfig`AutosuggestionsConfigUserSpecified

How is this guide?

GoodBad

[Previous PageCopilotSidebar](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotSidebar)[Next PageCopilotKit](https://docs.copilotkit.ai/reference/v1/components/CopilotKit)
