---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/ios/rtk-label/
title: RtkLabel \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:57:18.676198+00:00
---

# RtkLabel · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/ios/rtk-label/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /iOS
  5. /RtkLabel



# RtkLabel

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitializer parametersUsage Examples Basic Usage With custom appearance

A themed label that uses design token colors and fonts from the RTK Design System.

## Initializer parameters

Parameter | Type | Required | Default | Description  
---|---|---|---|---  
`appearance` | `RtkTextAppearance` | ❌ | - | Text appearance configuration for font and color  
  
## Usage Examples

### Basic Usage
    
    
    import RealtimeKitUI
    
    let label = RtkLabel()
    label.text = "Meeting Room"
    view.addSubview(label)

### With custom appearance
    
    
    import RealtimeKitUI
    
    let appearance = RtkTextAppearance(
        font: UIFont.systemFont(ofSize: 16, weight: .semibold),
        textColor: .white
    )
    let label = RtkLabel(appearance: appearance)
    label.text = "Meeting Room"
    view.addSubview(label)

[PreviousRtkJoinButton](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/ios/rtk-join-button/)[NextRtkLeaveDialog](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/ios/rtk-leave-dialog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/ios/rtk-label.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
