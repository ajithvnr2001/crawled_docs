---
url: https://docs.cloud.google.com/oracle/database/docs/create-manage-custom-dns/
title: Create and manage Custom DNS domains \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:19:14.398146+00:00
---

# Create and manage Custom DNS domains  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/create-manage-custom-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Create and manage Custom DNS domains Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage custom Domain Name System (DNS) domains.

You can choose the default custom DNS domain or create a custom DNS domain for your ODB Network. You can create multiple custom DNS domains, but you can associate each domain with only one ODB Network.

Custom DNS domains let you control the names of your resources, delegate DNS resolution within your organization, and issue SSL certificates for the hosts that reside within your domain. For example, if you create a custom DNS domain named `oradb.example.com` for your ODB Network, then you can name a cluster `db1.oradb.example.com`.

You can use custom DNS domains only with Exadata VM Clusters. Custom DNS domains replace the default `oraclevcn.com` domain for Exadata VM Clusters, aligning endpoints with your corporate namespace for easier connectivity and compliance.

## Create a custom DNS domain

To create a custom DNS domain, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the ODB Network for which you want to create the custom DNS domain.

  3. On **ODB Network details** page, go to the **Custom DNS domain** section.

  4. Click **Create**.

  5. On the **Create DNS domain** page, do the following:

     1. In the **Resource ID** field, enter a unique ID for the domain that follows these naming conventions:

        * Can have a maximum of 63 characters
        * Must consist of lowercase letters, numbers, and hyphens
        * Must start with a lowercase letter
        * Must end with a lowercase letter or a number
     2. In the **Domain name** field, enter a domain name that follows these naming conventions:

        * Can consist of alphanumeric characters
        * Can have a maximum of three subdomains
        * Must use periods to separate subdomains
        * The combined prefix and domain must be under 110 characters
        * The `oraclevcn.com` domain is reserved and you must not use the domain for your custom domains



### gcloud

Use the `gcloud oracle-database odb-networks odb-dns-zones create` command to create a custom DNS domain.
    
    
    gcloud oracle-database odb-networks odb-dns-zones create DOMAIN_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --odb-network=ODB_NETWORK_ID \
        --domain=DOMAIN_NAME
    

Replace the following:

  * DOMAIN_ID: a unique ID for the domain that follows these naming conventions:

    * Can have a maximum of 63 characters
    * Must consist of lowercase letters, numbers, and hyphens
    * Must start with a lowercase letter
    * Must end with a lowercase letter or a number
  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.

  * REGION: the region where your ODB Network is located.

  * ODB_NETWORK_ID: the ID of the ODB Network.

  * DOMAIN_NAME: a name for the domain that follows these naming conventions:

    * Can consist of alphanumeric characters
    * Can have a maximum of three subdomains
    * Must use periods to separate subdomains
    * The combined prefix and domain must be under 110 characters
    * The `oraclevcn.com` domain is reserved and you must not use the domain for your custom domains



###  API 

To create a custom DNS domain, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbDnsZones/DOMAIN_ID" \
    -d \
    '{
      "domain": "DOMAIN_NAME"
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.
  * REGION: the region where your ODB Network is located.
  * ODB_NETWORK_ID: the ID of the ODB Network.
  * DOMAIN_ID: a unique ID for the domain that follows these naming conventions:

    * Can have a maximum of 63 characters
    * Must consist of lowercase letters, numbers, and hyphens
    * Must start with a lowercase letter
    * Must end with a lowercase letter or a number
  * DOMAIN_NAME: a name for the domain that follows these naming conventions:

    * Can consist of alphanumeric characters
    * Can have a maximum of three subdomains
    * Must use periods to separate subdomains
    * The combined prefix and domain must be under 110 characters
    * The `oraclevcn.com` domain is reserved and you must not use the domain for your custom domains



After you create the custom DNS domain, it appears in the **Custom DNS domain** list.

## View custom DNS domain information

To view information about your custom DNS domains, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the ODB Network for which you want to view the custom DNS domains.

  3. On the **ODB Network details** page, go to the **Custom DNS domain** section.

  4. To view details about a domain, click its name.




### gcloud

  * **List domains**

Use the `gcloud oracle-database odb-networks odb-dns-zones list` command to list domains.
        
        gcloud oracle-database odb-networks odb-dns-zones list \
            --project=PROJECT_ID \
            --location=REGION \
            --odb-network=ODB_NETWORK_ID
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.
    * REGION: the region where your ODB Network is located.
    * ODB_NETWORK_ID: the ID of the ODB Network with which the domains are associated.
  * **View domain details**

Use the `gcloud oracle-database odb-networks odb-dns-zones describe` command to view details of a domain.
        
        gcloud oracle-database odb-networks odb-dns-zones describe DOMAIN_ID \
            --project=PROJECT_ID \
            --location=REGION \
            --odb-network=ODB_NETWORK_ID
        

Replace the following:

    * DOMAIN_ID: the ID of the domain.
    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.
    * REGION: the region where your ODB Network is located.
    * ODB_NETWORK_ID: the ID of the ODB Network with which the domain is associated.



###  API 

  * **List domains**

To list domains, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbDnsZones"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.
    * REGION: the region where your ODB Network is located.
    * ODB_NETWORK_ID: the ID of the ODB Network with which the domains are associated.
  * **View domain details**

To view details of a domain, run the following `curl` command:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbDnsZones/DOMAIN_ID"
        

Replace the following:

    * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.
    * REGION: the region where your ODB Network is located.
    * ODB_NETWORK_ID: the ID of the ODB Network with which the domain is associated.
    * DOMAIN_ID: the ID of the domain.



## Delete a custom DNS domain

If a resource is using a custom DNS domain, then you can't delete the domain. First, delete the resource, and then delete the domain.

To delete your custom DNS domain, do the following:

### Console

  1. Go to the **ODB Network** page.

[Go to ODB Network](https://console.cloud.google.com/oracle/odb-networks/)

  2. Click the ODB Network network for which you want to delete a domain.

  3. Go to the **Custom DNS Domain** section.

  4. For the domain that you want to delete, click more_vert **View actions** , and then click **Delete**.

  5. In the **Delete DNS domain?** dialog, type the domain name and **Confirm**.




### gcloud

Use the `gcloud oracle-database odb-networks odb-dns-zones delete` command to delete a domain.
    
    
    gcloud oracle-database odb-networks odb-dns-zones delete DOMAIN_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --odb-network=ODB_NETWORK_ID
    

Replace the following:

  * DOMAIN_ID: the ID of the domain.
  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.
  * REGION: the region where your ODB Network is located.
  * ODB_NETWORK_ID: the ID of the ODB Network with which the domain is associated.



###  API 

To delete a domain, run the following `curl` command:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/odbNetworks/ODB_NETWORK_ID/odbDnsZones/DOMAIN_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project. If you're using a Shared VPC, then use the ID of your host project.
  * REGION: the region where your ODB Network is located.
  * ODB_NETWORK_ID: the ID of the ODB Network with which the domain is associated.
  * DOMAIN_ID: the ID of the domain.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
