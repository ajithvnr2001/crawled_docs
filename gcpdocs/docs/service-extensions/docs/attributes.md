---
url: https://docs.cloud.google.com/service-extensions/docs/attributes/
title: Supported attributes \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:25:13.178357+00:00
---

# Supported attributes  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Reference ](https://docs.cloud.google.com/service-extensions/docs/apis)



Send feedback 

#  Supported attributes Stay organized with collections  Save and categorize content based on your preferences. 

When configuring extensions by using plugins or callouts, you can specify the request and connection attributes to forward to extension services. This page describes the supported attributes and identifies the ones that are available for each extension type.

By configuring extensions to forward specific attributes, you can achieve the following:

  * Make dynamic routing decisions.
  * Enrich request headers with client information.
  * Implement custom security policies based on client location or TLS parameters.
  * Generate detailed custom logs.



You can specify attributes with the `forwardAttributes` field in the YAML configuration for plugin and callout extensions. For example, for traffic extensions, see [Configure a traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions).

Specify attributes with `forwardAttributes` for the following types of extensions:

  * Cloud Load Balancing edge extensions (`LbEdgeExtension`) on global external Application Load Balancers
  * Cloud Load Balancing route and traffic extensions (`LbRouteExtension`, `LbTrafficExtension`) on Application Load Balancers
  * Authorization extensions (`AuthzExtension`) using `ext_proc` on Application Load Balancers
  * Media CDN edge extensions (`CdnEdgeExtension`) on Media CDN Edge Cache services



## Request attributes

You can extract and forward the following attributes from requests:

Attribute | Type | `LbEdge` | `LbRoute` | `LbTraffic` | `Authz` | `CdnEdge` | Description and behavioral differences  
---|---|---|---|---|---|---|---  
`request.method` | string | ✓ | ✓ | ✓ | ✓ | ✓ | The HTTP request method, such as `GET` or `POST`.  
`request.host` | string | ✓ | ✓ | ✓ | ✓ | ✓ | A convenience equivalent to `request.headers['host']`.  
`request.path` | string | ✓ | ✓ | ✓ | ✓ | ✓ | The requested HTTP URL path.  
`request.query` | string | ✓ | ✓ | ✓ | ✓ | ✓ | The HTTP URL query in the format `name1=value&name2=value2`.  
`request.scheme` | string | ✓ | ✓ | ✓ | ✓ | ✓ | The HTTP URL scheme (`http` or `https`). Values are in lowercase.  
`request.origin` | string | — | — | ✓ | ✓ | — | The value of the `Origin` request header for Cross-Origin Resource Sharing (CORS) use cases.  
`request.user_agent_family` | string | ✓ | — | ✓ | — | — | The parsed user-agent family string. Supported only on global external Application Load Balancers.  
`request.device_request_type` | string | ✓ | — | ✓ | — | — | The device classification category. Supported only on global external Application Load Balancers.  
`request.backend_service_name` | string | — | — | ✓ | ✓ | — | The target backend service. Not applicable to edge extensions (`LbEdgeExtension` or `CdnEdgeExtension`).  
`request.backend_service_project_number` | int | — | — | ✓ | ✓ | — | The project number of the backend service in Shared VPC. Not applicable to edge extensions.  
`request.mcp_method` | string | — | — | — | ✓ | — | The Model Context Protocol (MCP) method name.  
  
## Connection attributes

You can extract and forward the following attributes from connections: 

Attribute | Type | `LbEdge` | `LbRoute` | `LbTraffic` | `Authz` | `CdnEdge` | Description and behavioral differences  
---|---|---|---|---|---|---|---  
`source.ip` | string | ✓ | ✓ | ✓ | ✓ | — | The client IP address.  
`source.port` | int | ✓ | ✓ | ✓ | ✓ | ✓ | The client source port number.  
`source.client_region` | string | ✓ | — | ✓ | — | ✓ | The two-letter ISO-3166-1 or CLDR region code associated with the client IP address (for example, `US` or `DE`).  
`source.client_region_subdivision` | string | ✓ | — | ✓ | — | — | The region subdivision code, such as for a state or province. Supported only on global external Application Load Balancers.  
`source.client_city` | string | ✓ | — | ✓ | — | — | The city associated with the client IP address. Supported only on global external Application Load Balancers.  
`source.client_city_lat_long` | string | ✓ | — | ✓ | — | — | The latitude and longitude associated with the client city. Supported only on global external Application Load Balancers.  
`destination.ip` | string | — | — | ✓ | ✓ | — | The IP address of the load balancer that the client connects to.  
`destination.port` | int | — | — | ✓ | ✓ | — | The destination port number that the client connects to.  
`connection.client_encrypted` | bool | — | — | ✓ | ✓ | — | The value is `true` if the connection between the client and the load balancer is encrypted (using `HTTPS`, `HTTP/2`, or `HTTP/3`); otherwise, `false`.  
`connection.protocol` | string | — | — | ✓ | ✓ | — | The HTTP protocol used for communication (`HTTP/1.0`, `HTTP/1.1`, `HTTP/2`, or `HTTP/3`).  
`connection.sni` | string | ✓ | — | ✓ | ✓ | ✓ | The requested Server Name Indication (SNI) of the downstream TLS connection.  
`connection.tls_version` | string | ✓ | — | ✓ | ✓ | ✓ | The TLS version negotiated with the client (`TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, or `QUIC`).  
`connection.tls_cipher_suite` | string | — | — | ✓ | ✓ | — | The four-digit hexadecimal cipher suite negotiated during the TLS handshake—for example, `009C`.  
`connection.tls_ja3_fingerprint` | string | — | — | ✓ | — | — | The JA3 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2, or HTTP/3.  
`connection.tls_ja4_fingerprint` | string | ✓ | — | ✓ | — | — | The JA4 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2, or HTTP/3.  
`connection.client_rtt_msec` | int | — | — | ✓ | ✓ | — | The client round-trip time (RTT) measured in milliseconds.  
`connection.sha256_peer_certificate_digest` | string | ✓ | — | ✓ | ✓ | — | The hex-encoded SHA-256 peer certificate hash.  
`connection.client_cert_present` | bool | — | — | ✓ | ✓ | — | The value is `true` if the client provided a certificate during the TLS handshake; otherwise, `false`.  
`connection.client_cert_chain_verified` | bool | — | — | ✓ | ✓ | — | The value is `true` if the client certificate chain is verified against a configured `TrustStore`; otherwise, `false`.  
`connection.client_cert_error` | string | — | — | ✓ | ✓ | — | Predefined strings representing mTLS error conditions. For more information, see [mTLS client validation modes](https://docs.cloud.google.com/load-balancing/docs/mtls#mtls_errors).  
`connection.client_cert_serial_number` | string | — | — | ✓ | ✓ | — | The serial number of the client certificate.  
`connection.client_cert_spiffe_id` | string | — | — | ✓ | ✓ | — | The SPIFFE ID from the Subject Alternative Name (SAN) field.  
`connection.client_cert_uri_sans` | string | — | — | ✓ | ✓ | — | A comma-separated, Base64-encoded list of URI SAN extensions extracted from the client certificate.  
`connection.client_cert_dnsname_sans` | string | — | — | ✓ | ✓ | — | A comma-separated, Base64-encoded list of DNSName SAN extensions extracted from the client certificate.  
`connection.client_cert_valid_not_before` | string | — | — | ✓ | ✓ | — | The timestamp (RFC 3339 format) before which the client certificate is not valid.  
`connection.client_cert_valid_not_after` | string | — | — | ✓ | ✓ | — | The timestamp (RFC 3339 format) after which the client certificate is not valid.  
`connection.client_cert_issuer_dn` | string | — | — | ✓ | ✓ | — | The Base64-encoded DER encoding of the certificate `Issuer` field.  
`connection.client_cert_subject_dn` | string | — | — | ✓ | ✓ | — | The Base64-encoded DER encoding of the certificate `Subject` field.  
`connection.client_cert_leaf` | string | — | — | ✓ | ✓ | — | The Base64-encoded client leaf certificate for an established, validated mTLS connection (RFC 9440).  
`connection.client_cert_chain` | string | — | — | ✓ | ✓ | — | The comma-delimited, Base64-encoded client certificate chain in standard TLS order, excluding the leaf certificate (RFC 9440).  
  
## Limitations

  * **Attribute availability** : not all attributes are supported for all extension types. For more information, see the table on this page.

  * **Required configuration** : to send attributes to the extension, you must explicitly list the attributes in the `forwardAttributes` field of your extension configuration. If you don't list an attribute in this field, then the load balancer or Media CDN doesn't forward that specific attribute to your extension.

  * **Size limits** : you can configure a maximum of 16 attributes for a single extension.

  * **mTLS attributes** : client certificate attributes (`connection.client_cert_*`) are populated in the data passed to your extension only if you have enabled mTLS and the client presents a certificate.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
