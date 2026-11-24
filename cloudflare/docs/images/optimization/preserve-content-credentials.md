---
url: https://developers.cloudflare.com/images/optimization/preserve-content-credentials/
title: Preserve Content Credentials \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:00.837592+00:00
---

# Preserve Content Credentials · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/optimization/preserve-content-credentials/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /Optimization
  4. /Preserve Content Credentials



# Preserve Content Credentials

Last updated Nov 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewTurn on for remote images Use the cf CLI Use the API Use the dashboardTurn on for hosted images Dashboard REST API

[Content Credentials ↗︎](https://contentcredentials.org/) use the Coalition for Content Provenance and Authenticity (C2PA) standard to provide cryptographically signed information about an image's origin and edit history.

You configure Content Credentials preservation separately for remote and hosted images:

Image source | Setting scope  
---|---  
Remote images (transformations) | Each zone that serves image transformations  
Hosted images | Each Cloudflare account  
  
When preservation is disabled, Images omits Content Credentials from the re-encoded output and does not sign optimization actions.

When preservation is enabled, use the [`metadata`](https://developers.cloudflare.com/images/optimization/features/#metadata) parameter to control whether Images preserves existing Content Credentials and appends cryptographically signed [optimization actions](https://developers.cloudflare.com/images/optimization/features/).

If the source image does not contain Content Credentials, then Images does not create them or append signed optimization actions. When Images returns the source image unchanged, its original Content Credentials remain embedded.

To inspect the resulting provenance chain, use the [Content Credentials verification service ↗︎](https://contentcredentials.org/verify).

## Turn on for remote images

### Use the cf CLI

With the [Cloudflare CLI](https://developers.cloudflare.com/cf/) (`cf`) installed and authenticated, turn on Content Credentials preservation for a zone:
    
    
    cf zones transformations-c2pa edit --zone example.com --value on

The `--zone` flag accepts a zone ID or domain name. To turn the setting off, use `--value off`.

### Use the API

[Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the [Zone Settings Write permission](https://developers.cloudflare.com/fundamentals/api/reference/permissions/#zone-permissions) for the zone.

Use the [Change Image Transformations C2PA setting](https://developers.cloudflare.com/api/resources/zones/subresources/transformations_c2pa/methods/edit/) endpoint:
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/transformations_c2pa" \
      --request PATCH \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{"value":"on"}'

To turn off Content Credentials preservation, set `value` to `off`.

### Use the dashboard

  1. In the Cloudflare dashboard, go to **Images** > **Transformations**.

[ Go to **Transformations** ↗ ](https://dash.cloudflare.com/?to=/:account/images/transformations)
  2. Select the zone that serves your transformations.

  3. Turn on **Preserve Content Credentials**.

![Preserve Content Credentials setting for an Images transformation zone](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1632,height=350,format=webp/_astro/preserve-content-credentials.BDptgOn0.png)



## Turn on for hosted images

For hosted images, Content Credentials preservation is an account-wide setting. It applies to every image delivered through `imagedelivery.net` or a custom domain configured for your Images account.

### Dashboard

  1. In the Cloudflare dashboard, go to **Images** > **Hosted Images**.

[ Go to **Hosted images** ↗ ](https://dash.cloudflare.com/?to=/:account/images/hosted)
  2. Select **Delivery**.

  3. Turn on **Preserve Content Credentials**.




### REST API

Use the [Images config ↗︎](https://developers.cloudflare.com/api/resources/images/) endpoint to set `preserve_content_credentials`:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/images/v1/config" \
      --request PATCH \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{"preserve_content_credentials": true}'

[PreviousMake responsive images](https://developers.cloudflare.com/images/optimization/make-responsive-images/)[NextMethods](https://developers.cloudflare.com/images/storage/upload-images/methods/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/optimization/preserve-content-credentials.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
