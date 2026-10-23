---
url: https://docs.comfy.org/cloud/workspace/
title: Comfy Cloud workspaces: teams and members - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:05.796617+00:00
---

# Comfy Cloud workspaces: teams and members - ComfyUI

> Source: https://docs.comfy.org/cloud/workspace/

## On this page

  * Overview
  * Personal and Team workspaces
  * What is separate per workspace
  * Create a team workspace
  * Invite members
  * Roles and permissions
  * Manage a workspace
    * Delete a team workspace
  * Switch workspaces
  * How workspaces are billed
  * FAQ



Cloud Exclusive

# Comfy Cloud workspaces: teams and members

Copy pageCopy page

Create and manage Comfy Cloud workspaces: create a team workspace, invite members, set roles and permissions, and share files, workflows, and credits.

Copy pageCopy page

This is a **Comfy Cloud** feature and is only available in the cloud version. To learn more about Comfy Cloud, see [Comfy Cloud](https://docs.comfy.org/get_started/cloud).

## 

​

Overview

A workspace is the account boundary for your Comfy Cloud work. Workflows, uploaded files, outputs, and credits belong to the workspace rather than to a single user, so switching workspaces switches which files you see and which credits your runs spend. Every user gets a **Personal** workspace. To work with other people, create a **Team** workspace and invite them. If someone invited you to a team workspace, you do not need to create anything: open the invitation email, sign in with the address it was sent to, and switch to that workspace. See Switch workspaces.

## 

​

Personal and Team workspaces

Type| What it is  
---|---  
**Personal**|  Created automatically for every user, with a single seat. Only you can access it. It cannot be deleted, and you cannot leave it.  
**Team**|  A shared workspace that you create or are invited to. Members see the workspace’s files and share its credits.  
  
Creating a team workspace is free. To invite people, the workspace needs seats: a workspace that is not on a Team plan has one seat, which belongs to its owner. Team plans include a seat for each member.

## 

​

What is separate per workspace

Each workspace keeps its own:

  * **Files and outputs** : uploads, generated images, jobs, and history
  * **Workflows** : the workflow library you see in that workspace
  * **Plan and credits** : its own subscription and credit balance
  * **People** : members, roles, and pending invitations
  * **Access** : workspace API keys, and, on Enterprise workspaces, the partner models members can run

Switching workspaces switches all of these at once, and nothing is copied between workspaces automatically.

## 

​

Create a team workspace

1

Open the profile menu

Click your profile picture in the top right corner.

2

Open the workspace list

Click your workspace name in the menu. The list shows every workspace you belong to, with your role in it.![The workspace list, with Create a workspace at the bottom](https://mintcdn.com/dripart/_STmcLe16Xze8EdG/images/cloud/workspace/workspace-list.png?fit=max&auto=format&n=_STmcLe16Xze8EdG&q=85&s=9ec3540859ff51ece9770e4e20c64a87)

3

Create the workspace

Click **Create a workspace** at the bottom of the list.

4

Name it

Enter a name and click **Create**. Names are 1 to 50 characters long, must start with a letter or number, and can contain letters, numbers, spaces and the characters `- _ ' . , ( ) & +`.![The Create a new workspace dialog](https://mintcdn.com/dripart/_STmcLe16Xze8EdG/images/cloud/workspace/create-workspace.png?fit=max&auto=format&n=_STmcLe16Xze8EdG&q=85&s=badc3c2b42a5c6b91ddaf9b13c2e6560)

Comfy Cloud switches you to the new workspace and reloads the page.

You can own up to **10 workspaces** in total, including your Personal workspace. There is no limit on how many workspaces you can join as a member.

To open your workspace list directly, add `?create_workspace=1` to the Comfy Cloud URL, for example `https://cloud.comfy.org/?create_workspace=1`. It opens the team workspaces dialog, which lists your workspaces and has a **New workspace** field and a **Create workspace** button.

## 

​

Invite members

Only workspace owners can invite members. Team plans include a seat for each member, and the **Members** tab shows how many seats are in use, for example `3 of 20 members`. Pending invitations count toward that limit. A workspace can hold up to 50 members today; if you need more, [contact support](https://support.comfy.org/). ![The Members section of workspace settings, with the Invite button](https://mintcdn.com/dripart/_STmcLe16Xze8EdG/images/cloud/workspace/workspace-members.png?fit=max&auto=format&n=_STmcLe16Xze8EdG&q=85&s=3873c85c8a37fd3a019da1f944b2e995) To invite members:

1

Open workspace settings

In the profile menu, click **Workspace settings**.

2

Open the Members section

Select **Members**.

3

Send the invites

Click **Invite** , type one or more email addresses separated by commas, then click **Invite** in the dialog.

![The Invite members dialog with two email addresses entered](https://mintcdn.com/dripart/_STmcLe16Xze8EdG/images/cloud/workspace/invite-members.png?fit=max&auto=format&n=_STmcLe16Xze8EdG&q=85&s=c252284d37c35df8acbc1c0f9d5bdae2)

If **Invite** does not open the dialog, the workspace has no free seat. A workspace that is not on a Team plan has one seat, and a full team shows a maximum-members tooltip. Open **Plan & Credits** and upgrade to a Team plan, or contact us about Enterprise if you need more members.

Comfy Cloud emails each person a link to join. The invitation is tied to the address it was sent to, so the recipient has to sign in, or create an account, with that same address. If they are not signed in when they open the link, they are asked to sign in first, and the invitation is applied afterwards. Invitations that have not been accepted yet appear in the **Pending** tab of the Members section, with their expiry date. Owners see this tab; members only see the list of people who have already joined. From there an owner can:

  * **Copy invite link** : share the link directly instead of waiting for the email
  * **Resend invite** : send the email again with a fresh link
  * **Cancel invite** : revoke the invitation

Invitations expire 30 days after they are sent. ![Pending invitations with their invite and expiry dates](https://mintcdn.com/dripart/_STmcLe16Xze8EdG/images/cloud/workspace/pending-invites.png?fit=max&auto=format&n=_STmcLe16Xze8EdG&q=85&s=253ffad2ebe7b7271bd5ef724c042dfe)

## 

​

Roles and permissions

Role| Can do  
---|---  
**Owner**|  Invite and remove members, change roles, rename or delete the workspace, and manage the workspace plan and credits.  
**Member**|  Run workflows in the workspace and view the member list. Cannot invite members, see pending invitations, change workspace settings, or manage billing.  
  
Owners can change a member’s role from the Members section, which is how you promote a member to owner or demote an owner back to member. A workspace always keeps at least one owner, so the last remaining owner cannot be demoted or removed. Some messages in Comfy Cloud call the owner the workspace admin; they are the same role. Members can open **Workspace settings** and see the workspace’s plan and member list, but they cannot change anything there. When an owner removes a member, that person loses access to the workspace’s files and workflows, the seat is freed, and any workspace API keys they created stop working. Members cannot remove themselves; they leave the workspace instead.

## 

​

Manage a workspace

Open **Workspace settings** from the profile menu. The **Workspace** group in the settings dialog has these sections:

  * **Plan & Credits**: the workspace plan, credit balance, and top-ups. Only the owner can change these.
  * **Members** : the member list, roles, and pending invitations. Pending invitations are visible to owners.
  * **Partner Models** : shown to workspace owners. Restricting which provider models members can run is an Enterprise plan feature. Turn off **Allow all partner models** to choose which providers and models members can run; models added later stay disabled until you enable them. Changes can take up to 10 minutes to apply across the workspace.

The menu in the Members section lets owners:

  * **Edit workspace details** : rename the workspace
  * **Delete Workspace** : available once the workspace has no active subscription. See Delete a team workspace.
  * **Leave Workspace** : leave a team workspace. You cannot leave a workspace if you are its only owner.

![The workspace menu: Edit workspace details, Delete Workspace, Leave Workspace](https://mintcdn.com/dripart/_STmcLe16Xze8EdG/images/cloud/workspace/workspace-menu.png?fit=max&auto=format&n=_STmcLe16Xze8EdG&q=85&s=44fa6637c08fc269c1fdaff7652f9862) Members see this menu too, but only the **Leave Workspace** item.

### 

​

Delete a team workspace

Only the owner of a team workspace can delete it, and the workspace must not have an active subscription. Deleting a workspace is permanent: unused credits and unsaved assets are lost, and the workspace cannot be recovered. Your Personal workspace cannot be deleted, and Enterprise workspaces are managed with our sales team.

1

Cancel the plan

In **Workspace settings** → **Plan & Credits**, open the three-dot menu and select **Cancel plan**. If the workspace has no subscription, skip this step.

2

Delete the workspace

In **Workspace settings** → **Members** , open the three-dot menu and select **Delete Workspace** , then confirm in the dialog.

## 

​

Switch workspaces

  1. Open the profile menu.
  2. Click your workspace name to open the workspace list.
  3. Select the workspace you want to work in.

![The profile menu, where you click your workspace name to open the workspace list](https://mintcdn.com/dripart/_STmcLe16Xze8EdG/images/cloud/workspace/profile-menu.png?fit=max&auto=format&n=_STmcLe16Xze8EdG&q=85&s=3d48e5236baf4f808df5b4eefb1bc831) Comfy Cloud reloads the page on the selected workspace, and remembers it the next time you sign in.

URL parameter| Action  
---|---  
`?create_workspace=1`| Opens your workspace list, with a **New workspace** field and a **Create workspace** button  
`?invite=TOKEN`| Accepts a workspace invitation  
  
## 

​

How workspaces are billed

Plans and credits belong to the workspace, not to individual accounts. **Personal workspaces** use your own plan, and you are the only person who spends its credits. **Team workspaces** use a credit subscription that the owner sets up:

  * The owner chooses the workspace’s monthly credit amount in **Choose a Plan** (**For Teams**) with the credit slider. The price follows the amount you choose, and a larger commitment lowers the effective rate. Each billing period refills the pool with that amount.
  * Yearly commitments cost less than monthly, and the workspace receives the whole year of credits up front.
  * Members are not billed individually, and adding or removing members does not change the price. The plan includes the workspace’s seats. If you need more members than the plan includes, contact us about Enterprise.
  * Every member runs against the same credit pool.
  * Subscription credits are spent before top-up credits, and top-up credits stay valid for 12 months.
  * Changing the workspace to a personal plan removes all other members immediately, so move any shared work before you switch.

See [Comfy Cloud pricing](https://www.comfy.org/cloud/pricing) for current rates and discounts, [Subscribe to Comfy Cloud](https://docs.comfy.org/support/subscription/subscribing) to set up a team plan, and [Change your Comfy Cloud plan](https://docs.comfy.org/support/subscription/changing-plan) for plan changes.

## 

​

FAQ

Can I be in more than one team workspace?

Yes. You can own up to 10 workspaces in total, including your Personal workspace, and you can be a member of as many workspaces as you are invited to.

Do I need my own subscription to join a team workspace?

No. Members are not billed individually: runs in the workspace use the workspace’s credits, which the workspace owner manages.

What carries over when I upgrade my workspace to a Team plan?

Everything does. The upgrade applies to the workspace itself, so its workflows, models, run history, and top-up credits stay attached. The exception is unused monthly plan credits, which expire at the end of the current billing cycle because the workspace moves to a new credit allowance. Top-up credits carry over.

How do members hand work off to each other?

A Team plan shares one credit pool, one bill, and one set of owners. Sharing workflows and assets inside a workspace is still in development. Until it ships, hand work over by sharing the workflow link, exporting the workflow JSON, or dropping a Comfy-generated asset into the other member’s canvas.

The invitation email never arrived. What now?

Ask the workspace owner to use **Resend invite** , or to send you a **Copy invite link** from the **Pending** tab in the Members section. Invitations expire 30 days after they are sent, so an older invitation may need to be sent again.

Can I delete my Personal workspace?

No. Your Personal workspace is permanent and serves as your default workspace.

Can I invite someone to my Personal workspace?

No. Personal workspaces have a single seat and no member management.

What happens when I leave a team workspace?

The workspace disappears from your workspace list and you lose access to its files and workflows. Any workspace API keys you created for it stop working. Your Personal workspace and its contents are not affected.

What happens if the workspace runs out of credits?

Members cannot run workflows until the owner adds credits. The same applies when the workspace’s subscription is inactive, or a payment fails: ask the workspace owner to fix the plan or payment method.

Why is Delete Workspace unavailable?

The workspace still has an active subscription. Cancel it first with **Cancel plan** in **Plan & Credits**, then delete the workspace. **Delete Workspace** becomes available as soon as the plan is cancelled, so you do not have to wait for the billing period to end. Personal workspaces cannot be deleted at all, and Enterprise workspaces are ended through our sales team.

Can a deleted workspace be recovered?

No. Deleting a workspace is permanent.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/cloud/workspace.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/cloud/workspace)

[Plan & CreditsPrevious](https://docs.comfy.org/interface/credits)[Share workflowsNext](https://docs.comfy.org/cloud/share-workflow)

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
