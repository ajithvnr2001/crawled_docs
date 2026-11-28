---
url: https://developers.cloudflare.com/pages/framework-guides/deploy-a-sphinx-site/
title: Sphinx \u00b7 Cloudflare Pages docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:32.854668+00:00
---

# Sphinx · Cloudflare Pages docs

> Source: https://developers.cloudflare.com/pages/framework-guides/deploy-a-sphinx-site/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Pages](https://developers.cloudflare.com/pages/)
  3. /Framework guides
  4. /Sphinx



# Sphinx

Last updated Nov 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCreate a Sphinx projectBefore you continueCreate a GitHub repositoryDeploy with Cloudflare PagesLearn more

Note

Starting a new static documentation site? You can also deploy static sites to [Cloudflare Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/) with Git-connected [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/).

[Sphinx ↗︎](https://www.sphinx-doc.org/) is a documentation generator written in Python. In this guide, you will create a new Sphinx project and deploy it using Cloudflare Pages.

## Prerequisites

  * [Python 3 ↗︎](https://www.python.org/downloads/) (Cloudflare Pages Build Image v3 includes Python 3.13 by default; refer to [Build image](https://developers.cloudflare.com/pages/configuration/build-image/) for supported versions).
  * [`pip` ↗︎](https://pypi.org/project/pip/) for installing Python packages.



## Create a Sphinx project

  1. Create a new project directory, set up a Python virtual environment, and install Sphinx:


    
    
    mkdir my-sphinx-project
    cd my-sphinx-project
    python3 -m venv .venv
    source .venv/bin/activate
    pip install sphinx

  2. Record your dependencies in a `requirements.txt` file so Cloudflare Pages automatically installs Sphinx during builds:


    
    
    echo "sphinx" > requirements.txt

  3. Run `sphinx-quickstart` to scaffold your documentation site:


    
    
    sphinx-quickstart

When prompted, answer the setup questions:
    
    
    Separate source and build directories (y/n) [n]: y
    Project name: <Your project name>
    Author name(s): <Your author name>
    Project release []: <Leave blank or provide a version>
    Project language [en]: <Leave blank for en or provide a language code>

  4. Add a `.gitignore` file so your local virtual environment and build output are not committed to Git:

.gitignoretxt
    
    
    .venv/
    build/

This creates a project structure with `requirements.txt`, `Makefile`, and a `source/` directory containing `conf.py` and `index.rst`. For more details on authoring documentation with Sphinx, refer to the [Sphinx documentation ↗︎](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

## Before you continue

All of the framework guides assume you already have a fundamental understanding of [Git ↗︎](https://git-scm.com/). If you are new to Git, refer to this [summarized Git handbook ↗︎](https://guides.github.com/introduction/git-handbook/) on how to set up Git on your local machine.

If you clone with SSH, you must [generate SSH keys ↗︎](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) on each computer you use to push or pull from GitHub.

Refer to the [GitHub documentation ↗︎](https://guides.github.com/introduction/git-handbook/) and [Git documentation ↗︎](https://git-scm.com/book/en/v2) for more information.

## Create a GitHub repository

Create a new GitHub repository by visiting [repo.new ↗︎](https://repo.new). After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:
    
    
    git init
    git remote add origin https://github.com/<your-gh-username>/<repository-name>
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git push -u origin main

## Deploy with Cloudflare Pages

To deploy your site to Pages:

  1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

[ Go to **Workers & Pages** ↗ ](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
  2. Select **Create application**.

  3. Select the **Pages** tab.

  4. Select **Import an existing Git repository**.

  5. Select the new GitHub repository that you created and then select **Begin setup**.

  6. In the **Set up builds and deployments** section, provide the following information:




Configuration option | Value  
---|---  
Production branch | `main`  
Build command | `make html`  
Build directory | `build/html`  
  
Cloudflare Pages detects `requirements.txt` and installs your Python dependencies before running `make html`. If you need a specific Python version rather than the build image default, set the `PYTHON_VERSION` environment variable as described in [Override default versions](https://developers.cloudflare.com/pages/configuration/build-image/#override-default-versions).

Note

For the complete guide to deploying your first site to Cloudflare Pages, refer to the [Get started guide](https://developers.cloudflare.com/pages/get-started/).

After deploying your site, you will receive a unique subdomain for your project on `*.pages.dev`. Every time you commit new code to your Sphinx site, Cloudflare Pages automatically rebuilds your project and deploys it.

You will also get access to [preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/) on new pull requests, so you can preview how changes look to your site before deploying them to production.

## Learn more

By completing this guide, you have successfully deployed your Sphinx site to Cloudflare Pages. To get started with other frameworks, [refer to the list of Framework guides](https://developers.cloudflare.com/pages/framework-guides/).

[PreviousSolidStart](https://developers.cloudflare.com/pages/framework-guides/deploy-a-solid-start-site/)[NextStatic HTML](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/pages/framework-guides/deploy-a-sphinx-site.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
