# Projector Textures

*Document Summary: A thorough reference to the Projector settings relevant to the ProjectiveTexture.**Document Changelog: Last updated by Jason Lentz (DemiurgeStudios?) for splitting up the Projectors documents into smaller more manageable docs. Original authors were Lode Vandevenne ([UdnStaff](https://udn.epicgames.com/Main/UdnStaff)) and Jason Lentz (DemiurgeStudios?).*

* [Projector Textures](ProjectorTextures.md#projector-textures)
  + [Introduction](ProjectorTextures.md#introduction)
  + [ProjTexture](ProjectorTextures.md#projtexture)
  + [ClampMode](ProjectorTextures.md#clampmode)
  + [FrameBufferBlendingOp & MaterialBlendingOp](ProjectorTextures.md#framebufferblendingop-materialblendingop)
  + [Guidelines for Creating ProjTextures](ProjectorTextures.md#guidelines-for-creating-projtextures)

## Introduction

The following settings describe the Projector settings that are relevant to the ProjectiveTexture including properties you will need to set in the properties of the Texture itself. For the rest of the Projector properties, see the [MainProjectorProperties](MainProjectorProperties.md) doc.

## ProjTexture

The Projective Textures are projected with Projectors. This is an actor class like any other, where you can set the texture you want it to project, the direction, the FOV, and more. The Projector is in the Actor Class Browser --> Projector. When you add one in your map, the Projector is represented with a projector sprite. To give the projector a texture, open the Texture Browser, and select the texture you want to use, preferably a texture with a transparent background. The texture should be a square texture, for example 256\*256, and not a texture with a different height and width, for example 256\*128. In the last case, the texture will be resized to make it a square. When you have selected the texture, go to the properties of the Projector, expand Projector and click on ProjTexture. Press the Use button that appears, so the name of the selected texture appears in the text field. Also, set the FOV setting to something higher than 0, because if this setting is 0 the projection will look weird. For example if you set it to 1, it'll be almost parallel.

![projprop.jpg](../assets/![projprop.jpg](../assets/projprop.jpg))

![texture.jpg](../assets/![texture.jpg](../assets/texture.jpg))Now that it has a texture, rotate the Projector with the Rotation Tool

![rotatebutton.jpg](../assets/![rotatebutton.jpg](../assets/rotatebutton.jpg))

, so the arrow points towards the wall, ground, terrain or whatever you want the texture to be projected at. You should also see a yellow box and a blue frustum when you selected the Projector. The blue frustum represents the rays of the projector, and the section of the surfaces with this box will get the projection (in most cases).

![rotate.jpg](../assets/![rotate.jpg](../assets/rotate.jpg))

When you rotated it towards a BSP wall that's close enough, you should see something like this:

![project1.jpg](../assets/![project1.jpg](../assets/project1.jpg))

## ClampMode

If you project the texture on something, it'll normally be repeating. Only if you set bClipBSP to True, it'll not be repeating on BSP, but on other things, such as large Static Meshes, it still will. To avoid this, you have to set the UClampMode and VClampMode of the used texture to TC\_Clamp. These settings are in the Texture Properties --> Texture.

![textureprops2.jpg](../assets/![textureprops2.jpg](../assets/textureprops2.jpg))

For example, if you leave for this texture UClampMode and VClampMode to TC\_Wrap, and you project the texture on this big Static Mesh, it'll be repeating:

![uvwrap.jpg](../assets/![uvwrap.jpg](../assets/uvwrap.jpg))

If you set UClampMode to TC\_Clamp and VClampMode to TC\_Wrap, it'll look like the first screenshot, and it you set UClampMode to TC\_Wrap and VClampMode to TC\_Clamp, it'll look like the second picture:

![uclamp.jpg](../assets/![uclamp.jpg](../assets/uclamp.jpg))

![vclamp.jpg](../assets/![vclamp.jpg](../assets/vclamp.jpg))When you set both UClampMode and VClampMode to TC\_Clamp, the texture will not be repeating anymore:

![uvclamp.jpg](../assets/![uvclamp.jpg](../assets/uvclamp.jpg))

Warning: when you use TC\_Clamp, make sure all the pixels at the edge of the texture are 100% transparent: otherwise, these outer pixels are spread over the whole surface. For example, if I set bAlphaTexture to False for the texture, it'll become 100% opaque, and the whole Static Mesh has got the red-greed gradient now. You also have to make sure all the mipmaps have a transparent border, otherwise you may see the texture spread out if you look at it from a distance. If you save it as a \*.dds file with the DDS Plug-in (in PSP or PhotoShop), make sure you set the Border Color of the mipmaps to something that will become transparent, this means 127-grey if you want to use the texture modulated, black if it's transparent, or the alpha channel is black at the borders if you want to use it as AlphaTexture.

![uvclamp2.jpg](../assets/![uvclamp2.jpg](../assets/uvclamp2.jpg))

If you want the texture to be repeating, set one or both of the settings to TC\_Wrap, and if you project on BSP surfaces, also make sure bClipBSP is False. On BSP, the texture will only be repeated on the walls that touch the blue frustum, for example the wall on the screenshot exists out of 2 BSP surfaces: the upper one with the green texture, and the lower one with the grey texture. The texture will only be repeated on both surfaces if the projector is placed this way, that the blue frustum touches both surfaces:

![wrap1.jpg](../assets/![wrap1.jpg](../assets/wrap1.jpg))

![wrap2.jpg](../assets/![wrap2.jpg](../assets/wrap2.jpg))

![wrap3.jpg](../assets/![wrap3.jpg](../assets/wrap3.jpg))

## FrameBufferBlendingOp & MaterialBlendingOp

These options two fields determine the blending operation between the material being projected onto and the projected texture. Below each of their effects are described. Nearly each combination of every setting can produce a different effect. Below is a list of what each setting will get you. I have used both a StaticMesh and a ProjTexture with AlphaChannels to illustrate all the nuances.This is the Texture used for the ProjTexture:

![projtexture.jpg](../assets/![projtexture.jpg](../assets/projtexture.jpg))

| FrameBufferBlendingOp = None | \_ |
| --- | --- |
| ![FrameN_MaterialN.jpg](../assets/![FrameN_MaterialN.jpg](../assets/FrameN_MaterialN.jpg)) | ![FrameN_MaterialM.jpg](../assets/![FrameN_MaterialM.jpg](../assets/FrameN_MaterialM.jpg)) |
| MaterialBlendingOp = None | MaterialBlendingOp = Modulated |
| ![FrameN_MaterialB.jpg](../assets/![FrameN_MaterialB.jpg](../assets/FrameN_MaterialB.jpg)) | ![FrameN_MaterialA.jpg](../assets/![FrameN_MaterialA.jpg](../assets/FrameN_MaterialA.jpg)) |
| MaterialBlendingOp = AlphaBlend | MaterialBlendingOp = Add |

| FrameBufferBlendingOp = Modulated | \_ |
| --- | --- |
| ![FrameM_MaterialN.jpg](../assets/![FrameM_MaterialN.jpg](../assets/FrameM_MaterialN.jpg)) | ![FrameM_MaterialM.jpg](../assets/![FrameM_MaterialM.jpg](../assets/FrameM_MaterialM.jpg)) |
| MaterialBlendingOp = None | MaterialBlendingOp = Modulated |
| ![FrameM_MaterialB.jpg](../assets/![FrameM_MaterialB.jpg](../assets/FrameM_MaterialB.jpg)) | ![FrameM_MaterialA.jpg](../assets/![FrameM_MaterialA.jpg](../assets/FrameM_MaterialA.jpg)) |
| MaterialBlendingOp = AlphaBlend | MaterialBlendingOp = Add |

| FrameBufferBlendingOp = AlphaBlend | \_ |
| --- | --- |
| ![FrameB_MaterialN.jpg](../assets/![FrameB_MaterialN.jpg](../assets/FrameB_MaterialN.jpg)) | ![FrameB_MaterialM.jpg](../assets/![FrameB_MaterialM.jpg](../assets/FrameB_MaterialM.jpg)) |
| MaterialBlendingOp = None | MaterialBlendingOp = Modulated |
| ![FrameB_MaterialB.jpg](../assets/![FrameB_MaterialB.jpg](../assets/FrameB_MaterialB.jpg)) | ![FrameB_MaterialA.jpg](../assets/![FrameB_MaterialA.jpg](../assets/FrameB_MaterialA.jpg)) |
| MaterialBlendingOp = AlphaBlend | MaterialBlendingOp = Add |

| FrameBufferBlendingOp = Add | \_ |
| --- | --- |
| ![FrameA_MaterialN.jpg](../assets/![FrameA_MaterialN.jpg](../assets/FrameA_MaterialN.jpg)) | ![FrameA_MaterialM.jpg](../assets/![FrameA_MaterialM.jpg](../assets/FrameA_MaterialM.jpg)) |
| MaterialBlendingOp = None | MaterialBlendingOp = Modulated |
| ![FrameA_MaterialB.jpg](../assets/![FrameA_MaterialB.jpg](../assets/FrameA_MaterialB.jpg)) | ![FrameA_MaterialA.jpg](../assets/![FrameA_MaterialA.jpg](../assets/FrameA_MaterialA.jpg)) |
| MaterialBlendingOp = AlphaBlend | MaterialBlendingOp = Add |

## Guidelines for Creating ProjTextures

The blending mode you are planning on using for your ProjTexture will determine how you will create your texture or you can look at it as how you create your texture will influence what blending mode you will choose. In more plain English here are what each of the blending modes do to your texture.**None** - Obviously, the Projector will still blend with this setting, but as best as I can tell, it defaults to Modulated. See below.**Modulated** - This is in effect *multiplies* the ProjTexture with the surface it is casting on similar to how the Multiply Layer effect works in Photoshop. A more technical explanation for what it's doing is that it's taking the RGB values from 0 to 255 and reducing them in a spectrum of -1.0 to 1.0, so that 128, 128, 128 grey is at 0.0. The result in more comprehensible terms is that using Modulated will allow you to brighten as well as darken surfaces with the Projector. To create transparency in the ProjTexture then make sure that the texture is set to be 128,128,128 grey where you don't want it to show up. If you are trying to create Shadows, this is the setting you want and you can use gray scale images to create the shadow.**AlphaBlend** - If you have an alpha layer in your ProjTexture, it will use this to determine transparency for the blending effect. You will also want to choose a MaterialBlendingOp to determine how the rest of the ProjTexture will blend with the surface it casts on.**Add** - This will literally "add" the RGB values of the ProjTexture with whatever surface it ends up casting on. This can only make the surface you are projecting on brighter. If you are using the PB\_Add mode, then to create transparency in your ProjTexture you will need an alpha layer in your texture or use solid black (RGB value: 0,0,0). This setting is best used for Projectors that simulate casting lights
