---
url: https://developers.cloudflare.com/waf/tools/lists/create-dashboard/
title: Create a list in the dashboard \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:48.085317+00:00
---

# Create a list in the dashboard · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/lists/create-dashboard/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

Additional tools

  4. /[Lists](https://developers.cloudflare.com/waf/tools/lists/)
  5. /Create in the dashboard



# Create a list in the dashboard

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/lists/create-dashboard/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd items to a list Add items to a list manually Add items using a CSV file

To create a list, follow these steps:

  1. In the Cloudflare dashboard, go to the **Settings** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
  2. Go to **Lists**.

  3. Select **Create new list**.

  4. Enter a name for your list, observing the [list name guidelines](https://developers.cloudflare.com/waf/tools/lists/#list-names).

  5. (Optional) Enter a description for the list, with a maximum length of 500 characters.

  6. For **Content type** , select the [type of list](https://developers.cloudflare.com/waf/tools/lists/custom-lists/) you are creating.

  7. Select **Create**.

  8. Follow the instructions in the next section to add items to the list.




## Add items to a list

  1. (Optional) If you wish to add items to an existing list:

     1. Go to the **Settings** page.

[ Go to **Configurations** ↗ ](https://dash.cloudflare.com/?to=/:account/configurations)
     2. Go to **Lists**.

     3. Select **Edit** next to the list you want to edit.

  2. Select **Add items**.

  3. To add items to the list manually, use the available text inputs on the page.

  4. To add items using a CSV file, select **Upload CSV**.




Notes

Cloudflare will apply the following rules when you add items to an existing list (either manually or via CSV file):

  * Do not remove any existing list items before updating/adding items.
  * Update items that were already in the list.
  * Add items that were not present in the list.



### Add items to a list manually

  1. In the **Add items to list** page, enter values for the different fields (the exact fields depend on the list type).

As you enter information into a text input, a new row of inputs displays below the current one. To delete any of the items that you have entered, select **X**.

  2. Select **Add to list**.




### Add items using a CSV file

To add items to a list by uploading a CSV file:

  1. In the **Add items to list** page, select **Upload CSV**.

  2. Browse to the location of the CSV file, select the file, and then select **Open**. The displayed items in the page will include the items loaded from the CSV file.

The exact CSV file format depends on the list type. Refer to [Custom list types](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#custom-list-types) for details.

  3. You can continue to edit the items in the list before adding them:

     * To delete any of the items you have entered, select **X**.
     * To add extra items manually, enter the information in the text inputs.
  4. Select **Add to list**.




[PreviousManaged Lists](https://developers.cloudflare.com/waf/tools/lists/managed-lists/)[NextUse lists in expressions](https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/lists/create-dashboard.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
