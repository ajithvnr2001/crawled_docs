---
url: https://docs.cloud.google.com/looker/docs/admin-panel-database-connections/
title: Admin settings - Connections \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:48:06.219825+00:00
---

# Admin settings - Connections  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-database-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Connections Stay organized with collections  Save and categorize content based on your preferences. 

To access the **Connections** page, open the **Admin** menu and, under **Database** , choose **Connections**.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Viewing connections

On the **Connections** page, you can view your database connections and the IP addresses that are needed to allow network traffic. If the ability to create a new database has been enabled for your instance, you can also add a new connection.

### Databases tab

The **Databases** tab shows basic information about the database connections that you've defined. It also shows any Looker-managed connections that you've created, if the ability to create a new database has been enabled for your instance. You can also test the status of and edit the configuration of those connections from the **Databases** tab.

You can click **Public IP Addresses** to view the list of IP addresses that are needed to allow network traffic from your Looker instance. All network traffic from Looker will come from one of the listed IP addresses, based on the region where your Looker instance is hosted. Prohibiting traffic to your database, except from these and other trusted IP addresses, is a way to limit data access.

**Note:** The **Public IP Addresses** button is not available for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances. If you are using a Looker (Google Cloud core) instance that is set up for public secure connections or for hybrid connections, use the IP address listed in the **Egress Public IP** field on the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the **Instances** page in the Google Cloud console.

If you have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), you can click the **Test Reachability** button at the top of the Looker **Connections** page to check whether Looker can reach a hostname and port over the network. For more information, see Network reachability diagnostics.

The following table describes the elements on the **Databases** tab:

Column | Description  
---|---  
Name | The name of the connection, chosen by you, that is used in the [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) LookML parameter. When you test the connection, Looker displays the list of status checks under the connection name.  
Database | The name of the database that Looker will query when using this connection.  
Scope | Whether the connection can be used with all projects or only one specific project.  
SSH Server | The name of the SSH server configuration used to create an SSH tunnel to your database. This column shows only if the **SSH Servers** tab is enabled on your Looker instance.  
SSL | Whether or not you are using SSL encryption to protect the data traveling between Looker and your database (there are [other secure options](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) besides SSL).  
Type | The SQL dialect of the database connection.  
Actions | Actions that you can take for a connection: test a connection, edit a connection, view other information about a connection, jump to a list of links to the connection's Explores, or delete a connection. If the ability to create a new database has been enabled for your instance, you can also [add data from an additional data source](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#connecting_to_a_data_source) to any Looker-managed connections.  
  
### SSH Servers tab

> The **SSH Servers** tab isn't available for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances.
> 
> The **SSH Server** option is available if a Looker (original) instance is deployed on Kubernetes infrastructure, and only if the ability to add SSH server configuration information to your Looker instance has been enabled. If this option is not enabled on your Looker instance and you would like to enable it, [contact a Google Cloud sales specialist](https://cloud.google.com/contact) or [open a support request](http://console.cloud.google.com/support/cases).
> 
> Looker automatically chooses the localhost port for you when creating SSH tunnels; you cannot specify the localhost port.
> 
> SSH connections to PrestoDB or Trino databases may require additional database configuration. When SSL is enabled, the PrestoDB or Trino database defaults to listening on port 443. To establish the SSH tunnel, Looker must set the localhost port to 443, which is already in use by Looker. This will cause the SSH tunnel setup to fail. To correct the issue, configure your PrestoDB or Trino database to listen on a port other than port 443 when SSL is enabled.

The **SSH Servers** tab lists the SSH server configurations that you have added, indicates the status of connections to the SSH servers, and lists the [database connections](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#adding-connections) using each SSH server. From the **SSH Servers** tab, you can also test a connection to an SSH server, and add or edit SSH server configurations.

The following table describes the elements on the **SSH Servers** tab:

Column | Description  
---|---  
Server Name | The name of the SSH server configuration, chosen by you, that is used to connect to your database.  
Connections | A list of the database connections that connect to the SSH server. Clicking a database connection opens the **Edit Connection** page for that database connection.  
Three-dot **Options** menu more_vert | Actions that you can take for an SSH server configuration: test connections to an SSH server, [add a database connection to an SSH server](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#enable-ssh-server), edit an SSH server configuration, or delete an SSH server configuration.  
  
#### Adding or editing an SSH server configuration

To add a new SSH server configuration:

  1. In the **SSH Server** tab, click **Add Server**
  2. In the **Unnamed Server** field in the top right corner, enter a name for the SSH server configuration.
  3. Click **Download Key** to download the public key to a text file. Be sure to save this file for later use.
  4. In the **Server Username** field, enter the username that Looker will use to connect to the SSH server.
  5. In the **Server IP Address or Hostname** field, enter the SSH server IP address or hostname.
  6. In the **Server Port** field, enter the port number used to connect to the SSH server.
  7. Add the downloaded public key to the authorized key file on your SSH server. See the [Using an SSH server](https://docs.cloud.google.com/looker/docs/using-an-ssh-tunnel#step_4:_prepare_the_tunnel_host) documentation page for more information and an example.
  8. Ensure that the appropriate [Looker IP addresses are added to the allowlist](https://docs.cloud.google.com/looker/docs/using-an-ssh-tunnel#step_2:_create_ip_allowlist) on your SSH server so that Looker can connect to the SSH server.
  9. Click **Test & Request Fingerprint** to verify your connection to the SSH server.
  10. View the new SSH configuration. On this screen, you can also download or view the public key and view the unique fingerprint of the SSH server configuration.



To edit an existing SSH server configuration, click the three-dot **Options** menu in the row of the selected SSH server, and choose **Server Details**.

#### Testing the connections to an SSH server

To test all database connections to an SSH server:

  1. Click the three-dot **Options** menu in the row of the chosen SSH server.
  2. Choose **Test Connections**.



Looker will test all database connections using that SSH server and display a green checkmark next to the server name and all connections where the connection test passes. A red exclamation point icon indicates that the connection failed the test.

**Note:** If you make changes to your SSH server's `sshd_config` file, before testing the connection you'll need to restart the sshd daemon on your SSH server for the changes to take effect.

#### Adding a database connection to an SSH server

To add a new database connection using an SSH server:

  1. Click the three-dot **Options** menu in the row of the chosen SSH server.
  2. Choose **Add Connection**.



Looker displays the [**Connection Settings**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) page, with the SSH server listed in the **SSH Server** field.

#### Deleting an SSH server configuration

To delete an SSH server configuration:

  1. Click the three-dot **Options** menu in the row of the SSH server to delete.
  2. Choose **Delete Server**.



## Testing connections

Looker lets you test your existing connections to make sure they are functioning properly. You can also test connections as you add them, as described on the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page.

Each connection test includes a list of status checks to tell you whether Looker can successfully use the database connection.

Potential issues are shown in yellow; errors are shown in red. If a connection "passes", it appears in green.

**Note:** Database connections that use OAuth, such as [Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake#oauth) and [Google BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#oauth_for_bigquery_connections), require a user login. If you are not logged in to your OAuth user account when you test one of these connections, Looker will show a warning with a **Log In** link. Click the link to enter your OAuth credentials or to allow Looker access to your OAuth account information.

You can check the status of:

  * A single connection by clicking **Test** to the far right of that connection
  * All connections by clicking the **Test All Connections** button at the top of the page



Two checks are common cause for confusion:

  * Can find temp schema
  * Can use persistent derived tables



These checks don't need to pass for Looker to function. However, you do need them to pass to use [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables), which are a very valuable modeling feature.

## Network diagnostics

Looker provides two tools that help you find out whether a connection problem is caused by the network, such as a firewall rule or a missing route, or by the database, such as incorrect credentials:

  * Network diagnostics in connection test results: When a connection test can't connect to the database, Looker adds network diagnostics to the error message.
  * Network reachability diagnostics: If you have the Looker [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), you can use the **Test Reachability** button at the top of the Looker **Connections** page to check whether Looker can reach any hostname and port.



Both tools look up the hostname in DNS and then try to open a TCP connection to each IP address that the lookup returns. Because they use TCP connections instead of ICMP ping requests, a host that blocks ping requests can still show as reachable.

### Network diagnostics in connection test results

When a connection test can't connect to the database, Looker tests the following endpoints and adds the results to the end of the error message, under `Network Diagnostics:`:

  * For all connections, the host and port that are configured for the connection.
  * For Amazon Athena connections, the AWS Glue endpoint for the connection's AWS Region, on port 443, such as `glue.us-east-1.amazonaws.com`.
  * For Cloud SQL connections whose **Host** field contains an instance connection name, such as `my-project:us-central1:my-instance`, the `sqladmin.googleapis.com` endpoint on port 443. The Cloud SQL connector uses this endpoint to get instance information and certificates.



Looker tests up to three IP addresses for each endpoint, and the diagnostics take at most 3 seconds. Looker doesn't run network diagnostics for connections that use an [SSH tunnel](https://docs.cloud.google.com/looker/docs/using-an-ssh-tunnel).

For example, the following diagnostics show that Looker can reach the Athena endpoint, but connections to the AWS Glue endpoint time out:
    
    
    Network Diagnostics:
    - athena.eu-central-1.amazonaws.com (Port: 443):
      - 203.0.113.10 - success
    - glue.eu-central-1.amazonaws.com (Port: 443):
      - 203.0.113.20 - timeout (3000ms)
      - 203.0.113.21 - timeout (3000ms)
    

Each IP address shows one of the following results:

  * `success`: Looker opened a TCP connection to the IP address and port. If every IP address shows `success` but the test still fails, check the connection settings, such as the credentials, SSL settings, and database user permissions.
  * `timeout (3000ms)`: Looker got no response within 3 seconds. This result often means that a firewall rule, security group, or missing network route drops the traffic.
  * `failed:` followed by a reason: the connection was rejected, or the network was unreachable. For example, `Connection refused` means that nothing is listening on the port, or that a firewall rejected the connection.
  * `blocked (sensitive IP)`: Looker didn't test the IP address because it's in a restricted range.



If the DNS lookup fails, the endpoint shows `DNS resolution failed:` followed by the reason. Check the hostname for typos. If the database uses a private hostname, make sure that Looker can resolve it.

### Network reachability diagnostics

If you have the Looker [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), you can test a database host before you add a connection, or test an endpoint that a connection depends on, such as `sqladmin.googleapis.com` on port `443`.

To test network reachability, follow these steps:

  1. On the **Connections** page, click the **Test Reachability** button at the top of the page.
  2. In the **Network Reachability Diagnostics** dialog, in the **Hostname or Domain** field, enter a hostname or an IP address.
  3. In the **Port** field, enter the port to test. The default is `443`.
  4. Click **Test**.



Looker tests up to five IP addresses for the hostname, and the test takes at most 3 seconds. Here is an example Network Reachability Diagnostics dialog showing test results for a hostname and port:

![The Network Reachability Diagnostics dialog showing test results for a hostname and port.](https://docs.cloud.google.com/static/looker/docs/images/admin-connections-test-reachability-2620.png)

For each IP address, the dialog shows a message, how long the connection took in milliseconds if it succeeded, and one of the following statuses:

  * **Connected** : Looker opened a TCP connection to the IP address and port.
  * **Timed Out** : Looker got no response within 3 seconds.
  * **Failed** : the connection was rejected, or the network was unreachable. The message shows the reason.
  * **SSRF Blocked** : Looker didn't test the IP address because it's in a restricted range. These restrictions protect against server-side request forgery (SSRF).



If Looker can't resolve the hostname, or if the port is restricted, the dialog shows an error message instead of results.

### Restricted addresses and ports

To protect your instance, Looker network diagnostics doesn't test IP addresses in the following ranges:

  * Loopback, link-local, multicast, and other restricted address ranges, including the metadata server address `169.254.169.254`.
  * Private address ranges (`10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`), on Looker (Google Cloud core) instances that use only [public secure connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#public_ip_connections).



In addition, the **Test Reachability** function doesn't test some ports that are restricted for security reasons, such as port 22. If you enter one of these ports, the dialog shows a message such as `Port 22 is restricted from diagnostic probing for security reasons`.

## Adding connections

To add a new database connection, follow the steps described on the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page.

## Editing connections

To edit an existing connection, open the **Connections** page by selecting the **Admin** menu, and then, under **Database** , choose **Connections**. Click the **Edit** button for the connection. The same page that you use to create a connection will appear (described on the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#adding-connections) documentation page), but with the relevant information already filled out. Make any needed changes, and then click **Update Connection**.

## Actions available for all connections

All connections offer these options from the gear drop-down menu to the far right of each connection:

Option | Description  
---|---  
SQL Runner | This option brings you to Looker's SQL Runner, with the proper connection and schema already selected.  
Explore | This option brings you to a list of basic, automatically-generated Explore options for your connection. These are not based on your customized data models, but they enable some quick reporting on the raw data in your connection's tables. This is typically only useful for getting an idea of table contents before modeling, rather than for the purposes of actual data analysis.  
Delete | To delete an existing connection, click the gear drop-down menu to the far right of a connection and select **Delete**. You'll be given the opportunity to confirm the deletion but, once you do so, it cannot be undone. Accidentally deleting a connection will disable any queries that use it and can cause LookML validation errors for developers. However, if you re-create a new connection with the same name, functionality will be restored.  
  
## Actions available for some connections

Depending on the connection dialect, the gear drop-down menu to the right of the connection may offer the following additional options:

Option | Description  
---|---  
Show Tables | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the metadata of your connection. Although this option begins with the schema name, table name, and column count selected, you can manipulate it like any other Looker Explore.  
Show Databases | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the metadata of your connection. Although this option begins with the schema name, catalog name, table count, and column count selected, you can manipulate it like any other Looker Explore.  
Show Processes | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the processes running on this connection, the state they are in, how long they have been running, and other info. This can be useful in helping determine the cause if Looker is running slow, or if a query is not running at all.  
Show PDT Event Log | This option brings you to a Looker Explore page that lets you create Looker Explore queries based on the derived table activity for this connection. The available fields are described in more detail on our [Persistent derived tables](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#event_log) documentation page.  
  
## Safely deleting a database connection

Deleting a database connection that is still referenced by LookML models causes validation errors that can prevent developers from committing or merging branches. To safely delete a connection, follow these steps:

  1. **Identify dependencies** : In Development Mode, use [Project Search](https://docs.cloud.google.com/looker/docs/looker-ide#finding_and_replacing_text_in_your_project) for `connection: CONNECTION_NAME` to find all LookML model files that reference the connection.
  2. **Remove dependencies** : Update the `connection` parameter in those model files to point to a valid connection, or delete the dependent models if they are no longer needed.
  3. **Validate content** : Run the [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) to identify and fix any Looks or dashboards that relied on the models using the connection.
  4. **Deploy changes** : Commit and [deploy](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production) these LookML changes to the production branch.
  5. **Delete the connection** : Once all references are removed from the production branch, navigate to **Admin** > **Database** > **Connections** and delete the connection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
