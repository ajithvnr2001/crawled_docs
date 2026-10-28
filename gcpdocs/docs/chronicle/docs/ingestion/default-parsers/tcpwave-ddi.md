---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/
title: Collect TCPWave DDI logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:03:49.096979+00:00
---

# Collect TCPWave DDI logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/

[ Skip to main content ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/)
  * [Deutsch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=es-419)
  * [Français](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=id)
  * [Italiano](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=ja)
  * [한국어](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/secops-color.svg) ](https://docs.cloud.google.com/chronicle/docs)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#before_you_begin)
  * [Get Google SecOps credentials for the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#get-auth-file)
    * [Option 1: Create a service account for the Chronicle API (recommended)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#option_1_create_a_service_account_for_the_chronicle_api_recommended)
    * [Option 2: Download the ingestion authentication file (legacy)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#option_2_download_the_ingestion_authentication_file_legacy)
  * [Get Google SecOps customer ID](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#get_customer_id)
  * [Install the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#install_the_bindplane_agent)
    * [Windows installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#windows_installation)
    * [Linux installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#linux_installation)
    * [Additional installation resources](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#additional_installation_resources)
  * [Configure Bindplane agent to ingest syslog and send to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#configure_bindplane_agent_to_ingest_syslog_and_send_to)
    * [Locate the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#locate_the_configuration_file)
    * [Edit the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#edit_the_configuration_file)
    * [Configuration parameters](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#configuration_parameters)
    * [Legacy ingestion API exporter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#legacy_ingestion_api_exporter)
    * [Save the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#save_the_configuration_file)
  * [Restart the Bindplane agent to apply the changes](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#restart_the_bindplane_agent_to_apply_the_changes)
  * [Configure TCPWave DDI syslog forwarding](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#configure_tcpwave_ddi_syslog_forwarding)
  * [UDM mapping table](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#udm_mapping_table)
  * [Change Log](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#change_log)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)


Was this helpful?
Send feedback 
  * On this page
  * [Before you begin](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#before_you_begin)
  * [Get Google SecOps credentials for the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#get-auth-file)
    * [Option 1: Create a service account for the Chronicle API (recommended)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#option_1_create_a_service_account_for_the_chronicle_api_recommended)
    * [Option 2: Download the ingestion authentication file (legacy)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#option_2_download_the_ingestion_authentication_file_legacy)
  * [Get Google SecOps customer ID](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#get_customer_id)
  * [Install the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#install_the_bindplane_agent)
    * [Windows installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#windows_installation)
    * [Linux installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#linux_installation)
    * [Additional installation resources](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#additional_installation_resources)
  * [Configure Bindplane agent to ingest syslog and send to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#configure_bindplane_agent_to_ingest_syslog_and_send_to)
    * [Locate the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#locate_the_configuration_file)
    * [Edit the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#edit_the_configuration_file)
    * [Configuration parameters](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#configuration_parameters)
    * [Legacy ingestion API exporter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#legacy_ingestion_api_exporter)
    * [Save the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#save_the_configuration_file)
  * [Restart the Bindplane agent to apply the changes](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#restart_the_bindplane_agent_to_apply_the_changes)
  * [Configure TCPWave DDI syslog forwarding](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#configure_tcpwave_ddi_syslog_forwarding)
  * [UDM mapping table](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#udm_mapping_table)
  * [Change Log](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tcpwave-ddi/#change_log)


# Collect TCPWave DDI logs Stay organized with collections  Save and categorize content based on your preferences.
Supported in:
Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)
This document explains how to ingest TCPWave DDI logs to Google Security Operations using Bindplane.
TCPWave DDI is a DNS, DHCP, and IPAM management platform for enterprise network infrastructure. It provides centralized management of IP address allocation, DNS resolution, and DHCP services across on-premise environments.
## Before you begin
Make sure you have the following prerequisites:
  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the TCPWave DDI server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to TCPWave DDI with administrator permissions


## Get Google SecOps credentials for the Bindplane agent
To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:
  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.


### Option 1: Create a service account for the Chronicle API (recommended)
  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.


### Option 2: Download the ingestion authentication file (legacy)
  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.


## Get Google SecOps customer ID
  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.


## Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
### Windows installation
  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:

```
msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet

```

  3. Wait for the installation to complete.
  4. Verify the installation by running:

```
sc query observiq-otel-collector

```



The service should show as **RUNNING**.
### Linux installation
  1. Open a terminal with root or sudo privileges.
  2. Run the following command:

```
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh

```

  3. Wait for the installation to complete.
  4. Verify the installation by running:

```
sudo systemctl status observiq-otel-collector

```



The service should show as **active (running)**.
### Additional installation resources
For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).
## Configure Bindplane agent to ingest syslog and send to Google SecOps
### Locate the configuration file
  * **Linux:**

```
sudo nano /opt/observiq-otel-collector/config.yaml

```

  * **Windows:**

```
notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"

```



### Edit the configuration file
  * Replace the entire contents of `config.yaml` with the following configuration:

```
receivers:
  udplog:
    listen_address: "0.0.0.0:514"

exporters:
  chronicle/tcpwave_ddi:
    protocol: https
    # Region of your instance, for example us, europe, asia-southeast1
    location: <LOCATION>
    # Project number of the Google Cloud project linked to the instance
    project: '<PROJECT_NUMBER>'
    compression: gzip
    creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
    customer_id: '<customer_id>'
    endpoint: chronicle.googleapis.com
    log_type: TCPWAVE_DDI
    raw_log_field: body

service:
  pipelines:
    logs/tcpwave_ddi_to_chronicle:
      receivers:
        - udplog
      exporters:
        - chronicle/tcpwave_ddi

```



### Configuration parameters
Replace the following placeholders:
  * **Receiver configuration:**
    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.


### Legacy ingestion API exporter
  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).

```
exporters:
  chronicle/tcpwave_ddi:
    compression: gzip
    creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
    customer_id: '<customer_id>'
    endpoint: malachiteingestion-pa.googleapis.com
    log_type: TCPWAVE_DDI
    raw_log_field: body

```



### Save the configuration file
  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**


## Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux: 
  1. Run the following command:

```
sudo systemctl restart observiq-otel-collector

```

  2. Verify the service is running:

```
sudo systemctl status observiq-otel-collector

```

  3. Check logs for errors:

```
sudo journalctl -u observiq-otel-collector -f

```



To restart the Bindplane agent in Windows:
  1. Choose one of the following options:
     * Command Prompt or PowerShell as administrator:

```
net stop observiq-otel-collector && net start observiq-otel-collector

```

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:

```
sc query observiq-otel-collector

```

  3. Check logs for errors:

```
type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"

```



## Configure TCPWave DDI syslog forwarding
  1. Sign in to the **TCPWave DDI** management console.
  2. Go to **Administration > System Settings > Syslog Configuration**.
  3. Click **Add** to create a new syslog destination.
  4. Provide the following configuration details: 
     * **Syslog Server IP** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
     * **Facility** : Select **Local0** or your preferred facility.
     * **Severity Level** : Select **Informational** or higher.
  5. Select the log categories to forward (DNS queries, DHCP events, IPAM changes, system events).
  6. Click **Save** to apply the configuration.
  7. Verify that logs are being sent by checking the Bindplane agent logs.


## UDM mapping table  
| Log Field  | UDM Mapping  | Logic  |  
| --- | --- | --- |  
| `dhcp_pool_backup_label`  | `additional.fields`  | Merged  |  
| `dhcp_pool_free_label`  | `additional.fields`  | Merged  |  
| `dhcp_pool_lts_label`  | `additional.fields`  | Merged  |  
| `dhcp_pool_max_misbal_label`  | `additional.fields`  | Merged  |  
| `dhcp_pool_max_own_label`  | `additional.fields`  | Merged  |  
| `dhcp_pool_range_label`  | `additional.fields`  | Merged  |  
| `dhcp_pool_total_label`  | `additional.fields`  | Merged  |  
| `pool_id_label`  | `additional.fields`  | Merged  |  
| `intermediary_entry`  | `intermediary`  | Merged  |  
| `description`  | `metadata.description`  | Directly mapped  |  
| `ts`  | `metadata.event_timestamp`  | Parsed as `MMM d HH:mm:ss`  |  
| `description`  | `metadata.event_type`  | Mapped values (5 total, e.g. `DHCPDISCOVER` → `NETWORK_DHCP`, `DHCPACK` → `NETWORK_DHCP`, `D...  |  
| `client_label`  | `metadata.ingestion_labels`  | Merged  |  
| `label`  | `metadata.ingestion_labels`  | Merged  |  
| `smb_stage_label`  | `metadata.ingestion_labels`  | Merged  |  
| `zone_label`  | `metadata.ingestion_labels`  | Merged  |  
| `product_event_type`  | `metadata.product_event_type`  | Directly mapped  |  
| `description`  | `network.application_protocol`  | Mapped values (5 total, e.g. `DHCPDISCOVER` → `DHCP`, `DHCPACK` → `DHCP`, `DHCPREQUEST` → `D...  |  
| `src_mac`  | `network.dhcp.chaddr`  | Directly mapped  |  
| `d_clientID`  | `network.dhcp.client_identifier`  | Directly mapped  |  
| `description`  | `network.dhcp.type`  | Mapped values (5 total, e.g. `DHCPDISCOVER` → `DISCOVER`, `DHCPACK` → `ACK`, `DHCPREQUEST` →...  |  
| `intermediary_host`  | `principal.hostname`  | Directly mapped  |  
| `smb_host`  | `principal.hostname`  | Directly mapped  |  
| `field.value`  | `principal.location.country_or_region`  | Directly mapped  |  
| `filepath`  | `principal.process.file.full_path`  | Directly mapped  |  
| `smb_uid`  | `principal.user.userid`  | Directly mapped  |  
| `description`  | `security_result.action`  | Mapped: `rejected` → `security_action`  |  
| `security_action`  | `security_result.action`  | Merged  |  
| `des`  | `security_result.description`  | Directly mapped  |  
| `product_event_type`  | `security_result.severity`  | Mapped: `info` → `INFORMATIONAL`, `error` → `ERROR`  |  
| `thread`  | `security_result.summary`  | Directly mapped  |  
| `src`  | `src.hostname`  | Directly mapped  |  
| `src_mac`  | `src.mac`  | Merged  |  
| `d_domain`  | `target.administrative_domain`  | Directly mapped  |  
| `application`  | `target.application`  | Directly mapped  |  
| `d_host`  | `target.hostname`  | Directly mapped  |  
| `d_ip`  | `target.ip`  | Merged  |  
| `target_ip`  | `target.ip`  | Merged  |  
| `d_mac`  | `target.mac`  | Merged  |  
| `port`  | `target.port`  | Directly mapped  |  
| `pid`  | `target.process.pid`  | Directly mapped  |  
| N/A  | `metadata.event_type`  | Constant: `NETWORK_DHCP`  |  
| N/A  | `metadata.product_name`  | Constant: `TCPWAVE_DDI`  |  
| N/A  | `metadata.vendor_name`  | Constant: `TCPWAVE_DDI`  |  
| N/A  | `network.application_protocol`  | Constant: `DHCP`  |  
| N/A  | `network.dhcp.client_identifier`  | Constant: `bytes`  |  
| N/A  | `network.dhcp.type`  | Constant: `DISCOVER`  |  
| N/A  | `security_result.severity`  | Constant: `INFORMATIONAL`  |  
## Change Log
[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tcpwave-ddi-changelog)
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
