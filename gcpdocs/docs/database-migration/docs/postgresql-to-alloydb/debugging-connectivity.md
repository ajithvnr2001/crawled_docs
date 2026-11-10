---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-connectivity/
title: Debugging connectivity \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T12:42:56.187950+00:00
---

# Debugging connectivity  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/scenario-overview)



Send feedback 

#  Debugging connectivity Stay organized with collections  Save and categorize content based on your preferences. 

## Debug connectivity

You've set up connectivity between your source and destination databases, but how do you know they're connected? When your communications fail between them, how can you find out what's gone wrong and where?

The most basic tools are `ping` and `traceroute`.

### Ping

`Ping` performs a basic test to determine if the destination ("remote host") is available from the source. `Ping` sends an `ICMP Echo Request` packet to a remote host, and it expects an `ICMP Echo Reply` in return. If `ping` doesn't succeed, then there's no route from the source to the destination. Success, however, doesn't mean that your packets can get through, only that in general, the remote host can be reached.

While `ping` can tell if a host is alive and responding, it's not guaranteed to be reliable. Some network providers block `ICMP` as a security precaution, which can make connectivity debugging more difficult.

### Traceroute

`Traceroute` tests the complete route network packets take from one host to another. It shows all the steps ("hops") that the packet takes along the way, and how long each step takes. If the packet doesn't go through all the way to the destination, `traceroute` doesn't complete, but ends with a series of asterisks. In this case, look for the last IP address that was successfully reached along the way. This is where connectivity broke down.

`Traceroute` can time out. It can also fail to complete if a gateway along the way isn't configured correctly to pass the packet along to the next hop.

When `traceroute` fails to complete, you might be able to figure out where it stopped. Find the last IP address listed in the `traceroute` output, and do a browser search for `who owns [IP_ADDRESS]`. Results may or may not show the owner of the address, but it's worth a try.

### mtr

The `mtr` tool is a form of `traceroute` that remains live and continuously updated, similar to how the `top` command works for local processes.

### Locate your local IP address

If you don't know the local address of your host, then run the `ip -br address show` command. On Linux, this shows the network interface, the status of the interface, the local IP, and MAC addresses. For example: `eth0 UP 10.128.0.7/32 fe80::4001:aff:fe80:7/64`.

Alternatively, you can run `ipconfig` or `ifconfig` to see the status of your network interfaces.

### Locate the outgoing IP address

If you don't know the IP address that the source and destination databases use to communicate with each other (the outgoing IP address), then complete the following steps:

  1. Go to the **Clusters** page in the Google Cloud console: 

[Go to AlloyDB for PostgreSQL Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Locate the AlloyDB for PostgreSQL cluster that's associated with the migration job that you're debugging.
  3. Both outbound public IP addresses appear in the details of the cluster's primary instance.



### Open local ports

To verify that your host is listening on the ports you think it is, run the `ss -tunlp4` command. This tells you what ports are open and listening.

For example, if you have a PostgreSQL database running, then port `5432` should be up and listening. For SSH, you should see port `22`.

### All local port activity

Use the `netstat` command to see all the local port activity. For example, `netstat -lt` shows all the currently active ports.

### Connect to the remote host using telnet

To verify that you can connect to the remote host using `TCP`, run the `telnet` command. Telnet attempts to connect to the IP address and port you give it.

If your remote host is running a PostgreSQL database, for example, then you should be able to telnet to it on port `5432`: `telnet 35.193.198.159 5432`.

On success, you see the following: 
    
    
    Trying 35.193.198.159...
    Connected to 35.193.198.159.
    

On failure, you see `telnet` stops responding until you force-close the attempt: 
    
    
    Trying 35.193.198.159...
    ^C
    

### Client authentication

Client authentication is controlled by a configuration file, which is named `pg_hba.conf` (HBA stands for host-based authentication).

Make sure the replication connections section of the `pg_hba.conf` file on the source database is updated to accept connections from the AlloyDB for PostgreSQL VPC's IP address range.

### Cloud Logging

Database Migration Service and AlloyDB for PostgreSQL use Cloud Logging. See the [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs) for complete information.

#### View logs

You can view logs for AlloyDB for PostgreSQL instances and other Google Cloud projects such as Cloud VPN or Compute Engine instances. To view logs for your AlloyDB for PostgreSQL instance log entries:

### Console

  1. [Go to the Logs Explorer](https://console.cloud.google.com/logs/query)
  2. Select your AlloyDB for PostgreSQL project at the top of the page.
  3. In the Query builder, add the following: 
     * Resource: Select **AlloyDB for PostgreSQL Instance**. In the dialog, select your AlloyDB for PostgreSQL instance.
     * Log names: Scroll to the AlloyDB for PostgreSQL section and select appropriate log files for your instance. For example: 
       * `alloydb.googleapis.com/postgres.log`
     * Severity: Select a log level.
     * Time range: Select a preset or create a custom range.



### gcloud

Use the [`gcloud logging`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command to view log entries. In the example below, replace `PROJECT_ID`. The [`limit`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--limit) flag is an optional parameter that indicates the maximum number of entries to return.
    
    
    gcloud logging read "projects/PROJECT_ID/logs/alloydb.googleapis.com%2Fpostgres.log" --limit=10

### Private IP addresses

Connections to an AlloyDB for PostgreSQL cluster using a private IP address are authorized for [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). If your network uses non-RFC 1918 address ranges, you need to update the network peering to export any Non-RFC 1918 routes. For example: `gcloud compute networks peerings update servicenetworking-googleapis-com --network=NETWORK --export-subnet-routes-with-public-ip --project=PROJECT`

The IP range 172.17.0.0/16 is reserved for the Docker bridge network. Connections from any IP address within that range to AlloyDB for PostgreSQL clusters using a private IP address will fail.

### VPN troubleshooting

See the [Google Cloud Cloud VPN troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#common_problems_and_solutions) page.

## Troubleshoot TCP proxy errors

The way the TCP proxy is set up might also incur errors. To troubleshoot a TCP proxy error, see the following examples of issues and how they can be solved:

### Failure starting the virtual machine (VM)

You see the following message when starting the VM instance in Compute Engine:

`You do not currently have an active account selected.`

**Things to try**

Run one of the following commands to configure an active account:

  * To obtain new credentials, run the following command:
        
        gcloud auth login
        

  * To select an already authenticated account, run the following command:
        
        gcloud config set account <var>ACCOUNT</var>
        

Replace ACCOUNT with the name of the account that you want to configure.




### Failure connecting to the source database instance

You see the following error message when testing the migration job:

`Failure connecting to the source database. Make sure the connectivity information on the connection profile is correct and the source database is reachable.`

**Things to try**

Iterate through the following steps to understand where the issue might be:

  1. Check if the VM hosting the TCP proxy container is running: 
     1. In the Google Cloud console, go to the Compute Engine **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Search for the VM that was created as part of the proxy setup process. If it's not listed or it's not running, [configure your TCP proxy](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-tcp-proxy-via-cloud-hosted-vm) from scratch, and update the [source connection profile settings](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/manage-connection-profiles) in the migration job with the correct IP address. 
  2. If the VM is running, verify that there was no error when downloading the TCP proxy container image: 
     1. Select the VM that was created as part of the TCP proxy setup process. Under **Logs** , click **Serial port 1 (console)**.
     2. If you can't see the `Launching user container 'gcr.io/dms-images/tcp-proxy'` entry in the logs, the problem might be that your instance couldn't pull the image from [Container Registry](https://docs.cloud.google.com/container-registry/docs/overview). To verify if this is the case, connect to the VM, and manually try to pull the image from Container Registry using the following command: 
            
            docker pull gcr.io/dms-images/tcp-proxy

If you see the following error: `Error response from daemon: Get "https://gcr.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)`, it means that your VM couldn't connect to Container Registry. If your VM has only a private IP address, you must [enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) on the subnet that the IP address is part of; otherwise, the VM won't have access to [Google Enterprise APIs](https://docs.cloud.google.com/apis/docs/resources/enterprise-apis), such as Container Registry.

  3. Verify that the container can connect to the source instance: 
     1. Select the VM that was created as part of the proxy setup process. Under **Logs** , click **Cloud Logging**.
     2. If you see the following message: `Connection refused, please verify that the machine you are using to run the script can connect to the source database at`, it means that the TCP proxy container couldn't connect to the source database instance. There can be several reasons for this to happen: 
        * The IP address of the source instance is incorrect.
        * There is a firewall policy that refuses connections from the TCP proxy to the source instance.
        * The source instance is in a different Virtual Private Cloud (VPC) network than the VM hosting the TCP proxy.

You can debug the connectivity issue using Google Cloud's [Connectivity Testss](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to make sure that there's connectivity between the VM hosting the TCP proxy and the source database:

     1. In the Google Cloud console, go to the **Connectivity Testss** page. 

[Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests)

     2. Click **Create Connectivity Tests**.
     3. Enter a name for the test.
     4. Select **TCP** as the protocol.
     5. Select **IP address** from the **Source endpoint** list. Enter the public IP address of the newly created TCP proxy if the source database is accessible using a public IP address; otherwise, enter the private IP address of the TCP proxy.
     6. Select **IP address** from the **Destination endpoint** list, and enter the IP address of the source database.
     7. Enter the port number used to connect to the source database in the **Destination port** field.
     8. Click **Create**.

Run the connectivity test and address any connectivity issues that arise. After you fix the connectivity issue, verify that the TCP proxy can connect to the source instance:

     1. Go to **VM instances** in **Compute Engine**. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Select the VM that was created as part of the proxy setup process. Under **Logs** , click **Cloud Logging**.
     3. If you see the `Connection to source DB verified` log entry, it means that the TCP proxy can now connect to the source instance.
  4. Verify that the migration test is not failing with connection issues.



### Failure connecting to the destination database cluster

If the TCP proxy container can connect to the source instance, but the migration test is still failing because of connection issues, the issue might be the connectivity between the destination AlloyDB for PostgreSQL cluster and the VM hosting the TCP proxy container.

**Debug the issue**

To debug the issue, you can use Google Cloud [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to make sure that there's connectivity between the destination AlloyDB for PostgreSQL cluster and the VM hosting the TCP proxy:

  1. In the Google Cloud console, go to the **Connectivity Testss** page. 

[Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests)

  2. Click **Create Connectivity Tests**.
  3. Set the following parameters for your test: 
     1. Enter a name for the test.
     2. Select **TCP** as the protocol.
     3. Select **IP address** from the **Source endpoint** list, and enter the IP address of the newly created AlloyDB for PostgreSQL cluster.
     4. Select **IP address** from the **Destination endpoint** list, and enter the private IP address of the TCP proxy.
     5. Enter `5432` in the **Destination port** field.
  4. Click **Create**.
  5. Run the connectivity test and address any connectivity issues that arise.



**Possible causes**

There is a firewall rule that denies communication between the destination cluster and the TCP proxy VM.

**Things to try**

Add a firewall rule that allows the destination cluster to communicate with the TCP proxy using port `5432`.

**Possible causes**

There is a VPC mismatch between the destination cluster and the VM running the TCP proxy container.

**Things to try**

Select the same VPC for the destination cluster.

## Troubleshooting reverse SSH tunnel issues

SSH tunneling is a method to forward some communication on top of an SSH connection. Reverse SSH tunneling allows setting up an SSH tunnel, while maintaining that the destination network is the one that initiates the tunnel connection. This is useful when you don't want to open a port in your own network for security purposes.

What you're trying to achieve is to set up the following:

AlloyDB for PostgreSQL cluster \---> Compute Engine VM bastion \---> **tunnel** \---> source network bastion \---> source DB

**Note:** Although Database Migration Service migrates data from a source to a destination, you should enable connectivity from the destination to the source.

It's assumed that:

  * The AlloyDB for PostgreSQL cluster can access the Compute Engine VM bastion (this is achieved by peering the AlloyDB for PostgreSQL network to the Compute Engine VM network).

  * The source network bastion can access the source DB.




You then set up an SSH tunnel from the source network bastion to the Compute Engine VM bastion, which routes any incoming connections to some port on the Compute Engine VM bastion through the tunnel to the source DB.

Each link in the above scenario can be set up improperly and prevent the entire flow from working. Troubleshoot each link, one by one:

### source network bastion \---> source DB

  1. Connect to the source network bastion using SSH, or from the terminal if it's the local machine.
  2. Test connectivity to the source DB using one of the following methods: 
     * `telnet [source_db_host_or_ip] [source_db_port]` \- expect to see the telnet connection strings, ending with `Connected to x.x.x.x`.
     * `psql -h [source_db_host_or_ip] -p [source_db_port] -U [username] -d [database_name]` \- expect to see a password prompt or access denied.



If this fails, then you need to verify that you enabled access from this bastion to the source DB.

### Compute Engine VM bastion \---> source DB

  1. SSH to the Compute Engine VM bastion (using `gcloud compute ssh VM_INSTANCE_NAME`).
  2. Test connectivity to the source DB using one of the following methods: 
     * `telnet 127.0.0.1 [tunnel_port]` \- expect to see the telnet connection strings, ending with `Connected to x.x.x.x`.
     * `psql -h 127.0.0.1 -p [tunnel_port] -U [username] -d [database_name]` \- expect to see a password prompt or access denied.



If this fails, then you need to verify that the tunnel is up and running properly. Running `sudo netstat -tupln` shows all listening processes on this VM, and you should see `sshd listening on the tunnel_port`.

### AlloyDB for PostgreSQL cluster \---> source DB

This is best tested by [`testing the migration job`](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions#test) from Database Migration Service. If this fails, then it means there's some issue with VPC peering or routing between the AlloyDB for PostgreSQL network and the Compute Engine VM bastion network.

The source database server's firewall must be configured to allow the entire **internal IP range** allocated for the **private service connection** of the VPC network that the AlloyDB for PostgreSQL destination cluster uses.

To find the **internal IP range** in the console:

  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console. 
  2. Select the VPC network that you want to use.
  3. Select **Private services access** > **Allocated IP ranges for services**.
  4. Find the **Internal IP range** associated with the connection created by **servicenetworking-googleapis-com**.



You can also view the traffic between the AlloyDB for PostgreSQL cluster and the Compute Engine VM instance in the [Cloud Logging](https://console.cloud.google.com/logs) console in the `Cloud VPN gateway` project. In the Compute Engine VM logs, look for traffic coming from the AlloyDB for PostgreSQL cluster. In the AlloyDB for PostgreSQL cluster's logs, look for traffic from the Compute Engine VM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
