---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/
title: Install PostGIS for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:37:52.643916+00:00
---

# Install PostGIS for AlloyDB Omni  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fredhat-orchestrator%2F18.3.0%2Fdocs%2Finstall-postgis%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/#before-you-begin)
  * [Add PostGIS to your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/#add-postgis)


This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)


Was this helpful?
Send feedback 
#  Install PostGIS for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/#before-you-begin)
  * [Add PostGIS to your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis/#add-postgis)


Select a documentation version:  18.3.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-postgis)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-postgis)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-postgis)


To store, index, and query geospatial data in AlloyDB Omni, you can manually add the [PostGIS extension](https://postgis.net/) to your installation.
## Before you begin
[Install AlloyDB Omni using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).
## Add PostGIS to your AlloyDB Omni installation
To add the PostGIS extension to your AlloyDB Omni cluster, follow these steps manually on all database nodes including read pool nodes in your cluster: 
  1. Initialize Red Hat Subscription Manager on the VM where you installed the AlloyDB Omni server:

```
sudo dnf install -y subscription-manager
sudo subscription-manager register --username "RHSM_USER" --password "RHSM_PASS" --auto-attach --force

```

Replace the following:
     * `RHSM_USER`: the Red Hat Subscription Manager user.
     * `RHSM_PASS`: the Red Hat Subscription Manager password.
  2. Enable the CodeReady Builder repository:

```
sudo subscription-manager repos --enable="codeready-builder-for-rhel-9-$ARCH-rpms"

```

Replace `ARCH` with the RHEL architecture that you want to use—for example, `x86_64`.
  3. Add the PostgreSQL Yum repository:

```
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm

```

  4. Install the PostGIS extension:

```
sudo dnf install -y postgis35_18

```

  5. Create required symlinks so the extensions are in the expected paths:

```
set -e
PGVER="18"

sudo mkdir -p "/usr/lib/postgresql/${PGVER}/share/extension"

for file in /usr/pgsql-${PGVER}/share/extension/*; do
    target="/usr/lib/postgresql/${PGVER}/share/extension/$(basename "$file")"
    if [[ ! -e "$target" ]]; then
      sudo ln -s "$file" "$target" || (echo "Failed to link \"$file\" to \"$target\", exiting." && exit 1)
      echo "Created extension link for $(basename "$file")"
    else
      echo "Target $target already exists."
    fi
done

sudo mkdir -p "/usr/lib/postgresql/${PGVER}/lib"

for file in /usr/pgsql-${PGVER}/lib/*; do
    target="/usr/lib/postgresql/${PGVER}/lib/$(basename "$file")"
    if [[ ! -e "$target" ]]; then
      sudo ln -s "$file" "$target" || (echo "Failed to link \"$file\" to \"$target\", exiting." && exit 1)
      echo "Created lib link for $(basename "$file")"
    else
      echo "Target $target already exists."
    fi
done

```

  6. Connect to your database and run the `CREATE EXTENSION` command to enable PostGIS:
For instructions on connecting to your instance, see [Connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/connect).

```
CREATE EXTENSION IF NOT EXISTS POSTGIS;

```

  7. Confirm that PostGIS is installed and enabled:

```
SELECT postgis_full_version();

```

The output is similar to the following:

```
postgres=# SELECT postgis_full_version();
postgis_full_version
--------------------------------------------------------------------------------------------------------------------------------
POSTGIS="3.3.2 4975da8" [EXTENSION] PGSQL="150" GEOS="3.11.1-CAPI-1.18.1" PROJ="9.1.1" LIBXML="2.9.14" LIBJSON="0.16" LIBPROTOBUF="1.4.1" WAGYU="0.5.0 (Internal)"
(1 row)

```



Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
