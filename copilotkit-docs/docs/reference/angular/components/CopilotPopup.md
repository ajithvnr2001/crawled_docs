---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:26.944151+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotPopup/

Angular/Components

# CopilotPopup

Accessible floating Copilot chat dialog for Angular.

Copy MarkdownOpen

`CopilotPopup` renders a floating launcher and responsive chat dialog. It is a standalone, OnPush component with the selector `copilot-popup`.

Copy Text
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotPopup } from "@copilotkit/angular";
    
    @Component({
      imports: [CopilotPopup],
      template: `
        <copilot-popup
          [(open)]="open"
          title="Support assistant"
          [width]="420"
          [height]="560"
          [clickOutsideToClose]="false"
        />
      `,
    })
    export class SupportAssistant {
      readonly open = signal(false);
    }

## Inputs and modelCopy Anchor Link

Name| Type| Default| Behavior  
---|---|---|---  
`open`| `ModelSignal<boolean>`| `true`| Two-way bindable open state  
`title`| `string`| `"Copilot"`| Accessible dialog name and default header text  
`width`| `number | string`| `420`| Pixel number or CSS dimension  
`height`| `number | string`| `560`| Pixel number or CSS dimension  
`clickOutsideToClose`| `boolean`| `false`| Opts into backdrop-click closing  
`chatComponent`| `Type<unknown>`| `CopilotChat`| Replacement chat body component  
`headerComponent`| `Type<unknown> | undefined`| `undefined`| Replacement header component  
  
## BehaviorCopy Anchor Link

  * Focus: the dialog traps focus and moves initial focus to its close control.
  * Escape: closes the dialog. Focus returns to the launcher.
  * Compact viewports: the dialog becomes full-screen.
  * Reduced motion: the dialog has no entrance animation.
  * Destroy: removes the rendered dialog and its Angular CDK focus-trap state.
  * SSR: browser focus work starts after render and does nothing during SSR. Keep the initial `open` value unchanged until hydration completes.



How is this guide?

GoodBad

[Previous PageCopilotChatView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)[Next PageCopilotSidebar](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)
