---
url: https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/
title: Upgrade to the modular Web SDK (v9) \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:17:10.464077+00:00
---

# Upgrade to the modular Web SDK (v9)  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/

[ Skip to main content ](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/)
  * [Deutsch](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=de)
  * [Español](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=es-419)
  * [Français](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=id)
  * [Italiano](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=it)
  * [Português](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=ja)
  * [한국어](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fidentity-platform%2Fdocs%2Fweb%2Fmodular-sdk-upgrade%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/security-and-identity-color.svg) ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [About the compat libraries](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#about_the_compat_libraries)
  * [About the upgrade process](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#about_the_upgrade_process)
  * [Get the version 9 SDK](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#get_the_version_9_sdk)
  * [Update imports to v9 compat](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#update_imports_to_v9_compat)
  * [Refactor to the modular style](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#refactor_to_the_modular_style)
    * [Example: refactoring a simple Authentication function](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#example_refactoring_a_simple_authentication_function)
  * [Update initialization code](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#update_initialization_code)
  * [Remove compat code](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#remove_compat_code)
  * [Benefits and limitations of version 9](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#benefits_and_limitations_of_version_9)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)


Was this helpful?
Send feedback 
  * On this page
  * [About the compat libraries](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#about_the_compat_libraries)
  * [About the upgrade process](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#about_the_upgrade_process)
  * [Get the version 9 SDK](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#get_the_version_9_sdk)
  * [Update imports to v9 compat](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#update_imports_to_v9_compat)
  * [Refactor to the modular style](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#refactor_to_the_modular_style)
    * [Example: refactoring a simple Authentication function](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#example_refactoring_a_simple_authentication_function)
  * [Update initialization code](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#update_initialization_code)
  * [Remove compat code](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#remove_compat_code)
  * [Benefits and limitations of version 9](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade/#benefits_and_limitations_of_version_9)


# Upgrade to the modular Web SDK (v9) Stay organized with collections  Save and categorize content based on your preferences.
Apps currently using Web SDK version 8 or earlier should consider migrating to version 9 using the instructions in this guide.
This guide assumes that you are familiar with version 8 and that you will take advantage of a module bundler such as [webpack](https://webpack.js.org/) or [Rollup](https://rollupjs.org/) for upgrading and ongoing version 9 development.
Using a module bundler in your development environment is strongly recommended. If you don't use one, you won't be able to take advantage of version 9's main benefits in reduced app size. You'll need [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/) to install the SDK.
## About the compat libraries
There are two types of libraries available for Web SDK version 9:
  * **Modular** - a new API surface designed to facilitate tree-shaking (removal of unused code) to make your web app as small and fast as possible.
  * **Compat** - a familiar API surface which is fully compatible with version 8, allowing you to upgrade to version 9 without changing all of your SDK code at once. Compat libraries have little to no size or performance advantages over their version 8 counterparts.


This guide assumes that you will take advantage of the version 9 compat libraries to facilitate your upgrade. These libraries allow you to continue using version 8 code alongside code refactored for version 9. This means you can compile and debug your app more easily as you work through the upgrade process.
For apps with a very small exposure to the Web SDK, it might be practical to refactor version 8 code without using the version 9 compat libraries. If you are upgrading such an app, you can follow the instructions in this guide for "version 9 modular" without using the compat libraries.
## About the upgrade process
Each step of the upgrade process is scoped so that you can finish editing the source for your app and then compile and run it without breakage. In summary, here's what you'll do to upgrade an app:
  1. Add the version 9 libraries and the compat libraries to your app.
  2. Update import statements in your code to v9 compat.
  3. Refactor code to the modular style.
  4. Remove the Authentication compat library and compat code for Authentication in order to realize the app size benefit.
  5. Update initialization code to the modular style.
  6. Remove all remaining version 9 compat statements and compat code from your app.


## Get the version 9 SDK
To get started, get the version 9 libraries and compat libraries using npm (latest version <https://www.npmjs.com/package/firebase>):

```
npm i firebase@13.1.0

# OR

yarn add firebase@13.1.0

```

## Update imports to v9 compat
To keep your code functioning after updating your dependency from v8 to v9, change your import statements to use the "compat" version of each import. For example:
**Before: version 8**

```
import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

```

**After: version 9 compat**

```
// v9 compat packages are API compatible with v8 code
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';

```

## Refactor to the modular style
While the version 8 APIs are based on a dot-chained namespace and service pattern, version 9's modular approach means that your code will be organized principally around **functions**. In version 9, the firebase/app package and other packages do not return a comprehensive export that contains all the methods from the package. Instead, the packages export individual functions.
In version 9, services are passed as the first argument, and the function then uses the details of the service to do the rest.
### Example: refactoring a simple Authentication function
**Before: version 9 compat**
The version 9 compat code is identical to the version 8 code, but the imports have changed. Using the compat libraries during upgrade allows you to continue using version 8 code alongside code refactored for version 9.

```
import firebase from "firebase/compat/app";
import "firebase/compat/auth";

const auth = firebase.auth();
auth.onAuthStateChanged(user => {
  // Check for user status
});

```

**After: version 9 modular**
The `getAuth` function takes `firebaseApp` as its first parameter. The `onAuthStateChanged` function is not chained from the auth instance as it would be in version 8; instead, it's a free function which takes `auth` as its first parameter.

```
import { getAuth, onAuthStateChanged } from "firebase/auth";

const auth = getAuth(firebaseApp);
onAuthStateChanged(auth, user => {
  // Check for user status
});

```

## Update initialization code
Update your app's initialization code to use new modular version 9 syntax. It is important to update this code _after_ you have completed refactoring all the code in your app; this is because `firebase.initializeApp()` initializes global state for both the compat and modular APIs, whereas the modular `initializeApp()` function initializes only the state for modular.
**Before: version 9 compat**

```
import firebase from "firebase/compat/app"

firebase.initializeApp({ /* config */ });

```

**After: version 9 modular**

```
import { initializeApp } from "firebase/app"

const firebaseApp = initializeApp({ /* config */ });

```

## Remove compat code
To realize the size benefits of the version 9 modular SDK, you should eventually convert all invocations to the modular style shown above and remove all of the `import "firebase/compat/*` statements from your code. When you are done, there should be no more references to the `firebase.*` global namespace or any other code in the version 8 SDK style.
## Benefits and limitations of version 9
The fully modularized version 9 has these advantages over earlier versions:
  * Version 9 enables a dramatically reduced app size. It adopts the modern JavaScript Module format, allowing for "tree shaking" practices in which you import only the artifacts your app needs. Depending on your app, tree-shaking with version 9 can result in 80% less kilobytes than a comparable app built using version 8.
  * Version 9 will continue to benefit from ongoing feature development, while version 8 will be frozen at a point in the future.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
