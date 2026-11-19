---
url: https://docs.copilotkit.ai/reference/channels/components/Table/
title: Table, Row, and Cell
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:33.494176+00:00
---

# Table, Row, and Cell

> Source: https://docs.copilotkit.ai/reference/channels/components/Table/

Channels/Components

# Table, Row, and Cell

Render tabular data with portable Channels table primitives.

Copy MarkdownOpen

`Table` groups `Row` and `Cell` children.

Copy Text
    
    
    import { Cell, Row, Table } from "@copilotkit/channels/ui";
    
    <Table
      columns={[
        { header: "Service", align: "left" },
        { header: "p95", align: "right" },
      ]}
    >
      <Row>
        <Cell>Checkout</Cell>
        <Cell>1.8s</Cell>
      </Row>
    </Table>;

## PropsCopy Anchor Link

Component| Prop| Type| Description  
---|---|---|---  
`Table`| `columns`| `{ header: string; align?: "left" | "center" | "right" }[]`| Optional header and alignment metadata.  
`Table`| `children`| `BotChildren`| `Row` children.  
`Row`| `children`| `BotChildren`| `Cell` children.  
`Cell`| `children`| `BotChildren`| Cell text.  
  
Managed Slack renders a native table block. Managed Teams renders an Adaptive Card 1.5 table. Both renderers clamp rows, columns, and cell text to provider budgets. Keep a short textual summary outside the table for clients that cannot display the native structure.

How is this guide?

GoodBad

[Previous PageSelect](https://docs.copilotkit.ai/reference/channels/components/Select)[Next Pagebind](https://docs.copilotkit.ai/reference/channels/functions/bind)
