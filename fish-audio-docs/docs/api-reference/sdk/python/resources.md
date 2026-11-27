---
url: https://docs.fish.audio/api-reference/sdk/python/resources/
title: Resources - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-27T17:34:39.660921+00:00
---

# Resources - Fish Audio

> Source: https://docs.fish.audio/api-reference/sdk/python/resources/

## On this page

Back to top

  * fishaudio.resources.voices
  * VoicesClient Objects
    * list
    * get
    * create
    * update
    * delete
  * AsyncVoicesClient Objects
    * list
    * get
    * create
    * update
    * delete
  * fishaudio.resources.account
  * AccountClient Objects
    * get_credits
    * get_package
  * AsyncAccountClient Objects
    * get_credits
    * get_package
  * fishaudio.resources.tts
  * TTSClient Objects
    * stream
    * convert
    * stream_with_timestamps
    * convert_with_timestamps
    * stream_websocket
  * AsyncTTSClient Objects
    * stream
    * convert
    * stream_with_timestamps
    * convert_with_timestamps
    * stream_websocket
  * fishaudio.resources.realtime
    * iter_websocket_audio
    * aiter_websocket_audio
  * fishaudio.resources.asr
  * ASRClient Objects
    * transcribe
    * stream_websocket
  * AsyncASRClient Objects
    * transcribe
    * stream_websocket
  * fishaudio.resources.asr_realtime
    * encode_config
    * encode_message
    * decode_event
  * ASRRealtimeStream Objects
    * close
    * send
    * finalize
    * agent_speaking
    * add_context
    * configure
    * keepalive
  * AsyncASRRealtimeStream Objects
    * aclose
    * send
    * finalize
    * agent_speaking
    * add_context
    * configure
    * keepalive



Reference

# Resources

Copy pageCopy page

Copy pageCopy page

# fishaudio.resources.voices

Voice management namespace client. Install the Python SDK first: `pip install fish-audio-sdk`.

## VoicesClient Objects
    
    
    class VoicesClient()
    

Synchronous voice management operations.

#### list
    
    
    def list(
        *,
        page_size: int = 10,
        page_number: int = 1,
        title: Optional[str] = OMIT,
        tags: Optional[Union[list[str], str]] = OMIT,
        self_only: bool = False,
        author_id: Optional[str] = OMIT,
        language: Optional[Union[list[str], str]] = OMIT,
        title_language: Optional[Union[list[str], str]] = OMIT,
        sort_by: str = "task_count",
        request_options: Optional[RequestOptions] = None
    ) -> PaginatedResponse[Voice]
    

List available voices/models. **Arguments** :

  * `page_size` \- Number of results per page
  * `page_number` \- Page number (1-indexed)
  * `title` \- Filter by title
  * `tags` \- Filter by tags (single tag or list)
  * `self_only` \- Only return user’s own voices
  * `author_id` \- Filter by author ID
  * `language` \- Filter by language(s)
  * `title_language` \- Filter by title language(s)
  * `sort_by` \- Sort field (“task_count” or “created_at”)
  * `request_options` \- Request-level overrides

**Returns** : Paginated response with total count and voice items **Example** :
    
    
    client = FishAudio(api_key="...")
    
    # List all voices
    voices = client.voices.list(page_size=20)
    print(f"Total: {voices.total}")
    for voice in voices.items:
        print(f"{voice.title}: {voice.id}")
    
    # Filter by tags
    tagged = client.voices.list(tags=["male", "english"])
    

#### get
    
    
    def get(voice_id: str,
            *,
            request_options: Optional[RequestOptions] = None) -> Voice
    

Get voice by ID. **Arguments** :

  * `voice_id` \- Voice model ID
  * `request_options` \- Request-level overrides

**Returns** : Voice model details **Example** :
    
    
    client = FishAudio(api_key="...")
    voice = client.voices.get("voice_id_here")
    print(voice.title, voice.description)
    

#### create
    
    
    def create(*,
               title: str,
               voices: builtins.list[bytes],
               description: Optional[str] = OMIT,
               texts: Optional[builtins.list[str]] = OMIT,
               tags: Optional[builtins.list[str]] = OMIT,
               cover_image: Optional[bytes] = OMIT,
               visibility: Visibility = "private",
               train_mode: str = "fast",
               enhance_audio_quality: bool = True,
               request_options: Optional[RequestOptions] = None) -> Voice
    

Create/clone a new voice. **Arguments** :

  * `title` \- Voice model name
  * `voices` \- List of audio file bytes for training
  * `description` \- Voice description
  * `texts` \- Transcripts for voice samples
  * `tags` \- Tags for categorization
  * `cover_image` \- Cover image bytes
  * `visibility` \- Visibility setting (public, unlist, private)
  * `train_mode` \- Training mode (currently only “fast” supported)
  * `enhance_audio_quality` \- Whether to enhance audio quality
  * `request_options` \- Request-level overrides

**Returns** : Created voice model **Example** :
    
    
    client = FishAudio(api_key="...")
    
    with open("voice1.wav", "rb") as f1, open("voice2.wav", "rb") as f2:
        voice = client.voices.create(
            title="My Voice",
            voices=[f1.read(), f2.read()],
            description="Custom voice clone",
            tags=["custom", "english"]
        )
    print(f"Created: {voice.id}")
    

#### update
    
    
    def update(voice_id: str,
               *,
               title: Optional[str] = OMIT,
               description: Optional[str] = OMIT,
               cover_image: Optional[bytes] = OMIT,
               visibility: Optional[Visibility] = OMIT,
               tags: Optional[builtins.list[str]] = OMIT,
               request_options: Optional[RequestOptions] = None) -> None
    

Update voice metadata. **Arguments** :

  * `voice_id` \- Voice model ID
  * `title` \- New title
  * `description` \- New description
  * `cover_image` \- New cover image bytes
  * `visibility` \- New visibility setting
  * `tags` \- New tags
  * `request_options` \- Request-level overrides

**Example** :
    
    
    client = FishAudio(api_key="...")
    client.voices.update(
        "voice_id_here",
        title="Updated Title",
        visibility="public"
    )
    

#### delete
    
    
    def delete(voice_id: str,
               *,
               request_options: Optional[RequestOptions] = None) -> None
    

Delete a voice. **Arguments** :

  * `voice_id` \- Voice model ID
  * `request_options` \- Request-level overrides

**Example** :
    
    
    client = FishAudio(api_key="...")
    client.voices.delete("voice_id_here")
    

## AsyncVoicesClient Objects
    
    
    class AsyncVoicesClient()
    

Asynchronous voice management operations.

#### list
    
    
    async def list(
        *,
        page_size: int = 10,
        page_number: int = 1,
        title: Optional[str] = OMIT,
        tags: Optional[Union[list[str], str]] = OMIT,
        self_only: bool = False,
        author_id: Optional[str] = OMIT,
        language: Optional[Union[list[str], str]] = OMIT,
        title_language: Optional[Union[list[str], str]] = OMIT,
        sort_by: str = "task_count",
        request_options: Optional[RequestOptions] = None
    ) -> PaginatedResponse[Voice]
    

List available voices/models (async). See sync version for details.

#### get
    
    
    async def get(voice_id: str,
                  *,
                  request_options: Optional[RequestOptions] = None) -> Voice
    

Get voice by ID (async). See sync version for details.

#### create
    
    
    async def create(*,
                     title: str,
                     voices: builtins.list[bytes],
                     description: Optional[str] = OMIT,
                     texts: Optional[builtins.list[str]] = OMIT,
                     tags: Optional[builtins.list[str]] = OMIT,
                     cover_image: Optional[bytes] = OMIT,
                     visibility: Visibility = "private",
                     train_mode: str = "fast",
                     enhance_audio_quality: bool = True,
                     request_options: Optional[RequestOptions] = None) -> Voice
    

Create/clone a new voice (async). See sync version for details.

#### update
    
    
    async def update(voice_id: str,
                     *,
                     title: Optional[str] = OMIT,
                     description: Optional[str] = OMIT,
                     cover_image: Optional[bytes] = OMIT,
                     visibility: Optional[Visibility] = OMIT,
                     tags: Optional[builtins.list[str]] = OMIT,
                     request_options: Optional[RequestOptions] = None) -> None
    

Update voice metadata (async). See sync version for details.

#### delete
    
    
    async def delete(voice_id: str,
                     *,
                     request_options: Optional[RequestOptions] = None) -> None
    

Delete a voice (async). See sync version for details.

# fishaudio.resources.account

Account namespace client for billing and credits.

## AccountClient Objects
    
    
    class AccountClient()
    

Synchronous account operations.

#### get_credits
    
    
    def get_credits(*,
                    check_free_credit: Optional[bool] = OMIT,
                    request_options: Optional[RequestOptions] = None) -> Credits
    

Get API credit balance. **Arguments** :

  * `check_free_credit` \- Whether to check free credit availability
  * `request_options` \- Request-level overrides

**Returns** : Credits information **Example** :
    
    
    client = FishAudio(api_key="...")
    credits = client.account.get_credits()
    print(f"Available credits: {float(credits.credit)}")
    
    # Check free credit availability
    credits = client.account.get_credits(check_free_credit=True)
    if credits.has_free_credit:
        print("Free credits available!")
    

#### get_package
    
    
    def get_package(*,
                    request_options: Optional[RequestOptions] = None) -> Package
    

Get package information. **Arguments** :

  * `request_options` \- Request-level overrides

**Returns** : Package information **Example** :
    
    
    client = FishAudio(api_key="...")
    package = client.account.get_package()
    print(f"Balance: {package.balance}/{package.total}")
    

## AsyncAccountClient Objects
    
    
    class AsyncAccountClient()
    

Asynchronous account operations.

#### get_credits
    
    
    async def get_credits(
            *,
            check_free_credit: Optional[bool] = OMIT,
            request_options: Optional[RequestOptions] = None) -> Credits
    

Get API credit balance (async). **Arguments** :

  * `check_free_credit` \- Whether to check free credit availability
  * `request_options` \- Request-level overrides

**Returns** : Credits information **Example** :
    
    
    client = AsyncFishAudio(api_key="...")
    credits = await client.account.get_credits()
    print(f"Available credits: {float(credits.credit)}")
    
    # Check free credit availability
    credits = await client.account.get_credits(check_free_credit=True)
    if credits.has_free_credit:
        print("Free credits available!")
    

#### get_package
    
    
    async def get_package(*,
                          request_options: Optional[RequestOptions] = None
                          ) -> Package
    

Get package information (async). **Arguments** :

  * `request_options` \- Request-level overrides

**Returns** : Package information **Example** :
    
    
    client = AsyncFishAudio(api_key="...")
    package = await client.account.get_package()
    print(f"Balance: {package.balance}/{package.total}")
    

# fishaudio.resources.tts

TTS (Text-to-Speech) namespace client.

## TTSClient Objects
    
    
    class TTSClient()
    

Synchronous TTS operations.

#### stream
    
    
    def stream(*,
               text: str,
               reference_id: Optional[str] = None,
               references: Optional[list[ReferenceAudio]] = None,
               format: Optional[AudioFormat] = None,
               latency: Optional[LatencyMode] = None,
               speed: Optional[float] = None,
               config: TTSConfig = TTSConfig(),
               model: Union[Model, str] = "s2.1-pro",
               request_options: Optional[RequestOptions] = None) -> AudioStream
    

Stream text-to-speech audio chunks. **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided)
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : AudioStream object that can be iterated for audio chunks **Example** :
    
    
    from fishaudio import FishAudio
    
    client = FishAudio(api_key="...")
    
    # Stream and process chunks
    for chunk in client.tts.stream(text="Hello world"):
        process_audio_chunk(chunk)
    
    # Or collect all at once
    audio = client.tts.stream(text="Hello world").collect()
    

#### convert
    
    
    def convert(*,
                text: str,
                reference_id: Optional[str] = None,
                references: Optional[list[ReferenceAudio]] = None,
                format: Optional[AudioFormat] = None,
                latency: Optional[LatencyMode] = None,
                speed: Optional[float] = None,
                config: TTSConfig = TTSConfig(),
                model: Union[Model, str] = "s2.1-pro",
                request_options: Optional[RequestOptions] = None) -> bytes
    

Convert text to speech and return complete audio as bytes. This is a convenience method that streams all audio chunks and combines them. For chunk-by-chunk processing, use stream() instead. **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided)
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : Complete audio as bytes **Example** :
    
    
    from fishaudio import FishAudio
    from fishaudio.utils import play, save
    
    client = FishAudio(api_key="...")
    
    # Get complete audio
    audio = client.tts.convert(text="Hello world")
    
    # Play it
    play(audio)
    
    # Or save it
    save(audio, "output.mp3")
    

#### stream_with_timestamps
    
    
    def stream_with_timestamps(
            *,
            text: str,
            reference_id: Optional[str] = None,
            references: Optional[list[ReferenceAudio]] = None,
            format: Optional[AudioFormat] = None,
            latency: Optional[LatencyMode] = None,
            speed: Optional[float] = None,
            config: TTSConfig = TTSConfig(),
            model: Union[Model, str] = "s2.1-pro",
            request_options: Optional[RequestOptions] = None
    ) -> TTSTimestampStream
    

Stream text-to-speech audio together with word-level timestamps. Each event carries the next audio bytes and the newest timing snapshot. The returned stream keeps the timings up to date in `stream.segments`. **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided). “opus” is the best fit for playing audio while it streams; “wav” and “pcm” are uncompressed, which keeps sample positions exact.
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : TTSTimestampStream that yields TTSTimestampEvent objects **Example** :
    
    
    from fishaudio import FishAudio
    
    client = FishAudio(api_key="...")
    
    with client.tts.stream_with_timestamps(text="Hello world") as stream:
        for event in stream:
            player.write(event.audio)
            show_captions(stream.segments)  # timings received so far
    
    # Or collect the audio and final timings at once
    result = client.tts.stream_with_timestamps(text="Hello world").collect()
    

#### convert_with_timestamps
    
    
    def convert_with_timestamps(
            *,
            text: str,
            reference_id: Optional[str] = None,
            references: Optional[list[ReferenceAudio]] = None,
            format: Optional[AudioFormat] = None,
            latency: Optional[LatencyMode] = None,
            speed: Optional[float] = None,
            config: TTSConfig = TTSConfig(),
            model: Union[Model, str] = "s2.1-pro",
            request_options: Optional[RequestOptions] = None
    ) -> TTSTimestampResult
    

Convert text to speech and return the audio with word-level timestamps. This is a convenience method that reads the whole stream. To use audio and timings while they arrive, use stream_with_timestamps() instead. **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided). “opus” is the best fit for playing audio while it streams; “wav” and “pcm” are uncompressed, which keeps sample positions exact.
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : TTSTimestampResult with the complete audio, the timing of each word in seconds from the start of the audio, and the audio duration. When the API has no timings for the text (for example text without words), `segments` is empty and `duration` is None. **Example** :
    
    
    from fishaudio import FishAudio
    from fishaudio.utils import save
    
    client = FishAudio(api_key="...")
    
    result = client.tts.convert_with_timestamps(text="Hello world")
    save(result.audio, "output.mp3")
    
    for segment in result.segments:
        print(f"{segment.start:.2f}-{segment.end:.2f} {segment.text}")
    

#### stream_websocket
    
    
    def stream_websocket(
            text_stream: Iterable[Union[str, TextEvent, FlushEvent]],
            *,
            reference_id: Optional[str] = None,
            references: Optional[list[ReferenceAudio]] = None,
            format: Optional[AudioFormat] = None,
            latency: Optional[LatencyMode] = None,
            speed: Optional[float] = None,
            config: TTSConfig = TTSConfig(),
            model: Union[Model, str] = "s2.1-pro",
            max_workers: int = 10,
            ws_options: Optional[WebSocketOptions] = None) -> Iterator[bytes]
    

Stream text and receive audio in real-time via WebSocket. Perfect for conversational AI, live captioning, and streaming applications. **Arguments** :

  * `text_stream` \- Iterator of text chunks to stream
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided)
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `max_workers` \- ThreadPoolExecutor workers for concurrent sender
  * `ws_options` \- WebSocket connection options for configuring timeouts, message size limits, etc. Useful for long-running generations that may exceed default timeout values. See WebSocketOptions class for available parameters.

**Returns** : Iterator of audio bytes **Example** :
    
    
    from fishaudio import FishAudio, TTSConfig, ReferenceAudio, WebSocketOptions
    
    client = FishAudio(api_key="...")
    
    def text_generator():
        yield "Hello, "
        yield "this is "
        yield "streaming text!"
    
    # Simple usage with defaults
    with open("output.mp3", "wb") as f:
        for audio_chunk in client.tts.stream_websocket(text_generator()):
            f.write(audio_chunk)
    
    # With format and speed parameters
    with open("output.wav", "wb") as f:
        for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            format="wav",
            speed=1.3
        ):
            f.write(audio_chunk)
    
    # With reference_id parameter
    with open("output.mp3", "wb") as f:
        for audio_chunk in client.tts.stream_websocket(text_generator(), reference_id="your_model_id"):
            f.write(audio_chunk)
    
    # With references parameter
    with open("output.mp3", "wb") as f:
        for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            references=[ReferenceAudio(audio=audio_bytes, text="sample")]
        ):
            f.write(audio_chunk)
    
    # With WebSocket options for long-running generations
    # Useful if you're generating very long responses that may take >20 seconds
    ws_options = WebSocketOptions(keepalive_ping_timeout_seconds=60.0)
    with open("output.mp3", "wb") as f:
        for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            ws_options=ws_options
        ):
            f.write(audio_chunk)
    
    # Parameters override config values
    config = TTSConfig(format="mp3", latency="balanced")
    with open("output.wav", "wb") as f:
        for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            format="wav",  # Parameter wins
            config=config
        ):
            f.write(audio_chunk)
    

## AsyncTTSClient Objects
    
    
    class AsyncTTSClient()
    

Asynchronous TTS operations.

#### stream
    
    
    async def stream(
            *,
            text: str,
            reference_id: Optional[str] = None,
            references: Optional[list[ReferenceAudio]] = None,
            format: Optional[AudioFormat] = None,
            latency: Optional[LatencyMode] = None,
            speed: Optional[float] = None,
            config: TTSConfig = TTSConfig(),
            model: Union[Model, str] = "s2.1-pro",
            request_options: Optional[RequestOptions] = None) -> AsyncAudioStream
    

Stream text-to-speech audio chunks (async). **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided)
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : AsyncAudioStream object that can be iterated for audio chunks **Example** :
    
    
    from fishaudio import AsyncFishAudio
    
    client = AsyncFishAudio(api_key="...")
    
    # Stream and process chunks
    async for chunk in await client.tts.stream(text="Hello world"):
        await process_audio_chunk(chunk)
    
    # Or collect all at once
    stream = await client.tts.stream(text="Hello world")
    audio = await stream.collect()
    

#### convert
    
    
    async def convert(*,
                      text: str,
                      reference_id: Optional[str] = None,
                      references: Optional[list[ReferenceAudio]] = None,
                      format: Optional[AudioFormat] = None,
                      latency: Optional[LatencyMode] = None,
                      speed: Optional[float] = None,
                      config: TTSConfig = TTSConfig(),
                      model: Union[Model, str] = "s2.1-pro",
                      request_options: Optional[RequestOptions] = None) -> bytes
    

Convert text to speech and return complete audio as bytes (async). This is a convenience method that streams all audio chunks and combines them. For chunk-by-chunk processing, use stream() instead. **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided)
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : Complete audio as bytes **Example** :
    
    
    from fishaudio import AsyncFishAudio
    from fishaudio.utils import play, save
    
    client = AsyncFishAudio(api_key="...")
    
    # Get complete audio
    audio = await client.tts.convert(text="Hello world")
    
    # Play it
    play(audio)
    
    # Or save it
    save(audio, "output.mp3")
    

#### stream_with_timestamps
    
    
    async def stream_with_timestamps(
        *,
        text: str,
        reference_id: Optional[str] = None,
        references: Optional[list[ReferenceAudio]] = None,
        format: Optional[AudioFormat] = None,
        latency: Optional[LatencyMode] = None,
        speed: Optional[float] = None,
        config: TTSConfig = TTSConfig(),
        model: Union[Model, str] = "s2.1-pro",
        request_options: Optional[RequestOptions] = None
    ) -> AsyncTTSTimestampStream
    

Stream text-to-speech audio together with word-level timestamps (async). Each event carries the next audio bytes and the newest timing snapshot. The returned stream keeps the timings up to date in `stream.segments`. **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided). “opus” is the best fit for playing audio while it streams; “wav” and “pcm” are uncompressed, which keeps sample positions exact.
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : AsyncTTSTimestampStream that yields TTSTimestampEvent objects **Example** :
    
    
    from fishaudio import AsyncFishAudio
    
    client = AsyncFishAudio(api_key="...")
    
    async with await client.tts.stream_with_timestamps(text="Hello world") as stream:
        async for event in stream:
            await player.write(event.audio)
            show_captions(stream.segments)  # timings received so far
    
    # Or collect the audio and final timings at once
    stream = await client.tts.stream_with_timestamps(text="Hello world")
    result = await stream.collect()
    

#### convert_with_timestamps
    
    
    async def convert_with_timestamps(
            *,
            text: str,
            reference_id: Optional[str] = None,
            references: Optional[list[ReferenceAudio]] = None,
            format: Optional[AudioFormat] = None,
            latency: Optional[LatencyMode] = None,
            speed: Optional[float] = None,
            config: TTSConfig = TTSConfig(),
            model: Union[Model, str] = "s2.1-pro",
            request_options: Optional[RequestOptions] = None
    ) -> TTSTimestampResult
    

Convert text to speech and return the audio with word-level timestamps (async). This is a convenience method that reads the whole stream. To use audio and timings while they arrive, use stream_with_timestamps() instead. **Arguments** :

  * `text` \- Text to synthesize
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided). “opus” is the best fit for playing audio while it streams; “wav” and “pcm” are uncompressed, which keeps sample positions exact.
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `request_options` \- Request-level overrides

**Returns** : TTSTimestampResult with the complete audio, the timing of each word in seconds from the start of the audio, and the audio duration. When the API has no timings for the text (for example text without words), `segments` is empty and `duration` is None. **Example** :
    
    
    from fishaudio import AsyncFishAudio
    from fishaudio.utils import save
    
    client = AsyncFishAudio(api_key="...")
    
    result = await client.tts.convert_with_timestamps(text="Hello world")
    save(result.audio, "output.mp3")
    
    for segment in result.segments:
        print(f"{segment.start:.2f}-{segment.end:.2f} {segment.text}")
    

#### stream_websocket
    
    
    async def stream_websocket(text_stream: AsyncIterable[Union[str, TextEvent,
                                                                FlushEvent]],
                               *,
                               reference_id: Optional[str] = None,
                               references: Optional[list[ReferenceAudio]] = None,
                               format: Optional[AudioFormat] = None,
                               latency: Optional[LatencyMode] = None,
                               speed: Optional[float] = None,
                               config: TTSConfig = TTSConfig(),
                               model: Union[Model, str] = "s2.1-pro",
                               ws_options: Optional[WebSocketOptions] = None)
    

Stream text and receive audio in real-time via WebSocket (async). Perfect for conversational AI, live captioning, and streaming applications. **Arguments** :

  * `text_stream` \- Async iterator of text chunks to stream
  * `reference_id` \- Voice reference ID (overrides config.reference_id if provided)
  * `references` \- Reference audio samples (overrides config.references if provided)
  * `format` \- Audio format - “mp3”, “wav”, “pcm”, or “opus” (overrides config.format if provided)
  * `latency` \- Latency mode - “normal” or “balanced” (overrides config.latency if provided)
  * `speed` \- Speech speed multiplier, e.g. 1.5 for 1.5x speed (overrides config.prosody.speed if provided)
  * `config` \- TTS configuration (audio settings, voice, model parameters)
  * `model` \- TTS model to use
  * `ws_options` \- WebSocket connection options for configuring timeouts, message size limits, etc. Useful for long-running generations that may exceed default timeout values. See WebSocketOptions class for available parameters.

**Returns** : Async iterator of audio bytes **Example** :
    
    
    from fishaudio import AsyncFishAudio, TTSConfig, ReferenceAudio, WebSocketOptions
    
    client = AsyncFishAudio(api_key="...")
    
    async def text_generator():
        yield "Hello, "
        yield "this is "
        yield "async streaming!"
    
    # Simple usage with defaults
    async with aiofiles.open("output.mp3", "wb") as f:
        async for audio_chunk in client.tts.stream_websocket(text_generator()):
            await f.write(audio_chunk)
    
    # With format and speed parameters
    async with aiofiles.open("output.wav", "wb") as f:
        async for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            format="wav",
            speed=1.3
        ):
            await f.write(audio_chunk)
    
    # With reference_id parameter
    async with aiofiles.open("output.mp3", "wb") as f:
        async for audio_chunk in client.tts.stream_websocket(text_generator(), reference_id="your_model_id"):
            await f.write(audio_chunk)
    
    # With references parameter
    async with aiofiles.open("output.mp3", "wb") as f:
        async for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            references=[ReferenceAudio(audio=audio_bytes, text="sample")]
        ):
            await f.write(audio_chunk)
    
    # With WebSocket options for long-running generations
    # Useful if you're generating very long responses that may take >20 seconds
    ws_options = WebSocketOptions(keepalive_ping_timeout_seconds=60.0)
    async with aiofiles.open("output.mp3", "wb") as f:
        async for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            ws_options=ws_options
        ):
            await f.write(audio_chunk)
    
    # Parameters override config values
    config = TTSConfig(format="mp3", latency="balanced")
    async with aiofiles.open("output.wav", "wb") as f:
        async for audio_chunk in client.tts.stream_websocket(
            text_generator(),
            format="wav",  # Parameter wins
            config=config
        ):
            await f.write(audio_chunk)
    

# fishaudio.resources.realtime

Real-time WebSocket streaming helpers.

#### iter_websocket_audio
    
    
    def iter_websocket_audio(ws) -> Iterator[bytes]
    

Process WebSocket audio messages (sync). Receives messages from WebSocket, yields audio chunks, handles errors. Unknown events are ignored and iteration continues. **Arguments** :

  * `ws` \- WebSocket connection from httpx_ws.connect_ws

**Yields** : Audio bytes **Raises** :

  * `WebSocketError` \- On disconnect or error finish event



#### aiter_websocket_audio
    
    
    async def aiter_websocket_audio(ws) -> AsyncIterator[bytes]
    

Process WebSocket audio messages (async). Receives messages from WebSocket, yields audio chunks, handles errors. Unknown events are ignored and iteration continues. **Arguments** :

  * `ws` \- WebSocket connection from httpx_ws.aconnect_ws

**Yields** : Audio bytes **Raises** :

  * `WebSocketError` \- On disconnect or error finish event



# fishaudio.resources.asr

ASR (Automatic Speech Recognition) namespace client.

## ASRClient Objects
    
    
    class ASRClient()
    

Synchronous ASR operations.

#### transcribe
    
    
    def transcribe(
            *,
            audio: bytes,
            language: Optional[str] = OMIT,
            include_timestamps: bool = True,
            model: Optional[str] = None,
            request_options: Optional[RequestOptions] = None) -> ASRResponse
    

Transcribe audio to text. **Arguments** :

  * `audio` \- Audio file bytes
  * `language` \- Language code (e.g., “en”, “zh”). Auto-detected if not provided.
  * `include_timestamps` \- Whether to include timestamp information for segments (and speaker turns, on models that return them)
  * `model` \- ASR model, e.g. “transcribe-1-pro” (recommended). Sent as the `model` header and takes precedence over one in request_options. If not provided and request_options sets no `model` header, the request runs on the API’s default model, transcribe-1
  * `request_options` \- Request-level overrides

**Returns** : ASRResponse with transcription text, duration (in seconds), and segments, plus language, request ID and speaker turns when the API returns them **Example** :
    
    
    client = FishAudio(api_key="...")
    
    with open("audio.mp3", "rb") as f:
        audio_bytes = f.read()
    
    result = client.asr.transcribe(
        audio=audio_bytes, model="transcribe-1-pro"
    )
    print(result.text)
    for segment in result.segments:
        print(f"{segment.start}-{segment.end}: {segment.text}")
    

#### stream_websocket
    
    
    def stream_websocket(
            audio_stream: Iterable[Union[bytes, ASRRealtimeControl]],
            *,
            sample_rate: Optional[ASRSampleRate] = None,
            turn_detection: Optional[TurnDetectionMode] = None,
            eager: Optional[bool] = None,
            drafts: Optional[bool] = None,
            diarize: Optional[bool] = None,
            terms: Optional[list[str]] = None,
            config: ASRRealtimeConfig = ASRRealtimeConfig(),
            model: str = "transcribe-stream-1",
            ws_options: Optional[WebSocketOptions] = None) -> ASRRealtimeStream
    

Stream audio and receive transcripts in real-time via WebSocket. Audio is divided into turns. Each turn ends with one committed event that holds its final transcript; with drafts=True you also get live draft events while the turn is open. The session ends with a session_done event once audio_stream is exhausted. By default the transcript text starts with a speaker tag, e.g. `<|speaker:0|> Hello.`, and can contain sound tags such as `[laughter]`. Pass diarize=False for text without speaker tags; sound tags are turned off with config=ASRRealtimeConfig(results=ASRResults(tag_audio_events=False)). **Arguments** :

  * `audio_stream` \- Iterator of raw audio chunks: 16-bit little-endian mono PCM, ideally 20-40 ms each, sent as you capture them. It can also yield control messages (e.g. ASRFinalizeEvent()), which are sent at that position in the audio
  * `sample_rate` \- Sample rate of the audio in Hz: 8000, 12000, 16000, 22050, 24000, 32000, 44100 or 48000 (overrides config.sample_rate if provided)
  * `turn_detection` \- When a turn ends - “auto” (the server judges that the user has finished), “vad” (after a fixed silence) or “manual” (when you send finalize) (overrides config.turn_detection.mode if provided)
  * `eager` \- Send eager_end_of_turn events in auto mode (overrides config.turn_detection.eager if provided)
  * `drafts` \- Send live draft events (overrides config.results.drafts if provided)
  * `diarize` \- Speaker tags such as `<|speaker:0|>` in the transcript text. The server adds them by default; pass False for text without speaker tags (overrides config.results.diarize if provided)
  * `terms` \- Names, products and jargon to recognize (overrides config.context.terms if provided)
  * `config` \- Session configuration (audio, turn detection, results, context)
  * `model` \- Realtime speech-to-text model
  * `ws_options` \- WebSocket connection options for configuring timeouts, message size limits, etc. See WebSocketOptions class for available parameters.

**Returns** :

  * `ASRRealtimeStream` \- an iterator of typed events (check event.type), with methods to send control messages during the session: finalize(), agent_speaking(), add_context() and configure()

**Raises** :

  * `ASRRealtimeError` \- If the server reports an error that ends the session, or closes the connection abnormally (see error_type and close_code)
  * `APIError` \- If the connection is refused (e.g. AuthenticationError for 401)
  * `WebSocketError` \- If the connection is lost

**Example** :
    
    
    import wave
    
    from fishaudio import FishAudio
    
    client = FishAudio(api_key="...")
    
    def audio_chunks():
        with wave.open("speech.wav", "rb") as wav:  # 16-bit mono PCM
            while chunk := wav.readframes(640):  # 40 ms at 16 kHz
                yield chunk
    
    # Final transcript of each turn (diarize=False: no <|speaker:0|> tags)
    for event in client.asr.stream_websocket(
        audio_chunks(), sample_rate=16000, diarize=False
    ):
        if event.type == "committed":
            print(event.text)
    
    # Live captions: drafts while the turn is open, then the final text
    for event in client.asr.stream_websocket(audio_chunks(), drafts=True):
        if event.type == "draft":
            print("...", event.text)
        elif event.type == "committed":
            print(event.text)
    
    # Voice agent: answer the user's turns, and tell the server while you speak.
    # microphone_chunks() stands for your live audio source. It must keep
    # yielding audio: once the source ends, the session finishes and control
    # methods can no longer be sent.
    with client.asr.stream_websocket(microphone_chunks(), eager=True) as stream:
        for event in stream:
            if event.type == "committed" and event.user_turn:
                stream.agent_speaking(True)
                ...  # reply, then stream.agent_speaking(False)
    

## AsyncASRClient Objects
    
    
    class AsyncASRClient()
    

Asynchronous ASR operations.

#### transcribe
    
    
    async def transcribe(
            *,
            audio: bytes,
            language: Optional[str] = OMIT,
            include_timestamps: bool = True,
            model: Optional[str] = None,
            request_options: Optional[RequestOptions] = None) -> ASRResponse
    

Transcribe audio to text (async). **Arguments** :

  * `audio` \- Audio file bytes
  * `language` \- Language code (e.g., “en”, “zh”). Auto-detected if not provided.
  * `include_timestamps` \- Whether to include timestamp information for segments (and speaker turns, on models that return them)
  * `model` \- ASR model, e.g. “transcribe-1-pro” (recommended). Sent as the `model` header and takes precedence over one in request_options. If not provided and request_options sets no `model` header, the request runs on the API’s default model, transcribe-1
  * `request_options` \- Request-level overrides

**Returns** : ASRResponse with transcription text, duration (in seconds), and segments, plus language, request ID and speaker turns when the API returns them **Example** :
    
    
    client = AsyncFishAudio(api_key="...")
    
    async with aiofiles.open("audio.mp3", "rb") as f:
        audio_bytes = await f.read()
    
    result = await client.asr.transcribe(
        audio=audio_bytes, model="transcribe-1-pro"
    )
    print(result.text)
    for segment in result.segments:
        print(f"{segment.start}-{segment.end}: {segment.text}")
    

#### stream_websocket
    
    
    def stream_websocket(
            audio_stream: AsyncIterable[Union[bytes, ASRRealtimeControl]],
            *,
            sample_rate: Optional[ASRSampleRate] = None,
            turn_detection: Optional[TurnDetectionMode] = None,
            eager: Optional[bool] = None,
            drafts: Optional[bool] = None,
            diarize: Optional[bool] = None,
            terms: Optional[list[str]] = None,
            config: ASRRealtimeConfig = ASRRealtimeConfig(),
            model: str = "transcribe-stream-1",
            ws_options: Optional[WebSocketOptions] = None
    ) -> AsyncASRRealtimeStream
    

Stream audio and receive transcripts in real-time via WebSocket (async). Audio is divided into turns. Each turn ends with one committed event that holds its final transcript; with drafts=True you also get live draft events while the turn is open. The session ends with a session_done event once audio_stream is exhausted. By default the transcript text starts with a speaker tag, e.g. `<|speaker:0|> Hello.`, and can contain sound tags such as `[laughter]`. Pass diarize=False for text without speaker tags; sound tags are turned off with config=ASRRealtimeConfig(results=ASRResults(tag_audio_events=False)). **Arguments** :

  * `audio_stream` \- Async iterator of raw audio chunks: 16-bit little-endian mono PCM, ideally 20-40 ms each, sent as you capture them. It can also yield control messages (e.g. ASRFinalizeEvent()), which are sent at that position in the audio
  * `sample_rate` \- Sample rate of the audio in Hz: 8000, 12000, 16000, 22050, 24000, 32000, 44100 or 48000 (overrides config.sample_rate if provided)
  * `turn_detection` \- When a turn ends - “auto” (the server judges that the user has finished), “vad” (after a fixed silence) or “manual” (when you send finalize) (overrides config.turn_detection.mode if provided)
  * `eager` \- Send eager_end_of_turn events in auto mode (overrides config.turn_detection.eager if provided)
  * `drafts` \- Send live draft events (overrides config.results.drafts if provided)
  * `diarize` \- Speaker tags such as `<|speaker:0|>` in the transcript text. The server adds them by default; pass False for text without speaker tags (overrides config.results.diarize if provided)
  * `terms` \- Names, products and jargon to recognize (overrides config.context.terms if provided)
  * `config` \- Session configuration (audio, turn detection, results, context)
  * `model` \- Realtime speech-to-text model
  * `ws_options` \- WebSocket connection options for configuring timeouts, message size limits, etc. See WebSocketOptions class for available parameters.

**Returns** :

  * `AsyncASRRealtimeStream` \- an async iterator of typed events (check event.type), with methods to send control messages during the session: finalize(), agent_speaking(), add_context() and configure()

**Raises** :

  * `ASRRealtimeError` \- If the server reports an error that ends the session, or closes the connection abnormally (see error_type and close_code)
  * `APIError` \- If the connection is refused (e.g. AuthenticationError for 401)
  * `WebSocketError` \- If the connection is lost

**Example** :
    
    
    import wave
    
    from fishaudio import AsyncFishAudio
    
    client = AsyncFishAudio(api_key="...")
    
    async def audio_chunks():
        with wave.open("speech.wav", "rb") as wav:  # 16-bit mono PCM
            while chunk := wav.readframes(640):  # 40 ms at 16 kHz
                yield chunk
    
    # Final transcript of each turn (diarize=False: no <|speaker:0|> tags)
    async for event in client.asr.stream_websocket(
        audio_chunks(), sample_rate=16000, diarize=False
    ):
        if event.type == "committed":
            print(event.text)
    
    # Live captions: drafts while the turn is open, then the final text
    async for event in client.asr.stream_websocket(audio_chunks(), drafts=True):
        if event.type == "draft":
            print("...", event.text)
        elif event.type == "committed":
            print(event.text)
    
    # Voice agent: answer the user's turns, and tell the server while you speak.
    # microphone_chunks() stands for your live audio source. It must keep
    # yielding audio: once the source ends, the session finishes and control
    # methods can no longer be sent.
    async with client.asr.stream_websocket(microphone_chunks(), eager=True) as stream:
        async for event in stream:
            if event.type == "committed" and event.user_turn:
                await stream.agent_speaking(True)
                ...  # reply, then await stream.agent_speaking(False)
    

# fishaudio.resources.asr_realtime

Realtime speech-to-text sessions over WebSocket.

#### encode_config
    
    
    def encode_config(config: ASRRealtimeConfig) -> bytes
    

Pack the `config` message that opens a session.

#### encode_message
    
    
    def encode_message(item: Union[bytes, ASRRealtimeControl]) -> bytes
    

Pack an audio chunk or a control message for the wire.

#### decode_event
    
    
    def decode_event(message: bytes) -> Optional[ASRRealtimeEvent]
    

Parse a server message. Returns None for message types this SDK does not know.

## ASRRealtimeStream Objects
    
    
    class ASRRealtimeStream()
    

A realtime speech-to-text session (sync). Iterate it for the server’s events. The connection opens on the first iteration and closes when the session ends, when an error is raised, or when you leave the loop early. Use it as a context manager (or call `close()`) if you keep a reference to it after leaving the loop. The audio stream is read on a background thread. When the session ends before the audio does, that thread stops as soon as the audio stream yields its next chunk, and closes the stream if it is a generator. The SDK cannot interrupt an audio stream that is blocked waiting for audio (for example a microphone read with no timeout): make your audio source end, or yield regularly, so the thread can exit. Closing does not wait for a server that has stopped reading: a write that is still pending after half a second is interrupted by cutting the connection, without a close frame. Read the events from one thread at a time. The control methods send a message at the current position in the audio stream; they can be called from any thread once `session_started` has been received.

#### close
    
    
    def close() -> None
    

Close the connection. Safe to call more than once.

#### send
    
    
    def send(message: ASRRealtimeControl) -> None
    

Send a control message. **Raises** :

  * `WebSocketError` \- If the session is not open (not started yet, or closed)



#### finalize
    
    
    def finalize() -> None
    

Commit the current turn now (push-to-talk: the button was released).

#### agent_speaking
    
    
    def agent_speaking(speaking: bool) -> None
    

Tell the server that your voice agent started or stopped speaking.

#### add_context
    
    
    def add_context(items: list[ASRContextItem],
                    *,
                    reset_history: bool = False) -> None
    

Add conversation context, typically each line your agent speaks.

#### configure
    
    
    def configure(*,
                  turn_detection: Optional[ASRTurnDetection] = None,
                  results: Optional[ASRResults] = None,
                  terms: Optional[list[str]] = None) -> None
    

Change settings during the session. The server answers with a configured event.

#### keepalive
    
    
    def keepalive() -> None
    

Keep an idle session open. Rarely needed: WebSocket pings count as activity.

## AsyncASRRealtimeStream Objects
    
    
    class AsyncASRRealtimeStream()
    

A realtime speech-to-text session (async). Iterate it with `async for` for the server’s events. The connection opens on the first iteration and closes when the session ends, when an error is raised, or when you leave the loop early. Use it as an async context manager (or call `aclose()`) if you keep a reference to it after leaving the loop. Closing cancels the task that reads the audio stream and closes the stream if it is an async generator. Up to 256 events are buffered for a consumer that reads slowly; beyond that the session stops reading from the server until the consumer catches up. Read the events from one task at a time: a read started while another is waiting raises `RuntimeError`. A read that was cancelled (for example by `asyncio.wait_for`) loses nothing; just read again. The control methods send a message at the current position in the audio stream; they can be awaited once `session_started` has been received. Keep reading: when you stop, the SDK buffers a few hundred events and then stops reading from the connection, which also stops it answering keepalive pings. A consumer that stays stalled past the keepalive timeout (20 s by default, see `ws_options`) while events keep arriving loses the connection.

#### aclose
    
    
    async def aclose() -> None
    

Close the connection. Safe to call more than once.

#### send
    
    
    async def send(message: ASRRealtimeControl) -> None
    

Send a control message. **Raises** :

  * `WebSocketError` \- If the session is not open (not started yet, or closed)



#### finalize
    
    
    async def finalize() -> None
    

Commit the current turn now (push-to-talk: the button was released).

#### agent_speaking
    
    
    async def agent_speaking(speaking: bool) -> None
    

Tell the server that your voice agent started or stopped speaking.

#### add_context
    
    
    async def add_context(items: list[ASRContextItem],
                          *,
                          reset_history: bool = False) -> None
    

Add conversation context, typically each line your agent speaks.

#### configure
    
    
    async def configure(*,
                        turn_detection: Optional[ASRTurnDetection] = None,
                        results: Optional[ASRResults] = None,
                        terms: Optional[list[str]] = None) -> None
    

Change settings during the session. The server answers with a configured event.

#### keepalive
    
    
    async def keepalive() -> None
    

Keep an idle session open. Rarely needed: WebSocket pings count as activity.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/sdk/python/resources.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/sdk/python/resources)

[Client](https://docs.fish.audio/api-reference/sdk/python/client)[Types](https://docs.fish.audio/api-reference/sdk/python/types)
