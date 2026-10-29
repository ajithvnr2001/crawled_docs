---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-on-demand/
title: Collect Proofpoint On-Demand logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:07:03.649924+00:00
---

# Collect Proofpoint On-Demand logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-on-demand/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint On-Demand logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint On-Demand logs to Google Security Operations using built-in API integration. The parser extracts fields from JSON logs, transforming them into the Chronicle UDM format. It handles two primary log formats: one containing email metadata and the other containing SMTP transaction details, using conditional logic to parse fields appropriately and populate the Unified Data Model (UDM) fields based on the available data. The parser also performs data cleaning, such as removing extraneous characters and converting timestamps.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * **Proofpoint On-Demand Remote Syslog** license
  * Privileged access to Proofpoint



## Configure Proofpoint On-Demand API access

  1. Sign in to the **Proofpoint Admin** portal.
  2. Copy your **Cluster ID** (displayed on the upper-right corner of your management interface, next to the release number).
  3. Go to **Settings > API Key Management**.
  4. Click **Create New** to open the **Create New API Key** dialog.
  5. Enter a unique **Name** (for example, `Google SecOps Key`).
  6. Generate the **API Key**.
  7. Select **View Details** from the ellipsis menu on the new API Key.
  8. Copy the **API Key**.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. Click the **Proofpoint** feed pack. 
  4. Select the **Proofpoint On-Demand** log type.
  5. Click **Next**.
  6. Specify values for the following input parameters: 
     * **Source Type** : Third party API
     * **Authentication HTTP headers** : Enter the Proofpoint API Key in a `Authorization: Bearer {API_KEY}` format, and add in a new line with the following WebSocket-Key data: `Sec-WebSocket-Key: SGVsbG8sIHdvcmxkIQ==`.
     * **Cluster ID** : Enter the Proofpoint Cluster ID that you copied earlier.

**Advanced options**



  * **Feed Name** : A prepopulated value that identifies the feed.
  * **Asset Namespace** : Namespace associated with the feed.
  * **Ingestion Labels** : Labels applied to all events from this feed.


  1. Click **Create Feed**.



## UDM mapping table

The following tables list the mappings of Proofpoint On-Demand log fields to UDM fields.

### Event-type mappings

The following table lists the Proofpoint On-Demand event-type mappings. For more information, see [Metadata.EventType](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#metadataeventtype) and [Metadata](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#metadata). 

Event type | Mapping | Remarks  
---|---|---  
`EMAIL_TRANSACTION` | `metadata.event_type` | If `(([has_sender_email] == "true" or [has_recipient_email] == "true") and (([has_principal] == "true" or [has_principal_user] == "true")))`.  
`GENERIC_EVENT` | `metadata.event_type` | Default fallback for `event_type`.  
`NETWORK_CONNECTION` | `metadata.event_type` | If `[has_principal] == "true" and [has_target] == "true"`.  
`STATUS_UPDATE` | `metadata.event_type` | If `[has_principal] == "true"`.  
  
### General log fields

Log field | UDM mapping | Remarks  
---|---|---  
`aliasedRcptsvalue.alias` | `additional.fields` |   
`aliasedRcptsvalue.primary` | `additional.fields` |   
`alignment.fromDomain` | `additional.fields` |   
`alignmentresult.identity` | `security_result.detection_fields` |   
`alignmentresult.identityOrg` | `security_result.detection_fields` |   
`alignmentresult.result` | `security_result.detection_fields` |   
`ALLOW` | `security_result.action` | If `[tls][verify] == "OK"` or `[filter][disposition] in ["continue", "accept", "CLEAR", "OK", "redirect"]`.  
`app_protocol_output` | `network.application_protocol` | Extracted from a `data` field.  
`audit.action` | `security_result.about.resource.attribute.labels` |   
`audit.level` | `security_result.severity_details` | Extracted from a key-value pair in a `data` field.  
`audit.resourceType` | `target.resource.name` | Extracted from a key-value pair in a `data` field.  
`audit.tags.value` | `security_result.detection_fields` |   
`audit.user.email` | `principal.user.email_addresses` | If `[audit][user][email] =~ "^.+@.+$"`.  
`audit.user.id` | `principal.user.userid` | Extracted from a key-value pair in a `data` field.  
`audit.user.ipAddress` | `principal.asset.ip`,  
`principal.ip` |   
`autheresults.method` | `security_result.detection_fields` |   
`autheresults.result` | `additional.fields` |   
`BLOCK` | `security_result.action` | If `[tls][verify] == "FAIL"` or `[filter][disposition] in ["discard", "reject"]`.  
`campaignID` | `security_result.detection_fields` |   
`cc` | `network.email.cc` | If `[cc] =~ "^.+@.+$"`.  
`CHALLENGE` | `security_result.action` | If `[filter][disposition] in ["hold", "retry"]`.  
`charsets` | `security_result.detection_fields` |   
`classification` | `security_result.detection_fields` |   
`cluster` | `security_result.detection_fields` |   
`cmd` | `principal.process.command_line` | Extracted from a `data` field.  
`completelyRewritten` | `security_result.detection_fields` |   
`connection.country` | `principal.location.country_or_region` | Extracted from a key-value pair in a `data` field.  
`connection.helo` | `network.smtp.helo` | Extracted from a key-value pair in a `data` field.  
`connection.host` | `principal.asset.hostname`,  
`principal.hostname` | Extracted from a key-value pair in a `data` field.  
`connection.ip` | `principal.asset.ip`,  
`principal.ip` |   
`connection.resolveStatus` | `additional.fields` |   
`connection.sid` | `security_result.detection_fields` |   
`connection.tls.inbound.cipher` | `network.tls.cipher` | Extracted from a key-value pair in a `data` field. If `[tls_cipher] not in ["", "null", "None", "none", "NONE"] AND [tls_version] not in ["", "null", "None", "none", "NONE"]`.  
`connection.tls.inbound.cipherBits` | `additional.fields` |   
`connection.tls.inbound.version` | `network.tls.version` | Extracted from a key-value pair in a `data` field. If `[tls_cipher] not in ["", "null", "None", "none", "NONE"] AND [tls_version] not in ["", "null", "None", "none", "NONE"]`.  
`data` | `network.email.to`,  
`target.user.email_addresses` | If `[email] =~ "^.+@.+$"`.  
`detectedExt` | `additional.fields` |   
`detectedName` | `additional.fields` |   
`disposition` | `additional.fields` |   
`duration` | `security_result.detection_fields` |   
`emailaddr` | `target.user.email_addresses` |   
`emailaddrnorm` | `target.user.email_addresses` |   
`emailaddrparsed` | `target.user.email_addresses` |   
`envelope.from` | `network.email.from` |   
`ERROR` | `security_result.severity` | If `[audit][level] =~ "(?i)(error)"`.  
`eventTime` | `metadata.event_timestamp` |   
`event_type` | `security_result.summary` |   
`extracted_bytes` | `network.sent_bytes` | Extracted from a `data` field.  
`extracted_internal_id` | `additional.fields` |   
`extracted_msgid` | `additional.fields` |   
`extracted_queue_status` | `additional.fields` |   
`extracted_target_host` | `target.asset.hostname`,  
`target.hostname` | Extracted from a `data` field.  
`extracted_throughput` | `additional.fields` |   
`extracted_transfer_time` | `additional.fields` |   
`FAIL` | `security_result.action` | If `[filter][disposition] in ["FAIL", "TEMP"]`.  
`field_` | `additional.fields` | If `NOT = "agent"`.  
`FILTER` | `metadata.product_event_type` | If `[is_filter] == "true"`.  
`filter.actions.action` | `additional.fields` |   
`filter.actions.isFinal` | `security_result.detection_fields` |   
`filter.actions.module` | `additional.fields`,  
`security_result.detection_fields` |   
`filter.actions.rule` | `additional.fields`,  
`security_result.detection_fields` |   
`filter.disposition` | `security_result.action_details` | Extracted from a key-value pair in a `data` field. If `[filter_disposition] not in ["", "null", "None", "none", "NONE"]`.  
`filter.durationSecs` | `additional.fields` |   
`filter.isMsgEncrypted` | `additional.fields` |   
`filter.isMsgInDigest` | `additional.fields` |   
`filter.isMsgOnHold` | `additional.fields` |   
`filter.isMsgReinjected` | `additional.fields` |   
`filter.isMsgSplit` | `additional.fields` |   
`filter.langs` | `additional.fields` |   
`filter.modules.av.virusNames.0` | `security_result.threat_name` | Extracted from a key-value pair in a `data` field.  
`filter.modules.banner.insertedBanner` | `security_result.detection_fields` |   
`filter.modules.dkimv.domain` | `security_result.detection_fields` |   
`filter.modules.dkimv.result` | `security_result.detection_fields` |   
`filter.modules.dkimv.selector` | `security_result.detection_fields` |   
`filter.modules.dmarc.filterdResult` | `security_result.detection_fields` |   
`filter.modules.dmarc.isVerified` | `additional.fields` |   
`filter.modules.dmarc.srvid` | `additional.fields` |   
`filter.modules.pdr.v2.response` | `security_result.detection_fields` |   
`filter.modules.pdr.v2.rscore` | `additional.fields` |   
`filter.modules.spam.authority.analysis` | `additional.fields` |   
`filter.modules.spam.authority.cartVersion` | `additional.fields` |   
`filter.modules.spam.authority.isComplete` | `additional.fields` |   
`filter.modules.spam.authority.isTruncated` | `additional.fields` |   
`filter.modules.spam.authority.score` | `additional.fields` |   
`filter.modules.spam.classifiers.profile` | `additional.fields` |   
`filter.modules.spam.classifiers.status.clx` | `additional.fields` |   
`filter.modules.spam.classifiers.status.nostradamus` | `additional.fields` |   
`filter.modules.spam.classifiers.status.supernova` | `additional.fields` |   
`filter.modules.spam.classifiers.status.uribl` | `additional.fields` |   
`filter.modules.spam.scores.classifiers.adult` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.bulk` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.cot` | `additional.fields` |   
`filter.modules.spam.scores.classifiers.impostor` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.lowpriority` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.malware` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.mlx` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.mlxlog` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.phish` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.spam` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.suspect` | `security_result.detection_fields` |   
`filter.modules.spam.scores.classifiers.unknownsender` | `additional.fields` |   
`filter.modules.spam.scores.classifiers.unsafe` | `additional.fields` |   
`filter.modules.spam.scores.engine` | `security_result.detection_fields` |   
`filter.modules.spam.scores.overall` | `security_result.detection_fields` |   
`filter.modules.spam.triggeredClassifier` | `security_result.category_details` |   
`filter.modules.spam.version.definitions` | `security_result.summary` | Extracted from a key-value pair in a `data` field.  
`filter.modules.spam.version.engine` | `metadata.product_version` | Extracted from a key-value pair in a `data` field.  
`filter.modules.spf.domain` | `additional.fields` |   
`filter.modules.urldefense.counts.noRewriteIsEmail` | `additional.fields` |   
`filter.modules.urldefense.counts.noRewriteIsExcludedDomain` | `additional.fields` |   
`filter.modules.urldefense.counts.noRewriteIsSchemeless` | `additional.fields` |   
`filter.modules.urldefense.counts.noRewriteIsUnsupportedScheme` | `additional.fields` |   
`filter.modules.urldefense.counts.rewritten` | `additional.fields` |   
`filter.modules.urldefense.counts.total` | `security_result.detection_fields` |   
`filter.modules.urldefense.counts.unique` | `additional.fields` |   
`filter.modules.urldefense.counts.unrewritten` | `additional.fields` |   
`filter.modules.urldefense.version.engine` | `additional.fields` |   
`filter.modules.zerohour.score` | `additional.fields` |   
`filter.msgSizeBytes` | `network.received_bytes` | Extracted from a key-value pair in a `data` field.  
`filter.origGuid` | `additional.fields` |   
`filter.qid` | `additional.fields` |   
`filter.quarantine.expirationTs` | `security_result.detection_fields` |   
`filter.quarantine.folder` | `security_result.detection_fields` |   
`filter.quarantine.folderId` | `security_result.detection_fields` |   
`filter.quarantine.module` | `security_result.detection_fields` |   
`filter.quarantine.rule` | `security_result.detection_fields` |   
`filter.quarantine.type` | `security_result.detection_fields` |   
`filter.reinjectedType` | `additional.fields` |   
`filter.routes` | `additional.fields` |   
`filter.splitType` | `additional.fields` |   
`filter.startTime` | `metadata.event_timestamp` |   
`filter.suborgs.sender` | `additional.fields` |   
`from_hashed` | `additional.fields` |   
`fromadd` | `network.email.from` | Extracted from a key-value pair in a `data` field. If `[fromadd] =~ "^.+@.+$"`.  
`GUID` | `metadata.product_log_id` | Extracted from a `data` field.  
`guid` | `metadata.product_log_id` | Extracted from a `data` field.  
`headerfromHashedvalue` | `additional.fields` |   
`headertoHashedvalue` | `additional.fields` |   
`hostname` | `principal.asset.hostname`,  
`principal.hostname` | Extracted from a `message` field.  
`id` | `additional.fields` |   
`impostorScore` | `security_result.detection_fields` |   
`INBOUND` | `network.direction` | If `[rule] == "outbound"`, `[filter][routeDirection] == "inbound"`, or `[quarantineRule] =~ "outbound"`.  
`INFORMATIONAL` | `security_result.severity` | If `[audit][level] =~ "(?i)(notice)"`.  
`intermediary.ip` | `intermediary.asset.ip`,  
`intermediary.ip` |   
`intermediary.ip1` | `intermediary.asset.ip`,  
`intermediary.ip` |   
`intermediary_hostname` | `intermediary.asset.hostname`,  
`intermediary.hostname` | Extracted from a `data` field.  
`isArchive` | `additional.fields` |   
`isCorrupted` | `additional.fields` |   
`isDeleted` | `additional.fields` |   
`isProtected` | `additional.fields` |   
`isTimedOut` | `additional.fields` |   
`isVirtual` | `additional.fields` |   
`item.cluster` | `security_result.detection_fields` |   
`item.GUID` | `security_result.detection_fields` |   
`item.headerFrom` | `security_result.detection_fields` |   
`item.id` | `security_result.detection_fields` |   
`item.impostorScore` | `security_result.detection_fields` |   
`item.malwareScore` | `security_result.detection_fields` |   
`item.messageID` | `security_result.detection_fields` |   
`item.messageSize` | `security_result.detection_fields` |   
`item.modulesRun` | `additional.fields` |   
`item.phishScore` | `security_result.detection_fields` |   
`item.policyRoutes` | `additional.fields` |   
`item.QID` | `security_result.detection_fields` |   
`item.quarantineFolder` | `security_result.detection_fields` |   
`item.quarantineRule` | `security_result.detection_fields` |   
`item.sender` | `principal.user.email_addresses` | If `[item_sender] =~ "^.+@.+$"`.  
`item.senderIP` | `principal.asset.ip`,  
`principal.ip` |   
`item.spamScore` | `security_result.detection_fields` |   
`item.subject` | `network.email.subject` |   
`item.threats.classification` | `security_result.detection_fields` |   
`item.threats.threat` | `security_result.detection_fields` |   
`item.threats.threatID` | `security_result.detection_fields` |   
`item.threats.threatStatus` | `security_result.detection_fields` |   
`item.threats.threatTime` | `security_result.detection_fields` |   
`item.threats.threatType` | `security_result.detection_fields` |   
`item.threats.threatUrl` | `security_result.detection_fields` |   
`key.data` | `security_result.detection_fields` |   
`labeledCharset` | `additional.fields` |   
`labeledExt` | `additional.fields` |   
`labeledMime` | `about.file.mime_type` |   
`labeledName` | `about.file.full_path` |   
`malwareScore` | `security_result.detection_fields` |   
`matches.offset` | `additional.fields` |   
`matches.part` | `additional.fields` |   
`MEDIUM` | `security_result.severity` | If `[audit][level] =~ "(?i)(warn)"`.  
`messageID` | `network.email.mail_id` | Extracted from a `data` field.  
`messageSize` | `security_result.detection_fields` |   
`messageTime` | `metadata.event_timestamp` |   
`metadata.customerId` | `principal.resource.attribute.labels` |   
`metadata.origin.data.agent` | `network.http.parsed_user_agent`,  
`network.http.user_agent` | Extracted from a key-value pair in a `data` field.  
`metadata.origin.data.cid` | `additional.fields` |   
`metadata.origin.data.mode` | `additional.fields` |   
`metadata.origin.data.theater` | `additional.fields`,  
`principal.location.country_or_region` | `principal.location.country_or_region` is extracted from a key-value pair in a `data` field.  
`metadata.origin.data.version` | `metadata.product_version` | Extracted from a key-value pair in a `data` field.  
`metadata.origin.schemaVersion` | `additional.fields` |   
`mod` | `security_result.detection_fields` |   
`modulesRun` | `additional.fields` |   
`msg.header.cc` | `additional.fields` |   
`msg.header.from` | `additional.fields`,  
`principal.user.email_addresses` | `principal.user.email_addresses` is mapped to this field using a loop, with JSON array elements merged here, or non-JSON strings mapped here.  
`msg.header.message-id.0` | `additional.fields`,  
`network.email.mail_id` |   
`msg.header.reply-to.0` | `additional.fields`,  
`network.email.reply_to` |   
`msg.header.to` | `additional.fields`,  
`target.user.email_addresses` | `target.user.email_addresses` is mapped here as a non-JSON string using a loop.  
`msg.header.x-mailer` | `additional.fields` |   
`msg.lang` | `additional.fields` |   
`msg.normalizedHeader.from` | `principal.user.email_addresses` | Mapped to this field using a loop. JSON array elements are merged here; non-JSON strings are mapped here.  
`msg.normalizedHeader.subject` | `network.email.subject` | If `msg.normalizedHeader.subject` is not equal to `subject` raw log field value.  
`msg.normalizedHeader.to` | `target.user.email_addresses` | Mapped to this field using a loop. Non-JSON strings are mapped here.  
`msg.normalizedHeader.x-mailer` | `additional.fields` |   
`msg.parsedAddresses.from.0` | `additional.fields`,  
`network.email.from` |   
`msg.parsedAddresses.to` | `target.user.email_addresses` | Mapped to this field using a loop. Non-JSON string are mapped here.  
`msg.sizeBytes` | `additional.fields` |   
`msgBlocked.filename` | `about.file.full_path` |   
`msgBlocked.labeledMime` | `about.file.mime_type` |   
`msgBlocked.msgPart.detectedSizeBytes` | `about.file.size` |   
`msgBlocked.msgPart.md5` | `about.file.md5` |   
`msgheadersubject` | `additional.fields` |   
`msgheaderxmailervalue` | `additional.fields` |   
`msgPart.dataBase64` | `additional.fields` |   
`msgPart.detectedCharset` | `additional.fields` |   
`msgPart.detectedMime` | `additional.fields` |   
`msgPart.detectedSizeBytes` | `about.file.size` |   
`msgPart.filename` | `about.file.full_path` |   
`msgPart.md5` | `about.file.md5` |   
`msgPart.metadata.appversion` | `additional.fields` |   
`msgPart.metadata.codepage` | `additional.fields` |   
`msgPart.metadata.color-scheme` | `additional.fields` |   
`msgPart.metadata.content-language` | `additional.fields` |   
`msgPart.metadata.format-detection` | `additional.fields` |   
`msgPart.metadata.history[1]/stevt:action` | `additional.fields` |   
`msgPart.metadata.history[1]/stevt:softwareagent` | `additional.fields` |   
`msgPart.metadata.history[1]/stevt:when` | `additional.fields` |   
`msgPart.oContentType` | `additional.fields` |   
`msgPart.sha256` | `about.file.sha256` |   
`msgs.metadata._PROOFPOINT_CONTENT_LENGTH_` | `additional.fields` |   
`msgs.metadata.application` | `additional.fields` |   
`msgs.metadata.appname` | `additional.fields` |   
`msgs.metadata.author` | `security_result.detection_fields` |   
`msgs.metadata.company` | `security_result.detection_fields` |   
`msgs.metadata.createdate` | `additional.fields` |   
`msgs.metadata.documentid` | `additional.fields` |   
`msgs.metadata.instanceid` | `additional.fields` |   
`msgs.metadata.modifydate` | `additional.fields` |   
`msgs.metadata.pagecount` | `additional.fields` |   
`msgs.metadata.subject` | `additional.fields` |   
`msgs.metadata.title` | `additional.fields` |   
`msgs.textExtracted` | `additional.fields` |   
`msgUrls.url` | `additional.fields`,  
`security_result.detection_fields` |   
`normalizedHeader.x_originating_ip` | `principal.asset.ip`,  
`principal.ip` |   
`normalizedHeaderfromHashed` | `additional.fields` |   
`normalizedHeaderHashedvalue` | `additional.fields` |   
`normalizedHeaderMessageidvalue` | `additional.fields` |   
`normalizedheaderreplytohashed` | `additional.fields` |   
`normalizedheaderreturnpath` | `additional.fields` |   
`oContentType` | `additional.fields` |   
`OUTBOUND` | `network.direction` | If `[rule] == "outbound"`, `[filter][routeDirection] == "outbound"`, or `[quarantineRule] =~ "outbound"`.  
`parsed.useragent` | `network.http.parsed_user_agent` |   
`parsed_stat_value` | `security_result.detection_fields` |   
`parsedAddress` | `network.email.cc` | If `[parsedAddress] =~ "^.+@.+$"`.  
`parsedAddressesfromHashedvalue` | `additional.fields` |   
`parsedaddressesreplytohashed` | `additional.fields` |   
`parsedAddrestoHashedvalue` | `additional.fields` |   
`phishScore` | `security_result.detection_fields` |   
`pid` | `principal.process.pid` | Extracted from a `message` field.  
`PoD` | `metadata.product_name` | Static assignment.  
`policy_route.*` | `additional.fields` | `[list_values]` / used map function.  
`policyRoutes` | `additional.fields` |   
`pps.agent` | `observer.hostname` |   
`prod_event_name` | `metadata.product_event_type` | Extracted from a `message` field.  
`Proofpoint` | `metadata.vendor_name` | Static assignment.  
`QID` | `security_result.detection_fields` |   
`QUARANTINE` | `security_result.action` | If `[filter][disposition] == "quarantine"`.  
`quarantineFolder` | `security_result.detection_fields` |   
`quarantineRule` | `security_result.detection_fields` |   
`queryEndTime` | `metadata.collected_timestamp` |   
`rcd.error` | `additional.fields` |   
`rcd.record` | `additional.fields` |   
`rcpt` | `additional.fields`,  
`security_result.detection_fields` |   
`rcpt_hashed` | `additional.fields` |   
`reply` | `network.email.reply_to` | Extracted from a key-value pair in a `data` field. If `[reply] =~ "^.+@.+$"`.  
`replytohashed` | `additional.fields` |   
`res.emailIdentities.header.from` | `additional.fields` |   
`res.emailIdentities.smtp.mailfrom` | `additional.fields` |   
`res.emailIdentities.smtp.mailfromHashed` | `additional.fields` |   
`res.method` | `additional.fields` |   
`res.propspec.header.d` | `additional.fields` |   
`res.propspec.header.s` | `additional.fields` |   
`rules.name` | `additional.fields` |   
`rules.severity` | `additional.fields` |   
`s` | `network.session_id` | Extracted from a `data` field.  
`safeBlockedListMatches_listType` | `security_result.detection_fields` |   
`safeBlockedListMatchesvalue.listType` | `security_result.detection_fields` |   
`safeBlockedListMatchesvalue.rule` | `security_result.detection_fields` |   
`sandbox.status` | `additional.fields` |   
`sec_result_action` | `security_result.action` |   
`sec_result_category` | `security_result.category` |   
`sender` | `principal.user.email_addresses` | If `[sender] =~ "^.+@.+$"`.  
`senderIP` | `principal.asset.ip`,  
`principal.ip` |   
`SENDMAIL` | `metadata.product_event_type` | If `[message] =~ "sendmail"`.  
`sendmail_hostname` | `principal.asset.hostname`,  
`principal.hostname` | Extracted from a `data` field.  
`sendmail_process_name` | `principal.process.file.full_path` | Extracted from a `data` field.  
`sendmail_qid` | `additional.fields` |   
`sendmail_ts` | `metadata.collected_timestamp` | Extracted from a `data` field.  
`sig.engine` | `security_result.detection_fields` |   
`sig.isPresent` | `security_result.detection_fields` |   
`sig.signature` | `security_result.detection_fields` |   
`sizeDecodedBytes` | `additional.fields` |   
`sm.daemon` | `additional.fields` |   
`sm.delay` | `additional.fields` |   
`sm.dsn` | `additional.fields` |   
`sm.from` | `network.email.from` | Extracted from a key-value pair in a `data` field. If `[email_src] =~ "^.+@.+$"`.  
`sm.guid` | `metadata.product_log_id` | Extracted from a key-value pair in a `data` field. If `[message] =~ "sendmail"`.  
`sm.mailer` | `additional.fields` |   
`sm.messageTs` | `additional.fields` |   
`sm.msgid` | `network.email.mail_id` | Extracted from a key-value pair in a `data` field.  
`sm.nrcpts` | `additional.fields` |   
`sm.pri` | `additional.fields` |   
`sm.qid` | `security_result.detection_fields` |   
`sm.stat` | `security_result.description` | Extracted from a key-value pair in a `data` field.  
`sm.xdelay` | `additional.fields` |   
`smtoemail` | `network.email.to` | If `[sm_to_email] =~ "^.+@.+$"`.  
`spamScore` | `security_result.detection_fields` |   
`SpamType` | `security_result.detection_fields` |   
`subject` | `network.email.subject` |   
`suborgs` | `additional.fields` |   
`threat` | `security_result.detection_fields` |   
`threatType` | `security_result.detection_fields` |   
`tls.verify` | `security_result.action_details` | Extracted from a key-value pair in a `data` field. If `[tls_verify] not in ["", "null", "None", "none", "NONE"]`.  
`to` | `network.email.to` | If `[to] =~ "^.+@.+$"`.  
`ts` | `metadata.event_timestamp` |   
`uinteger` | `network.received_bytes`,  
`network.sent_bytes` |   
`UNKNOWN_ACTION` | `security_result.action` | If `[filter][disposition] in ["hold", "retry"]`.  
`UNKNOWN_SEVERITY` | `security_result.severity` |   
`urlsource` | `security_result.detection_fields` |   
`value` | `additional.fields` |   
`x_originating_ip` | `principal.asset.ip`,  
`principal.ip` |   
  
## UDM mapping delta reference

On October 13, 2026, Google SecOps released a new version of the Proofpoint On-Demand parser, which includes significant changes to the mapping of Proofpoint On-Demand log fields to UDM fields and updates to event type classifications (mappings).

### Log-field mapping delta

The following table shows the changes to how Proofpoint On-Demand log fields are mapped to UDM fields. The **Old mapping** column lists the fields exposed prior to October 13, 2026, and the **Current mapping** column lists the new fields.

Log field | Old mapping | Current mapping  
---|---|---  
`connection.sid` | `additional.fields` | `security_result.detection_fields`  
`filter.modules.pdr.v2.response` | `additional.fields` | `security_result.detection_fields`  
`filter.modules.urldefense.counts.total` | `additional.fields` | `security_result.detection_fields`  
`filter.quarantine.expirationTs` | `additional.fields` | `security_result.detection_fields`  
`filter.quarantine.folder` | `additional.fields` | `security_result.detection_fields`  
`filter.quarantine.folderId` | `additional.fields` | `security_result.detection_fields`  
`filter.quarantine.module` | `additional.fields` | `security_result.detection_fields`  
`filter.quarantine.rule` | `additional.fields` | `security_result.detection_fields`  
`filter.quarantine.type` | `additional.fields` | `security_result.detection_fields`  
`messageTime` | `additional.fields` | `metadata.event_timestamp`  
`messagesBlocked.spamScore` | `additional.fields` | `security_result.detection_fields`  
`metadata.customerId` | `additional.fields` | `principal.resource.attribute.labelsmod`  
`msgParts.detectedSizeBytes` | `additional.fields` | `about.file.size`  
`msg_header_from_json_array.value` | `additional.fields` | `principal.user.email_addresses`  
`principal.resource.attribute.labelsmod` | `additional.fields` | `security_result.detection_fields`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-on-demand-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
