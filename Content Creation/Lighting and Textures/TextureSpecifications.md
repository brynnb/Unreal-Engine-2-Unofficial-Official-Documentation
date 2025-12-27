# Unreal Texture Specifications

*Last updated by Tom Lin (DemiurgeStudios?) for deprecation. Original author was Vito Miliano ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)).***This doc is obsolete.** Much of the information in here has been updated, changed, or rearranged. See this doc for the latest and greatest: [ModelingTableOfContents](../../Uncategorized/ModelingTableOfContents.md)

* [Unreal Texture Specifications](#unreal-texture-specifications)
  + [Texture dimensions](#texture-dimensions)
  + [Texture formats](#texture-formats)
    - [DirectX Texture Compression](#directx-texture-compression)
      * [DXT1](#dxt1)
      * [DXT3](#dxt3)
      * [DXT5](#dxt5)
    - [Eight-bit Palettized](#eight-bit-palettized)
    - [Eight-bit Palettized with Alpha](#eight-bit-palettized-with-alpha)
    - [32-bit RGBA](#32-bit-rgba)
  + [Recommendation](#recommendation)
  + [Creating Textures](#creating-textures)
    - [DXTC](#dxtc)
      * [NVIDIA DXT Compression Tools](#nvidia-dxt-compression-tools)
      * [Microsoft DXTex Tool](#microsoft-dxtex-tool)
    - [Creating P8 Textures](#creating-p8-textures)
    - [Creating RGBA Textures](#creating-rgba-textures)

## Texture dimensions

Unreal texture dimensions may be any powers of two from 32 to 2048. Textures need not be square. Sizes such as 256x256, 1024x128, and 2048x32 are acceptable, but should not be smaller than 32x32.

## Texture formats

Unreal supports five texture formats: DirectX Texture Compression (DXTC), 8-bit palettized (P8), and 32-bit RGBA textures; and 8-bit and 16-bit greyscale heightmaps. The former three are discussed in this document, and the latter two are discussed in the terrain documentation.

### DirectX Texture Compression

DXTC is the native, compressed texture format used in DirectX 8. In many cases, DXTC reduces texture memory usage by 50% or more over palettized, 8-bit textures, allowing for twice the textures at the same resolution, or the same number of textures at twice the resolution. Three DXTC formats are available.

#### DXT1

DXT1 is a four-bit compressed color format that allows for opaque, and one-bit alpha textures; that is, textures with no transparency at all, and textures with a single transparent color. **A hardware bug in all nVidia chipsets, including the NV20 (GeForce3), potentially makes DXT1 textures gross and ugly.** Specifically, decompression is performed in 16-bit color mode internally, making the resulting texture potentially unacceptable for use, especially when combined with other operations. **Test your DXT1 textures on nVidia hardware before committing to their use.** All other DXTC formats on nVidia hardware are okay, as textures are decompressed in 32-bit color internally.

#### DXT3

DXT3 adds support for a four-bit explicit alpha channel, on top of DXT1's color compression. Four-bit explicit alpha allows for sixteen distinct alpha values, making it good for textures with sharply contrasting translucent/opaque areas.DXT2 textures assume the color data is premultiplied by the alpha channel, and are not supported.

#### DXT5

DXT5 support a four-bit interpolated alpha channel. Three bits are used to determine explicit alpha values, and two eight-bit values are used to interpolategradually between them. This makes the format especially suited for soft gradients and other textures where the alpha areas vary less wildly.DXT4 assumes colors are premultiplied by the alpha channel, and is not supported.

### Eight-bit Palettized

P8 textures, as they are denoted in the editor, are the same 8-bit palettized (256 color) textures used in the build 436 engine and earlier (*Unreal* and *Unreal Tournament* timeframe). Even though they are uploaded to the video card as a full 32-bit RGBA texture, when properly quantized a P8 can look identical to the original 24-bit source art, while still offering a 75% savings in disk and system memory.P8 textures offer 1-bit alpha in the form of a mask color. If a texture is imported as masked, color index 0 is set as transparent. Once you palettize your texture, you'll need to edit your 256-color image and apply color zero to the transparent portions of the texture.

### Eight-bit Palettized with Alpha

A special variation on P8 is the alpha-palettized format where each one of the 256, 32-bit palette entries holds an RGBA value instead of RGB. This is mostly relevant only for the PSX2 builds of the engine; given the PSX2 architecture, it's the most efficient form of storing a variable-alpha texture. The catch is that having to put variable alpha in a palette diminishes the already limited color variety available; but in many cases this isn't significant, and several font-and user interface textures have been created this way. See also the included text file in the attached `[alphapal.zip](../../assets/alphapal.zip)`, which contains AlphaPal.exe, a special alpha-aware version of the Bright utility, which generates BMP 8-bit alpha-palettized textures.

### 32-bit RGBA

32-bit RGBA is the obese godfather of textures. While extremely powerful, it's also terribly overweight. It features full 24-bit color, plus an 8-bit alpha channel, but takes up four bytes for every pixel; a 256x256 texture will require 256k of memory.

## Recommendation

Use DXT1 textures as much as is possible. While artists need to examine DXT1 versions of their textures due to the penetration of nVidia hardware with the decompression bug, the greatest space savings can be had with them.If watching for rendering artifacts is not an option, DXT5 supports the most flexible alpha channels, while not increasing memory usage beyond that of a normal 8-bit palettized texture.Also, if you need full color resolution for a texture, without an alpha channel, use an 8-bit palettized texture. While requiring the same amount of video memory, disk and system memory usage is a mere 25% of full RGBA, and the differences are undetectable in most cases. Use full RGBA only when DXT3/5 do not suffice in the both the color and alpha quality department, in highly visible expanses, such as skies.

## Creating Textures

### DXTC

Once you've produced a 24-bit color texture to use in-game, you'll need to convert it to the DXTC *DDS* format (DirectDrawSurface, the native DirectX texture format) for importing into UnrealEd. To do this, you'll need one of these two utilities.

#### NVIDIA DXT Compression Tools

![dds.jpg](../../assets/dds.jpg)

This Adobe-compatible plugin, produced by nVidia, allows you to open and save DDS files. Saving to DXT1, DXT3 and DXT5 formats is support, with or without autogenerated mipmaps. Support for saving uncompressed 16-bit and 32-bit images is also provided.The current version sports a preview mode for seeing what the texture will look like when rendered by the hardware, including emulation of the Xbox DXT1 hack fix. As a result, it requires DirectX 8 and a compatible video card, preferably one with a GeForce-series chipset.Standalone command-line utilities are also provided to batch compress images, extract mipmaps, and merge mipmaps, as well as a library to integrate these functions into your own application.The `[dxt_tools.zip](../../assets/dxt_tools.zip)` provided below contains all of these files, taken directly from the FTP site directory of the same name.

#### Microsoft DXTex Tool

This is a standalone compression utility, provided as part of the MS DirectX 8.1b SDK. It can open multiple BMP (Windows Bitmap) and DDS files. Bitmaps cannot have alpha channels, so it also supports opening separate BMP files as alpha channels, either explicitly or implicitly, using a \_a.bmp naming convention. Textures can be converted to all five DXTC formats. The utility can also be run from the command-line if desired. The current version of the DX8.1b SDK, released **8/12/2001**, is a 167mb installer, available here:<http://download.microsoft.com/download/DirectX/Patch/8.1b/W982KMeXP/EN-US/DX81b_SDK.exe>

### Creating P8 Textures

Steadfastly outperforming every other 8-bit color quantizer or palettization tool on the market is *Bright*, by Epic's own Erik de Neve. In fact, it's so good, we don't even bother telling you about anything else, and we have the comparisons to prove it.Bright is available in both Photoshop plugin and standalone commandline utility form. The commandline version is more robust, allowing you to specify multiple files that you would like to share a palette, specify the color to use as a mask, as well as to tweak the color quantization options themselves. The plugin simply exports an 8-bit Windows BMP file.The current version of the standalone command-line utility, version **1.81**, released **January 13, 1999**. The current version of the Adobe-compatible plugin was released **February 26, 2001**. Both are provided in the `[bright181.zip](../../assets/bright181.zip)` below.

### Creating RGBA Textures

32-bit RGBA textures are Targa (TGA) format graphic files, 24-bit, compressed or uncompressed, with or without an alpha channel.

