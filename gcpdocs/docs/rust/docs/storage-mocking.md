---
url: https://docs.cloud.google.com/rust/docs/storage-mocking/
title: Write tests using a mock Cloud Storage client \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:54:00.874507+00:00
---

# Write tests using a mock Cloud Storage client  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/storage-mocking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Write tests using a mock Cloud Storage client Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Client Libraries for Rust provide a way to stub real client implementations so that you can inject a mock for testing. You can use mocks to write controlled, reliable unit tests that don't make network calls or incur billed charges.

In this document, you learn about the following topics:

  * How to write testable interfaces using the Cloud Storage `Storage` client.
  * How to mock read operations.
  * How to mock write operations.
  * Why the design of the `Storage` client differs from other Google Cloud clients.

**Note:** This document covers mocking the `Storage` client specifically. For more information about mocking other clients, including `StorageControl`, see [Write tests using a mock client](https://docs.cloud.google.com/rust/docs/mocking).

## Dependencies

Add the Cloud Storage client library to your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage
    

To compile and run the unit tests in this document, add the following development dependencies:
    
    
    cargo add --dev anyhow bytes mockall
    cargo add --dev tokio --features macros,rt-multi-thread
    

## Write testable interfaces

If you don't unit test your storage code, you can write interfaces directly in terms of `Storage`, whose default stub type parameter is the production implementation of the client:
    
    
    pub async fn my_function(_client: Storage) {}

To test your code with a mock client, write your interfaces in terms of a generic type parameter `T` constrained by `gcs::stub::Storage + 'static`:
    
    
    pub async fn my_testable_function<T>(_client: Storage<T>)
    where
        T: gcs::stub::Storage + 'static,
    {
    }

## Mock read operations

To mock `read_object` requests, complete the following steps:

  1. Write an application function that takes a generic `&Storage<T>` client. For example, the following function downloads an object and counts how many newline characters it contains: 
         
         // Downloads an object from GCS and counts the total lines.
         pub async fn count_newlines<T>(
             client: &Storage<T>,
             bucket_id: &str,
             object_id: &str,
         ) -> gcs::Result<usize>
         where
             T: gcs::stub::Storage + 'static,
         {
             let mut count = 0;
             let mut reader = client
                 .read_object(format!("projects/_/buckets/{bucket_id}"), object_id)
                 .set_generation(42)
                 .send()
                 .await?;
             while let Some(buffer) = reader.next().await.transpose()? {
                 count += buffer.into_iter().filter(|c| *c == b'\n').count();
             }
             Ok(count)
         }

  2. Create a helper function that constructs a fake `ReadObjectResponse` stream of bytes by passing a payload to `ReadObjectResponse::from_source`. This method accepts the same payload types as `Storage::write_object`: 
         
         fn fake_response(size: usize) -> ReadObjectResponse {
             let mut contents = String::new();
             for i in 0..size {
                 contents.push_str(&format!("{i}\n"))
             }
             ReadObjectResponse::from_source(ObjectHighlights::default(), bytes::Bytes::from(contents))
         }

  3. Define a mock struct that implements `gcs::stub::Storage`. This document uses the `mockall` crate, though you can use a different mocking framework in your tests: 
         
         mockall::mock! {
             #[derive(Debug)]
             Storage {}
             impl gcs::stub::Storage for Storage {
                 async fn read_object(&self, _req: ReadObjectRequest, _options: RequestOptions) -> Result<ReadObjectResponse>;
                 async fn write_object_buffered<P: StreamingSource + Send + Sync + 'static>(
                     &self,
                     _payload: P,
                     _req: WriteObjectRequest,
                     _options: RequestOptions,
                 ) -> Result<Object>;
                 async fn write_object_unbuffered<P: StreamingSource + Seek + Send + Sync + 'static>(
                     &self,
                     _payload: P,
                     _req: WriteObjectRequest,
                     _options: RequestOptions,
                 ) -> Result<Object>;
             }
         }

  4. Write a unit test that sets expectations on the mock, constructs a client using `Storage::from_stub`, and calls `count_newlines`: 
         
         #[tokio::test]
         async fn test_count_lines() -> anyhow::Result<()> {
             let mut mock = MockStorage::new();
             mock.expect_read_object().return_once({
                 move |r, _| {
                     // Verify contents of the request
                     assert_eq!(r.generation, 42);
                     assert_eq!(r.bucket, "projects/_/buckets/my-bucket");
                     assert_eq!(r.object, "my-object");
         
                     // Return a `ReadObjectResponse`
                     Ok(fake_response(100))
                 }
             });
             let client = gcs::client::Storage::from_stub(mock);
         
             let count = count_newlines(&client, "my-bucket", "my-object").await?;
             assert_eq!(count, 100);
         
             Ok(())
         }




## Mock write operations

To mock `write_object` requests, complete the following steps:

  1. Write an application function that uploads an object using a generic `&Storage<T>` client: 
         
         // Uploads an object to GCS.
         pub async fn upload<T>(client: &Storage<T>, bucket_id: &str, object_id: &str) -> gcs::Result<Object>
         where
             T: gcs::stub::Storage + 'static,
         {
             client
                 .write_object(
                     format!("projects/_/buckets/{bucket_id}"),
                     object_id,
                     "payload",
                 )
                 .set_if_generation_match(42)
                 .send_unbuffered()
                 .await
         }

  2. Using the `MockStorage` struct defined in the previous section, write a unit test that configures expectations on the mock, constructs a client using `Storage::from_stub`, and calls `upload`: 
         
         #[tokio::test]
         async fn test_upload() -> anyhow::Result<()> {
             let mut mock = MockStorage::new();
             mock.expect_write_object_unbuffered()
                 .return_once(
                     |_payload: Payload<BytesSource>, r, _| {
                         // Verify contents of the request
                         assert_eq!(r.spec.if_generation_match, Some(42));
                         let o = r.spec.resource.unwrap_or_default();
                         assert_eq!(o.bucket, "projects/_/buckets/my-bucket");
                         assert_eq!(o.name, "my-object");
         
                         // Return the object
                         Ok(Object::default()
                             .set_bucket("projects/_/buckets/my-bucket")
                             .set_name("my-object")
                             .set_generation(42))
                     },
                 );
             let client = gcs::client::Storage::from_stub(mock);
         
             let object = upload(&client, "my-bucket", "my-object").await?;
             assert_eq!(object.generation, 42);
         
             Ok(())
         }




### Expectation details

Because the `upload` function calls `send_unbuffered`, set the expectation on the corresponding `expect_write_object_unbuffered` method:
    
    
    mock.expect_write_object_unbuffered()

The `mockall::mock!` macro treats each generic instantiation as a distinct method. Specify the concrete payload type, `Payload<BytesSource>`, in the closure signature so that the compiler can match the method expectation:
    
    
    |_payload: Payload<BytesSource>, r, _| {

## Design rationale

The following sections explain why the `Storage` client uses a generic type parameter for its stub rather than dynamic dispatch.

### Other clients

Most clients, such as `StorageControl`, hold a reference-counted (`Arc`), `dyn`-compatible implementation of their stub trait internally. They use dynamic dispatch to forward requests from the client to the underlying stub, which can be either the production implementation or a mock.

Because these clients use dynamic dispatch, the compiler doesn't need to resolve the concrete stub type at compile time, and the client structs don't need a generic type parameter for their stub.

### The `Storage` client

In Rust, a `dyn`-compatible trait can't have generic methods or return unboxed `impl Future` values:

  * The `write_object_buffered` and `write_object_unbuffered` methods are generic over the payload source type.
  * The `gcs::stub::Storage` trait methods return `impl Future` directly instead of boxing the returned future.



Using dynamic dispatch for the `Storage` client would require boxing payloads and futures on every call, adding heap allocations and dynamic dispatch overhead on the data path. To avoid this overhead, the `Storage` client uses a type parameter for a concrete implementation of the `gcs::stub::Storage` trait instead.

## Complete application code and test suite

The following code combines the application functions and unit tests into a complete example:
    
    
    use gcs::client::Storage;
    use gcs::model::Object;
    use google_cloud_storage as gcs;
    
    // Downloads an object from GCS and counts the total lines.
    pub async fn count_newlines<T>(
        client: &Storage<T>,
        bucket_id: &str,
        object_id: &str,
    ) -> gcs::Result<usize>
    where
        T: gcs::stub::Storage + 'static,
    {
        let mut count = 0;
        let mut reader = client
            .read_object(format!("projects/_/buckets/{bucket_id}"), object_id)
            .set_generation(42)
            .send()
            .await?;
        while let Some(buffer) = reader.next().await.transpose()? {
            count += buffer.into_iter().filter(|c| *c == b'\n').count();
        }
        Ok(count)
    }
    
    // Uploads an object to GCS.
    pub async fn upload<T>(client: &Storage<T>, bucket_id: &str, object_id: &str) -> gcs::Result<Object>
    where
        T: gcs::stub::Storage + 'static,
    {
        client
            .write_object(
                format!("projects/_/buckets/{bucket_id}"),
                object_id,
                "payload",
            )
            .set_if_generation_match(42)
            .send_unbuffered()
            .await
    }
    
    #[cfg(test)]
    mod tests {
        use super::{count_newlines, upload};
        use gcs::Result;
        use gcs::model::{Object, ReadObjectRequest};
        use gcs::model_ext::{ObjectHighlights, WriteObjectRequest};
        use gcs::read_object::ReadObjectResponse;
        use gcs::request_options::RequestOptions;
        use gcs::streaming_source::{BytesSource, Payload, Seek, StreamingSource};
        use google_cloud_storage as gcs;
    
        mockall::mock! {
            #[derive(Debug)]
            Storage {}
            impl gcs::stub::Storage for Storage {
                async fn read_object(&self, _req: ReadObjectRequest, _options: RequestOptions) -> Result<ReadObjectResponse>;
                async fn write_object_buffered<P: StreamingSource + Send + Sync + 'static>(
                    &self,
                    _payload: P,
                    _req: WriteObjectRequest,
                    _options: RequestOptions,
                ) -> Result<Object>;
                async fn write_object_unbuffered<P: StreamingSource + Seek + Send + Sync + 'static>(
                    &self,
                    _payload: P,
                    _req: WriteObjectRequest,
                    _options: RequestOptions,
                ) -> Result<Object>;
            }
        }
    
        fn fake_response(size: usize) -> ReadObjectResponse {
            let mut contents = String::new();
            for i in 0..size {
                contents.push_str(&format!("{i}\n"))
            }
            ReadObjectResponse::from_source(ObjectHighlights::default(), bytes::Bytes::from(contents))
        }
    
        #[tokio::test]
        async fn test_count_lines() -> anyhow::Result<()> {
            let mut mock = MockStorage::new();
            mock.expect_read_object().return_once({
                move |r, _| {
                    // Verify contents of the request
                    assert_eq!(r.generation, 42);
                    assert_eq!(r.bucket, "projects/_/buckets/my-bucket");
                    assert_eq!(r.object, "my-object");
    
                    // Return a `ReadObjectResponse`
                    Ok(fake_response(100))
                }
            });
            let client = gcs::client::Storage::from_stub(mock);
    
            let count = count_newlines(&client, "my-bucket", "my-object").await?;
            assert_eq!(count, 100);
    
            Ok(())
        }
    
        #[tokio::test]
        async fn test_upload() -> anyhow::Result<()> {
            let mut mock = MockStorage::new();
            mock.expect_write_object_unbuffered()
                .return_once(
                    |_payload: Payload<BytesSource>, r, _| {
                        // Verify contents of the request
                        assert_eq!(r.spec.if_generation_match, Some(42));
                        let o = r.spec.resource.unwrap_or_default();
                        assert_eq!(o.bucket, "projects/_/buckets/my-bucket");
                        assert_eq!(o.name, "my-object");
    
                        // Return the object
                        Ok(Object::default()
                            .set_bucket("projects/_/buckets/my-bucket")
                            .set_name("my-object")
                            .set_generation(42))
                    },
                );
            let client = gcs::client::Storage::from_stub(mock);
    
            let object = upload(&client, "my-bucket", "my-object").await?;
            assert_eq!(object.generation, 42);
    
            Ok(())
        }
    }

Run `cargo test` to execute `test_count_lines` and `test_upload`:
    
    
    cargo test
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
