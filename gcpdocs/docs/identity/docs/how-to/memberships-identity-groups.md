---
url: https://docs.cloud.google.com/identity/docs/how-to/memberships-identity-groups/
title: Managing identity-mapped group memberships \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:30:03.084981+00:00
---

# Managing identity-mapped group memberships  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/memberships-identity-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing identity-mapped group memberships

After a group exists, you can create memberships for it. This page explains how to perform some fundamental membership operations with the Cloud Identity Groups API.

**Note:** To learn how to create an identity-mapped group, refer to [Creating and searching for identity groups](https://docs.cloud.google.com/identity/docs/how-to/create-identity-groups).

## Before you begin

Set up authentication and install the client libraries. See [Setting up the Cloud Identity Groups API](https://docs.cloud.google.com/identity/docs/how-to/setup) to learn how.

## Adding a membership to an identity-mapped group

###  REST 

To add a member to an identity-mapped group, call [`groups.memberships.create()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/create) with the ID of the parent group and a [memberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships) resource.

###  Python 

The following code shows you how to associate a member with a group:
    
    
    def create_identity_group_membership(service, identity_source_id, group_id, member_key):
      param = "&groupKey.id=" + group_id + "&groupKey.namespace=identitysources/" + identity_source_id
      try:
        lookupGroupNameRequest = service.groups().lookup()
        lookupGroupNameRequest.uri += param
        lookupGroupNameResponse = lookupGroupNameRequest.execute()
        groupName = lookupGroupNameResponse.get("name")
        membership = {
          "memberKey": member_key,
          "roles" : {
            "name" : "MEMBER"
          }
        }
        # Create a membership using the ID for the parent group and a membership object
        response = service.groups().memberships().create(parent=groupName, body=membership).execute()
        print response
      except Exception, e:
        print e
    

## Listing memberships for an identity-mapped group

###  REST 

To list memberships in an identity-mapped group, call [`groups.memberships.list()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/list) with the ID of the parent group and a [memberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships) resource.

###  Python 

The following code lists the memberships for a group:
    
    
    def list_identity_group_membership(service, identity_source_id, group_id):
      param = "&groupKey.id=" + group_id + "&groupKey.namespace=identitysources/" + identity_source_id
      try:
        lookup_group_name_request = service.groups().lookup()
        lookup_group_name_request.uri += param
        lookup_group_name_response = lookup_group_name_request.execute()
        group_name = lookup_group_name_response.get("name")
        # List memberships
        response = service.groups().memberships().list(parent=group_name).execute()
        print response
      except Exception, e:
        print e
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
