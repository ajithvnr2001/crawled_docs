---
url: https://developer.android.com/tools/etc1tool/
title: etc1tool \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:39.292237+00:00
---

# etc1tool  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/tools/etc1tool/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ SDK tools guides ](https://developer.android.com/tools)



#  etc1tool Stay organized with collections  Save and categorize content based on your preferences. 

`etc1tool` is a command line utility that lets you encode PNG images to the [ETC1](https://registry.khronos.org/OpenGL/extensions/OES/OES_compressed_ETC1_RGB8_texture.txt) compression standard and decode ETC1 compressed images back to PNG.

The usage for `etc1tool` is:
    
    
    etc1tool infile [--help | --encode | --encodeNoHeader | --decode] [--showDifference
    diff-file] [-o outfile]

This table lists the command options:

Option | Description  
---|---  
`infile` | The input file to compress.  
`--help` | Print usage information.  
`--encode` | Create an ETC1 file from a PNG file. This is the default mode for the tool if nothing is specified.  
`--encodeNoHeader` | Create a raw ETC1 data file without a header from a PNG file.  
`--decode` | Create a PNG file from an ETC1 file.  
`--showDifference _diff-file_` | Write the difference between the original and encoded image to `_diff-file_`. This option is only valid when encoding.  
`-o _outfile_` | Specify the name of the output file. If `_outfile_` is not specified, the output file is constructed from the input filename with the appropriate suffix (`.pkm` or `.png`).   
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2023-04-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-04-12 UTC."],[],[]] 
