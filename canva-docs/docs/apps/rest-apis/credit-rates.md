---
url: https://www.canva.dev/docs/apps/rest-apis/credit-rates/
title: Canva REST API credit rates - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T16:58:42.705348+00:00
---

# Canva REST API credit rates - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/credit-rates/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

[API reference](https://www.canva.dev/docs/apps/api/)[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)[App UI Kit reference](https://www.canva.dev/docs/apps/app-ui-kit/changelog/)[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

[Canva REST API reference](https://www.canva.dev/docs/apps/rest-apis/reference/)[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)[Credit rates](https://www.canva.dev/docs/apps/rest-apis/credit-rates/)[Webhooks notification reference](https://www.canva.dev/docs/apps/rest-apis/webhooks/)[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

[Tools](https://www.canva.dev/docs/apps/mcp/tools/search-designs/)[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)[Restricted uses](https://www.canva.dev/docs/apps/restricted-uses/)

# Canva REST API credit rates

Understand how API jobs use credits, and how many credits each job costs.

Copy page

When you use the Canva Developers SDK to run certain jobs with the Canva REST APIs, each job uses credits. You can purchase credits with API top-ups, which are available from your app's settings in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/).

All APIs accessible through a service account (a Client Credentials Integration under [Schedule 1⁠(opens in a new tab or window)](https://www.canva.com/policies/api-services-sch1/)) are API Services for the purposes of [Schedule 1⁠(opens in a new tab or window)](https://www.canva.com/policies/api-services-sch1/) (Canva API Services Terms). The APIs listed on this page are chargeable at the rates shown; APIs not listed are currently provided at no charge.

## How credits work

Credits are deducted from the pool the moment a job is created. The job's final status, which the job's `GET` endpoint returns, decides whether the deduction is confirmed:

  * **`success`:** The deduction is final.
  * **`failed`:** Canva returns the credits to your balance.



## Credit rates

The following tables list the credits that each job uses.

### Design and presentation

API job| Credits  
---|---  
[Create design autofill job](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/)| 10 credits per page  
[Create design resize job](https://www.canva.dev/docs/apps/rest-apis/reference/resizes/create-design-resize-job/)| 1 credit per resize  
[Create design merge job](https://www.canva.dev/docs/apps/rest-apis/reference/merges/create-design-merge-job/)| 1 credit per merge  
  
### Image generation

To choose a model, set the `model` property when you call [Create image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/create-image-generation-job/).

Model| Model ID| Credits  
---|---|---  
Lucid Origin| `lucid_origin`| 0.5 credits per image  
Z Image Turbo| `z_image_turbo`| 0.2 credits per image  
CRAFT-1 2K| `craft_v1_2k`| 3 credits per 2K image  
  
### Image editing and transformation

API job| Credits  
---|---  
Magic Layers, using [Create image-to-design import job](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/create-image-to-design-import-job/)| 1.7 credits per image or page  
Background removal, using [Create image transformation job](https://www.canva.dev/docs/apps/rest-apis/reference/image-transformations/create-image-transformation-job/) with the `background_removal` transformation| 2 credits per image  
  
## Related

  * [API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)
  * [Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)


