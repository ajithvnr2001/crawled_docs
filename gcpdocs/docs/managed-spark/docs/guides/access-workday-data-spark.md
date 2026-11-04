---
url: https://docs.cloud.google.com/managed-spark/docs/guides/access-workday-data-spark/
title: Access Workday data with Spark \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:35:52.982217+00:00
---

# Access Workday data with Spark  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/access-workday-data-spark/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Access Workday data with Spark Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark lets you query and analyze external business data directly from your Spark workloads. You can use the Workday Live Data Query JDBC driver to connect to your Workday tenant, load live Workday datasets into Spark DataFrames, and integrate that data into your analytics pipeline on Google Cloud.

In this guide, you configure Workday Live Data Query, store your private key securely in Secret Manager, and use the Google Cloud Data Agent Kit extension to run a PySpark notebook in Visual Studio Code or Cloud Shell Editor against Managed Service for Apache Spark.

## Costs

The Data Agent Kit extension is available at no additional cost. However, this guide uses the following billable components of Google Cloud:

  * [Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/pricing)

  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)

  * [Secret Manager](https://docs.cloud.google.com/secret-manager/pricing)




To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Dataproc, Dataplex, Cloud Storage, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,dataplex.googleapis.com,storage-component.googleapis.com,secretmanager.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. Verify that you have the permissions required to complete this guide. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Dataproc, Dataplex, Cloud Storage, and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com,dataplex.googleapis.com,storage-component.googleapis.com,secretmanager.googleapis.com)




#### Required Identity and Access Management (IAM) roles

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles might have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam-serverless#do_you_need_to_grant_roles). For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

The roles that you need depend on how your workload runs. Managed Service for Apache Spark serverless 2.3 and earlier serverless runtimes run workloads as a service account. Managed Service for Apache Spark serverless runtimes 3.0 and later by default run workloads with your end-user credentials (EUC), so you grant data access roles to your user account instead of a service account. If you specify a custom service account for a 3.0 or later runtime, the workload runs with service account credentials. For more information, see [Serverless deployments roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam-serverless#s8s-role-requirements).

##### User roles

To get the permissions that you need to create an Managed Service for Apache Spark interactive notebook session and access resources, ask your administrator to grant you the following IAM roles: 

  * Use serverless runtime 2.3 or earlier: 
    * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account or a custom service account
  * Use serverless runtime 3.0 or later: [Dataproc Serverless Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`) on the project 
  * Read the JDBC driver from Cloud Storage with end-user credentials: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the bucket containing the driver 
  * Read the private key secret from Secret Manager with end-user credentials: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) on the secret or project 



##### Service account roles

Grant the following roles to the service account that runs your workload. Managed Service for Apache Spark serverless runtimes 3.0 and later need these roles only if the workload runs with service account credentials instead of the default end user credentials (EUC).

To ensure that the Compute Engine default service account or a custom service account has the necessary permissions to run Managed Service for Apache Spark workloads, read the driver, and access secrets, ask your administrator to grant the following IAM roles to the Compute Engine default service account or a custom service account: 

**Important:** You must grant these roles to the Compute Engine default service account or a custom service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Use serverless runtime 2.3 or earlier: [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) on the project 
  * Use serverless runtime 3.0 or later with service account credentials instead of the default end user credentials (EUC): 
    * [Dataproc Serverless Node ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`) on the project
    * [Dataproc Resource Manager Node Service Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.nodeServiceAgent) (`roles/dataprocrm.nodeServiceAgent`) on the project
  * Read the JDBC driver from Cloud Storage: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the bucket containing the driver 
  * Read the private key secret from Secret Manager: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) on the secret or project 



## Workday prerequisites

Before connecting to Workday using Live Data Query, complete the following setup:

  1. Download the Workday Live Data Query [JDBC driver](https://doc.workday.com/admin-guide/en-us/integrations/workday-data-cloud-downloads/live-data-query-downloads.html) from Workday.

  2. Upload the downloaded JDBC driver JAR file to a Cloud Storage bucket in your project.

  3. Complete the configuration steps for setting up Live Data Query in your Workday tenant as described in the [Workday Live Data Query documentation](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/workday-live-data-query.html).

During configuration in Workday, create an Integration System User (ISU), register an API client, and generate a private key pair.

  4. Note the following Workday configuration values:

     * **Workday host** : your Workday tenant host, for example, `services1.workday.com`.

     * **Tenant name** : your Workday tenant name.

     * **Client ID** : the registered API client ID from your Workday tenant.

     * **ISU username** : the Integration System User username.




### Store the private key in Secret Manager

Store the private key file generated during Workday Live Data Query configuration securely in Secret Manager:

  1. In Cloud Shell, run the following command to generate an x509 key pair:
         
         openssl req -x509 -newkey rsa:2048 -keyout private-key.pem -out public-key.cert -sha256 -days 365 -nodes
         

  2. To view the private key, run the following command:
         
         cat private-key.pem
         

  3. Store the private key in Secret Manager:

     1. In the Google Cloud console, go to the **Secret Manager** page:

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

     2. Click **Create Secret**.

     3. In the **Name** field, enter a name for the secret, such as `workday-private-key`.

     4. Under **Secret value** , upload `private-key.pem` or paste the private key contents, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` header and footer lines.

     5. Click **Create Secret**.

  4. To view the public key, run the following command:
         
         cat public-key.cert
         

  5. In Workday, search for **Create x509 Public Key** , paste the public key from `public-key.cert`, and click **OK**.

  6. In the Workday API client created earlier, update **x509 Certificate** to the new x509 key.




## Set up the Data Agent Kit in your IDE

You can set up the Data Agent Kit either by installing the extension in Visual Studio Code or another supported IDE, or by using the pre-installed extension in [Cloud Shell Editor](https://docs.cloud.google.com/shell/docs/launching-cloud-shell-editor#launch-standalone-session).

To configure the Data Agent Kit in your IDE or Cloud Shell Editor, complete the following steps:

  1. Set up and configure the Data Agent Kit:

     1. [Install the Data Agent Kit extension](https://docs.cloud.google.com/data-agent-kit/install-extension).

The Data Agent Kit extension is pre-installed in Cloud Shell Editor.
     2. [Configure the Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/configure).

        * [Configure Google Cloud project and region](https://docs.cloud.google.com/data-agent-kit/configure#configure-google)

        * [Review required roles](https://docs.cloud.google.com/data-agent-kit/configure#review-required)

        * [Create a Managed Service for Apache Spark serverless runtime](https://docs.cloud.google.com/data-agent-kit/configure#create-serverless-runtime) if you do not have one.




## Create a notebook

Using the Data Agent Kit, create an interactive PySpark notebook:

  1. In your IDE or Cloud Shell Editor, open the **Data Agent Kit** panel.

  2. Under **Apache Spark** , select **New Notebook** , and then select **Local Kernel**.

  3. Select a runtime from the list of available runtimes (also called session templates).

  4. Select **Start with a new notebook**.

A new notebook opens with an initial cell populated with Spark Connect session initialization code.

  5. At the top of the notebook editor, click **Select Kernel** , and then select a local Python kernel for your notebook.




## Query Workday data in PySpark

**Note:** For the fastest connection, you can download the sample notebook, and then upload it directly into BigQuery > Notebook.

  1. In the first notebook cell, install the required client libraries and set up environment variables:
         
         %pip install dataproc-spark-connect google-cloud-dataproc google-cloud-secret-manager google-cloud-storage
         
         #@title Set up all environment variables
         
         # Replace with your Project ID
         %env PROJECT_ID=PROJECT_ID
         
         # Replace with the name of the Secret Manager global secret in the project
         %env SECRET_NAME=workday-private-key
         # Replace with the version of the secret to use
         %env SECRET_VERSION=latest
         
         # Replace with the Cloud Storage bucket where you have the Workday Data Cloud JDBC Driver file stored
         %env JDBC_DRIVER_GCS_BUCKET=BUCKET_NAME
         # Replace with the name of the Workday Data Cloud JDBC Driver file in the Cloud Storage bucket
         %env JDBC_DRIVER_FILE_NAME=ldq-jdbc-driver-1.1.0-all.jar
         # Replace with the local directory of the notebook to copy the JDBC Driver File to
         %env JDBC_DRIVER_LOCAL_DIRECTORY=/tmp
         # Replace with the Driver Class for the Workday Data Cloud JDBC Driver
         %env WORKDAY_DRIVER_CLASS=com.workday.ldq.jdbc.Driver
         
         # ------------------------------------------------------------------------------
         
         # Replace with the Workday URL of your tenant
         %env WORKDAY_HOST=WORKDAY_HOST
         # Replace with your Workday tenant name
         %env TENANT_NAME=TENANT_NAME
         # Replace with the Client ID of the "API Client"
         %env CLIENT_ID=CLIENT_ID
         # Replace with the Integration System User username
         %env ISU_USERNAME=ISU_USERNAME
         

  2. In a new cell, grant the Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`) to the Compute Engine default service account:
         
         %%bash
         COMPUTE_ENGINE_DEFAULT_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --project="${PROJECT_ID}" \
           --filter="email ~ -compute@developer.gserviceaccount.com" \
           --format="value(email)")
         
         echo "COMPUTE_ENGINE_DEFAULT_SERVICE_ACCOUNT: ${COMPUTE_ENGINE_DEFAULT_SERVICE_ACCOUNT}"
         
         gcloud secrets add-iam-policy-binding ${SECRET_NAME} \
           --project="${PROJECT_ID}" \
           --member="serviceAccount:${COMPUTE_ENGINE_DEFAULT_SERVICE_ACCOUNT}" \
           --role="roles/secretmanager.secretAccessor"
         

  3. In a new cell, copy the JDBC driver from Cloud Storage to the local directory:
         
         gsutil cp gs://$JDBC_DRIVER_GCS_BUCKET/$JDBC_DRIVER_FILE_NAME $JDBC_DRIVER_LOCAL_DIRECTORY
         

  4. In a new cell, install the Secret Manager client library:
         
         %%bash
         pip install google-cloud-secret-manager
         

  5. In a new cell, verify that the driver JAR file is downloaded locally:
         
         !gsutil cp gs://$JDBC_DRIVER_GCS_BUCKET/$JDBC_DRIVER_FILE_NAME /tmp/
         !ls -lh /tmp/ldq-jdbc-driver-1.1.0-all.jar
         

  6. In a new cell, inject the Workday driver JAR into the PySpark jars directory:
         
         %%bash
         
         echo "Downloading Workday JAR from Cloud Storage..."
         # Downloads your specific 1.1.0 driver JAR into the notebook's /tmp folder
         gcloud storage cp gs://$JDBC_DRIVER_GCS_BUCKET/$JDBC_DRIVER_FILE_NAME /tmp/
         
         echo "Dynamically finding the PySpark jars directory..."
         PYSPARK_JARS=$(python -c "import os, pyspark; print(os.path.join(os.path.dirname(pyspark.__file__), 'jars'))")
         echo "Found PySpark jars at: $PYSPARK_JARS"
         
         echo "Injecting Workday driver into PySpark core..."
         cp /tmp/$JDBC_DRIVER_FILE_NAME "$PYSPARK_JARS/"
         
         echo "Success! The driver is now a native part of PySpark."
         

  7. In a new cell, configure the Spark environment and retrieve the x509 private key from Secret Manager:
         
         #@title Configure the Spark environment and retrieve the x509 private key from Secret Manager
         
         import os
         import pyspark
         from pyspark.sql import SparkSession
         from google.cloud import secretmanager
         
         PROJECT_ID = os.environ["PROJECT_ID"]
         SECRET_NAME = os.environ["SECRET_NAME"]
         SECRET_VERSION = os.environ["SECRET_VERSION"]
         JDBC_DRIVER_LOCAL_DIRECTORY = os.environ["JDBC_DRIVER_LOCAL_DIRECTORY"]
         JDBC_DRIVER_FILE_NAME = os.environ["JDBC_DRIVER_FILE_NAME"]
         LOCAL_JAR_PATH = JDBC_DRIVER_LOCAL_DIRECTORY + "/" + JDBC_DRIVER_FILE_NAME
         WORKDAY_HOST = os.environ["WORKDAY_HOST"]
         TENANT_NAME = os.environ["TENANT_NAME"]
         CLIENT_ID = os.environ["CLIENT_ID"]
         ISU_USERNAME = os.environ["ISU_USERNAME"]
         WORKDAY_DRIVER_CLASS = os.environ["WORKDAY_DRIVER_CLASS"]
         
         jdbc_url = f"jdbc:workday://{WORKDAY_HOST}:443/system/information_schema?SSLVerification=CA"
         
         def access_private_key_secret():
             print(f"Fetching secret contents from Secret Manager: {SECRET_NAME}...")
             client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
             secret_name = f"projects/{PROJECT_ID}/secrets/{SECRET_NAME}/versions/{SECRET_VERSION}"
             response = client.[access_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_access_secret_version)(request={"name": secret_name})
             print(f"Fetched secret contents from Secret Manager: {SECRET_NAME}")
             return response.payload.data.decode("UTF-8")
         
         private_key_content = access_private_key_secret()
         

  8. In a new cell, initialize the Spark session with the classpath configuration:
         
         # Stop the old cached Spark session so your newly downloaded JAR is not ignored!
         try:
             spark.stop()
             print("Stopped existing Spark session.")
         except Exception:
             pass
         
         print("Initializing fresh Spark session with Classpath configuration...")
         print(f"Loading JAR from: {LOCAL_JAR_PATH}")
         
         # Rebuild Spark session with explicit Driver & Executor classpaths
         spark = SparkSession.builder \
             .appName("WorkdayJDBC Connection Example") \
             .config("spark.jars", LOCAL_JAR_PATH) \
             .config("spark.driver.extraClassPath", LOCAL_JAR_PATH) \
             .config("spark.executor.extraClassPath", LOCAL_JAR_PATH) \
             .getOrCreate()
         print("Spark Session successfully booted with JAR!")
         

  9. In a final cell, initiate the connection and query Workday:
         
         import os
         import subprocess
         import zipfile
         from pyspark.sql import SparkSession
         
         LOCAL_JAR_PATH = "/tmp/ldq-jdbc-driver-1.1.0-all.jar"
         
         # Load bucket and file name from your Cell 1 environment variables
         GCS_BUCKET = os.environ.get("JDBC_DRIVER_GCS_BUCKET", "BUCKET_NAME")
         GCS_FILE = os.environ.get("JDBC_DRIVER_FILE_NAME", "ldq-jdbc-driver-1.1.0-all.jar")
         GCS_URI = f"gs://{GCS_BUCKET}/{GCS_FILE}"
         
         # 1. Ensure the JAR file is in the notebook's /tmp directory
         if not os.path.exists(LOCAL_JAR_PATH):
             print(f"Downloading {GCS_URI} to {LOCAL_JAR_PATH}...")
             subprocess.run(["gsutil", "cp", GCS_URI, LOCAL_JAR_PATH], check=True)
         print(f"JAR verified on disk: {LOCAL_JAR_PATH} ({os.path.getsize(LOCAL_JAR_PATH):,} bytes)")
         
         # 2. Read the real JDBC driver class name (skipping any '#' comment lines!)
         with zipfile.ZipFile(LOCAL_JAR_PATH, "r") as z:
             raw_lines = (
                 z.read("META-INF/services/java.sql.Driver")
                 .decode("utf-8")
                 .splitlines()
             )
             # Filter out empty lines and '#' comment lines
             valid_classes = [
                 line.strip()
                 for line in raw_lines
                 if line.strip() and not line.strip().startswith("#")
             ]
             driver_class = valid_classes[0]
         
         print(f"Real Driver Class inside JAR: {driver_class}")
         
         # 3. Get or create the Spark session
         spark = SparkSession.builder.appName("WorkdayJDBC Connection Example").getOrCreate()
         
         # 4. Inject the JAR directly into the running Java URLClassLoader (and Scala SparkContext)
         jvm = spark.sparkContext._jvm
         jar_url = jvm.java.io.File(LOCAL_JAR_PATH).toURI().toURL()
         
         # Add to both the Spark classloader and the current thread's context classloader
         jvm.org.apache.spark.util.Utils.getContextOrSparkClassLoader().addURL(jar_url)
         jvm.java.lang.Thread.currentThread().getContextClassLoader().addURL(jar_url)
         spark.sparkContext._jsc.sc().addJar(LOCAL_JAR_PATH)
         
         # Register the driver class with Spark's JDBC DriverRegistry
         jvm.org.apache.spark.sql.execution.datasources.jdbc.DriverRegistry.register(driver_class)
         print(f"Successfully registered {driver_class} in Spark's live JVM!")
         
         # 5. Query Workday
         print("Querying Workday...")
         df_data = (
             spark.read.format("jdbc")
             .option("driver", driver_class)
             .option("url", jdbc_url)
             .option("wd.authn.clientId", CLIENT_ID)
             .option("wd.authn.isu", ISU_USERNAME)
             .option(
                 "wd.authn.accessTokenEndpoint",
                 f"https://{WORKDAY_HOST}/ccx/oauth2/{TENANT_NAME}/token",
             )
             .option("wd.authn.privateKey", private_key_content)
             .option("query", "SELECT * FROM system.jdbc.catalogs")
             .load()
         )
         
         print("Connection Successful! Data Retrieved:")
         df_data.show(50, truncate=False)
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `LOCATION`: the Google Cloud region of your Managed Service for Apache Spark session template, for example, `us-central1`.
     * `RUNTIME_ID`: the ID of your Managed Service for Apache Spark session template.
     * `BUCKET_NAME`: the name of the Cloud Storage bucket containing the Workday JDBC driver.
     * `PATH/workday-live-data-query-jdbc-driver.jar`: the object path to the Workday JDBC driver JAR in your Cloud Storage bucket.
     * `WORKDAY_HOST`: your Workday tenant host, for example, `services1.workday.com`.
     * `TENANT_NAME`: your Workday tenant name.
     * `CLIENT_ID`: the registered API client ID from your Workday tenant.
     * `ISU_USERNAME`: the Integration System User username from your Workday tenant.
  10. Click **Execute Cell** (the play icon) next to the cell, or press `Shift+Enter`.

Managed Service for Apache Spark executes the query and displays the Workday DataFrame output below the cell.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this guide, terminate active interactive sessions or delete the created resources.

### Terminate interactive sessions

  1. In your IDE or Cloud Shell Editor, terminate the active notebook session when your workload finishes.

  2. **Optional:** Delete the Cloud Storage bucket or JDBC driver JAR file if you no longer need them.

  3. **Optional:** Delete the secret from Secret Manager if it is no longer needed:
         
         gcloud secrets delete workday-private-key
         




## What's next

  * Learn more about [Workday Live Data Query](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/workday-live-data-query.html).

  * Learn more about [Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview).

  * Explore [Managed Service for Apache Spark interactive sessions](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates).

  * Read about [Spark JDBC connection options](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html#data-source-option).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
