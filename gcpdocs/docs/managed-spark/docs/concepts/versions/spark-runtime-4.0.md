---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-4.0
title: Managed Service for Apache Spark runtime 4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:55:43.355223+00:00
---

# Managed Service for Apache Spark runtime 4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-4.0

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark runtime 4.0 Stay organized with collections  Save and categorize content based on your preferences. 

See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for the latest Managed Service for Apache Spark runtime update notices.

## Spark runtime version 4.0 components

Component | [4.0.0  
](https://docs.cloud.google.com/managed-spark/docs/release-notes)  
---|---  
[**Apache Spark**](https://spark.apache.org/) | [4.2.0](https://spark.apache.org/releases/spark-release-4-2-0.html)  
[**Cloud Storage Connector**](https://github.com/GoogleCloudDataproc/hadoop-connectors/tree/master/gcs) | [4.0.7](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v4.0.7)  
[**BigQuery Connector**](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.46.0](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases/tag/0.46.0)  
[**Java**](https://www.oracle.com/java/) | [25](https://jdk.java.net/25/)  
[**Python**](https://www.python.org/) | [3.13](https://docs.python.org/3/whatsnew/3.13.html)  
[**Scala**](https://www.scala-lang.org/) | [2.13.17](https://www.scala-lang.org/news/2.13.17)  
  
**Notes:**

  * The `4.0` runtime uses `UTF-8` as the default character encoding.

  * The `4.0` runtime uses [Pixi](https://pixi.prefix.dev) instead of Conda to manage its Python environment. For the packages that the environment includes, see Python libraries.




## Runtime 4.0 features and improvements

Compared with the `3.0` runtime, the `4.0` runtime includes the following changes to defaults and features:

  * **Premium tier by default:** Batch workloads run in the [premium tier](https://docs.cloud.google.com/managed-spark/docs/tiers) unless you set the [`dataproc.tier`](https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless#tier_property) property to `standard`. Interactive sessions always run in the premium tier. Premium tier workloads are charged at the premium Data Compute Unit (DCU) rate.

The `4.0` runtime also makes workloads easier to configure:

    * **Better defaults:** In the premium tier, the driver and executors use premium compute and disk resources by default, so you don't need to set properties to use them. For the default disk sizes, see Default disk size. In the premium tier, disk sizes don't need to be multiples of `375` GiB.
    * **Fewer properties:** The `dataproc.tier` property determines the compute and disk resources of the driver and executors, so you don't need to configure them separately. The `spark.dataproc.driver.compute.tier`, `spark.dataproc.executor.compute.tier`, `spark.dataproc.driver.disk.tier`, and `spark.dataproc.executor.disk.tier` properties are removed.
  * **Lightning Engine by default:** Premium tier batch workloads use [Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine-serverless) by default. To opt out, set `spark.dataproc.engine=default`. Interactive sessions don't use Lightning Engine by default. To enable it for an interactive session, set `spark.dataproc.engine=lightningEngine`. To also use [Native Query Execution](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine-serverless#native_query_execution), set `spark.dataproc.lightningEngine.runtime=native`.

  * **`highmem` memory shape by default:** The `4.0` runtime introduces memory shapes, which determine how much memory the driver and executors get. Drivers and executors use the `highmem` memory shape by default, which provides `7.75` GiB of memory per vCPU and gives them more memory than the default memory settings of the `3.0` runtime. Memory shapes also make memory easier to configure:

    * **New memory shape properties:** To select the memory shape of the driver or executors, set the `spark.dataproc.driver.memory.shape` or `spark.dataproc.executor.memory.shape` property to `highmem` or `standard`. The `standard` memory shape provides `3.75` GiB of memory per vCPU.
    * **Automatic memory sizing:** Managed Service for Apache Spark sizes the Spark memory and memory overhead of the driver and executors from their memory shape, so you don't need to set `spark.driver.memory`, `spark.executor.memory`, `spark.driver.memoryOverhead`, or `spark.executor.memoryOverhead`.
  * **Faster startup:** In the premium tier, workloads that use the default driver configuration are eligible to run the driver on a fast-startup VM, which reduces workload startup time.

  * **Lakehouse runtime catalog as the default catalog:** Batch workloads and interactive sessions use the [Lakehouse runtime catalog](https://docs.cloud.google.com/managed-spark/docs/guides/create-lakehouse#default-catalog) as the default Spark catalog, so you can create and query Apache Iceberg tables without configuring a catalog. The pre-configured `bigquery` Spark catalog is still available. To use a different catalog, see [Opt out of the starter catalog](https://docs.cloud.google.com/managed-spark/docs/guides/create-lakehouse#opt-out).

  * **DCU quota:** Workloads consume the Managed Service for Apache Spark **Data Compute Units** quota (`DataComputeUnitsPerProjectPerRegion`) instead of the Compute Engine CPU and disk quotas of your project. Workloads that use GPUs continue to consume Compute Engine quotas. For more information, see [Managed Service for Apache Spark serverless quotas](https://docs.cloud.google.com/managed-spark/quotas-serverless).




The `4.0` runtime also includes the features of the [`3.0` runtime](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-3.0), such as regional and multi-zonal workloads, end-user credentials by default, and fast resource cleanup.

## Memory shapes

In the `4.0` runtime, the memory shape of the driver and executors determines how much memory they were allocated. A memory shape provides a fixed amount of memory for each vCPU. Managed Service for Apache Spark splits that memory between the Spark heap (`spark.driver.memory` or `spark.executor.memory`) and the memory overhead (`spark.driver.memoryOverhead` or `spark.executor.memoryOverhead`).

Drivers and executors use the `highmem` memory shape by default, which provides `7.75` GiB of memory per vCPU. You don't need to set memory properties to use it.

The `4.0` runtime introduces the following properties to select the memory shape of the driver and executors:

Property | Description | Default  
---|---|---  
`spark.dataproc.driver.memory.shape` | The memory shape of the driver, either `highmem` or `standard`. | `highmem`  
`spark.dataproc.executor.memory.shape` | The memory shape of the executors, either `highmem` or `standard`. | `highmem`  
  
The following table lists the memory that each memory shape provides, and the default Spark memory settings of a driver or executor that has 4 vCPUs, which is the default value of `spark.driver.cores` and `spark.executor.cores`:

Memory shape | Memory per vCPU | PySpark batch workloads: memory and memory overhead | Other batch workloads and interactive sessions: memory and memory overhead  
---|---|---|---  
`highmem` | 7.75 GiB | `21154m` and `8462m` | `26924m` and `2692m`  
`standard` | 3.75 GiB | `9681m` and `3872m` | `12321m` and `1232m`  
  
**Notes:**

  * The memory of a memory shape scales with the number of vCPUs. For example, a `highmem` executor that has 8 vCPUs gets 62 GiB of memory.

  * Part of the memory of a memory shape is reserved for the system and isn't available to Spark. Workloads that use [custom container images](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) reserve additional memory, so their default Spark memory settings are slightly lower.

  * PySpark batch workloads use a memory overhead factor of `0.4`. Other batch workloads and interactive sessions use a memory overhead factor of `0.1`. To change how the memory of a memory shape is split between the heap and the memory overhead, set `spark.driver.memoryOverheadFactor` or `spark.executor.memoryOverheadFactor`.

  * The memory shape determines the memory that's provisioned for the driver and executors, which affects DCU usage. For more information, see [Managed Service for Apache Spark pricing](https://cloud.google.com/products/managed-service-for-apache-spark/pricing).




### How memory shapes are applied

Managed Service for Apache Spark applies memory shapes to the driver and executors as follows:

  * A driver or executor uses the `highmem` memory shape unless you set one of the following for it:

    * A memory shape: `spark.dataproc.driver.memory.shape` or `spark.dataproc.executor.memory.shape`.
    * Memory: `spark.driver.memory` or `spark.executor.memory`.
    * Memory overhead: `spark.driver.memoryOverhead` or `spark.executor.memoryOverhead`.
    * A [GPU accelerator](https://docs.cloud.google.com/managed-spark/docs/guides/gpus-serverless). Drivers and executors that use GPUs get a fixed amount of memory.
  * If you set the memory or memory overhead of a driver or executor and don't set its memory shape, the driver or executor doesn't use a memory shape. Instead, Managed Service for Apache Spark sizes the driver or executor from the memory that you specify, as in earlier runtimes.

  * Setting the memory overhead factor of a driver or executor doesn't change its memory shape.

  * Managed Service for Apache Spark rejects a batch workload or interactive session in the following cases:

    * It sets the memory shape of a driver or executor, and also sets the memory or memory overhead of the same driver or executor. To change how the memory of a memory shape is split, set the memory overhead factor instead.
    * It sets a memory shape to a value other than `highmem` or `standard`.



### Fast-startup driver

In the premium tier, Managed Service for Apache Spark can run the driver on a fast-startup VM to reduce workload startup time. The driver is eligible to run on a fast-startup VM if all of the following conditions are met:

  * The workload runs in the premium tier, which is the default in the `4.0` runtime.
  * The driver uses a memory shape.
  * The driver has 4 vCPUs (`spark.driver.cores=4`), which is the default.
  * The driver disk size (`spark.dataproc.driver.disk.size`) is `450g` or less. The default is `400g`.
  * The workload doesn't set `spark.driver.memory`, `spark.driver.memoryOverhead`, `spark.driver.memoryOverheadFactor`, or a GPU accelerator for the driver.



A driver that runs on a fast-startup VM gets the same memory as other drivers that use the same memory shape.

## Default disk size

In the `4.0` runtime, the [tier](https://docs.cloud.google.com/managed-spark/docs/tiers) of a workload determines the default disk size of its driver and executors:

Tier | Default disk size of each driver and executor  
---|---  
Premium (default) | 100 GiB per vCPU, and at least `375` GiB. For example, 400 GiB for 4 vCPUs.  
Standard | `75` GiB per vCPU, and up to 1,000 GiB. For example, `300` GiB for 4 vCPUs.  
  
To change the disk size, set the `spark.dataproc.driver.disk.size` or `spark.dataproc.executor.disk.size` [resource allocation property](https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless#resource_allocation_properties). In the premium tier, disk sizes don't need to be multiples of 375 GiB.

## Unsupported functionality and behavior changes

The following functionality isn't supported or behaves differently in the `4.0` runtime:

  * **Compute and disk tier properties:** The `spark.dataproc.driver.compute.tier`, `spark.dataproc.executor.compute.tier`, `spark.dataproc.driver.disk.tier`, and `spark.dataproc.executor.disk.tier` properties aren't supported. Instead, use the [`dataproc.tier`](https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless#tier_property) property.

  * **Off-heap memory properties:** The `spark.memory.offHeap.enabled` and `spark.memory.offHeap.size` properties aren't supported.

  * **Subnetworks:** You must specify a subnetwork when you submit a batch workload or create an interactive session. Dual-stack (IPv4 and IPv6) and IPv6-only subnetworks aren't supported. For more information, see [Network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless).

  * **Custom Spark BigQuery connector:** If you add a Spark BigQuery connector JAR file to a batch workload, also set the [`dataproc.artifacts.remove=spark-bigquery-connector`](https://docs.cloud.google.com/managed-spark/docs/concepts/spark-properties-serverless#other_properties) property to remove the pre-installed connector. Otherwise, the batch workload fails.

  * **Staging buckets:** The `4.0` runtime doesn't use Cloud Storage [staging](https://docs.cloud.google.com/managed-spark/docs/concepts/staging-bucket-serverless) buckets.

  * **Persistent History Server (PHS):** The PHS isn't supported. Instead, use the [Spark UI](https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-batches#spark_ui).

  * **SparkR:** SparkR batches aren't supported. Instead, use [`sparklyr`](https://spark.posit.co).

  * **Jupyter sessions:** Jupyter sessions aren't supported. Instead, use [Spark Connect sessions](https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client), the industry standard for interactive Spark development.




## Python libraries

The following table lists the Python packages that the `4.0` runtime includes. If the table doesn't list a version for a package, the runtime includes the latest version of the package that's compatible with the other packages when the runtime is built. These versions can change in subminor runtime releases.

**Note:** You can't use distributed Spark XGBoost on a Managed Service for Apache Spark batch workload that has [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling) enabled (the default behavior) because new nodes that start elastic scaling can't receive new tasks and remain idle.

To use XGBoost with a batch workload, you can set the [`spark.dynamicAllocation.enabled = false`](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling#spark_dynamic_allocation_properties) property on a batch workload to disable dynamic allocation.

serverless-spark-4.0-debian-13 python librariesPackage Name | Version  
---|---  
accelerate |   
bigframes |   
ca-certificates |   
certifi |   
cookiecutter |   
cuda | 12.9  
cudnn |   
cython |   
dask |   
datasets |   
db-dtypes |   
deepspeed |   
delta-spark | 4.4.0  
evaluate |   
fastavro |   
fastparquet |   
gcsfs |   
google-auth-oauthlib |   
google-cloud-aiplatform |   
google-cloud-alloydb-connector[pg8000] |   
google-cloud-bigquery |   
google-cloud-bigtable |   
google-cloud-container |   
google-cloud-datacatalog |   
google-cloud-dataproc |   
google-cloud-datastore |   
google-cloud-dlp |   
google-cloud-language |   
google-cloud-logging |   
google-cloud-monitoring |   
google-cloud-pubsub |   
google-cloud-redis |   
google-cloud-secret-manager |   
google-cloud-spanner |   
google-cloud-spark-connect[interactive] |   
google-cloud-speech |   
google-cloud-storage |   
google-cloud-storage-control |   
google-cloud-texttospeech |   
google-cloud-translate |   
google-cloud-vision |   
holoviews |   
ipyparallel |   
keyrings.google-artifactregistry-auth |   
langchain |   
lightgbm |   
mkl |   
mlflow |   
nccl |   
nltk |   
numba |   
numba-cuda |   
numpy |   
onnx |   
opencv-python |   
optuna |   
pandas |   
papermill |   
polars |   
psycopg2-binary |   
pyarrow |   
pydot |   
pyiceberg |   
pymongo |   
pynvml |   
python | 3.13  
python-dateutil |   
pytorch-gpu |   
requests |   
rtree |   
scikit-image |   
scikit-learn |   
scipy |   
seaborn |   
sentence-transformers |   
sentencepiece |   
shap |   
spacy |   
sqlalchemy |   
statsforecast |   
sympy |   
tables |   
torcheval |   
torchvision |   
transformers |   
virtualenv |   
wordcloud |   
xgboost | 3.4  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
