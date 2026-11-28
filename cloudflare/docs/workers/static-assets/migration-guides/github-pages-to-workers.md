---
url: https://developers.cloudflare.com/workers/static-assets/migration-guides/github-pages-to-workers/
title: Migrate from GitHub Pages to Workers \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:28.093607+00:00
---

# Migrate from GitHub Pages to Workers · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/static-assets/migration-guides/github-pages-to-workers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Static Assets](https://developers.cloudflare.com/workers/static-assets/)

  4. /Migration Guides
  5. /Migrate from GitHub Pages to Workers



# Migrate from GitHub Pages to Workers

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Prepare your repository Plain HTML or JavaScript static sites Jekyll sites hosted on GitHub Pages2\. Create a Wrangler configuration file3\. Connect your repository to Workers Builds4\. Migrate your custom domainRelated resources

This guide walks you through migrating a static site or [Jekyll ↗︎](https://jekyllrb.com/) site from [GitHub Pages ↗︎](https://docs.github.com/en/pages) to Cloudflare Workers with [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/) and [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/).

## 1\. Prepare your repository

### Plain HTML or JavaScript static sites

Confirm your project's build command (if any) and static output directory (for example, `dist`, `public`, `build`, or `.` for pre-built HTML files).

### Jekyll sites hosted on GitHub Pages

GitHub Pages preinstalls a default set of Jekyll plugins even when no `Gemfile` is present. If your Jekyll repository does not already contain a `Gemfile` and `Gemfile.lock`, create them so Workers Builds can install your dependencies:

  1. In your repository root, initialize a `Gemfile`:
         
         bundle init

  2. Add the `github-pages` gem to your `Gemfile`:

Gemfileruby
         
         source "https://rubygems.org"
         
         gem "github-pages", group: :jekyll_plugins

  3. Generate `Gemfile.lock` and commit both files:
         
         bundle update
         git add Gemfile Gemfile.lock
         git commit -m "Add Gemfile for Jekyll build"




## 2\. Create a Wrangler configuration file

In the root of your repository, create a `wrangler.jsonc` file pointing `assets.directory` to your site's output folder (for example, `./_site` for Jekyll or `.` for plain HTML in the repository root):
    
    
    {
    	"name": "<your-project-name>",
    	// Set this to today's date
    	"compatibility_date": "2026-11-28",
    	"assets": {
    		"directory": "./_site"
    	}
    }
    
    
    name = "<your-project-name>"
    # Set this to today's date
    compatibility_date = "2026-11-28"
    
    [assets]
    directory = "./_site"

If your site is a Single Page Application (SPA) rather than a static site, add `"not_found_handling": "single-page-application"` inside the `assets` object. If you have a custom `404.html` page, add `"not_found_handling": "404-page"`. Refer to [Static Assets routing](https://developers.cloudflare.com/workers/static-assets/routing/) for details.

Commit and push `wrangler.jsonc` to your GitHub repository.

## 3\. Connect your repository to Workers Builds

  1. Follow [Connect a new Worker](https://developers.cloudflare.com/workers/ci-cd/builds/#connect-a-new-worker) to connect your GitHub repository to Workers Builds.
  2. Set the **Build command** for your site: 
     * **Jekyll** : `bundle exec jekyll build`
     * **Plain HTML** : Leave blank
     * **Other static site generators** : Your framework build command (for example, `npm run build` or `hugo`)
  3. Keep the default **Deploy command** (`npx wrangler deploy`) and select **Save and Deploy**.



After the initial build completes, every push to your production branch deploys automatically, and pull requests receive [Preview URLs](https://developers.cloudflare.com/workers/previews/).

## 4\. Migrate your custom domain

Workers [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) support domains whose DNS is managed by Cloudflare.

  1. Verify your deployed site on its `*.workers.dev` subdomain.
  2. In your GitHub repository settings under **Pages** , remove the custom domain so GitHub no longer serves it.
  3. In the Cloudflare dashboard under **DNS** > **Records** , remove the `CNAME` or `A` records pointing to `<your-username>.github.io` or GitHub Pages IP addresses.
  4. Follow [Add a Custom Domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/#add-a-custom-domain) to attach your domain to your Worker.



## Related resources

  * [Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/)
  * [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/)
  * [Configure custom headers](https://developers.cloudflare.com/workers/static-assets/headers/) and [redirects](https://developers.cloudflare.com/workers/static-assets/redirects/)



[PreviousMigrate from Firebase Hosting to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/firebase-to-workers/)[NextMigrate from Netlify to Workers](https://developers.cloudflare.com/workers/static-assets/migration-guides/netlify-to-workers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/migration-guides/github-pages-to-workers.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
