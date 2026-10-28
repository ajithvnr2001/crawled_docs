---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/extension-framework-troubleshooting/
title: Troubleshooting the Looker extension framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:21.871076+00:00
---

# Troubleshooting the Looker extension framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/extension-framework-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting the Looker extension framework Stay organized with collections  Save and categorize content based on your preferences. 

The Looker [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) lets you build custom JavaScript and TypeScript applications and visualizations that run inside Looker. Extensions run in a sandboxed `iframe` and interact with your Looker instance through the Extension SDK. If you encounter issues with a custom extension—such as a blank page or error message inside the `iframe`, browser console JavaScript or Cross-Origin Resource Sharing (CORS) errors, failed Looker API requests (`4xx` or `5xx` status codes), or `manifest.lkml` configuration errors—this document helps you troubleshoot and resolve them.

**Note:** This document covers custom-developed extensions that are built with the Looker extension framework. It doesn't cover core Looker features unrelated to the extension framework, general LookML development outside of an extension, or third-party extensions that are installed from the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace).

## Prerequisites and common configuration requirements

Before you begin troubleshooting, verify that your environment, LookML project, and user account meet the requirements for running a Looker extension:

  * **Extension framework enabled:** A Looker administrator must enable the [**Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) setting under **Admin > Platform > Extension Framework**.
  * **LookML project and model configuration:** Every extension requires a [LookML project](https://docs.cloud.google.com/looker/docs/lookml-project-files) that includes the following components: 
    * A [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) that's configured with a valid [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) parameter.
    * A [project manifest file](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files) (`manifest.lkml`) that contains an [`application`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application) declaration.
    * A configured [Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection).
  * **Manifest entitlements:** The `application` declaration in the `manifest.lkml` file must explicitly define all [`entitlements`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements) that the extension requires, such as `core_api_methods` for Looker API calls or `external_api_urls` for requests to external domains. An extension won't run without an `entitlements` block.
  * **User permissions:** Users must have [extension permissions](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions) (such as `access_data`, `explore`, or `develop`) for a model set that includes the extension's LookML model. To build an extension, developers require LookML `develop` permissions.
  * **Diagnostic tools and environment details:** Have the following details and tools ready before you begin troubleshooting: 
    * Your Looker instance URL, the LookML project name, and the `application` name that's declared in `manifest.lkml`.
    * Access to your web browser's developer tools (**Console** and **Network** tabs) on the client machine.
    * During local development, access to the terminal that runs your local development server.
    * For `5xx` server errors on Looker API calls, access to Looker instance logs (`looker.log` on customer-hosted instances, or Logs Explorer in Cloud Logging in the Google Cloud console for Looker (Google Cloud core) instances).



## Debugging tree

Use the following decision tree to begin troubleshooting Looker extension framework issues:

The following sections describe the scenarios in the tree in further detail.

## Inspect browser console and network logs

Because Looker extensions run client-side in your browser, start troubleshooting by inspecting your browser's developer tools for JavaScript errors, security policy violations, and failed HTTP requests.

### Check the browser console for errors

To identify client-side errors that prevent the extension from loading or running:

  1. In Looker, open the page where the extension loads.
  2. Right-click anywhere on the page and select **Inspect** (or press `Control+Shift+I` on Windows and Linux, or `Command+Option+I` on macOS).
  3. In the developer tools panel, select the **Console** tab.
  4. Refresh the page to capture errors that occur during the initial load.
  5. Inspect any red error messages in the console: 
     * **JavaScript runtime errors (such as`Uncaught TypeError` or `ReferenceError`):** Note the file and line number in the stack trace, and see Troubleshoot runtime JavaScript and logic errors.
     * **`401 Unauthorized` or `403 Forbidden` errors:** Indicate authentication or permission issues. See Troubleshoot authentication and API access.
     * **`404 Not Found` errors:** Indicate that the extension's JavaScript bundle or a requested resource couldn't be found. Verify your manifest configuration and local development server.
     * **CORS or Content Security Policy (CSP) errors:** Indicate that the browser blocked a cross-origin request or resource. See Troubleshoot networking, CORS, and security policies.



### Inspect the Network tab for failed requests

To analyze HTTP requests that are made by the extension for JavaScript bundles, assets, or API endpoints, follow these steps:

  1. In the browser developer tools panel, select the **Network** tab.
  2. Select the **Disable cache** checkbox so the browser doesn't load stale cached resources.
  3. Refresh the page where the extension loads.
  4. Check the list of network requests for any `4xx` or `5xx` status codes, and select a failed request to inspect its **Headers** , **Payload** , and **Response** tabs: 
     * **`404` on the extension bundle (such as `bundle.js`):** Verify that the development server is running and that the `url` or `file` parameter in `manifest.lkml` is accurate.
     * **`401` or `403` on a Looker API request:** Investigate authentication, permissions, and entitlements.
     * **`400` or `422` on an API request:** Inspect the **Payload** and **Response** tabs to identify malformed JSON or invalid request parameters.
     * **`5xx` server errors:** Indicate server-side errors on the Looker instance. Check `looker.log` on customer-hosted instances or Logs Explorer in the console for Looker (Google Cloud core) instances to find entries with matching timestamps.



If no errors appear in the **Console** or **Network** tabs, or if you need to verify how Looker loads the extension, proceed to the next section.

## Verify manifest and project configuration

The [`application`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application) declaration in your project's `manifest.lkml` file controls how Looker loads the extension and which resources the extension can use. Misconfigurations in `manifest.lkml` are a common cause of loading and API failures:

  * **Verify the`url` or `file` parameter:** In the Looker IDE, open your project's `manifest.lkml` file and inspect the `application` declaration: 
    * An `application` declaration must include either a [`url`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#url) parameter or a [`file`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#file) parameter, but not both.
    * **During local development:** Verify that the `url` parameter matches the exact protocol (`http` or `https`), hostname, port, and path that are served by your local development server (for example, `https://localhost:8080/bundle.js`).
    * **In production:** Verify that you updated the `application` declaration from the local development `url` to the production `file` path in your LookML project (for example, `file: "apps/bundle.js"`) or production bundle URL.
  * **Verify`manifest.lkml` entitlements:** Review the [`entitlements`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements) block in your `application` declaration. An extension can't use a Looker resource or external domain unless that entitlement is explicitly declared, as follows: 
    * **`core_api_methods`:** Must list every Looker API method that your extension calls (for example, `core_api_methods: ["me", "all_looks", "run_inline_query"]`).
    * **`external_api_urls`:** Must list all external, non-Looker domains that the extension requests directly or through the proxy.
    * **Additional entitlements:** Verify whether your extension requires `local_storage`, `navigation`, `new_window`, `new_window_external_urls`, `use_form_submit`, `use_embeds`, `use_downloads`, `use_iframes`, `use_clipboard`, `oauth2_urls`, `global_user_attributes`, or `scoped_user_attributes`.
  * **Validate, commit, and deploy:** After editing `manifest.lkml`, click **Validate LookML** , commit your changes, and click **Deploy to Production** so the updated configuration takes effect.



## Troubleshoot the local development server and environment

When you're developing an extension locally by using the `url` parameter in `manifest.lkml`, your local development server must be running and accessible from your browser:

  * **Confirm that the development server is running:** Check the terminal window where you started the development server (for example, using `yarn develop` or `npm start`): 
    * Verify that the build compiled without errors and displays a listening message (such as `webpack compiled successfully` or `listening on localhost:8080`).
    * If the server isn't running, start it with `yarn develop` or `npm start`.
    * If the server exited with a syntax error or missing dependency error, resolve the code error or run `yarn install` (or `npm install`) to install missing packages.
    * If the server fails with a port conflict (`EADDRINUSE`), stop the other process that's using that port, or configure your development server and `manifest.lkml` `url` parameter to use a different port.
  * **Open the extension URL directly in your browser:** Copy the `url` value from `manifest.lkml` (for example, `https://localhost:8080/bundle.js`) and open it in a new browser tab: 
    * **Untrusted self-signed SSL certificate:** Local development servers frequently use self-signed SSL certificates. If your browser displays a certificate security warning, select **Advanced** and proceed to `localhost` to trust the certificate for your browser session. Until the certificate is trusted, the browser blocks the bundle from loading inside the Looker `iframe`.
    * **Connection refused or blocked:** If the browser can't reach the URL, verify that no local firewall or endpoint security software is blocking connections to `localhost` on the configured port.



## Troubleshoot networking, CORS, and security policy issues

Web browsers enforce the Same-Origin Policy, which prevents Looker from loading extension resources or calling external servers on a different origin unless Cross-Origin Resource Sharing (CORS) headers and security policies are configured:

  * **Identify CORS errors in the browser console:** Look for error messages in the **Console** tab containing `Cross-Origin Resource Sharing`, `CORS`, `has been blocked by CORS policy`, or missing `Access-Control-Allow-Origin` headers.
  * **Configure local development server CORS headers:** If you use `webpack-dev-server` (or a similar bundler), ensure that the `devServer` configuration in `webpack.config.js` includes the `Access-Control-Allow-Origin` header: `javascript devServer: { headers: { "Access-Control-Allow-Origin": "*" } }`
  * **Configure production hosting and external API CORS headers:** If your extension loads assets or requests data from an external service (such as Cloud Storage, Amazon S3, or a custom backend server), configure the hosting service to return the `Access-Control-Allow-Origin` header that allows your Looker instance domain. Also verify that no network proxy or firewall is stripping CORS headers from the response, and ensure that the external domain is listed in `external_api_urls` in `manifest.lkml`.
  * **Check Content Security Policy (CSP) and Enhanced Extension Loading:** If you encounter CSP violations when loading an extension, check the [**Enhanced Extension Loading**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework#enhanced_extension_loading) setting under **Admin > Platform > Extension Framework**.



## Troubleshoot authentication and API access issues

Extensions interact with the Looker API on behalf of the signed-in user through the Extension SDK. If API calls fail with `401 Unauthorized` or `403 Forbidden` status codes in the **Network** tab, investigate the following:

  * **Distinguish between`401` and `403` errors:**
    * **`401 Unauthorized`:** The request wasn't authenticated. This error typically occurs if the Extension SDK wasn't initialized properly or if the extension attempted an API call before the SDK completed its authentication handshake.
    * **`403 Forbidden`:** The request was authenticated, but either the signed-in user lacks the required Looker permissions or the extension's `manifest.lkml` doesn't include the called method in `core_api_methods`.
  * **Verify user roles and permissions:** In **Admin > Users** and **Admin > Roles**, check the signed-in user's assigned roles, permission sets, and model sets: 
    * Confirm that the user has [permissions to use the extension](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions#permissions_to_use_extensions), including `access_data` (and `explore` or `develop` as needed) for a model set that contains the extension's LookML model and any models that are queried by the extension.
    * Confirm that the user's role includes the specific permissions that are required by each Looker API endpoint that the extension calls.
  * **Ensure that the SDK context is ready before calling the API:** Verify that your extension code waits for the Extension SDK context to initialize before invoking API methods.



## Troubleshoot the Extension SDK and dependencies

Issues with npm or Yarn package installation or missing SDK provider components can prevent an extension from compiling or connecting to Looker:

  * **Verify Node.js module installation:** In your terminal, go to the root directory of your extension project and check the `node_modules` directory: 
    1. If `node_modules` is missing or dependencies appear corrupted, delete the `node_modules` directory and the lockfile (`yarn.lock` or `package-lock.json`).
    2. Optional: If package installation fails repeatedly, clear your package manager cache (for example, run `npm cache clean --force`).
    3. Verify that your installed Node.js version is compatible with the project's requirements, and then run `yarn install` or `npm install` to perform a clean installation.
  * **Check`ExtensionProvider` initialization:** Open your extension's main entry file (such as `App.js` or `index.js`) and confirm that `<ExtensionProvider>` (imported from `@looker/extension-sdk-react`) wraps the application components that need the Looker SDK context: `javascript ReactDOM.render( <ExtensionProvider> <App /> </ExtensionProvider>, document.getElementById('root') );` If `<ExtensionProvider>` is missing or if you placed it following components that call the SDK, child components can't access the SDK context.



## Troubleshoot runtime JavaScript and logic errors

If the extension's configuration, development server, permissions, and SDK setup are valid, the issue might be a runtime error in the extension's custom JavaScript or TypeScript code:

  * **Analyze console stack traces:** In the browser's **Console** tab, locate the red error message and click the expander arrow to view the full stack trace. The top lines of the stack trace identify the file and line number in your source code where the error occurred. Click the file link (for example, `MyComponent.js:42`) to jump directly to that line in the **Sources** tab.
  * **Check for undefined or null values:** For errors such as `TypeError: Cannot read properties of undefined`, verify that asynchronous API responses or props have finished loading before your code reads nested properties. Add defensive checks (such as `if (myObject && myObject.property)` or optional chaining `myObject?.property`).
  * **Verify API response formats:** Confirm that your code handles the actual data structure that's returned by Looker API calls (for example, verifying whether a response payload is an object or an array before calling array methods).
  * **Debug with breakpoints and logging:** In the browser's **Sources** tab, set breakpoints prior to the failing line to pause execution and inspect variable values in real time, or add `console.log()` statements to trace the execution flow.



## Verify Looker version compatibility

Major feature updates or changes in Looker can require a compatible version of the Looker Extension SDK:

  1. Check the version of `@looker/extension-sdk` (and `@looker/extension-sdk-react`, if used) in your extension project's `package.json` file.
  2. In the Looker web interface, check your instance's current release version under **Help > About** or **Admin > General > Settings**.
  3. Compare your Looker release version with the compatibility notes in the [`@looker/extension-sdk` documentation](https://www.npmjs.com/package/@looker/extension-sdk).
  4. If your Looker instance was recently upgraded and the extension uses an outdated SDK—or if the extension uses a newer SDK feature that isn't supported by an earlier Looker version—update the SDK package to a compatible version: `bash npm install @looker/extension-sdk@latest` After updating the package, reinstall dependencies and restart your development server.



## Gather diagnostic information

If you can't resolve the issue after following the troubleshooting steps, gather the following information before contacting Support:

  1. **Looker instance and project information:**
     * Looker instance URL (for example, `instance_name.looker.com`).
     * Looker release version.
     * Name of the LookML project that contains the extension and the `application` name in `manifest.lkml`.
  2. **Extension configuration and SDK details:**
     * A copy or screenshot of the `application` declaration in the `manifest.lkml` file.
     * The version of `@looker/extension-sdk` that is specified in `package.json`.
     * Whether the extension is running from a local development server (`url`) or deployed in production (`file`).
  3. **Error logs and screenshots:**
     * Screenshots or full text of errors from the browser's **Console** and **Network** tabs (including request headers and response payloads for failed `4xx` or `5xx` requests).
     * If API calls consistently return `5xx` server errors, matching log excerpts from `looker.log` (for customer-hosted instances) or Logs Explorer in Logging (for Looker (Google Cloud core) instances).
  4. **Troubleshooting summary and reproduction steps:**
     * A summary of the troubleshooting steps that you've already performed and their outcomes.
     * Exact steps to reproduce the issue, or a minimal reproducible example if you suspect an issue in the Looker extension framework or Extension SDK.



## Contact Support

If you have verified all the previous steps and the issue is still not resolved:

  * [Contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) and provide the diagnostic information that you gathered in the previous section. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
