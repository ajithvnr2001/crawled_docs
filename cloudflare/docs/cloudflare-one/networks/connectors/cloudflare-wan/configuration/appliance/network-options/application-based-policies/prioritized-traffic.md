---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/
title: Prioritized traffic \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:19.552355+00:00
---

# Prioritized traffic · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)Configuration[Configure with Connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/)Network options

  4. /[Application-aware policies](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/)
  5. /Prioritized traffic



# Prioritized traffic

Last updated Nov 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow traffic prioritization works Set the provisioned upload bandwidth ConsiderationsAdd an application to your account Add an application to Cloudflare One Appliance Delete an application from Cloudflare One Appliance

Prioritized traffic allows you to define which applications Cloudflare One Appliance (formerly Magic WAN Connector) should process first when a WAN is congested. Applications not in the list are sent as default (best effort) traffic, queued behind prioritized traffic.

Similarly to breakout traffic, prioritized traffic also works via DNS requests inspection.

Caution

Prioritized traffic will not work for applications that use DNS-over-HTTPS.

## How traffic prioritization works

Cloudflare One Appliance sorts the upload traffic it sends out of each WAN into two classes:

Class | Traffic in this class  
---|---  
**Prioritized** | Traffic that matches an application in the site's **Prioritized traffic** list.  
**Default (best effort)** | All other traffic.  
  
When a WAN is congested, the appliance sends prioritized traffic ahead of default traffic. Prioritized traffic cannot completely starve default traffic, so a high-volume prioritized application does not block all other traffic on the WAN. Within each class, the appliance shares bandwidth fairly between flows, so a single large transfer does not crowd out other connections.

Prioritization applies to upload traffic that the appliance sends through its IPsec tunnels to Cloudflare, and to [breakout traffic](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/) that it sends directly to the Internet.

### Set the provisioned upload bandwidth

The appliance can only prioritize traffic that is waiting in a queue on the appliance. If your WAN circuit is slower than the appliance port it is connected to (for example, a 100 Mbps circuit on a 1 Gbps port), traffic leaves the appliance at full port speed and queues in your modem or your ISP's network instead. Prioritization then has little or no effect.

To make prioritization take effect, set **Provisioned upload bandwidth** on each WAN to the upload speed of that circuit. The appliance then limits (shapes) the upload traffic on that WAN to 95% of the value you enter. This keeps the queue on the appliance, where prioritized traffic can be sent first.

  1. Log in to the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com/), and go to **Networks**.
  2. Go to **Connectors** > **Appliances** > **Profiles**.
  3. Select the Cloudflare One Appliance profile you want to configure > **Edit**.
  4. Go to **Network configuration** > **WAN configuration**.
  5. Find the WAN you want to configure > select the three dots next to it > **Edit**.
  6. In **Provisioned upload bandwidth (Mbps)** , enter the upload speed of the WAN circuit. Enter a value from `0.001` to `1,000,000` Mbps, with up to three decimal places.
  7. (Optional) In **Provisioned download bandwidth (Mbps)** , enter the download speed of the WAN circuit.
  8. Select **Save**.



To stop shaping a WAN, clear **Provisioned upload bandwidth (Mbps)** and select **Save**.

Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

Send a `PATCH` request to [update the WAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/edit/). Set `provisioned_upload_kbps` and, optionally, `provisioned_download_kbps` in kilobits per second (kbps). Both fields accept integers from `1` to `1000000000`. For example, a 100 Mbps upload circuit is `100000`.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Patch Site WANbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/wans/$WAN_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"provisioned_upload_kbps": 100000,
    		"provisioned_download_kbps": 500000
    	}'

You can also set both fields when you [create a WAN](https://developers.cloudflare.com/api/resources/magic_transit/subresources/sites/subresources/wans/methods/create/). To remove a value and stop shaping the WAN, set the field to `null` in a `PATCH` request.

### Considerations

  * **No provisioned upload bandwidth means no shaping.** If you leave **Provisioned upload bandwidth** empty, the appliance does not shape the WAN. Prioritized traffic still goes first, but only when the appliance itself is the bottleneck.
  * **Use the real circuit speed.** If the value is too low, the appliance limits throughput below what the circuit can carry. If it is too high, traffic queues upstream of the appliance and prioritization becomes less effective.
  * **Each WAN is shaped on its own.** If several WANs share one physical port (for example, as VLANs), the appliance shapes each WAN separately. Make sure the combined provisioned upload bandwidth of those WANs does not exceed what the shared port or circuit can carry.
  * **Download traffic is not shaped.** The appliance does not currently shape or prioritize download traffic. It saves **Provisioned download bandwidth** with the WAN, but does not use it for shaping.
  * **IPv4 only.** Traffic prioritization applies to IPv4 traffic.
  * **Appliance version.** Upload shaping requires Appliance version 2026.10.3 or later. Appliances update automatically during their [interrupt window](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/).



## Add an application to your account

Before you can add or remove Prioritized traffic applications to your Cloudflare One Appliance, you need to create an account-level list with the applications that you want to configure. Currently, adding to or modifying this list is only possible via API, through the [`managed_app_id`](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/create/) endpoint.

To add applications to your account:

Send a `POST` request to add new apps to your account.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Magic WAN Write`
  * `Magic Transit Write`

Create a new Appbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/apps" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"managed_app_id": "<APP_ID>",
    		"name": "<APP_NAME>",
    		"type": "<APP_TYPE>"
    	}'
    
    
    {
    	"result": {
    		"account_app_id": "eb09v665c0784618a3e4ba9809258fd4",
    		"name": "<APP_NAME>",
    		"type": "<APP_TYPE>",
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

You can now add this new app to the Prioritized traffic list in your Cloudflare One Appliance.

### Add an application to Cloudflare One Appliance

You need to configure Prioritized traffic applications for each of your existing sites, as this is a per-site configuration.

  1. Log in to the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com/), and go to **Networks**.

  2. Go to **Connectors** > **Appliances** > **Profiles**.

  3. Select the Cloudflare One Appliance you want to configure > **Edit**.

  4. Select **Traffic Steering**.

  5. In **Prioritized traffic** , select **Create**.

  6. Select one or more applications that should bypass Cloudflare filtering from the list. You can also use the search box.

  7. Select **Save**.




The traffic for the application you chose is now processed first by Connector.

Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

  1. Send a `GET` [request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/list/) to list the applications associated with an account.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Magic WAN Write`
     * `Magic WAN Read`
     * `Magic Transit Read`
     * `Magic Transit Write`
List Appsbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/apps" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    	{
    		"result": [
    			{
    				"managed_app_id": "<APP_ID>",
    				"name": "<APP_NAME>",
    				"type": "File Sharing",
    				"hostnames": [
    					"<app_name.com>",
    					"<app-name.info>"
    				]
    			}
    		]
    	}

Take note of the `"managed_app_id"` value for any application you want to add.

  2. Send a `POST` request to add new apps to the Prioritized traffic policy.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Magic WAN Write`
     * `Magic Transit Write`
Create a new App Configbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/app_configs" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"managed_app_id": "<MANAGED_APP_ID>",
    		"breakout": true
    	}'
    
    {
    	"result": {
    		"account_app_id": "<APP_ID>",
    		"name": "<APP_NAME>",
    		"type": "<BREAKOUT_OR_PRIORITY>"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }




### Delete an application from Cloudflare One Appliance

  1. Log in to the [Cloudflare One dashboard ↗︎](https://one.dash.cloudflare.com/), and go to **Networks**.

  2. Go to **Connectors** > **Appliances** > **Profiles**.

  3. Select the Appliance you want to configure > **Edit**.

  4. Select **Traffic Steering**.

  5. In **Prioritized traffic** , find the application you want to delete > select the **three dots** next to it > **Remove application traffic**.

  6. (Optional) If you have several pages of applications, you can use the search box to quickly find the application you are looking for.




Note

You will need your [account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/) and [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) to use the API.

You need to delete Prioritized traffic applications for each of your existing sites, as this is a per-site configuration.

  1. Send a [`GET` request](https://developers.cloudflare.com/api/resources/magic_transit/subresources/apps/methods/list/) to list the applications associated with a site.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `Magic WAN Write`
     * `Magic WAN Read`
     * `Magic Transit Read`
     * `Magic Transit Write`
List App Configsbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/magic/sites/$SITE_ID/app_configs" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
    
    	{
    		"result": [
    			{
    				"id": "<APP_ID>",
    				"site_id": "<SITE_ID>",
    				"managed_app_id": "<APP_NAME>",
    				"breakout": true
    			}
    		]
    	}

Take note of the `"id"` value for the application that you want to delete.

  2. Send a `DELETE` request to delete an application from the Prioritized traffic policy.
         
         curl "https://api.cloudflare.com/client/v4/accounts/%7Baccount_id%7D/magic/sites/%7Bsite_id%7D/app_configs/%7Bid%7D" \
         	--request DELETE
         
         {
         		"result": {
         				"id": "<APP_ID>",
         				"site_id": "<SITE_ID>",
         				"managed_app_id": "<APP_NAME>",
         				"breakout": true
         		},
         		"success": true,
         		"errors": [],
         		"messages": []
         }




[PreviousBreakout traffic](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/)[NextConfigure link aggregation groups](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/link-aggregation/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
