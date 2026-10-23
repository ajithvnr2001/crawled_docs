---
url: https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/get-started/
title: Get started \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:09:48.037878+00:00
---

# Get started · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /[Cloud Workload Security](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/)
  4. /Get started



# Get started

Last updated Oct 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSet up the proxy locally Create the guardrail policy Create a policy set Create a deployment Create the proxy API token Prepare a certificate authority Configure the proxy Validate and start the proxy Route the CLI through the proxy Verify the guardrail Remove the test bucketNext steps

Run a Cloud Workload Security (CWS) proxy locally and block requests that make an R2 bucket public. This walkthrough uses an empty test bucket in your Cloudflare account.

The proxy and `cf` client run on the same Linux machine. For pipeline runners, application hosts, and shared proxies, refer to [Proxy deployment options](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/platform/#proxy-deployment-options).

## Prerequisites

Zero Trust subscription required

Your account must have a [Zero Trust subscription](https://developers.cloudflare.com/cloudflare-one/setup/#2-create-a-zero-trust-organization). The Zero Trust Free plan is sufficient.

  * A Linux machine or virtual machine with APT or DNF, `curl`, and `sudo` access.
  * A Cloudflare account with access to manage CWS resources and create account API tokens.
  * R2 access in the same account and permission to create and configure a test bucket.
  * The [Cloudflare CLI installed and signed in](https://developers.cloudflare.com/cf/get-started/). Use Node.js 24.5 or later for the client proxy settings in this guide.
  * OpenSSL and a terminal on the proxy host.



## Set up the proxy locally

  1. ### Install the proxy

Install `cws-proxy` using your Linux distribution's package manager:
         
         sudo curl -fsSLo /usr/share/keyrings/cloudflare-cws.gpg \
           https://downloads.cac.cloudflare.com/packages/keys/cws-package-signing.gpg
         
         sudo curl -fsSLo /etc/apt/sources.list.d/cws-proxy.sources \
           https://downloads.cac.cloudflare.com/packages/cws-proxy.sources
         
         sudo apt update
         sudo apt install cws-proxy
         
         sudo rpm --import \
           https://downloads.cac.cloudflare.com/packages/keys/cws-package-signing.asc
         
         sudo curl -fsSLo /etc/yum.repos.d/cws-proxy.repo \
           https://downloads.cac.cloudflare.com/packages/cws-proxy.repo
         
         sudo dnf install cws-proxy

Confirm that the installed command is available:
         
         cws-proxy --help

For the proxy's Beta terms, license notices, and acknowledgments, refer to [Legal](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/legal/).

  2. ### Create the guardrail policy

In the Cloudflare dashboard, select your account and go to **Cloud Workload Security** > **Policies**.

[ Go to **Policies** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/policies)

Select **Add policy** and name it `restrict-r2-public-access`. In **Filters** , select **Wirefilter** and enter:
         
         application.name == "Cloudflare" and application.service == "r2" and application.operation == "r2-put-bucket-public-policy"

In **Rego source** , enter this policy. It permits the selected operation only when the request turns off public access:

Rego sourcetxt
         
         package policy.cf_r2_no_public_access
         
         default valid := false
         
         valid if {
           input.http.request.body.enabled == false
         }

Select **Add policy** to save it.

  3. ### Create a policy set

Go to **Cloud Workload Security** > **Policy sets**.

[ Go to **Policy sets** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/policy-sets)

Select **Add policy set** and name it `r2-private-buckets`. In **Policies** , select **Attach policy** , choose `restrict-r2-public-access`, and select **Attach policies**.

Turn on **Enforce** for the policy. Leave **Workloads** empty for this walkthrough, then select **Add policy set**.

  4. ### Create a deployment

Go to **Cloud Workload Security** > **Deployments**.

[ Go to **Deployments** ↗ ](https://dash.cloudflare.com/?to=/:account/one/cloud-workload-security/deployments)

Select **Add deployment** and name it `cws-r2-test`. In **Policy sets** , select **Attach policy set** , choose `r2-private-buckets`, and select **Attach policy sets**.

In **Deployment settings** , choose _Default allow_ for **Default mode**. This permits requests outside the guardrail's filter. Select **Add deployment** to save it.

Open the deployment and copy its **ID**. Also copy your [Cloudflare Account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).

  5. ### Create the proxy API token

In the same account, go to **Manage account** > **Account API tokens**.

[ Go to **Account API tokens** ↗ ](https://dash.cloudflare.com/?to=/:account/api-tokens)

Create a custom account token with the **Cloud Workload Security Deployment** permission. Save the token for the proxy configuration.

This token loads CWS configuration. Your signed-in `cf` client uses its own credentials for R2 requests.

  6. ### Prepare a certificate authority

The proxy needs a certificate authority (CA) certificate and its matching private key. Clients need to trust the CA certificate.

To create a local test CA, save this configuration as `openssl.cnf`. If you already have a CA pair, use those files instead.

openssl.cnfini
         
         [req]
         prompt = no
         distinguished_name = subject
         x509_extensions = v3_ca
         
         [subject]
         O = Example Inc
         CN = CWS Local Proxy CA
         
         [v3_ca]
         basicConstraints = critical,CA:true
         keyUsage = critical,keyCertSign,cRLSign
         subjectKeyIdentifier = hash
         authorityKeyIdentifier = keyid:always,issuer

Generate the certificate and private key:
         
         umask 077
         openssl genrsa -out ca-key.pem 4096
         openssl req -config openssl.cnf -key ca-key.pem -new -x509 -days 730 -sha256 -out ca-cert.pem

Keep `ca-key.pem` on the proxy host. Configure clients with `ca-cert.pem` only.

  7. ### Configure the proxy

Save this configuration as `config.yaml`. Replace `<ACCOUNT_ID>` and `<DEPLOYMENT_ID>` with the values you copied. Use absolute certificate paths if the files are outside your working directory.

config.yamlyaml
         
         cws:
           api_base_url: "https://api.cloudflare.com/client/v4"
           api_poll_interval_secs: 30
           api_token_env: "CWS_DEPLOYMENT_TOKEN"
           account_id: "<ACCOUNT_ID>"
           deployment_id: "<DEPLOYMENT_ID>"
         
         proxy:
           logging:
             format: json
             verbosity: INFO
           listen_addr: "127.0.0.1:8080"
           tls_interception:
             ca_cert: ./ca-cert.pem
             ca_private_key: ./ca-key.pem
             extra_root_cas: []
           upstream:
             proxy:
               http_proxy: null
               https_proxy: null
               ca_cert: null
               no_proxy: null
         
         redis:
           enabled: false

`api_token_env` contains an environment variable name, not the token value. This local example binds the proxy to loopback and does not require a Redis server.

For other authentication modes, upstream proxies, logging, and Redis options, refer to [Proxy configuration](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/configuration/).

  8. ### Validate and start the proxy

In the terminal that runs the proxy, set your token and validate the file:
         
         export CWS_DEPLOYMENT_TOKEN="<DEPLOYMENT_API_TOKEN>"
         cws-proxy --config config.yaml --config-test

Successful validation prints `CWS proxy configuration is valid`. It checks the local configuration, not API access.

Start the proxy in that terminal:
         
         cws-proxy --config config.yaml

Keep the terminal open. Wait for `remote_config_loaded` and `action_mapper_loaded` in the logs before sending requests. Do not point this terminal's `HTTP_PROXY` or `HTTPS_PROXY` variables at the local proxy.

  9. ### Route the CLI through the proxy

Open a second terminal for the client. Replace the certificate path and Account ID, then set:
         
         export HTTP_PROXY="http://127.0.0.1:8080"
         export HTTPS_PROXY="http://127.0.0.1:8080"
         export NODE_USE_ENV_PROXY=1
         export NODE_EXTRA_CA_CERTS="<ABSOLUTE_PATH_TO_CA_CERT_PEM>"
         export CLOUDFLARE_ACCOUNT_ID="<ACCOUNT_ID>"

`NODE_EXTRA_CA_CERTS` points to the CA certificate, not its private key. These variables apply to the `cf` client in this terminal. Make sure `NO_PROXY` and `no_proxy` do not bypass `api.cloudflare.com`.

  10. ### Verify the guardrail

In the client terminal, create an empty test bucket and inspect managed public access:
         
         cf r2 buckets create --name cws-r2-guardrails-demo
         cf r2 buckets domains managed list --bucket-name cws-r2-guardrails-demo

The managed-domain result should contain `"enabled": false`. Use a different bucket name if this name already exists in your account.

First, confirm the policy permits turning off public access:
         
         cf r2 buckets domains managed update cws-r2-guardrails-demo --enabled false

This request should succeed. Then attempt to turn on public access:
         
         cf r2 buckets domains managed update cws-r2-guardrails-demo --enabled true

The request should fail with HTTP status `403` and a `CWS.Error` response. Check the managed-domain result again to confirm public access remains off.

If the request succeeds, immediately turn off public access with `--enabled false`. Check that the CLI uses the proxy, the deployment contains your policy set, and **Enforce** is on. For further checks, refer to [Requests expected to be blocked succeed](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/troubleshooting/#requests-expected-to-be-blocked-succeed).

  11. ### Remove the test bucket

In the client terminal, delete the empty bucket:
         
         cf r2 buckets delete cws-r2-guardrails-demo

Confirm the deletion when prompted.




## Next steps

To apply guardrails outside this local walkthrough, review [Proxy deployment options](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/platform/#proxy-deployment-options).

To target specific request groups or add more policies, follow [Configure policies](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/configure-policies/). For destination controls, follow [Manage traffic scope](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/guides/manage-traffic-scope/).

For startup, certificate, or unexpected request results, refer to [Troubleshooting](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/troubleshooting/).

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/concepts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/cloud-workload-security/get-started/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
