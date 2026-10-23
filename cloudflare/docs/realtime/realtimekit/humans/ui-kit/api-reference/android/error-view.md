---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/error-view/
title: RtkErrorView \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:48.323041+00:00
---

# RtkErrorView · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/error-view/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans[Build using UI Kit](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/)Component Reference

  4. /Android
  5. /RtkErrorView



# RtkErrorView

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMethodsUsage Examples Basic Usage With Methods

A full-screen error view that displays an error message and a retry button.

## Methods

Method | Parameters | Description  
---|---|---  
`refresh` | `errorMessage: String, onRetryClicked: () -> Unit` | Set the error message and retry button callback  
  
## Usage Examples

### Basic Usage
    
    
    <com.cloudflare.realtimekit.ui.view.RtkErrorView
        android:id="@+id/rtk_error_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

### With Methods
    
    
    val errorView = findViewById<RtkErrorView>(R.id.rtk_error_view)
    errorView.refresh("Failed to connect") {
        // Retry connection
    }

[PreviousRtkDesignTokens](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/design-tokens/)[NextRtkGridPaginatorView](https://developers.cloudflare.com/realtime/realtimekit/humans/ui-kit/api-reference/android/grid-paginator/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/ui-kit/api-reference/android/error-view.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
