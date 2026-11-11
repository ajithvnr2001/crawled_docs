---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage-email/
title: Set up external storage for email \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:00:12.114360+00:00
---

# Set up external storage for email  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Set up external storage for email Stay organized with collections  Save and categorize content based on your preferences. 

Setting up external storage is a requirement for the email channel. You can use Cloud Storage or Amazon S3 as your external storage.

## Set up Cloud Storage

To set up Cloud Storage for email, see [Cloud Storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage#gcs).

Be sure that your JSON service account key contains the following fields:

  * `type: "service_account"`

  * `project_id`

  * `private_key_id`

  * `private_key`

  * `client_email`

  * `client_id`

  * `auth_uri`

  * `token_uri`

  * `auth_provider_x509_cert_url`

  * `Client_x509_cert_url`




## Set up Amazon S3 storage

When you set up authentication for Amazon S3, Contact Center AI Platform (CCAI Platform) assumes an Identity and Access Management (IAM) role that you create in your AWS account. This role grants CCAI Platform the permissions required to access your Amazon S3 bucket.

The JSON service account key for this authentication method requires the following fields:

  * `region`: The AWS region where your Amazon S3 bucket is located—for example, `"us-east-1"`.

  * `role_arn`: The Amazon Resource Name (ARN) of the IAM role that CCAI Platform assumes. This ARN uniquely identifies the role that has been configured with the appropriate access policies.

  * `external_id`: An identifier that you provide when creating the trust policy for the role. CCAI Platform passes this ID when it requests to assume the role, ensuring that only the intended entity can do so.




To create an Amazon S3 JSON service account key, follow these steps:

  1. Sign in to your AWS account.

  2. Navigate to the **IAM Dashboard**.

  3. In the **IAM Dashboard** , select **Roles** , and then **Create role**.

  4. To configure the trust relationship, do the following:

     1. Select **Another AWS account** as the trusted entity.

     2. Enter the account ID of the entity that will be assuming the role.

**Note:** If you don't have your account ID, contact Support.
     3. Optional: You can add an external ID for an additional layer of security.

  5. Set permissions, attach a policy that grants the role the necessary permissions for your Amazon S3 bucket. Google recommends that you use a policy with the least privilege necessary (for example, read and write access to a specific bucket) rather than full Amazon S3 access. The following are the required Amazon S3 permissions:

     * `"s3:ListBucket"`,

     * `"s3:GetObject"`,

     * `"s3:PutObject"`,

     * `"s3:DeleteObject"`

  6. Follow the remaining prompts to create the role. You will be provided with a **Role ARN**.

  7. To create the JSON file, use the Role ARN and an external ID (if used) as in the following example:
         
         {
           "region": "YOUR-AWS-REGION",
           "role_arn": "YOUR_ROLE_ARN",
           "external_id": "YOUR_EXTERNAL_ID"
         }
         




## Configure email storage

If you are using Google Cloud as your data server, ensure that your Cloud Storage role is set to **Storage Admin** to prevent errors during setup. For more information, see [IAM roles for Cloud Storage](https://cloud.google.com/storage/docs/access-control/iam-roles).

To configure your email storage, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Email Account Management** section, and then click **Manage Email Account**.

  3. In the **Data Management** section, select a data storage duration.

  4. In the **Data Server** section, select either **Google Cloud** or **Amazon S3**. The same information is required for both options:

     * **Bucket Name** : Enter the exact name of your storage bucket.

     * **Service Account Key (JSON file)** : Upload the JSON key file for your Google Cloud or Amazon S3 service account.

     * **Folder Path** : This path is automatically generated. When you link an email account, the system automatically creates a folder within your specified bucket.

  5. Click **Test Connection** to verify credentials and bucket details are correct.

  6. Click **Save**.




The system is configured to store email data from linked email accounts. You can expect the following behavior:

  * Automatic data sync: The system automatically syncs email data, including metadata and attachments, from your mail servers to the configured storage bucket every 45 seconds.

  * Connection monitoring: The system continuously monitors the connection to your email storage and email servers. If a connection can't be re-established for more than 30 minutes, an automated notification email is sent to the Admin users for your instance. The system also has an automatic retry logic to re-establish a failed connection.




### Email retention policy

The storage duration that you set in the **Data Management** section represents the amount of time an email is held in your storage bucket. After that time, the email is deleted from storage. If you reply to an email thread after the set storage time (for example, storage time is set to 60 days, and you reply on day 61), then the entire email thread is retrieved from your IMAP server, including any attachments. However, emails older than three years aren't visible.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
