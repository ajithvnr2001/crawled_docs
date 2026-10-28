---
url: https://docs.cloud.google.com/recaptcha/docs/sign-requests-web-bot-auth/
title: Sign outbound requests with Web Bot Auth \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T19:53:52.804159+00:00
---

# Sign outbound requests with Web Bot Auth  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/sign-requests-web-bot-auth/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)



Send feedback 

#  Sign outbound requests with Web Bot Auth Stay organized with collections  Save and categorize content based on your preferences. 

The [Web Bot Auth (WBA)](https://www.ietf.org/archive/id/draft-ietf-webbotauth-httpsig-protocol-00.html) protocol lets you cryptographically prove your agent or bot's identity by using [HTTP Message Signatures (RFC 9421)](https://www.rfc-editor.org/rfc/rfc9421).

When you sign outbound requests, services like Google Cloud Fraud Defense (the evolution of reCAPTCHA) can verify your agent directly without relying only on IP addresses or `User-Agent` strings.

To authenticate your agent with WBA, complete the following tasks:

  1. Generate an Ed25519 key pair and format the public key as a JSON Web Key (JWK) Set.
  2. Host your public key directory at a well-known HTTPS endpoint.
  3. Sign each outbound HTTP request with your private key.
  4. Optional: Sign the experimental `Agent-Context` header to isolate reputation across tenants that share a signing key.

**Note:** The `Agent-Context` header is an experimental reCAPTCHA extension that isn't part of the base IETF WBA specification. Its fields are optional and subject to change as the specification matures. Standard WBA verifiers that don't use `Agent-Context` still validate your request signature.

## Generate an Ed25519 key pair

WBA requires an [Ed25519 (RFC 8032)](https://www.rfc-editor.org/rfc/rfc8032.html) asymmetric key pair. You keep the private key secret to sign outbound HTTP requests, and you publish the public key in a [JSON Web Key (JWK) Set (RFC 7517)](https://www.rfc-editor.org/rfc/rfc7517).

### Generate a key pair with OpenSSL and jwker

You can generate an Ed25519 key pair with OpenSSL and convert the public key to a JWK using the open-source [`jwker`](https://github.com/jphastings/jwker) tool:

  1. Generate an Ed25519 private key in PEM format:
         
         openssl genpkey -algorithm ed25519 -out private-key.pem
         

  2. Extract the public key in PEM format:
         
         openssl pkey -in private-key.pem -pubout -out public-key.pem
         

  3. If you don't already have `jwker` installed, install it by following the [`jwker` installation instructions](https://github.com/jphastings/jwker#installation).

  4. Convert the PEM public key to a JWK file using `jwker`:
         
         jwker public-key.pem public-key.jwk
         

This command writes a single JWK object to `public-key.jwk`:
         
         {
           "kty": "OKP",
           "crv": "Ed25519",
           "x": "16JuFxlu7PYOFULk_W6t3sZO4NF8Yj-2QpBxCAiXQfs"
         }
         

  5. Wrap the JWK object inside a JWK Set `keys` array (`jwks.json`) and add the required `alg`, `use`, and `kid` fields:
         
         {
           "keys": [
             {
               "kty": "OKP",
               "crv": "Ed25519",
               "alg": "EdDSA",
               "use": "sig",
               "kid": "OE_x89FAZvHnzOd9gMU0zFW-AhHTESAL5cV5aL0dqyw",
               "x": "16JuFxlu7PYOFULk_W6t3sZO4NF8Yj-2QpBxCAiXQfs"
             }
           ]
         }
         


**Important:** Don't serve the raw `public-key.jwk` file directly at your key directory endpoint. Verifiers require a JWK Set object containing a top-level `"keys"` array, with `"alg": "EdDSA"` and `"kid"` set on each key object.

### Public JWK Set field reference

Each public key object in your JWK Set `keys` array supports the following fields:

Field | Value | Description  
---|---|---  
`kty` | `"OKP"` | Key type. Must be `"OKP"` (Octet Key Pair) as defined in [RFC 8037](https://www.rfc-editor.org/rfc/rfc8037).  
`crv` | `"Ed25519"` | Cryptographic curve. Must be `"Ed25519"`.  
`alg` | `"EdDSA"` | Algorithm intended for use with the key. Must be `"EdDSA"`.  
`use` | `"sig"` | Intended use of the public key. Set to `"sig"` (signature).  
`x` | `"BASE64URL_PUBLIC_KEY"` | The 32-byte raw Ed25519 public key, encoded using unpadded base64url ([RFC 4648 Section 5](https://www.rfc-editor.org/rfc/rfc4648#section-5)).  
`kid` | `"KEY_ID"` | Unique key identifier that matches the `keyid` parameter in your signed requests. Use the [RFC 7638](https://www.rfc-editor.org/rfc/rfc7638) SHA-256 JWK thumbprint (unpadded base64url) for cross-vendor compatibility.  
`nbf` | `UNIX_SECONDS` | Optional. Unix timestamp in **seconds** before which the key isn't valid.  
`exp` | `UNIX_SECONDS` | Optional. Unix timestamp in **seconds** after which the key expires. Verifiers reject expired keys.  
**Caution:** If you include the `exp` or `nbf` fields, format the timestamp in **Unix seconds** (for example, `1792646036`), not milliseconds.

## Host your public key directory

Verifiers fetch your public keys from a well-known HTTPS endpoint on your agent's domain.

### Endpoint and header requirements

To host your key directory, configure your web server to meet the following requirements:

  * **URL path** : Serve the JWK Set JSON at `https://YOUR_AGENT_DOMAIN/.well-known/http-message-signatures-directory`.
  * **Transport security** : Serve the endpoint over HTTPS on default port `443`. Don't redirect requests to a different host or scheme.
  * **Content type** : Set the `Content-Type` response header to `application/http-message-signatures-directory+json` (or `application/json`).
  * **Caching** : Set the `Cache-Control` response header with a `max-age` directive (for example, `Cache-Control: public, max-age=3600`).
  * **Key rotation** : Before you sign requests with a new private key, add its public JWK to the `keys` array and wait for your `Cache-Control` TTL to expire. Remove revoked or expired keys from the `keys` array.



The following example shows an HTTP response from `GET /.well-known/http-message-signatures-directory`:
    
    
    HTTP/1.1 200 OK
    Content-Type: application/http-message-signatures-directory+json
    Cache-Control: public, max-age=3600
    
    {
      "keys": [
        {
          "kty": "OKP",
          "crv": "Ed25519",
          "alg": "EdDSA",
          "use": "sig",
          "kid": "OE_x89FAZvHnzOd9gMU0zFW-AhHTESAL5cV5aL0dqyw",
          "x": "16JuFxlu7PYOFULk_W6t3sZO4NF8Yj-2QpBxCAiXQfs"
        }
      ]
    }
    

**Note:** To comply with the [HTTP Message Signatures Directory draft](https://datatracker.ietf.org/doc/html/draft-meunier-http-message-signatures-directory), your server can also sign the directory response itself. To sign the directory response, include `Signature-Input` and `Signature` response headers signed with `tag="http-message-signatures-directory"` covering the `"@authority";req` component.

## Sign an outbound HTTP request

To authenticate an outbound HTTPS request with WBA, attach three required headers: `Signature-Agent`, `Signature-Input`, and `Signature`.

### HTTP headers

  1. **`Signature-Agent`** : Specifies the HTTPS origin of your key directory as a quoted string:
         
         Signature-Agent: "https://agent.example.com"
         

  2. **`Signature-Input`** : Maps a signature label (such as `sig1`) to an inner list of covered HTTP components and signature metadata parameters:
         
         Signature-Input: sig1=("@authority" "signature-agent");created=1772400000;expires=1772400300;keyid="OE_x89FAZvHnzOd9gMU0zFW-AhHTESAL5cV5aL0dqyw";tag="web-bot-auth"
         

Include the following covered components and parameters:

     * **Covered components** : 
       * `"@authority"`: Required. Binds the signature to the destination host (for example, `www.example.com`).
       * `"signature-agent"`: Required. Binds the signature to your `Signature-Agent` header.
     * **Metadata parameters** : 
       * `created`: Current Unix timestamp in seconds (integer).
       * `expires`: Expiration Unix timestamp in seconds (integer). Set `expires` to at most 300 seconds (5 minutes) after `created`.
       * `keyid`: Your public key's `kid` string from your JWK Set.
       * `tag`: Must be `"web-bot-auth"`.
  3. **`Signature`** : Maps the same signature label (`sig1`) to the base64-encoded Ed25519 signature formatted as an [RFC 8941](https://www.rfc-editor.org/rfc/rfc8941) byte sequence (wrapped in `:` colons):
         
         Signature: sig1=:BASE64_ENCODED_SIGNATURE:
         




### Construct the signature base

Before signing, construct the canonical signature base string defined in [RFC 9421 Section 2.5](https://www.rfc-editor.org/rfc/rfc9421#section-2.5). Each covered component appears on its own line in lowercase, followed by the `@signature-params` line with no trailing newline:
    
    
    "@authority": www.example.com
    "signature-agent": "https://agent.example.com"
    "@signature-params": ("@authority" "signature-agent");created=1772400000;expires=1772400300;keyid="OE_x89FAZvHnzOd9gMU0zFW-AhHTESAL5cV5aL0dqyw";tag="web-bot-auth"
    

Sign the UTF-8 bytes of this signature base string using your Ed25519 private key.

### Go example

The following example loads the `private-key.pem` file generated by OpenSSL and signs an outbound `*http.Request` using Go's standard `crypto/ed25519` package and `github.com/dunglas/httpsfv`:
    
    
    package main
    
    import (
        "crypto/ed25519"
        "crypto/x509"
        "encoding/base64"
        "encoding/pem"
        "fmt"
        "net/http"
        "strings"
        "time"
    
        "github.com/dunglas/httpsfv"
    )
    
    // loadPrivateKey parses a PKCS#8 PEM-encoded Ed25519 private key
    // generated by OpenSSL.
    func loadPrivateKey(pemBytes []byte) (ed25519.PrivateKey, error) {
        // Decode the PEM armor to get the raw DER bytes.
        block, _ := pem.Decode(pemBytes)
        if block == nil {
            return nil, fmt.Errorf("failed to decode PEM block")
        }
    
        // OpenSSL generates private keys in PKCS#8 format by default.
        key, err := x509.ParsePKCS8PrivateKey(block.Bytes)
        if err != nil {
            return nil, err
        }
    
        // Confirm that the parsed key is an Ed25519 private key.
        privKey, ok := key.(ed25519.PrivateKey)
        if !ok {
            return nil, fmt.Errorf("not an Ed25519 private key")
        }
        return privKey, nil
    }
    
    // signRequestEd25519 signs req with WBA headers.
    func signRequestEd25519(
        req *http.Request,
        privKey ed25519.PrivateKey,
        keyID string,
    ) error {
        const (
            // sigLabel links the Signature-Input and Signature entries.
            sigLabel = "sig1"
            // agentURL is the HTTPS origin where your JWK Set is hosted.
            agentURL = "https://agent.example.com"
        )
    
        // 1. Set the Signature-Agent header as a quoted string.
        sigAgentHeader := fmt.Sprintf("%q", agentURL)
        req.Header.Set("Signature-Agent", sigAgentHeader)
    
        // 2. List the HTTP components to cover in the signature.
        // Always cover "@authority" (the target host) and "signature-agent".
        authority := strings.ToLower(req.URL.Host)
        items := []httpsfv.Item{
            httpsfv.NewItem("@authority"),
            httpsfv.NewItem("signature-agent"),
        }
        baseLines := []string{
            fmt.Sprintf(`"@authority": %s`, authority),
            fmt.Sprintf(`"signature-agent": %s`, sigAgentHeader),
        }
    
        // If the optional Agent-Context header is set, sign it too.
        if agentCtx := req.Header.Get("Agent-Context"); agentCtx != "" {
            items = append(items, httpsfv.NewItem("agent-context"))
            line := fmt.Sprintf(`"agent-context": %s`, agentCtx)
            baseLines = append(baseLines, line)
        }
    
        // 3. Set the signature metadata parameters.
        // Set expires to 300 seconds (5 minutes) after created.
        now := time.Now().Unix()
        params := httpsfv.NewParams()
        params.Add("created", now)
        params.Add("expires", now+300)
        params.Add("keyid", keyID)
        params.Add("tag", "web-bot-auth")
    
        // Serialize the covered components and parameters for Signature-Input.
        innerList := httpsfv.InnerList{
            Items:  items,
            Params: params,
        }
        sigParamsStr, err := httpsfv.Marshal(innerList)
        if err != nil {
            return err
        }
    
        // 4. Build the RFC 9421 signature base string.
        // Join each covered component line and @signature-params with "\n".
        // Don't add a trailing newline after the @signature-params line.
        paramLine := fmt.Sprintf(`"@signature-params": %s`, sigParamsStr)
        baseLines = append(baseLines, paramLine)
        sigBase := strings.Join(baseLines, "\n")
    
        // 5. Sign the UTF-8 bytes of the signature base with your private key.
        sigBytes := ed25519.Sign(privKey, []byte(sigBase))
        sigB64 := base64.StdEncoding.EncodeToString(sigBytes)
    
        // 6. Attach the Signature-Input and Signature headers to the request.
        req.Header.Set("Signature-Input", fmt.Sprintf("%s=%s", sigLabel, sigParamsStr))
        req.Header.Set("Signature", fmt.Sprintf("%s=:%s:", sigLabel, sigB64))
        return nil
    }
    

## Include the experimental Agent-Context header

**Note:** The `Agent-Context` header is an experimental reCAPTCHA extension that isn't part of the base IETF WBA specification. All fields in it are optional and might change in future revisions. Standard WBA verifiers that don't use `Agent-Context` ignore the header and still validate your signature.

Multi-tenant platforms (such as hosted browser providers or cloud agent runtimes) often sign outbound requests from multiple customer agents or tenants using a single shared signing key. By default, WBA identifies only the signing domain (`Signature-Agent`), so all traffic signed by that key shares the same reputation.

When you include and sign the `Agent-Context` header, reCAPTCHA can evaluate reputation separately across distinct products, projects, users, or sessions that share a common signing key on your platform.

### Format the Agent-Context header

Format `Agent-Context` as an [RFC 8941](https://www.rfc-editor.org/rfc/rfc8941) Structured Field Dictionary where each key is a lowercase token and each value is a quoted ASCII string:
    
    
    Agent-Context: product="ResearchBot", project="prj_89a0f", user="usr_29df3", session="sess_88b1"
    

**Warning:** Don't include personally identifiable information (PII). The `Agent-Context` header is sent in plaintext and is readable in HTTP logs across proxies, CDNs, and destination web servers. Never put raw email addresses, usernames, phone numbers, or IP addresses into `Agent-Context` fields. Always use opaque tokens, UUIDs, or salted hashes (such as a SHA-256 hash of your internal account ID with a secret salt).

All fields are optional. Include only the fields that apply to your architecture:

Field | Description | Example  
---|---|---  
`product` | Application or commercial name of the agent making the request. | `product="ResearchBot"`  
`project` | Pseudonymous account, workspace, or tenant project identifier on the host platform. | `project="prj_89a0f"`  
`user` | Pseudonymous identifier (such as an opaque UUID or salted hash) for the customer or end user. Keep this value stable across requests from the same user to build reputation, and never include real PII. | `user="usr_29df3"`  
`session` | Ephemeral, opaque identifier for a single task, workflow run, or browsing session. | `session="sess_88b1"`  
  
### Sign the Agent-Context header

reCAPTCHA only uses `Agent-Context` for reputation isolation when you include `"agent-context"` in your WBA signature. Unsigned `Agent-Context` headers are ignored.

To sign the `Agent-Context` header, complete the following steps:

  1. Set the `Agent-Context` header on your outbound `*http.Request` before calling `signRequestEd25519`:
         
         req.Header.Set("Agent-Context", `product="ResearchBot", project="prj_89a0f", user="usr_29df3", session="sess_88b1"`)
         

  2. Include `"agent-context"` in the `Signature-Input` component list and signature base string (handled automatically by the Go example):
         
         "@authority": www.example.com
         "signature-agent": "https://agent.example.com"
         "agent-context": product="ResearchBot", project="prj_89a0f", user="usr_29df3", session="sess_88b1"
         "@signature-params": ("@authority" "signature-agent" "agent-context");created=1772400000;expires=1772400300;keyid="OE_x89FAZvHnzOd9gMU0zFW-AhHTESAL5cV5aL0dqyw";tag="web-bot-auth"
         




The following example shows a complete HTTP request signed with `Agent-Context`:
    
    
    GET /api/data HTTP/1.1
    Host: www.example.com
    Signature-Agent: "https://agent.example.com"
    Agent-Context: product="ResearchBot", project="prj_89a0f", user="usr_29df3", session="sess_88b1"
    Signature-Input: sig1=("@authority" "signature-agent" "agent-context");created=1772400000;expires=1772400300;keyid="OE_x89FAZvHnzOd9gMU0zFW-AhHTESAL5cV5aL0dqyw";tag="web-bot-auth"
    Signature: sig1=:BASE64_ENCODED_SIGNATURE:
    

## What's next

Signing your requests with WBA proves cryptographic control of your agent's domain, but websites also need metadata about who operates your agent and what purpose it serves.

  * **Learn how site owners use Verified Agent signals** : 
    * [Monitor agent traffic](https://docs.cloud.google.com/recaptcha/docs/monitor-agents) in the **Agent overview** dashboard.
    * [Configure challenge policies](https://docs.cloud.google.com/recaptcha/docs/challenge-policies) using the `verified_bots` condition variable.
  * **Read the protocol specifications** : 
    * [IETF Web Bot Auth HTTP Signature Protocol draft](https://www.ietf.org/archive/id/draft-ietf-webbotauth-httpsig-protocol-00.html)
    * [RFC 9421: HTTP Message Signatures](https://www.rfc-editor.org/rfc/rfc9421)
    * [HTTP Message Signatures Directory draft](https://datatracker.ietf.org/doc/html/draft-meunier-http-message-signatures-directory)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
