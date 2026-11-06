---
url: https://www.canva.dev/docs/apps/rest-apis/generate-images-with-craft/
title: Generate images with CRAFT - Canva for your platform - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T16:58:42.774400+00:00
---

# Generate images with CRAFT - Canva for your platform - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/generate-images-with-craft/

Canva for your platform

[About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)

Fundamentals

[API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)[Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)[Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/)[API versions](https://www.canva.dev/docs/apps/rest-apis/versions/)

Development guides

[Generate images with CRAFT](https://www.canva.dev/docs/apps/rest-apis/generate-images-with-craft/)[Autofill designs with data](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/)[Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)

Design guidelines

[User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/)[UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/)[Brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/)

# Generate images with CRAFT

Set up an app and generate your first image with Canva's CRAFT-1 2K model.

Copy page

The image generation APIs are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview APIs will not pass the review process, and can't be made available to all Canva users.



Use CRAFT-1 2K (`craft_v1_2k`), Canva's first-party image generation model, to generate an image from your own platform. This guide shows you how to create an app, start a generation job, and download the image.

## Set up your app

Image generation works with a public or private app, or with a service app. Choose one of the following:

  * **Public or private app:** The app acts on behalf of a Canva user, who signs in and authorizes it. The access token needs the `asset:write` scope, and the user needs the `image_generation` capability. Starting a job uses that user's [AI credit allowance⁠(opens in a new tab or window)](https://www.canva.com/help/ai-access/). If the user has reached their allowance, the request returns a `402` error with the `credit_quota_exceeded` code.
  * **Service app:** The app acts on its own behalf, using the OAuth client credentials flow. The access token needs the `service:asset:write` scope. [Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/) don't apply to a service app. Starting a job uses credits from your team's API credit pool. CRAFT-1 2K costs 3 credits per 2K image. For the rates, and for how a failed job returns credits, see [Canva REST API credit rates](https://www.canva.dev/docs/apps/rest-apis/credit-rates/). If the app has reached its credit quota, the request returns a `402` error with the `app_credit_quota_exceeded` code.



You can download the generated image from a URL. A public or private app can also save the image to the user's Canva account.

### Public or private app

To set up a public or private app:

  1. Create an app and enable the REST APIs using the [Quickstart for public or private apps](https://www.canva.dev/docs/apps/quickstart/?app-surface=Canva%20for%20your%20platform&platform-app-type=Public%20or%20private%20app).
  2. In the Developer Portal, go to **Outside Canva > Configuration**. Under **Scopes** , select **Write** for **asset**. This grants the `asset:write` scope.
  3. Authorize the user with the [authorization code flow](https://www.canva.dev/docs/apps/rest-apis/authentication/#authenticate-public-or-private-apps). You can check the `image_generation` capability with [Get user capabilities](https://www.canva.dev/docs/apps/rest-apis/reference/users/get-user-capabilities/).



### Service app

To set up a service app:

  1. Create a service app and buy an API pack using the [Quickstart for service apps](https://www.canva.dev/docs/apps/quickstart/?app-surface=Canva%20for%20your%20platform&platform-app-type=Service%20app).
  2. In the Developer Portal, go to **Outside Canva > Configuration**. Under **Scopes** , select **Write** for `service:asset`. This grants the `service:asset:write` scope.
  3. Generate an access token that includes `service:asset:write`, using the [client credentials flow](https://www.canva.dev/docs/apps/rest-apis/authentication/#authenticate-service-apps).



## Generate an image

From your backend, call [Create image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/create-image-generation-job/). Set `model` to `craft_v1_2k` so the job uses CRAFT-1 2K. If you omit `model`, Canva selects the model for the request.

Replace `{access token}` with your access token, and `{idempotency key}` with a new UUID for this attempt. Reuse that UUID when you retry the same request. A repeated key returns the original job for 24 hours, including when that job failed. To start a new attempt, use a new UUID.
    
    
    curl --request POST 'https://api.canva.com/rest/v1/image-generations' \
    
      --header 'Authorization: Bearer {access token}' \
    
      --header 'Content-Type: application/json' \
    
      --data '{
    
        "prompt": "A ceramic coffee cup on a sunlit table, soft natural light",
    
        "model": "craft_v1_2k",
    
        "idempotency_key": "{idempotency key}"
    
      }'

SHELL

Copy

The response includes `job.id`. Copy it for the next step.

To also save the image in the user's Canva account, add `"asset_upload": { "type": "upload" }` to the request body. This requires a public or private app. The job then stays `in_progress` until the asset has finished importing, and a successful result includes `job.result.image.asset` as well as the download URL.

## Get the generated image

Call [Get image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/get-image-generation-job/) with the same access token that created the job. Generation is asynchronous, so request the job again while `job.status` is `in_progress`. For the workflow and how often to poll, see [Asynchronous job endpoints](https://www.canva.dev/docs/apps/rest-apis/requests-responses/#asynchronous-job-endpoints).
    
    
    curl --request GET 'https://api.canva.com/rest/v1/image-generations/{jobId}' \
    
      --header 'Authorization: Bearer {access token}'

SHELL

Copy

Replace `{jobId}` with `job.id` from the create response.

When `job.status` is `success`, download the image from `job.result.image.url`. The URL is valid for 24 hours. When `job.status` is `failed`, read `job.error.code` and `job.error.message`. For `model_not_available` and `model_retired`, see [Generations](https://www.canva.dev/docs/apps/rest-apis/reference/generations/).

The prompt in this guide generates an image like the following:

![A speckled ceramic coffee cup on a saucer, on a sunlit wooden table beside a croissant, an open notebook, and a glass vase of daisies](https://www.canva.dev/_next/static/media/example-output.75f8fd72.webp)

## Call CRAFT from the Canva CLI

You can run the same requests from a terminal with the [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/). The CLI calls the REST APIs as the Canva account you're logged in with, so that account needs the `image_generation` capability. Run `canva login` first. If a call fails with `MISSING_SCOPE`, log in again so the CLI can request `asset:write`.
    
    
    canva api generations create-image \
    
      --model craft_v1_2k \
    
      --prompt "A ceramic coffee cup on a sunlit table, soft natural light" \
    
      --idempotency-key "{idempotency key}"

SHELL

Copy

The CLI prints a JSON object. The job ID is `data.job.id`.
    
    
    canva api generations get-image --job-id "{job ID}"

SHELL

Copy

Check `data.job.status` the same way as the REST response. On success, the download URL is `data.job.result.image.url`.

## Next steps

For more detail:

  * Read the request and response fields for [Create image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/create-image-generation-job/) and [Get image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/get-image-generation-job/).
  * Compare CRAFT-1 2K with the other image models on [Generations](https://www.canva.dev/docs/apps/rest-apis/reference/generations/).
  * See how many credits a service app uses on [Canva REST API credit rates](https://www.canva.dev/docs/apps/rest-apis/credit-rates/).


