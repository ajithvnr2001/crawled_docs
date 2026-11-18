---
url: https://docs.copilotkit.ai/generative-ui/a2ui/styling/
title: Styling
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.903991+00:00
---

# Styling

> Source: https://docs.copilotkit.ai/generative-ui/a2ui/styling/

# Styling

Customize the appearance of A2UI surfaces with CSS custom properties, fonts, and component-level overrides.

Copy MarkdownOpen

A2UI surfaces support theming through CSS custom properties scoped to the `.a2ui-surface` class.

This page covers the A2UI v0.9 surfaces you render through the `a2ui` prop. To theme the A2UI v1.0 standard components, see [Theming](https://docs.copilotkit.ai/generative-ui/components/theming).

## Theme CSSCopy Anchor Link

Create a theme file and import it in your layout:

src/a2ui/theme.css

Copy Text
    
    
    .a2ui-surface {
      --a2ui-color-surface: #ffffff;
      --a2ui-color-border: #e0e0e0;
      --a2ui-color-muted: #737373;
      --a2ui-color-error: #dc2626;
      --a2ui-primary-color: #111111;
    }

src/app/layout.tsx

Copy Text
    
    
    import "@/a2ui/theme.css";

## CSS custom properties referenceCopy Anchor Link

Variable| Default| Description  
---|---|---  
`--a2ui-color-surface`| `#fff`| Card, modal, chip, and button backgrounds  
`--a2ui-color-border`| `#ccc`| Borders, dividers, and the tab rule  
`--a2ui-color-muted`| `#666`| Captions and secondary text  
`--a2ui-color-error`| `red`| Validation errors  
`--a2ui-primary-color`| `#007bff`| Primary buttons, selected chips, and the active tab  
  
The built-in components set their own border radius, so there is no radius variable.

These variables are scoped to `.a2ui-surface`, so they won't affect the rest of your app. You can also set them on `:root` if you want global defaults.

## Custom fontsCopy Anchor Link

Override the font family on the surface container:

src/a2ui/theme.css

Copy Text
    
    
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .a2ui-surface {
      font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, system-ui, sans-serif !important;
      letter-spacing: -0.01em;
    }

## Image sizingCopy Anchor Link

An Image with no `variant` stretches to the width of its container. To keep logos and avatars small, set `variant` to `icon` or `avatar` in the schema, or constrain them with CSS:

src/a2ui/theme.css

Copy Text
    
    
    /* Constrain logos and avatars */
    .a2ui-surface img {
      max-width: 28px;
      max-height: 28px;
      border-radius: 4px;
    }
    
    /* Smaller status indicator icons */
    .a2ui-surface img[alt="On Time"],
    .a2ui-surface img[alt="Delayed"] {
      max-width: 10px;
      max-height: 10px;
      border-radius: 50%;
    }

## Dark modeCopy Anchor Link

CopilotKit sets dark A2UI colors for you when `.dark` is on an ancestor of the chat. To use your own dark colors, scope the variables under `.dark`:

src/a2ui/theme.css

Copy Text
    
    
    .dark .a2ui-surface {
      --a2ui-color-surface: #1a1a1a;
      --a2ui-color-border: #333333;
      --a2ui-color-muted: #a3a3a3;
      --a2ui-primary-color: #3b82f6;
    }

## Full exampleCopy Anchor Link

Here's a complete theme file combining all the patterns above:

src/a2ui/theme.css

Copy Text
    
    
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .a2ui-surface {
      /* Colors */
      --a2ui-color-surface: #ffffff;
      --a2ui-color-border: #e0e0e0;
      --a2ui-color-muted: #737373;
      --a2ui-color-error: #dc2626;
      --a2ui-primary-color: #111111;
    
      /* Typography */
      font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, system-ui, sans-serif !important;
      letter-spacing: -0.01em;
    }
    
    /* Image constraints */
    .a2ui-surface img {
      max-width: 28px;
      max-height: 28px;
      border-radius: 4px;
    }
    
    /* Dark mode */
    .dark .a2ui-surface {
      --a2ui-color-surface: #1a1a1a;
      --a2ui-color-border: #333333;
      --a2ui-color-muted: #a3a3a3;
      --a2ui-primary-color: #3b82f6;
    }

How is this guide?

GoodBad
