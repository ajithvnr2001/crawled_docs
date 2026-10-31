---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/identity-delegation-architecture/
title: Identity delegation architecture \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:56:18.385976+00:00
---

# Identity delegation architecture  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/identity-delegation-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Identity delegation architecture Stay organized with collections  Save and categorize content based on your preferences. 

To enforce trust boundaries across human users, autonomous workloads, and external tools without relying on service account impersonation, Agent Identity uses a three-identity delegation framework. This framework separates and coordinates three distinct identity contexts across your environment:

  * **User identity:** The initiating end user's identity, authenticated through standard OAuth 2.0 or OpenID Connect (OIDC) with Google Identity or a federated workforce identity provider (IdP).
  * **Agent identity:** The deployed agent's unique, cryptographically attested [SPIFFE identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview#spiffe-identity) and auto-provisioned X.509 certificate, representing the agent acting on its own authority.
  * **Delegated identity:** The combined authority context when the agent acts on behalf of the initiating human user using scoped 3-legged OAuth (3LO) credentials brokered by [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/auth-manager-overview).



The following diagram illustrates how the user identity, agent identity, and delegated identity interact across ingress, runtime, and egress trust boundaries:

![Identity delegation architecture diagram mapping the user identity, agent identity, and delegated identity across ingress, runtime, and egress trust boundaries.](https://docs.cloud.google.com/static/iam/img/agent-identity-delegation-arch.svg)

In this architecture, the user identity establishes caller context during ingress, the agent identity authenticates the workload within the runtime boundary, and the delegated identity combines both authorities when the agent accesses downstream services on behalf of the user.

## How identities propagate across trust boundaries

As a request moves across these trust boundaries, the platform evaluates and propagates each identity layer:

  1. **Client-to-Agent ingress boundary (user identity):** The human user authenticates to the client application using an OAuth 2.0 or OIDC token. When traffic enters through Agent Gateway (in `CLIENT_TO_AGENT` ingress mode), the authorization policies attached to Agent Gateway verify the user identity to confirm that the user is authorized to invoke the target agent and forward the verified user context to the runtime.
  2. **Agent runtime and credential brokering (agent identity):** Inside the isolated runtime environment, the agent operates under its own SPIFFE agent identity with an auto-rotated 24-hour X.509 certificate. When the agent needs credentials for downstream tools, it authenticates to Agent Identity auth manager using its agent identity.
  3. **Autonomous egress path (agent identity):** When the agent calls Google Cloud APIs or machine-to-machine endpoints on its own authority, it authenticates using certificate-bound tokens enforced by mutual TLS (mTLS) and Demonstrating Proof of Possession (DPoP), OIDC ID tokens, or 2-legged OAuth (2LO) credentials from the auth manager. IAM allow and deny policies, Principal Access Boundary (PAB) policies, and Context-Aware Access policies evaluate the request strictly against the agent identity.
  4. **User-delegated egress path (delegated identity):** When the agent calls user-scoped Model Context Protocol (MCP) servers or third-party APIs on behalf of the human user, the auth manager brokers a consented 3LO user token representing the delegated identity. Outbound calls are governed by both the agent's egress policies and the delegating user's permissions and consented OAuth scopes, and audit logs record both the agent identity and the user identity.



## Identity layer comparison

The following table summarizes how the three identity layers govern access and auditability:

Identity layer | Principal and credential type | Trust boundary and policy enforcement | Audit log attribution  
---|---|---|---  
**User identity** | Initiating end user (Google Account or workforce identity principal) authenticated with an OAuth 2.0 or OIDC token. | **Client-to-Agent (ingress):** Agent Gateway authorization policies verify whether the user can invoke the agent and initiate a session. | Logs the human user identity as the caller invoking the agent endpoint.  
**Agent identity** | Autonomous agent workload (agent identity principal) authenticated with a SPIFFE X.509 certificate (mTLS and DPoP), OIDC ID token, or 2LO credential or API key from the auth manager. | **Agent-to-Anywhere (egress):** IAM allow, deny, Principal Access Boundary, and Context-Aware Access policies enforce which Google Cloud resources, auth providers, and external endpoints the agent can reach on its own authority. | Logs the agent's unique SPIFFE principal as the acting identity.  
**Delegated identity** | Agent identity acting on behalf of the consenting human user (Google Account or workforce identity principal) using a scoped 3LO access token brokered by Agent Identity auth manager. | **Agent-to-Anywhere (egress):** Enforces least-privilege intersection—the call must satisfy both the agent's outbound governance policies and the delegating user's permissions and consented OAuth scopes. | Records dual attribution, capturing both the agent's SPIFFE identity and the delegating human user.  
  
## What's next

  * Learn more about the [Agent Identity overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview).

  * Learn more about [using agent identity with Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity).

  * Learn more about [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
