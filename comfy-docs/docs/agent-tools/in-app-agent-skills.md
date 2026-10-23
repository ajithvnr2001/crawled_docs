---
url: https://docs.comfy.org/agent-tools/in-app-agent-skills/
title: Comfy Agent Skills - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:05.671891+00:00
---

# Comfy Agent Skills - ComfyUI

> Source: https://docs.comfy.org/agent-tools/in-app-agent-skills/

## On this page

  * What is a personal skill?
  * Create a skill in chat
  * Use a skill
  * Update or delete a skill
  * Save an existing skill file
  * Use a public skill
  * Built-in guidance and coding-agent skills



Comfy Agent

# Comfy Agent Skills

Copy pageCopy page

Use personal and public skills to give Comfy Agent reusable instructions for your work.

Copy pageCopy page

## 

​

What is a personal skill?

A personal skill is a reusable set of instructions for Comfy Agent. It includes a name, a one-line description of when to use it, and the instructions themselves. Use personal skills to repeat instructions such as “make square images,” “use a white background,” or “check node connections before running.” Personal skills are saved to your account. The Agent loads a skill when its description matches your request or when you ask for it by name.

## 

​

Create a skill in chat

Tell the Agent what to save, what to call it, and when it should be used:

> Save this as a skill called product-shot: When I ask for a product image, use a square 1024 × 1024 canvas, a neutral gray background, and a Save Image node. Validate the workflow before running it.

The Agent saves the skill for future messages. A new or updated skill takes effect with your next message.

## 

​

Use a skill

Ask for a skill by name:

> Use my product-shot skill to create a studio photo workflow for a red sneaker.

The Agent can also select a skill automatically when your request matches its description.

## 

​

Update or delete a skill

Use the same skill name to replace its instructions:

> Update my product-shot skill to use a white background and a 1536 × 1536 canvas.

Delete a skill by name:

> Delete my product-shot skill.

## 

​

Save an existing skill file

Paste the contents of your `SKILL.md` file into chat and ask the Agent to save it as a personal skill. The Agent reads its name and description from the header at the top of the file. The saved skill is available from your next message.

## 

​

Use a public skill

Public skills are shared skills anyone can use, not just the ones you created. Ask for a public skill by name or describe what you want to do, and the Agent uses it the same way it uses one of your own:

> Use the product-shot public skill for a red sneaker on a neutral gray background.

## 

​

Built-in guidance and coding-agent skills

Comfy Agent includes guidance for building workflows and choosing models. Personal and public skills add instructions for repeated tasks on top of that guidance. [Skills for coding agents](https://docs.comfy.org/agent-tools/skills) are installed separately in tools such as Claude Code. Installing one there does not add it to Comfy Agent. Keep API keys, passwords, and access tokens out of skill instructions. For data handling, see [Data and privacy](https://docs.comfy.org/agent-tools/in-app-agent-data-privacy#skills-and-guidance).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/agent-tools/in-app-agent-skills.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/agent-tools/in-app-agent-skills)

[Get Started with Comfy AgentPrevious](https://docs.comfy.org/agent-tools/in-app-agent-installation)[Comfy Agent Data and PrivacyNext](https://docs.comfy.org/agent-tools/in-app-agent-data-privacy)

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
