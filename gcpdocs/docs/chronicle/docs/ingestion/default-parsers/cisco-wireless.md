---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/
title: Collect Cisco Wireless LAN Controller (WLC) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:05:21.286547+00:00
---

# Collect Cisco Wireless LAN Controller (WLC) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/

[ Skip to main content ](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/)
  * [Deutsch](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=de)
  * [Español](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=es-419)
  * [Français](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=id)
  * [Italiano](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=it)
  * [Português](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=ja)
  * [한국어](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/secops-color.svg) ](https://docs.cloud.google.com/chronicle/docs)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#before_you_begin)
  * [Get Google SecOps credentials for the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#get-auth-file)
    * [Option 1: Create a service account for the Chronicle API (recommended)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#option_1_create_a_service_account_for_the_chronicle_api_recommended)
    * [Option 2: Download the ingestion authentication file (legacy)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#option_2_download_the_ingestion_authentication_file_legacy)
  * [Get Google SecOps customer ID](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#get_customer_id)
  * [Install the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#install_the_bindplane_agent)
    * [Windows installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#windows_installation)
    * [Linux installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#linux_installation)
    * [Additional installation resources](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#additional_installation_resources)
  * [Configure the Bindplane agent to ingest syslog and send to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#configure_the_bindplane_agent_to_ingest_syslog_and_send_to)
    * [Locate the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#locate_the_configuration_file)
    * [Edit the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#edit_the_configuration_file)
    * [Configuration parameters](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#configuration_parameters)
    * [Legacy ingestion API exporter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#legacy_ingestion_api_exporter)
    * [Save the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#save_the_configuration_file)
  * [Restart the Bindplane agent to apply the changes](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#restart_the_bindplane_agent_to_apply_the_changes)
  * [Configure syslog on Cisco WLC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#configure_syslog_on_cisco_wlc)
  * [UDM mapping table](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#udm_mapping_table)
  * [Change Log](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#change_log)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)


Send feedback 
  * On this page
  * [Before you begin](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#before_you_begin)
  * [Get Google SecOps credentials for the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#get-auth-file)
    * [Option 1: Create a service account for the Chronicle API (recommended)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#option_1_create_a_service_account_for_the_chronicle_api_recommended)
    * [Option 2: Download the ingestion authentication file (legacy)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#option_2_download_the_ingestion_authentication_file_legacy)
  * [Get Google SecOps customer ID](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#get_customer_id)
  * [Install the Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#install_the_bindplane_agent)
    * [Windows installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#windows_installation)
    * [Linux installation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#linux_installation)
    * [Additional installation resources](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#additional_installation_resources)
  * [Configure the Bindplane agent to ingest syslog and send to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#configure_the_bindplane_agent_to_ingest_syslog_and_send_to)
    * [Locate the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#locate_the_configuration_file)
    * [Edit the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#edit_the_configuration_file)
    * [Configuration parameters](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#configuration_parameters)
    * [Legacy ingestion API exporter](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#legacy_ingestion_api_exporter)
    * [Save the configuration file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#save_the_configuration_file)
  * [Restart the Bindplane agent to apply the changes](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#restart_the_bindplane_agent_to_apply_the_changes)
  * [Configure syslog on Cisco WLC](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#configure_syslog_on_cisco_wlc)
  * [UDM mapping table](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#udm_mapping_table)
  * [Change Log](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wireless/#change_log)


# Collect Cisco Wireless LAN Controller (WLC) logs Stay organized with collections  Save and categorize content based on your preferences.
**Parser Version:** 12.0
Supported in:
Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)
This document explains how to ingest Cisco Wireless LAN Controller (WLC) logs to Google Security Operations using the Bindplane agent.
The parser extracts fields from Cisco WLC syslog messages using grok patterns, handling various log formats including DHCP, authentication, and network events. It maps extracted fields to the Unified Data Model (UDM) and determines the event type based on the `mnemonic` and message content.
## Before you begin
Make sure you have the following prerequisites:
  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco WLC
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Cisco WLC


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
For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).
## Configure the Bindplane agent to ingest syslog and send to Google SecOps
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
  chronicle/cisco_wireless:
    protocol: https
    # Region of your instance, for example us, europe, asia-southeast1
    location: <LOCATION>
    # Project number of the Google Cloud project linked to the instance
    project: '<PROJECT_NUMBER>'
    compression: gzip
    creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
    customer_id: '<customer_id>'
    endpoint: chronicle.googleapis.com
    log_type: CISCO_WIRELESS
    raw_log_field: body

service:
  pipelines:
    logs/cisco_wireless_to_chronicle:
      receivers:
        - udplog
      exporters:
        - chronicle/cisco_wireless

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
  chronicle/cisco_wireless:
    compression: gzip
    creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
    customer_id: '<customer_id>'
    endpoint: malachiteingestion-pa.googleapis.com
    log_type: CISCO_WIRELESS
    raw_log_field: body

```



### Save the configuration file
  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**


## Restart the Bindplane agent to apply the changes
  * To restart the Bindplane agent in Linux, run the following command:

```
sudo systemctl restart observiq-otel-collector

```

    1. Verify the service is running:

```
sudo systemctl status observiq-otel-collector

```

    2. Check logs for errors:

```
sudo journalctl -u observiq-otel-collector -f

```

  * To restart the Bindplane agent in Windows, choose one of the following options:
    * Command Prompt or PowerShell as administrator:

```
net stop observiq-otel-collector && net start observiq-otel-collector

```

    * Services console:
      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:

```
sc query observiq-otel-collector

```

      5. Check logs for errors:

```
type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"

```



## Configure syslog on Cisco WLC
  1. Sign in to the **WLC** web UI.
  2. Go to **Management > Logs > Config**.
  3. Enter the Bindplane agent IP address in the **Syslog Server IP Address** field.
  4. Click **Add**.
  5. Provide the following configuration details: 
     * **Syslog Severity** : Select **Informational**.
     * **Syslog Facility** : Select **Local Use 0**.
  6. Click **Apply**.
  7. Click **Save Configuration**.


## UDM mapping table  
| Log Field  | UDM Mapping  | Logic  |  
| --- | --- | --- |  
| `action_data`  | `read_only_udm.security_result.action_details`  | Directly mapped from the `action_data` field.  |  
| `data`  | `read_only_udm.metadata.description`  | Directly mapped from the `data` field after some processing (e.g., removing timestamps, extra characters). Extracted from the timestamp at the beginning of the log message. Various formats are handled by the parser. Determined based on the `mnemonic` and `messageToProcess` fields using complex logic within the `cisco_wireless.include` file. Set to "CISCO_WIRELESS". Concatenation of `facility`, `cisco_severity`, and `mnemonic` fields. Extracted from the log message when available. Set to "CISCO_WIRELESS". Extracted from the `version` field when available. Set to "CISCO". Set to "DHCP" when the event relates to DHCP. Set to "BROADCAST" for broadcast network events. Set to "UDP" for UDP network events. Extracted from the description when available. Extracted from the description when available. Mapped from `wlc_controller` or `hostname` fields, depending on the log format. Extracted from the description or `MessageSourceAddress` when available. Mapped from `wlc_controller` or `hostname` fields, depending on the log format. Extracted from the description or `MessageSourceAddress` when available. Extracted from the description when available. Extracted from the description when available. Created from `SourceModuleName` and `SourceModuleType` fields when available. Mapped from `read_only_udm.principal.user.userid` when the userid looks like an email address. Extracted from the description when available. Extracted from the description when available. Determined based on the event type and description. Determined based on the event type and description. Created from specific fields within the description when available. Extracted from the description when available. Sometimes combines information from multiple fields. Determined based on the `cisco_severity` field and event type. Derived from the `read_only_udm.security_result.severity` field. A concise summary of the security result, derived from the description and event type. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Extracted from the description when available. Set to "SETTING" for setting modification events. Extracted from the description when available.  |  
| `event_data`  | `read_only_udm.metadata.product_event_type`  | Directly mapped from the `event_data` field.  |  
| `event_id`  | `read_only_udm.metadata.product_log_id`  | Directly mapped from the `event_id` field.  |  
| `event_ts`  | `read_only_udm.metadata.event_timestamp`  | Directly mapped from the `event_ts` field.  |  
| `facility`  | `read_only_udm.metadata.product_event_type`  | Directly mapped from the `facility` field.  |  
| `hostname`  | `read_only_udm.principal.hostname`  | Directly mapped from the `hostname` field.  |  
| `hostname`  | `read_only_udm.target.hostname`  | Directly mapped from the `hostname` field.  |  
| `inter_mac`  | `read_only_udm.intermediary.mac`  | Directly mapped from the `inter_mac` field.  |  
| `intermediary_hostname`  | `read_only_udm.intermediary.hostname`  | Directly mapped from the `intermediary_hostname` field.  |  
| `kv_data`  | `read_only_udm.principal.resource.attribute.labels`  | Parsed as key-value pairs and used to populate labels.  |  
| `log_message`  | `read_only_udm.security_result.description`  | Directly mapped from the `log_message` field.  |  
| `MessageSourceAddress`  | `read_only_udm.principal.asset.ip`  | Directly mapped from the `MessageSourceAddress` field.  |  
| `MessageSourceAddress`  | `read_only_udm.principal.ip`  | Directly mapped from the `MessageSourceAddress` field.  |  
| `messageToProcess`  | `read_only_udm.metadata.description`  | Directly mapped from the `messageToProcess` field after some processing.  |  
| `mnemonic`  | `read_only_udm.metadata.event_type`  | Used in conjunction with other fields to determine the event type.  |  
| `mnemonic`  | `read_only_udm.metadata.product_event_type`  | Directly mapped from the `mnemonic` field.  |  
| `severity_data`  | `read_only_udm.security_result.severity`  | Mapped from the `severity_data` field after converting it to an enum value.  |  
| `SourceModuleName`  | `read_only_udm.principal.resource.attribute.labels`  | Directly mapped from the `SourceModuleName` field.  |  
| `SourceModuleType`  | `read_only_udm.principal.resource.attribute.labels`  | Directly mapped from the `SourceModuleType` field.  |  
| `timestamp`  | `read_only_udm.metadata.event_timestamp`  | Directly mapped from the `timestamp` field.  |  
| `version`  | `read_only_udm.metadata.product_version`  | Directly mapped from the `version` field.  |  
| `wlc_controller`  | `read_only_udm.principal.hostname`  | Directly mapped from the `wlc_controller` field.  |  
| `wlc_controller`  | `read_only_udm.target.hostname`  | Directly mapped from the `wlc_controller` field.  |  
| `mnemonic`  | `event.idm.read_only_udm.metadata.product_event_type`  | Mapped from changelog  |  
| `urlHolder`  | `event.idm.read_only_udm.target.url`  | Mapped from changelog  |  
| `syslog_sequence`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `userid`  | `event.idm.read_only_udm.principal.user.userid`  | Mapped from changelog  |  
| `principal_mac`  | `event.idm.read_only_udm.principal.mac`  | Mapped from changelog  |  
| `obs_host`  | `event.idm.read_only_udm.observer.hostname`  | Mapped from changelog  |  
| `obs_desc`  | `event.idm.read_only_udm.observer.labels`  | Mapped from changelog  |  
| `addr`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `component_status`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `ecc`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `multipleErrorsDetected`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `rep[0]`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `rep[1]`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `rep[2]`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `suppressed_times`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `valid`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `interface`  | `event.idm.read_only_udm.additional.fields`  | Mapped from changelog  |  
| `event_id`  | `event.idm.read_only_udm.metadata.product_log_id`  | Mapped from changelog  |  
| `principal_hostname`  |  `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`  | Mapped from changelog  |  
| `wlc_controller`  |  `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`  | Mapped from changelog  |  
| `src_ip_1`  | `event.idm.read_only_udm.principal.ip`  | Mapped from changelog  |  
| `src_ip_2`  | `event.idm.read_only_udm.principal.ip`  | Mapped from changelog  |  
| `mac1`  | `event.idm.read_only_udm.principal.mac`  | Mapped from changelog  |  
| `mac2`  | `event.idm.read_only_udm.principal.mac`  | Mapped from changelog  |  
| `slot`  | `event.idm.read_only_udm.security_result.detection_fields`  | Mapped from changelog  |  
| `username`  | `event.idm.read_only_udm.principal.user.userid`  | Mapped from changelog  |  
| `src_ip`  |  `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`  | Mapped from changelog  |  
| `ssid`  | `event.idm.read_only_udm.security_result.detection_fields`  | Mapped from changelog  |  
| `SourceModuleName" and "SourceModuleType`  | `principal.resource.attribute.labels`  | Mapped from changelog  |  
| `client_host", and "hostname`  | `principal.hostname`  | Mapped from changelog  |  
| `client_ip`  | `principal.ip`  | Mapped from changelog  |  
| `client_mac`  | `principal.mac`  | Mapped from changelog  |  
| `ap_ip`  | `target.ip`  | Mapped from changelog  |  
| `ap_mac`  | `target.mac`  | Mapped from changelog  |  
| `messageToProcess" and "description`  | `metadata.description`  | Mapped from changelog  |  
| `inter_url`  | `intermediary.url`  | Mapped from changelog  |  
| `inter_ip`  | `intermediary.ip`  | Mapped from changelog  |  
| `sec_desc`  | `security_result.description`  | Mapped from changelog  |  
| `latest_version", "current_version", "certificate", "expiry_date", "clostest_sensor", "ssid", "client", "xid", "failure_reason", "auth_failure_reason", and "interface`  | `security_result.detection_fields`  | Mapped from changelog  |  
| `action_data`  | `security_result.acion_details`  | Mapped from changelog  |  
| `username`  | `principal.user.userid`  | Mapped from changelog  |  
| `vendor", and "RSSI`  | `principal.resource.attribute.labels`  | Mapped from changelog  |  
| `vendor", "security_setting", "channel", "protocol", and "RSSI`  | `target.resource.attribute.labels`  | Mapped from changelog  |  
| `msg1`  | `metadata.description`  | Mapped from changelog  |  
| `wlc_controller`  | `event.idm.read_only_udm.principal.hostname`  | Mapped from changelog  |  
| `event.idm.read_only_udm.metadata.event_type`  | `USER_RESOURCE_ACCESS`  | Mapped from changelog  |  
## Change Log
[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wireless-changelog)
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
