---
url: https://docs.cloud.google.com/tpu/docs/custom-os-image/
title: Use a custom OS image \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T05:45:39.115357+00:00
---

# Use a custom OS image  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/custom-os-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use a custom OS image

You can use a custom OS image for your TPU VMs to pre-load software, use a specific OS distribution, or apply custom kernel modifications. Creating a custom image involves making specific system modifications during the image creation process and configuring the image to handle boot-time tasks required for TPU functionality.

**Important:** The system modifications, scripts, and configuration steps listed in this document are validated **only** for the specific Ubuntu versions certified by Google. For a list of supported versions, see [Google-managed OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images#google-managed_os_images). These instructions are Ubuntu-specific and are **not** validated for other operating system distributions or other Ubuntu versions.

Keep the following disclaimers in mind if you use a custom OS image with TPUs:

  * Google provides default TPU-optimized Ubuntu long-term support (LTS) images. The OS changes listed on this page are only validated for the Google-supported, TPU-optimized Ubuntu LTS images.
  * You are responsible for extrapolating the required OS changes for any other OS distribution or custom images. Google doesn't guarantee that the modifications for Ubuntu listed on this page work with other OS distributions or another Ubuntu image with a custom kernel.
  * Google doesn't build or provide testing for any OS images other than the default TPU-optimized Ubuntu LTS images. You must build and test your custom OS image.



For more information about the default TPU-optimized Ubuntu LTS images, see [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images).

## Prerequisites

Your base image must have the following components installed:

  * Docker
  * `ethtool`, version 6.7 or later if you use TPU v6e or TPU7x
  * Python 3 with the `PyYAML` and `requests` packages, available in Ubuntu as `python3-yaml` and `python3-requests`
  * gcloud CLI



For TPU7x VMs, your base image must use a minimum guest OS Linux kernel version of 6.8.

## Make modifications during image creation

Apply the following modifications while building your custom Ubuntu image.

### Disable unattended upgrades

Disable and remove `unattended-upgrades` so that background package updates don't hold the `dpkg` lock or interrupt TPU workloads:
    
    
    echo 'APT::Periodic::Unattended-Upgrade "0";' > /etc/apt/apt.conf.d/99cloudtpuconf
    DEBIAN_FRONTEND=noninteractive apt-get -y purge unattended-upgrades
    

### Bind TPU devices to VFIO

To allow the guest OS to access TPU hardware, you must bind TPU devices to the [`vfio-pci` driver](https://docs.kernel.org/driver-api/vfio.html).

  1. Create a udev rules file named `99-tpu-vfiopci.rules` in `/etc/udev/rules.d/`:
         
         # Rules for binding vfio-enabled TPU devices to vfio-pci.
         
         # v5p
         SUBSYSTEM=="pci", ACTION=="add", ATTRS{vendor}=="0x1ae0", ATTRS{device}=="0x0062", ATTRS{subsystem_vendor}=="0x1ae0", ATTRS{subsystem_device}=="0x00ad", DRIVER!="vfio-pci", TAG+="bind_to_vfio_pci"
         
         # v6e
         SUBSYSTEM=="pci", ACTION=="add", ATTRS{vendor}=="0x1ae0", ATTRS{device}=="0x006f", ATTRS{subsystem_vendor}=="0x1ae0", ATTRS{subsystem_device}=="0x00d1", DRIVER!="vfio-pci", TAG+="bind_to_vfio_pci"
         
         # TPU7x
         SUBSYSTEM=="pci", ACTION=="add", ATTRS{vendor}=="0x1ae0", ATTRS{device}=="0x0076", ATTRS{subsystem_vendor}=="0x1ae0", ATTRS{subsystem_device}=="0x00f2", DRIVER!="vfio-pci", TAG+="bind_to_vfio_pci"
         
         # Bind all 'bind_to_vfio_pci' tagged devices to vfio-pci.
         TAG=="bind_to_vfio_pci", RUN+="/lib/udev/bind_to_vfio_pci.sh $kernel"
         

  2. Create a script named `bind_to_vfio_pci.sh` in `/lib/udev/`:
         
         #!/bin/bash
         
         # Run ./bind_to_vfio_pci.sh <DBDF>
         # Binds the device at <DBDF> to vfio-pci.
         # If the device is already bound to a driver, unbinds it first.
         
         # Load the vfio-pci module into the kernel. No-op if already loaded.
         modprobe vfio-pci
         
         DBDF_REGEX="^[[:xdigit:]]{4}:[[:xdigit:]]{2}:[[:xdigit:]]{2}.[[:xdigit:]]$"
         
         unset BDF
         if [[ $1 =~ $DBDF_REGEX ]]; then
             BDF=$1
         else
             echo "Error: BDF arg ($1) is not in form dddd:bb:dd.f"
             exit 1
         fi
         
         PCI_PATH="/sys/bus/pci/devices/$BDF"
         
         echo "vfio-pci" > "$PCI_PATH/driver_override"
         
         PCI_DRIVER_PATH="$PCI_PATH/driver"
         if [[ -d "$PCI_DRIVER_PATH" ]]; then
             curr_driver=$(readlink "$PCI_DRIVER_PATH")
                 curr_driver=${curr_driver##*/}
             if [[ $curr_driver == "vfio-pci" ]]; then
                 echo "$BDF already bound to vfio-pci"
                 exit 0
             else
                 echo "$BDF" > "$PCI_DRIVER_PATH/unbind"
                 if [[ -d "$PCI_DRIVER_PATH" ]]; then
                     echo "Error: Unable to unbind $PCI_DRIVER_PATH"
                     exit 1
                 fi
                 echo "Unbound $BDF from driver $curr_driver"
             fi
         fi
         echo "$BDF" > /sys/bus/pci/drivers_probe
         echo "Bound $BDF to vfio-pci"
         
         # Grant read/write access on VFIO device to all users
         IOMMU_GROUP=$(readlink "$PCI_PATH/iommu_group" | xargs basename)
         VFIO_DEV="/dev/vfio/$IOMMU_GROUP"
         if [[ -c "$VFIO_DEV" ]]; then
             chmod 0666 "$VFIO_DEV"
         else
             echo "$VFIO_DEV not found"
             exit 1
         fi
         
         # Set allow_unsafe_interrupts for x86 platforms.
         (uname -a | grep -q x86_64) && echo 1 > /sys/module/vfio_iommu_type1/parameters/allow_unsafe_interrupts
         
         # This is only needed to avoid non-zero exit code from previous command.
         echo "All Done!"
         

  3. Make the script executable:
         
         chmod +x /lib/udev/bind_to_vfio_pci.sh
         

  4. Grant all users on the system access to the TPU device:
         
         echo 'KERNEL=="accel*" MODE="0666"' >> /etc/udev/rules.d/99-tpu.rules
         




### Modify the image to enhance performance

To ensure optimal performance, adjust the following system limits and parameters.

#### Memory limits

Allow a single process to lock unlimited memory by updating `/etc/security/limits.conf`:
    
    
    echo '*  hard  memlock  unlimited' >> /etc/security/limits.conf
    echo '*  soft  memlock  unlimited' >> /etc/security/limits.conf
    

#### File limits

Increase the number of open files by updating `/etc/security/limits.conf`:
    
    
    echo "*    soft    nofile       100000" >> /etc/security/limits.conf
    echo "*    hard    nofile       100000" >> /etc/security/limits.conf
    echo "root soft    nofile       100000" >> /etc/security/limits.conf
    echo "root hard    nofile       100000" >> /etc/security/limits.conf
    

#### Kernel parameters

Update your GRUB configuration (typically in `/etc/default/grub`) to include the following parameters in `GRUB_CMDLINE_LINUX`:

  * `idle=poll`: Prevents the CPU from entering low-power idle states.
  * `transparent_hugepage=always`: Enables Transparent Huge Pages (THP).
  * `iommu.passthrough=0`: Disables Input-Output Memory Management Unit (IOMMU) passthrough mode.
  * `panic=-1`: Configures the kernel to reboot immediately if a kernel panic occurs.
  * `intel_iommu=on,sm_on`: Enables Intel IOMMU in scalable mode. Required for TPU7x and v5p architectures.



The following steps show how to update these kernel parameters:

  1. Set the kernel command-line variable with the common parameters:
         
         kernel_cmdline="idle=poll transparent_hugepage=always iommu.passthrough=0 panic=-1"
         

  2. If you are building an image for TPU7x or TPU v5p, append the Intel IOMMU parameter:
         
         kernel_cmdline="${kernel_cmdline} intel_iommu=on,sm_on"
         

  3. Update `GRUB_CMDLINE_LINUX` in `/etc/default/grub` and regenerate the GRUB configuration:
         
         sed -i "s/^GRUB_CMDLINE_LINUX=\".*\"/GRUB_CMDLINE_LINUX=\"${kernel_cmdline}\"/" /etc/default/grub
         echo "Status: New kernel cmdline: $(grep -e '^GRUB_CMDLINE_LINUX=' /etc/default/grub)"
         
         update-grub
         




## Install vBar agent

The vBar agent is required for the inter-chip interconnect (ICI) network to function.

**Note:** Skip this section if you are building a custom OS image for use with Google Kubernetes Engine. GKE installs and manages the vBar agent for you, and installing it in the image can conflict with the version that GKE provides.

To pull the vBar agent container image during image creation, run the following commands:

  1. Authenticate Docker with `gcr.io`:
         
         gcloud auth configure-docker gcr.io
         

  2. Pull the vBar agent Docker image:
         
         docker pull gcr.io/cloud-tpu-v2-images/vbar_control_agent:0.0.3
         




To learn how to configure the image to start the vBar agent container at boot time, see Start the vBar agent.

## Optional: Install and run AI Telemetry Collector

The AI Telemetry Collector runs inside the TPU VM and lets you access runtime and infrastructure metrics through Cloud Monitoring or through your own Prometheus-based monitoring pipeline. You can use the AI Telemetry Collector with a custom OS by using the `ai-telemetry-collector` Docker image. You can install the image onto your custom OS and use a `config.yaml` file to dictate the collection intervals, enable or disable specific metrics, or change the export destinations.

**Note:** Skip this section if you are building a custom OS image for use with Google Kubernetes Engine. GKE installs and manages the AI Telemetry Collector for you.

To install and run the AI Telemetry Collector, run the following commands:

  1. Authenticate Docker with `gcr.io`:
         
         gcloud auth configure-docker gcr.io
         

  2. Pull the AI Telemetry Collector Docker image:
         
         docker pull gcr.io/cloud-tpu-v2-images/ai-telemetry-collector:latest
         

  3. Run a container using the AI Telemetry Collector image with the default configuration:
         
         docker run -d --restart=always --privileged --net=host gcr.io/cloud-tpu-v2-images/ai-telemetry-collector:latest
         

For information about using a custom configuration file or adding additional configuration files, see [AI Telemetry Collector](https://docs.cloud.google.com/tpu/docs/monitor-tpu#telemetry-collector).




## Make boot time modifications

Configure your image to perform the tasks in the following sections every time a VM boots. You can use the [`cloud-init`](https://docs.cloud-init.io/en/latest/index.html) tool to configure boot time tasks by passing metadata to your instances. The configurations in the following sections use modules such as [`write_files`](https://docs.cloud-init.io/en/latest/reference/modules.html#write-files) and [`runcmd`](https://docs.cloud-init.io/en/latest/reference/modules.html#runcmd). Snippets that define files to be written should be included under the `write_files:` key, and commands that should be run at boot time should be included under the `runcmd:` key in your `cloud-init` configuration.

### Start the vBar agent

**Note:** Skip this section if you are building a custom OS image for use with Google Kubernetes Engine. GKE runs and manages the vBar agent for you.

Start the vBar control agent container at boot time:
    
    
    docker run -d --restart=always --privileged --net=host \
      -e HOME=/home/tpu-runtime --name=vbar_control_agent \
      gcr.io/cloud-tpu-v2-images/vbar_control_agent:0.0.3 \
      vbar_control_agent_files/bin/vbar_control_agent --logtostderr
    

### Configure environment variables

To ensure your environment is correctly initialized for TPU workloads, you must retrieve runtime configuration variables from the Compute Engine metadata server during the system boot process. To do this, add the following snippet to the `write_files:` section of your `cloud-init` configuration, which creates a script named `/var/scripts/configure-env-vars.sh`. This script automates retrieval of attributes from the `tpu-env` metadata key and saves them in `/home/tpu-runtime/tpu-env` to be used by the TPU software stack.
    
    
    write_files:
      - path: /var/scripts/configure-env-vars.sh
        permissions: '0755'
        owner: root
        content: |
          #!/bin/bash
          grep -q CLOUDSDK_PYTHON /etc/environment || echo "CLOUDSDK_PYTHON=/usr/bin/python3" >> /etc/environment
          export HOME=/home/tpu-runtime
          mkdir -p "${HOME}"
          curl -s 'http://metadata.google.internal/computeMetadata/v1/instance/attributes/tpu-env' -H 'Metadata-Flavor: Google' > /tmp/tpu-env.yaml
          python3 -c '
          import yaml
          with open("/tmp/tpu-env.yaml", "r") as stream_in:
            for k, v in (yaml.safe_load(stream_in) or {}).items():
              print("{var}={value}".format(var=k, value=str(v)))
          ' > "${HOME}/tpu-env"
          rm -f /tmp/tpu-env.yaml
          set -a
          source "${HOME}/tpu-env"
          set +a
    

### Get VM metadata

The following snippet creates a script named `/var/scripts/get-vm-metadata.py`, a Python utility to programmatically query the metadata server for specific instance attributes and custom metadata tags. Add the following to the `write_files:` section of your `cloud-init` configuration:
    
    
    write_files:
      - path: /var/scripts/get-vm-metadata.py
        permissions: '0755'
        owner: root
        content: |
          #!/usr/bin/env python3
          import os
          import sys
          import requests
    
          if len(sys.argv) < 2:
            sys.stderr.write('Must provide key')
            os._exit(1)
    
          key = sys.argv[1]
          default = None
          if len(sys.argv) > 2:
            default = sys.argv[2]
    
          attribute_type = 'attributes'
          if len(sys.argv) > 3:
            attribute_type = sys.argv[3]
    
          request = requests.get(
              'http://metadata.google.internal/computeMetadata/v1/instance/{}/{}'.format(
                  attribute_type, key
              ),
              headers={'Metadata-Flavor': 'Google'},
          )
          if request.status_code == 200:
            print(request.text)
          elif request.status_code in (403, 404):
            sys.stderr.write('Metadata key: {} does not exist\n'.format(key))
            if default:
              print(default)
          else:
            sys.stderr.write('Lookup failed with: {}'.format(request))
    

### Increase Cloud Storage timeouts

If your workload interacts with Cloud Storage, increase timeout durations by adding timeout values to `/etc/environment`. To do this, add the following snippet to the `write_files:` section of your `cloud-init` configuration, which creates a script named `/var/scripts/configure-gcs-timeouts.sh`.
    
    
    write_files:
      - path: /var/scripts/configure-gcs-timeouts.sh
        permissions: '0755'
        owner: root
        content: |
          #!/bin/bash
          echo "GCS_RESOLVE_REFRESH_SECS=60" >> /etc/environment
          echo "GCS_REQUEST_CONNECTION_TIMEOUT_SECS=300" >> /etc/environment
          echo "GCS_METADATA_REQUEST_TIMEOUT_SECS=300" >> /etc/environment
          echo "GCS_READ_REQUEST_TIMEOUT_SECS=300" >> /etc/environment
          echo "GCS_WRITE_REQUEST_TIMEOUT_SECS=600" >> /etc/environment
    

### Configure network settings

To optimize network throughput and latency on TPU VMs, add the following scripts to the `write_files:` section of your `cloud-init` configuration. On TPU v6e and TPU7x VMs, these scripts also enable TCP data splitting, increased TCP receive buffer limits, and spreading NIC interrupts across NUMA cores. These scripts require the `/var/scripts/get-vm-metadata.py` script from the Get VM metadata section.
    
    
    write_files:
      - path: /var/scripts/configure-networking.sh
        permissions: '0755'
        owner: root
        content: |
          #!/bin/bash
          ACCELERATOR_TYPE=$(/usr/bin/python3 /var/scripts/get-vm-metadata.py accelerator-type)
          if [[ "$ACCELERATOR_TYPE" =~ ^v6e ]] || [[ "$ACCELERATOR_TYPE" =~ ^tpu7 ]]; then
            echo "Enabling max rx buffer size for v6e, tpu7x & tpu7"
            for port in $(ls /sys/class/net | grep ens); do
              dhclient -r "$port"
              if ethtool -h | grep -q tcp-data-split; then
                if ethtool -G "$port" tcp-data-split on; then
                  echo "Max RX buffer size and TCP data split enabled for $port"
                else
                  echo "Unable to enable max RX buffer size and TCP data split for $port"
                fi
              else
                if ethtool --set-priv-flags "$port" enable-max-rx-buffer-size on; then
                  echo "Max RX buffer size enabled for $port"
                else
                  echo "Unable to enable max RX buffer size for $port"
                fi
              fi
              dhclient "$port"
            done
          else
            echo "Skipping max rx buffer size for TPU generation $ACCELERATOR_TYPE before v6e"
          fi
    
      - path: /var/scripts/set_tcp_config.sh
        permissions: '0755'
        owner: root
        content: |
          #!/bin/bash
          echo "Setting TCP config"
    
          # Disable metrics cache
          sysctl -w net.ipv4.tcp_no_metrics_save=1
    
          # Disable slow start after idle
          sysctl -w net.ipv4.tcp_slow_start_after_idle=0
    
          # Set rto_min 5ms and enable quickack
          sysctl_rto_min_exists=$(sysctl -a | grep tcp_rto_min_us)
          if [[ -z "$sysctl_rto_min_exists" ]]; then
            ip route show | while IFS= read -r route; do
              if ! echo "$route" | grep -q "linkdown"; then
                ip route change ${route/lock/} rto_min 5ms quickack 1
              fi
            done
          else
            sysctl -w net.ipv4.tcp_rto_min_us=5000
            ip route show | while IFS= read -r route; do
              if ! echo "$route" | grep -q "linkdown"; then
                ip route change ${route/lock/} quickack 1
              fi
            done
          fi
    
          # Increase TCP zerocopy control memory
          sysctl -w net.core.optmem_max=131072
    
          # Disable Cubic Hystart Ack-Train
          echo 2 > /sys/module/tcp_cubic/parameters/hystart_detect
    
          ACCELERATOR_TYPE=$(/usr/bin/python3 /var/scripts/get-vm-metadata.py accelerator-type)
          if [[ "$ACCELERATOR_TYPE" =~ ^v6e ]] || [[ "$ACCELERATOR_TYPE" =~ ^tpu7 ]]; then
            # Increase TCP receive buffer limits
            echo "4096 41943040 314572800" > /proc/sys/net/ipv4/tcp_rmem
          fi
    
      - path: /var/scripts/spread-nic-irqs.sh
        permissions: '0755'
        owner: root
        content: |
          #!/bin/bash
          ACCELERATOR_TYPE=$(/usr/bin/python3 /var/scripts/get-vm-metadata.py accelerator-type)
          if [[ "$ACCELERATOR_TYPE" == v6e* ]] || [[ "$ACCELERATOR_TYPE" == tpu7* ]]; then
            node0_cores=$(echo /sys/devices/system/node/node0/cpu[0-9]* | wc -w)
            ht_buddies=$(cat /sys/devices/system/cpu/cpu0/topology/core_cpus_list | tr ',' ' ' | wc -w)
            total_schedulable_cores=$((node0_cores / ht_buddies))
            second_numa_starting_core=${total_schedulable_cores}
    
            first_numa_core=0
            second_numa_core=${second_numa_starting_core}
            for nic in $(ls -1 /sys/class/net); do
              if [[ -d "/sys/class/net/$nic/device" ]]; then
                NUM_QUEUES=$(echo /sys/class/net/"$nic"/queues/tx* | wc -w)
                base_ntfy_block=$(ls -1 /sys/class/net/"${nic}"/device/msi_irqs | sort -n | head -n 1)
                num_ntfy_blocks=$(ls /sys/class/net/"${nic}"/device/msi_irqs/ | wc -w)
                tx_irq_base_directory=$((base_ntfy_block))
                rx_irq_base_directory=$((base_ntfy_block + (num_ntfy_blocks / 2)))
    
                core=0
                max_core=${total_schedulable_cores}
                nic_numa=$(cat /sys/class/net/"${nic}"/device/numa_node)
                if [[ "${nic_numa}" -eq "1" ]]; then
                  core=${second_numa_core}
                  max_core=$((second_numa_starting_core + total_schedulable_cores))
                else
                  core=${first_numa_core}
                fi
    
                for ((queue = 0; queue < $NUM_QUEUES; queue++)); do
                  echo $core > /proc/irq/$((tx_irq_base_directory + $queue))/smp_affinity_list
                  echo $core > /proc/irq/$((rx_irq_base_directory + $queue))/smp_affinity_list
                  cp /proc/irq/$((tx_irq_base_directory + $queue))/smp_affinity /sys/class/net/"$nic"/queues/tx-"$queue"/xps_cpus
                  core=$((core + 1))
                  if [[ $core -ge $max_core ]]; then
                    if [[ "${nic_numa}" -eq "1" ]]; then
                      core=${second_numa_starting_core}
                    else
                      core=0
                    fi
                  fi
                done
    
                if [[ "${nic_numa}" -eq "1" ]]; then
                  second_numa_core=${core}
                else
                  first_numa_core=${core}
                fi
              fi
            done
          else
            echo "Skipping NIC IRQ spreading for TPU generation $ACCELERATOR_TYPE before v6e"
          fi
    

### Run the boot scripts

To run the configuration scripts automatically when the VM boots, add a `runcmd:` section to your `cloud-init` configuration:
    
    
    runcmd:
      - /var/scripts/configure-env-vars.sh
      - /var/scripts/configure-gcs-timeouts.sh
      - /var/scripts/configure-networking.sh
      - /var/scripts/set_tcp_config.sh
      - /var/scripts/spread-nic-irqs.sh
    

## What's next

  * Learn how to [Create a TPU VM instance](https://docs.cloud.google.com/tpu/docs/create-instance-compute) with your custom image.
  * Review available [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images).
  * Learn how to [Manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
