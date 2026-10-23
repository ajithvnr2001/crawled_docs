---
url: https://ai.google.dev/gemini-api/docs/aistudio-deploying/
title: Deploying from Google AI Studio
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:46.699747+00:00
---

# Deploying from Google AI Studio

> Source: https://ai.google.dev/gemini-api/docs/aistudio-deploying/

Google AI Studio lets you to deploy your full-stack applications directly from Build mode. This provides a fast path from prototype to a managed, scalable production environment.

## Deployment options

To deploy your application from AI Studio Build mode, the requirements depend on the tier you use:

  * [**Google Cloud Starter Tier**](https://docs.cloud.google.com/docs/starter-tier): Lets eligible accounts publish up to 2 full-stack applications without setting up a Google Cloud project or billing account.
  * **Standard deployment** : Requires a Google Cloud project linked to your AI Studio account and billing enabled on that project.



## About the Starter Tier

The Google Cloud Starter Tier provides a streamlined path for eligible accounts to deploy applications to Google Cloud directly from Google AI Studio. You don't need to set up a full Google Cloud environment or billing account.

Each Google AI Studio deployment creates a corresponding service in Cloud Run. For services deployed in Google AI Studio with Starter Tier, the following limitations apply:

  * You can deploy up to two services.
  * Your services are deployed in a [single Cloud Run region](https://docs.cloud.google.com/run/docs/locations).



### Starter Tier eligibility

Not all accounts are eligible for the Google Cloud Starter Tier. Your account may be ineligible if any of the following apply:

  * You're signed in with a Google Workspace account (including paid or free Google Workspace, Google Workspace for Education, or Google for Nonprofits subscriptions).
  * You have an active or prior paid Google Cloud billing account.
  * We don't have enough evidence from your account activity to grant Starter Tier access at this time.



The Google AI Studio support team can't override Starter Tier eligibility. If your account isn't eligible, attach a billing account and use standard deployment to publish apps.

## Deploy with the Starter Tier

After designing your app in Build mode, deploy it with Starter Tier:

  1. Click the **Publish** button in the top right corner.
  2. Click **Get Started**.
  3. Click **Publish App**.



Once deployment is complete, AI Studio provides a Cloud Run URL where you can access your live application.

## Custom URLs for AI Studio

When publishing an application from Google AI Studio, you can set a custom, memorable subdomain under `ai.studio` (for example, `https://your-app-name.ai.studio`).

Google AI Studio requires subdomains to be globally unique across all projects, and assigns them on a first-come, first-served basis. If another project already uses a name, AI Studio prompts you to choose a different one. If you unpublish or delete an application, its custom URL is released and becomes available for other users to claim.

### Set a custom URL

To set or update a custom URL for your application:

  1. Open your application in Google AI Studio in **Build** mode.
  2. Click **Publish** in the top right corner.
  3. In the deployment configuration, enter your preferred subdomain in the **Custom URL** field or accept the suggested URL.
  4. Click **Publish App**.



To transfer an existing custom URL to a different application, you must first unpublish or delete the application which is assigned that custom URL, and then publish your new application using the chosen subdomain.

### Report trademark or copyright issues

Custom subdomains must comply with the [Google Terms of Service](https://policies.google.com/terms). If you notice a custom URL that infringes on a trademark or uses a copyrighted name without permission, you can report it using the [Google Legal Troubleshooter](https://support.google.com/legal/troubleshooter/1114905).

## Standard deployment

As your applications evolve, you might require capabilities beyond the Starter Tier, such as higher quotas or increased compute resources or other Google Cloud products not available in the Starter Tier. To unlock these capabilities, you can convert your fully managed Starter Tier project into a standard Google Cloud project.

This ensures that you can scale seamlessly without losing your progress. Follow the steps to [create a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#create-new-billing-account), formally accept the standard Google Cloud Terms of Service, and [upgrade to a standard Google Cloud project](https://docs.cloud.google.com/docs/starter-tier#upgradee). For more information, see [Setup for Paid accounts](https://docs.cloud.google.com/billing/docs/in-product-billing-setup#paid-setup).

To learn more about billing tiers, see [Billing](https://ai.google.dev/gemini-api/docs/billing).

## Delete your application

If you no longer need your app, you can delete it in Google AI Studio by following these instructions:

  1. In Google AI Studio, go to your [Apps page](https://aistudio.google.com/app/apps).
  2. In the left menu, select **Apps**.
  3. Hold the pointer over the app you want to delete.
  4. Click the trash can icon on the right-side of the row to delete the app.



## What's next

  * Learn more about the [Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier).
  * Read about [Billing](https://ai.google.dev/gemini-api/docs/billing) in Gemini API.


