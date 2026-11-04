---
url: https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:39.494355+00:00
---

# Security bulletins  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes security bulletins related to Apigee.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://cloud.google.com/feeds/apigee-security-bulletins.xml`



## GCP-2026-077

**Published:** 2026-11-03

### Description

Description | Severity | Notes  
---|---|---  
Following the private-key compromise of intermediate Certificate Authorities (CAs) associated with eMudhra (emSign), outbound TLS connections trusting affected roots—specifically `emSign ECC Root CA - G3`—are vulnerable to Man-in-the-Middle (MITM) interception. An attacker possessing compromised intermediate keys can issue fraudulent TLS certificates for arbitrary domain names. Outbound HTTPS connections made from Apigee runtimes (such as TargetEndpoints, TargetServers, ServiceCallouts, and outbound JWKS policy lookups) using default or unmanaged system trust stores may accept forged certificates. This security bulletin outlines required remediation steps for Apigee X, Apigee Hybrid, Apigee Edge (SaaS), and Apigee Edge for Private Cloud (OPDK).

#### Impact of remediation

Moving forward, outbound connections to endpoints using certificates signed by compromised roots will be blocked unless a custom trust store is configured in your outbound setup. Disruption of outbound connectivity resulting from the security revocation of compromised third-party certificates or customer trust store configurations does not constitute Google Cloud service downtime under applicable Service Level Agreements (SLAs).

#### Affected products and versions

  * For all Apigee products, you must review your custom TrustStores (in TargetEndpoint, TargetServer, or ServiceCallout configurations).

| Product | Status / Action Required  
---|---  
Apigee Edge (SaaS) | Patch in progress / No customer action required for platform defaults. Customers must review custom TrustStores to ensure compromised roots are not part of the trust chain and consider adding a custom TrustStore if one does not exist to mitigate target server connections.  
Apigee Edge for Private Cloud (OPDK) |  Manual remediation required (Update OS CA trust store, sanitize Java truststores, restart Apigee services). Customers must review custom TrustStores to ensure compromised roots are not part of the trust chain and consider adding a custom TrustStore if one does not exist to mitigate target server connections.  
Apigee X | Patch in progress / No customer action required for platform defaults. Customers must review custom TrustStores to ensure compromised roots are not part of the trust chain and consider adding a custom TrustStore if one does not exist to mitigate target server connections.  
Apigee Hybrid | Upgrade to patched Apigee Hybrid containers once released. Customers must review custom TrustStores to ensure compromised roots are not part of the trust chain and consider adding a custom TrustStore if one does not exist to mitigate target server connections.  
  
#### What should I do?

**Important:** The remediation steps and commands provided herein are for guidance purposes only. Customers are solely responsible for testing modifications in a non-production environment and taking complete backups of keystores, trust stores, and system configurations prior to execution. Google provides these instructions "as-is" without warranty of any kind.

##### Apigee X

Google Cloud is conducting a rollout across Apigee X infrastructure to remediate affected trust stores and Go toolchains.

**Customer Action Required:** Automated platform rollout handles control plane and runtime containers. Customers must review custom TrustStores in TargetEndpoint or TargetServer configurations to ensure compromised emSign or AAA Certificate Services certificates are not explicitly trusted. To verify trust store compliance, see Apigee X/Hybrid: Review and Update Custom TrustStores (eMudhra CA Compromise).

##### Apigee Hybrid

Apigee Hybrid containers do not bind-mount host OS certificate stores and use isolated trust stores baked into image builds; customers must upgrade to patched container images once released:

  * **Custom TrustStores Audit & Configuration:** Inspect custom TargetServer, TargetEndpoint, and ServiceCallout TrustStores for compromised emSign or AAA Certificate Services intermediate/root certificates, and update them accordingly. To verify trust store compliance, see Apigee X/Hybrid: Review and Update Custom TrustStores (eMudhra CA Compromise).



##### Apigee Edge (SaaS)

Google Cloud is applying automated platform updates across all Apigee Edge infrastructure to remove compromised eMudhra and AAA Certificate Services root and intermediate certificates from system keystores.

**Customer Action Required:** Automated platform rollout handles system trust stores. Customers must review custom TrustStores in TargetEndpoint or TargetServer settings to ensure compromised emSign or AAA Certificate Services certificates are not explicitly trusted. To review or create trust stores, see [Creating keystores and truststores using the Edge UI](https://docs.apigee.com/api-platform/system-administration/creating-keystores-and-truststore-cloud-using-edge-ui).

##### Apigee Edge for Private Cloud (OPDK)

Customers hosting Apigee Edge on-premises or in private cloud infrastructure (OPDK) must update their system environment, sanitize Java keystores, and perform a host/service reload across all cluster nodes.

###### Phase 1: Update the Host OS CA Certificate Store

For Red Hat Enterprise Linux / CentOS / Rocky Linux:
    
    
    sudo yum update -y ca-certificates
    sudo update-ca-trust extract
    

###### Phase 2: Sanitize FIPS JVM TrustStores

1\. If you're FIPS-enabled and still use the shipped BCFKS store, set up your own first: after Phase 1, follow Option A in [Default Java keystore/truststore](https://docs.apigee.com/private-cloud/v4.53.01/fips-considerations-rhel-8#default-java-keystoretruststore) on the FIPS page. Then run the commands below against your store to confirm neither root is in it, and delete any that are. Don't edit the shipped store; Edge updates replace it.
    
    
    # Path and password for the BCFKS truststore configured in /opt/apigee/customer/application/COMPONENT.properties:
    BCFKS_PATH="/opt/apigee/customer/application/my-cacerts.bcfks"
    BCFKS_PASS="YOUR_STORE_PASSWORD"
    # Automatically resolve the bc-fips jar version
    BC_FIPS_JAR=$(ls /opt/apigee/edge-gateway/lib/thirdparty/bc-fips-*.jar | head -n 1)
    # 1. Inspect and identify the exact alias names in the BCFKS store
    keytool -J-Dcom.redhat.fips=false -list \
      -keystore "$BCFKS_PATH" \
      -storetype BCFKS \
      -storepass "$BCFKS_PASS" \
      -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
      -providername BCFIPS \
      -providerpath "$BC_FIPS_JAR" | grep -i -E "emudhra|emsign|aaa certificate|comodo"
    # 2. Delete the compromised aliases (replace with the exact case-sensitive alias names from step 1)
    sudo keytool -J-Dcom.redhat.fips=false -delete \
      -alias "emsigneccrootca-g3" \
      -keystore "$BCFKS_PATH" \
      -storetype BCFKS \
      -storepass "$BCFKS_PASS" \
      -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
      -providername BCFIPS \
      -providerpath "$BC_FIPS_JAR"
    sudo keytool -J-Dcom.redhat.fips=false -delete \
      -alias "comodoaaaservicesroot" \
      -keystore "$BCFKS_PATH" \
      -storetype BCFKS \
      -storepass "$BCFKS_PASS" \
      -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
      -providername BCFIPS \
      -providerpath "$BC_FIPS_JAR"
    # 3. Ensure file ownership remains apigee:apigee (since sudo was used)
    sudo chown apigee:apigee "$BCFKS_PATH"
    

2\. Audit and Create Custom Target Server TrustStores: Review all custom TrustStores referenced by TargetEndpoint, TargetServer, or ServiceCallout TLS configurations and remove eMudhra/emSign or AAA Certificate Services certificates. If no custom TrustStore is used for outbound TLS, create and assign one to enforce explicit server certificate verification. For step-by-step guidance, see [Creating keystores and truststores using the Edge UI](https://docs.apigee.com/api-platform/system-administration/creating-keystores-and-truststore-cloud-using-edge-ui).

###### Phase 3: Restart Apigee Edge Services

Perform a rolling reboot of all Apigee Edge nodes:
    
    
    /opt/apigee/apigee-service/bin/apigee-all stop
    /opt/apigee/apigee-service/bin/apigee-all start
    

#### Detection

Verify OS Trust Bundle:
    
    
    grep -i "emSign ECC Root CA - G3" /etc/pki/tls/certs/ca-bundle.crt
    

##### Step-by-Step Remediation Validation & Keystore Configuration

  * **Step 1 (Validate OS & JVM Trust Stores):** Execute the verification commands above to ensure affected CA certificates (such as `emSign ECC Root CA - G3`) are purged from system and JVM trust bundles.
  * **Step 2 (Audit Existing Keystores/Truststores):** Use the Apigee Management API or UI to audit all existing Keystores and Truststores in your environment. Verify that no revoked or compromised intermediate/root certificates exist within your `SSLInfo` definitions.
  * **Step 3 (Create & Update Custom Truststores):** If your outbound target configurations rely on default or system-wide trust stores, create a new custom TrustStore and upload only validated CA chains. Update your TargetEndpoint, TargetServer, or ServiceCallout `SSLInfo` configuration to reference the new TrustStore. For details, see [Creating keystores and truststores](https://docs.apigee.com/api-platform/system-administration/creating-keystores-and-truststore-cloud-using-edge-ui).
  * **Step 4 (Test Target Connections):** Deploy updated API proxy revisions and test outbound connectivity to target backends to verify mTLS and TLS handshakes succeed without relying on system-wide trust stores.



#### Apigee X/Hybrid: Review and Update Custom TrustStores (eMudhra CA Compromise)

Following the compromise of intermediate Certificate Authorities associated with eMudhra (emSign) and cross-signed roots from Comodo AAA Certificate Services, Google Cloud is automatically updating Apigee X runtime and control plane platform trust bundles and releasing new versions of Apigee Hybrid.

However, if your Apigee X or Apigee Hybrid API proxies use custom TrustStores in TargetEndpoint, TargetServer, or ServiceCallout configurations, you must manually inspect those TrustStores to ensure affected certificates are removed.

##### Step 1: Identify if Custom TrustStores are in Use

Custom TrustStores are configured at the environment level and referenced in your outbound TLS configurations.

  * **TargetEndpoint or ServiceCallout:** Check if your proxy configuration specifies a `<TrustStore>` inside `<SSLInfo>`: 
    * If `<TrustStore>` is present (for example, `<TrustStore>my-truststore</TrustStore>` or `<TrustStore>ref://myTrustStoreRef</TrustStore>`), a custom TrustStore is used.
    * If `<TrustStore>` is omitted and only `<Enabled>true</Enabled>` is set, the proxy uses the platform default CA bundle. On Apigee X, Google Cloud updates it automatically. On Apigee Hybrid, the bundle is baked into the container images; see the Apigee Hybrid steps above.
  * **TargetServer:** Inspect your TargetServers in each environment to check if `sSLInfo.trustStore` is set.



##### Step 2: Inspect Certificates in Your TrustStores

Review the certificates contained in each custom TrustStore across your Apigee environments using either the Google Cloud console or the Apigee REST API.

###### Option A: Using the Google Cloud console

  1. In the Google Cloud console, navigate to **Apigee** > **Management** > **Environments**.
  2. Select an environment.
  3. Click the **TLS Keystores** (or **Keystores**) tab.
  4. Click each TrustStore to expand and view the uploaded certificates.
  5. Review the **Subject** , **Issuer** , and **Alias** of each certificate.



###### Option B: Using the Apigee REST API

  1. List all keystores in the environment: 
         
         curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
           "https://apigee.googleapis.com/v1/organizations/ORGANIZATION/environments/ENVIRONMENT/keystores"
         

  2. List all certificates inside the keystore: 
         
         curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
           "https://apigee.googleapis.com/v1/organizations/ORGANIZATION/environments/ENVIRONMENT/keystores/KEYSTORE/aliases"
         

  3. Retrieve certificate details: 
         
         curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
           "https://apigee.googleapis.com/v1/organizations/ORGANIZATION/environments/ENVIRONMENT/keystores/KEYSTORE/aliases/CERT_ALIAS"
         




##### Step 3: Identify Affected Certificates

Check if any certificate in your TrustStore matches the affected CA authorities:

  * **eMudhra Roots:**
    * Common Name (CN): `emSign ECC Root CA - G3`, `emSign Root TLS CA - G3`, `emSign Root CA - G1`, `emSign Root CA - G2`, `emSign Root CA - C1`, or `emSign ECC Root CA - C3`
    * Organization (O): `eMudhra Technologies Limited` or `eMudhra Inc`
    * SHA-256 Fingerprint for `emSign ECC Root CA - G3`: `86:A1:EC:BA:08:9C:4A:8D:3B:BE:27:34:C6:12:BA:34:1D:81:3E:04:3C:F9:E8:A8:62:CD:5C:57:A3:6B:BE:6B`
    * SHA-256 Fingerprint for `emSign Root TLS CA - G3`: `7D:D7:8D:5F:4F:13:45:9A:83:DF:F9:AB:BB:A6:2E:DB:AF:6F:2D:10:2B:F2:57:FD:71:2F:4D:9F:27:46:ED:8D`
  * **Cross-Signing Root (AAA Certificate Services):**
    * Common Name (CN): `AAA Certificate Services`
    * Organization (O): `Comodo CA Limited`
    * SHA-256 Fingerprint for `AAA Certificate Services`: `D7:A7:A0:FB:5D:7E:27:31:D7:71:E9:48:4E:BC:DE:F7:1D:5F:0C:3E:0A:29:48:78:2B:C8:3E:E0:EA:69:9E:F4`
  * **eMudhra Compromised Intermediate CAs:**
    * Common Name (CN): `EM DV TLS CA - G3B`, `EM DV TLS CA - G3C`, `EM OV TLS CA - G3B`, `EM OV TLS CA - G3C`, `EM EV TLS CA - G3B`, `EM EV TLS CA - G3C`, `EM OV CS CA - G3B`, or `EM OV CS CA - G3C`



##### Step 4: Verify Target Backend Server Certificates

Before removing CA certificates from your TrustStore, verify that your backend servers are not actively using certificates issued by eMudhra:

  1. Test the TLS certificate of your backend target server using OpenSSL: 
         
         echo | openssl s_client -connect BACKEND_HOST:443 -servername BACKEND_HOST -showcerts 2>/dev/null \
           | openssl x509 -noout -subject -issuer
         

  2. Verify the issuer: 
     * **If the issuer indicates`emSign` or `eMudhra`:** Your backend server is using a certificate from the compromised CA. You must replace and reissue the certificate from a trusted public CA (such as Google Trust Services, Let's Encrypt, or DigiCert) immediately.
     * **If the issuer is another CA:** Your backend certificate doesn't need replacing. You still need to remove the affected roots from your TrustStore in Step 5.



##### Step 5: Remove Distrusted Certificates from the TrustStore

After verifying your target backend servers, remove any affected certificates from your Apigee TrustStore.

###### Option A: Using the Google Cloud console

  1. In the Google Cloud console, navigate to **Apigee** > **Management** > **Environments** > **ENVIRONMENT** > **TLS Keystores**.
  2. Select your TrustStore.
  3. Locate the certificate alias for the affected certificate.
  4. Click the **Delete** icon (trash can) next to the certificate.
  5. Confirm deletion.



###### Option B: Using the Apigee REST API

Delete the certificate by alias:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://apigee.googleapis.com/v1/organizations/ORGANIZATION/environments/ENVIRONMENT/keystores/KEYSTORE/aliases/CERT_ALIAS"
    

**Note:** If your API proxies use a KeyStore Reference (`ref://myTrustStoreRef`), changes to the TrustStore take effect without proxy redeployment. If a proxy references the TrustStore by direct name, redeploy the proxy to ensure the updated TLS context is loaded.

#### Vulnerability Details

Vulnerability Type: MITM / CA Compromise (CVE-2026-111943)

#### References

For technical assistance or questions regarding custom TrustStore updates in Apigee Edge for Private Cloud, contact Cloud Customer Care or submit a ticket through the standard Apigee Support Portal.

Additional Details:

  * [CVE-2026-91403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-91403)
  * [CVE-2026-111943](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943)

Medium |  [CVE-2026-111943](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-111943)  
[CVE-2026-91403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-91403)  
  
## GCP-2026-072

**Published:** 2026-10-24

### Description

Description | Severity | Notes  
---|---|---  
Two vulnerabilities in PHP core, CVE-2026-109618 and CVE-2026-109619 ("PHP2Shell"), allow an unauthenticated attacker to execute code remotely on a server running a vulnerable PHP version. They are fixed in PHP 8.2.35, 8.3.36, 8.4.27, and 8.5.12. No fixed release exists for PHP 8.1 or earlier. Apigee, Apigee Hybrid, Apigee Edge for Public Cloud, API hub, and the Apigee integrated portal don't use PHP and aren't affected. Apigee Edge for Private Cloud isn't affected, apart from its optional Drupal developer portal, covered later in this bulletin. The impact is limited to Drupal-based Apigee developer portals, which customers deploy and operate. Updating the Apigee Drupal modules doesn't fix these vulnerabilities; only updating PHP does. The latest module releases (`apigee_edge` 3.1.2 and 4.1.2, `apigee_m10n` 2.2.1, `apigee_api_catalog` 3.1.1) require a fixed PHP version, so update PHP first.

#### Affected products

  * Apigee Developer Portal Kickstart from Google Cloud Marketplace
  * Apigee Developer Portal Kickstart Docker image (`ghcr.io/apigee/docker-apigee-drupal-kickstart`)
  * Self-hosted Drupal 10 and Drupal 11 developer portals built with Apigee Developer Portal Kickstart or the Apigee Edge Drupal module
  * Apigee Edge for Private Cloud Drupal 7 and Drupal 9 developer portals (all versions)
  * Apigee Edge for Public Cloud Drupal 7 developer portals that customers have hosted themselves since Apigee ended portal hosting on 2020-05-31



#### What should I do?

##### Apigee Developer Portal Kickstart from Google Cloud Marketplace

New deployments from Google Cloud Marketplace use a patched image with PHP 8.3.36. Existing deployments aren't updated automatically: patch the running VMs, then update the image. Step 1 - Patch the running VMs now. Your site, database, and files stay where they are. On each existing portal VM, run:
    
    
    sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -o Dpkg::Options::=--force-confold
    sudo supervisorctl restart php-fpm
    sudo supervisorctl status php-fpm
    sudo php-fpm8.3 -v
    

Confirm that php-fpm shows as RUNNING with a short uptime and that the last command reports PHP 8.3.36. Restart PHP-FPM with `supervisorctl`, not `systemctl`. Step 2 - Move the instance group to the patched image, so VMs the group creates later are also patched. A Marketplace portal runs in a regional managed instance group with autoscaling and autohealing; a VM the group creates later boots from the instance template's image, which `startup.sh` doesn't upgrade. The database is in Cloud SQL and the files are on Filestore, so replacing the VMs keeps your site. In the following commands, replace DEPLOYMENT with your deployment name and REGION with its region.

  * Find the image the group uses: `gcloud compute instance-groups managed describe DEPLOYMENT-igm --region REGION --format='value(versions[0].instanceTemplate)'`, then run `gcloud compute instance-templates describe TEMPLATE --format='value(properties.disks[0].initializeParams.sourceImage)'`, where TEMPLATE is the output of the first command.
  * If the image ends in `images/apigee-devportal-drupal` with no date, that name now points to the patched image and no template change is needed. Optionally, replace the VMs so that they boot from the patched image: `gcloud compute instance-groups managed rolling-action replace DEPLOYMENT-igm --region REGION --max-unavailable=0`.
  * If the image name includes a date, check it. `apigee-devportal-drupal-202610231240` and later images are patched and need no template change. Older images (for example `apigee-devportal-drupal-202610060628`) are vulnerable. In the Google Cloud console, open the current instance template, click **Create similar** , set the boot disk image to `projects/bap-marketplace/global/images/apigee-devportal-drupal`, and save the new template as NEW_TEMPLATE. Then run `gcloud compute instance-groups managed rolling-action start-update DEPLOYMENT-igm --version=template=NEW_TEMPLATE --region REGION --max-unavailable=0`. If you manage the deployment with Terraform, set `source_image_path` to the patched image and apply instead; a manual template change is reverted on the next apply.

Then confirm that `sudo php-fpm8.3 -v` reports PHP 8.3.36 on every VM in the group.

##### Apigee Developer Portal Kickstart Docker image

The `:latest`, `:main`, and `:nightly` tags have been republished with PHP 8.3.36. Your database and uploaded files are kept as long as they are stored on Docker volumes or bind mounts, not inside the container. Check `docker-compose.yml` before you recreate the container, and back them up first. If you use the prebuilt image, pull it before restarting:
    
    
    docker-compose pull apigee-kickstart
    docker-compose up -d apigee-kickstart
    

If you build the image yourself:
    
    
    docker-compose build --pull apigee-kickstart
    docker-compose up -d apigee-kickstart
    

Then confirm that `docker-compose exec apigee-kickstart php -v` reports PHP 8.3.36. On Kubernetes, run `kubectl rollout restart deployment/DEPLOYMENT_NAME -n NAMESPACE` so that the pods pull the republished image.

##### Self-hosted Drupal 10 and Drupal 11 portals

Update PHP on every portal server to 8.2.35, 8.3.36, 8.4.27, 8.5.12, or a later release in the same branch. Then restart PHP-FPM or your web server.

  * PHP 8.1: no fix is available. Upgrade to PHP 8.2 or later.
  * CentOS 7 or RHEL 7 with PHP from Remi: no packaged fix is available. Move to a supported OS with a maintained PHP package, or build PHP from source.



##### Apigee Edge for Private Cloud Drupal 7 and Drupal 9 portals

These portals run PHP 7.3 or 7.4 on RHEL/CentOS 7, RHEL 8, or Amazon Linux 2, where no packaged fix is available. Drupal 7 and Drupal 9 are end of life.

  * Don't install the developer-portal profile (`setup.sh -p dp`). Upcoming `apigee-setup` releases for Apigee Edge for Private Cloud 4.53.01 and 4.54.00 will block it.
  * Take the portal offline, or restrict access to internal networks.
  * Apply the interim mitigations later in this bulletin.
  * Migrate to a Drupal 10 or Drupal 11 portal on a supported PHP version.



##### Apigee Edge for Public Cloud self-hosted Drupal 7 portals

After Apigee ended hosting of Drupal 7 developer portals on 2020-05-31, Apigee Edge for Public Cloud customers who kept their portals took over hosting them. If your portal is hosted on Pantheon or Acquia, confirm with your provider that your site runs a patched PHP version. Portals moved to a customer's own servers run whatever PHP the customer installed: on Debian or Ubuntu, PHP 7.4 can be updated in place with Sury packages, while PHP 7.3 and earlier have no fix - move to PHP 8.2 or later. Then restart PHP-FPM.

##### Interim mitigations

These settings reduce exposure until you can update PHP; they don't fix the vulnerabilities. Set them administratively, as `php_admin_value` or `php_admin_flag` entries in the PHP-FPM pool configuration (or with `php_admin_value` in your Apache configuration), so that the application can't override them. Then restart all PHP-FPM workers, and confirm that no other pool, directory, or application setting restores a finite memory limit.

  * `session.upload_progress.enabled=0`
  * `memory_limit=-1`. On the Marketplace image, change the existing `php_admin_value[memory_limit]` line in `/etc/php/8.3/fpm/pool.d/www.conf` to -1 rather than adding a second one; when a pool file sets the same value twice, only one of them takes effect. VM-level changes don't survive managed-instance-group VM replacement; update the image (Step 2 of the Marketplace instructions) for a durable fix.
  * A small `post_max_size` (for example 8M), with `upload_max_filesize` below it. Because `post_max_size` can be bypassed and `memory_limit=-1` removes PHP's per-request memory cap, also enforce a request body size limit at your web server or load balancer (for example, `client_max_body_size` in nginx).
  * On PHP 8.5: `fatal_error_backtraces=0`
  * If your portal doesn't accept file uploads, block `multipart/form-data` requests at your load balancer or web server.

For more information, see the PHP advisories [GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) and [GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp). For help, contact Apigee Support: for Apigee and Apigee Hybrid, see [Getting started with Apigee support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support); for Apigee Edge and Apigee Edge for Private Cloud, see [Getting started with Apigee Edge support](https://docs.apigee.com/api-platform/troubleshoot/getting-started-with-support).

##### Check for compromise

Updating PHP doesn't remove an attacker who exploited the portal before it was patched. Look for PHP-FPM worker processes that started shells, interpreters, `curl`, or `wget`; new or changed files in the web root, `sites/default/files`, or the private files directory; multipart requests followed by memory-limit errors or bursts of HTTP 500 in the web server and PHP-FPM logs; and malformed or oversized `PHPSESSID` cookies in requests. If you find any of these, or can't rule them out for an internet-facing portal, rotate the Apigee credentials stored in the portal (the Apigee Edge module's connection credentials, or the service account key for Apigee), the Drupal administrator passwords, and the database password, and rebuild the portal VMs from a patched image. | Critical |  [CVE-2026-109618](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109618)  
[CVE-2026-109619](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-109619)  
  
## GCP-2026-041

**Published:** 2026-06-24

### Description

Description | Severity | Notes  
---|---|---  
A recent security investigation was conducted regarding log4j vulnerabilities (CVE-2026-34480 and CVE-2026-34477) reported in Apigee Edge for Private Cloud. Google has determined that Apigee Edge for Private Cloud is **not vulnerable** to these CVEs. **No customer action is required.** **CVE-2026-34480:** Apache Log4j Core's `XmlLayout` fails to sanitize characters forbidden by the XML 1.0 specification, producing invalid XML output whenever a log message or MDC value contains such characters. **CVE-2026-34477:** Addressed hostname verification issues where TLS connections could be left vulnerable to interception when using SMTP, Socket, or Syslog appenders. **Mitigation Note:** Apigee Edge for Private Cloud only ships the log4j library in gateway components but doesn't actually use them, as logback is used instead. Furthermore, Apigee Edge for Private Cloud does not use SMTP, Socket, or Syslog appender features of log4j. As a result, neither of these vulnerabilities is applicable to Apigee Edge for Private Cloud. **Affected Products**

  * Apigee Edge for Private Cloud

**What Should I Do?**

#### Apigee Edge for Private Cloud

No customer action is required. Apigee Edge for Private Cloud is not affected by these vulnerabilities. Customers running vulnerability scanners against Apigee Edge for Private Cloud deployments may see CVE-2026-34480 and CVE-2026-34477 flagged because the log4j library is present on disk. Customers can cite this security bulletin in their scanner-finding exception process to mark these CVEs as Not Applicable for their Apigee Edge for Private Cloud deployment. | High |  [CVE-2026-34480](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-34480)  
[CVE-2026-34477](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-34477)  
  
## GCP-2026-034

**Published:** 2026-05-20

### Description

Description | Severity | Notes  
---|---|---  
A vulnerability was found in Apigee where the `IntegrationRegion` parameter in the `SetIntegrationRequest` policy lacks validation, allowing for Server-Side Request Forgery (SSRF) and service account token exfiltration. The issue arises when an attacker can control a flow variable used for `IntegrationRegion`, leading to requests being sent to an attacker-controlled host with the service account token. **Affected Products** Impact is confined to the `SetIntegrationRequest` policy. This includes deployments on the following Apigee platforms:

  * Apigee
  * Apigee Hybrid

**What Should I Do?** Take the following actions for each affected product:

#### Apigee

No action is required for customers using the Google Cloud version of Apigee. Vulnerability fixes have been applied to Apigee release [1-16-0-apigee-5](https://docs.cloud.google.com/apigee/docs/release-notes#January_20_2026).

#### Apigee Hybrid

You must upgrade to one of the following security patch releases: | Hybrid major version | Security patch release for the affected minor version  
---|---  
1.14 | [1.14.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#April_27_2026)  
1.15 | [1.15.2](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1152)  
1.16 | [1.16.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#April_20_2026)  
High |  [CVE-2026-2264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2264)  
  
## GCP-2026-010

**Published:** 2026-02-13

### Description

Description | Severity | Notes  
---|---|---  
A vulnerability was identified in the Apigee platform that could have allowed a malicious actor with administrative or developer-level permissions in their own Apigee environment to elevate privileges and access cross-tenant data. Specifically, a vulnerability in Apigee's sandboxing technology allowed the use of a link-local endpoint to access service account tokens (P4SA) within a customer tenant project. By leveraging this identity, an attacker could theoretically read analytics metadata or tamper with internal monitoring records across other Apigee organizations (tenants). **What should I do?** Take the following actions for each affected product:

#### Apigee

No action is required for customers using the Google Cloud version of Apigee. Vulnerability fixes have been applied to Apigee release [1-16-0-apigee-3](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).

#### Apigee Hybrid

To resolve this vulnerability, customers must [enable the Pub/Sub-based analytics pipeline](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/data-collection-with-data-residency) and upgrade to a supported hybrid version: | Feature configuration | Minimum remediated version  
---|---  
Standard Apigee Hybrid | v1.14.0 or higher  
With Monetization (Mint) enabled | v1.14.3, v1.15.1, or v1.16.0  
High |  [CVE-2025-13292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-13292)  
  
## GCP-2025-023

**Published:** 2025-05-05

Description | Severity | Notes  
---|---|---  
This bulletin addresses potential security gaps which could be exploited if not addressed in the JavaCallout and PythonScript policies that were discovered and addressed. These policies could lead to unauthorized remote code execution (RCE) and privilege escalation within the Apigee runtime environment. These possible exploits require internal authorized user access (users who have privilege to deploy proxies) to exploit. These potential vulnerabilities stem from insufficient sandboxing for scenarios such as access by reflection and spoofing permission objects to bypass the security manager.  **Affected Products** Impact is confined to the JavaCallout and PythonScript policies. This includes deployments on the following Apigee platforms: 

  * Apigee
  * Apigee Edge for Public Cloud
  * Apigee Hybrid
  * Apigee Edge for Private Cloud

**What Should I Do?** Take the following actions for each affected product:

#### Apigee

No action is required for customers using the Google Cloud version of Apigee. Vulnerability fixes have been applied to Apigee release [1-14-0-apigee-8](https://docs.cloud.google.com/apigee/docs/release-notes#February_28_2025). If the release team is not able to make the release rollout for your orgs, either a TAM or a support representative will reach out to you to fix any affected JavaCallout proxy bundles.

#### Apigee Hybrid

You must upgrade to one of the following security patch releases: | Hybrid major version | Security patch release for the affected minor version  
---|---  
1.12 | [1.12.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#March_01_2025)  
1.13 | [1.13.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133)  
1.14 | [1.14.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)  
1.11 | [1.11.2 hotfix3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1112-hotfix3)  
High |   
  
#### Apigee Edge for Public Cloud

No action is required from Apigee Edge customers. Fixes have been applied to the latest Edge runtime. If you are a customer who cannot be updated to the latest Edge release due to known pending action items, a customer support representative will reach out to you.

#### Apigee Edge for Private Cloud

If you are an Edge for Private Cloud user, you should review your JavaCallout and PythonScript policies to ensure you are using code and libraries from trusted sources. Modifications to such policies require internal authorized access (users who have permissions to deploy proxies), so it is recommended that you audit your permissions to ensure only trusted users retain such access. Vulnerability fixes have been applied to Edge Private Cloud releases [4.52.02](https://docs.apigee.com/private-cloud/v4.52.02/installation-requirements) and [4.53.00](https://docs.apigee.com/private-cloud/v4.53.00/installation-requirements).

## GCP-2024-040

**Published:** 2024-07-02

This bulletin includes details specific to each of these Apigee products:

  * Edge Public Cloud
  * Edge Private Cloud
  * Edge Microgateway
  * Apigee
  * Apigee Hybrid



### Edge Public Cloud

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, Apigee Edge for Public Cloud is not exploitable and mitigations are in place. Even though this CVE is not exploitable, Apigee will upgrade the workloads to address the above CVE. **What should I do?** No action item is required from Apigee users. Patching for workloads will be done in the upcoming days and the security bulletin will be updated once the patching is completed. | Critical |   
  
### Edge Private Cloud

Description | Severity  
---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to VM nodes. Edge Private Cloud customers own and manage the VMs/Physical hosts where Edge Private Cloud is deployed. | Version | Impact  
---|---  
OpenSSH < 4.4p1 | Vulnerable  
4.4p1 <= OpenSSH < 8.5p1 | Not Vulnerable  
8.5p1 <= OpenSSH < 9.8p1 | Vulnerable  
  
**What should I do?**

Review the OpenSSH version by issuing the command `ssh -V` and validate the OpenSSH version. If you are running on any OpenSSH versions that are impacted, update to a version which is NOT vulnerable to this CVE. OpenSSH has released [9.8p1](https://www.openssh.com/releasenotes.html#9.8p1) on July 1, 2024.

Critical |   
  
### Edge Microgateway

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to VM nodes. Edge Microgateway customers own and manage the VMs/Physical hosts where Edge Microgateway is deployed. | Version | Impact  
---|---  
OpenSSH < 4.4p1 | Vulnerable  
4.4p1 <= OpenSSH < 8.5p1 | Not Vulnerable  
8.5p1 <= OpenSSH < 9.8p1 | Vulnerable  
  
**What should I do?**

Please review the OpenSSH version by issuing commands `ssh -V` and validate the OpenSSH version. If you are running on any OpenSSH versions which are impacted, please update to a version which is NOT vulnerable to this CVE. OpenSSH has released [9.8p1](https://www.openssh.com/releasenotes.html#9.8p1) on July 1, 2024.

Critical |   
  
### Apigee

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, Apigee is not exploitable and mitigations are in place. Even though this CVE is not exploitable, Apigee will upgrade the workloads to address CVE-2024-6387. **What should I do?** No action item is required from Apigee users. Patching for workloads will be done in the upcoming days and the security bulletin will be updated once the patching is completed. Note: If Managed Instance Groups are deployed in a customer project for [northbound load balancing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing), specifically [InternalRouting (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internal-routing-vpc) and [ExternalRouting (MIG)](https://cloud.google.com/apigee/docs/api-platform/get-started/install-cli#external-routing-mig), verify the OpenSSH version installed on them. If the version is vulnerable to the CVE, then update to OpenSSH [version 9.8p1](https://www.openssh.com/releasenotes.html#9.8p1) released on July 1, 2024 by yourself, as Apigee does not manage these MIGs. | Critical |   
  
### Apigee Hybrid

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, hybrid images are not vulnerable because OpenSSH is not packaged into any of the hybrid container images. However if your host/GKE-node OS is running with the below vulnerable versions of OpenSSH, your hybrid clusters will be exploitable. | Version | Impact  
---|---  
OpenSSH < 4.4p1 | Vulnerable  
4.4p1 <= OpenSSH < 8.5p1 | Not Vulnerable  
8.5p1 <= OpenSSH < 9.8p1 | Vulnerable  
  
**What should I do?**

This issue has been addressed in Google Cloud Customer Care Security Bulletin [GCP-2024-040](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040). 

For instructions and more details, see the following bulletins:

  * [GKE security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gke)
  * [GKE on VMware security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gdcvmware)
  * [GKE on AWS security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gkeaws)
  * [GKE on Azure security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gkeazure)
  * [GKE on Bare Metal security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gdcbm)
  * **AWS** : There is no update yet (As of July 1st 2024 2:22 PM PST). Refer their bulletin page for [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)
  * **Azure** : There is no update yet (As of July 1st 2024 2:22 PM PST). Refer their bulletin page for [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)
  * **OpenShift** : [OpenSSH's server (sshd) [CVE-2024-6387] | Red Hat Customer Portal](https://access.redhat.com/security/cve/cve-2024-6387)

Critical |   
  
## GCP-2024-006

**Published:** 2024-2-5

Description | Severity | Notes  
---|---|---  
When an Apigee API Management proxy connects to a [target endpoint](https://docs.apigee.com/api-platform/reference/api-proxy-configuration-reference#targetendpoint) or [ target server](https://docs.apigee.com/api-platform/deploy/load-balancing-across-backend-servers), the proxy does not perform hostname validation for the certificate presented by the target endpoint or target server by default. If hostname validation is not enabled using one of the following options, Apigee proxies connecting to a target endpoint or target server may be at risk for a man-in-the-middle attack by an authorized user. For more information, see [Configuring TLS from Edge to the backend (Cloud and Private Cloud)](https://docs.apigee.com/api-platform/system-administration/configuring-ssl-edge-backend-service).  **Affected Products** Apigee proxy deployments on the following Apigee platforms are affected:

  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud

**What Should I Do?** Customers can utilize either of the following options to enable this validation: **Option 1 - Add a configuration to your proxy** You can enable validation of your target endpoint or target server by adding a `<CommonName>` configuration to the `SSLInfo` section of the `<HTTPTargetConnection>` element in your [proxy configuration](https://docs.apigee.com/api-platform/reference/api-proxy-configuration-reference#targetendpoint-targetendpointconfigurationelements) as shown:
    
    
    <HTTPTargetConnection>
      <SSLInfo>
        <Enabled>true</Enabled>
        <TrustStore>ref://mytruststoreref</TrustStore>
        <CommonName>*.example.com</CommonName>
      </SSLInfo>
      <URL>https://my.example.com/</URL>
    </HTTPTargetConnection>

If this configuration is present in the `<HTTPTargetConnection>` element of your proxy configuration, Apigee will use the value specified in `<CommonName>`for hostname validation. Wildcards may be used in this field. Apigee recommends this approach. You can test proxies individually to confirm that validation is performing as intended, with minimal potential disruption to traffic. For more information on testing hostname validation in your proxies and viewing faults, see [Using the Trace Tool](https://docs.apigee.com/api-platform/debug/using-trace-tool-0). **Option 2 - Set an organization-level flag** You can set an Apigee organization-level flag to enable hostname validation for all deployed proxies and targets in your organization. If the `features.strictSSLEnforcement` flag is set to `true` in org properties, hostname validation will be enforced each time the proxy connects to a target endpoint or target server. **Note** : While this option can help you enable the feature across the organization, hostname validation failures can occur if your targets do not present the expected certificates.

  * For **Apigee Edge for Public Cloud** deployments**:** Contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support) to have the `features.strictSSLEnforcement` flag set to `true` in org properties. **Note** : Enabling this flag will enforce the SSL check for all environments in an organization and all proxies deployed within those environments.
  * For **Apigee Edge for Private Cloud** deployments: The `features.strictSSLEnforcement `flag can be set to `true` by the organization or system administrator. For more information on setting the flag, see [Updating organization properties](https://apidocs.apigee.com/docs/organizations/1/routes/organizations/%7Borg_name%7D/post). **Note** : When updating organization level flags using the Organizations API, make sure to include _all_ existing flags in your POST request to avoid overwriting earlier configuration settings. Once the flag is set, each message processor must be individually restarted for the change to take effect. Use the following command:
        
        apigee-service edge-message-processor restart

To roll back this change, use the same Organizations API to set the flag to `false` and then restart each message processor. **Note** : Enabling this flag will enforce the SSL check for all environments in an organization and all proxies deployed within those environments. However, if `[<IgnoreValidationErrors>](https://docs.apigee.com/api-platform/system-administration/options-configuring-tls#about-setting-tls-options-in-a-virtual-host-or-target-endpoint-target-server) `is set to `true`, any validation errors detected will be ignored.

Apigee recommends implementing this change in non-production environments first, to ensure that the validation works as intended and does not result in production outages. In the event that hostname validation fails for any targets, the following fault message is returned:
    
    
    {"fault":{"faultstring":"SSL Handshake failed java.security.cert.CertificateException: No subject alternative DNS name matching example.com found.","detail":{"errorcode":"messaging.adaptors.http.flow.SslHandshakeFailed"}}}

| High |   
  
## GCP-2023-032

**Published:** 2023-10-13

**Updated:** 2023-11-03

Description | Severity | Notes  
---|---|---  
**2023-11-03 Update:** Added [ known issue](https://docs.apigee.com/release/known-issues#private-cloud-known-issues) for Apigee Edge for Private Cloud.  A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the Apigee Ingress (Cloud Service Mesh) service used by Apigee X and Apigee hybrid. The vulnerability could lead to a DoS of Apigee API management functionality.  **Affected Products**

  * **Apigee X** Deployments of Apigee X that are accessible through a Google Cloud Network Load Balancer (Layer 4), or a custom layer 4 load balancer, are affected. A hotfix has been applied to all Apigee X instances. 
  * **Apigee hybrid** Apigee hybrid instances that allow HTTP/2 requests to reach the Apigee Ingress are affected. Customers should verify if the load balancers fronting their Apigee hybrid ingresses allow for HTTP/2 requests to reach the Apigee Ingress service. 
  * **Apigee Edge for Private Cloud** The Edge for Private Cloud router and management server components are exposed to the internet and can potentially be vulnerable. Although HTTP/2 is enabled on the management port of other Edge-specific components of Edge for Private Cloud, none of those components are exposed to the internet. On non-Edge components, like Cassandra, Zookeeper and others, HTTP/2 is not enabled. We recommend that you take the steps in [ Known issues with Edge for Private Cloud](https://docs.apigee.com/release/known-issues#private-cloud-known-issues) to address the Edge for Private Cloud vulnerability. 

**Unaffected products**

  * **Apigee X** Apigee X instances which are accessed only via Google Cloud Application Load Balancers (Layer 7) are not affected. This includes deployments that have HTTP/2 enabled for gRPC proxies. 
  * **Google Cloud API Gateway** Google Cloud API Gateway is not affected.
  * **Apigee Edge Cloud** Apigee Edge Cloud is not impacted by this vulnerability.

**What Should I Do?**

  * **Apigee X** **November 3, 2023 Update:** the vulnerability has been addressed via the update to Apigee X instances that was released on October 13, 2023. See the [ Release notes](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_13_2023) for details. 
  * **Apigee hybrid** Apigee hybrid customers will need to upgrade to one of the following patch versions: 
    * [ v1.10.3-hotfix.2](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1103-hotfix2) released on Friday, October 13, 2023 
    * [ v1.9.4-hotfix.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v194-hotfix1) released on Friday, October 13, 2023 
  * **Apigee Edge for Private Cloud** Apigee Edge for Private Cloud users can follow the instructions published in [ Known issues with Edge for Private Cloud](https://docs.apigee.com/release/known-issues#private-cloud-known-issues) for explicit disablement of HTTP/2 for exposed components. 

**What Vulnerabilities Are Addressed By These Patches?** The vulnerability, CVE-2023-44487, could lead to a DoS of Apigee API management functionality.  | High |  [ CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
