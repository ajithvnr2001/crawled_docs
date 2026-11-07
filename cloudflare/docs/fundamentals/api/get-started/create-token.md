---
url: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
title: Create API token \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:31:57.784441+00:00
---

# Create API token · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Cloudflare's API

  4. /Get started
  5. /Create API token



# Create API token

Last updated Nov 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Prerequisite

Before you begin, [find your zone and account IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).

  1. Determine if you want a user token or an [Account API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/). Use Account API tokens if you prefer service tokens that are not associated with users and your [desired API endpoints are compatible](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/#compatibility-matrix).

  2. From the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/profile/api-tokens/), go to **My Profile** > **API Tokens** for user tokens. For Account Tokens, go to **Manage Account** > **API Tokens**.

  3. Select **Create Token**.

  4. Add a token name to describe why or how the token is used.

  5. Select a template from the available [API token templates](https://developers.cloudflare.com/fundamentals/api/reference/template/) or start from scratch. Templates include policies with predefined permissions. The following example uses the **Edit zone DNS** template.

![Token template overview screen](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2953,height=1955,format=webp/_astro/template-customize.BZQKf5iV.png)
  6. Create a policy to organize the token's permissions. Select a policy type (_Account_ , _User_ , or _Zone_), then select resource rules within the policy to specify which resources the permissions apply to, such as specific accounts or zones.

  7. Choose the permissions to grant within the policy. Most permissions offer `Edit` or `Read` access. `Edit` is full CRUDL (create, read, update, delete, list) access, while `Read` is the read permission and list where appropriate. For example, `Zone DNS Read` for `example.com` allows the token to read DNS records only for that zone. Refer to the [available token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) for more information.

  8. (Optional) Restrict how a token is used in the **Token expiration** and **Client IP Address Filtering** fields.

  9. Select **Continue to summary**.

  10. Review the token summary. Select **Back** to make adjustments. You can also edit a token after creation.


![Token summary screen displaying the resources and permissions selected](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2953,height=1949,format=webp/_astro/token-summary.B2YcuQmd.png)

  11. Select **Create Token** to generate the token's secret.
  12. Copy the secret to a secure place.



Warning

The token secret is **only shown once**. Do not store the secret in plaintext where others can access it. Anyone with this token can perform the authorized actions against the resources that the token has access to.

![Token creation completion screen displaying your API token and the curl command to test your token](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2953,height=1955,format=webp/_astro/token-complete.ethtDojh.png)

The token secret page also includes an example command to test the token. Use the `/user/tokens/verify` endpoint to fetch the current status of the given token.
    
    
    curl "https://api.cloudflare.com/client/v4/user/tokens/verify" \
    --header "Authorization: Bearer <API_TOKEN>"

The result:
    
    
    {
    	"result": {
    		"id": "100bf38cc8393103870917dd535e0628",
    		"status": "active"
    	},
    	"success": true,
    	"errors": [],
    	"messages": [
    		{
    			"code": 10000,
    			"message": "This API Token is valid and active",
    			"type": null
    		}
    	]
    }

New API tokens use the `cfut_` prefixed [scannable format](https://developers.cloudflare.com/fundamentals/api/get-started/token-formats/), which allows credential scanning tools to detect leaked tokens.

With this you have successfully created an API token and can start working with the Cloudflare API. After creating your first API token, you can create additional API tokens [via the API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/).

[PreviousUnder a DDoS attack?](https://developers.cloudflare.com/fundamentals/security/under-ddos-attack/)[NextGet Global API key (legacy)](https://developers.cloudflare.com/fundamentals/api/get-started/keys/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/api/get-started/create-token.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
