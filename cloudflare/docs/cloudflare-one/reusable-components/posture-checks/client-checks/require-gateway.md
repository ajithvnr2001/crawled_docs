---
url: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/
title: Require Gateway \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:14:02.344559+00:00
---

# Require Gateway · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Reusable components[Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/)

  4. /[Cloudflare One Client checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/)
  5. /Require Gateway



# Require Gateway

Last updated Oct 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCheck result per client modePrerequisites1\. Enable the Gateway check2\. Add the check to an Access application

With Require Gateway, you can allow access to your applications only to devices enrolled in your Zero Trust organization. Unlike [Require WARP](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/), which will check for any WARP instance (including the consumer version), Require Gateway will only allow requests coming from devices whose traffic is filtered by your organization's Cloudflare Gateway configuration. This policy is best used when you want to protect company-owned assets by only allowing access to employees.

## Check result per client mode

The check result depends on the [client mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/) configured on the device.

Client mode | Result | Reason  
---|---|---  
Traffic and DNS mode | ✅ Pass | Device traffic is routed through and filtered by Gateway  
Traffic only mode | ✅ Pass | Device traffic is routed through Gateway except the DNS queries  
DNS only mode | ❌ Fail | Only DNS queries are forwarded; network traffic does not flow through Gateway  
Local proxy mode | ⚠️ Partial | The check passes only for traffic explicitly configured to use the local SOCKS/HTTP proxy on port `40000`, as this traffic is tunneled through Gateway. Traffic not routed through the proxy bypasses Gateway and fails the check.  
Posture only mode | ❌ Fail | The client is enrolled and collects posture data, but does not route traffic through Gateway  
  
## Prerequisites

  * Cloudflare One Client is [deployed](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/) on the device. For a list of supported modes and operating systems, refer to [Cloudflare One Client Checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/).




## 1\. Enable the Gateway check

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Reusable components** > **Posture checks**.

  2. Go to **Cloudflare One Client checks** and select **Add a check**.

  3. Select **Gateway** , then select **Save**.




## 2\. Add the check to an Access application

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Applications**.

  2. Locate the application for which you want to require Gateway. Select **Configure**.

  3. In the **Policies** tab, create a new Access policy or edit an existing policy.

  4. In the policy builder, add an Include or Require rule which uses the _Gateway_ selector. Save the policy.

  5. Save the Access application.




Before granting access to the application, the policy will check that the device is running the Cloudflare One Client and enrolled in your Zero Trust organization.

[PreviousOS version](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/)[NextRequire WARP](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
