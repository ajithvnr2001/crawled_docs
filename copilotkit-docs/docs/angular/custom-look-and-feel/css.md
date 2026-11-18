---
url: https://docs.copilotkit.ai/angular/custom-look-and-feel/css/
title: CSS Customization
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.574800+00:00
---

# CSS Customization

> Source: https://docs.copilotkit.ai/angular/custom-look-and-feel/css/

Chat/Custom Look and Feel

# CSS Customization

Restyle the prebuilt Angular chat with scoped CSS on its stable classes.

Copy MarkdownOpen

Restyle the prebuilt chat from [Prebuilt Components](https://docs.copilotkit.ai/angular/prebuilt-components) with plain CSS. Import the package stylesheet first, as shown in [Add an inline chat](https://docs.copilotkit.ai/angular/prebuilt-components#add-an-inline-chat).

## Scope CSS changesCopy Anchor Link

The package stylesheet exposes stable chat classes. Put a scope class on your feature host so the change stays local.

src/styles.css

Copy Text
    
    
    .support-chat .copilotKitUserMessage {
      color: white;
      background: #2563eb;
      border-radius: 0.75rem;
    }
    
    .support-chat .copilotKitAssistantMessage {
      padding: 0.75rem;
      color: #172554;
      background: #eff6ff;
      border-radius: 0.75rem;
    }

## Next stepsCopy Anchor Link

  * [Slots](https://docs.copilotkit.ai/angular/custom-look-and-feel/slots): replace a part of the chat with your own component.



How is this guide?

GoodBad

[Previous PagePrebuilt Components](https://docs.copilotkit.ai/angular/prebuilt-components)[Next PageSlots (Subcomponents)](https://docs.copilotkit.ai/angular/custom-look-and-feel/slots)
