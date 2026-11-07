---
url: https://docs.cloud.google.com/compute/docs/gpus/gpu-multi-host-nic/
title: Patterns for using multiple host NICs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:32:26.928813+00:00
---

# Patterns for using multiple host NICs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/gpu-multi-host-nic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Patterns for using multiple host NICs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes configuration patterns and best practices for using the two host LAN network interfaces (NICs) for storage and management on Compute Engine instances.

## Overview

Some accelerator-optimized machine series—including A5X, A4X Max, A4X, A4, and A3 Ultra—have two host LAN network interfaces for storage and management that attach to regular Virtual Private Cloud (VPC) networks. These machines also have `MRDMA` network interfaces that must attach to a Remote Direct Memory Access over Converged Ethernet (RoCE) VPC network.

This document focuses on configuring the host LAN interfaces (`gVNIC` or `IDPF`) on regular VPC networks, not RDMA network interfaces. The host LAN interfaces are [Titanium](https://cloud.google.com/titanium) infrastructure processing units (IPUs) that connect to separate CPU sockets and non-uniform memory access (NUMA) nodes. Inside the compute instance, these IPUs appear as [Google Virtual NICs (gVNICs) or Infrastructure Data Path Function (IDPF) network interfaces](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#review-network-nic). These interfaces provide network bandwidth for storage and management activities, such as checkpointing, loading training data, and loading models. The machine's NUMA topology, including the topology of the network interfaces, is visible to the guest operating system (OS).

Use the following configurations regardless of which pattern you choose for multiple host NICs:

  * **Network settings:** [Configure each gVNIC or IDPF interface to use a separate VPC network](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts). For your VPC setup, complete the following configurations: 
    * Configure a large [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) for each VPC network, such as `8896` (the maximum supported MTU).
    * If dropped incoming data packets on the receiver side slow down ingress performance for your workload, then check for dropped packets by using the `ethtool` utility. To optimize data allocation from the page cache so that each incoming layer 2 frame fits within two 4 KB buffers, adjust the TCP maximum segment size (MSS), the interface MTU, or the VPC MTU.
  * **Application settings:**
    * NUMA-align your application by using CPU cores, memory allocations, and a network interface from the same NUMA node. If you're running a dedicated instance of the application for a specific NUMA node or network interface, then bind the application's CPU and memory resources to that NUMA node by using a tool such as `numactl`.
  * **Operating system settings:**
    * Enable TCP segmentation offload (TSO) and large receive offload (LRO).
    * For each gVNIC or IDPF interface, configure symmetric multiprocessing (SMP) affinity to route interrupt requests (IRQs) to the same NUMA node as the interface and spread interrupts across CPU cores. If you use a Google-provided Linux image, the Compute Engine guest agent runs the `google_set_multiqueue` script at boot to apply this configuration automatically. If you use a custom image, [install the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment). If the script doesn't run automatically, run the `sudo /usr/bin/google_set_multiqueue` command.
    * Evaluate [Receive Flow Steering (RFS), Receive Packet Steering (RPS), and Transmit Packet Steering (XPS)](https://www.kernel.org/doc/Documentation/networking/scaling.txt) settings to determine whether they benefit your workload.
    * For A4X Max and A4X instances, NVIDIA recommends that you [disable automatic NUMA scheduling](https://docs.nvidia.com/grace-perf-tuning-guide/os-settings.html#automatic-numa-scheduling-and-balancing).
    * Don't use Linux kernel bonding with the gVNIC or IDPF interfaces on these machines, because kernel bonding isn't supported.



## Patterns for using multiple host NICs

The following table outlines general patterns for using multiple host NICs on Google Cloud:

General patterns for using multiple host NICs Pattern | Supported process layout | Deployment path: Compute Engine | Deployment path: Google Kubernetes Engine | Deployment path: Slurm | Notes  
---|---|---|---|---|---  
Change an application to use a specific interface | Process shard per interface | Yes | Yes | Yes | Requires code changes to the application.  
Change an application to use both interfaces | Dual-interface process | Yes | Yes | Yes | Requires code changes to the application.  
Use a dedicated network namespace for specific applications | Process shard per interface | Yes | Yes (privileged containers only) | No | None  
Map an entire container's traffic to a single interface | All container traffic mapped to one interface | Yes | Yes | No | None  
Use VPC peering and let the system load-balance sessions across interfaces | Dual-interface process | Yes | Yes | Yes | Challenging or impossible to NUMA-align. Requires Linux kernel 6.16 or later.  
Shard traffic across networks | 

  * Dual-interface process
  * Process shard per interface

| Yes | Yes | Yes | Might require code changes to NUMA-align if you're running a dual-interface process.  
Use source network address translation (SNAT) to choose the source interface | 

  * Dual-interface process
  * Process shard per interface

| Yes | Yes (setup requires administrator privileges) | Yes (setup requires administrator privileges) | Can be challenging to configure.  
  
### Notes

  * **For theUse VPC peering and let the system load-balance sessions across interfaces and Shard traffic across networks patterns:** These options aren't generally recommended, but they might be useful for limited workloads on x86 (A4 and A3 Ultra) platforms.



## Change an application to use a specific interface

**Requirements:**

  * Requires code changes to your application.
  * Requires permissions for one or more of the following methods: 
    * `bind()`: requires special permissions only if you use a privileged source port.
    * `SO_BINDTODEVICE`: requires the `CAP_NET_RAW` permission.
  * Might require you to modify your kernel routing table to establish routes and prevent asymmetric routing.



### High-level overview

**Note:** Some applications and libraries already support multi-NUMA or multi-socket topologies with multiple network interfaces. If you're using third-party or open source software, then check the documentation for that software.

To configure your application to use a specific network interface, complete the following steps:

  1. Add binding for a network interface to your application's source code by using one of the following options: 
     * Use the `bind()` system call to bind a socket to a specific source IP address.
     * Use the `SO_BINDTODEVICE` socket option to bind a socket to a specific network interface.
  2. Modify the kernel routing table as needed to make sure that a route exists from the source network interface to the destination address. To prevent asymmetric routing, configure policy routing as described in [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).
  3. Optional: Run your application on the memory and CPUs that share the same NUMA node as your chosen network interface by using the `numactl` command.



After you complete these steps, your application uses the specified network interface.

## Change an application to use both interfaces

**Requirements:**

  * Requires code changes to your application.
  * Requires permissions for one or more of the following methods: 
    * `bind()`: requires special permissions only if you use a privileged source port.
    * `SO_BINDTODEVICE`: requires the `CAP_NET_RAW` permission.
  * Might require you to modify your kernel routing table to establish routes and prevent asymmetric routing.



### High-level overview

**Note:** Some applications and libraries already support multi-NUMA or multi-socket topologies with multiple network interfaces. If you're using third-party or open source software, then check the documentation for that software.

To configure your application to use both network interfaces, complete the following steps:

  1. Add a binding for each network interface to your application's source code by using one of the following options: 
     * Use the `bind()` system call to bind each socket to the source IP address of the corresponding network interface.
     * Use the `SO_BINDTODEVICE` socket option to bind each socket to a specific network interface.
  2. If your application acts as a client, create a separate client socket for each source network interface.
  3. Modify the kernel routing table as needed to make sure that a route exists from each source network interface to the destination address. To prevent asymmetric routing, configure policy routing as described in [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).
  4. Partition network activity into threads that run on the same NUMA node as the corresponding gVNIC or IDPF interface—for example, by calling `pthread_setaffinity_np`. Because the application uses resources across multiple NUMA nodes, avoid using `numactl`, or make sure that your `numactl` command includes the NUMA nodes of all network interfaces that your application uses.



## Use a dedicated network namespace for specific applications

**Requirements:**

  * Requires the `CAP_SYS_ADMIN` capability.
  * Isn't compatible with GKE Autopilot.
  * If you're using GKE, then you must use a privileged container.



This section describes patterns that you can use to create a network namespace for a secondary network interface. The best pattern for your workload depends on your scenario. Approaches that use a virtual switch or IPvlan work best when multiple applications need to share the secondary interface from different network namespaces.

### Move the secondary interface into a dedicated network namespace

With this pattern, you create a network namespace, move the secondary gVNIC or IDPF interface into the new namespace, and then run the application from that namespace. This pattern is simpler to set up and tune compared to a virtual switch, but applications outside of the new network namespace can't access the secondary network interface.

To move the `eth1` interface into a network namespace named `app-net` and run a command in that namespace, run the following commands:
    
    
    ip netns add app-net
    ip link set eth1 netns app-net
    ip netns exec app-net ip addr add ETH1_IP/PREFIX dev eth1
    ip netns exec app-net ip link set dev eth1 up
    ip netns exec app-net ip route add default via GATEWAY_IP dev eth1
    ip netns exec app-net COMMAND
    

Replace the following:

  * `ETH1_IP`: the internal IP address of the `eth1` interface.
  * `PREFIX`: the subnet prefix length for the `eth1` interface.
  * `GATEWAY_IP`: the default gateway IP address for the `eth1` subnet.
  * `COMMAND`: the command to run inside the `app-net` network namespace.



When you run these commands, `COMMAND` runs inside the `app-net` network namespace and uses the `eth1` interface.

Applications running inside the new network namespace use the secondary gVNIC or IDPF interface. You can also use the `numactl` command to run your application by using the memory and CPUs on the same NUMA node as your chosen network interface.

### Use a virtual switch and network namespace for a secondary interface

With this pattern, you configure a virtual switch to access the secondary gVNIC or IDPF interface from a network namespace:

  1. Open an SSH connection to the compute instance. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).
  2. Create a [Virtual Ethernet (`veth`)](https://man7.org/linux/man-pages/man4/veth.4.html) device pair by using the `ip link add` command—for example, `ip link add veth0 type veth peer name veth1`.
  3. Adjust the MTU on each device to match the MTU of the secondary interface by using the `ip link set` command:
         
         ip link set dev veth0 mtu MTU
         ip link set dev veth1 mtu MTU
         

Replace `MTU` with the MTU of the secondary interface—for example, `8896`.

  4. Enable IPv4 packet forwarding:
         
         sysctl -w net.ipv4.ip_forward=1
         

  5. Move one end of the `veth` pair into a new network namespace, and leave the other end in the root namespace.

  6. Map traffic from the `veth` device to the secondary interface. To configure this mapping, [create an alias IP range for the compute instance's secondary interface](https://docs.cloud.google.com/vpc/docs/alias-ip) and assign an IP address from this range to the child interface in the namespace.

  7. Run the application from the new network namespace. You can use the `numactl` command to run your application by using the memory and CPUs on the same NUMA node as the chosen network interface.




Alternatively, depending on your guest OS and workload setup, you can link an [IPvlan](https://www.kernel.org/doc/Documentation/networking/ipvlan.txt) interface to the secondary gVNIC or IDPF interface instead of creating `veth` devices.

## Map an entire container's traffic to a single interface

**Requirements:**

  * Your application must run inside a container that uses a network namespace for container networking, such as GKE, Docker, or Podman. You can't use the host network.



Container runtimes such as GKE, Docker, and Podman use a dedicated network namespace for each container to isolate its traffic. You can modify this network namespace—either directly or by using the container runtime's tools—to map traffic to a different network interface.

GKE requires the primary interface for internal Kubernetes communication. However, you can change the default route in the Pod to use the secondary interface, as shown in the following GKE Pod manifest:
    
    
    metadata:
      # ...
      annotations:
        networking.gke.io/default-interface: 'eth1'
        networking.gke.io/interfaces: |
          [
            {"interfaceName":"eth0","network":"default"},
            {"interfaceName":"eth1","network":"secondary-network"}
          ]
    

This approach doesn't guarantee NUMA alignment between the default network interface and the assigned CPUs or memory.

## Use VPC peering and let the system load-balance sessions across interfaces

**Requirements:**

  * You must establish VPC Network Peering between the VPC networks of the primary and secondary host NICs.
  * You must use Linux kernel version 6.16 or later to load-balance TCP sessions across source interfaces when sending traffic to a single destination IP address and port.
  * Your workload must tolerate cross-socket memory transfers without missing its performance targets.



### High-level overview

If you can't easily shard network connections within an application or across application instances, and your workload runs on A4 or A3 Ultra compute instances that aren't sensitive to cross-NUMA or cross-socket transfers, then you can treat the two interfaces as fungible.

To configure this behavior, enable the `fib_multipath_hash_policy` sysctl parameter and add a multipath route:
    
    
    PRIMARY_GW=192.168.1.1  # Gateway of nic0
    SECONDARY_GW=192.168.2.1  # Gateway of nic1
    PRIMARY_IP=192.168.1.15  # Internal IP address for nic0
    SECONDARY_IP=192.168.2.27  # Internal IP address for nic1
    
    # Enable L4 5-tuple equal-cost multipath (ECMP) hashing
    sysctl -w net.ipv4.fib_multipath_hash_policy=1
    ip route add DESTINATION_NETWORK/SUBNET_MASK \
        nexthop via ${PRIMARY_GW} \
        nexthop via ${SECONDARY_GW}
    

Replace the following:

  * `DESTINATION_NETWORK`: the destination internal IP address range.
  * `SUBNET_MASK`: the subnet prefix length for the destination network.



## Shard traffic across networks

**Requirements:**

  * `nic0` and `nic1` on the compute instance must connect to separate VPC networks and subnets, and destination IP addresses must be sharded across the two VPC networks.



### High-level overview

By default, the Linux kernel creates routes for the `nic0` subnet and the `nic1` subnet that route traffic by destination IP address through the corresponding network interface.

For example, suppose `nic0` uses VPC network `net1` with subnet `subnet-a`, and `nic1` uses VPC network `net2` with subnet `subnet-b`. By default, traffic to peer IP addresses in `subnet-a` uses `nic0`, and traffic to peer IP addresses in `subnet-b` uses `nic1`. This configuration commonly applies when a set of peer single-NIC compute instances connects to `net1` and a second set connects to `net2`.

**Tip:** If you run two instances of your application (one per VPC network), then you can use the `numactl` utility to NUMA-align each application's memory and compute resources with its network interface to minimize cross-socket transfers.

## Use SNAT to choose the source interface

**Warning:** This pattern is complex and has multiple interdependent parts. Make sure that you evaluate these rules in the context of other networking configurations on your machine. If you misconfigure the rules, then the system might misroute or drop system-wide traffic.

**Requirements:**

  * Requires the `CAP_NET_ADMIN` capability to set up the initial `iptables` rules, though not to run the application.
  * Requires careful evaluation when combined with other nontrivial `iptables` rules or routing configurations.

**Note:** NIC binding applies only when a connection is created. If a thread moves to a CPU on a different NUMA node, then the connection incurs cross-NUMA penalties. Bind threads to specific CPU sets when you use this pattern. Only outbound connections that originate from the instance bind to a specific NIC; inbound connections use the NIC that matches their destination IP address.

### High-level overview

If you can't use network namespaces or modify your application, then you can use SNAT to select a source interface. By using a tool such as `iptables`, you can rewrite the source IP address of a flow to match a specific interface's IP address based on a property of the sending application, such as its `cgroup`, user, or CPU.

The following example uses CPU-based rules so that any flow originating from a thread on a given CPU egresses through the gVNIC or IDPF interface attached to that CPU's NUMA node:
    
    
    # --- Begin Configuration ---
    OUTPUT_INTERFACE_0="enp0s19"        # CHANGEME: NIC0
    OUTPUT_INTERFACE_1="enp192s20"      # CHANGEME: NIC1
    
    CPUS_0=($(seq 0 55; seq 112 167))   # CHANGEME: CPU IDs for NIC0
    GATEWAY_0="10.0.0.1"                # CHANGEME: Gateway for NIC0
    SNAT_IP_0="10.0.0.2"                # CHANGEME: SNAT IP for NIC0
    CONNMARK_0="0x1"
    RT_TABLE_0="100"
    
    CPUS_1=($(seq 56 111; seq 168 223)) # CHANGEME: CPU IDs for NIC1
    GATEWAY_1="10.0.1.1"                # CHANGEME: Gateway for NIC1
    SNAT_IP_1="10.0.1.2"                # CHANGEME: SNAT IP for NIC1
    CONNMARK_1="0x2"
    RT_TABLE_1="101"
    # --- End Configuration ---
    
    # Specify which interface to use for packets in each routing table.
    ip route add default via "$GATEWAY_0" dev "$OUTPUT_INTERFACE_0" table "$RT_TABLE_0"
    ip route add default via "$GATEWAY_1" dev "$OUTPUT_INTERFACE_1" table "$RT_TABLE_1"
    
    # Route replies to connections from peers through the matching egress interface.
    # Add these rules before the fwmark rules so that fwmark takes precedence.
    ip rule add from "$SNAT_IP_0" table "$RT_TABLE_0"
    ip rule add from "$SNAT_IP_1" table "$RT_TABLE_1"
    
    # Select the routing table based on the packet mark set in OUTPUT.
    ip rule add fwmark "$CONNMARK_0" table "$RT_TABLE_0"
    ip rule add fwmark "$CONNMARK_1" table "$RT_TABLE_1"
    
    # Relax reverse path filtering so that the kernel doesn't drop legitimate
    # replies to the SNAT IP addresses.
    sysctl -w net.ipv4.conf."$OUTPUT_INTERFACE_0".rp_filter=2
    sysctl -w net.ipv4.conf."$OUTPUT_INTERFACE_1".rp_filter=2
    
    # Mark packets and connections with a per-NIC mark based on the source CPU.
    # The fwmark rules then select the corresponding routing table for this traffic.
    for cpu_id in "${CPUS_0[@]}"; do
        iptables -t mangle -A OUTPUT -m state --state NEW -m cpu --cpu "$cpu_id" -j CONNMARK --set-mark "$CONNMARK_0"
        iptables -t mangle -A OUTPUT -m state --state NEW -m cpu --cpu "$cpu_id" -j MARK --set-mark "$CONNMARK_0"
    done
    for cpu_id in "${CPUS_1[@]}"; do
        iptables -t mangle -A OUTPUT -m state --state NEW -m cpu --cpu "$cpu_id" -j CONNMARK --set-mark "$CONNMARK_1"
        iptables -t mangle -A OUTPUT -m state --state NEW -m cpu --cpu "$cpu_id" -j MARK --set-mark "$CONNMARK_1"
    done
    
    # Restore the connection mark for established connections so that packets use
    # the same NIC regardless of other routing rules.
    iptables -t mangle -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j CONNMARK --restore-mark
    
    # Rewrite the source address after the packet is routed to the target interface
    # so that replies return to the same NIC and pass VPC network validation.
    iptables -t nat -A POSTROUTING -m mark --mark "$CONNMARK_0" -j SNAT --to-source "$SNAT_IP_0"
    iptables -t nat -A POSTROUTING -m mark --mark "$CONNMARK_1" -j SNAT --to-source "$SNAT_IP_1"
    

## What's next

  * [Learn about networking and GPU machine types](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth)
  * [Use higher network bandwidth on GPU instances](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus)
  * [Configure multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
