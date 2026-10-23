---
url: https://docs.comfy.org/tutorials/partner-nodes/data-retention/
title: Partner Node Data Retention - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:28.395483+00:00
---

# Partner Node Data Retention - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/data-retention/

## On this page

  * What gets stored
  * How long files are kept
  * What happens after deletion
  * Keeping files longer
  * Reference



Partner Nodes

# Partner Node Data Retention

Copy pageCopy page

How Comfy stores and deletes Partner Node inputs and outputs, and how long media files are retained.

Copy pageCopy page

Every Partner Node request produces data that is stored on our platform: inputs (images, videos, 3D assets, audio), and outputs produced by the model. This page explains how long each kind of data is retained. Where each provider processes that data by default is tracked separately on the [Model Providers](https://docs.comfy.org/tutorials/partner-nodes/model-providers).

## 

​

What gets stored

When you run a Partner Node, two kinds of files are stored:

  * **Input files** : reference images, audio, and other media you provide to a node. Inputs are uploaded to your account’s storage space.
  * **Output files** : the images, videos, audio, and other media a node generates. Outputs are written to Comfy-managed storage and returned to you as download URLs.

Both input and output files are stored in Comfy-managed cloud storage buckets.

## 

​

How long files are kept

All Partner Node media files are automatically deleted **24 hours** after they are created. The deletion applies to both input and output files.

File type| Deleted after  
---|---  
Input files| 24 hours  
Output files| 24 hours  
  
The 24-hour deletion window is a platform default and applies to all Partner Node calls. If you need to keep files longer, download them to your own storage before they expire.

## 

​

What happens after deletion

Once a file is deleted, its download URL returns an error. Deleted files cannot be recovered, and the same media must be re-uploaded or regenerated if you need it again. Deleting an input file also removes the corresponding file record from your account storage, so the input cannot be reused by later calls.

## 

​

Keeping files longer

If your workflow needs an input file to remain available for longer than 24 hours, re-upload the file before each job. For long-running pipelines, re-upload right before the call that needs it. For outputs you want to keep, download them to your own storage within the 24-hour window.

## 

​

Reference

Item| Value  
---|---  
Input file retention| 24 hours  
Output file retention| 24 hours  
  
For general information about how Comfy handles customer data, see [Data Retention](https://docs.comfy.org/support/data-retention).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/data-retention.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/data-retention)

[FAQs about Partner NodesPrevious](https://docs.comfy.org/tutorials/partner-nodes/faq)[Model provider verification, licensing, and data residencyNext](https://docs.comfy.org/tutorials/partner-nodes/model-providers)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
