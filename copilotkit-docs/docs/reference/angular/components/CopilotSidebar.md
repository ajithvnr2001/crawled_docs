---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:26.799670+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar/

Angular/Components

# CopilotSidebar

Responsive docked or overlay Copilot chat sidebar for Angular.

Copy MarkdownOpen

`CopilotSidebar` renders a left- or right-positioned assistant in docked or overlay mode. It is a standalone, OnPush component with the selector `copilot-sidebar`.

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotSidebar } from "@copilotkit/angular";
    
    @Component({
      imports: [CopilotSidebar],
      template: `
        <copilot-sidebar
          [(open)]="open"
          mode="docked"
          position="right"
          [width]="480"
          title="Workspace assistant"
        />
      `,
    })
    export class WorkspaceAssistant {
      readonly open = signal(false);
    }

## Inputs and modelCopy Anchor Link

Name| Type| Default| Behavior  
---|---|---|---  
`open`| `ModelSignal<boolean>`| `true`| Two-way bindable open state  
`mode`| `"docked" | "overlay"`| `"docked"`| Desktop presentation mode  
`position`| `"left" | "right"`| `"right"`| Logical side of the viewport  
`width`| `number | string`| `480`| Pixel number or CSS dimension  
`title`| `string`| `"Copilot"`| Landmark/dialog name and header text  
`clickOutsideToClose`| `boolean`| `false`| Opts into overlay backdrop closing  
`chatComponent`| `Type<unknown>`| `CopilotChat`| Replacement chat body component  
`headerComponent`| `Type<unknown> | undefined`| `undefined`| Replacement header component  
  
## BehaviorCopy Anchor Link

  * Overlay mode: uses modal dialog semantics and traps focus. Escape closes the sidebar, and focus returns to the launcher.
  * Docked mode: uses a complementary landmark and adjusts the logical body margin of the document.
  * Compact viewports: always use the modal presentation.
  * One docked sidebar per document: a second open docked sidebar is rejected and logs a warning. Overlay sidebars do not have this limit.
  * Close or destroy: the owner restores the exact prior body margin and removes its media-query listener.
  * SSR: DOM and media-query work runs only in the browser, after render. Keep `open`, `mode`, and `position` stable through hydration.



How is this guide?

GoodBad

[Previous PageCopilotPopup](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)[Next PageCopilotKitAgentContext](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)
