---
url: https://docs.copilotkit.ai/reference/channels/components/Actions/
title: Actions
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:48.266078+00:00
---

# Actions

> Source: https://docs.copilotkit.ai/reference/channels/components/Actions/

Channels/Components

# Actions

Group portable buttons and Slack-select controls in one message action area.

Copy MarkdownOpen

`Actions` groups interactive controls.

Copy Text
    
    
    import { Actions, Button, Message, Section } from "@copilotkit/channels/ui";
    
    <Message>
      <Section>Approve this deployment?</Section>
      <Actions>
        <Button value="approve" style="primary" onClick={handleDecision}>
          Approve
        </Button>
        <Button value="deny" style="danger" onClick={handleDecision}>
          Deny
        </Button>
      </Actions>
    </Message>;

Prop| Type| Description  
---|---|---  
`children`| `BotChildren`| Interactive Channels components.  
  
Managed Slack renders an actions block. Managed Teams lifts `Button` children to the Adaptive Card's top-level actions. Use buttons for cross-provider managed workflows. A Teams Button callback receives named Adaptive Card input fields in `ctx.values`; Teams does not dispatch `Select.onSelect` or `Input.onSubmit` as independent callbacks.

How is this guide?

GoodBad

[Previous PageTranscripts](https://docs.copilotkit.ai/reference/channels/classes/Transcripts)[Next PageButton](https://docs.copilotkit.ai/reference/channels/components/Button)
