---
url: https://developers.cloudflare.com/containers/concepts/placement/
title: Placement \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:03.245377+00:00
---

# Placement · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/concepts/placement/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /[Concepts](https://developers.cloudflare.com/containers/concepts/)
  4. /Placement



# Placement

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPlacement and routingJurisdictionPlacement constraints for the default policy Regional constraints Jurisdictional constraints Configure placement

With the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy), your Durable Object starts a Container instance on demand through `ctx.container.start()`. Cloudflare selects a suitable location based on request routing, available capacity, and image availability.

## Placement and routing

A Container and its associated Durable Object are not guaranteed to run in the same location. Placement balances request routing with startup speed, so the Container may start in another eligible location.

Requests to a running Container continue to reach that instance, regardless of where the requests originate. After the Container stops, its next start may use a different location.

## Jurisdiction

Container placement uses the jurisdiction of its associated Durable Object to determine eligible locations. Configure the Durable Object namespace's jurisdiction using the [Durable Objects data location API](https://developers.cloudflare.com/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction).

The `durable_object` policy does not support application-level regional constraints or application-level EU and US jurisdiction settings. Set jurisdiction through the Durable Object namespace.

Image and snapshot storage

Jurisdiction controls where Container instances run. It does not determine where Container images or [snapshots](https://developers.cloudflare.com/containers/guides/snapshots/) are stored. If storage location is part of your requirement, confirm the supported image workflow with your account team before you deploy.

For Data Localization Suite support, refer to [Product compatibility](https://developers.cloudflare.com/data-localization/compatibility/#developer-platform).

## Placement constraints for the default policy

Applications that use the [`default` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-default-scheduling-policy) can set application-level placement constraints in their Wrangler configuration.

### Regional constraints

Use the `regions` constraint to limit container placement to specific geographic areas:

Region | Description | Notes  
---|---|---  
`ENAM` | Eastern North America |   
`WNAM` | Western North America |   
`EEUR` | Eastern Europe |   
`WEUR` | Western Europe |   
`APAC` | Asia Pacific |   
`SAM` | South America |   
`ME` | Middle East | Limited capacity  
`OC` | Oceania | Limited capacity  
`AFR` | Africa | Limited capacity  
  
Limited capacity regions (ME, OC, AFR) cannot be used exclusively. Include at least one other region, or contact support for dedicated access.

### Jurisdictional constraints

Use the `jurisdiction` constraint to restrict containers to compliance boundaries:

Jurisdiction | Regions | Use case  
---|---|---  
`eu` | EEUR, WEUR | EU data residency  
`us` | ENAM, WNAM | US data residency  
`fedramp` | ENAM, WNAM | FedRAMP regions  
  
When you specify both `jurisdiction` and `regions`, the regions must be valid for that jurisdiction. For example, specifying `jurisdiction: "eu"` with `regions: ["ENAM"]` is invalid.

### Configure placement

Set placement constraints in your Wrangler configuration:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "containers": [
        {
          "class_name": "MyContainer",
          "image": "docker.io/my-org/my-image:latest",
          "constraints": {
            "regions": [
              "ENAM",
              "WNAM"
            ],
            "jurisdiction": "fedramp"
          }
        }
      ]
    }
    
    
    [[containers]]
    class_name = "MyContainer"
    image = "docker.io/my-org/my-image:latest"
    
    [containers.constraints]
    regions = ["ENAM", "WNAM"]
    jurisdiction = "fedramp"

Refer to [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/) for more details on how placement affects container startup and routing.

[PreviousLifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/)[NextDeploy Containers](https://developers.cloudflare.com/containers/guides/deploy/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/concepts/placement.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
