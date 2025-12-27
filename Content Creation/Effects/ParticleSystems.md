# Particle Systems

*Document Summary: A comprehensive guide to Emitters using the new Particle System Editor (available in the UDN build).**Document Changelog: Last updated by Chris Linder (DemiurgeStudios?), to update for UDNBuild 2226. Original authors were Albert Reed, Chris Linder, and Tom Lin (DemiurgeStudios?).*

## Unsupported Disclaimer

The code described in this document is provided to you as a service of UDN or other licensees. It is not supported by Epic.

* [Particle Systems](#particle-systems)
  + [Unsupported Disclaimer](#unsupported-disclaimer)
  + [Introduction](#introduction)
  + [Quick-Start](#quick-start)
    - [Creating the Particle System](#creating-the-particle-system)
    - [Editing the Particle System](#editing-the-particle-system)
    - [Adding a Sprite Emitter](#adding-a-sprite-emitter)
    - [Making Them Move](#making-them-move)
    - [Picking a Texture](#picking-a-texture)
    - [Play around](#play-around)
  + [Particle Editor Interface](#particle-editor-interface)
    - [Adding an Emitter](#adding-an-emitter)
    - [Editing Emitters](#editing-emitters)
    - [Deleting an Emitter](#deleting-an-emitter)
    - [Refreshing](#refreshing)
    - [Exporting](#exporting)
    - [Duplicate Emitter](#duplicate-emitter)
    - [Save/Load Emitter](#saveload-emitter)
    - [Getting Help](#getting-help)
  + [Parameter Reference](#parameter-reference)
    - [General](#general)
    - [Texture](#texture)
    - [Rendering](#rendering)
    - [Color/Fading](#colorfading)
    - [Time](#time)
    - [Movement](#movement)
    - [Location](#location)
    - [Mesh Spawning](#mesh-spawning)
    - [Skeletal Mesh](#skeletal-mesh)
    - [Rotation](#rotation)
    - [Revolution](#revolution)
    - [Size](#size)
    - [Collision](#collision)
    - [Sounds](#sounds)
    - [Mesh](#mesh)
    - [Spark](#spark)
    - [Beam](#beam)
    - [Beam Noise](#beam-noise)
    - [Beam Branching](#beam-branching)
    - [Trigger](#trigger)
  + [Editing the "Old Way"](#editing-the-old-way)

## Introduction

Particle systems are tools for creating various effects which cannot be creating using static geometry or animations. These effects are achieved by having several instances of the same thing, usually sprites, move and change in a pattern. Using this simple concept artists can create effects as diverse as waterfalls, flames and lightening.Note for old-school engine users: In the Unreal Engine, particle systems are called *Emitters*. In this document when we refer to particle systems we are talking about the *Emitter* actor. A particle system does nothing by itself but rather is composed of one or more of *Sprite Emitters*, *Mesh Emitters*, *Beam Emitters* or *Spark Emitters*. (Note that these \_ "emitters"\_ are not the actor *Emitter* nor are they derived from the actor *Emitter*) A single particle system can contain as many or few of these as you wish.To get you started the following section of the manual will walk you through creating your first emitter. After that we'll cover the interface to the editor, give you some more examples and finally there is a reference which explains every parameter in the Particle system editor.

## Quick-Start

### Creating the Particle System

Begin with a new map and subtract out a 1024x1024x1024 cube from the world (If you need more help with this check out the [UnrealEdInterface](../Basics/UnrealEdInterface.md) document) If you prefer, you may edit an existing level. Add a few lights to the empty cube and do a **Build->Build All**. Your level should look something like this:

![emptyroom.jpg](../../assets/![emptyroom.jpg](../../assets/emptyroom.jpg))

With the room setup, open up the actor browser and select **Emitter**.

![actorbrowser.jpg](../../assets/![actorbrowser.jpg](../../assets/actorbrowser.jpg))

Right-click on the far wall and select **Add Emitter Here**.With your emitter created we are now ready to start editing it. Before we do however, make sure you have *Realtime Preview* turned on by clicking the joystick at the top of the viewport like this:

![realtimepreview.jpg](../../assets/![realtimepreview.jpg](../../assets/realtimepreview.jpg))

With that selection you'll be able to see the changes you make to your emitters update in realtime. Before moving on, drag the emitter to the middle of the room so there will be plenty of space when it begins emitting particles.

### Editing the Particle System

With the emitter selected pull down **Particle Editor** from the **Tools** menu in UnrealEd. A window like this will appear:

![blankemitter.jpg](../../assets/![blankemitter.jpg](../../assets/blankemitter.jpg))

.From this tool you will be doing all of your particle editing.

### Adding a Sprite Emitter

The [introduction](#introduction) of this manual explains that particle systems can be made up of *Sprite Emitters*. The first thing to do is to add a sprite emitter to your particle system. To do this click the

![newemitterbutton.jpg](../../assets/![newemitterbutton.jpg](../../assets/newemitterbutton.jpg))

*New Particle Emitter* button in the top toolbar of the particle editor.
Fill the the dialoge that appears like this and click Ok.

![newdlg.jpg](../../assets/![newdlg.jpg](../../assets/newdlg.jpg))

.This will create a new Sprite Emitter called "MyFirstEmitter". After you click okay. The Particle System Editor will now look like this:

![myfirstemitter.jpg](../../assets/![myfirstemitter.jpg](../../assets/myfirstemitter.jpg))

If everything worked correctly, you'll notice your particle system has begun spitting out some ugly particles and will look like this:

![firstparticles.jpg](../../assets/![firstparticles.jpg](../../assets/firstparticles.jpg))

.

### Making Them Move

Right now the particle system doesn't do much at all. The first step in making it a bit more interesting is to get the particle to move rather than piling up in one place. To do this select the [Movement](#movement) category from the left-hand column. The large scrolling area on the right will zip down to the Movement heading. Fill in the values under [Start Velocity](#start-velocity) to look like this and things will start to happen.

![startvelocity.jpg](../../assets/![startvelocity.jpg](../../assets/startvelocity.jpg))

The [Start Velocity](#start-velocity) settings, like most of the settings in the particle system editor change things in real time. You can type numbers in or you can click and **drag** the buttons next to the fields to change values and watch the system change as you drag. You can also "link" values together so you don't have to change each one individually.

![startvelocity2.jpg](../../assets/![startvelocity2.jpg](../../assets/startvelocity2.jpg))

### Picking a Texture

Another major change you can make to a particle system is to change the texture it is using for the sprites. From the texture browser, select a texture and then under the [Texture](#texture) category click the **Use** button in the [Texture](#texture) field.

### Play around

Take some time to play around with all the properties available to you. They may not all make sense the first time around but most do what they say. If at anytime you want further explanation visit the [reference](#parameter-reference) section of this document. [Acceleration](#acceleration), [Max Number Of Particles](#max-number-of-particles), [Lifetime](#lifetime), [Fading](#fading), and [Start Location](#startlocation) are all good places to start.

## Particle Editor Interface

### Adding an Emitter

To add an emitter to a particle system click the

![newemitterbutton.jpg](../../assets/![newemitterbutton.jpg](../../assets/newemitterbutton.jpg))

*New Particle Emitter* button in the top toolbar of the particle editor. This dialogue will appear:

![newdlg.jpg](../../assets/![newdlg.jpg](../../assets/newdlg.jpg))

Give your particle system a name and select the type you would like and click *Ok*.

### Editing Emitters

#### Categories

The left column contains a list of categories which organize the various properties of a given emitter. Clicking on the categories will scroll to that set of variables. Checking and unchecking the boxes will show and hide those categories.

![categories.jpg](../../assets/![categories.jpg](../../assets/categories.jpg))

#### Controls

There are several types of controls that are used in the particle system editor. Almost all of the controls have fields where you can values and watch the particle system change. Some properties will force the system to re-start others will update smoothly in realtime.All of the numeric fields have "Scroll Buttons"

![scrollbutton.jpg](../../assets/![scrollbutton.jpg](../../assets/scrollbutton.jpg))

next to them. These buttons make it simple to edit the values in the corresponding text boxes. Clicking, holding and dragging a scroll button will cycle the value inside of the text box up or down. You can also just click up and down to increment the value.Many of the controls also have a Hide/Expand button

![hideexpand.jpg](../../assets/![hideexpand.jpg](../../assets/hideexpand.jpg))

which can be used to hide or show a tool.

![rangevectedit.jpg](../../assets/![rangevectedit.jpg](../../assets/rangevectedit.jpg))

Some controls have mins and maxes. In addition to being able to set the individual components of the vector with the scroll buttons, you can click the Different/Same/Mirror button to alter the min and max of a variable in sync.

* The blue and red Lego signify that you can edit min and max independent of each other.
* The two blue Legos signify that the values in min and max will be kept the same.
* The two red Legos signify that the min and max values will be mirrored. For example, setting the max to 40.0 will automatically set the Min to -40.0.

Some controls like [Start Velocity](#start-velocity) have a min and max for several fields, in this case X, Y and Z. Checking the check boxes on the right of the tool will keep the checked X, Y or Z values the same.

### Deleting an Emitter

Clicking the Delete Emitter button

![deleteemitter.jpg](../../assets/![deleteemitter.jpg](../../assets/deleteemitter.jpg))

will remove the emitter tab currently selected from the particle system.

### Refreshing

Many particle systems aren't designed to be going constantly. For example, a muzzle flash or breaking glass need to be restarted in order to preview them properly. Clicking the *Refresh Button*

![refresh.jpg](../../assets/![refresh.jpg](../../assets/refresh.jpg))

causes a system to start over.

### Exporting

If you need to spawn a particle system dynamically in-game you'll need to make a script out of it. You might also want to make a script so that your particle system is availible in the actor browser. To create a script click the

![exportbutton.jpg](../../assets/![exportbutton.jpg](../../assets/exportbutton.jpg))

*Export to Script* button.

![exporttoscript.jpg](../../assets/![exporttoscript.jpg](../../assets/exporttoscript.jpg))

Fill in the package and name of the actor you want to create and click *Ok* to export the script. Checking *Auto Destroy* creates an actor that will delete itself when it no longer has particles. You will need to recompile the package the script was exported to in order for it to work or show up in the editor.

### Duplicate Emitter

Clicking the

![duplicatebutton.jpg](../../assets/![duplicatebutton.jpg](../../assets/duplicatebutton.jpg))

*Duplicate Emitter* button will cause the emitter currently being edited to be duplicated and added as the last tab.

### Save/Load Emitter

Individual emitters can be saved to ".emt" files for later use by clicking the

![savebutton.jpg](../../assets/![savebutton.jpg](../../assets/savebutton.jpg))

*Save Emitter* button. These files may later be loaded into a particle system by clicking on the

![openbutton.jpg](../../assets/![openbutton.jpg](../../assets/openbutton.jpg))

*Open Emitter* button.

### Getting Help

You can also use the context-help tool

![helpbutton.jpg](../../assets/![helpbutton.jpg](../../assets/helpbutton.jpg))

at the top of the UnrealEd toolbar. Click that button once and then click on any of the tool headings to open up this page's help section on that tool.

## Parameter Reference

The referance section of this document borrows heavily from Lode Vandevenne's original emitter tutorial which is masterful piece of work from dark and troubled times.

### General

![generalcat.jpg](../../assets/![generalcat.jpg](../../assets/generalcat.jpg))

#### Disable

If Disable is checked, the particle emitter will not work. You can for example use it if you want to remember the settings of a p particle emitter, but you currently don't want it to work in the map.

#### Max Number of Particles

The Max Number of Particles setting sets the maximum number of particles that may be on screen for this Particle Emitter. If the maximum number is reached, the oldest particle gets killed, so a new one can get spawned. If you set it to 0, the editor crashes. For example, if you set this number to 4, there will be 4 particles on screen once the warmuptime is over. On the screenshot, the particles are moving to the left, and the most left one gets destroyed while a new one appears on the right:

![maxparticles.jpg](../../assets/![maxparticles.jpg](../../assets/maxparticles.jpg))

This setting is quite important, especially if you want to reduce the amount of particles on screen to get more performance.

#### Name

This parameter simply gives the particle system a name. Next time you load the editor, the new *Name* will appear on the tab.

#### Respawn Dead Particles

Unchecking this box will cause dead particles not to respawn. If you are making an explosion or other tempoary effect, uncheck this box.

#### Automatic Spawning

Automatic Spawning causes the number of particles to remain equal to Max Number of Particles regardless of other particle system properties. For example, with this box checked and Max Particles set to 10 once the system warms up there will always be exactly 10 particles regardless of the [Lifetime](#lifetime) of the system. With Automatic Spawning checked you cannot directly control how many [Particles Per Second](#particles-per-second) are spawned.

#### Particles Per Second

With Automatic Spawning unchecked, you can now control the rate at which your particles are released. Keep in mind that no matter what you can not cause there to be more particles than what [Max Particles](#max-number-of-particles) is set to.

#### Scale Emitter

This tool adjusts several properties throughout the editor to make your emitter larger or smaller. Pick a value and click the apply button to scale the emitter.

### Texture

![texturecat.jpg](../../assets/![texturecat.jpg](../../assets/texturecat.jpg))

#### Texture Picker

Select a texture from the texture browser and click the **Use** button to use that texture on your emitter.

#### Draw Style

Using the Draw Style property you can change the way the texture is drawn in the map. The Draw Style for Particles is somewhat the same as the Draw Style you find under Display of normal actors, but has some added options, and some other removed.For the example screenshots, the blue texture is one without alphachannel, and the second one is a texture with different colors and an alphachannel that has 16 dark dots, like this:

![alphatexture1.jpg](../../assets/![alphatexture1.jpg](../../assets/alphatexture1.jpg))

*Regular* makes the texture opaque, so it's a non-transparent square.

![regular2.jpg](../../assets/![regular2.jpg](../../assets/regular2.jpg))

![regular.jpg](../../assets/![regular.jpg](../../assets/regular.jpg))

![regular3.jpg](../../assets/![regular3.jpg](../../assets/regular3.jpg))

*Alpha Blend* makes the darker parts of the A-channel of the RGBA texture more transparent than the bright parts. Black becomes 100% transparent (invisible) and white becomes 100% opaque. Grey becomes semi-transparent. This effect is not good visible on very bright textures.

![alphablend2.jpg](../../assets/![alphablend2.jpg](../../assets/alphablend2.jpg))

![alphablend.jpg](../../assets/![alphablend.jpg](../../assets/alphablend.jpg))*Modulated* makes the texture some sort of inverse translucent: it makes the brightest colors of the texture more transparent than the darkest colors, so black becomes opaque, white becomes 100% transparent (invisible). Grey, red, blue, etc... become semi-transparent.

![modulated2.jpg](../../assets/![modulated2.jpg](../../assets/modulated2.jpg))

![modulated.jpg](../../assets/![modulated.jpg](../../assets/modulated.jpg))*Translucent* makes the darkest colors of the texture more transparent than the brightest colors, so white become opaque, while black become 100% transparent (invisible). Grey, red, blue, etc... become semi-transparent.

![translucent2.jpg](../../assets/![translucent2.jpg](../../assets/translucent2.jpg))

![translucent.jpg](../../assets/![translucent.jpg](../../assets/translucent.jpg))*AlphaModulate* makes the actual RGB texture brighter on places where the alphachannel is darker. It looks somewhat the opposite of *Alpha Blend*. This effect isn't good to see on very bright textures.

![alphamodulate2.jpg](../../assets/![alphamodulate2.jpg](../../assets/alphamodulate2.jpg))

![alphamodulate.jpg](../../assets/![alphamodulate.jpg](../../assets/alphamodulate.jpg))*Darken* makes the colors of the texture negative and translucent.

![darken2.jpg](../../assets/![darken2.jpg](../../assets/darken2.jpg))

![darken.jpg](../../assets/![darken.jpg](../../assets/darken.jpg))*Brighten* makes the texture to brighten the background, so the texture becomes translucent and brighter than it's original version.

![brighten2.jpg](../../assets/![brighten2.jpg](../../assets/brighten2.jpg))

![brighten.jpg](../../assets/![brighten.jpg](../../assets/brighten.jpg))As you can see, the alphachannel of an RGBA8 texture is only used for the Draw Styles *Alpha Blend* and *Alpha Modulate*.

#### Subdivisions

You can divide one texture into different subdivisions. You can make the particles randomly pick one of the textures, or make one particle change from one subdivision to another during it's [Lifetime](#lifetime). You have to make a texture that can be used for this yourself: divide into a \* b equal rectangles, and give every rectangle it's own picture. For example, this is a texture that can be divided into 3 \* 3 = 9 Subdivisions:

![shapes.jpg](../../assets/![shapes.jpg](../../assets/shapes.jpg))

To set the Subdivisions, use U-Subdivisions and V-Subdivisions for the horizontal and vertical Subdivisions.
Setting these settings to 0 or 1 does exactly the same: it divides the texture into 1 Subdivision, meaning there are no Subdivisions at all (the Subdivision is the texture itself), so the particles will look like this:

![subdiv1.jpg](../../assets/![subdiv1.jpg](../../assets/subdiv1.jpg))

If you set both U-Subdivisions and V-Subdivisions to 3, it looks like this:

![subdiv2.jpg](../../assets/![subdiv2.jpg](../../assets/subdiv2.jpg))

If you set them to 2 or 4, some pictures of this texture will be cut into half, because it has 3 \* 3 Subdivisions and isn't made for other values.

![subdiv3.jpg](../../assets/![subdiv3.jpg](../../assets/subdiv3.jpg))

![subdiv4.jpg](../../assets/![subdiv4.jpg](../../assets/subdiv4.jpg))If you set respectively U-Subdivisions=1 and V-Subdivisions=3 or U-Subdivisions=3 and V-Subdivisions=1, it'll look like this:

![subdiv13.jpg](../../assets/![subdiv13.jpg](../../assets/subdiv13.jpg))

![subdiv31.jpg](../../assets/![subdiv31.jpg](../../assets/subdiv31.jpg))If you check the Use Random Subdivision box the Emitter will give each particle a random Subdivision at the beginning, and the particle keeps this Subdivision as long as it lives.

![subdiv5.jpg](../../assets/![subdiv5.jpg](../../assets/subdiv5.jpg))

If leave Use Random Subdivision un-checked, the particles will change during their [Lifetime](#lifetime). For example if you'd have 2 \* 2 Subdivisions, then first they'll have the upper left Subdivision, then the bottom left, then the upper right and finally the bottom right. The time it takes to change from one Subdivision to another, depends on their [Lifetime](#lifetime), more about this further in the section Time. On the screenshot, there are 9 Subdivisions.

![subdiv6.jpg](../../assets/![subdiv6.jpg](../../assets/subdiv6.jpg))

If you check Blend Between Subdivisions (and Use Random Subdivision is not checked), the particles will Fade from one Subdivision to another:

![subdivblend.jpg](../../assets/![subdivblend.jpg](../../assets/subdivblend.jpg))

Normally, the particles go through the different Subdivisions this way, that they will have all the Subdivision one for the same amount of time. The time is divided in equal parts for each Subdivision. If you don't want this, you can use the Subdivision Scale feature. To do this, first check the Use Subdivision Scale box. Next, click the *Insert* button under Subdivision Scale that so there are 3 Subdivision Scales (then 4 of the 9 Subdivisions will be used). If you want the 9 Subdivisions to be used, you have to make 8 Subdivision Scales. If you make less than 8 Subdivision Scales, the last Subdivisions will never appear. There's also nothing wrong with making too many Subdivision Scales, then the last ones will just be ignored.The Subdivision Scale is relative to the [Lifetime](#lifetime) of the particles (see the section [Time](#time) for this), so a Subdivision Scale of 1.000000 takes as long as the [Lifeime](#lifetime) of the particles. Each Subdivision Scale represents a certain point in the Lifetime of the particle. For example if the [Lifetime](#lifetime) is 4 seconds, a Subdivision Scale of 0.25 is the end of the first second of the Lifetime. A successive Subdivision Scale should always be larger than the previous one, otherwise you're going back in time and it will be ignored. For example if you make Subdivision [0] = 0.1, [1] = 0.3 and [2] = 0.6, and LifeTimeRange is 4 seconds, the particle will have Subdivision 1 for 0.4 seconds, then Subdivision 2 for 0.8 seconds, Subdivision 3 for 1.2 seconds and Subdivision 4 for the remaining 1.6 seconds. On the screenshot, the particles move from left to right.

![subdivscale1.jpg](../../assets/![subdivscale1.jpg](../../assets/subdivscale1.jpg))

If you make Subdivision Scale [0] = 0.4 and [1] = 1, only two of the Subdivisions will be used. Then it doesn't matter anymore what value you entered in [2].

![subdivscale2.jpg](../../assets/![subdivscale2.jpg](../../assets/subdivscale2.jpg))

To get this effect at it's best, you have to use the correct LifeTimeRange and also make sure the [Number of Particles](#max-number-of-particles) value is high enough. Read sections [General](#general) and [Time](#time) for this.Use the Subdivision End and Subdivision Start values if you want only a few Subdivisions of the texture to be used. Subdivision 0 is the Subdivision in the upper left corner of the texture, Subdivision 1 the one below that, and the last one is in the lower right corner of the texture. This picture shows the numbering:

![subdiv.jpg](../../assets/![subdiv.jpg](../../assets/subdiv.jpg))

#### Custom Texture Set

This option is only shown when the emitter is a mesh emitter. This is different set of textures to use instead of the standard texture for the selected mesh. See [Mesh](#mesh) for more details on mesh emitters.

### Rendering

![renderingcat.jpg](../../assets/![renderingcat.jpg](../../assets/renderingcat.jpg))

#### Disable Fogging

If chcked, the fogging on the particles will be disabled, so you can see them through the distance fog.

#### Alpha Test/Alpha Ref

When checked, the video hardware will not write pixels that already has accumlated an alpha value of Alpha Ref.

#### Z-Test

The the default and normal behavior for emitters is with this box checked. Unchecking this box makes the emitter draw on top almost everything. This may not draw on top of other emitters with z-test unchecked or other alpha'ed objects.

#### Z-Write

This causes the particles to write to the Z-buffer. ("In a graphics card, this section of video memory keeps track of which onscreen elements can be viewed and which are hidden behind other objects." - CNET Glossary)

### Color/Fading

![colorfadingcat.jpg](../../assets/![colorfadingcat.jpg](../../assets/colorfadingcat.jpg))

#### Opacity

This utility tool will adjust the translucency of the entire emitter. It changes several properties in the Color/Fading category.

#### Fading

With this, you can make the particles fade in or fade out, for example when they fade in they are invisible at the beginning and become more and more visible. You can also make only a few of the colorchannels fade, so for example the red and green parts of the texture will be invisible while the blue parts are always visible.To cause your particle emitter to fade in, drag the *Fade-In End Time* slider away from the left side. On the screenshot, the particles have a [Lifetime](#lifetime) of 5.0 and a Fade In End Time of 5.0, so they are 100% visible at the moment they die:

![fadein.jpg](../../assets/![fadein.jpg](../../assets/fadein.jpg))

*Fade-Out Start Time* works the same as *Fade-In End Time*. If this is 0 (Slider all the way to the left) the particles will will already start fading when they're born and be completely Faded out at the moment they die. On the screenshot, *Fade-Out Start Time* is 1.

![fadeout.jpg](../../assets/![fadeout.jpg](../../assets/fadeout.jpg))

#### Fade Out/In Factor

You can use *Fade In Factor* and *Fade Out Factor* to fade individual color channels. If the values are 1, the particles fade normally. If you make for example R = 0, the red channel will get changed 0%, so while the other colors are invisible (this is at the start of a fade in, or the end of a fade out), the red will still be visible (left part of the first screen). Or when G = 0, the green will still be visible (right part of the first screen). If R and G are 0, both will be visible, it looks somewhat yellowish here (left part of the second screen). If R, G and B are 5, the whole texture will get super-invisible so it fades out much faster (right part of the second screen). If R, G and B would all be 0, the texture wouldn't get invisible at all.

![fade3.jpg](../../assets/![fade3.jpg](../../assets/fade3.jpg))

![fade4.jpg](../../assets/![fade4.jpg](../../assets/fade4.jpg))

#### Color Multiplier Range

The *Color Multiplier Range* is a multiplier that is applied to each particle individually at the start of its lifetime. This can be used in two main ways; to give the particles random variation in color, and to adjust the color of the emitter without having to change the texture or the color scale. To give the particles a slightly random color set the min and max of a field to different values; the wider the range the more the variation in color. To adjust the color of the emitter just change the value of R, G, or B to make the emitter less Red, Green or Blue.

#### Use Color Scale

This turns on the use of color scale and color scale repeats (see below)

#### Color Scale

This is another scale that can be applied to the particles. A scale changes something of the particle during its lifetime, in this case the color. To use a Color Scale, first set "Use Color Scale" to True, and then add a new color bar. To add a new a new color bar double click somewhere in the color scale box. This will bring up a color picker window where you can pick a color and click OK. This will show the color you choose on a vertical bar where you double clicked.

![colorfade1.jpg](../../assets/![colorfade1.jpg](../../assets/colorfade1.jpg))

You can change this color at any time by double clicking on the color to bring up the color picker window or by single clicking on the color and manually adjusting the R, G, B, and A values. The alpha values (which only are only relevant for alpha blend mode) must be changed manually in this way because the color picker does not support alpha. The color in the color bar is combined with the color of the texture so if your texture is bluish and your color bar is white, the particle will still look bluish. If the color bar is cyan on the other hand, the particle will look more cyan but not as cyan as the color bar. White textures generally work best with color scale because they take the color of the color bars best.The position of the color bar represents the relative time of this color. This is the time in the life of the particle that the particle will be the color you have chosen. If the color bar is in the middle of the Color Scale the value will be somewhere around 0.5. If the lifetime of the particles is 4.0 seconds, about 2.0 seconds into the particle's life it will be the color you have chosen. The relative time can be changed by dragging the color bar or manually adjusting the relative time field below the Color Scale box.Color scale is most useful with two or more color bars. If you do not have a color bar at the far right of the Color Scale box, the color of the particles will pop back their normal color after the rightmost color bar. This is generally undesired. If you do not have a color bar at the far left of the Color Scale box, the system will behave as if there is a white color bar there. This is an example of 3 color bars used with a white texture. The middle color bar is selected so the field values correspond to that color bar.

![colorfade2.jpg](../../assets/![colorfade2.jpg](../../assets/colorfade2.jpg))

#### Color Scale Repeats

With "Color Scale Repeats", the Color Scale process can be repeated an arbitrary number of times. The default is 0 which means that the color scale with work once, but not repeat any times. With the value set to 1.0, there will be two scales, once for the normal color scale and one repeat. This is the same color scale as above but with "Color Scale Repeats" set to 1.0.

![colorfade3.jpg](../../assets/![colorfade3.jpg](../../assets/colorfade3.jpg))

This is an image with color scale repeats set to 2.5. Note how the color ends on green, which is in the middle of the color scale.

![colorfade4.jpg](../../assets/![colorfade4.jpg](../../assets/colorfade4.jpg))

### Time

![timecat.jpg](../../assets/![timecat.jpg](../../assets/timecat.jpg))

#Lifetime

#### Lifetime

The Lifetime is the number of seconds the particle will live. After this time, it gets destroyed and might respawn.

#### Initial Time

The \_Initial Time\_ lets the particles be several seconds old already when they get spawned. If [Lifetime](#lifetime) is 4 and \_Initial Time\_ is 3, the particle will already be 3 seconds old when spawned and live for only one second. This setting can be interesting when you use scales: the [Subdivision Scale](#usesubdivisionscale), [Color Scale](#color-scale) and [SizeScale](#size-scale) will also be calculated as if they're 3 seconds old already.

#### Initial Delay

The *Initial Delay* is the time it takes before the emitter starts its job. For example, if you enter an *Initial Delay* of 5, when you start the map or click [[#Refreshing][refresh], it'll do nothing for 5 seconds before it starts emitting.For all the settings you can use a Min and Max value. If you make them the same, that exact value will be used. If you make Min smaller than Max, every particle will get it's own random LifeTimeRange or InitialTimeRange when it gets spawned, and this random value is something between Min and Max. If you use a random LifeTime, the particles will look like the screenshot at constant speed: there appear holes because some of the particles die already while others are still continuing their way.

![randomlifetime.jpg](../../assets/![randomlifetime.jpg](../../assets/randomlifetime.jpg))

#### Seconds Before Inactive

When this value is 0.000000, the movements of the particles are always calculated by the computer, even if they're out of view. If you enter a value in here, the computer will stop calculating the movements of the particles after the Emitter actor is out of view for this many seconds. This way you gain performance. So when you look away from the Emitter, the particles will freeze, and only come back to life when you look at them again. So when *Seconds Before Inactive* = 0.010000 and you see this:

![initial1.jpg](../../assets/![initial1.jpg](../../assets/initial1.jpg))

and then rotate the camera 180�, wait an hour and then look again at the Emitter, you'll still see exactly the same image (where the warmup is not finished yet). When you can't see the Emitter actor, but you should be able to see some particles, you will not see these particles! Only when you can see the Emitter itself, you'll be able to see it's particles. If you don't want this, set \_Seconds Before Inactive to 0.000000.

#### Relative Warmup Time/Warmup Ticks Per Second

You can make the engine precalculate the Emitter, so when you start the map it's as if the Particle Emitter has been there already for a few seconds and you will not see the warmup effect. The warmup is the time where not yet all the particles are spawned. With the setting *Relative Warmup Time* you can set how many seconds have to be precalculated, relative to the [Lifetime](#lifetime) of the particles. This means if you set it to 1, there are exactly as much precalculated seconds as the first particles will live. But before this works you also have to set the WarmupTicksPerSecond: this is how many ticks each second of the RelativeWarmupTime has. The higher the *Warmup Ticks Per Second*, the more there will be precalculated.In short, the longer the *Relative Warmup Time* of a certain Particle Emitter takes, the higher you have to make the *Warmup Ticks Per Second* setting (and set *Relative Warmup Time* to 1) if you want there to be no visible warmup.

### Movement

![movementcat.gif](../../assets/![movementcat.gif](../../assets/movementcat.gif))

#### Start Velocity

Use *Start Velocity* to give the particles a constant speed. The X, Y and Z values will adjust how fast the particles travel in that direction. If Min and Max are the same, you get what you would expect: the particle moves with the speed you entered to the direction you used. If Min < Max, the particle will move with a random, constant speed that is something between the Min and Max value. For example, if you set X-Min equal to X-Max and Y-Min equal to Y-Max and Z-Min equal to Z-Man (and make sure there is no acceleration), all the particles will move towards the same direction:

![velocity1.jpg](../../assets/![velocity1.jpg](../../assets/velocity1.jpg))

But if you set X-Min to -500 and X-Max to +500 (and keep the Y values), the particles will move with a random direction:

![velocity2.jpg](../../assets/![velocity2.jpg](../../assets/velocity2.jpg))

If you'd have made X-Min = -150 and X-Max = +150, there'd be less difference in the directions:

![velocity3.jpg](../../assets/![velocity3.jpg](../../assets/velocity3.jpg))

#### Acceleration

To make the particles moving, you can give them Velocity and/or Acceleration. The Acceleration makes them move faster and faster, and is very easy to set up: open the properties of the Emitter and in there open the properties of the *Sprite Emitter*. In there, expand Acceleration.There you can enter the amount of Acceleration you want along the X, Y and Z axis. You can enter negative values too. If you assume that the upper part of the Top View is the North, here's what the settings do:

![base.jpg](../../assets/![base.jpg](../../assets/base.jpg))

If X > 0, the particle will go to the East
If X < 0, it'll go to the West
If Y > 0, it'll go to the South
If Y < 0, it'll go to the North
If Z > 0, it'll go to the ceiling or sky
If Z < 0, it'll go to the ground
The total acceleration is the sum of these 3 components, so if X = 425, Y = -950 and Z = -950, the particles will go to the North-East and down, and will go to the North with more acceleration than to the East. However, if you rotated the Emitter actor with the Rotation tool, this won't be correct anymore, the CoordinateSystem will be rotated then. The X-axis will then be the direction of the arrow if you set bDirectional to True in advanced. Once you gave it some acceleration, you'll see the particles move.While *Acceleration* makes the particle move faster every second, the [Start Velocity](#start-velocity) is a constant speed. If no *Acceleration* is used, but there is a Velocity, the particle will move with the same speed as long as it lives. If you use Velocity AND *Acceleration* the total speed of the particle will be the sum of the constant Velocity and the variable speed caused by the Acceleration. If there is a Velocity and a Acceleration along the same axis, but they have opposite signs, the particle will first move in one direction, but at a certain point the absolute value of the speed caused but the Acceleration will be larger than the absolute value of the Velocity, so the particles will move back to the direction they came from. If you use a Velocity and an Acceleration, both along a different axis, the particles will make a parabola. A parabola is the realistic trajectory for example a bullet or an object you throw follow. For example if Acceleration has Z = -950, and *Start Velocity* has X-Min = 500 X-Max = 500, it'll look like this:

![parabola1.jpg](../../assets/![parabola1.jpg](../../assets/parabola1.jpg))

If you now set also the X of Acceleration to -1000, it'll do the following:

![parabola2.jpg](../../assets/![parabola2.jpg](../../assets/parabola2.jpg))

#### Max Velocity

The sum of the velocity caused by the [Acceleration](#acceleration) and the Velocity is the Absolute Velocity, and you can set a *Max Velocity* value for every axis. If you use this, the Acceleration will keep speeding up the particle until the *Max Velocity* speed is reached. The particle will then have a constant speed. If you change the first parabola example to have Z value of *Max Velocity* to 600, the function will look like a parabola in the beginning, but once the absolute value of the speed along the Z axis is 600, the function will become a constant function (a line).

![parabola3.jpg](../../assets/![parabola3.jpg](../../assets/parabola3.jpg))

#### Velocity Loss

The *Velocity Loss* setting hinders the particle from moving along any axis you chose (if you set X = Y = Z it will slow down particles the same no matter which way they are moving). It works sort of like friction or air resistance. If it's larger than 100, the particles suddenly get shot away at very high speed. Again, you can use a Min and Max value if you want the *Velocity Loss* to be something random between the Min and Max value.

#### Add Velocity From Other Emitter

*Add Velocity From Other Emitter* gives the particles the same Velocity as a random particle coming from another Particle Emitter inside the same Emitter actor. This setting works very similar to [[#AddLocationFromOtherEmitter][Add Location From Other Emitter] in [Location](#location).

#### Add Velocity Multiplier

If [Add Velocity From Other Emitter](#add-velocity-from-other-emitter) is not set to *None* then the particle's velocity will be multiplied by this value. For example, if you want the particles from this emitter to have twice the velocity of the particles from other emitter you could set all the values in this tool equal to 2.0.

#### Get Velocity Direction From

With *Get Velocity Direction From*, you can choose in what direction the Velocity is used. None is the default and works as explained above. With *Start Position And Owner*, the particles will go in the direction determinated by the start position of the particle, and the Emitter Actor, and it moves away from the Emitter. *Owner and Start Position* does the same, but now the particle will move from it's startposition towards the Emitter Actor and when it reached that keep going further. This only works if it's startposition is not the Emitter itself, more about this is in [Location](#location).
(coming soon)

#### Coordinate System

The CoordinateSystem determinates what the X, Y and Z values for the [Location](#location) of the particles mean. If you set the CoordinateSystem to PTCS\_Relative, the (X,Y,Z) = (0,0,0) position for the particles is the position of the Emitter actor in the editor, so the particles will get spawned there:

![coorrelative.jpg](../../assets/![coorrelative.jpg](../../assets/coorrelative.jpg))

But if you set the CoordinateSystem to PTCS\_Absolute, the CoordinateSystem of the world in the editor is used, and there the (0,0,0) [Location](#location) is the exact center of the world (there the lines of the grid are painted a little darker than the others in the 2D views). So the particles will start in the center of the map (where the thicker gridlines in the 2D view cut each other), no matter where the Emitter actor is: note the emitter actor on the right of the screenshot:

![coorabsolute.jpg](../../assets/![coorabsolute.jpg](../../assets/coorabsolute.jpg))

The default CoordinateSystem PTCS\_Independent does the same as PTCS\_Relative, but after they are spawned the particles become independent and use the absolute coordinatesystem. The difference between PTCS\_Relative and PTCS\_Independent becomes important when you use [Moving Emitters](#moveem).All the three CoordinateSystems will rotate if you rotate the Emitter actor with the Rotation Tool. If you set in the properties of the Emitter actor in Advanced bDirectional to True, an arrow will be displayed in the editor to help you to rotate it better.In the section [Location](#location) is explained how you can make the particles spawn at another [Location](#location), again relative or absolute to the Emitter actor depending on the CoordinateSystem you use.

#### Min Squared Velocity

This controls the minimum velocity a particle may have before it becomes inactive. This is important if you use [[#CollisioN][Collision]: the particles will then get less velocity every time they bounce on the wall.

#### Use Velocity Scale

![velocityscale.jpg](../../assets/![velocityscale.jpg](../../assets/velocityscale.jpg))

*UseVelocityScale* turns velocity scale on an off. Velocity scale is used to scale the velocity of the particle over time. Given that this is a component scale, velocity scale can be used to make the particles change direction over time and even reverse directions.

#### Velocity Scale

*Velocity Scale* allows you to scale the velocity of particles over the course of their lifetime. This can allow you to do things such as stop moving particles and then start them again. It can also allow you change the direction of particles by setting the X scale to 0.0 and the Y scale to 1.0 for one entry and then setting the X scale to 1.0 and the Y scale to 0.0 for another entry. *Relative Velocity* is a multiplier for the current velocity of the particle and *Relative Time* is the time at which that multiplier will be applied. As with all scales, the entries in *Velocity Scale* will be interpolated between.

#### Velocity Scale Repeats

*Velocity Scale Repeats* is the number of times the *Velocity Scale* will be additional repeated. Setting this to 0 will cause the velocity scale to happen just once. Setting this to 1 will cause the velocity scale to happen twice.

### Location

![locationcat.jpg](../../assets/![locationcat.jpg](../../assets/locationcat.jpg))

#### Start Location Shape

This will determine the overall shape that particle spawn in.Selecting *Box* uses the variables in ***Start Location*** to spawn all of the particles in the specified \_ Box\_. For example if you set X, Y and Z(Min) to -150 and X, Y and Z(Max) to +150, all the particles will start inside a 300\*300\*300 box.

![box.jpg](../../assets/![box.jpg](../../assets/box.jpg))

Selecting *Sphere* makes it possible spawn the particles inside of a sphere with a radius equal to the values inside of ***Sphere Radius***.

![sphere.jpg](../../assets/![sphere.jpg](../../assets/sphere.jpg))

*Polor* is rather complicated, but uses the X, Y, and Z varibles in ***Start Location Polar Range*** as theta, phi, and *r* repsectively in the standard polar equation. Basically, this makes a hollowed partial-sphere with radius *r*. It will sweep longitudally *theta* degrees and latitdually *phi* degrees.

#### Start Location Offset

The settings in [Start Location Shape](#start-location-shape) work in combination with *Location Offset*, so the final Start Location is the sum of those. This makes is possible for spawning area of particles to not be centered over the emitter.

#### Add Location From Other Emitter

In Add Location From Other Emitter you can select another Particle Emitter that is inside the same Emitter actor. If you set it to something other than *None*, the particles will not be spawned where they normally should spawn, but at the location of one of the particles of the selected particle emitter. They will not keep following that particle, they only get spawned there and get independent after that. You can for example make a trace of particles behind another moving particle. This is done in the DEMO-Particles example map:

![locationfromotheremitter.jpg](../../assets/![locationfromotheremitter.jpg](../../assets/locationfromotheremitter.jpg))

The blue sprites never move, but when they die they respawn at one of the bouncing balls, so together all the blue sprites form the shape of the traces the balls follow.

### Mesh Spawning

![meshspawning.gif](../../assets/![meshspawning.gif](../../assets/meshspawning.gif))

Mesh Spawning uses the vertices of a static mesh to calculate the spawn location and optionally the velocity and the color of the particles in this emitter. The static mesh does not have to exist in the world nor do the faces of the static mesh matter. This means that you can make arbitrary shapes for static meshes in a modeling program. You can also use existing static meshes in the world and attach effects to them to produce results like a bush on fire.

#### Mesh Spawning Type

| Mesh Spawning Type | Description |
| --- | --- |
| Do Not Use Mesh Spawning | Off. The mesh spawning is not used at all. |
| Linear | The particles will be spawned on each subsequent vertex based on numbering of the vertices. |
| Random | The particles will spawned on a random vertex. |

#### Static Mesh

This is the static to use for the mesh spawning. Select a mesh in the mesh browser and click "Use".

#### Mesh Scale

*Mesh Scale* is the scale of the *Static Mesh*. Given that this is a range, a random number in the range is chosen for every particles spawned.

#### Uniform Mesh Scale

This will cause only the X component to be used to uniformly scale the mesh. With will prevent stretching and squashing and just change the size of the static mesh.

#### Velocity From Mesh Normal

This will use the normal of each vertex to determine the initial velocity of each particle.

#### Velocity Scale

This scales the velocity from the mesh normal. For example if you have a mesh sphere with outward facing normals, you can set the *Velocity Scale* to negative values and the particles will move inwards towards the center of the sphere.

#### Uniform Velocity Scale

*Uniform Velocity Scale* will cause the only the X component of the *Velocity Scale* to be used to uniformly scale the velocity.

#### Spawn Only In Normal Direction

(Note: Do not use with *Respawn Dead Particles* = true!)This will only use the normals within *Normal Direction Threshold* of *Normal Direction* to spawn particles.

#### Normal Direction

This is the direction of the normals to use for spawning particles. This will only work is *Spawn Only In Normal Direction* is true.

#### Normal Direction Threshold

This is the threshold for the *Normal Direction*. This will only work is *Spawn Only In Normal Direction* is true.

#### Use Color From Mesh

This uses the color of the each vertex to determine the color the particle being spawned.

### Skeletal Mesh

![skelmesh1.gif](../../assets/![skelmesh1.gif](../../assets/skelmesh1.gif))

Skeletal Mesh animation allows you to attach particles to the bones of a skeletal mesh. The mesh is used to determine the spawn location of the particles and can also be used to determine the movement the particles. The main way to use this system is to attach effects to existing character models such as the dead greens DeRes effect in UT2003.

![skelmesh2.jpg](../../assets/![skelmesh2.jpg](../../assets/skelmesh2.jpg))

Another way to use skeletal mesh animation is to create a simple model that moves a bone in a pattern that you want an emitter to move in. This can be used to move emitters in more complex patterns than is otherwise possible with the PSE. The example below moves an emitter in a decreasing spiral that travels upwards.

![skelmesh3.jpg](../../assets/![skelmesh3.jpg](../../assets/skelmesh3.jpg))

Complex movement patterns can also be achieved by using [Anim Notifies](../Animation/AnimNotifies.md) to attach particles systems to bones. (See *AnimNotify\_Effect*).While it is possible to use skeletal mesh animation without any new code (the spiral example did not use any new code for example) the system works best when coupled with game specific code. This is mainly do to the fact that [SkeletalMeshActor](#skeletalmesh-actor) must be an *Actor* that exists in the level. This makes it impossible to preview this type of particle system in Unrealed because characters do not move around or animate in the editor. Below is an example of attaching the dead green DeRes effect in UT2003:

```

DeResFX = Spawn(class'DeResPart', self, , Location);
if ( DeResFX != None )
{
   DeResFX.Emitters[0].SkeletalMeshActor = self;
   DeResFX.SetBase(self);
}
```

If you do not want to use code you can create a *Pawn* (or a subclass of *Pawn* if you are not using the UDNBuild) and set it to draw with a particular skeletal mesh and then animate that mesh using a scripted sequence. You will also have to attach the particle system to the pawn using the *AttachTag* and *bHardAttach* = true, if you want the particle system to move with the pawn. Also, make sure you place the pawn and particle system at the same location in the level.

#### Use Skeletal Location As

*UseSkeletalLocationAs* is used to tell the particles of the emitter how to spawn and move relative to the bones of the mesh.

| UseSkeletalLocationAs | Description |
| --- | --- |
| Don't Use SkeletalMesh | Off. The skeletal mesh animation is not used at all. |
| Spawn at Vertex | The particles will spawn at bone locations but once the particle is spawned, it will not be effected by the mesh. The spiral example uses *Spawn at Vertex* which is why you see the trail in the path of the bone. |
| Move with Vertex | The particles will spawn at a bone location and will continue to be effected by the location of the bone but not the rotation. The spiral example from above would just look like a fat vertical white line moving around in a spiral. |

#### SkeletalMesh Actor

*SkeletalMesh Actor* is the *Actor* in the level whole skeletal mesh will be used to determine the spawning and motion of the particles in this emitter. In most cases this will be set in code. If you want to set this in the editor you will have type this in directly. First find the **Name** of the actor in the level by looking at the properties of this actor under **Object** or looking at the top of the properties window. In the *SkeletalMesh Actor* text window type the name of the actor.

#### Skeletal Scale

*Skeletal Scale* is used to set the scale of the "mesh" used to spawn the particles. The mesh of the actor that the emitter is attached to is not exactly the mesh used to spawn the particles. For example if the mesh is scaled in the animation browser, this skeletal mesh animation system will use the size before the scale. You can use *Skeletal Scale* to match the size of scaled meshes or you can use it to intentionally make the size larger or smaller.

#### RelativeBoneIndexRange

*RelativeBoneIndexRange* is used to determine which bones are used to for spawning particles. For all bones set this range from 0.0 to 1.0. If you only want some bones, set it to a sub range between 0 and 1. Which bones you get is dependent on how the bones are indexed in your model.

### Rotation

![rotationcat.jpg](../../assets/![rotationcat.jpg](../../assets/rotationcat.jpg))

#### Spin

To make the particles Spin while they move, check *Sping Particles and enter an X-Min and X-Max value at \_Spins Per Second*. The value you enter is the number of times per second the texture of the particle will spin. If X-Min and X-Max values are different, each particle will get a random value between Min and Max. You can also set to spin Counter Clock Wise or Clock Wise with the *Spin CCW or CW* slider. If you set it to something between 0 and 1, for example 0.7, there's 70% chance a particle will rotate Clock-Wise and 30% chance it'll rotate Counter-Clock-Wise. If SpinsPerSecondRange is 0.5 and SpinCCWorCW is 1, it'll look somewhat like the first animated gif. If you set *Spin CCW or CW* to 0.5, it'll do for example like on the second animated gif (on the second screenshot, some particles may suddenly switch from CCW to CW, but that's because otherwise the gif would require TOO many frames. This never happens in the editor.)

![spin1.gif](../../assets/![spin1.gif](../../assets/spin1.gif))

![spin2.gif](../../assets/![spin2.gif](../../assets/spin2.gif))

#### Start Spin

With *Start Spin*, you can set the rotation the particle has when it's spawned. You can also make the particle to have a random *Start Spin*, if you enter a different Min and Max value.

#### Facing Direction

![facingdir.jpg](../../assets/![facingdir.jpg](../../assets/facingdir.jpg))

Facing Direction determines how particles are oriented in the world. It is important to remember that this orientation is calculated BEFORE the spin of the particles is calculated. If there is any spin it will be applied after the facing direction making it difficult to see the effects of the facing direction. To illustrate the effect of this tool, I created a simple particle system effected by gravity. The texture on the particles is this arrow.

![facingdirtex.jpg](../../assets/![facingdirtex.jpg](../../assets/facingdirtex.jpg))

**Facing Camera** is the default and most common choice for facing direction. All the particles are billboarded facing the camera no matter where the camera is. This can be seen in the image below. The one confusing part about *Facing Camera* is that it flips the texture vertically. Another confusing aspect of this settings is that the size of particles has a constant aspect ratio because X size (from [Start Size](#start-size)) is used to scale both X and Y. Y size is ignored when facing direction is set to *Facing Camera*.

![facingdir1a.jpg](../../assets/![facingdir1a.jpg](../../assets/facingdir1a.jpg))

![facingdir1b.jpg](../../assets/![facingdir1b.jpg](../../assets/facingdir1b.jpg))**Along Movement Facing Camera** is fairly straightforward. The particles orient themselves so that the "up" of the texture is always facing the direction the particle is moving. The particle tries its best to also face the camera at the same time but it is hard at certain angles like looking along the direction the particle is moving. These two images illustrate the effect of this setting.

![facingdir2a.jpg](../../assets/![facingdir2a.jpg](../../assets/facingdir2a.jpg))

![facingdir2b.jpg](../../assets/![facingdir2b.jpg](../../assets/facingdir2b.jpg))**Specified Normal** is very simple; the particle normal is specified by [Projection Normal](#projection-normal). In the case of the first image the normal is straight up (0, 0, 1). The second image has a normal of (-0.5, 0.3, 1.0).

![facingdir3.jpg](../../assets/![facingdir3.jpg](../../assets/facingdir3.jpg))

![facingdir3b.jpg](../../assets/![facingdir3b.jpg](../../assets/facingdir3b.jpg))**Along Movement Facing Normal** is like *Along Movement Facing Camera* but instead of facing the camera, the particles faces the specified [Projection Normal](#projection-normal). This is very useful for things like waterfalls where the particles should orient with its movement but not face the camera. The effects can be seen below.

![facingdir4a.jpg](../../assets/![facingdir4a.jpg](../../assets/facingdir4a.jpg))

![facingdir4b.jpg](../../assets/![facingdir4b.jpg](../../assets/facingdir4b.jpg))**Perpendicular to Movement** orients the particles perpendicular to the movement direction. This has the unfortunate side effect that in some cases it rotates the particles 90 degrees mid flight. This can be seen in the image below.

![facingdir5.jpg](../../assets/![facingdir5.jpg](../../assets/facingdir5.jpg))

#### Projection Normal

This tool is enabled and used for the *Specified Normal* and *Along Movement Facing Normal* settings of [Facing Direction](#facing-direction).

#### Use Rotation From:

You can also rotate the entire particle system for the particles using *Use Rotation From* . This affects the location and velocity, but not the acceleration. With *Use Rotation From, you can set how to rotate it. If it's \_None*, the particle system is not rotated, cause the X-Axis, for example, to face the same direction as the main X-Axis in the editor.If *Use Rotation From* is set to *Actor*, the rotation of the Emitter Actor is used. If you set in Advanced bDirectional=True, the Emitter gets an arrow. The direction of that arrow is the X-Axis that now will be used for velocity and location.If *Use Rotation From* is set to *Offset*, the settings in *Rotation Offset* are used. There you can set how much the particle system has to Pitch, Yaw and Roll.If *Use Rotation From* is set to *Normal*, the settings in *Rotation Normal* are used for the rotation. Now, you can enter the direction of a plane, and the X-Axis will be perpendicular on that plane.For example on the first screenshot there is no *Rotation Offset* used, and the particles are moving with a Velocity of X = 500. On the second screenshot, they still have the same Velocity, but *Use Rotation From* is set to *Offset* and the *Pitch+ of \_Rotation Offset* is set to 90.

![rotation1.jpg](../../assets/![rotation1.jpg](../../assets/rotation1.jpg))

![rotation2.jpg](../../assets/![rotation2.jpg](../../assets/rotation2.jpg))

### Revolution

![revolution.jpg](../../assets/![revolution.jpg](../../assets/revolution.jpg))

While [Rotation](#rotation) is for rotating individual particles about their center, Revolution is for rotation particles about a fixed point in space. Using Revolution will cause the particles to change position.

#### Use Revolution

Checking *Use Revolution* will enable the use or revoltion.

#### Revolution Center Offset

In general particles will revolve about the center of the particle system. *Revolution Center Offset* will allow you to change this so that particles rotate about a point other than the center of the particle system.

#### Revolutions Per Second

*Revolutions Per Second* specifies the number of revolutions per second around the specified axes.

#### Use Revolution Scale

If *Use Revolution Scale* is true, the *Revolution Scale* will be used.

#### Revolution Scale

This *Revolution Scale* is used as a multiplier for each of the axes of *Revolutions Per Second* range. Using *Revolution Scale* you increase or decrease the speed of revolution of particular axes over the lifetime of the particle. You can even reverse the direction of revolution by using negative numbers.

#### Revolution Scale Repeats

*Revolution Scale Repeats* is the number of times the *Revolution Scale* will be additional repeated. Setting this to 0 will cause the revolution scale to happen just once. Setting this to 1 will cause the revolution scale to happen twice.

### Size

![sizecat.jpg](../../assets/![sizecat.jpg](../../assets/sizecat.jpg))

#### Uniform Size

If Uniform Size is set to True, only the X is used for both U and V (or X, Y and Z for meshes). You may need this if you use a random Size if you want to preserve the aspect ratio.

#### Start Size

The *Start Size Range* determinates the Size the particles will get when spawned. For Sprites, only the X values are useful if [Facing Direction](#facing-direction) is **Facing Camera**. For all other settings of **Facing Direction** the X and Y can be used to change the width and height of the texture separately (but only if [UniformSize](#uniform-size)  is false). For Meshes, X, Y, and Z are used (but only if [UniformSize](#uniform-size)  is false). The default value is 100, the screenshots show X(Min) = X(Max) = 50, and X(Min) = X(Max) = 150.

![size1.jpg](../../assets/![size1.jpg](../../assets/size1.jpg))

![size2.jpg](../../assets/![size2.jpg](../../assets/size2.jpg))If you enter a different X(Min) and X(Max) value, the particles will get a random Size.

![size3.jpg](../../assets/![size3.jpg](../../assets/size3.jpg))

#### Size Scale

The *Size Scale* works exactly the same as the [Color Scale](#color-scale), only now you're working with a Size instead of a color. If you set *Use Size Scale* to True AND *Shrink Particles Exponentially* to True, the Particles will always shrink, and you don't have to add any SizeScales.

![size4.jpg](../../assets/![size4.jpg](../../assets/size4.jpg))

### Collision

![collisioncat.gif](../../assets/![collisioncat.gif](../../assets/collisioncat.gif))

#### Use Actor Forces

Enabling *Use Actor Forces* lets actors with their force parameters set influence particles. *(Any sort of actor works but pawns are the easiest because they already have their collision properties set just right.)* The force parameters can be found by double clicking on the actor and selecting the **Force** category in the *Properties* window. *ForceType* must be set to **FT\_DragAlong** and *ForceScale* must be greater than 0. To see a large effect set *ForceScale* > 50. *ForceRadius* can be set to anything but it might work well to set it to the *CollisionRadius* of the actor. Now with these parameters set, when this actor moves into the particles of this system, the actor will knock them radially away from the itself in the direction of movement. However, when the actor is stopped near the particles and the particles are moving, the particles will move towards the actor and circle around it. While this effect looks good, it is can be ***VERY*** slow. Sometimes it will run OK and then if the pawn moves just a little, or the view changes, the game might pause for several seconds while it recalculates the motion of all the particles.

#### Use Collision

  
 NOTE: Collision will not work if your coordinate system is set to "Relative" in the default code base.The Collision can make the particles realistically bounce on walls, floors or ceilings. It looks for example like the animated gif:

![collision.gif](../../assets/![collision.gif](../../assets/collision.gif))

If you have no Collision, the particles will just disappear in the wall:

![collision0.jpg](../../assets/![collision0.jpg](../../assets/collision0.jpg))

But if you set UseCollision to True, the particles will bounce on the wall. If they hit the wall perpendicularly, they will bounce back to from where they came as on the first screenshot, in any other case they'll bounce like on the second screenshot.

![collision1.jpg](../../assets/![collision1.jpg](../../assets/collision1.jpg))

![collision2.jpg](../../assets/![collision2.jpg](../../assets/collision2.jpg))

#### Damping Factor

The DampingFactor changes the velocity of the Particle every time it bounces on the wall. The Velocity gets multiplied by this factor. For example in the real world if you let a tennis-ball fall on the ground, it bounces less high every time it hits the ground again. On the following screenshots, there is an acceleration Z = -950, and a velocity of X = 500. The Particles are falling towards the ground, and then bounce. On every screenshot, the Z value of the DampingFactor is modified to show the difference. It's the Z value that's used, because in this case the particles are bouncing on the floor. If the DampingFactor is 1 they can keep and keep bouncing as long as they live, as shown on the first screenshot. If you make it lower than 1, for example 0.9, they'll bounce less high every time they hit the ground (this is most realistic).

![collision3.jpg](../../assets/![collision3.jpg](../../assets/collision3.jpg))

![collision4.jpg](../../assets/![collision4.jpg](../../assets/collision4.jpg))If you make the DampingFactor higher than 1, for example 1.5, the particles will bounce higher and higher (1st screenshot). If you give a different Min and Max value, every particle will bounce randomly something between the Min and Max value (2nd screenshot).

![collision5.jpg](../../assets/![collision5.jpg](../../assets/collision5.jpg))

![collision6.jpg](../../assets/![collision6.jpg](../../assets/collision6.jpg))

#### Rotation Damping Factor

To use rotation damping factor you first have to check *Use Rotation Damping*. With *Rotation Damping Factor*, you can set the damping factor for the spinning particles, this works the same way as the [Damping Factor](#damping-factor) of Collision, only it makes the particles spin slower or faster every time they bounce. For example if you make the Z-Min and Z-Max values of the *Rotation Damping Factor* 0, the spin will stop after the first bounce on the floor already because the *Spins Per Second* gets multiplied by 0. Note on the screenshot all the textures to have the same Rotation after the bounce:

![spin3.jpg](../../assets/![spin3.jpg](../../assets/spin3.jpg))

#### Extent Multiplier

The *Extent Multiplier* is multiplied by the [Size](#size) of the particle, and this is used for the collision detection. This multiplied [Size](#size) determinates where the colliding sides of the particles are, and as soon as that (invisible) side reached the surface, the particle will bounce. 0 represents the middle of the particle and 1 represents the normal size of the particle. For numbers larger than 1, the particle will bounce even sooner. This is useful because when particles are rotated the corners might hit the wall when *Extent Multiplier* is 1.

#### Collision Planes

If you set *Use Collision Planes* to True, you can make invisible planes, where the particles will bounce on. The planed don't collide anything else, only the particles of that particular emitter. These planes are 1-sided which means the particle can go through it at one side but will bounce against it if it goes the other direction. You have to make the planes in the *Collision Planes* setting. For each plane, you can enter W, X, Y and Z. W is the distance from the plane to the center of the editor grid, and X, Y and Z determinate the normal of theplane and the that direction W moves the plane. You can also enter negative values, for example to get on the other side of the grid or to turn around the 1-sided direction. On the screenshots, the red dot represents the center of the editor grid, the grid itself is 256 units, and the red line shows the (invisible) plane. The small red triangles point into the direction the particles can go through the plane. On the first screenshot, W=256, X=0, Y=1 and Z=0. The particles can go to the south until they bounce against the wall, and when going north again, they'll bounce against the plane. On the second screenshot, W is changed to -256 and Y to -1, so the direction turns around, and the particles will bounce against the other side of the plane instead.

![plane256_0_1_0.jpg](../../assets/![plane256_0_1_0.jpg](../../assets/plane256_0_1_0.jpg))

![plane256_0_-1_0.jpg](../../assets/![plane256_0_-1_0.jpg](../../assets/plane256_0_-1_0.jpg))

#### Max Collisions

If you set *Use Max Collisions* to True, the particle will die when it bounced the (random) number of times you enter in *MaxCollosions*, no matter what the [lifeTime](#lifetime) is.

#### Spawn From Other Emitter

With SpawnFromOtherEmitter, you can make something to get spawned at the location where the particle bounces, for example sparks leaving a glowing mark where they hit, or rippels in shallow water. For this to work, you have to make a second emitter inside of the same emitter actor, and select that emitter is *Spawn From Other Emitter*. The particles of this new emitter are the ones that will be spawned at the location of bouncing particle when it bounces (this is subtly different from the location of the bounce particularly if you have a large [Extent Multiplier](#extent-multiplier)). For the new emitter, set [Respawn Dead Particles](#respawn-dead-particles) and [Automatic Spawning](#automatic-spawning) to False. The reason for this is, otherwise these particles may also get spawned at the wrong moment at the location of the particle system in the world.Then, in *Spawn Amount Range*, enter the number of particles you want to get spawned when the bouncing particle hits the surface. This must be at least 1 for the anything to happen.

#### Spawned Velocity Scale

If you check *Use Spawned Velocity Scale*, you can also give the particles that get spawned when it bounces a velocity. You can set this Velocity in the *Spawned Velocity Scale* settings: you can give Minimum and Maximup X, Y and Z settings. If the particle bounces, the spawned particles only get the velocity in the normal direction on the surface. The best way to use this to give the mins and maxs of X, Y, and Z all the same positive value so that the they will travel in the direction of the normal (If you give X, Y, and Z negative values the spawned particles will more towards the surface they bounced off).Spawned Velocity Scale can be used very well with [Facing Direction](#facing-direction). If you set *Facing Direction* to 'Perpendicular To Movement' and set the spawned velocity to a very small value (like 1.0) the secondary particles will be aligned with the surface they bounced off. This works very well for impact marks.

### Sounds

![sounds.gif](../../assets/![sounds.gif](../../assets/sounds.gif))

Sounds can be played when particles are spawned and also when they collide with the world.

#### Spawning Sound

Spawning sounds can be enabled by setting the *Spawning Sound* pull down to anything other than **Don't Use Spawning Sounds**. The other options for *Spawning Sound* are as follows:

* **Linear Global / Linear Local** - These both play though the sounds in a linear order when particles are spawned. Every time a particle is spawned, the next sound in the *Sound Array* in the range specified by *Spawning Sound Index* is played.
* **Random** - plays a random sound in the *Sound Array* in the range specified by *Spawning Sound Index*.

#### Spawning Sound Index

*Spawning Sound Index* selects the range for which sounds will play. When you specify a sound range using *Spawning Sound Index*, the *Min* and *Max* must be different numbers. If they are the same, Min=0 and Max=0 for example, all the sounds in *Sound Array* will be used.

#### Spawning Sound Probability

*Spawning Sound Probability* is a range for the probability that a sound will play on spawning. One might wonder, "Why a range when this is already a probability?" I wonder the same thing.

#### Collision Sound

Collision sounds can be enabled by setting the *Collision Sound* pull down to anything other than **Don't Use Collision Sounds**. The other options for *Collision Sound* are as follows:

* **Linear Global** - plays the sounds in the *Sound Array* in order, in a loop without, regard to the particle's lifetime. This loop is per particle and so if a burst of particles is spawned at the same time, and this burst hits a wall, all the particles will play the same collision sound.
* **Linear Local** - is like *Linear Global* except that the loop for each particles is reset at the end of it's lifetime. This mean that if the *Sound Array* contains the sounds "Boing!", "Bop!", and "Thud!", in that order, particles will always start with "Boing!". If a particle only collided with the world twice, the first time it collides in its next life, it will not go "Thud!", as it would in the case of *Linear Global*.
* **Random** - plays a random sound in the *Sound Array*.

#### Collision Sound Index

*Collision Sound Index* selects the range for which sounds will play. When you specify a sound range using *Collision Sound Index*, the *Min* and *Max* must be different numbers. If they are the same, Min=0 and Max=0 for example, all the sounds in *Sound Array* will be used.

#### Collision Sound Probability

*Collision Sound Probability* is a range for the probability that a sound will play on collision. One might wonder, "Why a range when this is already a probability?" I wonder the same thing.

#### Sound Array

*Sound Array* is an array of sounds that contain *Sound*, *Radius*, *Pitch*, *Volume*, and *Probability*.

* To set the *Sound*, select a sound in the Sounds browser and click **Use**.
* The *Radius* is in stand unit for sound radii which is something other than Unreal units. 64 seems to be a good value.
* For *Pitch*, 1.0 is the default pitch.
* The *Volume* setting only accepts values between 0.0 and 1.0. 1.0 is the standard volume and it can only be made more quiet.
* *Probability* is the chance that this sound will play if it is told to play. The sound will be told to play based on [Spawning Sound Probability](#spawning-sound-probability) or [Collision Sound Probability](#collision-sound-probability).

### Mesh

![meshcat.jpg](../../assets/![meshcat.jpg](../../assets/meshcat.jpg))

#### Mesh

This is very similar to the [Texture](#texture) field. In the Static Mesh browser select the mesh you want to use for this mesh emitter and click **Use**.

#### Use Mesh Blend Mode

If this is true, the blend mode of the mesh is used. This means that the particles will look just like they do when you drop them in the level. If this is false, the particles will use the blend mode defined in the [Texture](#texture) category.

#### Render Two Sided

If this set, the mesh will render all triangles two sided. This is usefull only if [UseMeshBlendMode](#use-mesh-blend-mode) is false.

#### Use Particle Color

If this is set, the mesh will use the settings in Color/Fading?. This is only usefull if [UseMeshBlendMode](#use-mesh-blend-mode) is true.

### Spark

![sparkcat.jpg](../../assets/![sparkcat.jpg](../../assets/sparkcat.jpg))

This ParticleEmitter generates sparks, for example the kind of sparks you see when someone's welding. This emitter turns it's Texture into one thin line with the colors of the texture. Settings such as [Acceleration](#acceleration), [Start Velocity](#start-velocity), and [Start Location](#startlocation) still work on it, but [Collision](#collision), [Rotation](#rotation), [Size](#size), etc... don't work on it because the particles are just lines. [Texture](#texture) still works to color the particle but because it is just a line the entire texture can not be seen. Things such as the [Color Scale](#color-scale) and [Fading](#fading) work, but these work per segment so you might not get the look you expected. On the screenshot: a random [Start Location](#startlocation) and a subtle red [Color Scale](#color-scale) on a white texture.

![spark10.jpg](../../assets/![spark10.jpg](../../assets/spark10.jpg))

To get a working Spark Emitter, add one the same way you'd add a Sprite or Mesh Emitter, and first give the it Velocity or Acceleration and then go to it's Spark properties. There set the Min and Max value of [Time Between Segments](#time-between-segments) to 1, you'll see the emitter working already.

![spark1.jpg](../../assets/![spark1.jpg](../../assets/spark1.jpg))

#### Line Segment Range

*Line Segments Range* this determinates how long the sections of the lines of the sparks will be, and also how visible they are. You can also make the length to be random if you enter a different Min and Max value. If you make this setting too high or too low (depending on other settings), the Spark Emitter will not work. The first screenshot has Min = Max = 5, the second screen has Min = Max = 3. A setting of 5 most of the times works the best.

![spark1.jpg](../../assets/![spark1.jpg](../../assets/spark1.jpg))

![spark2.jpg](../../assets/![spark2.jpg](../../assets/spark2.jpg))

#### Time Before Visible

*Time Before Visible Range* doesn't seem to do too much.

#### Time Between Segments

The effect of *Time Between Segments* is best visible if you let the line to be curved, when you use some acceleration. *Time Between Segments Range* determinates in how many segments the line should be divided. If this settings is low, for example 0.1, the line will be divided into a lot of segments so the curve looks smooth (first screenshot). If it's high (for example 0.5), you'll see the line broken into segments. (second screenshot). A higher *Time Between Segments* means less particles and thus better performance, but it doesn't look as good.

![spark3.jpg](../../assets/![spark3.jpg](../../assets/spark3.jpg))

![spark4.jpg](../../assets/![spark4.jpg](../../assets/spark4.jpg))For low *Time Between Segments* settings, there will have to be more particles created (every segment of the line is a particle), so you might have to set [Max Particles](#maxparticles) and to something higher before it looks good. A very high [Max Particles](#maxparticles) might create something like this (again with low and high *Time Between Segments*)

![spark5.jpg](../../assets/![spark5.jpg](../../assets/spark5.jpg))

![spark6.jpg](../../assets/![spark6.jpg](../../assets/spark6.jpg))

### Beam

![beamcat.jpg](../../assets/![beamcat.jpg](../../assets/beamcat.jpg))

Beam Emitters are very useful to create lightning and other such things. The emitter stretches the chosen Texture into a beam with [High Frequency Points](#highfrequencypoints) and [Low Frequency Points](#lowfrequencypoints). There must be at least two of each to make the lightning work. Each particle will be such a beam, and once created a particle never moves. The way to get the lightning moving is to create a new beam all the time while the old one gets destroyed, or to make the lightning flash with a Color Scale. Normally, the beam is only one angular line, but you can also give it branches.Getting started: Given a new beam emitter, leave all the settings at default, and add some Velocity and you will start to see something. The length of the beams depends on the magnitude of the Velocity and the Lifetime.

![beam1.jpg](../../assets/![beam1.jpg](../../assets/beam1.jpg))

You may recognize the 5 colored dot texture on this beam. If you want, you can change it in something better in [Texture](#texture). In the following examples a square, white texture is used. To make the lightning look much better, use a better texture for it. The texture for the lightning should be rotated 90�, like this:

![lightning8.jpg](../../assets/![lightning8.jpg](../../assets/lightning8.jpg))

For beams, some basic settings can be used in interesting new ways. [Location](#location) can to used to make it seem as if lightning is coming from different places. With [Start Location Range](#startlocationrange), you can make random start points for the lightning by entering a different value in Min and Max for the X and Y (the Z is not interesting for lightnings, because most of the times lightnings start at the same height).

![lightning7.gif](../../assets/![lightning7.gif](../../assets/lightning7.gif))

The best way to make the lightning to flash realistically is to use a [[#ColorScale][color scale]. This will make the whole beam change it's color during it's LifeTime. On the animated screenshot, there are 2 [[#ColorScale][color scales]: orange and yellow and the [lifetime](#lifetime) of the particles is 0.6 seconds. You can also use [Fade In](#fadein) and [Fade Out](#fadeout) to make a flashing effect.

![lightning14.gif](../../assets/![lightning14.gif](../../assets/lightning14.gif))

#### Number of Beam Planes

This option determinates how many planes the Beam is made of. 0 and 1 mean the same: only one sheet. The screenshots show 0, 3 and 10.

![sheet0.jpg](../../assets/![sheet0.jpg](../../assets/sheet0.jpg))

![sheet3.jpg](../../assets/![sheet3.jpg](../../assets/sheet3.jpg))

![sheet10.jpg](../../assets/![sheet10.jpg](../../assets/sheet10.jpg))

#### Beam Texture Scale

By default, the texture is repeated only once for the Beam. In Beam, with BeamTextureUScale you can set how many times to repeat the texture in the length of the Beam, and with BeamTextureVScale how many times to repeat it in the width: it's repeated 4 times on the screenshots.

![lightning12.jpg](../../assets/![lightning12.jpg](../../assets/lightning12.jpg))

![lightning13.jpg](../../assets/![lightning13.jpg](../../assets/lightning13.jpg))

#### Determine End Point By

![determineendpointby.jpg](../../assets/![determineendpointby.jpg](../../assets/determineendpointby.jpg))

This property sets what determines the EndPoint of the beam. The StartPoint is determined by the location of the Emitter actor and the settings in [Location](#location). There's more about StartPoints for beams [later](#huh).*Velocity* is the default setting. With this selected the end point is determinated by the [Velocity](#movement) of the particle and the [Lifetime](#time). The length of the beam is then determinated by the StartVelocityRange values and the [Lifetime](#time) of the particles. The direction of it is determinated by the X, Y and Z values of the StartVelocityRange. You can again use random values, so for example if X(Max) = Y(Max) = Z(Max) = +1000 and X(Min) = Y(Min) = Z(Min) = -1000, each Beam will be anything random between this. It'll do almost exactly the same as on this animated gif below. You'll be able to see more than one Beam now, because MaxParticles is set to 10 by default. Also, lightnings normally only goes straight towards the ground, so only using negative Z values for StartVelocityRange is useful.

![lightning1.gif](../../assets/![lightning1.gif](../../assets/lightning1.gif))

*Distance* does the same as *Velocity*, but the StartVelocityRange only determines the direction of the beam. The length is set with [Beam Distance](#beamdistance), in editor units.*Offset* allows you to determinate the EndPoint in relative coordinates. You have to enter these coordinates in Offset, inside BeamEndPoints[0]. To get this, first expand
[Beam End Points](#beam-end-points) and press the Insert button.

![beamendpoints.jpg](../../assets/![beamendpoints.jpg](../../assets/beamendpoints.jpg))

In Offset, enter the X, Y and Z coordinate range for the EndPoint of the Beam. The coordinates are relative to the StartPoint (most of the times this is the Emitter actor), so for example X = 0, Y = 0, Z = -1000 means the EndPoint will be 1000 units below the StartPoint. Before it works, you also have to set Weight to something larger than 0. You can again use different Min and Max values if you want a random Location for the EndPoint. You can add more *Beam End Points*, and then the Beam will use one of these *Beam End Points* by random. With Weight, you can set the importance of each *Beam End Point*, this is the probability that it'll be used. If you give all the *Beam End Points* a Weight of 1, the chances will be equally divided. If for the Offset X = Y = Z = 0, the EndPoint and the StartPoint the same, so there won't be a Beam. You can use this if you want the lightning to strike only a few times and to be invisible for the rest of the time. Then you can give the *Beam End Point* with this 0-Offset a high Weight, so the lightning is most of the times invisible.*TraceOffset* does the same as *Offset*, but if there is a solid surface in the way the lightning will hit against it, instead of going to the actual end point. *TraceOffset* does not work well in combination with the relative coordinate systems.*OffsetAsAbsolute* does the same thing as *Offset* but interprets the offset range as world coordinates instead of relative coordinates. So if X = Y = Z = 0, the beam end point would be at the origin.*Actor* lets you make the beam go to a certain actor. This also uses [[#BeamEndPoints][Beam End Points], but this time, you have to fill in the Actor Tag property (and not the Offset property). The lightning will go towards the actor you gave that Tag (in the Event properties of that actor). If you want the lightning to go randomly towards different actors, you have to add more *Beam End Points*, and in each *Beam End Points* enter a different Actor Tag. Of course also give the actors these Tags. If you'd give three trees the SAME tag and use only the first *Beam End Point*, it won't work, the lightning will go to only one of the trees then. Again you have to give each of the *Beam End Points* a Weight higher than 0, that is the chance this *Beam End Point* will be used.For example if there are three trees, with Tags FullTree, FullTree2 and FullTree3, and you want the lightning to strike each of the trees randomly, but to strike FullTree3 twice as much as the other trees, give the following properties to the emitter:

![beamendpoints2.jpg](../../assets/![beamendpoints2.jpg](../../assets/beamendpoints2.jpg))

![lightning2.gif](../../assets/![lightning2.gif](../../assets/lightning2.gif))If the actor is moving, the Beam will follow it:

![lightning4.jpg](../../assets/![lightning4.jpg](../../assets/lightning4.jpg))

#### Beam Distance Range

This determines the length of the beam when [Determine End Point By](#determine-end-point-by) is set to *Velocity*.

#### Beam End Points

This determines the various end points of the beam when [Determine End Point By](#determine-end-point-by) is set to *Offset*, *Actor*, and *TraceOffset*.

#### Trigger Actor End Point

If *Trigger Actor End Point* is true, the beam will trigger the actor it draws to. This only works if [Determine End Point By](#determine-end-point-by) is set to *Actor* and there are valid actor tags in the the [Beam End Points](#beam-end-points) array. For example, this can be used to spawn impact effects for lighting at the strike point.

### Beam Noise

![beamnoisecat.gif](../../assets/![beamnoisecat.gif](../../assets/beamnoisecat.gif))

Here you can give the beam noise. You can give *High Frequency Points* and *Low Frequency Points*. Both do exactly the same, but you can use them independent for example to give the lightning a lot of small bends inside a few large bends. There must be at least 2 *High Frequency Points* (and 2 *Low Frequency Points*), these represent the start point and end point. If you set it to 0, the editor crashes. If you set it to 1, there will be no beam. If it's 2, the beam will always be straight. If *High Frequency Points* is 3 (and *Low Frequency Points* is 2), there will be 1 bend in the half of the beam. The higher the value, the more bends. You can determinate the size of the bend with *High or Low Frequency Noise Range* by entering Min and Max values for X, Y and Z there. This way you can set the direction of the bend, the size of it, and you can make it to be random. Actually, you have to make it random, otherwise it'll not work the way you want. For example if *High Frequency Noise Range* has Y(Max) = 1000 and Y(Min) = -1000 and there are 4 *High Frequency Points*, it'll look like the screenshot. 1 particle will not change during it's lifetime, so to get the lightning moving make sure the [lifetime](#time) is short enough for new particles to get spawned fast enough.

![lightning5.gif](../../assets/![lightning5.gif](../../assets/lightning5.gif))

You can also make a *High Frequency Scale*. This is similar to the [Color Scale](#color-scale), [Size Scale](#size-scale), etc..., only the *High Frequency Scale* determinates the [High Frequency Noise Range](#highfrequencynoiserange) on the different places of the beam. You can see the effect of the *High Frequency Scale* best on beams with a lot of *High Frequency Points*, so set it to for example 100. Without the *High Frequency Scale*, the whole beam has the same *Noise Range* everywhere:

![noise.jpg](../../assets/![noise.jpg](../../assets/noise.jpg))

To enable the *High Frequency Scale*, first set *Use High Frequency Scale* to True, and then add a *High Frequency Scale*, the same way as you added [Color Scale](#color-scale): expand the *High Frequency Scale Factors* and press the Insert button until you have enough scale factors. The frequency scale multiplies the *High Frequency Noise Range* (X, Y and Z separately), and *Relative Length* determinates the location on the beam where you want this multiplier to happen. 100% represents the length of the whole beam. If you set *Relative Length* of the first *High Frequency Scale Factor* to 70%, the first 70% of the Beam will have the scale of that *High Frequency Scale Factor*, and if you then set the *Relative Lentgh* of next *High Frequency Scale Factor* to 100%, the remaining 30% will get multiplied by the this *Frequency Scale*. On the screenshot the first *Frequency Scale* is 1 for X, Y and Z, and the second *Frequency Scale* is 10 for X, Y and Z.

![freqscale.jpg](../../assets/![freqscale.jpg](../../assets/freqscale.jpg))

![freqscale2.jpg](../../assets/![freqscale2.jpg](../../assets/freqscale2.jpg))You can use *High Frequency Scale Repeats* to repeat the scale 1 or more times, just the same way as for the [Color Scale](#color-scale) and the other scales. For example it looks like this if *High Frequency Scale Repeats* = 2.

![freqscale3.jpg](../../assets/![freqscale3.jpg](../../assets/freqscale3.jpg))

The *Low Frequency* settings do exactly the same as the *High Frequency* settings. Low frequency and high frequency work independently from each other, and can be used "through" each other. For example, you can use a lot of small [High Frequency Points](#highfrequencypoints), and a few, very large, [Low Frequency Points](#lowfrequencypoints). Then the beam will have a few large bends, and a lot of small bends at the same time, as shown on the screenshot:

![lightning6.jpg](../../assets/![lightning6.jpg](../../assets/lightning6.jpg))

*NoiseDeterminesEndPoint* allows the noise applied to the beam to also affect its endpoint, which in most cases, it already does. Sometimes, however, the location of the endpoint is locked-- if the DetermineEndPointBy setting is PTEP\_Actor, for example. In this case the endpoint will be set to the center point of the specified actor. However, this might not be the desired effect. It might look odd to see lightning strike the exact same place repeatedly. Checking this box will allow the beam to strike the desired actor but in a more random fashion. If the beam were striking a triggerable actor, allowing the noise to determine the endpoint will not stop the actor from triggering, even if the beam does not visually strike that actor. Note that this might result in visual glitches if the amount of noise is great. For example, let's say your beam is supposed to strike a tree and set off a fire particle system. However, it will look strange if a lightning bolt strikes the ground and tree 40 feet away from the impact bursts into flame. Reducing the amount of noise on the beam would fix this problem.Dynamic High Frequency Noise is used to make the beam actually move over the course of its lifetime. The feature uses the *High Frequency Points* described above. The only drawback of dynamic noise is that it only works on the first beam in a beam emitter. If you have more than one beam, the dynamic noise will not apply to the additional beams. The movement of the high frequency points is calculated on a time interval determined by *Dynamic Noise Points Update Time*. If you want the beam to updates continuously set *Dynamic Noise Points Update Time* to 0 or some very small number. Each timestep the high frequency points between the min and max of *Dynamic High Frequency Noise Points* will be skewed by a random amount based on *Dynamic High Frequency Noise*. The high frequency points start at index 0 at the start of the beam and end at 1 less than the total number of points. If the beam has 20 high frequency points and *Dynamic High Frequency Noise Points* is set from 0 to 10, only have the beam will move dynamically.

### Beam Branching

![beambranching.gif](../../assets/![beambranching.gif](../../assets/beambranching.gif))

To make good looking lightning effects, you can give beams branches. If this is used correctly, you can get a very cool and realistic lightning. It works like this: you have to create more than one [BeamEmitter](#beamemitter) (inside the same Emitter). Then you can tell the first [BeamEmitter](#beamemitter) to use the second [BeamEmitter](#beamemitter) for the branches. Then again, you can tell the second [BeamEmitter](#beamemitter) to use a third one for sub-branches, and so on. The *Max Particles* setting is also the maximum number of branches.First add multiple beam emitters and give each Emitter the properties you want. Make the first one big, and set it's *Max Particles* to 1. Make the second and third one smaller; they're for the branches. Give them many more *Max Particles*, for example 10 or 25. Also, set[RespawnDeadParticles](#respawn-dead-particles) to False for all branches, and set [AutomaticInitialSpawning](#automaticinitialspawning) to False, otherwise the branches might get spawned at the start point of the emitter itself instead of the new start point they get when they become branch. Also, make sure the beam emitters that will get branches, have a lot of [Beam Noise](#beam-noise). The branches will appear in the bends only, so if there aren't enough [High Frequency Points](#highfrequencypoints), there will not be a place for all the branches! You can of course make the noise very subtle, so you won't notice it, only the number of [High Frequency Points](#highfrequencypoints) is important; the more the better.

#### Use Branching, Branch Emitter

Then go to the *Beam Branching* properties of the first beam emitter. Set *Use Branching* to True, and set *Branch Emitter* to one of the first other beam emitter. Now the beam emitter you selected will be used for the branches.

#### Branch Probabilty

With *BranchProbability*, you can set the chance of branches to appear. If you set both Min and Max to 1, all the branches will be there (this is, the number of branches that you set in *Max Particles*). If you set Min and Max to 1, the branches may appear only at the top of the main beam depending on the number of beams on the branching emitter. This is because each chance the beam gets to spawn, it will spawn. If Min=0 and Max=1, the branches will be divided over the whole beam but may not use all the beams of the branching emitter. You have to experiment a little with this setting to find the best result.

#### Branch Spawn Amount Range

In *Branch Spawn Amount Range*, both Min and Max have to be larger than 1, as soon as you make one of them smaller than 1, there won't appear any branches at all. The *Branch Spawn Amount* is the number of beams to spawn at each high frequency point. When this is 1, there will be at most 1 branch at each point. If this is 10, there will be up to 10 branches coming off each point.

#### Branch High Frequency Points

This is the range of high frequency points the branches of the beam will be spawned on. The high frequency points are indexed starting with 0 at the beam's origin and continuing up to the number of high frequency points. The *Max* of this can be set well beyond the number of the high frequency points so if you don't want to think about this setting make sure the *Min* is 0 and the *Max* is very large, like 1000.

#### Linkup Lifetime

If *Linkup Lifetime* is False, the branches may stay behind while the large beam is somewhere else already. This happens when the branch has a bigger [lifetime](#lifetime). If you set *Linkup Lifetime* to True, this problem is gone because the branches will live as long as the main beam, no matter what lifeTime they have. Only make sure [Respawn Dead Particles](#respawn-dead-particles) is False for the branches then, otherwise they get spawned at the wrong place when *Linkup Lifetime* is True.For example, here the main beam is red, it has 12 [Low Frequency Points](#lowfrequencypoints), and 60 very small [High Frequency Points](#highfrequencypoints) that can be used as spawnpoints for the 25 green branches.

![branchemitter1.jpg](../../assets/![branchemitter1.jpg](../../assets/branchemitter1.jpg))

You can now do the same in the *Beam Branching* properties of the second beam emitter (the one that was used as branch). In this emitter also set [Use Branching](#usebranching) to True, and set [Branch Emitter](#branchemitter) to the last emitter. This way, the branches get sub-branches themself. Note that not all the branches will get sub-branches, especially the ones closest to the top will get the least. Also, if [Max Particles](#maxparticles) is 10 for the sub-branches, there will be 10 sub-branches total, and not 10 for every branch. For example, this emitter has 10 sub-branches (pink).

![branchemitter2.jpg](../../assets/![branchemitter2.jpg](../../assets/branchemitter2.jpg))

### Trigger

![trigger.jpg](../../assets/![trigger.jpg](../../assets/trigger.jpg))

Triggering allows you to change the behavior of an emitter when it is triggered. You can trigger an emitter just like everything else in Unrealed by setting the *Tag* of the Particle System to be that of an *Event* of a trigger. It is important to note that the *Tag* is not specified per emitter but for the entire particle system. Each emitter can configure how it handles the trigger differently but they will all receive the same trigger event at the same time.Triggers are use mainly to turn emitters on and off in different ways. This trigger system provides good ways to turn emitters on but it unfortunately does not provide a very smooth way to turn emitters off.

#### Toggle Disable

This will toggle the disabledness of the emitter. If the emitter is currently disabled, triggering it will turn it back on. If the emitter is not disabled, triggering it will disable it. When an emitter is toggled, all the particles will either disappear or appear instantly.

#### Reset

This will reset the emitter. This is very much like pressing the

![reset.gif](../../assets/![reset.gif](../../assets/reset.gif))

reset button. The emitter will start over with all its initial values.

#### Number of Particles to Spawn

*Number of Particles to Spawn* is the number of particles that will be spawned when the emitter is triggered. This setting depends on *Particles per Second* described below and also [Max Number of Particles](#max-number-of-particles) in *General*. The particles whose number you specify here will spawn at rate described in *Particles per Second* and will not exceed *Max Number of Particles*.

#### Particles per Second

*Particles per Second* is the rate at which the particles specified above in *Number of Particles to Spawn* will spawn when triggered. If either *Particles per Second* or *Number of Particles to Spawn* are 0, no effect will be observed. If the emitter is currently emitting particles, this setting should be greater than the current rate of particles per second, otherwise no effect will be observed. In most cases *Particles per Second* and *Number of Particles to Spawn* will be used when [Respawn Dead Particles](#respawn-dead-particles) is false but it does not have to be.

## Editing the "Old Way"

To edit the old way, just double click on the emitter in Unrealed. [EmittersReference](EmittersReference.md) covers editing in this manner but it does not include the new particle system features.

