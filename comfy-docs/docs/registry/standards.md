---
url: https://docs.comfy.org/registry/standards/
title: Comfy Registry Node Quality and Security Standards - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:12.681754+00:00
---

# Comfy Registry Node Quality and Security Standards - ComfyUI

> Source: https://docs.comfy.org/registry/standards/

## On this page

  * Base Standards
    * 1\. Community Value
    * 2\. Node Compatibility
    * 3\. Legal Compliance
    * 5\. Quality Requirements
    * 6\. Fork Guidelines
  * Security Standards
    * eval/exec Calls
    * Policy
    * Reasoning
    * subprocess for pip install
    * Policy
    * Reasoning
    * Code Obfuscation
    * Policy
    * Reasoning



Package & Publish

# Comfy Registry Node Quality and Security Standards

Copy pageCopy page

Security and other standards for publishing to the Registry

Copy pageCopy page

## 

​

Base Standards

### 

​

1\. Community Value

Custom nodes must provide valuable functionality to the ComfyUI community Avoid:

  * Excessive self-promotion
  * Impersonation or misleading behavior
  * Malicious behavior
  * Self-promotion is permitted only within your designated settings menu section
  * Top and side menus should contain only useful functionality



### 

​

2\. Node Compatibility

Do not interfere with other custom nodes’ operations (installation, updates, removal)

  * For dependencies on other custom nodes: 
    * Display clear warnings when dependent functionality is used
    * Provide example workflows demonstrating required nodes



### 

​

3\. Legal Compliance

Must comply with all applicable laws and regulations

### 

​

5\. Quality Requirements

Nodes must be fully functional, well documented, and actively maintained.

### 

​

6\. Fork Guidelines

Forked nodes must:

  * Have clearly distinct names from original
  * Provide significant differences in functionality or code

Below are standards that must be met to publish custom nodes to the registry.

## 

​

Security Standards

Custom nodes should be secure. We will start working with custom nodes that violate these standards to be rewritten. If there is some major functionality that should be exposed by core, please request it in the [rfcs repo](https://github.com/comfy-org/rfcs).

### 

​

eval/exec Calls

#### 

​

Policy

The use of `eval` and `exec` functions is prohibited in custom nodes due to security concerns.

#### 

​

Reasoning

These functions can enable arbitrary code execution, creating potential Remote Code Execution (RCE) vulnerabilities when processing user inputs. Workflows containing nodes that pass user inputs into `eval` or `exec` could be exploited for various cyberattacks, including:

  * Keylogging
  * Ransomware
  * Other malicious code execution



### 

​

subprocess for pip install

#### 

​

Policy

Runtime package installation through subprocess calls is not permitted.

#### 

​

Reasoning

  * First item ComfyUI manager will ship with ComfyUI and lets the user install dependencies
  * Centralized dependency management improves security and user experience
  * Helps prevent potential supply chain attacks
  * Eliminates need for multiple ComfyUI reloads



### 

​

Code Obfuscation

#### 

​

Policy

Code obfuscation is prohibited in custom nodes.

#### 

​

Reasoning

Obfuscated code:

  * Impossible to review and likely to be malicious



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/standards.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/standards)

[Claim My NodePrevious](https://docs.comfy.org/registry/claim-my-node)[Custom Node CI/CDNext](https://docs.comfy.org/registry/cicd)

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
