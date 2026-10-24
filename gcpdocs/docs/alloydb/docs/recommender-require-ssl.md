---
url: https://docs.cloud.google.com/alloydb/docs/recommender-require-ssl/
title: Improve instance security by enforcing SSL or TLS encryption \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:25:48.670502+00:00
---

# Improve instance security by enforcing SSL or TLS encryption  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/recommender-require-ssl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Improve instance security by enforcing SSL or TLS encryption Stay organized with collections  Save and categorize content based on your preferences. 

To identify AlloyDB for PostgreSQL production instances that allow unencrypted direct connections and protect your data in transit, you can view and apply recommendations from the AlloyDB enforce SSL mode [recommender](https://docs.cloud.google.com/recommender/docs/whatis-activeassist).

The AlloyDB enforce SSL mode recommender analyzes instance metadata. If an instance is a production instance and doesn't enforce encryption requirements for direct connections, the recommender recommends that you enable SSL mode.

Recommendations are generated daily.

## Before you begin

Before you can view recommendations and insights, do the following:

  * [Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api).

  * To get the permissions to view and work with insights and recommendations, ask your administrator to grant you the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions): 

Tasks | Roles  
---|---  
View recommendations |  AlloyDB Recommender Viewer (`roles/recommender.alloydbViewer`)   
Apply recommendations |  AlloyDB Recommender Admin (`roles/recommender.alloydbAdmin`) or AlloyDB Admin (`roles/alloydb.admin`)   
  
See [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access) for more information.




## List the recommendations

You can list recommendations for enforcing SSL mode by using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

For more information, see [Find recommendations with Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist).

  2. In the **Resources** list table, find the cluster and click **View issues** in the **Issues** column.

A list of issues is displayed in the **Aggregated issues** panel. Select the **Allows direct unencrypted connections** recommendation card.




###  gcloud CLI 

To list recommendations for enforcing SSL mode by using the gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.alloydb.instance.SecurityRecommender \
    --filter=recommenderSubtype=REQUIRE_SSL
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




###  API 

To list recommendations for enforcing SSL mode by using the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.alloydb.instance.SecurityRecommender/recommendations?filter=recommenderSubtype=REQUIRE_SSL
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that require enforcing SSL mode by using the Google Cloud console, gcloud CLI, or the Recommender API.

To view insights and detailed recommendations, follow these steps:

###  Console 

On the **Clusters** page, under the **Resources** table, click **View issues** in the **Issues** column for the cluster.

The **Aggregated issues** panel appears on the right, which contains insights and detailed recommendations for **Allows direct unencrypted connections**.

###  gcloud CLI 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.alloydb.instance.SecurityInsight \
    --filter=insightSubtype=SSL_NOT_REQUIRED
    
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.alloydb.instance.SecurityInsight/insights?filter=insightSubtype=SSL_NOT_REQUIRED
    

Replace the following:

  * `PROJECT_ID`: your project ID.

  * `LOCATION`: the region where your instances are located, such as `us-central1`.




## Apply the recommendation

Evaluate the recommendation carefully and do any of the following:

###  Console 

To implement the recommendation, [enforce SSL/TLS mode](https://docs.cloud.google.com/alloydb/docs/instance-ssl#configure_the_ssl_enforcement_mode_on_an_instance) on your instance.

###  gcloud CLI 

To implement the recommendation, [enforce SSL/TLS mode](https://docs.cloud.google.com/alloydb/docs/instance-ssl#configure_the_ssl_enforcement_mode_on_an_instance) on your instance.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
