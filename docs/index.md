# INTRODUCTION TO UCUPAINT

![project-example](source/00.introduction/00-yang_guifei.jpg)

## What is Ucupaint?

Ucupaint is Blender addon to manage textures as layers for Eevee and Cycles renderer.

## Requirements

You need at least Blender 2.79 to use this addon, but more advance features are only available on the modern version of Blender (2.80 & above).

## Installation

- Go to [github.com/ucupumar/ucupaint/releases](https://github.com/ucupumar/ucupaint/releases), and download according to your Blender version.
- Open Blender, go to Edit > User Preferences, select add-ons tabs and press install button, browse your downloaded addon zip file and click install add-on.

## Limitations

- It can be really slow if you have a lot of layers with a lot of channels
- Layer group can make it even slower
- UDIM images are not supported yet
- At the time of this writing, Blender already have [a plan](https://code.blender.org/2022/02/layered-textures-design/) to add texture layer features natively, so if it's already available, you should probably use that instead for better performance.

## Contribute
Visit [Ucupaint Github](https://github.com/ucupumar/ucupaint) to access or contribute to the source code. Or, visit [Ucupaint Wiki Github](https://github.com/ucupumar/ucupaint-wiki) to access or contribute to the source code of this wiki.

## Locations

You can find Ucupaint on the properties panel of 3D viewport and node editor. 

### Blender 2.79

For Blender 2.79, you should be using Cycles render engine.

|![00.b279-loc](./source/00.b279_loc.png)|
|:--:|
|Ucupaint locations on Blender 2.79 are only available if you're using Cycles| {align=center}

### Blender 2.80 and above

For Blender 2.80 and above, it's on the Ucupaint tab.

|![00.b280-loc](./source/00.b280_loc.png)|
|:--:|
|Ucupaint location on Blender 2.80 and above| {align=center}

