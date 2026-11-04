---
url: https://docs.comfy.org/custom-nodes/js/primevue-removal-migration/
title: PrimeVue Removal Migration for Frontend Extensions - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:51.061537+00:00
---

# PrimeVue Removal Migration for Frontend Extensions - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/primevue-removal-migration/

## On this page

Back to top

  * Extensions that render PrimeVue components
  * Extensions that read --p-* variables
  * Tooltips
  * Deprecated variable names



Migration Guides

# PrimeVue Removal Migration for Frontend Extensions

Copy pageCopy page

Replace $primevue, PrimeVue components, —p-* CSS variables and PrimeVue tooltip selectors after the ComfyUI frontend removed PrimeVue.

Copy pageCopy page

ComfyUI frontend no longer installs PrimeVue. The host app does not call `app.use(PrimeVue)`, so extensions lose three things they may have relied on:

  * the `$primevue` global property on the host Vue app;
  * the PrimeVue theme stylesheet, so PrimeVue components that an extension renders inside the host app render unstyled; and
  * every global `--p-*` CSS variable, such as `--p-primary-color`, `--p-surface-*`, `--p-text-color`, `--p-content-background` and `--p-form-field-border-color`.



## 

​

Extensions that render PrimeVue components

Do not rely on the host app’s PrimeVue instance. Either replace the PrimeVue components with your own markup, or create your own Vue app for your UI and install PrimeVue and its theme on that app.

## 

​

Extensions that read `--p-*` variables

Replace them with the design system theme variables, which follow the active light or dark theme and the active color palette:

PrimeVue variable| Theme variable  
---|---  
`--p-primary-color`| `--primary`  
`--p-text-color`| `--foreground`  
`--p-text-muted-color`| `--muted-foreground`  
`--p-content-background`| `--background`  
`--p-surface-*` (panels, elevated areas)| `--secondary`  
`--p-content-border-color`, `--p-form-field-border-color`| `--border`  
  
## 

​

Tooltips

The global `v-tooltip` directive is gone, and tooltips no longer render the PrimeVue DOM:

  * `.p-tooltip` and `.p-tooltip-text`
  * the `data-pd-tooltip` attribute
  * the `$_ptooltip*` element properties

An open tooltip now renders one element with `data-slot="tooltip-content"`, portaled to the end of `document.body`. It exists only while the tooltip is open. Extensions that hide tooltips during their own UI should target `[data-slot="tooltip-content"]` instead of `.p-tooltip`. The `--node-component-tooltip*` CSS variables are also removed from the design system stylesheet. Use the theme variables instead: `--background`, `--foreground` and `--border`. The older names `--base-background`, `--base-foreground` and `--border-default` are deprecated; see Deprecated variable names.

## 

​

Deprecated variable names

Earlier versions of these notes pointed at older design system names. They still resolve, but they are deprecated and will be removed in a future release. Move to the theme variable now:

Deprecated name| Theme variable  
---|---  
`--base-background`| `--background`  
`--base-foreground`| `--foreground`  
`--border-default`| `--border`  
`--primary-background`| `--primary`  
`--secondary-background`| `--secondary`  
`--component-node-background`| `--node`  
  
PrimeIcons are still loaded, so existing `pi pi-*` icon classes keep working, but they are being phased out. Don’t add new uses.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/primevue-removal-migration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/primevue-removal-migration)

[Node geometry migration](https://docs.comfy.org/custom-nodes/js/node-geometry-migration)[Node replacement](https://docs.comfy.org/custom-nodes/backend/node-replacement)
