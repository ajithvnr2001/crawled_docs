---
url: https://docs.copilotkit.ai/slack/ms-agent-python/render-and-carousel/
title: Slack + MS Agent Framework (Python): Render and carousel
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:09.382812+00:00
---

# Slack + MS Agent Framework (Python): Render and carousel

> Source: https://docs.copilotkit.ai/slack/ms-agent-python/render-and-carousel/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/ms-agent-python)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/ms-agent-python/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/ms-agent-python/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/ms-agent-python/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/ms-agent-python/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/ms-agent-python/rich-messages)[Posting JSX as images](https://docs.copilotkit.ai/slack/ms-agent-python/posting-jsx-as-images)[Render and carousel](https://docs.copilotkit.ai/slack/ms-agent-python/render-and-carousel)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/ms-agent-python/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/ms-agent-python/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/ms-agent-python/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/ms-agent-python/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/ms-agent-python/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/ms-agent-python/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/ms-agent-python/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Build

# Render and carousel

Mix native channel UI with React snapshots in one message using Render and Carousel.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

You want native text plus React cards in one message. A header, a sale note, and a Buy button sit next to a product card that your app already draws in React.

Wrap each snapshot in `<Render alt>`. Group the slides in `<Carousel>`. The SDK draws each snapshot to a PNG and keeps the rest as native channel UI.
    
    
    <Message>
      <Header>This week</Header>
      <Carousel>
        <CarouselCard>
          <Header>Shoes</Header>
          <Render alt="Red shoes" width={400}>
            <ProductCard product={shoes} />
          </Render>
          <Section>On sale</Section>
          <Button
            value="buy-shoes"
            onClick={async ({ thread }) => {
              await thread.post("Added the red shoes to your cart.");
            }}
          >
            Buy
          </Button>
        </CarouselCard>
        <Render alt="Hat">
          <ProductCard product={hat} />
        </Render>
      </Carousel>
    </Message>

`alt` is required and must not be blank on `<Render>`. Its canvas inherits `render.width` and `render.height`, defaulting to 720 by 480 pixels. Set `width` and `height` on an individual `<Render>` to override them.

`<Image url>` is still a public URL image. It does not take children. Inside a carousel, supply both a URL and nonblank `alt` text. A carousel accepts 1 to 10 slides; each `<CarouselCard>` allows one header, one section, one image or snapshot, and up to three native buttons.

Use `thread.post()` or `thread.update()` for messages containing `<Render>`. These native messages keep normal message references and button callbacks. Ephemeral snapshots are unsupported: `thread.postEphemeral()` rejects `<Render>` before posting.

No Channels Button inside Render

A Channels `<Button>` inside `<Render>` throws. A host HTML button is fine. The snapshot is a PNG, so that HTML button does not receive clicks.

Set the renderer, fonts, and styles once on `createChannel({ render })`. `<Render>` needs `render.renderer`, the same as an image post. See [Posting JSX as images](https://docs.copilotkit.ai/slack/ms-agent-python/posting-jsx-as-images).

The Slack example posts this mix with `/carousel` or by asking the bot to show a carousel (`render_carousel` in `examples/slack`).

This feature targets managed Slack and Teams:

  * **Slack:** the SDK stores each PNG and puts its file handle in `slack_file.id`. Intelligence stages the image in Slack before posting the native message or carousel. Native buttons keep their action callbacks.
  * **Teams:** the SDK embeds snapshots as data URIs in an Adaptive Card. The complete delivery packet, including all images, text, and actions, must fit the existing **64 KiB** limit. Oversized cards fail with an error explaining the limit. Reduce the snapshot dimensions, use public `<Image url>` images, or post a larger snapshot separately with `thread.post(jsx)`, which uses the managed upload path.



Run `pnpm channel` in `examples/slack` for the managed example. Existing direct adapters and Discord and WhatsApp behavior are unchanged.

Managed platform| Carousel output  
---|---  
Slack| Native carousel with interactive buttons  
Teams| Adaptive Card carousel with interactive actions
