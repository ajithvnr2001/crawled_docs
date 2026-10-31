---
url: https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates/
title: Create interactive sessions and runtime profiles \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:53:24.534205+00:00
---

# Create interactive sessions and runtime profiles  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create interactive sessions and runtime profiles Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create Managed Service for Apache Spark interactive sessions and runtime profiles, which are called session templates in the Google Cloud CLI and the Dataproc API. A runtime profile is a reusable set of serverless Spark runtime settings, such as compute tier and executor configuration, that you can use to create interactive notebooks and sessions.

**Note:** Managed Service for Apache Spark interactive sessions are associated with interactive notebooks. For an example of session use with Jupyter notebooks, see [Use the JupyterLab extension to develop serverless Spark workloads](https://docs.cloud.google.com/managed-spark/docs/guides/jupyterlab-sessions-serverless). For examples of session use in BigQuery Studio notebooks, see [Run PySpark code in BigQuery Studio notebooks](https://docs.cloud.google.com/bigquery/docs/use-spark).

## Create an interactive session

You can use the Google Cloud CLI or the Managed Service for Apache Spark API to create a Managed Service for Apache Spark interactive session.

### gcloud

You can use the [`gcloud beta dataproc sessions create spark SESSION_ID`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create) command to create a Managed Service for Apache Spark interactive session:
    
    
    gcloud beta dataproc sessions create spark SESSION_ID \
        --location=[REGION](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
        optional flags ...
    

Replace or add the following:

  * `SESSION_ID`: required. An ID for the session.

  * `REGION`: required. An [available Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) to locate your session.

  * [`--version`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--version): optional. A supported [Spark runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions). If you don't specify a version, the default Spark runtime version is used.

  * [`--container-image`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--container-image): optional. A [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) to use for your session.

  * [`--property`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--property): optional. One or more comma-separated [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless) for your session.

  * [`--service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--service-account): optional. The [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless) to use for your session. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

  * [`--subnet`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--subnet): optional. The name of a subnet in the session region. If not specified, Managed Service for Apache Spark uses the `default` subnet in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless#open-subnet).




### REST

You can use the Managed Service for Apache Spark [`sessions.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessions/create) API method to create a Managed Service for Apache Spark interactive session. Configure the following request fields:

  * [`name`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessions#Session.FIELDS.name): required. The session name.

  * [`version`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.version): optional. Any of the supported [Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions) for your session. If you don't specify a version, the default version is used.

  * [`containerImage`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.container_image): optional. A [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) to use for your session.

  * [`properties`](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.properties): optional. A mapping of session property names to values. For more information about supported properties, see [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless).

  * [`serviceAccount`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.service_account): optional. The [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless) to use to run your session. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

  * [`subnetworkUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.subnetwork_uri): optional. The name of a subnet in the session region. If not specified, Managed Service for Apache Spark uses the `default` subnet in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless#open-subnet).




## Create a runtime profile

A Managed Service for Apache Spark runtime profile (sometimes called a session template) defines reusable configuration settings for creating Managed Service for Apache Spark interactive sessions. You can use the Google Cloud console, the gcloud CLI, or the Managed Service for Apache Spark API to create a runtime profile. In the gcloud CLI and the Dataproc API, runtime profiles are called `session templates`.

**Note:** You can create an interactive session in a BigQuery Studio notebook from a Managed Service for Apache Spark runtime profile. For more information about using runtime profiles in BigQuery Studio, see [Run PySpark code in BigQuery Studio notebooks](https://docs.cloud.google.com/bigquery/docs/use-spark).

### Console

To create a Managed Service for Apache Spark runtime profile using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Runtime Profiles** page.

[Go to Runtime Profiles](https://console.cloud.google.com/dataproc/runtimeProfiles)

  2. Click **Create**.

  3. On the **Create a runtime profile** page, configure the following primary settings:

     * **Display name** : required. Enter a display name for the runtime profile, or accept the prefilled generated name. The display name must contain at least one letter or number, and is saved as a top-level display name for all session types, including Spark Connect. The **Runtime profile name** is the resource ID and is automatically derived from the display name by converting letters to lowercase and invalid characters to hyphens, shown as a hint beneath the field. To customize the resource ID separately from the display name, expand **Additional configuration** and edit **Runtime configuration**.

     * **Region** : required. Select an [available Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for sessions that use this runtime profile. The default region is `us-east4` (previously `us-central1`), and the list displays region descriptions.

     * **Description** : optional. Enter a description to help identify the runtime profile.

     * **Tier** : select the [Managed Service for Apache Spark tier](https://docs.cloud.google.com/managed-spark/docs/tiers) for workload execution:

       * **Premium** : default. Optimizes complex or latency-sensitive queries with acceleration engines and supports high-memory and GPU-accelerated executor shapes. When **Premium** is selected, the **Enable Lightning Engine to accelerate performance** checkbox is displayed and selected by default to accelerate Spark jobs with [Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine-serverless), which sets `spark.dataproc.engine=lightningEngine`.

       * **Standard** : provides a standard Spark execution environment for routine data processing. Interactive sessions always run on the premium tier; selecting **Standard** affects only batch execution. Choosing **Standard** turns Lightning Engine off, restricts machine shapes to standard CPU shapes (`standard-4`, `standard-8`, or `standard-16`), and requires `HDD (standard)` disks. If you switch from **Premium** to **Standard** , high-memory or GPU shapes are reset to `standard-4` and SSD disks are reset to a `200 GiB` HDD.

     * **Executor configuration** : select the compute sizing mode and machine shape for the Spark executors and driver that run your workload:

       * **General** : default. Provides CPU-only machine shapes suited for general extract, transform, and load (ETL) workloads. In the **Executor type** list, select a **High memory** shape, such as `highmem-4` (default) with 4 vCPUs and 32 GB memory, `highmem-8` with 8 vCPUs and 64 GB memory, or `highmem-16` with 16 vCPUs and 128 GB memory, or select a **Standard** shape, such as `standard-4` with 4 vCPUs and 16 GB memory, `standard-8` with 8 vCPUs and 32 GB memory, or `standard-16` with 16 vCPUs and 64 GB memory. **High memory** shapes are available only on the **Premium** tier.

       * **Accelerated** : provides [GPU-attached machine shapes](https://docs.cloud.google.com/managed-spark/docs/guides/gpus-serverless) suited for data science and AI or ML training and inference workloads. Selecting an **Accelerated** shape automatically switches the tier to **Premium** and the disk tier to **SSD (premium)** with a default size of `375 GiB`. In the **Executor type** list, select an **L4** shape with 4, 8, 12, 16, 24, 48, or 96 vCPUs, or select an **A100** shape, such as `A100 40GB (12 vCPU)` or `A100 80GB (12 vCPU)`.

  4. Optional: To customize advanced runtime, compute, autoscaling, metastore, network, security, lifecycle, or property settings, click **Additional configuration** to expand the panel. Next to any category that you want to customize, click **Edit** , configure the settings in the pane, and then click **Save** :

     * **Runtime configuration** : configure the runtime identifier, Spark version, container image, staging bucket, and Python package repository:

       * **Runtime profile name** : required. Accept the generated resource ID derived from the display name or enter a custom ID. The ID must be 4 to 63 characters, contain only lowercase letters, numbers, and hyphens, start and end with a lowercase letter or number, and can't be changed after the runtime profile is created.

       * **Spark runtime version** : required. Select a supported [Managed Service for Apache Spark runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions).

       * **Custom Spark image** : optional. Enter the Artifact Registry or Container Registry URI of a [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) that includes custom Java or Python dependencies.

       * **Staging bucket** : optional. Click **Browse** to select or create a [Cloud Storage staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/staging-bucket-serverless) to store workload dependencies, job driver output, and configuration files. If left empty, Managed Service for Apache Spark automatically manages the staging bucket (indicated by `Auto` in the summary).

       * **Python package repository** : optional. Enter the URI of a custom repository, such as `https://pypi.org/simple`, to install Python packages. If left empty, packages are installed from the Google-managed PyPI pull-through cache (the default summary).

     * **Executor and driver configuration** : customize the compute tier, disk tier, disk size, and separate driver configuration:

       * **Tier** : select **Premium** , which includes the optional **Enable Lightning Engine to accelerate performance** checkbox, or **Standard**.

       * **Executor type** : select a **General** `High memory` or `Standard` machine shape, or an **Accelerated** `L4` or `A100` machine shape.

       * **Disk tier** : select `HDD (standard)` or `SSD (premium)`. `HDD (standard)` is the default for CPU shapes and is required on the **Standard** tier. `SSD (premium)` is available on the **Premium** tier for shuffle-heavy or spill-heavy workloads and is required for **Accelerated** GPU shapes.

       * **Disk size** : select a disk size in GiB. `HDD (standard)` supports `200 GiB` to `1500 GiB` in 100 GiB increments, with a default of `200 GiB`. `SSD (premium)` supports `375 GiB`, `750 GiB`, or `1500 GiB`, with a default of `375 GiB`.

       * **Use different configuration for driver** : optional. By default, the driver uses the same machine shape and disk configuration as the executor. Select this checkbox to customize the driver machine type, driver disk tier, and driver disk size independently.

**Note:** These compute settings are written as Spark properties: `spark.dataproc.executor.compute.tier`, `spark.dataproc.driver.compute.tier`, `spark.executor.cores`, `spark.executor.memory`, `spark.driver.cores`, `spark.driver.memory`, `spark.dataproc.executor.resource.accelerator.type`, `spark.dataproc.executor.disk.tier`, `spark.dataproc.executor.disk.size`, `spark.dataproc.driver.disk.tier`, and `spark.dataproc.driver.disk.size`.
     * **Autoscaling** : configure [dynamic resource allocation](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling-serverless) to scale executors based on workload demand:

       * **Enabled** : selected by default, which sets `spark.dynamicAllocation.enabled`. Clear this checkbox to disable autoscaling.

       * **Initial executors** : enter the initial number of executors, which sets `spark.dynamicAllocation.initialExecutors`. The default is `5`. Valid values range from `2` to `2000` for runtime versions `2.3` and earlier, or from `0` to `2000` for runtime version `3.0` and later.

       * **Minimum executors** : enter the minimum number of executors, which sets `spark.dynamicAllocation.minExecutors`. The default is `2` for runtime versions `2.3` and earlier, or `0` for runtime version `3.0` and later, with an upper limit of `2000`.

       * **Maximum executors** : enter the maximum number of executors, which sets `spark.dynamicAllocation.maxExecutors`. The default is `1000`, with a maximum allowed limit of `2000`.

     * **Metastore configuration** : select the metastore that manages your dataset metadata:

       * **Lakehouse runtime catalog** : default. Uses a serverless [Lakehouse runtime catalog](https://docs.cloud.google.com/managed-spark/docs/guides/spark-workloads-with-bigquery-metastore) catalog in the current project, with the **Iceberg REST Endpoint** enabled by default. You can specify the **Project ID** and either choose an existing **Catalog ID** or define a new catalog. You can also select the **Hive Endpoint** checkbox to specify a Hive endpoint **Project ID** , **Catalog ID** , and **Catalog Name**.

       * **Dataproc Metastore** : attaches a managed [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc) Hive Metastore (HMS) instance. Select the project in **Selected project** and choose a service instance in the **Metastore service** list.

       * **None** : disables metastore integration for sessions that use this runtime profile.

     * **Network and security** : configure VPC networking, execution credentials, and encryption keys:

       * **Connect your cluster** : under [network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless), the Google Cloud console automatically selects an eligible network or subnetwork in the chosen region. If the chosen region does not have an available default network, **Additional configuration** automatically opens and displays a warning that the default network isn't available. In this situation, the **Create** button remains disabled until you click **Configure network** and select an available subnetwork. You can select **Networks in this project** to choose a **Primary network** and **Subnetwork** in the current project, or select **Networks shared from host project** to choose a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) subnetwork. The selected subnetwork must have [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) enabled. For network connectivity requirements, see [Open subnet connectivity](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless#open-subnet). You can also enter optional **Network tags** to apply [firewall rules and routes](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) to workload VMs.

       * **Execute notebooks with** : select **User Account** , which is the default, to execute notebooks using end-user credentials, or select **Service Account** to run sessions with a custom [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless). When **Service Account** is selected, specifying a service account in the **Service account** field is required.

       * **Encryption** : select **Google-owned and Google-managed encryption key** , which is the default, or select **Cloud KMS key** to encrypt workload data using a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/managed-spark/docs/guides/cmek-serverless).

     * **Session lifecycle** : configure automatic session termination limits:

       * **Max idle time** : optional. Enter a **Max idle time quantity** and select a **Max idle time unit** in `seconds`, `minutes`, `hours`, or `days`, from 10 minutes to 330 hours, to specify how long a notebook session can remain idle before it is automatically terminated.

       * **Max session time** : optional. Enter a **Max session time quantity** and select a **Max session time unit** in `seconds`, `minutes`, `hours`, or `days`, from 10 minutes to 330 hours, to specify the maximum lifetime of a session.

     * **Other customizations** : add custom Spark properties and resource labels:

       * **Spark properties** : optional. Click **Add property** and enter **Key** and **Value** pairs for custom Spark properties. Properties controlled by dedicated fields in the form (such as compute tier, executor and driver sizing, Lightning Engine, `spark.dynamicAllocation.*`, and Lakehouse catalog properties) are managed by those fields and are hidden from the free-form list. In the Google Cloud console, don't include the `spark:` prefix.

       * **Labels** : optional. Click **Add label** and enter **Key** and **Value** pairs to attach [labels](https://docs.cloud.google.com/managed-spark/docs/guides/creating-managing-labels) to the runtime profile.

  5. Review the configuration details in the **Summary** card and the estimated Data Compute Unit (DCU) usage in the **Pricing estimate** card on the right side of the page. For more information about DCU charges, see [Managed Service for Apache Spark pricing](https://cloud.google.com/managed-spark/pricing).

  6. Click **Create**.




### gcloud

In the gcloud CLI, runtime profiles are managed as session templates. You can't directly create a Managed Service for Apache Spark runtime profile using a `create` command in the gcloud CLI, but you can use the [`gcloud beta dataproc session-templates import`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/import) command to create or update a runtime profile from a YAML configuration file. You can also export an existing runtime profile using the [`gcloud beta dataproc session-templates export`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/export) command.

### REST

In the Managed Service for Apache Spark API, runtime profiles are represented by [`SessionTemplate`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessionTemplates#SessionTemplate) resources. You can use the Managed Service for Apache Spark [`sessionTemplates.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessionTemplates/create) API method to create a Managed Service for Apache Spark runtime profile. Configure the following request fields:

  * [`name`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessionTemplates#SessionTemplate.FIELDS.name): required. The resource name of the runtime profile.

  * [`version`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.version): optional. Any of the supported [Spark runtime versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#supported-dataproc-serverless-for-spark-runtime-versions) for your sessions. If you don't specify a version, the default version is used.

  * [`sessionConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.sessionTemplates#SessionTemplate.FIELDS.spark_connect_session): specify either `jupyterSession` or `sparkConnectSession`. If you specify `jupyterSession`, also specify the [`JupyterConfig.displayName`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/JupyterConfig#FIELDS.display_name) and [`JupyterConfig.kernel`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/JupyterConfig#kernel) fields. For more information about Jupyter notebook sessions, see [Launch a Jupyter notebook on Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/jupyterlab-sessions-serverless#launch_a_jupyter_notebook_on_dataproc-serverless).

  * [`containerImage`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.container_image): optional. A [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) to use for your sessions.

  * [`properties`](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.properties): optional. A mapping of Spark property names to values, including tier, engine, machine shape, disk, and autoscaling properties. For more information about supported properties, see [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless).

  * [`serviceAccount`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.service_account): optional. A [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless) to use to run your sessions. If not specified, the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

  * [`subnetworkUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.subnetwork_uri): optional. The name of a subnet in the session region. If not specified, Managed Service for Apache Spark uses the `default` subnet in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless#open-subnet).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
