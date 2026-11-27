---
url: https://docs.fish.audio/developer-guide/integrations/n8n/
title: n8n - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-27T17:34:39.026607+00:00
---

# n8n - Fish Audio

> Source: https://docs.fish.audio/developer-guide/integrations/n8n/

## On this page

Back to top

  * Installation
  * Configuration
  * Features
  * Workflow templates
  * Resources



Integrations

# n8n

Copy pageCopy page

Automate workflows with Fish Audio and n8n

Copy pageCopy page

[n8n](https://n8n.io/) is a fair-code licensed workflow automation platform. The Fish Audio community node brings text-to-speech, speech-to-text, and voice cloning capabilities to your n8n workflows.

## Installation

On self-hosted n8n, install from n8n community nodes:

  1. Go to **Settings** > **Community Nodes**
  2. Select **Install**
  3. Enter `@fishaudio/n8n-nodes-fishaudio`
  4. Accept the risks and install

See the [n8n community nodes guide](https://docs.n8n.io/integrations/community-nodes/installation/) for details. On n8n Cloud, an instance owner or admin opens the nodes panel, searches for **Fish Audio** , and installs the node from there. n8n Cloud offers only the community nodes and versions that n8n has verified, so the node there can be an earlier version, published under the previous name `n8n-nodes-fishaudio`.

The package was previously published as `n8n-nodes-fishaudio`. Workflows that use it keep working. To switch a workflow to `@fishaudio/n8n-nodes-fishaudio`, see [Move from n8n-nodes-fishaudio](https://github.com/fishaudio/fish-audio-n8n#move-from-n8n-nodes-fishaudio).

## Configuration

  1. Go to **Credentials** > **Add Credential**
  2. Search for “Fish Audio API”
  3. Enter your API key from [fish.audio/app/api-keys](https://fish.audio/app/api-keys)



## Features

The node supports:

  * **Text-to-Speech** : Generate audio from text using any voice model. Choose the model: new nodes use `s2.1-pro`, and `s2.1-pro-free` and `drama-3` are also in the list. Under **Additional Options** , **Language** sets the language used to read out numbers, dates, units and symbols while **Normalize Text** is on; see [Supported normalization languages](https://docs.fish.audio/features/text-to-speech#supported-normalization-languages).
  * **Speech-to-Text** : Transcribe audio files. New nodes use `transcribe-1-pro`.
  * **Voice Models** : List, get, create, and delete custom voices
  * **Account** : Check credit balance

The node is also available as an AI tool for use with n8n’s AI Agent nodes. When a request fails and stops the workflow, the error’s description shows the Fish Audio trace ID and error code if the API returned them. Include them when you contact support. With **Continue On Fail** , the output item carries only the error message, and older n8n versions that drop the API response from the error do not show these details. These model choices, the **Language** option, and the trace ID in errors require version 0.5.0 or later of the node.

## Workflow templates

The node’s repository has [workflow templates](https://github.com/fishaudio/fish-audio-n8n#workflow-templates) you can import: a text-to-speech webhook, a form that transcribes an uploaded recording, and a form that re-voices a recording. They need `@fishaudio/n8n-nodes-fishaudio` 0.5.0 or later.

## Resources

  * [npm package](https://www.npmjs.com/package/@fishaudio/n8n-nodes-fishaudio)
  * [GitHub](https://github.com/fishaudio/fish-audio-n8n)
  * [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/integrations/n8n.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/integrations/n8n)

[LiveKit](https://docs.fish.audio/developer-guide/integrations/livekit)[Telnyx](https://docs.fish.audio/developer-guide/integrations/telnyx)
