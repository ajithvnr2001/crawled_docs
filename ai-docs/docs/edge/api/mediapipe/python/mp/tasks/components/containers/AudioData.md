---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/AudioData/
title: mp.tasks.components.containers.AudioData \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:08.658846+00:00
---

# mp.tasks.components.containers.AudioData  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/AudioData/




#  mp.tasks.components.containers.AudioData

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/audio_data.py#L38-L152) MediaPipe Tasks' audio container.
    
    
    mp.tasks.components.containers.AudioData(
        buffer_length: int,
        audio_format: [mp.tasks.components.containers.AudioDataFormat](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/AudioDataFormat) = [AudioDataFormat()](https://ai.google.dev/edge/api/mediapipe/python/mp/tasks/components/containers/AudioDataFormat)
    ) -> None
    

| 

## Args  
  
---  
  
`buffer_length` |  the length of the audio buffer.   
`audio_format` |  the audio format metadata.   
  
## Attributes  
  
---  
  
`audio_format` |  Gets the audio format of the audio.   
`buffer` |  Gets the internal buffer.   
`buffer_length` |  Gets the sample count of the audio.   
  
## Methods

### `clear`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/audio_data.py#L56-L58)
    
    
    clear()
    

Clears the internal buffer and fill it with zeros.

### `create_from_array`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/audio_data.py#L106-L127)
    
    
    @classmethod
    create_from_array(
        src: np.ndarray, sample_rate: Optional[float] = None
    ) -> 'AudioData'
    

Creates an `AudioData` object from a NumPy array.

Args  
---  
  
`src` |  A NumPy source array contains the input audio.   
`sample_rate` |  the optional audio sample rate.   
  
Returns  
---  
An `AudioData` object that contains a copy of the NumPy source array as the data.   
  
### `load_from_array`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/components/containers/audio_data.py#L60-L104)
    
    
    load_from_array(
        src: np.ndarray, offset: int = 0, size: int = -1
    ) -> None
    

Loads the audio data from a NumPy array.

Args  
---  
  
`src` |  A NumPy source array contains the input audio.   
`offset` |  An optional offset for loading a slice of the `src` array to the buffer.   
`size` |  An optional size parameter denoting the number of samples to load from the `src` array.   
  
Raises  
---  
  
`ValueError` |  If the input array has an incorrect shape or if `offset` \+ `size` exceeds the length of the `src` array.   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 
