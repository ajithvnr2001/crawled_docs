---
url: https://docs.comfy.org/account/login/
title: Log in to your Comfy account - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:52:05.135142+00:00
---

# Log in to your Comfy account - ComfyUI

> Source: https://docs.comfy.org/account/login/

## On this page

Back to top

  * Supported login methods
  * Sign in with single sign-on (SSO)
  * Logging in on Comfy Cloud
  * Logging in locally
    * Logging in with an API Key
  * Forgot your password
  * Troubleshooting login issues
  * Security tips



Account Management

# Log in to your Comfy account

Copy pageCopy page

Sign in to ComfyUI with email, Google, GitHub, or single sign-on, on Comfy Cloud or in the local app, including API Key login for self-hosted servers.

Copy pageCopy page

Your Comfy account gives you access to [partner nodes (Partner Node)](https://docs.comfy.org/tutorials/partner-nodes/overview) and [cloud subscriptions](https://www.comfy.org/cloud), enabling you to use premium features and services across the ComfyUI platform.

## Supported login methods

ComfyUI supports the following login methods:

  * **Email** : Log in with your email address and password
  * **Google** : Log in with your Google account
  * **GitHub** : Log in with your GitHub account
  * **Single sign-on (SSO)** : Log in through your organization’s identity provider



## Sign in with single sign-on (SSO)

If your organization manages Comfy accounts through an identity provider, you sign in with **Continue with SSO** instead of an email address and password, Google, or GitHub. Single sign-on is available after your organization enables it. Until then, use email, Google, or GitHub.

  1. On the sign-in page, enter your email address, or click **Continue with SSO** first.
  2. If prompted, click **Continue with SSO**.
  3. Finish signing in on your identity provider’s page. You return to Comfy Cloud signed in.

If single sign-on is not set up, or an administrator turned it off for your organization, contact your administrator.

SSO accounts cannot sign in to the ComfyUI desktop app yet. Use the browser instead. Workspace invite links also cannot be accepted from an SSO account yet, so ask a workspace admin to add you directly.

## Logging in on Comfy Cloud

To access your Comfy account for ComfyUI on Comfy Cloud:

  1. Navigate to [Comfy Cloud](https://www.comfy.org)
  2. Click **Log in** or **Sign in**
  3. Choose your login method: 
     * **Email** : Enter your email address and password, then click **Log in**
     * **Google** : Click the Google login button and authenticate
     * **GitHub** : Click the GitHub login button and authenticate
     * **SSO** : Click **Continue with SSO** (enter your email first, or go straight to SSO) and finish on your identity provider



## Logging in locally

If you have ComfyUI installed locally:

  1. Open ComfyUI on your local machine
  2. Navigate to **Settings** in the interface
  3. Go to the **User** section (see [User settings](https://docs.comfy.org/interface/user) for details)
  4. Choose your login method: 
     * **Email** : Enter your email address and password
     * **Google** : Click the Google login button and authenticate
     * **GitHub** : Click the GitHub login button and authenticate
     * **API Key** : Use an API Key for non-whitelisted deployments (see below)

![User settings interface](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/user.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4aacfc636460e073d16ef1fdaccb0888)

### Logging in with an API Key

Since not all ComfyUI deployments are on our domain authorization whitelist, we have provided API Key login in a recent update (2025-05-10) for logging in through non-whitelisted sites. Below are the steps for logging in with an API Key:

  * Have an API Key

  * No API Key, Apply for an API Key First




1

Select Comfy API Key Login on the Login Screen

Select `Comfy API Key` login in the login popup![Select Comfy API Key Login](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda)

2

Enter Your API Key

![Enter API Key](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-2.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=df2f26ee4d89a8296496d2f1b4eff825)

  1. Enter your API Key and save it
  2. If you don’t have an API Key, click the `Get one here` link to go to the [Comfy Platform login page](https://platform.comfy.org/login) and log in to obtain it.



3

Login Successful

After a successful login, you can see the corresponding API Key login information in the settings menu![Logged In](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-api-logged.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c5bac79e062f6b2225e2b10675559356)

Please refer to the following steps to apply for and obtain an API Key:

1

Visit the Comfy Platform and Log In

Please visit the [Comfy Platform login page](https://platform.comfy.org/login) and log in with the corresponding account![Visit Platform Login Page](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-1.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=c9516c73148a20ac2de9fcd5f56860c9)

2

Click `+ New` in API Keys to Create an API Key

Click `+ New` in API Keys to create an API Key![Create API Key](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-2.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=9e1f6dc2a5a28fbbe5074f4267dd8d14)

3

Enter API Key Name

![Enter API Key Name](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-3.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=112f28de30c52898bca15513706c70f2)

  1. (Required) Enter the API Key name,
  2. Click `Generate` to create



4

Save the Obtained API Key

![Obtain API Key](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-4.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=223b5d1941d0d9a2f2644807b08a676f)

Since the API Key is only visible upon first creation, please save it immediately after creation. It cannot be viewed later, so please keep it safe. Please note that you should not share your API Key with others. Once it leaked, you can delete it and create a new one.

1

API Key Management

![API Key Management](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-5.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=5a6a40f226903d03ddd3111eb2eb5d24)For unused API Keys or those at risk of being leaked, you can click `Delete` to remove them to prevent unnecessary losses.

2

(Optional) Log Out

![Log Out](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-6.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=26fdf19fe5e8eaac528d923786c123ae)If you have obtained an API Key and are logged in on a public device, please log out promptly.

## Forgot your password

If you can’t remember your password (for email login):

  1. Click the **Forgot password?** link on the login page
  2. Enter your registered email address
  3. Check your email for password reset instructions
  4. Click the reset link in the email
  5. Create a new password
  6. Log in with your new password



## Troubleshooting login issues

If you’re having trouble logging in:

  * Verify your email address is correct
  * Check that Caps Lock is not enabled when entering your password
  * Clear your browser cookies and cache
  * Try using a different browser or incognito mode
  * Ensure your account email has been verified
  * Contact [support](https://docs.comfy.org/support/contact-support) if issues persist



## Security tips

To keep your account secure:

  * Use a strong, unique password
  * Don’t share your login credentials
  * Log out when using shared devices
  * Regularly update your password



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/account/login.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/account/login)

[Create account](https://docs.comfy.org/account/create-account)[Delete account](https://docs.comfy.org/account/delete-account)
