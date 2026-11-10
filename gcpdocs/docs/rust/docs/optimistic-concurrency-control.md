---
url: https://docs.cloud.google.com/rust/docs/optimistic-concurrency-control/
title: Working with optimistic concurrency control (OCC) \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:48:47.538547+00:00
---

# Working with optimistic concurrency control (OCC)  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/optimistic-concurrency-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Working with optimistic concurrency control (OCC) Stay organized with collections  Save and categorize content based on your preferences. 

Optimistic concurrency control (OCC) is a strategy for managing shared resources and preventing lost updates or race conditions when multiple users or processes modify the same resource at the same time.

For example, when working with Identity and Access Management, an IAM policy is a shared resource attached to a resource such as a project, bucket, or service. Without concurrency control, simultaneous modifications can overwrite recent policy changes, inadvertently revoking legitimate access or granting unauthorized permissions.

To implement OCC, systems typically use a version number or an `etag` (entity tag) field on the resource struct.

## How OCC works

Suppose two processes, A and B, try to update a shared resource at the same time:

  1. Process A reads the current state of the resource.
  2. Process B reads the same current state.
  3. Process A modifies its copy and writes it back to the server.
  4. Process B modifies its copy and writes it back to the server.



Because Process B overwrites the resource without knowing that Process A already changed it, Process A's updates are lost.

OCC solves this problem by introducing a unique fingerprint that changes every time an entity is modified. In many systems, such as IAM, this fingerprint is an `etag`. The server checks this tag on every write:

  1. When you read the resource, the server returns an `etag` (a unique fingerprint).
  2. When you send the modified resource back, you must include the original `etag`.
  3. If the stored `etag` doesn't match the `etag` that you sent—meaning another process modified the resource after you read it—the write operation fails with an `ABORTED` or `FAILED_PRECONDITION` error.



This failure signals the client to retry the entire process: re-read the updated state, re-apply the changes, and try the write again with the new `etag`.

## Implement the OCC loop

The core of an OCC implementation is a retry loop that reads, modifies, and attempts to save the resource, exiting after a successful write. To prevent infinite loops during high contention, configure a reasonable maximum number of retry attempts.

### Steps of the loop

The following table describes each step in an OCC retry loop:

Step | Action | Implementation example  
---|---|---  
**Read** | Fetch the current resource state, including the `etag`. | 
    
    
    let mut policy = client
        .get_iam_policy()
        .set_resource(&secret_name)
        .send()
        .await?;  
  
**Modify** | Apply the changes to the local struct. | 
    
    
    policy.bindings.push(new_binding);  
  
**Write and check** | Attempt to save the modified resource using the existing `etag`, and check for concurrency error codes. | 
    
    
    match client
        .set_iam_policy()
        .set_resource(&secret_name)
        .set_policy(policy)
        .send()
        .await
    {
        Ok(p) => return Ok(p),
        Err(e) => { /* ... */ }
    }  
  
**Success or retry** | If the write succeeds, exit the loop. If it fails with a concurrency error, increment the retry counter and continue the loop from the **Read** step. | -  
  
### Example

The following example demonstrates how to implement an OCC loop that updates an IAM policy on a Secret Manager secret resource by granting a member the `roles/secretmanager.secretAccessor` role.

**Note:** Although this example uses the Secret Manager client, the same OCC pattern applies to any service or database that implements versioned updates.

To run this example, first declare the dependency in your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1
    

Then implement the OCC retry loop:
    
    
    const ROLE: &str = "roles/secretmanager.secretAccessor";
    const ATTEMPTS: u32 = 5;
    
    let secret_name = format!("projects/{project_id}/secrets/{secret_id}");
    let client = SecretManagerService::builder().build().await?;
    for _attempt in 0..ATTEMPTS {
        let mut current = client
            .get_iam_policy()
            .set_resource(&secret_name)
            .send()
            .await?;
    
        match current.bindings.iter_mut().find(|b| b.role == ROLE) {
            None => current
                .bindings
                .push(Binding::new().set_role(ROLE).set_members([member])),
            Some(b) => {
                if b.members.iter().any(|m| m == member) {
                    return Ok(current);
                }
                b.members.push(member.to_string());
            }
        };
        let updated = client
            .set_iam_policy()
            .set_resource(&secret_name)
            .set_policy(current)
            .set_update_mask(FieldMask::default().set_paths(["bindings"]))
            .send()
            .await;
        match updated {
            Ok(p) => return Ok(p),
            Err(e)
                if e.status().is_some_and(|s| {
                    s.code == Code::Aborted || s.code == Code::FailedPrecondition
                }) =>
            {
                continue;
            }
            Err(e) => return Err(e.into()),
        }
    }
    anyhow::bail!("could not set IAM policy after {ATTEMPTS} attempts")

### Complete code

The following code shows the complete function with all required imports:
    
    
    use google_cloud_gax::error::rpc::Code;
    use google_cloud_iam_v1::model::Binding;
    use google_cloud_iam_v1::model::Policy;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use google_cloud_wkt::FieldMask;
    
    /// Executes an Optimistic Concurrency Control (OCC) loop to safely update a resource.
    ///
    /// This function demonstrates the core Read-Modify-Write-Retry pattern. It uses the secret manager
    /// service and a hard-coded role. The principles apply to any other service or role.
    ///
    /// # Parameters
    /// * `project_id` The Google Cloud Project ID (e.g., "my-project-123").
    /// * `secret_id` The Google Cloud Project ID (e.g., "my-secret").
    /// * `member` The member to add (e.g., "user:user@example.com").
    ///
    /// # Returns
    /// The new IAM policy.
    pub async fn sample(project_id: &str, secret_id: &str, member: &str) -> anyhow::Result<Policy> {
        const ROLE: &str = "roles/secretmanager.secretAccessor";
        const ATTEMPTS: u32 = 5;
    
        let secret_name = format!("projects/{project_id}/secrets/{secret_id}");
        let client = SecretManagerService::builder().build().await?;
        for _attempt in 0..ATTEMPTS {
            let mut current = client
                .get_iam_policy()
                .set_resource(&secret_name)
                .send()
                .await?;
    
            match current.bindings.iter_mut().find(|b| b.role == ROLE) {
                None => current
                    .bindings
                    .push(Binding::new().set_role(ROLE).set_members([member])),
                Some(b) => {
                    if b.members.iter().any(|m| m == member) {
                        return Ok(current);
                    }
                    b.members.push(member.to_string());
                }
            };
            let updated = client
                .set_iam_policy()
                .set_resource(&secret_name)
                .set_policy(current)
                .set_update_mask(FieldMask::default().set_paths(["bindings"]))
                .send()
                .await;
            match updated {
                Ok(p) => return Ok(p),
                Err(e)
                    if e.status().is_some_and(|s| {
                        s.code == Code::Aborted || s.code == Code::FailedPrecondition
                    }) =>
                {
                    continue;
                }
                Err(e) => return Err(e.into()),
            }
        }
        anyhow::bail!("could not set IAM policy after {ATTEMPTS} attempts")
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
