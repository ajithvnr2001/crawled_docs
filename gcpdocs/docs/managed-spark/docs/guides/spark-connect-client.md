---
url: https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client/
title: Use the serverless Spark Connect client \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:59:07.790598+00:00
---

# Use the serverless Spark Connect client  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use the serverless Spark Connect client Stay organized with collections  Save and categorize content based on your preferences. 

The Managed Service for Apache Spark Connect client (`google-cloud-spark-connect`) is a Python client library built on top of the open-source [Apache Spark Connect](https://spark.apache.org/spark-connect/) client. It lets your local applications, scripts, and notebooks run PySpark workloads on a remote Managed Service for Apache Spark session over the Spark Connect protocol.

Compared to using the standard Apache Spark Connect client directly, `google-cloud-spark-connect` provides the following benefits:

  * **Automated session lifecycle and authentication** : `ManagedSparkSession.builder.getOrCreate()` automatically provisions, configures, or reuses a remote Managed Service for Apache Spark interactive session and attaches refreshing Google Cloud credentials. Code written with `ManagedSparkSession` also runs unchanged when submitted as a Managed Service for Apache Spark batch workload, provided that the `google-cloud-spark-connect` package is installed in the batch workload's Python environment.
  * **Live progress bars and monitoring links** : Displays real-time progress bars in notebooks and interactive terminals during session creation and Spark job execution (tracking task completion across stages), along with direct links to the session details page in the Google Cloud console, the **Spark UI** , and individual **Spark Query** execution pages.
  * **Interactive notebook extras** : When installed with the `interactive` extra, importing `google.cloud.managed_spark_connect` in an IPython or Jupyter notebook automatically loads: 
    * [`explore_dataframe()`](https://docs.cloud.google.com/managed-spark/docs/guides/visualize-dataframes-notebooks) (powered by `google-colabsqlviz`) to interactively explore, filter, sort, aggregate, and chart PySpark DataFrames without writing plotting code.
    * `%%sparksql` and `%sparksql` magic commands to run Spark SQL queries in notebook cells with interactive result visualization and Python variable or DataFrame binding.
    * `%dpip` magic command to install PyPI packages directly onto the remote session's driver and executors without building a custom container image.



Like the open-source Spark Connect client, `google-cloud-spark-connect` doesn't require a local Spark installation. With the `[client]` extra, it installs only the lightweight `pyspark-client` package instead of the full `pyspark` distribution, so you don't need to download Spark or install Java on your machine to run PySpark on Managed Service for Apache Spark.

This document shows you how to install, configure, and use the client.

## Before you begin

  1. Ensure you have the [Identity and Access Management roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#dataproc-roles) that contain the permissions needed to manage interactive sessions and runtime profiles (session templates).

  2. If you run the client outside of Google Cloud, provide [authentication credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc). Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file.




## Install or uninstall the client

You can install or uninstall the `google-cloud-spark-connect` package using `pip`.

### Install

For local notebooks and development environments (such as VS Code with [Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview) or JupyterLab), install the client from the command line in a virtual environment:
    
    
    pip install 'google-cloud-spark-connect[interactive,client]'
    

This installs `google-cloud-spark-connect`, with two optional extras:

  * `interactive`: Installs interactive notebook extensions (`explore_dataframe()`, `%%sparksql`, and `%dpip`). May be omitted for standalone Python scripts outside of a notebook.
  * `client`: Installs the lightweight `pyspark-client` package, which doesn't require a local JVM.



In managed notebook environments such as Colab Enterprise (where full `pyspark` is pre-installed), run `%pip install` with the `spark` extra instead of `client` in a dedicated setup cell at the top of your notebook:
    
    
    %pip install 'google-cloud-spark-connect[interactive,spark]'
    

### Uninstall

To uninstall the client, run the following command:
    
    
    pip uninstall google-cloud-spark-connect pyspark-client
    

## Configure the client

Specify the project and region for your session. You can set these values using environment variables or by using the builder API in your code.

### Environment variables

Set the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_REGION` environment variables. 

Expand example Collapse example
    
    
    # Google Cloud Configuration for Managed Spark Connect Integration Tests
    # Copy this file to .env and fill in your actual values
    
    # ============================================================================
    # REQUIRED CONFIGURATION
    # ============================================================================
    
    # Your Google Cloud Project ID
    GOOGLE_CLOUD_PROJECT="your-project-id"
    
    # Google Cloud Region where Managed Spark sessions will be created
    # Integration tests also accept a comma-separated ordered list of fallback regions
    # (e.g. "us-east1,us-central1,us-west1") when using a short subnet name.
    GOOGLE_CLOUD_REGION="us-central1"
    
    # Path to service account key file (if using SERVICE_ACCOUNT auth)
    GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
    
    # ============================================================================
    # AUTHENTICATION CONFIGURATION
    # ============================================================================
    
    # Authentication type (SERVICE_ACCOUNT or END_USER_CREDENTIALS). If not set, API default is used.
    # MANAGED_SPARK_CONNECT_AUTH_TYPE="SERVICE_ACCOUNT"
    # MANAGED_SPARK_CONNECT_AUTH_TYPE="END_USER_CREDENTIALS"
    
    # Service account email for workload authentication (optional)
    # MANAGED_SPARK_CONNECT_SERVICE_ACCOUNT="your-service-account@your-project.iam.gserviceaccount.com"
    
    # ============================================================================
    # SESSION CONFIGURATION
    # ============================================================================
    
    # Session timeout in seconds (how long session stays active)
    # MANAGED_SPARK_CONNECT_TTL_SECONDS="3600"
    
    # Session idle timeout in seconds (how long session stays active when idle)
    # MANAGED_SPARK_CONNECT_IDLE_TTL_SECONDS="900"
    
    # Automatically terminate session when Python process exits (true/false)
    # MANAGED_SPARK_CONNECT_SESSION_TERMINATE_AT_EXIT="false"
    
    # Custom file path for storing active session information
    # MANAGED_SPARK_CONNECT_ACTIVE_SESSION_FILE_PATH="/tmp/managed_spark_connect_session"
    
    # ============================================================================
    # DATA SOURCE CONFIGURATION
    # ============================================================================
    
    # Default data source for Spark SQL (currently only supports "bigquery")
    # Only available for Managed Spark runtime version 2.3
    # MANAGED_SPARK_CONNECT_DEFAULT_DATASOURCE="bigquery"
    
    # ============================================================================
    # ADVANCED CONFIGURATION
    # ============================================================================
    
    # Custom Dataproc API endpoint (uncomment if needed)
    # GOOGLE_CLOUD_DATAPROC_API_ENDPOINT="your-region-dataproc.googleapis.com"
    
    # Subnet name or URI for Managed Spark Connect (optional; defaults to "default" in tests)
    # Accepts a short subnet name (e.g. "default") or full resource URI:
    # MANAGED_SPARK_CONNECT_SUBNET="default"
    # MANAGED_SPARK_CONNECT_SUBNET="projects/your-project-id/regions/us-central1/subnetworks/your-subnet-name"
    
    
    

### Builder API

Use the `.projectId()`, `.location()`, and `.sessionId()` methods.
    
    
    spark = (
        ManagedSparkSession.builder
        .projectId("my-project")
        .location("us-central1")
        .sessionId("my-spark-session")
        .getOrCreate()
    )
    

## Start a Spark session

To start a Spark session, import `ManagedSparkSession` in your PySpark application or notebook, then call the `ManagedSparkSession.builder.getOrCreate()` API. We recommend setting a custom session ID with `.sessionId()` so that re-running your notebook or running multiple notebooks within the session's time to live (TTL) reuses the active session and eliminates session startup time.

  1. Import the `ManagedSparkSession` class. In an IPython or Jupyter notebook, importing `google.cloud.managed_spark_connect` also automatically loads the interactive notebook extras (`explore_dataframe()`, `%%sparksql`, and `%dpip`) if the `interactive` extra is installed.

  2. Call `.sessionId()` and `.getOrCreate()` to start or reuse the session.
         
         from google.cloud.managed_spark_connect import ManagedSparkSession
         spark = ManagedSparkSession.builder.sessionId("my-spark-session").getOrCreate()
         




While a new session starts, the client displays a live progress bar and a link to the session details page in the Google Cloud console (in VS Code, the link opens the session in Data Agent Kit instead). If an active session with the specified ID already exists, the client connects to it instead of creating a new one. In that case, the client ignores the session configuration in your code. To apply configuration changes, terminate the existing session (`spark.stop(terminate=True)`) or use a different session ID. If a session with the specified ID has already terminated, the client automatically deletes the old session and creates a new one with the same ID. Once the session is active:

  * Evaluating `spark` in a notebook cell displays direct links to the session details page and the **Spark UI**.
  * Running Spark actions (such as `df.show()`, `df.collect()`, or `df.toPandas()`) displays a real-time task progress bar and a **Spark Query** link to the operation's execution page in the **Spark UI**.

**Note:** To disable automatic loading of interactive notebook extras when importing `google.cloud.managed_spark_connect`, set the environment variable `MANAGED_SPARK_CONNECT_ENABLE_EXTRAS=false` or run `%config ManagedSparkConnect.enable_extras = False` before importing the module.

## Configure Spark properties

To configure Spark properties, chain one or more `.config()` methods to the builder.
    
    
    from google.cloud.managed_spark_connect import ManagedSparkSession
    
    spark = (
        ManagedSparkSession.builder
        .sessionId('my-spark-session')
        .config('spark.executor.memory', '48g')
        .config('spark.executor.cores', '8')
        .getOrCreate()
    )
    

**Note:** Managed Service for Apache Spark `3.0`\+ runtimes support Spark [single-node execution](https://spark.apache.org/docs/latest/submitting-applications.html#master-urls). To enable it, set `spark.master=local` in your session config.

## Use advanced configuration

You can configure common session settings—such as the session ID, runtime version, subnetwork, service account, session template, TTL (`.ttl()` / `.ttlSeconds()` and `.idleTtl()` / `.idleTtlSeconds()`), or labels—directly using builder methods:
    
    
    import datetime
    from google.cloud.managed_spark_connect import ManagedSparkSession
    
    spark = (
        ManagedSparkSession.builder
        .projectId('my-project')
        .location('us-central1')
        .sessionId('my-spark-session')
        .runtimeVersion('3.0')
        .subnetwork('SUBNET')
        .idleTtl(datetime.timedelta(minutes=30))
        .getOrCreate()
    )
    

For full customization of the underlying session resource, pass a `google.cloud.dataproc_v1.Session` object to `.sessionConfig()`:
    
    
    from google.cloud.managed_spark_connect import ManagedSparkSession
    from google.cloud.dataproc_v1 import [Session](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Session.html)
    
    session_config = Session()
    session_config.environment_config.execution_config.subnetwork_uri = 'SUBNET'
    session_config.runtime_config.version = '3.0'
    
    spark = (
        ManagedSparkSession.builder
        .projectId('my-project')
        .location('us-central1')
        .sessionId('my-spark-session')
        .sessionConfig(session_config)
        .getOrCreate()
    )
    

## Reuse a named session

Setting a custom session ID with `.sessionId()` lets you reuse a single Spark session across multiple notebooks or across kernel restarts within the session's TTL, eliminating session startup latency and reducing costs.

  1. In your first notebook, create a session with a custom ID.
         
         from google.cloud.managed_spark_connect import ManagedSparkSession
         
         session_id = 'my-ml-pipeline-session'
         spark = ManagedSparkSession.builder.sessionId(session_id).getOrCreate()
         df = spark.createDataFrame([(1, 'data')], ['id', 'value'])
         df.show()
         

  2. In another notebook (or after restarting the kernel), reuse the session by specifying the same session ID.
         
         from google.cloud.managed_spark_connect import ManagedSparkSession
         
         session_id = 'my-ml-pipeline-session'
         spark = ManagedSparkSession.builder.sessionId(session_id).getOrCreate()
         df = spark.createDataFrame([(2, 'more-data')], ['id', 'value'])
         df.show()
         




Session IDs must be 4-63 characters long, start with a lowercase letter, and contain only lowercase letters, numbers, and hyphens. The ID cannot end with a hyphen. Named sessions persist until they are explicitly terminated or reach their configured TTL. If a session with the specified ID is already in a `TERMINATED`, `TERMINATING`, or `FAILED` state, the client emits a warning, deletes the old session, and creates a new session with the same ID (deleting the old session removes its previous metadata and Spark UI history from Managed Service for Apache Spark, though logs remain available in Cloud Logging).

If an active session with the specified ID already exists, the client connects to it and ignores the session configuration in your code. To apply configuration changes, terminate the existing session or use a different session ID.

To terminate a named session, call `spark.stop(terminate=True)`. Calling `spark.stop()` without arguments disconnects the client but leaves a named session running. Sessions created without `.sessionId()` are terminated by `spark.stop()`.

## Use Spark SQL magic commands

The `interactive` extra includes the `%%sparksql` cell magic and `%sparksql` line magic to execute Spark SQL queries in Jupyter notebooks and render interactive tables and charts using `google-colabsqlviz` (the same visualization widget used by [`explore_dataframe()`](https://docs.cloud.google.com/managed-spark/docs/guides/visualize-dataframes-notebooks)).

When you install `google-cloud-spark-connect` with the `interactive` extra and import `google.cloud.managed_spark_connect` in a notebook, the magic extension loads automatically.

  1. Optional: Load the magic extension explicitly if you haven't imported `google.cloud.managed_spark_connect`.
         
         %load_ext google.cloud.managed_spark_magics
         

  2. Optional: configure default settings.
         
         %config SparkSql.limit=20
         

  3. Execute SQL queries using the `%%sparksql` cell magic (which renders an interactive table and stores the full DataFrame in `_df` by default) or the `%sparksql` line magic (which suppresses table display and returns the DataFrame directly):
         
         %%sparksql
         SELECT * FROM your_table
         
         
         df = %sparksql SELECT * FROM your_table
         

  4. Optional: Pass Python variables and DataFrames into a query. Typed SQL literal values can be bound with `:name`, table or column identifiers with `IDENTIFIER(:name)`, and DataFrames in the notebook namespace with `{df}`:
         
         min_id = 10
         df = spark.createDataFrame([(5, 'a'), (15, 'b')], ['id', 'val'])
         
         
         %%sparksql
         SELECT * FROM {df} WHERE id >= :min_id
         




To use advanced options, add flags to the `%%sparksql` command. For example, to cache results and create a view, run the following command:
    
    
    %%sparksql --cache --view result_view df
    SELECT * FROM your_table WHERE condition = true
    

The following options are available:

  * `--cache` or `-c`: caches the DataFrame.
  * `--eager` or `-e`: computes the result immediately using `localCheckpoint(eager=True)`.
  * `--view VIEW` or `-v VIEW`: creates a temporary view.
  * `--limit N` or `-l N`: overrides the default row display limit (cell magic only).
  * `--display MODE` or `-d MODE`: sets the display mode (`colabsqlviz` or `html`; cell magic only).
  * `--quiet` or `-q`: suppresses table display.
  * `--explain [MODE]`: prints the query plan instead of displaying results.
  * `--session NAME` or `-s NAME`: runs against the `SparkSession` in variable `NAME`.
  * `variable_name`: stores the result in a variable (cell magic only; defaults to `_df`).



## Install PyPI packages on the remote session

To use third-party Python packages inside PySpark user-defined functions (UDFs) without building a custom container image or restarting the session, you can install PyPI packages directly onto the remote session's driver and executors:

### Notebook magic

In an interactive notebook with an active `ManagedSparkSession`, use the `%dpip` magic command (loaded automatically with `google.cloud.managed_spark_connect` when the `interactive` extra is installed):
    
    
    %dpip install scipy
    

`%dpip` only installs packages on the remote session. To import a package in local code outside Spark, install it in your local Python environment as well.

### Python API

In scripts or notebooks, pass `pypi=True` to `spark.addArtifacts()`:
    
    
    spark.addArtifacts("scipy", pypi=True)
    

## What's next

  * Learn more about [Managed Service for Apache Spark sessions and runtime profiles (session templates)](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates).

  * [Visualize Spark DataFrames in notebooks](https://docs.cloud.google.com/managed-spark/docs/guides/visualize-dataframes-notebooks).

  * Learn about developing Spark code in VS Code using [Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
