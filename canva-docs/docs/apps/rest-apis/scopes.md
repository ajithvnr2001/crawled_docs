---
url: https://www.canva.dev/docs/apps/rest-apis/scopes/
title: Scopes - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T16:58:47.494854+00:00
---

# Scopes - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/scopes/

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

# Scopes

Copy page

The Canva REST APIs use scopes to specify the access an access token grants. The scopes your app can request depend on your app type:

  * **Public or private apps** act on behalf of a user, using the OAuth authorization code flow.
  * **Service apps** act on behalf of your app itself, using the OAuth client credentials flow.



Scopes are explicit. A scope that grants write access doesn't also grant read access.

For example, `asset:write` doesn't grant `asset:read` access. To get both read and write access to a user's assets, request both scopes. The same applies to service apps: request each `service:` scope your app needs.

## Scopes for public or private apps

Use these scopes when your app accesses data or performs actions on behalf of a user. Request them as part of the user authorization flow.

Scope| Description  
---|---  
`asset:read`| View the metadata for the user's assets, such as uploaded images.  
`asset:write`| Upload, update, or delete assets on the user's behalf.  
`brandtemplate:content:read`| Read the content of the brand templates associated with the user's brand.  
`brandtemplate:content:write`| Publish brand templates associated with the user's brand.  
`brandtemplate:meta:read`| View the metadata of the brand templates associated with the user's brand.  
`collaboration:event`| Receive webhook notifications about events relevant to the user.  
`comment:read`| View the comments on the user's designs, and the associated metadata.  
`comment:write`| Create comments and replies on the user's designs.  
`design:content:read`| View the contents of the user's designs.  
`design:content:write`| Create designs on the user's behalf.  
`design:meta:read`| View the metadata of the user's designs.  
`email`| Read user email address through OIDC.  
`folder:permission:write`| Set, update, or remove permissions assigned to the user's folders.  
`folder:read`| View the metadata and contents of the user's folders, including their **Projects** folder.  
`folder:write`| Add, move, or remove the user's folders. It also lets you edit folder metadata, such as the folder's name.  
`openid`| Read user information through Open ID Connect (OIDC).  
`profile`| Read user profile information through OIDC.  
`profile:read`| Read a user's profile and account information.  
  
For example, to read a user's design metadata, request the `design:meta:read` scope. To also write to the user's folders, request both `design:meta:read` and `folder:write`.

## Scopes for service apps

Use these scopes when your app accesses resources on its own behalf, without acting on behalf of a user. Request them when generating an access token using the client credentials flow.

Scope| Description  
---|---  
`service:asset:read`| View the metadata for the app's assets, such as uploaded images.  
`service:asset:write`| Upload assets on the app's behalf.  
`service:brandtemplate:content:read`| Read the content of the brand templates associated with the developer's brand.  
`service:brandtemplate:meta:read`| View the metadata of the brand templates associated with the developer's brand.  
`service:design:content:read`| View the contents of the app's designs.  
`service:design:content:write`| Create designs on the app's behalf.  
`service:design:meta:read`| View the metadata of the app's designs.  
`service:folder:write`| Move designs, assets, and folders between folders on the app's behalf.
