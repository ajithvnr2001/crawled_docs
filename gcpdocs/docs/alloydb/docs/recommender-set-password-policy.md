---
url: https://docs.cloud.google.com/alloydb/docs/recommender-set-password-policy/
title: Improve instance security by setting password policies \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T01:29:25.378590+00:00
---

# Improve instance security by setting password policies  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/recommender-set-password-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Improve instance security by setting password policies Stay organized with collections  Save and categorize content based on your preferences. 

To identify AlloyDB for PostgreSQL instances without a password policy, enforce strong passwords, and help meet compliance requirements, you can view and apply recommendations from the AlloyDB password policy [Recommender](https://docs.cloud.google.com/recommender/docs/whatis-activeassist).

The AlloyDB password policy Recommender detects instances that don't have an instance password policy enabled and provides insights and recommendations to improve your instance security.

Recommendations are generated daily.

## Pricing

The AlloyDB password policy Recommender is available at no additional charge to all Google Cloud customers. For more information, see [Recommender pricing](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, you must do the following:

  * [Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api).

  * To get the permissions to view and work with insights and recommendations, ask your administrator to grant you the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions): 

Tasks | Roles  
---|---  
View recommendations |  AlloyDB Recommender Viewer (`roles/recommender.alloydbViewer`)   
Apply recommendations |  AlloyDB Recommender Admin (`roles/recommender.alloydbAdmin`) or AlloyDB Admin (`roles/alloydb.admin`)   
  
See [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access) for more information.




## List the recommendations

You can list the password policy recommendations by using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

To list password policy recommendations by using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the AlloyDB **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

For more information, see [Getting started with Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist).

  2. In the **Resources** list table, find the cluster and click **View issues** in the **Issues** column.

  3. In the **Aggregated issues** panel, select the **No password policy** recommendation card.




###  gcloud CLI 

To list password policy recommendations by using the gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.alloydb.instance.SecurityRecommender \
    --filter=recommenderSubtype=ENABLE_INSTANCE_PASSWORD_POLICY
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




###  API 

To list password policy recommendations by using the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.alloydb.instance.SecurityRecommender/recommendations?filter=recommenderSubtype=ENABLE_INSTANCE_PASSWORD_POLICY
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that require enabling instance password policies by using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

On the **Clusters** page, under the **Resources** table, click **View issues** in the **Issues** column for the cluster.

The **Aggregated issues** panel appears on the right, which contains insights and detailed recommendations for **No password policy**.

###  gcloud CLI 

To view insights and detailed recommendations about instances that require enabling instance password policies, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.alloydb.instance.SecurityInsight \
    --filter=insightSubtype=INSTANCE_PASSWORD_POLICY_NOT_ENABLED
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




###  API 

To view insights and detailed recommendations about instances that require enabling instance password policies by using the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.alloydb.instance.SecurityInsight/insights?filter=insightSubtype=INSTANCE_PASSWORD_POLICY_NOT_ENABLED
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




## Apply the recommendation

To implement this recommendation, do the following:

  1. In the **Resources** list table, click **View issues** in the **Issues** column for the cluster.
  2. In the **Aggregated issues** panel, select the **No password policy** recommendation card and click **Edit instance**.
  3. [Set an instance password policy](https://docs.cloud.google.com/alloydb/docs/database-users/manage-password-policy#set-password-policy).

**Note:** Carefully evaluate the recommendation before you update the instance to avoid disrupting existing database users whose passwords don't meet the policy requirements.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
