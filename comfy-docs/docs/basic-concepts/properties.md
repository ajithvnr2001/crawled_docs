---
url: https://docs.comfy.org/basic-concepts/properties/
title: ComfyUI Properties: Widgets, Inputs, and Data Types - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:18.551237+00:00
---

# ComfyUI Properties: Widgets, Inputs, and Data Types - ComfyUI

> Source: https://docs.comfy.org/basic-concepts/properties/

## On this page

  * Nodes are containers for properties
  * Data types



Basic Concepts

# ComfyUI Properties: Widgets, Inputs, and Data Types

Copy pageCopy page

Learn how node properties work in ComfyUI: widgets for manual control, input slots for connections, and the data types that keep a node graph valid.

Copy pageCopy page

## 

​

Nodes are containers for properties

Nodes usually have _**properties**_. Also known as _**parameters**_ or _**attributes**_ , node properties are variables that can be changed. Some properties can be adjusted manually by the user, using a data entry field called a _**widget**_. Other properties can be driven automatically by other nodes connected to the property _**input slot**_ or port. Usually, a property can be converted from widget to input and vice versa, allowing users to control property values manually or automatically. Properties can take many forms and hold many different types of information. For example, a **Load Checkpoint** node has a single property: the file path to the generative model checkpoint file. A **KSampler** node has multiple properties such as the number of sampling **steps** , **CFG** scale, **sampler_name** , etc. ![node properties](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2121d646aef4f1386f1f09162312785b)

## 

​

Data types

Information can come in many different forms, called _**data types**_. For example, alphanumeric text is known as a _**string**_ , a whole number is an _**integer**_ , and a number with a decimal point is known as a _**floating point**_ number or _**float**_. New data types are always being added to ComfyUI. ComfyUI is written in the Python scripting language, which is very forgiving about data types. By contrast, the ComfyUI environment is very _**strongly typed**_. This means that different data types can’t be mixed up. For example, we can’t connect an image output to an integer input. This is a huge benefit to users, guiding them to proper workflow construction and preventing program errors.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/basic-concepts/properties.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/basic-concepts/properties)

[Custom NodesPrevious](https://docs.comfy.org/basic-concepts/custom-nodes)[ComfyUI Links: How Node Connections WorkNext](https://docs.comfy.org/basic-concepts/links)

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
