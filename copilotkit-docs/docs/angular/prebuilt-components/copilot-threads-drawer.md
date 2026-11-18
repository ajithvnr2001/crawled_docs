---
url: https://docs.copilotkit.ai/angular/prebuilt-components/copilot-threads-drawer/
title: Threads Drawer
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.550093+00:00
---

# Threads Drawer

> Source: https://docs.copilotkit.ai/angular/prebuilt-components/copilot-threads-drawer/

Threads

# Threads Drawer

Put the ready-made CopilotThreadsDrawer next to an Angular chat to list, switch, and manage conversations.

Copy MarkdownOpen

`CopilotThreadsDrawer` supplies a ready-made list, selection, filtering, pagination, and mutation controls. Put the drawer and chat under the same `provideCopilotChatConfiguration` provider so selection and new-thread actions update the chat. The drawer reads the platform's `threads` license feature and shows its locked state when that feature is unavailable.

Copy Text
    
    
    import { Component } from "@angular/core";
    import {
      CopilotChat,
      CopilotThreadsDrawer,
      provideCopilotChatConfiguration,
    } from "@copilotkit/angular";
    
    @Component({
      selector: "app-conversations",
      imports: [CopilotChat, CopilotThreadsDrawer],
      providers: [provideCopilotChatConfiguration({ agentId: "support" })],
      template: `
        <copilot-threads-drawer agentId="support" [limit]="20" />
        <copilot-chat />
      `,
    })
    export class ConversationsComponent {}

## Next stepsCopy Anchor Link

  * [Headless Threads](https://docs.copilotkit.ai/angular/headless-threads): build your own thread list with `injectThreads`.



How is this guide?

GoodBad

[Previous PageVoice](https://docs.copilotkit.ai/angular/voice)[Next PageHeadless Threads](https://docs.copilotkit.ai/angular/headless-threads)
