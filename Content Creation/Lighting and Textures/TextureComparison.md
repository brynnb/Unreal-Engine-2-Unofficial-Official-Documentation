# DXTC: DXTC Examples and Technical Comparison

*Document Summary: Comparison between DirectX Texture compression types with uncompressed and palettized. Excellent for all skill and experience levels.**Document Changelog: Last updated by Tom Lin (DemiurgeStudios?), for document summary. Original author was Lucas Alonso.*

* [DXTC: DXTC Examples and Technical Comparison](#dxtc-dxtc-examples-and-technical-comparison)
  + [Introduction](#introduction)
    - [Purpose](#purpose)
    - [DXTC Fundamentals](#dxtc-fundamentals)
    - [NVIDIA DXT1 Issue](#nvidia-dxt1-issue)
  + [Examples](#examples)
    - [Texture 1](#texture-1)
    - [Gradient](#gradient)
    - [Texture 2](#texture-2)
    - [Texture 3](#texture-3)
    - [Rainbow Gradient](#rainbow-gradient)
    - [Text/HUD Art](#texthud-art)
    - [DXTC Nightmare](#dxtc-nightmare)
  + [Conclusions](#conclusions)

## Introduction

### Purpose

The purpose of this document is to enlighten you, the content creator, on when it is appropriate to use the DXTC format to compress your textures, and in which cases they're better left uncompressed, or palettized using Bright.

### DXTC Fundamentals

The portion of the DXTC algorithm that concerns us for this document is the part that compresses color information, because this is done the same way in **ALL DXTC variants (DXT1-5)**. Color information is stored in a similar fashion as standard palettized bitmaps, but instead of storing a 256 color palette for the whole image, DXTC stores a small palette for every 4x4 block of pixels. Each of these mini-palettes can represent up to four colors, but two of the colors are interpolated from the other two and are not actually stored with the file. This allows you to compress a bitmap that would have normally been 65k into merely 32k, and therefore allows you to store twice the amount of textures in video memory, or store the same amount of textures but at double the resolution.

![colourtable.gif](../../assets/colourtable.gif)

### NVIDIA DXT1 Issue

The hardware implementation of the DXT1 decompressor on NVidia hardware has some problems with quality. This is because the texture is processed internally in 16bit color instead of 32bit, and therefore quality, particularly that of darker shades, suffers considerably. All the other DXTC formats (DXT2-5) are not affected by this problem, but they store alpha information, which isn't so great if the texture you're trying to compress doesn't even utilize the alpha channel. But since the only format that doesn't store alpha information has quality issues, you're limited to using it in very specific cases.

## Examples

### Texture 1

| SOURCE | SOURCE DETAIL |
| --- | --- |
| ![Bradley1_SOURCE.png](../../assets/Bradley1_SOURCE.png) | ![Bradley1_SOURCE_ZOOM.png](../../assets/Bradley1_SOURCE_ZOOM.png) |
| **BRIGHT** | **BRIGHT DETAIL** |
| ![Bradley1_BRIGHT.png](../../assets/Bradley1_BRIGHT.png) | ![Bradley1_BRIGHT_ZOOM.png](../../assets/Bradley1_BRIGHT_ZOOM.png) |
| **DXTC** | **DXTC DETAIL** |
| ![Bradley1_DXTC.png](../../assets/Bradley1_DXTC.png) | ![Bradley1_DXTC_ZOOM.png](../../assets/Bradley1_DXTC_ZOOM.png) |
| **NVIDIA DXT1** | **NVIDIA DXT1 DETAIL** |
| ![Bradley1_DXT1.png](../../assets/Bradley1_DXT1.png) | ![Bradley1_DXT1_ZOOM.png](../../assets/Bradley1_DXT1_ZOOM.png) |

While you can't really tell the difference between the 3 textures with this example at normal scale, by zooming in we can begin to see the artifacts caused by DXTC compression (small blocks of uniform colors). In this case, the artifacting is barely appreciable even when magnified, so this type of texture would be ideal to use with DXTC. The in-game NVidia DXT1 looks quite blurry, so unless you don't mind the lost clarity, you might consider using DXT3.

### Gradient

| SOURCE | SOURCE DETAIL |
| --- | --- |
| ![Gradient_SOURCE.png](../../assets/Gradient_SOURCE.png) | ![Gradient_SOURCE_ZOOM.png](../../assets/Gradient_SOURCE_ZOOM.png) |
| **BRIGHT** | **BRIGHT DETAIL** |
| ![Gradient_BRIGHT.png](../../assets/Gradient_BRIGHT.png) | ![Gradient_BRIGHT_ZOOM.png](../../assets/Gradient_BRIGHT_ZOOM.png) |
| **DXTC** | **DXTC DETAIL** |
| ![Gradient_DXTC.png](../../assets/Gradient_DXTC.png) | ![Gradient_DXTC_ZOOM.png](../../assets/Gradient_DXTC_ZOOM.png) |
| **NVIDIA DXT1** | **NVIDIA DXT1 DETAIL** |
| ![Gradient_DXT1.png](../../assets/Gradient_DXT1.png) | ![Gradient_DXT1_ZOOM.png](../../assets/Gradient_DXT1_ZOOM.png) |

However, in this case you can plainly see the banding in the DXTC texture, while the Bright example retains full quality. Again, this is because the DXTC algorithm can only use 4 colors per 4x4 block of pixels, which means if there's enough color variation within the blocks, you get output like this. Definitely don't use DXT1 for this type of thing.

### Texture 2

| SOURCE | SOURCE DETAIL |
| --- | --- |
| ![MoreRocks_SOURCE.png](../../assets/MoreRocks_SOURCE.png) | ![MoreRocks_SOURCE_ZOOM.png](../../assets/MoreRocks_SOURCE_ZOOM.png) |
| **BRIGHT** | **BRIGHT DETAIL** |
| ![MoreRocks_BRIGHT.png](../../assets/MoreRocks_BRIGHT.png) | ![MoreRocks_BRIGHT_ZOOM.png](../../assets/MoreRocks_BRIGHT_ZOOM.png) |
| **DXTC** | **DXTC DETAIL** |
| ![MoreRocks_DXTC.png](../../assets/MoreRocks_DXTC.png) | ![MoreRocks_DXTC_ZOOM.png](../../assets/MoreRocks_DXTC_ZOOM.png) |
| **NVIDIA DXT1** | **NVIDIA DXT1 DETAIL** |
| ![MoreRocks_DXT1.png](../../assets/MoreRocks_DXT1.png) | ![MoreRocks_DXT1_ZOOM.png](../../assets/MoreRocks_DXT1_ZOOM.png) |

Like Example 1, this is the type of texture you would normally use DXTC on. It's very difficult to appreciate the lost quality of the DXTC compressed texture.

### Texture 3

| SOURCE | SOURCE DETAIL |
| --- | --- |
| ![Wall_SOURCE.png](../../assets/Wall_SOURCE.png) | ![Wall_SOURCE_ZOOM.png](../../assets/Wall_SOURCE_ZOOM.png) |
| **BRIGHT** | **BRIGHT DETAIL** |
| ![Wall_BRIGHT.png](../../assets/Wall_BRIGHT.png) | ![Wall_BRIGHT_ZOOM.png](../../assets/Wall_BRIGHT_ZOOM.png) |
| **DXTC** | **DXTC DETAIL** |
| ![Wall_DXTC.png](../../assets/Wall_DXTC.png) | ![Wall_DXTC_ZOOM.png](../../assets/Wall_DXTC_ZOOM.png) |
| **NVIDIA DXT1** | **NVIDIA DXT1 DETAIL** |
| ![Wall_DXT1.png](../../assets/Wall_DXT1.png) | ![Wall_DXT1_ZOOM.png](../../assets/Wall_DXT1_ZOOM.png) |

Again, a standard texture. While the DXTC artifacting is easily visible in the magnified texture, you would be hard pressed to tell the difference between the SOURCE texture and the DXTC compressed one. Bright does a great job as well.

### Rainbow Gradient

| SOURCE | SOURCE DETAIL |
| --- | --- |
| ![Rainbow_SOURCE.png](../../assets/Rainbow_SOURCE.png) | ![Rainbow_SOURCE_ZOOM.png](../../assets/Rainbow_SOURCE_ZOOM.png) |
| **BRIGHT** | **BRIGHT DETAIL** |
| ![Rainbow_BRIGHT.png](../../assets/Rainbow_BRIGHT.png) | ![Rainbow_BRIGHT_ZOOM.png](../../assets/Rainbow_BRIGHT_ZOOM.png) |
| **DXTC** | **DXTC DETAIL** |
| ![Rainbow_DXTC.png](../../assets/Rainbow_DXTC.png) | ![Rainbow_DXTC_ZOOM.png](../../assets/Rainbow_DXTC_ZOOM.png) |
| **NVIDIA DXT1** | **NVIDIA DXT1 DETAIL** |
| ![Rainbow_DXT1.png](../../assets/Rainbow_DXT1.png) | ![Rainbow_DXT1_ZOOM.png](../../assets/Rainbow_DXT1_ZOOM.png) |

In this example, you can plainly see that Bright is having a hard time turning the 42,000 colors used in this texture into just 256. While Bright's attempt is impressive, the DXTC compressed or the uncompressed 32bit texture are better choices in this type of situation. You should avoid DXT1.

### Text/HUD Art

| SOURCE | SOURCE DETAIL |
| --- | --- |
| ![Text_SOURCE.png](../../assets/Text_SOURCE.png) | ![Text_SOURCE_ZOOM.png](../../assets/Text_SOURCE_ZOOM.png) |
| **BRIGHT** | **BRIGHT DETAIL** |
| ![Text_BRIGHT.png](../../assets/Text_BRIGHT.png) | ![Text_BRIGHT_ZOOM.png](../../assets/Text_BRIGHT_ZOOM.png) |
| **DXTC** | **DXTC DETAIL** |
| ![Text_DXTC.png](../../assets/Text_DXTC.png) | ![Text_DXTC_ZOOM.png](../../assets/Text_DXTC_ZOOM.png) |
| **NVIDIA DXT1** | **NVIDIA DXT1 DETAIL** |
| ![Text_DXT1.png](../../assets/Text_DXT1.png) | ![Text_DXT1_ZOOM.png](../../assets/Text_DXT1_ZOOM.png) |

For composite text/hud images and related textures, you probably don't want to use DXTC, as this example shows. The block artifacting around the text makes it quite ugly. Bright or the uncompressed texture are better options.

### DXTC Nightmare

| SOURCE | SOURCE DETAIL |
| --- | --- |
| ![Haha_SOURCE.png](../../assets/Haha_SOURCE.png) | ![Haha_SOURCE_ZOOM.png](../../assets/Haha_SOURCE_ZOOM.png) |
| **BRIGHT** | **BRIGHT DETAIL** |
| ![Haha_BRIGHT.png](../../assets/Haha_BRIGHT.png) | ![Haha_BRIGHT_ZOOM.png](../../assets/Haha_BRIGHT_ZOOM.png) |
| **DXTC** | **DXTC DETAIL** |
| ![Haha_DXTC.png](../../assets/Haha_DXTC.png) | ![Haha_DXTC_ZOOM.png](../../assets/Haha_DXTC_ZOOM.png) |
| **NVIDIA DXT1** | **NVIDIA DXT1 DETAIL** |
| ![Haha_DXT1.png](../../assets/Haha_DXT1.png) | ![Haha_DXT1_ZOOM.png](../../assets/Haha_DXT1_ZOOM.png) |

This is truly unfair :-). With 16 unique colors in each 4x4 block, there's no way DXTC can even come close to compressing this in an acceptable manner. Bright has no problem, since there are only 16 unique colors in the whole texture.

## Conclusions

* Avoid DXT1 when guaranteed quality is needed - choose another DXTC variant that doesn't have issues on NVidia hardware, and check your DXT1 textures on NVidia hardware before committing to them.
* Don't use DXTC for special purpose textures where quality is of utmost importance, like text and height maps.
* Do use DXTC when compressing normal textures, the quality degradation is barely noticeable (DXT3/5).
* Since 8bit palettized textures are converted to 32bit before uploading, there's no benefit to them except the smaller stored size on disk. Use only when they look the same as an uncompressed 32bit.

