---
url: https://developers.cloudflare.com/fundamentals/manage-members/manage/
title: Manage account members \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:38:31.893334+00:00
---

# Manage account members · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/manage-members/manage/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /[Members and permissions](https://developers.cloudflare.com/fundamentals/manage-members/)
  4. /Manage



# Manage

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView account membersAdd account membersEdit member permissionsManage member settingsResend an invitationRemove account membersSuper Administrator access

Granting access to others on your account is done with several sets of data principles:

  1. Accounts have Account Members.
  2. Account Members have policies.
  3. Policies are constructed out of actors, roles, and scopes.



When inviting a new member, you can assign one or more permission policies to them directly. Policies can also be added or revoked at a later time.

Learn how to add new account members, edit or revoke their access, and resend verification emails.

Note

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

## View account members

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To view members using the dashboard:

In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)

To view members using the API, send a [`GET` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/list/).

## Add account members

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To add a member to your account:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. Select **Invite members**.

  3. Under **Add email addresses** , enter one or more email addresses. Separate multiple addresses with commas.

  4. Under **Add permission policies** , create the first permission policy for these members:

a. Choose the policy's [scope](https://developers.cloudflare.com/fundamentals/manage-members/scope/): either the entire account, or specific resources such as individual domains, Workers, or Access applications.

b. Select one or more [roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/) to include in the policy. Search by role name, or expand a role category (for example, **App Security** or **Cloudflare One / Zero Trust**) and select individual roles. To select every role in a category, select the category's checkbox.

c. Select **Create policy**.

  5. (Optional) Repeat the previous step to add more permission policies with different scopes or roles.

  6. Select **Invite members**.




Each invitee receives an email invitation and appears on the **Members** page with a **Pending** status until they accept it.

Note

If a user already has an account with Cloudflare and you have an Enterprise account, you can also select **Skip email confirmation** to add them to your account without sending an email invitation.

To add a member using the API, send a [`POST` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/create/).

## Edit member permissions

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To edit member permissions using the dashboard:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. On the member's row, select **...** > **View & Edit permission policies**.

  3. On the **Permission policies** tab, make your changes:

     * To add a policy, select **Create a policy** , choose the [scope](https://developers.cloudflare.com/fundamentals/manage-members/scope/) and [roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/), then select **Create policy**.
     * To change an existing policy, select **...** > **Edit policy** on its row, adjust the scope and roles, then save your changes.
     * To remove a policy, select **...** > **Delete policy** on its row.



To edit member permissions using the API, get a [list of roles](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/methods/list/) available for an account.

Then, send a [`PUT` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/update/) to edit their permissions.

Requestbash
    
    
    curl --request PUT \
      --url https://api.cloudflare.com/client/v4/accounts/{account_id}/members/{member_id} \
      --header 'Authorization: Bearer <API_TOKEN>' \
      --header 'Content-Type: application/json' \
      --data '{
    	  "roles": [
    	        {
    	            "id": "<ROLE_ID1>"
    	        },
    	        {
    	            "id": "<ROLE_ID2>"
    	        }
    	  	]
    		}'

## Manage member settings

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

Each member has settings that apply only to them, such as their API access.

To manage a member's settings:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. On the member's row, select **...** > **Manage member settings**.

  3. Under **API access for this member** , choose one of the following:

     * **Account default** : Follow the account-wide API access setting.
     * **Allow access** : Always allow API access, even if the account-wide setting is off.
     * **Block access** : Always block API access, even if the account-wide setting is on.



## Resend an invitation

If you invited a member to your account but they cannot find the invitation or the invitation expires, you can resend the invitation through the Cloudflare dashboard:

  1. In the Cloudflare dashboard, go to the **Members** page.1

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. On the row of the member whose **Status** is **Pending** , select **...** > **Resend invite**.




## Footnotes

  1. To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/). ↩




## Remove account members

To manage account members, you must have a role of **Super Administrator** and have a [verified email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/).

To revoke a member's access to your account, or to cancel a pending invitation:

  1. In the Cloudflare dashboard, go to the **Members** page.

[ Go to **Members** ↗ ](https://dash.cloudflare.com/?to=/:account/members)
  2. On the member's row, select **...** > **Remove member**.

  3. In the confirmation dialog, select **Remove member**.




To revoke a member's access to your account using the API, send a [`DELETE` request](https://developers.cloudflare.com/api/resources/accounts/subresources/members/methods/delete/).

Note

If you have been invited to an account and want to remove yourself from the account, go to the **Members** page. On your own row, select **...** > **Leave account**.

## Super Administrator access

If you are a Super Administrator for an account that has existing domains and you decide to leave the account, you can invite a new Super Administrator who will have access to the same account privileges.

You can delete your user as a Super Administrator, but you cannot delete your account. Other Super Administrators will continue to have access to the appropriate privileges to manage the account, including billing information.

[PreviousMembers and permissions](https://developers.cloudflare.com/fundamentals/manage-members/)[NextPolicies](https://developers.cloudflare.com/fundamentals/manage-members/policies/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/manage-members/manage.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
