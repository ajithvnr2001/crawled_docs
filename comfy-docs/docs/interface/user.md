---
url: https://docs.comfy.org/interface/user/
title: Account Management - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:03.417762+00:00
---

# Account Management - ComfyUI

> Source: https://docs.comfy.org/interface/user/

## On this page

  * ComfyUI Version Requirements
  * Network Requirements
  * How to Log In
  * Login Methods
  * Post-Login Status
  * Frequently Asked Questions



Account & credits

# Account Management

Copy pageCopy page

Sign in to ComfyUI from Settings → User: email, Google, GitHub, or API Key. After login, Plan & Credits appears under Workspace.

Copy pageCopy page

The settings described on this page are located in the **ComfyUI in-app settings menu**. You can open it by navigating to **Settings** (gear icon) or using the `Ctrl + ,` keyboard shortcut, then select the corresponding category to view and configure these options.

Partner Nodes and Cloud billing need a signed-in ComfyUI account. Sign in from **Settings → User** (under the **General** group). After login, **Settings → Workspace → Plan & Credits** appears for balance and top-up — see [Plan & Credits](https://docs.comfy.org/interface/credits). Currently, we support the following login methods:

  * Email login
  * Google login
  * Github login
  * API Key login (for non-whitelisted site authorization)

We will provide relevant login requirements and explanations in this document.

## 

​

ComfyUI Version Requirements

You may need to use at least [ComfyUI v0.3.0](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.3.30) to use the account system. Ensure that the corresponding frontend version is at least `1.17.11`. Sometimes the frontend may fail to install and revert to an older version, so please check if the frontend version is greater than `1.17.11` in `Settings` -> `About`. In some regions, network restrictions may prevent normal access to the login API, causing timeouts or failures. Before logging in, please **ensure that your network environment does not restrict access to the corresponding API** , and make sure you can access sites like Google or Github.

Since we are still in rapid iterative updates, related functions may change. If there are no special circumstances, please try to update to the latest version to get support for relevant functions.

## 

​

Network Requirements

To login to ComfyUI account, you must be in a secure network environment:

  * Only allow access from `127.0.0.1` or `localhost`.
  * Do not support using the `--listen` parameter to access the Partner Node through a local network.
  * If you are using a non-SSL certificate or a site that does not start with `https`, you may not be able to successfully log in.
  * You may not be able to log in on a site that is not in our whitelist (but you can log in using an API Key now).
  * Ensure you can connect to our service normally (some regions may require a proxy).



## 

​

How to Log In

Log in via **Settings → User** : ![ComfyUI User Interface](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/user.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4aacfc636460e073d16ef1fdaccb0888)

## 

​

Login Methods

![user-login](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user-login.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=70d1bb2128baed57bcd3d87d0744eb46) If this is your first login, please create an account first.

## Logging in with an API Key

For non-whitelisted sites or LAN environments, you can use API Key login. See the detailed guide in the account login documentation.

## 

​

Post-Login Status

After logging in, the top menu shows your account control. From there you can reopen the user panel, sign out, and on Cloud open **Manage plan** (same **Plan & Credits** panel as **Settings → Workspace → Plan & Credits**). ![user-logged](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/user-logged.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=82fd894f75b3cdcf9c6e029bdab62b7c) ![menu-user-logged](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/menu-user-logged.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=949118faed113120dd12b35bb4536075)

## 

​

Frequently Asked Questions

Are there any login device restrictions?

We do not restrict login devices. You can log in to your account on any device, but please note that your account information may be accessed by other devices, so do not log in to your account on public devices.

How to log in in a LAN environment?

Currently, only API Key login is supported in a LAN environment. If you are accessing ComfyUI services through a LAN, please use API Key to log in.

Why can't I log in on some websites?

Our login service has a whitelist, so you may not be able to log in to ComfyUI deployed on some servers, for this case, you can use API Key login to solve it.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/user.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/user)

[ComfyUI About Page: Version Badges and System InfoPrevious](https://docs.comfy.org/interface/settings/about)[Plan & CreditsNext](https://docs.comfy.org/interface/credits)

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
