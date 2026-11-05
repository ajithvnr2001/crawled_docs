---
url: https://developers.cloudflare.com/realtime/realtimekit/platform/pricing/
title: Pricing \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:08.252086+00:00
---

# Pricing · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /[Platform](https://developers.cloudflare.com/realtime/realtimekit/platform/)
  5. /Pricing



# Pricing

Last updated Nov 5, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAI usage and Workers AI

RealtimeKit usage is charged according to the pricing model below:

Note

RealtimeKit participant and export usage is measured in minutes. In contrast, Realtime SFU, MoQ Relay, and TURN usage is measured in GB of egress. RealtimeKit transcription and summarization use Workers AI pricing.

To estimate your RealtimeKit costs, refer to the [RealtimeKit pricing calculator ↗︎](https://realtime.cloudflare.com/#pricing-calculator).

The included usage applies to all accounts, including Free and Enterprise accounts.

Feature | Included per month | Price after included usage  
---|---|---  
Audio/Video Participant | 10,000 minutes | $0.002 / minute  
Audio-Only Participant | 10,000 minutes | $0.0005 / minute  
Export (recording, RTMP or HLS streaming) | 100 minutes | $0.010 / minute  
Export (recording, RTMP or HLS streaming, audio only) | 100 minutes | $0.003 / minute  
Export (Raw RTP) into R2 | 100 minutes | $0.0005 / minute  
Transcription and summarization | See [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) | Standard model pricing via Workers AI  
  
Whether a participant is an audio-only participant or an audio/video participant is determined by the `Meeting Type` of their [preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).

## AI usage and Workers AI

RealtimeKit uses [Workers AI](https://developers.cloudflare.com/workers-ai/) for transcription and meeting summarization. This usage is billed to your Cloudflare account under [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/), separately from RealtimeKit participant and export usage.

Workers AI includes 10,000 free Neurons per day across your account. To continue using transcription and summarization beyond this daily allowance, subscribe to the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers). Workers Paid includes the same daily allowance and charges for additional usage.

RealtimeKit uses [Deepgram Nova-3](https://developers.cloudflare.com/workers-ai/models/nova-3/) for real-time transcription and [Whisper Large v3 Turbo](https://developers.cloudflare.com/workers-ai/models/whisper-large-v3-turbo/) for post-meeting transcription. For model rates and how usage is measured, refer to [transcription billing and Free plan limits](https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#billing-and-free-plan-limits).

Monitor Neuron usage in the [Workers AI dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/ai/workers-ai). Eligible accounts can also view usage and charges under **Manage Account** > **Billing** > **Billable Usage**. The [billable usage dashboard](https://developers.cloudflare.com/billing/manage/billable-usage/) is not available to Enterprise contract accounts.

[PreviousOverview](https://developers.cloudflare.com/realtime/realtimekit/platform/)[NextLimits](https://developers.cloudflare.com/realtime/realtimekit/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
