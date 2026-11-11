---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-wss/
title: Collect Symantec Web Security Service (WSS) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:27:02.212904+00:00
---

# Collect Symantec Web Security Service (WSS) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-wss/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec Web Security Service (WSS) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec Web Security Service (WSS) logs to Google Security Operations using Cloud Storage. The parser first attempts to parse the log message as JSON. If that fails, it uses a series of increasingly specific grok patterns to extract fields from the raw text, ultimately mapping the extracted data to the Unified Data Model (UDM). Symantec Web Security Service (WSS) is a cloud-based web security solution that provides real-time protection against web-based threats, including malware, phishing, and data loss.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Symantec Web Security Service Portal



## Collect Symantec WSS API credentials

### Get Symantec WSS site URL

  1. Sign in to your Symantec Web Security Service portal.
  2. Note your portal URL from the browser address bar. 
     * Format: `https://portal.threatpulse.com` or your organization-specific URL
     * Example: If you access WSS at `https://portal.threatpulse.com/reportpod`, your site URL is `https://portal.threatpulse.com`



### Create API credentials

  1. Sign in to the **Symantec Web Security Service Portal** as an administrator.
  2. Go to **Account > API Credentials**.
  3. Click **Add API Credentials**. The portal displays the **Add API Credential** dialog with auto-generated **Username** and **Password**.
  4. Copy and save the **Username** and **Password** securely.

**Note:** These credentials are only displayed once. If you lose them, you will need to generate new credentials.
  5. Select the **API Expiry** option:

     * **Time-based** : Define the date and time when this token expires.
     * **Never expires** : Token remains valid indefinitely (recommended for production).
  6. For the **Access** option, select **Reporting Access Logs**.

  7. Click **Save**.




### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the **Symantec Web Security Service Portal**.
  2. Go to **Account > API Credentials**.
  3. If you can see the API credentials you created with **Access** set to **Reporting Access Logs** , you have the required permissions.
  4. If you cannot see this option, contact your administrator to grant **Reporting Access Logs** permission.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        WSS_USERNAME="your-api-username"
        WSS_PASSWORD="your-api-password"
        WSS_SYNC_URL="https://portal.threatpulse.com/reportpod/logs/sync"
        
        # startDate must be within the last 7 days. This requests logs from the start of the current hour.
        START_MS=$(( $(date +%s) / 3600 * 3600 * 1000 ))
        
        curl -sS -o wss-test.zip -w "HTTP %{http_code}\n" \
          -H "X-APIUsername: ${WSS_USERNAME}" \
          -H "X-APIPassword: ${WSS_PASSWORD}" \
          "${WSS_SYNC_URL}?token=none&startDate=${START_MS}&maxmb=10"
        
        # The sync status is appended to the end of the response, after the ZIP data
        tail -c 300 wss-test.zip | strings | grep -i "X-sync"
        
        # List the log files in the archive
        unzip -l wss-test.zip
        




Expected result:

  * `HTTP 200`.
  * Two lines `X-sync-token: ...` and `X-sync-status: done` (or `more`).
  * A list of `.log.gz` files, for example `cloud_<tenant_ID>_<timestamp>.log.gz`. The list is empty if there are no logs for the current hour yet.

**Note:** Run this test only once. Requests with `token=none` start a new sync, and the Sync API blocks clients that send too many of them, raising a 409 error.

## Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `symantec-wss-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to the Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **Google Cloud console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `symantec-wss-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Symantec WSS logs`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
     3. Click **\+ Add another role**.
     4. Search for and select **Cloud Run Invoker**.
     5. Click **\+ Add another role**.
     6. Search for and select **Cloud Functions Invoker**.
  6. Click **Continue**.
  7. Click **Done**.



These roles are required for:

  * **Storage Object Admin** : Writes logs to the Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allows Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allows function invocation



### Grant IAM permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `symantec-wss-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **Google Cloud console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `symantec-wss-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Symantec WSS Sync API and write them to Cloud Storage.

The Sync API returns a ZIP archive of gzip-compressed log files. The function extracts the archive and writes each `.log.gz` file to the bucket as a separate object, because the feed cannot read log files inside a ZIP archive. The function stores the sync token returned by the API in a state file, so each run continues exactly where the previous run stopped.

  1. In the **Google Cloud console** , go to **Cloud Run**.
  2. Click **Write a function**.
  3. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `symantec-wss-collector`  
**Region** | Select the region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  4. In the **Trigger** section, click **Add trigger** and select **Pub/Sub trigger**.

  5. In the **Eventarc trigger** pane, provide the following configuration details:

     * **Trigger name** : Keep the generated name or enter a name for the trigger.
     * **Trigger type** : Select **Google Sources**.
     * **Event provider** : Select **Pub/Sub**.
     * **Event type** : Select **google.cloud.pubsub.topic.v1.messagePublished**.
     * **Select a Cloud Pub/Sub topic** : Choose the topic `symantec-wss-trigger`.
     * **Region** : Select the same region as the function.
     * **Service account** : Select the service account `symantec-wss-collector-sa`.
  6. Click **Save trigger**.

**Note:** The trigger options come from Eventarc. If **Pub/Sub trigger** is not listed, enable the **Eventarc API** for the project and reload the page. If the pane reports that the service account is missing the **Eventarc Event Receiver** or **Cloud Run Invoker** role, click **Grant**.
  7. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check**Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  8. Navigate to and and expand **Containers, Networking, Security**.

  9. Go to the **Security** tab:

     * **Service account** : Select the service account (`symantec-wss-collector-sa`).
  10. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `symantec-wss-logs` | GCS bucket name  
`GCS_PREFIX` | `symantec/wss/` | Prefix for log files  
`STATE_KEY` | `symantec-wss-state.json` | State path, outside the log prefix  
`WSS_SYNC_URL` | `https://portal.threatpulse.com/reportpod/logs/sync` | WSS Sync API endpoint  
`WSS_API_USERNAME` | `your-api-username` (from API credentials) | WSS API username  
`WSS_API_PASSWORD` | `your-api-password` (from API credentials) | WSS API password  
`INITIAL_LOOKBACK_HOURS` | `1` | Hours of logs to collect on the first run (maximum 167, because the Sync API returns at most the last 7 days)  
`WSS_MAX_MB` | `100` | Approximate maximum size of one Sync API response in MB (1 to 2560)  
`HTTP_TIMEOUT` | `120` | HTTP read timeout in seconds  
`MAX_RETRIES` | `3` | Maximum retry attempts for network errors and HTTP 5xx responses  
`RUN_BUDGET_SECONDS` | `480` | Time after which the function stops requesting new pages; keep it below the request timeout  
`USER_AGENT` | `symantec-wss-to-gcs/2.0` | User agent string  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  11. In the **Variables & Secrets** section, navigate to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  12. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **1 GiB** or higher. The function holds one Sync API response (up to `WSS_MAX_MB`) in memory while it extracts it.
       * **CPU** : Select **1**.
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `1`. The Sync API allows one client per sync token, so runs must not overlap.
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** will open automatically.




### Add the function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.api_core import [exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html) as gcs_exceptions
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import io
    import json
    import os
    import re
    import time
    import uuid
    import zipfile
    from datetime import datetime, timedelta, timezone
    from urllib.parse import urlencode
    import urllib3
    
    http = urllib3.PoolManager(retries=False)
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # The Sync API returns a ZIP archive of gzipped ELFF files followed by a
    # plain-text footer with the X-sync-token and X-sync-status lines.
    ZIP_SIGNATURES = (b'PK\x03\x04', b'PK\x05\x06')  # archive with files, empty archive
    FOOTER_SCAN_BYTES = 4096
    TOKEN_RE = re.compile(rb'X-sync-token:\s*(\S+)', re.IGNORECASE)
    STATUS_RE = re.compile(rb'X-sync-status:\s*(\S+)', re.IGNORECASE)
    MAX_LOOKBACK = timedelta(days=7)
    THROTTLE_WAIT_SECONDS = 60
    MIN_SECONDS_PER_REQUEST = 120
    
    class SyncApiError(Exception):
        """The Sync API returned a response that must not be processed."""
    
    class TokenExpired(Exception):
        """The Sync API rejected the saved token (HTTP 410)."""
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """Fetch Symantec WSS access logs from the Sync API and write them to GCS."""
        bucket_name = os.environ['GCS_BUCKET']
        prefix = os.environ.get('GCS_PREFIX', 'symantec/wss/')
        state_key = os.environ.get('STATE_KEY', 'symantec-wss-state.json')
        sync_url = os.environ.get('WSS_SYNC_URL', 'https://portal.threatpulse.com/reportpod/logs/sync')
        username = os.environ['WSS_API_USERNAME']
        password = os.environ['WSS_API_PASSWORD']
        lookback_hours = int(os.environ.get('INITIAL_LOOKBACK_HOURS', '1'))
        max_mb = int(os.environ.get('WSS_MAX_MB', '100'))
        http_timeout = int(os.environ.get('HTTP_TIMEOUT', '120'))
        max_retries = int(os.environ.get('MAX_RETRIES', '3'))
        run_budget = int(os.environ.get('RUN_BUDGET_SECONDS', '480'))
        user_agent = os.environ.get('USER_AGENT', 'symantec-wss-to-gcs/2.0')
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        state, generation = load_state(bucket, state_key)
        deadline = time.monotonic() + run_budget
    
        while time.monotonic() + MIN_SECONDS_PER_REQUEST <= deadline:
            token = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('token') or 'none'
            params = {'token': token, 'maxmb': max_mb}
            if token == 'none':
                params['startDate'] = initial_start_ms(state, lookback_hours)
            requested_at = datetime.now(timezone.utc)
    
            try:
                body = fetch_page(sync_url, params, username, password, user_agent,
                                  http_timeout, max_retries, deadline)
            except TokenExpired:
                # Restart the sync from the hour of the last successful page.
                # Events from that hour can be ingested again.
                print('Sync token expired (HTTP 410). Restarting with token=none.')
                state['token'] = None
                generation = save_state(bucket, state_key, state, generation)
                continue
            if body is None:
                print('Sync API is throttling requests. The next run continues from the saved token.')
                return
    
            archive, next_token, status = split_footer(body)
            if status not in ('more', 'done'):
                raise SyncApiError(
                    f'X-sync-status is {status!r}. The data was discarded; the next run retries token {token!r}.')
    
            written = write_archive(bucket, prefix, archive)
            [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).update({
                'token': next_token,
                'last_status': status,
                'last_success': requested_at.isoformat(),
            })
            # resume_ms is where a restart after an expired token begins: the
            # startDate of a new sync, then the hour of the last fully synced point.
            if token == 'none':
                state['resume_ms'] = params['startDate']
            if status == 'done':
                state['resume_ms'] = hour_floor_ms(requested_at)
            generation = save_state(bucket, state_key, state, generation)
            print(f'Wrote {len(written)} log files ({len(archive)} bytes), X-sync-status: {status}')
    
            if status == 'done':
                # The API expects at least 60 seconds before the next request.
                print('Sync is up to date.')
                return
            time.sleep(1)
    
        print('Run time budget reached. The next run continues from the saved token.')
    
    def initial_start_ms(state, lookback_hours):
        """startDate for a token=none request: within the last 7 days, at an hour boundary."""
        now = datetime.now(timezone.utc)
        oldest_ms = hour_floor_ms(now - MAX_LOOKBACK) + 3600 * 1000
        start_ms = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('resume_ms') or hour_floor_ms(now - timedelta(hours=lookback_hours))
        return max(start_ms, oldest_ms)
    
    def hour_floor_ms(dt):
        return int(dt.replace(minute=0, second=0, microsecond=0).timestamp() * 1000)
    
    def fetch_page(sync_url, params, username, password, user_agent, timeout, max_retries, deadline):
        """Return the response body, None when throttled past the deadline, or raise."""
        url = f'{sync_url}?{urlencode(params)}'
        headers = {
            'User-Agent': user_agent,
            'X-APIUsername': username,
            'X-APIPassword': password,
        }
        failures = 0
        while True:
            try:
                response = http.request('GET', url, headers=headers,
                                        timeout=urllib3.Timeout(connect=10.0, read=timeout))
            except urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).HTTPError as e:
                failures += 1
                if failures > max_retries:
                    raise
                print(f'Request failed ({e}), retry {failures}/{max_retries}')
                time.sleep(min(30, 2 ** failures))
                continue
    
            if response.status == 200:
                return response.data
            if response.status == 410:
                raise TokenExpired()
            if response.status in (423, 429):
                # 423: another request with this token is in progress. 429: throttled.
                wait = retry_after_seconds(response)
                if time.monotonic() + wait + MIN_SECONDS_PER_REQUEST > deadline:
                    return None
                print(f'HTTP {response.status}, waiting {wait}s')
                time.sleep(wait)
                continue
            if response.status >= 500:
                failures += 1
                if failures <= max_retries:
                    print(f'HTTP {response.status}, retry {failures}/{max_retries} with the same token')
                    time.sleep(min(30, 2 ** failures))
                    continue
            detail = response.data[:500].decode('utf-8', errors='replace')
            raise SyncApiError(f'HTTP {response.status}: {detail}')
    
    def retry_after_seconds(response):
        value = response.headers.get('Retry-After', '')
        return int(value) if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).isdigit() else THROTTLE_WAIT_SECONDS
    
    def split_footer(body):
        """Split the response into the ZIP archive bytes, X-sync-token and X-sync-status."""
        tail_start = max(0, len(body) - FOOTER_SCAN_BYTES)
        tail = body[tail_start:]
        token_match = TOKEN_RE.search(tail)
        status_match = STATUS_RE.search(tail)
        if not token_match or not status_match:
            raise SyncApiError(
                f'Response of {len(body)} bytes has no X-sync-token/X-sync-status footer (incomplete download).')
        footer_start = tail_start + min(token_match.start(), status_match.start())
        token = token_match.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1).decode('ascii')
        status = status_match.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1).decode('ascii').lower()
        return body[:footer_start], token, status
    
    def write_archive(bucket, prefix, archive):
        """Upload every file in the ZIP archive to GCS as a separate object."""
        if not archive:
            return []
        if not archive.startswith(ZIP_SIGNATURES):
            raise SyncApiError(f'Expected a ZIP archive, got bytes starting with {archive[:8]!r}')
    
        date_path = datetime.now(timezone.utc).strftime('%Y/%m/%d')
        batch_id = f'{int(time.time())}_{uuid.uuid4().hex[:8]}'
        written = []
        with zipfile.ZipFile(io.BytesIO(archive)) as zf:
            for member in zf.infolist():
                if member.is_dir():
                    continue
                file_name = os.path.basename(member.filename)
                blob_name = f'{prefix}{date_path}/{batch_id}_{file_name}'
                content_type = 'application/gzip' if file_name.endswith('.gz') else 'text/plain'
                # if_generation_match=0 creates the object only if it does not exist,
                # which also makes the upload safe to retry.
                bucket.blob(blob_name).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                    zf.read(member), content_type=content_type, if_generation_match=0)
                written.append(blob_name)
        return written
    
    def load_state(bucket, key):
        """Return the saved state and its object generation (0 if there is no state yet)."""
        blob = bucket.[get_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_get_blob)(key)
        if blob is None:
            return {}, 0
        return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()), blob.generation
    
    def save_state(bucket, key, state, generation):
        """Save the state only if no other run changed it since it was loaded."""
        blob = bucket.blob(key)
        try:
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(state), content_type='application/json',
                                    if_generation_match=generation)
        except gcs_exceptions.PreconditionFailed:
            raise RuntimeError(f'{key} was changed by another run; stopping to avoid a token conflict.')
        return blob.generation
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **Google Cloud console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `symantec-wss-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`symantec-wss-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click your function name (`symantec-wss-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Wrote N log files (X bytes), X-sync-status: done
         Sync is up to date.
         

If the Sync API has more data than fits in one response, the log shows several `Wrote N log files` lines with `X-sync-status: more` before the final `done`.

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder (`symantec/wss/`).

  11. Verify that new `.log.gz` files were created, for example `symantec/wss/YYYY/MM/DD/<run_ID>_cloud_<tenant_ID>_<timestamp>.log.gz`. The run does not create files if Symantec WSS has no new logs.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables. Verify username and password are correct.
  * **HTTP 403** : Verify API credentials have "Reporting Access Logs" permission enabled in WSS portal.
  * **HTTP 400** : The first request of a sync used a start date older than 7 days. Lower `INITIAL_LOOKBACK_HOURS`.
  * **HTTP 409** : Too many requests started a new sync with `token=none`. Wait 90 minutes before the next run.
  * **HTTP 423 or 429** : Another request is in progress, or the Sync API is throttling requests. The function waits and retries. If the wait doesn't fit in the run time, the next run continues from the saved token.
  * **Sync token expired (HTTP 410)** : The function restarts the sync from the hour of the last completed sync. Some events from that hour can be ingested again.
  * **X-sync-status is 'abort'** or **no X-sync-token/X-sync-status footer** : The response was incomplete and was discarded. The next run retries with the same token.
  * **Expected a ZIP archive** : The Sync API returned something other than a log archive. Check the response with the test in Test API access.
  * **Changed by another run** : Two runs overlapped. Set **Maximum number of instances** to `1`.
  * **KeyError** for a variable name: Check that all required environment variables are set in the Cloud Run function configuration.

**Note:** If you are upgrading from an earlier version of this function that wrote `.bin` files to the bucket: 

  * The `.bin` files are ZIP archives that the feed cannot parse. Delete them from the feed prefix.
  * The function doesn't use the state file of the earlier version. Its first run starts a new sync `INITIAL_LOOKBACK_HOURS` back. To collect again the logs that were written as `.bin` files, set `INITIAL_LOOKBACK_HOURS` to cover that period (up to `167` hours) before the first run. The function collects the backlog over several runs.
  * For `.bin` files older than 7 days, rename each file to `.zip`, extract it, and upload the `.log.gz` files that it contains to the feed prefix.



## Configure a feed in Google SecOps to ingest Symantec WSS logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Symantec WSS logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Symantec WSS** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
    
    gs://symantec-wss-logs/symantec/wss/
    

     * Replace:

     * `symantec-wss-logs`: Your Cloud Storage bucket name.

     * `symantec/wss/`: Optional prefix or folder path where logs are stored (leave empty for root).

**Examples:** \- Root bucket: `gs://company-logs/` \- With prefix: `gs://company-logs/symantec-wss/` \- With subfolder: `gs://company-logs/symantec/wss/`

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select both of the following:
     * **Storage Object Viewer** : reads the log objects.
     * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`content_type_label` | `additional.fields` | Merged  
`cs_uri_extension_label` | `additional.fields` | Merged  
`cs_uri_path_label` | `additional.fields` | Merged  
`hostname_categories_label` | `additional.fields` | Merged  
`_intermediary` | `intermediary` | Merged  
`msg_desc` | `metadata.description` | Directly mapped  
`s_action` | `metadata.description` | Directly mapped  
`device_time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`log_time` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`timestamp` | `metadata.event_timestamp` | Parsed as `UNIX`  
`when` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`s-action` | `metadata.product_event_type` | Directly mapped  
`product_data.x-bluecoat-transaction-uuid` | `metadata.product_log_id` | Directly mapped  
`ref_uid` | `metadata.product_log_id` | Directly mapped  
`uuid` | `metadata.product_log_id` | Directly mapped  
`x-bluecoat-transaction-uuid` | `metadata.product_log_id` | Directly mapped  
`product_name` | `metadata.product_name` | Directly mapped  
`product_ver` | `metadata.product_version` | Directly mapped  
`connection.url.scheme` | `network.application_protocol` | Directly mapped  
`cs-uri-scheme` | `network.application_protocol` | Mapped: `(?i)https` → `HTTPS`  
`uri_scheme` | `network.application_protocol` | Directly mapped  
`cs-version` | `network.application_protocol_version` | Directly mapped  
`connection.url.method` | `network.http.method` | Directly mapped  
`cs-method` | `network.http.method` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`cs_referer` | `network.http.referral_url` | Directly mapped  
`connection.http_status` | `network.http.response_code` | Renamed/mapped  
`status` | `network.http.response_code` | Directly mapped  
`connection.http_user_agent` | `network.http.user_agent` | Directly mapped  
`cs(user-agent)` | `network.http.user_agent` | Directly mapped  
`http_user_agent` | `network.http.user_agent` | Directly mapped  
`connection.url.scheme` | `network.ip_protocol` | Directly mapped  
`uri_scheme` | `network.ip_protocol` | Directly mapped  
`connection.bytes_download` | `network.received_bytes` | Renamed/mapped  
`received_bytes` | `network.received_bytes` | Renamed/mapped  
`connection.bytes_upload` | `network.sent_bytes` | Renamed/mapped  
`sent_bytes` | `network.sent_bytes` | Renamed/mapped  
`time_taken` | `network.session_duration.seconds` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`cs_connection_negotiated_cipher` | `network.tls.cipher` | Directly mapped  
`product_data.x-cs-connection-negotiated-cipher` | `network.tls.cipher` | Directly mapped  
`x-cs-connection-negotiated-cipher` | `network.tls.cipher` | Directly mapped  
`certificate_hostname` | `network.tls.client.server_name` | Directly mapped  
`product_data.x-rs-certificate-hostname` | `network.tls.client.server_name` | Directly mapped  
`x-rs-certificate-hostname` | `network.tls.client.server_name` | Directly mapped  
`product_data.x-rs-certificate-observed-errors` | `network.tls.server.certificate.issuer` | Directly mapped  
`x-rs-certificate-observed-errors` | `network.tls.server.certificate.issuer` | Directly mapped  
`certificate_validate` | `network.tls.server.certificate.subject` | Directly mapped  
`product_data.x-rs-certificate-validate-status` | `network.tls.server.certificate.subject` | Directly mapped  
`x-rs-certificate-validate-status` | `network.tls.server.certificate.subject` | Directly mapped  
`connection.tls.version` | `network.tls.version_protocol` | Directly mapped  
`cs_ssl_version` | `network.tls.version_protocol` | Directly mapped  
`product_data.x-cs-connection-negotiated-ssl-version` | `network.tls.version_protocol` | Directly mapped  
`x-cs-connection-negotiated-ssl-version` | `network.tls.version_protocol` | Directly mapped  
`agent_type` | `observer.application` | Directly mapped  
`product_data.x-client-agent-type` | `observer.application` | Directly mapped  
`x-client-agent-type` | `observer.application` | Directly mapped  
`os_version` | `observer.platform_version` | Directly mapped  
`product_data.x-client-agent-sw` | `observer.platform_version` | Directly mapped  
`x-client-agent-sw` | `observer.platform_version` | Directly mapped  
`user_domain` | `principal.administrative_domain` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`c-ip` | `principal.asset.ip` | Merged  
`c_ip` | `principal.asset.ip` | Merged  
`collector_device_ip` | `principal.asset.ip` | Merged  
`connection.src_ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`x-sr-vpop-ip` | `principal.asset.ip` | Merged  
`x-client-os` | `principal.asset.platform_software.platform` | Mapped: `Windows` → `WINDOWS`  
`hostname` | `principal.hostname` | Directly mapped  
`c-ip` | `principal.ip` | Merged  
`c_ip` | `principal.ip` | Merged  
`collector_device_ip` | `principal.ip` | Merged  
`connection.src_ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`x-sr-vpop-ip` | `principal.ip` | Merged  
`product_data.r-supplier-country` | `principal.location.country_or_region` | Directly mapped  
`r-supplier-country` | `principal.location.country_or_region` | Directly mapped  
`supplier_country` | `principal.location.country_or_region` | Directly mapped  
`src_port` | `principal.port` | Renamed/mapped  
`x-client-device-id` | `principal.resource.product_object_id` | Directly mapped  
`user.name` | `principal.user.user_display_name` | Directly mapped  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`cs-userdn` | `principal.user.userid` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`filter_result` | `security_result.action_details` | Directly mapped  
`result` | `security_result.action_details` | Directly mapped  
`rs_icap_status` | `security_result.action_details` | Directly mapped  
`category_details` | `security_result.category_details` | Merged  
`cs-categories` | `security_result.category_details` | Merged  
`cs-icap-status` | `security_result.description` | Directly mapped  
`cs_icap_status` | `security_result.description` | Directly mapped  
`product_data.cs-icap-status` | `security_result.description` | Directly mapped  
`additional_x_tenant_id` | `security_result.detection_fields` | Merged  
`architecture_label` | `security_result.detection_fields` | Merged  
`content_type_label` | `security_result.detection_fields` | Merged  
`risk_groups_label` | `security_result.detection_fields` | Merged  
`rs_negotiated_cipher_size_label` | `security_result.detection_fields` | Merged  
`verdict_label` | `security_result.detection_fields` | Merged  
`x_bluecoat_access_type_label` | `security_result.detection_fields` | Merged  
`x_bluecoat_application_operation_label` | `security_result.detection_fields` | Merged  
`x_cs_connection_negotiated_cipher_size_label` | `security_result.detection_fields` | Merged  
`x_data_leak_detected` | `security_result.detection_fields` | Merged  
`x_rs_certificate_hostname_threat_risk_label` | `security_result.detection_fields` | Merged  
`x_rs_connection_negotiated_cipher_label` | `security_result.detection_fields` | Merged  
`x_rs_connection_negotiated_cipher_size_label` | `security_result.detection_fields` | Merged  
`x_rs_connection_negotiated_ssl_version_label` | `security_result.detection_fields` | Merged  
`x_rs_ocsp_error_label` | `security_result.detection_fields` | Merged  
`x_x_virus_id_label` | `security_result.detection_fields` | Merged  
`rule_name1` | `security_result.rule_name` | Directly mapped  
`severity_id` | `security_result.severity` | Mapped: `1 , 2` → `LOW`, `3 , 4` → `MEDIUM`, `5 , 6` → `HIGH`  
`product_data.x-exception-id` | `security_result.summary` | Directly mapped  
`device_name` | `src.asset.hostname` | Directly mapped  
`product_data.x-client-device-name` | `src.asset.hostname` | Directly mapped  
`x-client-device-name` | `src.asset.hostname` | Directly mapped  
`connection.src_ip` | `src.asset.ip` | Merged  
`device_name` | `src.hostname` | Directly mapped  
`product_data.x-client-device-name` | `src.hostname` | Directly mapped  
`x-client-device-name` | `src.hostname` | Directly mapped  
`connection.src_ip` | `src.ip` | Merged  
`product_data.x_bluecoat_application_name` | `target.application` | Directly mapped  
`target_application` | `target.application` | Directly mapped  
`x_bluecoat_application_name` | `target.application` | Directly mapped  
`connection.dst_name` | `target.asset.hostname` | Directly mapped  
`connection.url.host` | `target.asset.hostname` | Directly mapped  
`cs-host` | `target.asset.hostname` | Directly mapped  
`device_name` | `target.asset.hostname` | Directly mapped  
`connection.dst_ip` | `target.asset.ip` | Merged  
`s-ip` | `target.asset.ip` | Merged  
`target_ip` | `target.asset.ip` | Merged  
`os_name` | `target.asset.platform_software.platform` | Mapped: `Windows` → `WINDOWS`, `macOS` → `MAC`  
`os_ver` | `target.asset.platform_software.platform_version` | Directly mapped  
`connection.dst_name` | `target.hostname` | Directly mapped  
`connection.url.host` | `target.hostname` | Directly mapped  
`cs-host` | `target.hostname` | Directly mapped  
`device_name` | `target.hostname` | Directly mapped  
`connection.dst_ip` | `target.ip` | Merged  
`s-ip` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`ip_geo_artifact_entry` | `target.ip_geo_artifact` | Merged  
`client_country` | `target.location.country_or_region` | Directly mapped  
`connection.dst_location.country` | `target.location.country_or_region` | Directly mapped  
`product_data.x-cs-client-ip-country` | `target.location.country_or_region` | Directly mapped  
`x-cs-client-ip-country` | `target.location.country_or_region` | Directly mapped  
`connection.dst_port` | `target.port` | Renamed/mapped  
`cs-uri-port` | `target.port` | Renamed/mapped  
`device_id` | `target.resource.id` | Directly mapped  
`product_data.x-client-device-id` | `target.resource.id` | Directly mapped  
`device_id` | `target.resource.product_object_id` | Directly mapped  
`product_data.x-client-device-id` | `target.resource.product_object_id` | Directly mapped  
`x_bluecoat_location_id` | `target.resource.product_object_id` | Directly mapped  
`connection.url.path` | `target.url` | Directly mapped  
`connection.url.text` | `target.url` | Directly mapped  
`target_url` | `target.url` | Directly mapped  
`uri_query` | `target.url` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_UNCATEGORIZED`  
N/A | `metadata.product_event_type` | Constant: `Security`  
N/A | `metadata.vendor_name` | Constant: `SYMANTEC`  
N/A | `network.http.parsed_user_agent` | Constant: `cs(user-agent)}`  
N/A | `principal.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `target.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `target.resource.type` | Constant: `DEVICE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-wss-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
