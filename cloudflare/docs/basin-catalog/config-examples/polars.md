---
url: https://developers.cloudflare.com/basin-catalog/config-examples/polars/
title: Polars \u00b7 Cloudflare Basin Catalog docs
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.743168+00:00
---

# Polars · Cloudflare Basin Catalog docs

> Source: https://developers.cloudflare.com/basin-catalog/config-examples/polars/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)
  3. /Connect to Iceberg engines
  4. /Polars



# Polars

Last updated Nov 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesExample usage

The following example uses [Polars ↗︎](https://pola.rs/) to create, read, and query an Iceberg table in Basin Catalog. For more information on Polars and Iceberg, refer to the [Polars documentation ↗︎](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_iceberg.html).

## Prerequisites

  * Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  * [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable the data catalog](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#enable-basin-catalog-on-a-bucket).
  * [Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) and [enable Basin Catalog](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#enable-basin-catalog-on-a-bucket) on it.
  * Install [Polars ↗︎](https://docs.pola.rs/user-guide/installation/) 2.2.0 or later with the `iceberg` extra: `pip install 'polars[iceberg]'`.



## Example usage
    
    
    import polars as pl
    from pyiceberg.catalog.rest import RestCatalog
    
    # Connect to Basin Catalog (replace the placeholders)
    catalog = RestCatalog(
        name="my_catalog",
        warehouse="<WAREHOUSE>",
        uri="<CATALOG_URI>",
        token="<TOKEN>",
    )
    
    # Create an Iceberg table (and the namespace) from a Polars DataFrame
    df = pl.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
    })
    df.lazy().sink_iceberg(
        "default.my_table",
        catalog=catalog,
        mode="append",
        create_if_not_exists=True,
        create_namespace_if_not_exists=True,
    )
    
    # Read the table back lazily and filter it
    print(
        pl.scan_iceberg("default.my_table", catalog=catalog)
        .filter(pl.col("id") > 1)
        .collect()
    )
    
    # Or query it with SQL
    ctx = pl.SQLContext()
    ctx.register_catalog("my_catalog", catalog, default_namespace="default", default=True)
    print(ctx.execute("SELECT name FROM my_table WHERE id = 2").collect())

[PreviousDuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/)[NextPyIceberg](https://developers.cloudflare.com/basin-catalog/config-examples/pyiceberg/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-catalog/config-examples/polars.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
