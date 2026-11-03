---
url: https://docs.cloud.google.com/oracle/database/docs/troubleshoot-database-connection/
title: Troubleshoot Database Connections and SQL runtime issues \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:19:00.110290+00:00
---

# Troubleshoot Database Connections and SQL runtime issues  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/troubleshoot-database-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Troubleshoot Database Connections and SQL runtime issues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Database Connections and SQL runtime issues and how to resolve them.

## Configuration and validation errors

This section describes issues that you might encounter when using Database Connections.

Issue | Cause | Resolution  
---|---|---  
`INVALID_CONNECTION_STRING` | Must be **Easy Connect** or **TNS**. **Easy Connect Plus** isn't supported. | Use `host:port/service` or a TNS descriptor.  
`MISSING_TNS_COORDINATES` | TNS descriptor is missing `ADDRESS` or `CONNECT_DATA` values. | Update the TNS Descriptor with correct values.  
`UNSUPPORTED_HA_PARAMETERS` | Parameters `FAILOVER`, `LOAD_BALANCE`, `RETRY_*`, and `CONNECT_TIMEOUT` aren't supported. | Remove these parameters from the TNS string.  
`SERVICE_CONNECTIVITY_NOT_ENABLED` | The ODB Network doesn't have service connectivity. | Update the ODB Network with a network attachment, or create a new one.  
`ODB_NETWORK_NOT_FOUND` or `ODB_NETWORK_NOT_AVAILABLE` | The ODB Network doesn't exist or isn't available. | Wait for the ODB Network to become available. Also, check if you've used the correct ODB Network name.  
`ODB_NETWORK_MISSING_PSC_NETWORK_ATTACHMENT` | No PSC network attachment. | Set network attachment.  
`ODB_NETWORK_SERVICE_CONNECTIVITY_CONFIG_BEING_DELETED` | Service connectivity is being removed. | Wait, or re-enable the service connectivity.  
`ODBNETWORK_IN_USE_BY_DATABASE_CONNECTIONS` | Can't delete the ODB Network while it is in use by the Database Connections. | Delete the connections first.  
`ODBNETWORK_SERVICE_CONNECTIVITY_CONFIG_IN_USE` | Can't disable service connectivity while connections use it. | before disabling service connectivity, delete the Database Connections.  
`SECRET_ACCESS_DENIED` | Service account can't access the secret. | Grant Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`) to the service account (`service-PROJECT_NUMBER@gcp-sa-oci.iam.gserviceaccount.com`). You can find the service account and the secret from the error message itself.  
`SERVICE_AGENT_PERMISSION_DENIED` | Service agent lacks a permission on a resource. | Grant the permission that's named in the message.  
  
### Runtime error

This section describes issues that you might encounter when testing Database Connections and executing SQL statements.

**Note:** Some errors have `is_retryable` field that indicates if you can retry the request.Issue | Cause | Resolution  
---|---|---  
`ORACLE_AUTH_FAILED` | Wrong database username or password. | Confirm that you're using the correct secret and check the credentials in the secret.  
`DATABASE_NOT_READY` | The database or the listener isn't accepting connections. | Check the database state and retry.  
`DATABASE_NETWORK_UNREACHABLE` | Can't reach the host or the hostname in the connection string couldn't be resolved. | Use an IP address as the host and check the network attachment setup.  
`DATABASE_CERTIFICATE_INVALID` | TLS handshake or certificate DN mismatch. | Check the `ssl_server_cert_dn`, the wallet, and the port.  
`DATABASE_CONNECTION_FAILED` | Connection couldn't be opened or was dropped. | Check the network and retry.  
`QUERY_TIMEOUT` | Statement ran longer than the timeout. | Optimize the query or narrow its scope.  
`SESSION_QUEUE_TIMEOUT` or `SESSION_CAPACITY_EXHAUSTED` | Too many concurrent requests. | Retry with backoff and reduce concurrency.  
`SQL_EXECUTION_SERVICE_UNAVAILABLE` or `INTERNAL_DRIVER_ERROR` | There might be an issue on the Google Cloud side. | Retry. If the issue persists, contact [Cloud Customer Care](https://cloud.google.com/support-hub).  
`ORA-00942` | The table or view doesn't exist. | Check the name of the table or view, and if it exists or not.  
`ORA-29024` | The certification doesn't match or is missing. | Check if the certificate is valid or obtain a new certificate.  
`ORA-01017` | Wrong database username or password. | Confirm that you're using the correct secret and check the credentials in the secret.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
