---
url: https://www.canva.dev/docs/apps/rest-apis/deep-links/
title: Open designs with deep links - Canva for your platform - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-17T18:48:04.539399+00:00
---

# Open designs with deep links - Canva for your platform - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/deep-links/

Canva for your platform

[About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)

Fundamentals

[API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)[Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)[Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/)[API versions](https://www.canva.dev/docs/apps/rest-apis/versions/)

Development guides

[Generate images with CRAFT](https://www.canva.dev/docs/apps/rest-apis/generate-images-with-craft/)[Autofill designs with data](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/)[Open designs with deep links](https://www.canva.dev/docs/apps/rest-apis/deep-links/)[Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)

Design guidelines

[User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/)[UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/)[Brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/)

# Open designs with deep links

Control what users see when they open a design in Canva from your platform.

Copy page

When your platform sends a user to Canva to edit or view a design, you can use a _deep link_ to control how the design opens. A deep link is a design URL returned by the Canva REST APIs, with a `target_state` query parameter added to it.

With a deep link, you can:

  * Open the design at a specific page.
  * Open an app in the Canva editor.
  * Pass context that Canva returns to your platform when the user navigates back.



You can use these options on their own, or combine them in the same link. Deep links only control how a design opens. They don't grant additional access to the design or to an app.

This page covers deep links that open an existing design from your platform. To create links that open an app inside Canva with a new design, see [Deep linking](https://www.canva.dev/docs/apps/deep-linking/).

## How deep links work

The REST APIs return a `urls` object with each design, for example, in the responses of the [Get design](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design/), [List designs](https://www.canva.dev/docs/apps/rest-apis/reference/designs/list-designs/), and [Create design](https://www.canva.dev/docs/apps/rest-apis/reference/designs/create-design/) APIs:
    
    
    {
    
      "urls": {
    
        "edit_url": "https://www.canva.com/api/design/{token}/edit",
    
        "view_url": "https://www.canva.com/api/design/{token}/view"
    
      }
    
    }

JSON

Copy

The `edit_url` opens the design in the Canva editor, and the `view_url` opens the design for viewing. Both URLs are temporary, and only the user that made the API request can access them. Always use the URLs that the REST APIs return, including their tokens, instead of constructing a URL from a design ID.

To create a deep link, add the `target_state` query parameter to either URL. The parameter's value is a JSON object, called the _target state_ , encoded as [base64url⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc4648#section-5) without padding:
    
    
    https://www.canva.com/api/design/{token}/edit?target_state={ENCODED_TARGET_STATE}

Copy

Deep links don't require additional scopes or API requests. Canva reads the target state when the user opens the link, not when you create it.

The target state object has the following properties:

Property| Required| Description| Supported URLs  
---|---|---|---  
`schema`| Yes| The version of the target state format. Must be `v1`.| `edit_url` and `view_url`  
`page`| No| The [page to open the design at](https://www.canva.dev/docs/apps/rest-apis/deep-links/#open-a-design-at-a-specific-page).| `edit_url` and `view_url`  
`focus`| No| The feature to open with the design, such as [an app](https://www.canva.dev/docs/apps/rest-apis/deep-links/#open-an-app-with-a-design).| `edit_url` only  
`return_navigation`| No| The [context to return to your platform](https://www.canva.dev/docs/apps/rest-apis/deep-links/#pass-context-for-return-navigation) with the user.| `edit_url` and `view_url`  
  
## Create a deep link

To create a deep link from a design URL:

  1. Create a target state object that contains `schema` and the properties you want to use.

For example, the following target state opens a design at its third page:
         
         {
         
           "schema": "v1",
         
           "page": {
         
             "type": "number",
         
             "page_number": 3
         
           }
         
         }

JSON

Copy

  2. Serialize the object to a JSON string, then encode the string's UTF-8 bytes as base64url. Remove any trailing `=` padding characters.

  3. Add the encoded value to the design URL as the `target_state` query parameter.
         
         https://www.canva.com/api/design/{token}/edit?target_state=eyJzY2hlbWEiOiJ2MSIsInBhZ2UiOnsidHlwZSI6Im51bWJlciIsInBhZ2VfbnVtYmVyIjozfX0

Copy




The following TypeScript example for Node.js creates a deep link from a design URL and a target state:
    
    
    import { Buffer } from "node:buffer";
    
    
    
    
    type TargetState = {
    
      // The version of the target state format
    
      schema: "v1";
    
      page?:
    
        | { type: "id"; page_id: string }
    
        | { type: "number"; page_number: number };
    
      focus?: { type: "design_editor_app"; app_id: string };
    
      return_navigation?: { correlation_state: string };
    
    };
    
    
    
    
    function createDeepLink(designUrl: string, targetState: TargetState): string {
    
      // Canva expects the target state as base64url-encoded JSON without padding.
    
      // Node's "base64url" encoding is URL safe and omits the "=" padding characters.
    
      const encodedTargetState = Buffer.from(
    
        JSON.stringify(targetState),
    
        "utf8",
    
      ).toString("base64url");
    
    
    
    
      // The URL API keeps any query parameters that are already on the design URL
    
      const url = new URL(designUrl);
    
      url.searchParams.set("target_state", encodedTargetState);
    
      return url.toString();
    
    }
    
    
    
    
    // Use the edit_url or view_url returned by the REST APIs for the design
    
    const deepLink = createDeepLink(
    
      "https://www.canva.com/api/design/{token}/edit",
    
      {
    
        schema: "v1",
    
        page: { type: "number", page_number: 3 },
    
      },
    
    );

TYPESCRIPT

Copy

If your platform doesn't use Node.js, use any base64url encoder that supports output without padding.

## Open a design at a specific page

To open a design at a page other than its first page, add the `page` property to the target state. You can use `page` with both the `edit_url` and the `view_url`.

You can identify the page by its ID or by its page number. Choose one of the following approaches:

  * **Page ID:** The link keeps targeting the same page, even if the user reorders the pages in the design.
  * **Page number:** The link targets whichever page is at that position when the user opens the link. Use this approach when the position matters more than the page itself, or when you don't have a page ID.



To get the page IDs and page numbers for a design, use the [Get design pages](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-pages/) API. Some designs don't have page IDs.

The Get design pages API is currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview APIs will not pass the review process, and can't be made available to all Canva users.



### Target a page by ID

Set `type` to `id`, and `page_id` to the `id` of the page. The `page_id` must be a non-empty string:
    
    
    {
    
      "schema": "v1",
    
      "page": {
    
        "type": "id",
    
        "page_id": "{PAGE_ID}"
    
      }
    
    }

JSON

Copy

### Target a page by number

Set `type` to `number`, and `page_number` to the position of the page in the design. The `page_number` must be an integer of `1` or greater. Page numbers start at `1`, and match the `page_number` property returned by the Get design pages API:
    
    
    {
    
      "schema": "v1",
    
      "page": {
    
        "type": "number",
    
        "page_number": 3
    
      }
    
    }

JSON

Copy

Canva looks for the page when the user opens the link, not when you create it. If pages are deleted or reordered after you create a link, the link might no longer target the page you intended, so make sure you target a page that exists in the design.

## Open an app with a design

To open an app in the Canva editor when the design opens, add the `focus` property to the target state. Set `type` to `design_editor_app`, and `app_id` to the ID of the app:
    
    
    {
    
      "schema": "v1",
    
      "focus": {
    
        "type": "design_editor_app",
    
        "app_id": "{APP_ID}"
    
      }
    
    }

JSON

Copy

Apps only open in the Canva editor, so this property only works with the `edit_url`. If you add it to a `view_url`, Canva ignores it.

A deep link doesn't grant access to an app, so use the ID of an app that the user can access.

### Find an app ID

The IDs of your own apps are listed in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).

To find the ID of an app developed by someone else, or by Canva:

  1. Navigate to the [Canva Apps page⁠(opens in a new tab or window)](https://www.canva.com/your-apps).

  2. Find the app you want to open.

  3. Click the app. A dialog containing information about the app opens, and the page URL changes.

  4. Copy the app ID from the URL. The app ID is the segment that appears after `/your-apps/`.

For example, if you click the app _Acquia DAM (Widen)_ , the URL is `https://www.canva.com/your-apps/AAFcE5stzlQ/acquia-dam-(widen)`, and the app ID is `AAFcE5stzlQ`.




## Pass context for return navigation

With return navigation, users can return from Canva to your platform using the _Return_ button in Canva. To identify what the user was doing in your platform when they return, you can pass a `correlation_state` string in the target state.

Before you add `return_navigation` to a link, turn on **Return navigation** and set a **Return URL** for your app in the Developer Portal. If return navigation is turned off, a link that contains a correlation state returns an error instead of opening the design. For the complete setup, see [Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/).

Add the `return_navigation` property to the target state, and set `correlation_state` to a string of your choice:
    
    
    {
    
      "schema": "v1",
    
      "return_navigation": {
    
        "correlation_state": "order-1234"
    
      }
    
    }

JSON

Copy

The `correlation_state` string has the following requirements:

  * Must be 50 characters or less.
  * Should include everything you need to redirect your user or update your platform's state.



You can use `return_navigation` with both the `edit_url` and the `view_url`, and it doesn't require the `focus` property.

When the user returns to your platform, Canva includes the string in the `correlation_state` claim of the signed `correlation_jwt` that it appends to your app's return URL. Always [validate the `correlation_jwt`](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/#step-3-parse-the-return-url) before you use its contents.

## Combine deep link options

A target state can contain any combination of the `page`, `focus`, and `return_navigation` properties. For example, the following target state opens a design at a specific page with an app open, and passes an order ID back to your platform when the user returns:
    
    
    {
    
      "schema": "v1",
    
      "page": {
    
        "type": "id",
    
        "page_id": "{PAGE_ID}"
    
      },
    
      "focus": {
    
        "type": "design_editor_app",
    
        "app_id": "{APP_ID}"
    
      },
    
      "return_navigation": {
    
        "correlation_state": "order-1234"
    
      }
    
    }

JSON

Copy

Use the `edit_url` for this combination, because the `focus` property only works with the `edit_url`.

Canva handles each property independently. If one of the properties is invalid, Canva still applies the others.

## How Canva handles invalid target states

If a target state is invalid, Canva doesn't return an error. Instead, it ignores the invalid parts, and opens the design:

  * If the `target_state` value isn't valid base64url, doesn't decode to a JSON object, or doesn't have a supported `schema` value, Canva ignores the entire target state.
  * If a property has a `type` that Canva doesn't recognize, or a value that isn't valid, Canva ignores that property. For example, Canva ignores a `page` property with an empty `page_id`, or a `page_number` that's less than `1`.
  * If a property isn't supported for the URL, Canva ignores that property. For example, Canva ignores a `focus` property that opens an app on a `view_url`.



These checks only cover the structure of the target state. They don't guarantee that the page still exists, or that the app is available to the user, when the user opens the link.

The exception is a link that contains a correlation state for an app that doesn't have return navigation turned on. In this case, the link returns an error, as described in [Pass context for return navigation](https://www.canva.dev/docs/apps/rest-apis/deep-links/#pass-context-for-return-navigation).

Because Canva doesn't report whether it applied a target state, test your deep links before you release them to your users.

## Use deep links with existing query parameters

Design URLs also support the `correlation_state` and `app_id` query parameters, which predate the `target_state` parameter. These parameters remain supported, so you don't need to change existing links. For new links, use `target_state`, because it supports every deep link option in a single parameter. To learn how to use the query parameters, see [Use separate query parameters](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/#use-separate-query-parameters-alternative).

The following table shows the target state property that's equivalent to each query parameter:

Query parameter| Target state property  
---|---  
`correlation_state`| `return_navigation`, with the same string as its `correlation_state`  
`app_id`| `focus`, with a `type` of `design_editor_app` and the same `app_id`  
  
If a link contains `target_state` and these query parameters, Canva handles them as follows:

  * If the target state contains a `return_navigation` property with a `correlation_state`, Canva uses it. Otherwise, Canva uses the `correlation_state` query parameter.
  * If the target state contains a `focus` property, Canva uses it and ignores the `app_id` query parameter, even if the `focus` property is invalid. Otherwise, Canva uses the `app_id` query parameter.
  * If Canva ignores the entire target state, it still uses both query parameters.



## Next steps

  * [Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)
  * [Get design pages](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-pages/)
  * [Designs](https://www.canva.dev/docs/apps/rest-apis/reference/designs/)


