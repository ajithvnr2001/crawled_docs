---
url: https://docs.copilotkit.ai/reference/channels/components/Chart/
title: Chart
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:37.826102+00:00
---

# Chart

> Source: https://docs.copilotkit.ai/reference/channels/components/Chart/

Channels/Components

# Chart

Render Teams chart extensions with a portable Channels chart node and a Slack-safe fallback.

Copy MarkdownOpen

`Chart` describes a small numeric series.

Copy Text
    
    
    import { Chart, Message, Section } from "@copilotkit/channels/ui";
    
    <Message>
      <Section>Checkout latency rose 28% this week.</Section>
      <Chart
        type="line"
        title="p95 latency"
        yAxisTitle="milliseconds"
        data={[
          { label: "Mon", value: 780 },
          { label: "Fri", value: 998 },
        ]}
      />
    </Message>;

## PropsCopy Anchor Link

Prop| Type| Description  
---|---|---  
`type`| `"verticalBar" | "horizontalBar" | "line" | "pie" | "donut"`| Chart kind. Defaults to `verticalBar`.  
`title`| `string`| Optional chart title.  
`xAxisTitle`| `string`| Cartesian x-axis title.  
`yAxisTitle`| `string`| Cartesian y-axis title.  
`data`| `{ label: string; value: number }[]`| Required data points.  
  
Managed Teams renders Teams chart extensions in clients that support them. Managed Slack currently omits `Chart` entirely. Always include the important result in a `Section`, `Fields`, or `Table`, as the example does.

How is this guide?

GoodBad

[Previous PageButton](https://docs.copilotkit.ai/reference/channels/components/Button)[Next PageContext](https://docs.copilotkit.ai/reference/channels/components/Context)
