---
url: https://docs.fish.audio/api-reference/sdk/python/core/
title: Core - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-27T17:34:39.904741+00:00
---

# Core - Fish Audio

> Source: https://docs.fish.audio/api-reference/sdk/python/core/

## On this page

Back to top

  * fishaudio.core.client_wrapper
  * BaseClientWrapper Objects
    * get_headers
  * ClientWrapper Objects
    * request
    * client
    * close
  * AsyncClientWrapper Objects
    * request
    * client
    * close
  * fishaudio.core.request_options
  * RequestOptions Objects
    * get_timeout
  * fishaudio.core.iterators
  * AudioStream Objects
    * __init__
    * __iter__
    * close
    * collect
  * AsyncAudioStream Objects
    * __init__
    * __aiter__
    * aclose
    * collect
  * TTSTimestampStream Objects
    * __init__
    * segments
    * close
    * collect
  * AsyncTTSTimestampStream Objects
    * __init__
    * segments
    * aclose
    * collect
  * fishaudio.core.websocket_options
  * WebSocketOptions Objects
    * to_httpx_ws_kwargs
  * fishaudio.core.omit



Reference

# Core

Copy pageCopy page

Copy pageCopy page

# fishaudio.core.client_wrapper

HTTP client wrapper for managing requests and authentication. Install the Python SDK first: `pip install fish-audio-sdk`.

## BaseClientWrapper Objects
    
    
    class BaseClientWrapper()
    

Base wrapper with shared logic for sync/async clients.

#### get_headers
    
    
    def get_headers(
            additional_headers: Optional[dict[str, str]] = None) -> dict[str, str]
    

Build headers including authentication and user agent.

## ClientWrapper Objects
    
    
    class ClientWrapper(BaseClientWrapper)
    

Wrapper for httpx.Client that handles authentication and error handling.

#### request
    
    
    def request(method: str,
                path: str,
                *,
                request_options: Optional[RequestOptions] = None,
                stream: bool = False,
                **kwargs: Any) -> httpx.Response
    

Make an HTTP request with error handling. **Arguments** :

  * `method` \- HTTP method (GET, POST, etc.)
  * `path` \- API endpoint path
  * `request_options` \- Optional request-level overrides
  * `stream` \- If True, return as soon as the response headers arrive and leave the body unread. The caller must consume it with `iter_bytes()` and then call `close()` on the response.
  * `**kwargs` \- Additional arguments to pass to httpx.request

**Returns** : httpx.Response object **Raises** :

  * `APIError` \- On non-2xx responses



#### client
    
    
    @property
    def client() -> httpx.Client
    

Get underlying httpx.Client for advanced usage (e.g., WebSockets).

#### close
    
    
    def close() -> None
    

Close the HTTP client.

## AsyncClientWrapper Objects
    
    
    class AsyncClientWrapper(BaseClientWrapper)
    

Wrapper for httpx.AsyncClient that handles authentication and error handling.

#### request
    
    
    async def request(method: str,
                      path: str,
                      *,
                      request_options: Optional[RequestOptions] = None,
                      stream: bool = False,
                      **kwargs: Any) -> httpx.Response
    

Make an async HTTP request with error handling. **Arguments** :

  * `method` \- HTTP method (GET, POST, etc.)
  * `path` \- API endpoint path
  * `request_options` \- Optional request-level overrides
  * `stream` \- If True, return as soon as the response headers arrive and leave the body unread. The caller must consume it with `aiter_bytes()` and then call `aclose()` on the response.
  * `**kwargs` \- Additional arguments to pass to httpx.request

**Returns** : httpx.Response object **Raises** :

  * `APIError` \- On non-2xx responses



#### client
    
    
    @property
    def client() -> httpx.AsyncClient
    

Get underlying httpx.AsyncClient for advanced usage (e.g., WebSockets).

#### close
    
    
    async def close() -> None
    

Close the HTTP client.

# fishaudio.core.request_options

Request-level options for API calls.

## RequestOptions Objects
    
    
    class RequestOptions()
    

Options that can be provided on a per-request basis to override client defaults. **Attributes** :

  * `timeout` \- Override the client’s default timeout (in seconds)
  * `max_retries` \- Accepted but not used: the client does not retry requests
  * `additional_headers` \- Additional headers to include in the request
  * `additional_query_params` \- Additional query parameters to include



#### get_timeout
    
    
    def get_timeout() -> Optional[httpx.Timeout]
    

Convert timeout to httpx.Timeout if set.

# fishaudio.core.iterators

Audio stream wrappers with collection utilities.

## AudioStream Objects
    
    
    class AudioStream()
    

Wrapper for sync audio byte streams with collection utilities. This class wraps an iterator of audio bytes and provides a convenient `.collect()` method to gather all chunks into a single bytes object. **Examples** :
    
    
    from fishaudio import FishAudio
    
    client = FishAudio(api_key="...")
    
    # Collect all audio at once
    audio = client.tts.stream(text="Hello!").collect()
    
    # Or stream chunks manually
    for chunk in client.tts.stream(text="Hello!"):
        process_chunk(chunk)
    
    # Use a with-block (or call close()) if you may stop early,
    # so the HTTP connection is released right away
    with client.tts.stream(text="Hello!") as stream:
        for chunk in stream:
            if done(chunk):
                break
    

#### __init__
    
    
    def __init__(iterator: Iterator[bytes],
                 *,
                 on_close: Optional[Callable[[], None]] = None)
    

Initialize the audio iterator wrapper. **Arguments** :

  * `iterator` \- The underlying iterator of audio bytes
  * `on_close` \- Called by close() to release the underlying resource, for example the open HTTP response



#### __iter__
    
    
    def __iter__() -> Iterator[bytes]
    

Allow direct iteration over audio chunks.

#### close
    
    
    def close() -> None
    

Stop the stream and release the underlying connection. Safe to call more than once, and before iteration has started.

#### collect
    
    
    def collect() -> bytes
    

Collect all audio chunks into a single bytes object. This consumes the iterator and returns all audio data as bytes. After calling this method, the iterator cannot be used again. **Returns** : Complete audio data as bytes **Examples** :
    
    
    audio = client.tts.stream(text="Hello!").collect()
    with open("output.mp3", "wb") as f:
        f.write(audio)
    

## AsyncAudioStream Objects
    
    
    class AsyncAudioStream()
    

Wrapper for async audio byte streams with collection utilities. This class wraps an async iterator of audio bytes and provides a convenient `.collect()` method to gather all chunks into a single bytes object. **Examples** :
    
    
    from fishaudio import AsyncFishAudio
    
    client = AsyncFishAudio(api_key="...")
    
    # Collect all audio at once
    stream = await client.tts.stream(text="Hello!")
    audio = await stream.collect()
    
    # Or stream chunks manually
    async for chunk in await client.tts.stream(text="Hello!"):
        await process_chunk(chunk)
    
    # Use async with (or await aclose()) if you may stop early,
    # so the HTTP connection is released right away
    async with await client.tts.stream(text="Hello!") as stream:
        async for chunk in stream:
            if done(chunk):
                break
    

#### __init__
    
    
    def __init__(async_iterator: AsyncIterator[bytes],
                 *,
                 on_close: Optional[Callable[[], Awaitable[None]]] = None)
    

Initialize the async audio iterator wrapper. **Arguments** :

  * `async_iterator` \- The underlying async iterator of audio bytes
  * `on_close` \- Awaited by aclose() to release the underlying resource, for example the open HTTP response



#### __aiter__
    
    
    def __aiter__() -> AsyncIterator[bytes]
    

Allow direct async iteration over audio chunks.

#### aclose
    
    
    async def aclose() -> None
    

Stop the stream and release the underlying connection. Safe to call more than once, and before iteration has started.

#### collect
    
    
    async def collect() -> bytes
    

Collect all audio chunks into a single bytes object. This consumes the async iterator and returns all audio data as bytes. After calling this method, the iterator cannot be used again. **Returns** : Complete audio data as bytes **Examples** :
    
    
    stream = await client.tts.stream(text="Hello!")
    audio = await stream.collect()
    with open("output.mp3", "wb") as f:
        f.write(audio)
    

## TTSTimestampStream Objects
    
    
    class TTSTimestampStream()
    

Sync stream of text-to-speech audio with timestamps. Iterating yields `TTSTimestampEvent` objects as the server produces them. While you iterate, `segments` holds the timings received so far, measured from the start of the complete audio. Alternatively, call `collect()` instead of iterating to get the complete audio with its final timings. **Examples** :
    
    
    from fishaudio import FishAudio
    
    client = FishAudio(api_key="...")
    
    # Play audio as it arrives and keep the timings up to date
    with client.tts.stream_with_timestamps(text="Hello world") as stream:
        for event in stream:
            player.write(event.audio)
            show_captions(stream.segments)
    
    # Or collect everything at once
    result = client.tts.stream_with_timestamps(text="Hello world").collect()
    

#### __init__
    
    
    def __init__(iterator: Iterator[TTSTimestampEvent],
                 *,
                 on_close: Optional[Callable[[], None]] = None)
    

Initialize the stream. **Arguments** :

  * `iterator` \- The underlying iterator of events
  * `on_close` \- Called by close() to release the underlying resource, for example the open HTTP response



#### segments
    
    
    @property
    def segments() -> list[TTSTimestampSegment]
    

Timings received so far, in speaking order. Times are in seconds from the start of the complete audio. Entries near the end can still be corrected by later events, so read this again after each event instead of appending to an earlier copy. Empty until the first timings arrive, and it stays empty when the API has no timings for the text (for example text without words). The audio still arrives in full.

#### close
    
    
    def close() -> None
    

Stop the stream and release the underlying connection. Safe to call more than once, and before iteration has started.

#### collect
    
    
    def collect() -> TTSTimestampResult
    

Read the whole stream and return the complete audio with its timings. Call this instead of iterating, not after it. Events that were already yielded are not kept, so the complete audio can no longer be returned once iteration has started; in that case use the audio you received and read `segments` when the stream ends. **Returns** : TTSTimestampResult with the complete audio and final timings. When the API has no timings for the text, `segments` is empty and `duration` is None; the audio is still complete. **Raises** :

  * `RuntimeError` \- If iteration has already started



## AsyncTTSTimestampStream Objects
    
    
    class AsyncTTSTimestampStream()
    

Async stream of text-to-speech audio with timestamps. Iterating yields `TTSTimestampEvent` objects as the server produces them. While you iterate, `segments` holds the timings received so far, measured from the start of the complete audio. Alternatively, call `collect()` instead of iterating to get the complete audio with its final timings. **Examples** :
    
    
    from fishaudio import AsyncFishAudio
    
    client = AsyncFishAudio(api_key="...")
    
    # Play audio as it arrives and keep the timings up to date
    async with await client.tts.stream_with_timestamps(text="Hello world") as stream:
        async for event in stream:
            await player.write(event.audio)
            show_captions(stream.segments)
    
    # Or collect everything at once
    stream = await client.tts.stream_with_timestamps(text="Hello world")
    result = await stream.collect()
    

#### __init__
    
    
    def __init__(async_iterator: AsyncIterator[TTSTimestampEvent],
                 *,
                 on_close: Optional[Callable[[], Awaitable[None]]] = None)
    

Initialize the stream. **Arguments** :

  * `async_iterator` \- The underlying async iterator of events
  * `on_close` \- Awaited by aclose() to release the underlying resource, for example the open HTTP response



#### segments
    
    
    @property
    def segments() -> list[TTSTimestampSegment]
    

Timings received so far, in speaking order. Times are in seconds from the start of the complete audio. Entries near the end can still be corrected by later events, so read this again after each event instead of appending to an earlier copy. Empty until the first timings arrive, and it stays empty when the API has no timings for the text (for example text without words). The audio still arrives in full.

#### aclose
    
    
    async def aclose() -> None
    

Stop the stream and release the underlying connection. Safe to call more than once, and before iteration has started.

#### collect
    
    
    async def collect() -> TTSTimestampResult
    

Read the whole stream and return the complete audio with its timings. Call this instead of iterating, not after it. Events that were already yielded are not kept, so the complete audio can no longer be returned once iteration has started; in that case use the audio you received and read `segments` when the stream ends. **Returns** : TTSTimestampResult with the complete audio and final timings. When the API has no timings for the text, `segments` is empty and `duration` is None; the audio is still complete. **Raises** :

  * `RuntimeError` \- If iteration has already started



# fishaudio.core.websocket_options

WebSocket-level options for WebSocket connections.

## WebSocketOptions Objects
    
    
    class WebSocketOptions()
    

Options for configuring WebSocket connections. These options are passed directly to httpx_ws’s connect_ws/aconnect_ws functions. For complete documentation, see <https://frankie567.github.io/httpx-ws/reference/httpx_ws/> **Attributes** :

  * `keepalive_ping_timeout_seconds` \- Maximum delay the client will wait for an answer to its Ping event. If the delay is exceeded, WebSocketNetworkError will be raised and the connection closed. Default: 20 seconds.
  * `keepalive_ping_interval_seconds` \- Interval at which the client will automatically send a Ping event to keep the connection alive. Default: 20 seconds. `None` keeps the default; it does not turn the pings off.
  * `max_message_size_bytes` \- Message size in bytes to receive from the server. Default: 65536 bytes (64 KiB).
  * `queue_size` \- Size of the queue where received messages will be held until they are consumed. If the queue is full, the client will stop receiving messages from the server until the queue has room available. Default: 512.

**Notes** : Parameter descriptions adapted from httpx_ws documentation.

#### to_httpx_ws_kwargs
    
    
    def to_httpx_ws_kwargs() -> dict[str, Any]
    

Convert to kwargs dict for httpx_ws aconnect_ws/connect_ws.

# fishaudio.core.omit

OMIT sentinel for distinguishing None from not-provided parameters.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/sdk/python/core.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/sdk/python/core)

[Types](https://docs.fish.audio/api-reference/sdk/python/types)[Utils](https://docs.fish.audio/api-reference/sdk/python/utils)
