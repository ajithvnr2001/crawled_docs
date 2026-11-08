---
url: https://docs.cloud.google.com/rust/docs/mocking-lros/
title: Write tests for long-running operations \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T05:38:28.258145+00:00
---

# Write tests for long-running operations  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/mocking-lros/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Write tests for long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud Client Libraries for Rust provide helpers that simplify interaction with long-running operations (LROs). Simulating the behavior of LROs in unit tests involves understanding the underlying details that these helpers abstract away. This guide shows you how to write unit tests for both automatic and manual LRO polling, including error scenarios.

## Prerequisites

This guide assumes that you are familiar with the following guides:

  * [Working with long-running operations](https://docs.cloud.google.com/rust/docs/long-running-operations)
  * [Write tests using a mock client](https://docs.cloud.google.com/rust/docs/mocking)



## Test automatic polling

Assume that your application code awaits `lro::Poller::until_done()` (automatic polling):
    
    
    // An example application function that automatically polls.
    //
    // It starts an LRO, awaits the result, and processes it.
    pub async fn my_automatic_poller(
        client: &speech::client::Speech,
        project_id: &str,
    ) -> Result<Option<wkt::Duration>> {
        use google_cloud_lro::Poller;
        client
            .batch_recognize()
            .set_recognizer(format!(
                "projects/{project_id}/locations/global/recognizers/_"
            ))
            .poller()
            .until_done()
            .await
            .map(|r| r.total_billed_duration)
    }

Because the application only uses the final result of the LRO, you don't need to test how it handles intermediate polling results. Your test can return the final result of the LRO directly from the mock.

### Create the `longrunning::model::Operation`

Assume that you want the call to return the following response:
    
    
    fn expected_duration() -> Option<wkt::Duration> {
        Some(wkt::Duration::clamp(100, 0))
    }
    
    fn expected_response() -> BatchRecognizeResponse {
        BatchRecognizeResponse::new().set_or_clear_total_billed_duration(expected_duration())
    }

The stub returns a `longrunning::model::Operation` rather than a `BatchRecognizeResponse`. Pack the expected response into `Operation::result`:
    
    
    fn make_finished_operation(response: &BatchRecognizeResponse) -> Result<Response<Operation>> {
        let any = wkt::Any::from_msg(response).expect("test message should succeed");
        let operation = Operation::new()
            .set_done(true)
            .set_result(OperationResult::Response(any.into()));
        Ok(Response::from(operation))
    }

Set the `done` field to `true` to indicate to the `Poller` that the operation is complete, ending the polling loop:
    
    
    .set_done(true)

### Write the test

  1. Define the mock struct, which implements the [`speech::stub::Speech`](https://docs.rs/google-cloud-speech-v2/latest/google_cloud_speech_v2/stub/trait.Speech.html) trait: 
         
         mockall::mock! {
             #[derive(Debug)]
             Speech {}
             impl speech::stub::Speech for Speech {
                 async fn batch_recognize(&self, req: BatchRecognizeRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
             }
         }

  2. In the test, create the mock and set expectations on it: 
         
         let mut mock = MockSpeech::new();
         mock.expect_batch_recognize()
             .return_once(|_, _| make_finished_operation(&expected_response()));

  3. Create a client from the mock, call the function, and verify the response: 
         
         // Create a client, implemented by our mock.
         let client = speech::client::Speech::from_stub(mock);
         
         // Call our function which automatically polls.
         let billed_duration = my_automatic_poller(&client, "my-project").await?;
         
         // Verify the final result of the LRO.
         assert_eq!(billed_duration, expected_duration());




## Test manual polling with intermediate metadata

Assume that your application code polls manually and processes partial updates:
    
    
    pub struct BatchRecognizeResult {
        pub progress_updates: Vec<i32>,
        pub billed_duration: Result<Option<wkt::Duration>>,
    }
    
    // An example application function that manually polls.
    //
    // It starts an LRO. It consolidates the polling results, whether full or
    // partial.
    //
    // In this case, it is the `BatchRecognize` RPC. If we get a partial update,
    // we extract the `progress_percent` field. If we get a final result, we
    // extract the `total_billed_duration` field.
    pub async fn my_manual_poller(
        client: &speech::client::Speech,
        project_id: &str,
    ) -> BatchRecognizeResult {
        use google_cloud_lro::{Poller, PollingResult};
        let mut progress_updates = Vec::new();
        let mut poller = client
            .batch_recognize()
            .set_recognizer(format!(
                "projects/{project_id}/locations/global/recognizers/_"
            ))
            .poller();
        while let Some(p) = poller.poll().await {
            match p {
                PollingResult::Completed(r) => {
                    let billed_duration = r.map(|r| r.total_billed_duration);
                    return BatchRecognizeResult {
                        progress_updates,
                        billed_duration,
                    };
                }
                PollingResult::InProgress(m) => {
                    if let Some(metadata) = m {
                        // This is a silly application. Your application likely
                        // performs some task immediately with the partial
                        // update, instead of storing it for after the operation
                        // has completed.
                        progress_updates.push(metadata.progress_percent);
                    }
                }
                PollingResult::PollingError(e) => {
                    return BatchRecognizeResult {
                        progress_updates,
                        billed_duration: Err(e),
                    };
                }
            }
            tokio::time::sleep(std::time::Duration::from_millis(500)).await;
        }
    
        // We can only get here if `poll()` returns `None`, but it only returns
        // `None` after it returned `PollingResult::Completed`. Therefore this
        // is never reached.
        unreachable!("loop should exit via the `Completed` branch.");
    }

You can simulate how the application behaves when it receives intermediate metadata by returning in-progress operations from the mock.

### Create the `longrunning::model::Operation`

The `BatchRecognize` RPC returns partial results as a `speech::model::OperationMetadata`. Pack this metadata into the `Operation::metadata` field of the returned `longrunning::model::Operation`:
    
    
    fn make_partial_operation(progress: i32) -> Result<Response<Operation>> {
        let metadata = OperationMetadata::new().set_progress_percent(progress);
        let any = wkt::Any::from_msg(&metadata).expect("test message should succeed");
        let operation = Operation::new().set_metadata(any);
        Ok(Response::from(operation))
    }

### Write the test

  1. Define the mock struct, which implements the [`speech::stub::Speech`](https://docs.rs/google-cloud-speech-v2/latest/google_cloud_speech_v2/stub/trait.Speech.html) trait and overrides `get_operation()`: 
         
         mockall::mock! {
             #[derive(Debug)]
             Speech {}
             impl speech::stub::Speech for Speech {
                 async fn batch_recognize(&self, req: BatchRecognizeRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
                 async fn get_operation(&self, req: GetOperationRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
             }
         }

  2. In the test, create the mock and set expectations on it to return partial results (25%, 50%, 75%) followed by the final outcome: 
         
         let mut seq = mockall::Sequence::new();
         let mut mock = MockSpeech::new();
         mock.expect_batch_recognize()
             .once()
             .in_sequence(&mut seq)
             .returning(|_, _| make_partial_operation(25));
         mock.expect_get_operation()
             .once()
             .in_sequence(&mut seq)
             .returning(|_, _| make_partial_operation(50));
         mock.expect_get_operation()
             .once()
             .in_sequence(&mut seq)
             .returning(|_, _| make_partial_operation(75));
         mock.expect_get_operation()
             .once()
             .in_sequence(&mut seq)
             .returning(|_, _| make_finished_operation(&expected_response()));

Note the following details about how the expectations are configured:

     * **Initial vs. subsequent RPCs:** The first expectation is set on `batch_recognize()`, whereas all subsequent expectations are set on `get_operation()`. The initial `BatchRecognize` RPC starts the LRO on the server and returns an operation identifier in the `name` field (omitted from the test code for brevity). From then on, the client library polls the status of that LRO using the `GetOperation` RPC.
     * **Call ordering:** Expectations are registered in a [`Sequence`](https://docs.rs/mockall/latest/mockall/struct.Sequence.html). This lets `mockall` verify the order of the calls and determine which `expect_get_operation` expectation matches each poll.
  3. Create a client from the mock, call the function, and verify the response: 
         
         // Create a client, implemented by our mock.
         let client = speech::client::Speech::from_stub(mock);
         
         // Call our function which manually polls.
         let result = my_manual_poller(&client, "my-project").await;
         
         // Verify the partial metadata updates, and the final result.
         assert_eq!(result.progress_updates, [25, 50, 75]);
         assert_eq!(result.billed_duration?, expected_duration());




## Simulate errors

Errors can arise at several points during an LRO.

If your application uses automatic polling, all error sources are equivalent: `until_done()` returns the error in the `Result`, regardless of where it originated. Simulating an error starting an LRO produces the simplest test.

**Note:** A client created from a stub does not have a retry or polling policy. In all cases, the polling loop terminates on the first error, even if the error is normally considered transient.

### Simulate an error starting an LRO

To simulate an error when starting an LRO, configure the initial request to fail with an error:
    
    
    mock.expect_batch_recognize().return_once(|_, _| {
        use gax::error::Error;
        use gax::error::rpc::{Code, Status};
        let status = Status::default()
            .set_code(Code::Aborted)
            .set_message("Resource exhausted");
        Err(Error::service(status))
    });

For manual polling, the `PollingResult::Completed` branch receives the error from starting the LRO, which ends the polling loop:
    
    
    PollingResult::Completed(r) => {

### Simulate an LRO resulting in an error

To simulate an LRO that fails after returning intermediate metadata, return the error in the final `longrunning::model::Operation`:
    
    
    fn make_failed_operation(status: rpc::model::Status) -> Result<Response<Operation>> {
        let operation = Operation::new()
            .set_done(true)
            .set_result(OperationResult::Error(status.into()));
        Ok(Response::from(operation))
    }

Set expectations to return the failed `Operation` from `get_operation`:
    
    
    mock.expect_get_operation()
        .once()
        .in_sequence(&mut seq)
        .returning(|_, _| {
            // This is a common error for `Create*` RPCs, which are often
            // LROs. It is less applicable to `BatchRecognize` in practice.
            let status = rpc::model::Status::default()
                .set_code(gax::error::rpc::Code::AlreadyExists as i32)
                .set_message("resource already exists");
            make_failed_operation(status)
        });

In manual polling, the `PollingResult::Completed` branch receives the error outcome, ending the polling loop:
    
    
    PollingResult::Completed(r) => {

### Simulate a polling error

Polling loops can also exit when the polling policy is exhausted. When this happens, the client library can't determine definitively whether the LRO completed.

If your application has custom logic to handle polling errors, you can test it by returning an error directly from the `get_operation` expectation:
    
    
    mock.expect_get_operation()
        .once()
        .in_sequence(&mut seq)
        .returning(|_, _| {
            use gax::error::Error;
            use gax::error::rpc::{Code, Status};
            let status = Status::default()
                .set_code(Code::Aborted)
                .set_message("Operation was aborted");
            Err(Error::service(status))
        });

In manual polling, the `PollingResult::PollingError` branch receives the simulated polling error:
    
    
    PollingResult::PollingError(e) => {

## Complete test code

The following sections show the complete code for the tests described in this guide.

### Automatic polling: full test
    
    
    use gax::Result;
    use gax::response::Response;
    use google_cloud_gax as gax;
    use google_cloud_longrunning as longrunning;
    use google_cloud_speech_v2 as speech;
    use google_cloud_wkt as wkt;
    use longrunning::model::Operation;
    use longrunning::model::operation::Result as OperationResult;
    use speech::model::{BatchRecognizeRequest, BatchRecognizeResponse};
    
    // Example application code that is under test
    mod my_application {
        use super::*;
    
        // An example application function that automatically polls.
        //
        // It starts an LRO, awaits the result, and processes it.
        pub async fn my_automatic_poller(
            client: &speech::client::Speech,
            project_id: &str,
        ) -> Result<Option<wkt::Duration>> {
            use google_cloud_lro::Poller;
            client
                .batch_recognize()
                .set_recognizer(format!(
                    "projects/{project_id}/locations/global/recognizers/_"
                ))
                .poller()
                .until_done()
                .await
                .map(|r| r.total_billed_duration)
        }
    }
    
    #[cfg(test)]
    mod tests {
        use super::my_application::*;
        use super::*;
    
        mockall::mock! {
            #[derive(Debug)]
            Speech {}
            impl speech::stub::Speech for Speech {
                async fn batch_recognize(&self, req: BatchRecognizeRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
            }
        }
    
        fn expected_duration() -> Option<wkt::Duration> {
            Some(wkt::Duration::clamp(100, 0))
        }
    
        fn expected_response() -> BatchRecognizeResponse {
            BatchRecognizeResponse::new().set_or_clear_total_billed_duration(expected_duration())
        }
    
        fn make_finished_operation(response: &BatchRecognizeResponse) -> Result<Response<Operation>> {
            let any = wkt::Any::from_msg(response).expect("test message should succeed");
            let operation = Operation::new()
                .set_done(true)
                .set_result(OperationResult::Response(any.into()));
            Ok(Response::from(operation))
        }
    
        #[tokio::test]
        async fn automatic_polling() -> Result<()> {
            // Create a mock, and set expectations on it.
            let mut mock = MockSpeech::new();
            mock.expect_batch_recognize()
                .return_once(|_, _| make_finished_operation(&expected_response()));
    
            // Create a client, implemented by our mock.
            let client = speech::client::Speech::from_stub(mock);
    
            // Call our function which automatically polls.
            let billed_duration = my_automatic_poller(&client, "my-project").await?;
    
            // Verify the final result of the LRO.
            assert_eq!(billed_duration, expected_duration());
    
            Ok(())
        }
    }

### Manual polling with intermediate metadata: full test
    
    
    use gax::Result;
    use gax::response::Response;
    use google_cloud_gax as gax;
    use google_cloud_longrunning as longrunning;
    use google_cloud_speech_v2 as speech;
    use google_cloud_wkt as wkt;
    use longrunning::model::operation::Result as OperationResult;
    use longrunning::model::{GetOperationRequest, Operation};
    use speech::model::{BatchRecognizeRequest, BatchRecognizeResponse, OperationMetadata};
    
    // Example application code that is under test
    mod my_application {
        use super::*;
    
        pub struct BatchRecognizeResult {
            pub progress_updates: Vec<i32>,
            pub billed_duration: Result<Option<wkt::Duration>>,
        }
    
        // An example application function that manually polls.
        //
        // It starts an LRO. It consolidates the polling results, whether full or
        // partial.
        //
        // In this case, it is the `BatchRecognize` RPC. If we get a partial update,
        // we extract the `progress_percent` field. If we get a final result, we
        // extract the `total_billed_duration` field.
        pub async fn my_manual_poller(
            client: &speech::client::Speech,
            project_id: &str,
        ) -> BatchRecognizeResult {
            use google_cloud_lro::{Poller, PollingResult};
            let mut progress_updates = Vec::new();
            let mut poller = client
                .batch_recognize()
                .set_recognizer(format!(
                    "projects/{project_id}/locations/global/recognizers/_"
                ))
                .poller();
            while let Some(p) = poller.poll().await {
                match p {
                    PollingResult::Completed(r) => {
                        let billed_duration = r.map(|r| r.total_billed_duration);
                        return BatchRecognizeResult {
                            progress_updates,
                            billed_duration,
                        };
                    }
                    PollingResult::InProgress(m) => {
                        if let Some(metadata) = m {
                            // This is a silly application. Your application likely
                            // performs some task immediately with the partial
                            // update, instead of storing it for after the operation
                            // has completed.
                            progress_updates.push(metadata.progress_percent);
                        }
                    }
                    PollingResult::PollingError(e) => {
                        return BatchRecognizeResult {
                            progress_updates,
                            billed_duration: Err(e),
                        };
                    }
                }
                tokio::time::sleep(std::time::Duration::from_millis(500)).await;
            }
    
            // We can only get here if `poll()` returns `None`, but it only returns
            // `None` after it returned `PollingResult::Completed`. Therefore this
            // is never reached.
            unreachable!("loop should exit via the `Completed` branch.");
        }
    }
    
    #[cfg(test)]
    mod tests {
        use super::my_application::*;
        use super::*;
    
        mockall::mock! {
            #[derive(Debug)]
            Speech {}
            impl speech::stub::Speech for Speech {
                async fn batch_recognize(&self, req: BatchRecognizeRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
                async fn get_operation(&self, req: GetOperationRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
            }
        }
    
        fn expected_duration() -> Option<wkt::Duration> {
            Some(wkt::Duration::clamp(100, 0))
        }
    
        fn expected_response() -> BatchRecognizeResponse {
            BatchRecognizeResponse::new().set_or_clear_total_billed_duration(expected_duration())
        }
    
        fn make_finished_operation(
            response: &BatchRecognizeResponse,
        ) -> Result<gax::response::Response<Operation>> {
            let any = wkt::Any::from_msg(response).expect("test message should succeed");
            let operation = Operation::new()
                .set_done(true)
                .set_result(OperationResult::Response(any.into()));
            Ok(Response::from(operation))
        }
    
        fn make_partial_operation(progress: i32) -> Result<Response<Operation>> {
            let metadata = OperationMetadata::new().set_progress_percent(progress);
            let any = wkt::Any::from_msg(&metadata).expect("test message should succeed");
            let operation = Operation::new().set_metadata(any);
            Ok(Response::from(operation))
        }
    
        #[tokio::test]
        async fn manual_polling_with_metadata() -> Result<()> {
            let mut seq = mockall::Sequence::new();
            let mut mock = MockSpeech::new();
            mock.expect_batch_recognize()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_partial_operation(25));
            mock.expect_get_operation()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_partial_operation(50));
            mock.expect_get_operation()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_partial_operation(75));
            mock.expect_get_operation()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_finished_operation(&expected_response()));
    
            // Create a client, implemented by our mock.
            let client = speech::client::Speech::from_stub(mock);
    
            // Call our function which manually polls.
            let result = my_manual_poller(&client, "my-project").await;
    
            // Verify the partial metadata updates, and the final result.
            assert_eq!(result.progress_updates, [25, 50, 75]);
            assert_eq!(result.billed_duration?, expected_duration());
    
            Ok(())
        }
    }

### Simulating errors: full tests
    
    
    use gax::Result;
    use gax::response::Response;
    use google_cloud_gax as gax;
    use google_cloud_longrunning as longrunning;
    use google_cloud_rpc as rpc;
    use google_cloud_speech_v2 as speech;
    use google_cloud_wkt as wkt;
    use longrunning::model::operation::Result as OperationResult;
    use longrunning::model::{GetOperationRequest, Operation};
    use speech::model::{BatchRecognizeRequest, OperationMetadata};
    
    // Example application code that is under test
    mod my_application {
        use super::*;
    
        pub struct BatchRecognizeResult {
            pub progress_updates: Vec<i32>,
            pub billed_duration: Result<Option<wkt::Duration>>,
        }
    
        // An example application function that manually polls.
        //
        // It starts an LRO. It consolidates the polling results, whether full or
        // partial.
        //
        // In this case, it is the `BatchRecognize` RPC. If we get a partial update,
        // we extract the `progress_percent` field. If we get a final result, we
        // extract the `total_billed_duration` field.
        pub async fn my_manual_poller(
            client: &speech::client::Speech,
            project_id: &str,
        ) -> BatchRecognizeResult {
            use google_cloud_lro::{Poller, PollingResult};
            let mut progress_updates = Vec::new();
            let mut poller = client
                .batch_recognize()
                .set_recognizer(format!(
                    "projects/{project_id}/locations/global/recognizers/_"
                ))
                .poller();
            while let Some(p) = poller.poll().await {
                match p {
                    PollingResult::Completed(r) => {
                        let billed_duration = r.map(|r| r.total_billed_duration);
                        return BatchRecognizeResult {
                            progress_updates,
                            billed_duration,
                        };
                    }
                    PollingResult::InProgress(m) => {
                        if let Some(metadata) = m {
                            // This is a silly application. Your application likely
                            // performs some task immediately with the partial
                            // update, instead of storing it for after the operation
                            // has completed.
                            progress_updates.push(metadata.progress_percent);
                        }
                    }
                    PollingResult::PollingError(e) => {
                        return BatchRecognizeResult {
                            progress_updates,
                            billed_duration: Err(e),
                        };
                    }
                }
                tokio::time::sleep(std::time::Duration::from_millis(500)).await;
            }
    
            // We can only get here if `poll()` returns `None`, but it only returns
            // `None` after it returned `PollingResult::Completed`. Therefore this
            // is never reached.
            unreachable!("loop should exit via the `Completed` branch.");
        }
    }
    
    #[cfg(test)]
    mod tests {
        use super::my_application::*;
        use super::*;
    
        mockall::mock! {
            #[derive(Debug)]
            Speech {}
            impl speech::stub::Speech for Speech {
                async fn batch_recognize(&self, req: BatchRecognizeRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
                async fn get_operation(&self, req: GetOperationRequest, _options: gax::options::RequestOptions) -> Result<Response<Operation>>;
            }
        }
    
        fn make_partial_operation(progress: i32) -> Result<Response<Operation>> {
            let metadata = OperationMetadata::new().set_progress_percent(progress);
            let any = wkt::Any::from_msg(&metadata).expect("test message should succeed");
            let operation = Operation::new().set_metadata(any);
            Ok(Response::from(operation))
        }
    
        fn make_failed_operation(status: rpc::model::Status) -> Result<Response<Operation>> {
            let operation = Operation::new()
                .set_done(true)
                .set_result(OperationResult::Error(status.into()));
            Ok(Response::from(operation))
        }
    
        #[tokio::test]
        async fn error_starting_lro() -> Result<()> {
            let mut mock = MockSpeech::new();
            mock.expect_batch_recognize().return_once(|_, _| {
                use gax::error::Error;
                use gax::error::rpc::{Code, Status};
                let status = Status::default()
                    .set_code(Code::Aborted)
                    .set_message("Resource exhausted");
                Err(Error::service(status))
            });
    
            // Create a client, implemented by our mock.
            let client = speech::client::Speech::from_stub(mock);
    
            // Call our function which manually polls.
            let result = my_manual_poller(&client, "my-project").await;
    
            // Verify the the final result.
            assert!(
                result.billed_duration.is_err(),
                "{:?}",
                result.billed_duration
            );
    
            Ok(())
        }
    
        #[tokio::test]
        async fn lro_ending_in_error() -> Result<()> {
            let mut seq = mockall::Sequence::new();
            let mut mock = MockSpeech::new();
            mock.expect_batch_recognize()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_partial_operation(25));
            mock.expect_get_operation()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_partial_operation(50));
            mock.expect_get_operation()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_partial_operation(75));
            mock.expect_get_operation()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| {
                    // This is a common error for `Create*` RPCs, which are often
                    // LROs. It is less applicable to `BatchRecognize` in practice.
                    let status = rpc::model::Status::default()
                        .set_code(gax::error::rpc::Code::AlreadyExists as i32)
                        .set_message("resource already exists");
                    make_failed_operation(status)
                });
    
            // Create a client, implemented by our mock.
            let client = speech::client::Speech::from_stub(mock);
    
            // Call our function which manually polls.
            let result = my_manual_poller(&client, "my-project").await;
    
            // Verify the partial metadata updates, and the final result.
            assert_eq!(result.progress_updates, [25, 50, 75]);
            assert!(
                result.billed_duration.is_err(),
                "{:?}",
                result.billed_duration
            );
    
            Ok(())
        }
    
        #[tokio::test]
        async fn polling_loop_error() -> Result<()> {
            let mut seq = mockall::Sequence::new();
            let mut mock = MockSpeech::new();
            mock.expect_batch_recognize()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| make_partial_operation(25));
            mock.expect_get_operation()
                .once()
                .in_sequence(&mut seq)
                .returning(|_, _| {
                    use gax::error::Error;
                    use gax::error::rpc::{Code, Status};
                    let status = Status::default()
                        .set_code(Code::Aborted)
                        .set_message("Operation was aborted");
                    Err(Error::service(status))
                });
    
            // Create a client, implemented by our mock.
            let client = speech::client::Speech::from_stub(mock);
    
            // Call our function which manually polls.
            let result = my_manual_poller(&client, "my-project").await;
    
            // Verify the partial metadata updates, and the final result.
            assert_eq!(result.progress_updates, [25]);
            assert!(
                result.billed_duration.is_err(),
                "{:?}",
                result.billed_duration
            );
    
            Ok(())
        }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
