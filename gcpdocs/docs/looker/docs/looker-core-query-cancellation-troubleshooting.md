---
url: https://docs.cloud.google.com/looker/docs/looker-core-query-cancellation-troubleshooting/
title: Troubleshoot unexpected query cancellations in Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:42:30.825611+00:00
---

# Troubleshoot unexpected query cancellations in Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-query-cancellation-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Troubleshoot unexpected query cancellations in Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

When you run an interactive query in Looker (Google Cloud core), the query might appear to run indefinitely in the Explore UI or on a dashboard. However, backend database logs indicate that the query was explicitly canceled after 20 to 30 seconds.

This page explains why this behavior occurs and how to resolve it by adjusting timeout settings on your intermediate network infrastructure. This guide is intended for administrators who manage network routing and troubleshoot queries in Looker (Google Cloud core).

## Symptoms

When you run an interactive query in an Explore or on a dashboard, you might experience the following symptoms:

  * **Looker user interface** : The Looker Explore UI or dashboard tile remains in a **Running** (spinning) state indefinitely and never returns results or displays an error.
  * **Backend database execution time** : In your backend database (such as BigQuery, Snowflake, or PostgreSQL), the query is canceled after a short duration—typically 20 to 30 seconds.
  * **Backend database query logs** : The query history or audit logs in your backend database indicate that the job was explicitly canceled by the user, even though you didn't cancel the query or close the browser tab.



## Cause

This issue occurs due to a mismatch between Looker's session heartbeat mechanism and the timeout settings that are configured on intermediate network devices that route traffic between your browser and the Looker (Google Cloud core) instance.

### Session heartbeat and query abandonment mechanism

To manage database resource usage efficiently, Looker (Google Cloud core) monitors client connectivity during query execution through the following mechanism:

  * **Continuous heartbeat** : When you run an interactive query in the Looker UI, your web browser maintains an active connection and sends continuous heartbeat signals to the Looker (Google Cloud core) instance to keep the query session active.
  * **Intermediate connection timeout** : If an intermediate network device—such as an Application Load Balancer, a corporate reverse proxy, a Web Application Firewall (WAF), or a VPN gateway—has a short idle or response timeout configuration (for example, the default 30-second backend service timeout on Google Cloud Application Load Balancers), the device prematurely closes or drops the connection when the query runtime exceeds that threshold.
  * **Query abandonment detection** : After the intermediate connection is closed, Looker (Google Cloud core) stops receiving heartbeat signals from your browser. After approximately 30 seconds without a heartbeat signal, Looker (Google Cloud core) detects that the client session is no longer reachable and identifies the query as abandoned.
  * **Database cleanup** : To avoid consuming unnecessary database compute resources on queries that no user is waiting for, Looker (Google Cloud core) automatically sends a cancellation request to your backend database. Because Looker issues the cancellation on behalf of the user who ran the query, the database logs record that the job was canceled by the user.
  * **Indefinite running state in the UI** : Because the intermediate proxy or gateway closed the connection between your browser and Looker (Google Cloud core), your browser never receives the cancellation status or error response. As a result, the Looker Explore UI or dashboard tile remains stuck in the **Running** state.



## Identify the issue

To determine whether your query cancellations are caused by intermediate network timeouts, follow these steps:

  1. **Check database query logs** : Review the execution history in your backend database for the canceled query: 
     * In **BigQuery** , go to the **Query history** page in the Google Cloud console or check the project's job history in the Google Cloud console and locate the failed job. Check the job details to confirm that the query was canceled after approximately 20 to 30 seconds with a cancellation status.
     * In **Snowflake** , inspect the `QUERY_HISTORY` view or the **History** tab in Snowsight. Check whether the query status displays `FAILED_WITH_ERROR` or indicates that the query was canceled by the user after roughly 30 seconds.
     * In **PostgreSQL** , review the server log for messages such as `canceling statement due to user request` that match the timestamp of your query.
  2. **Verify query duration** : In the database logs, note the exact duration of the query before it was canceled. If the query consistently cancels around 30 seconds (or around the timeout limit that is configured on your proxy or load balancer), an intermediate network timeout likely triggered the cancellation.
  3. **Check intermediate network infrastructure** : Identify any reverse proxies, load balancers, or VPNs in the network path between your users' browsers and the Looker (Google Cloud core) instance.



## Resolution

To resolve this issue, increase the idle and response timeout settings on all network devices that route traffic between your users' browsers and the Looker (Google Cloud core) instance. Set the timeout limit higher than the expected duration of your longest-running interactive queries.

### Increase the Application Load Balancer backend service timeout

If your Looker (Google Cloud core) instance is fronted by an external or internal Application Load Balancer, follow these steps:

  1. In the Google Cloud console, go to the **Load balancing** page:

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click **Backends** , and then click the name of the backend service that is associated with your Looker (Google Cloud core) instance.

  3. Click **Edit**.

  4. In the **Timeout** field, increase the timeout value. For example, change the default value from 30 seconds to 300 seconds (5 minutes) or higher, depending on your expected query execution times.

  5. Click **Save**.




### Increase proxy, WAF, or VPN timeouts

If your users access Looker (Google Cloud core) through a corporate forward proxy, reverse proxy (such as NGINX or Apache), WAF, or VPN gateway, follow these steps:

  1. Locate the connection, response, or idle timeout configurations in your proxy or gateway settings, such as the following examples: 
     * In **NGINX** , increase the `proxy_read_timeout` and `proxy_send_timeout` directives.
     * In **Apache** , increase the `TimeOut` or `ProxyTimeout` directives.
     * In corporate VPNs or firewall gateways, increase the TCP session idle timeout for HTTPS traffic to the Looker (Google Cloud core) domain.
  2. Allow long-lived HTTP and WebSocket connections through the proxy so that browser heartbeat signals reach Looker (Google Cloud core) without interruption.
  3. Apply the configuration changes and restart or reload the proxy service.



### Verify the resolution

After increasing the timeout settings on your load balancer or intermediate proxies, follow these steps to verify that queries complete successfully:

  1. In Looker (Google Cloud core), go to an Explore or dashboard where queries were previously canceled.
  2. Run the query that previously failed.
  3. Verify that the query executes past the previous timeout threshold (such as 30 seconds) without cancellation and displays results in the UI.
  4. Optionally, check your backend database query logs to confirm that the job completed successfully without a user cancellation status.



## Related resources

  * [Troubleshoot Looker (Google Cloud core) networking issues: 504 timeout error](https://docs.cloud.google.com/looker/docs/looker-core-networking-troubleshooting#504-upstream-request-timeout)
  * [View instance logs for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-logging)
  * [Get support for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
