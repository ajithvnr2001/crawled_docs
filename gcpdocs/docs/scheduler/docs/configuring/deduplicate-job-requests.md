---
url: https://docs.cloud.google.com/scheduler/docs/configuring/deduplicate-job-requests/
title: Deduplicate job requests \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T14:05:06.484682+00:00
---

# Deduplicate job requests  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/configuring/deduplicate-job-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Deduplicate job requests Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Scheduler includes job identification and schedule-time HTTP headers on HTTP and App Engine requests that let you deduplicate retried executions and make your target handlers [idempotent](https://cloud.google.com/discover/idempotency). Because Cloud Scheduler provides _at-least-once_ delivery, deduplicating requests prevents your handler or downstream Google Cloud APIs from processing the same scheduled run more than once when timeouts or transient network interruptions occur.

## How request deduplication works

Duplicate job requests for the same scheduled run can occur in the following situations:

  * **Long-running targets** : The target service takes longer to respond than the job's [attempt deadline (`attemptDeadline`)](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.attempt_deadline), causing Cloud Scheduler to time out and [retry the job](https://docs.cloud.google.com/scheduler/docs/configuring/retry-jobs) while the first attempt is still running. For HTTP targets, `attemptDeadline` defaults to 3 minutes and can be configured up to 30 minutes. Align `attemptDeadline` with your target's timeout, or process long-running work asynchronously if execution can exceed 30 minutes.
  * **Lost network acknowledgments or transient proxy retries** : The target receives and processes the request, but a transient network interruption or proxy disconnect prevents Cloud Scheduler from receiving the HTTP `2xx` response. Even if you set `retryCount` to `0`, at-least-once delivery means a target can still receive duplicate requests during transient transport failures.



To make your job handler idempotent and deduplicate retried requests, use the [HTTP headers](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#HttpTarget) that Cloud Scheduler automatically includes on requests to HTTP and App Engine targets:

Header | Description  
---|---  
`X-CloudScheduler-JobName` | The short job identifier (`JOB_ID`) from `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`.  
`X-CloudScheduler-ScheduleTime` | For jobs specified in [`unix-cron` format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules#cron_job_format), the scheduled execution time as an offset of UTC formatted according to RFC 3339—for example, `2026-10-16T12:00:00Z` or `2026-10-16T05:00:00-07:00`. This value remains constant across all retry attempts for the same scheduled run. This header isn't guaranteed for jobs that use the [alternative `groc` schedule format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules#use-groc), such as `every 5 minutes`. If you trigger a job manually (for example, by running `gcloud scheduler jobs run` or clicking **Force a job run** in the Google Cloud console), this header uses the next scheduled run's timestamp or might be omitted. As a result, header-based deduplication skips that upcoming scheduled run and any additional manual runs triggered before that scheduled time.  
  
### Require authentication on your target endpoint

The `X-CloudScheduler-*` headers aren't authenticated and can be set by any caller. Don't use these headers for authentication. Instead, secure your endpoint based on the target type:

  * **HTTP targets** : Configure the job to send an OIDC or OAuth token and require authentication on your endpoint. For more information, see [Use authentication with HTTP targets](https://docs.cloud.google.com/scheduler/docs/http-target-auth).
  * **App Engine targets** : Restrict access to the handler by setting [`login: admin`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_login) in your `app.yaml` file and configuring [App Engine firewall rules](https://docs.cloud.google.com/appengine/docs/standard/understanding-firewalls#allowing_incoming_requests_from_your_services).



### Use case-insensitive header lookups

Header capitalization can vary across HTTP versions and infrastructure (for example, `X-Cloudscheduler-Jobname` in HTTP/1.1 or lowercase `x-cloudscheduler-jobname` and `x-cloudscheduler-scheduletime` in HTTP/2 environments such as Cloud Run). Always use case-insensitive header lookups in your handler.

### Disambiguate job IDs across projects or regions

Cloud Scheduler doesn't automatically send project ID or region headers. A single handler endpoint might receive requests from multiple projects or regions that share the same `JOB_ID`. In this case, pass the project ID or region in [`HttpTarget.headers`](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#HttpTarget.FIELDS.headers), [`AppEngineHttpTarget.headers`](https://docs.cloud.google.com/scheduler/docs/reference/rest/v1/projects.locations.jobs#AppEngineHttpTarget.FIELDS.headers), or the target URL path or query parameters, and include those values in your deduplication key.

## Deduplicate requests in an HTTP handler

Before you implement request deduplication in your handler, complete the following setup prerequisites:

  * Configure your job's schedule in [`unix-cron` format](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules#cron_job_format) (for example, `*/5 * * * *` instead of `every 5 minutes`) so that Cloud Scheduler sends the `X-CloudScheduler-ScheduleTime` header.
  * Set up a persistent datastore that supports transactions or atomic conditional writes, such as [Firestore](https://docs.cloud.google.com/firestore/docs), [Spanner](https://docs.cloud.google.com/spanner/docs), or [Memorystore](https://docs.cloud.google.com/memorystore/docs). Configure a [time-to-live (TTL) policy](https://docs.cloud.google.com/firestore/native/docs/ttl) on the collection or table (for example, on the `expire_at` field) to delete old deduplication records after the job's retry window (`maxRetryDuration`). Firestore TTL deletes expired records asynchronously, typically within 24-72 hours. To let retries reclaim runs from crashed instances before TTL cleanup, also store a lease expiration timestamp (such as `lease_expires`, set to at least your target's request timeout and `attemptDeadline`) and evaluate it in a transaction.



To process each scheduled run only once in your HTTP handler, complete the following steps:

  1. Read `X-CloudScheduler-JobName` and `X-CloudScheduler-ScheduleTime` from the incoming request headers and hash them into a fixed-length deduplication key (`run_id`).
  2. Run a transaction in your datastore to check and claim the record for the deduplication key: 
     * If the record exists and `status` is `completed`, return an HTTP `200 OK` (or `204 No Content`) status code immediately without running the job logic so that Cloud Scheduler stops retrying.
     * If the record exists, `status` is `in_progress`, and the lease (`lease_expires`) hasn't expired, return a retryable error status code such as `409 Conflict` so that Cloud Scheduler keeps its retry policy active in case the in-flight attempt fails. Avoid returning `503 Service Unavailable` from App Engine targets, because App Engine treats `503` as a system error and retries the request without counting it against `retryCount`.
     * If the record doesn't exist or its lease has expired, write the record with `status` set to `in_progress`, a unique attempt ID (`attempt_id`), a lease expiration timestamp (`lease_expires`), and a TTL expiration timestamp (`expire_at`).
  3. After claiming the record, run your job logic. In a transaction, verify that the record's `attempt_id` still matches the current attempt before modifying the record:

     * If the job logic succeeds, update `status` to `completed` and return an HTTP `200 OK` status code.
     * If the job logic fails with an error that you can retry, delete the deduplication record before returning a `5xx` status code so that Cloud Scheduler can retry the run without waiting for the lease to expire.
**Note:** Cloud Scheduler treats any `2xx` response (`200`–`299`) as a successful acknowledgment and stops retrying the run. Return `2xx` for a duplicate request only after an attempt has completed (or if your handler processes the accepted request asynchronously and manages its own retries).



### Example HTTP handler

The following Python example (for [Cloud Run](https://docs.cloud.google.com/run/docs) or [Cloud Run functions](https://docs.cloud.google.com/functions/docs)) uses a Firestore transaction with a lease to claim runs and deduplicate retried job requests.

This sample isn't production-ready. Review and adjust it to your needs before deploying:
    
    
    import datetime
    import hashlib
    import uuid
    
    import flask
    import functions_framework
    from google.cloud import firestore
    
    # Longer than the work takes, and at least the job's attempt deadline.
    LEASE = datetime.timedelta(minutes=5)
    # Keep records past the job's retry window. A TTL policy on expire_at deletes them.
    RETENTION = datetime.timedelta(days=1)
    
    db = firestore.Client()
    
    
    def run_job_logic() -> None:
        """Does the scheduled work. Replace the body with your own task."""
    
    
    @firestore.transactional
    def claim_run(
        transaction: firestore.Transaction,
        run_ref: firestore.DocumentReference,
        attempt_id: str,
        now: datetime.datetime,
    ) -> str:
        """Claims the run unless it's done or another attempt holds the lease."""
        snapshot = run_ref.get(transaction=transaction)
        if snapshot.exists:
            run = snapshot.to_dict()
            if run["status"] == "completed":
                return "completed"
            if run["lease_expires"] > now:
                return "in_progress"
        transaction.set(
            run_ref,
            {
                "status": "in_progress",
                "attempt_id": attempt_id,
                "lease_expires": now + LEASE,
                "expire_at": now + RETENTION,
            },
        )
        return "claimed"
    
    
    @firestore.transactional
    def finish_run(
        transaction: firestore.Transaction,
        run_ref: firestore.DocumentReference,
        attempt_id: str,
        succeeded: bool,
    ) -> None:
        """Completes or releases the run, if this attempt still holds the claim."""
        snapshot = run_ref.get(transaction=transaction)
        if not snapshot.exists or snapshot.to_dict().get("attempt_id") != attempt_id:
            return  # A retry claimed the run after this attempt's lease expired.
        if succeeded:
            transaction.update(run_ref, {"status": "completed"})
        else:
            transaction.delete(run_ref)
    
    
    @functions_framework.http
    def handle_scheduled_job(request: flask.Request) -> tuple[str, int]:
        """Runs a job's work once per scheduled run, even if the run is delivered twice."""
        job_name = request.headers.get("X-CloudScheduler-JobName")
        schedule_time = request.headers.get("X-CloudScheduler-ScheduleTime")
        if not job_name or not schedule_time:
            return "error: missing Cloud Scheduler headers", 400
    
        # Retries keep the same schedule time. A forced run uses the next
        # scheduled time, so that scheduled run is then skipped.
        run_id = hashlib.sha256(f"{job_name}/{schedule_time}".encode()).hexdigest()
        run_ref = db.collection("scheduler_runs").document(run_id)
        now = datetime.datetime.now(datetime.timezone.utc)
        attempt_id = uuid.uuid4().hex
    
        status = claim_run(db.transaction(), run_ref, attempt_id, now)
        if status == "completed":
            return "Duplicate run skipped", 200
        if status == "in_progress":
            # A non-2xx response keeps retries going in case that attempt fails.
            return "Run in progress", 409
    
        try:
            run_job_logic()
        except Exception:
            # Releases the claim so that a retry can process the run.
            finish_run(db.transaction(), run_ref, attempt_id, succeeded=False)
            raise
        finish_run(db.transaction(), run_ref, attempt_id, succeeded=True)
        return "Run processed", 200
    
    

## Prevent duplicate requests to Google Cloud API targets

When Cloud Scheduler invokes a Google Cloud API endpoint (`*.googleapis.com`) directly over HTTP, the target API ignores the `X-CloudScheduler-JobName` and `X-CloudScheduler-ScheduleTime` headers. For example, calling `workflowexecutions.googleapis.com` to start a [Workflows execution](https://docs.cloud.google.com/workflows/docs/schedule-workflow), `run.googleapis.com` to run a [Cloud Run job](https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule), or `cloudbuild.googleapis.com` to run a [Cloud Build trigger](https://docs.cloud.google.com/build/docs/schedule-builds) starts a new run on every retry attempt.

For production reliability, enforce idempotency in the most downstream service that modifies state. Deduplicating requests only at an upstream layer narrows the retry window, but if a downstream request succeeds and the HTTP response is lost over the network, the upstream caller can't determine whether the operation completed and might still retry the request.

To prevent duplicate executions when scheduling Google Cloud API targets, use the following approaches together for end-to-end idempotency:

  * **Route requests through an idempotent proxy** : Instead of calling the `*.googleapis.com` endpoint directly from Cloud Scheduler, deploy your own Cloud Run service or Cloud Run function proxy and configure Cloud Scheduler to invoke that proxy. In the proxy, implement the Python and Firestore **atomic** transactional claim pattern described in this document, in Deduplicate requests in an HTTP handler.

The proxy reads `X-CloudScheduler-JobName` and `X-CloudScheduler-ScheduleTime`, deduplicates retried requests, and passes the deduplication key as an idempotency token in the request payload (for example, in the `argument` field when starting a Workflows execution).

Require authentication on the proxy (for example, deploy with `--no-allow-unauthenticated`) and configure the Cloud Scheduler job to [authenticate with an OIDC token](https://docs.cloud.google.com/scheduler/docs/http-target-auth). Run the proxy under a dedicated service account with only the minimum required Identity and Access Management (IAM) roles (such as `roles/workflows.invoker` on the target workflow and `roles/datastore.user` for the deduplication records).

  * **Enforce idempotency in the downstream services** : Use the idempotency token to perform an **atomic** or transactional check in a datastore such as Firestore before running state-changing steps. Pass the token to any downstream HTTP endpoints or Cloud Run functions that your service invokes so that those targets can also deduplicate retries. For an end-to-end example using Workflows, Firestore transactions, and Cloud Run functions, see the Google Cloud blog post, [Making API calls exactly once when using Workflows](https://cloud.google.com/blog/products/application-development/using-single-execution-calls-with-workflows).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
