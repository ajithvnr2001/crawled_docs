---
url: https://developers.cloudflare.com/changelog/post/2026-10-23-build-images-emudhra-certificates/
title: Workers Builds and Pages build images reject compromised eMudhra certificates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-27T07:31:30.214407+00:00
---

# Workers Builds and Pages build images reject compromised eMudhra certificates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-23-build-images-emudhra-certificates/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 23, 2026

## Workers Builds and Pages build images reject compromised eMudhra certificates

[Workers](https://developers.cloudflare.com/workers/)[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The private keys of [eight eMudhra intermediate certificate authorities ↗︎](https://blog.cloudflare.com/emudhra-certificate-compromise/) can be recovered, so anyone can forge a certificate for any hostname that chains to them. The Workers Builds and Pages build images now reject these certificates when your build clones your repository, installs dependencies, or makes HTTPS requests.

The updated images include patched CA certificates, Node.js 22.23.4 and 24.22.1, Bun 1.4.4, and pip 26.2.2. Build commands also run with [environment variables](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#trusted-certificates) that point older runtimes at the patched CA certificates.

#### What you need to do

Most projects need no changes. Update your project if:

  * You set `BUN_VERSION` below `1.4.4`. Older Bun versions trust the compromised certificates.
  * You set your own `SSL_CERT_FILE`, `PIP_CERT`, or `REQUESTS_CA_BUNDLE`, or set `--use-bundled-ca` in `NODE_OPTIONS`. Make sure your CA certificates do not trust the compromised intermediates.
  * Your build installs tools that ship their own CA certificates. Update them to a version that removes the compromised intermediates.



For details, refer to the build image documentation for [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/) and [Pages](https://developers.cloudflare.com/pages/configuration/build-image/).
