---
url: https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/manage-traffic-scope/
title: Manage traffic scope \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:09:48.121621+00:00
---

# Manage traffic scope · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/manage-traffic-scope/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Cloud Workload Security](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/)

  4. /[Guides](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/)
  5. /Manage traffic scope



# Manage traffic scope

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a domain ACLAttach a domain ACLCreate a Basic Auth credentialRotate a secret

Domain access control lists (ACLs) control which destinations a deployment can reach. Use the Basic Auth page to manage credentials and their secrets. To understand how these controls relate to request policies, refer to [Request Validation](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/concepts/request-validation/).

You need access to manage Cloud Workload Security in your account.

## Create a domain ACL

A domain ACL contains domain-specific actions and a default action. The default action applies when no domain entry matches.

  1. In the Cloudflare dashboard, select your account and go to **Cloud Workload Security** > **Traffic scope** > **Domain ACLs**.

[ Go to **Domain ACLs** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/domain-acls)
  2. Select **Add a domain ACL** and enter a **Name**.

  3. Choose **Allow** or **Block** for **Default action**.

  4. In **Domains** , select **Add domain**. Enter a **Domain** and choose its **Action**. For example, block `api.example.com` with a default action of **Allow**.

  5. Select **Add a domain ACL** to save the list.




Use `example.com` for an exact domain match. Use `.example.com` to match the parent domain and its subdomains.

## Attach a domain ACL

  1. In the Cloudflare dashboard, go to **Cloud Workload Security** > **Deployments** and open the deployment.

[ Go to **Deployments** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/deployments)
  2. In **Domain ACL** , select from the list and select **Save**.

  3. After the proxy refreshes its configuration, test an allowed destination and a blocked destination through it.




An ACL allow decision permits the connection. CWS policies can still block API requests on that connection.

To detach the list, select **None** in **Domain ACL** and select **Save**. Detach an ACL from its deployments before deleting it.

## Create a Basic Auth credential

Basic Auth credentials are separate from the Cloudflare API token used in your proxy configuration.

  1. In the Cloudflare dashboard, go to **Cloud Workload Security** > **Traffic scope** > **Credentials** > **Basic Auth**.

[ Go to **Basic Auth credentials** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/credentials/basic-auth)
  2. Select **Create credential** and enter a **Username**. Use printable characters without spaces or colons.

  3. In **Secrets** , select **Add a secret**. Enter **Password** and **Confirm password**. Optionally, set an **Expiration**.

  4. In the dialog, select **Add a secret** , then select **Create credential** to save the credential and its initial secret.




The username is read-only after creation. Open the credential to manage its secrets.

## Rotate a secret

Use this procedure for a credential your clients already use.

  1. In **Basic Auth** , open the credential.

  2. In **Secrets** , select **Add a secret**. Enter and confirm the new password, set an optional expiration, and select **Add a secret**.

  3. Allow the deployment configuration to refresh before updating clients to use the new password. Verify requests from those clients before deleting the old secret.

  4. For the old secret, select **Delete** and confirm the deletion.




The secret list displays creation and expiration information. It does not display stored passwords.

[PreviousConfigure policies](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/configure-policies/)[NextPolicy reference resources](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/policy-reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/cloud-workload-security/guides/manage-traffic-scope.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
