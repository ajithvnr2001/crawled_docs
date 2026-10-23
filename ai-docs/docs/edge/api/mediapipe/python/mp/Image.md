---
url: https://ai.google.dev/edge/api/mediapipe/python/mp/Image/
title: mp.Image \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:16:04.842039+00:00
---

# mp.Image  |  Google AI for Developers

> Source: https://ai.google.dev/edge/api/mediapipe/python/mp/Image/




#  mp.Image

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L200-L554) A container for storing an image or a video frame.

#### View aliases

**Main aliases** [`mp.tasks.vision.drawing_styles.drawing_utils.face_landmarker.image_lib.Image`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/Image), [`mp.tasks.vision.drawing_styles.face_landmarker.image_lib.Image`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/Image), [`mp.tasks.vision.drawing_styles.hand_landmarker.image_lib.Image`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/Image), [`mp.tasks.vision.drawing_styles.pose_landmarker.image_lib.Image`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/Image), [`mp.tasks.vision.drawing_utils.face_landmarker.image_lib.Image`](https://ai.google.dev/edge/api/mediapipe/python/edge/api/mediapipe/python/mp/Image)
    
    
    mp.Image(
        image_format: [mp.ImageFormat](https://ai.google.dev/edge/api/mediapipe/python/mp/ImageFormat),
        data: np.ndarray
    )
    

Formats supported by Image are listed in the ImageFormat enum. Pixels are encoded row-major in an interleaved fashion. Image supports uint8, uint16, and float as its data types. Image can be created by copying the data from a numpy ndarray that stores the pixel data continuously. The data in an Image will become immutable after creation. The pixel data in an Image can be retrieved as a numpy ndarray by calling [`Image.numpy_view()`](https://ai.google.dev/edge/api/mediapipe/python/mp/Image#numpy_view). The returned numpy ndarray is a reference to the internal data and itself is unwritable. If the callers want to modify the numpy ndarray, it's required to obtain a copy of it. Pixel data retrieval examples:
    
    
    for channel in range(num_channel):
      for col in range(width):
        for row in range(height):
          print(image[row, col, channel])
    
    output_ndarray = image.numpy_view()
    print(output_ndarray[0, 0, 0])
    copied_ndarray = np.copy(output_ndarray)
    copied_ndarray[0,0,0] = 0
    

| 

## Args  
  
---  
  
`image_format` |  The format of the image data.   
`data` |  A numpy ndarray containing the image data.   
  
## Attributes  
  
---  
  
`channels` |  Returns the number of channels in the image.   
`height` |  Returns the height of the image.   
`image_format` |  Returns the image format.   
`step` |  Returns the width step of the image.   
`width` |  Returns the width of the image.   
  
## Methods

### `create_from_file`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L296-L328)
    
    
    @classmethod
    create_from_file(
        file_name: str
    ) -> 'Image'
    

Creates an `Image` object from an image file.

Args  
---  
  
`file_name` |  The path to the image file.   
  
Returns  
---  
An `Image` object.   
  
Raises  
---  
  
`RuntimeError` |  If the image file cannot be decoded.   
  
### `is_aligned`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L510-L524)
    
    
    is_aligned(
        alignment_boundary: int
    ) -> bool
    

Return True if each row of the data is aligned to alignment boundary, which must be 1 or a power of 2.

Args  
---  
  
`alignment_boundary` |  An integer.   
  
Returns  
---  
A boolean.   
  
Examples  
---  
      
    
    image.is_aligned(16)
      
  
### `is_contiguous`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L502-L504)
    
    
    is_contiguous() -> bool
    

Return True if the pixel data is stored contiguously (without any alignment padding areas).

### `is_empty`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L506-L508)
    
    
    is_empty() -> bool
    

Return True if the pixel data is unallocated.

### `numpy_view`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L365-L426)
    
    
    numpy_view() -> np.ndarray
    

Returns the image pixel data as an unwritable numpy ndarray.

Realign the pixel data to be stored contiguously and return a reference to the unwritable numpy ndarray. If the callers want to modify the numpy array data, it's required to obtain a copy of the ndarray.

Returns  
---  
An unwritable numpy ndarray.   
  
Examples  
---  
      
    
    output_ndarray = image.numpy_view()
    copied_ndarray = np.copy(output_ndarray)
    copied_ndarray[0,0,0] = 0
      
  
### `uses_gpu`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L498-L500)
    
    
    uses_gpu() -> bool
    

Return True if data is currently on the GPU..

### `__getitem__`

[View source](https://github.com/google/mediapipe/blob/master/mediapipe/tasks/python/vision/core/image.py#L428-L496)
    
    
    __getitem__(
        key: tuple[int, ...]
    ) -> Any
    

Use the indexer operators to access pixel data.

Args  
---  
  
`key` |  A tuple of integers representing the row, column, and channel indices (or row and column for single channel images).   
  
Returns  
---  
The pixel data at the specified index.   
  
Raises  
---  
  
`IndexError` |  If the index is invalid or out of bounds.   
  
Examples  
---  
      
    
    for channel in range(num_channel):
      for col in range(width):
        for row in range(height):
          print(image[row, col, channel])
    </td>
    </tr>
    
    </table>
    
    
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-06-05 UTC. [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-05 UTC."],[],[]] 

  * [ Terms ](https://policies.google.com/terms)
  * [ Privacy ](https://policies.google.com/privacy)
  * Manage cookies 



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Shqip
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


