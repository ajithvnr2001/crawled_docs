---
url: https://docs.comfy.org/custom-nodes/js/node-id-migration/
title: Node ID Migration for Frontend Extensions - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T14:55:22.543223+00:00
---

# Node ID Migration for Frontend Extensions - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/node-id-migration/

Migration Guides

# Node ID Migration for Frontend Extensions

Copy pageCopy page

Migrate ComfyUI frontend extensions to branded string node IDs and the string subgraph boundary sentinels SUBGRAPH_INPUT_ID and SUBGRAPH_OUTPUT_ID.

Copy pageCopy page

ComfyUI frontend now normalizes local node IDs to the branded `NodeId` string type at internal boundaries. Serialized workflows and API payloads may still contain numeric IDs, but node IDs in litegraph, such as `node.id`, `LLink.origin_id` and `LLink.target_id`, should be treated as strings after they enter the frontend. Link IDs (`LLink.id`) and reroute IDs remain numbers. Extension authors should avoid numeric comparisons against node IDs. In particular, subgraph boundary sentinels are exposed as branded string IDs:

  * `SUBGRAPH_INPUT_ID` serializes from `-10`
  * `SUBGRAPH_OUTPUT_ID` serializes from `-20`

Compare against the strings `'-10'` and `'-20'`, or normalize both sides to strings before comparing legacy values.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/node-id-migration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/node-id-migration)

[Context menu migration](https://docs.comfy.org/custom-nodes/js/context-menu-migration)[Link registration migration](https://docs.comfy.org/custom-nodes/js/link-registration-migration)
