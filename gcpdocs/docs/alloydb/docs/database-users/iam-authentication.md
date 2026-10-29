---
url: https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication/
title: IAM database authentication overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:51:33.382759+00:00
---

# IAM database authentication overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  IAM database authentication overview Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) database authentication lets you control and manage access to your AlloyDB for PostgreSQL databases using centralized IAM policies instead of database passwords.

IAM database authentication offers the following options:

  * Individual IAM authentication: you add specific users or service accounts to the cluster.
  * Group IAM authentication: you add an IAM group to the cluster, and all members of that group inherit permissions to authenticate.



Individual authentication is useful when you need to grant access to specific accounts directly. Group authentication lets you manage database access by modifying group membership, reducing the need to add or remove individual users at the cluster level.

## IAM authentication concepts

When you use IAM authentication, permission to access an AlloyDB instance isn't granted directly to the end user. Instead, permissions are grouped into roles, and roles are granted to principals. For more information about IAM roles and permissions, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

Administrators who have users sign in through IAM database authentication can use IAM to centrally manage access control to their instances using IAM policies.

IAM policies involve the following entities:

  * Principals: in AlloyDB, you can use a user account, a service account for applications, or an IAM group. For more information about principals, see [Principals](https://docs.cloud.google.com/iam/docs/overview#principals).

  * Roles: for IAM database authentication, a principal requires the `alloydb.users.login` permission, which is included in the AlloyDB Database User role (`roles/alloydb.databaseUser`), and the Service Usage Consumer role (`roles/serviceusage.serviceUsageConsumer`). To grant these permissions, bind the user, service account, or group to these predefined roles or a custom role that includes the required permissions. For more information about roles and permissions, see [Permissions and roles](https://docs.cloud.google.com/iam/docs/overview#permissions).

  * Resources: the resources that principals access are AlloyDB clusters. IAM policy bindings are applied at the project level, so that principals receive role permissions for all AlloyDB instances in the project. For more information about resources, see [Resources](https://docs.cloud.google.com/iam/docs/overview#resource).




## Compare database authentication options

Use the following table to help you decide which authentication method is the best fit for your use case.

Feature | Built-in database authentication | IAM database authentication  
---|---|---  
Authentication method | Password | Temporary authentication token  
Network traffic encryption | SSL not required | SSL required  
User management | Manual | Centralized through IAM  
  
## Automatic versus manual IAM database authentication

AlloyDB offers two methods for IAM database authentication: automatic and manual.

### Automatic IAM database authentication

Automatic IAM database authentication lets you hand off requesting and managing access tokens to an intermediary AlloyDB connector, such as the [Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview) or one of the [Language Connectors](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview).

With [automatic IAM database authentication](https://docs.cloud.google.com/alloydb/docs/connect-iam#automatic), an application needs to pass only the IAM database username in a connection request from the client. The connector submits the access token information for the password attribute on behalf of the client.

### Manual IAM database authentication

[Manual IAM database authentication](https://docs.cloud.google.com/alloydb/docs/connect-iam#procedure) requires the IAM principal to explicitly pass the access token for the password attribute in the client connection request. Principals must first sign in to Google Cloud and explicitly request the access token from IAM.

**Note:** If you're using Context-Aware Access in your IAM configuration, then you can't use an AlloyDB connector such as the Auth Proxy or one of the Language Connectors with IAM database authentication. Attempts to sign in either manually or automatically with IAM authentication fail. Connect directly to the instance instead.

To keep records of data access, including sign-ins, you can use Cloud Audit Logs. Cloud Audit Logs is turned off by default. Turn on Data Access audit logs for sign-in tracking.

## IAM group authentication

IAM group authentication lets you manage AlloyDB users at a group level on new and existing clusters, such as by using a [Cloud Identity group](https://docs.cloud.google.com/identity/docs/groups). You can manage PostgreSQL roles and permissions for multiple IAM users at the same time instead of updating each user or service account individually. When you grant or revoke database roles for a Cloud Identity group, any accounts that you add to that group inherit the privileges and roles of the group.

To enable IAM group authentication on an instance, set both the `alloydb.iam_authentication` and `alloydb.iam_group_authentication` database flags to `on`.

Using IAM group authentication, you can do the following:

  * Enable group authentication on both new and existing clusters without manual cluster patching.

  * Add a user to a group so that the user inherits IAM roles and database privileges automatically.

  * Remove a user from a group to revoke their login access and database privileges across AlloyDB clusters.

  * Grant or revoke login permissions and access to database objects for an entire group at once instead of updating individual accounts.

  * Sign in directly to AlloyDB Studio in the Google Cloud console, primary instances, or read pool instances, including first-time sign-ins directly to read pool instances without first connecting to the primary instance.

  * Restore or migrate an AlloyDB cluster from a Cloud SQL for PostgreSQL backup while mapping and preserving individual and IAM group user configurations.




Even though IAM roles and permissions are assigned at the group level, users and service accounts use their individual IAM accounts and credentials—not a shared group account—to sign in to primary instances, read pool instances, or AlloyDB Studio. AlloyDB creates a database account on the cluster for that principal during their first sign-in.

Individual sign-in and database activity for each user or service account appears in [audit logs](https://docs.cloud.google.com/alloydb/docs/audit-logging), letting you verify which account performed each action in your database.

For more information about working with Cloud Identity groups, see [Overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview). For more information about migrating from a Cloud SQL for PostgreSQL backup, see [Migrate from Cloud SQL for PostgreSQL to AlloyDB](https://docs.cloud.google.com/alloydb/docs/migrate-cloud-sql-to-alloydb).

When you add a user or service account to a group, the following changes in AlloyDB occur:

  * If you have already given IAM login permissions to the group, then the user or service account gains the ability to sign in to the AlloyDB cluster because the user or service account belongs to the group.

  * The user automatically inherits any [database privileges](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth#grant-db-privileges-iam-group) or roles that have been granted to the group.


**Note:** If you're adding an account that already has access to the cluster through individual IAM authentication, first [remove that IAM user or service account from the cluster](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth#delete-user). Then add the user or service account to the group.

When you remove a user or service account from the group, the following changes in AlloyDB occur:

  * The user loses any database privileges that were previously inherited by being a member of the group.
  * The user might still be able to create new sessions if they receive IAM sign-in permissions for the AlloyDB cluster through other group memberships. However, the user won't have database privileges from their former group membership upon signing in.

**Note:** Group membership changes take time to propagate. After a user is removed from a group, it can take some time to revoke their inherited group database privileges.

### Best practices

Follow these best practices when you use IAM group authentication:

  * When you revoke the `roles/alloydb.databaseUser` role for an IAM group in IAM, delete the group from the AlloyDB cluster.

  * When you delete a group from Cloud Identity, delete that group from the AlloyDB cluster.

  * Use groups to configure role-based access control in your database. Provide the least required privileges to the group.




### Limitations

IAM group authentication has the following limitations:

  * IAM group authentication is supported only in database version `POSTGRES_15` and later.

  * To support security, sign-ins using IAM database authentication are available only over an SSL connection. Unencrypted connections are rejected.

  * There is a per-minute sign-in quota for each instance, which includes both successful and unsuccessful sign-ins. When the quota is exceeded, sign-ins are temporarily unavailable. Avoid frequent sign-ins and restrict sign-ins by using authorized networks.

  * The shortened principal of a service account, which is the email address without the `.gserviceaccount.com` suffix, must not exceed 63 characters. PostgreSQL truncates role names longer than 63 characters in the database catalog, which causes IAM authentication to fail. If you can't shorten the service account name, see the [service account impersonation workaround](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-iam-auth).

  * You can add a maximum of 200 IAM groups to a cluster.

  * You can't add individual IAM users or service accounts that belong to a group on the same cluster. In other words, you can't add an account with the type `ALLOYDB_IAM_USER` if an identical account with the type `ALLOYDB_IAM_GROUP_USER` or `ALLOYDB_IAM_GROUP_SERVICE_ACCOUNT` already exists.

  * If an individual account already exists on a cluster with the type `ALLOYDB_IAM_USER`, you can't use the account for IAM group authentication. These user types don't inherit IAM roles and database privileges from a group. To fix this issue and to use the account with IAM group authentication, remove the individual IAM user or service account. For more information about resolving this issue, see [An existing account isn't inheriting privileges](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth#account-not-inheriting-privileges).

  * Changes to Cloud Identity group membership—such as the addition of an account—take about 15 minutes to propagate. This propagation time is in addition to the [time required for IAM changes](https://docs.cloud.google.com/iam/docs/access-change-propagation).

  * IAM group authentication requires all [password-related database flags](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags) that govern the minimum number of characters, numerical characters, and minimum length to be relaxed or disabled.

  * IAM group authentication isn't supported with managed connection pooling or PgBouncer connections.

  * IAM group authentication isn't supported with federated identities.




## What's next

  * [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth)
  * [Troubleshoot IAM authentication](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-iam-auth)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
