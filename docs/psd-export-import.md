# Export and Import Layers to PSD file

!!! warning
    Currently, the export/import layers feature is available only in Ucupaint Plus, which you can get by becoming at least a silver [Github sponsor](https://github.com/sponsors/ucupumar)

Ucupaint Plus supports exporting and importing layer data to and from PSD files. This feature lets you save your layers in a format compatible with other image editors that use PSD.

## Export Layers to PSD

To export layers as PSD, press the special menu button beside the layer list (the one with `V` icon), and choose `Export Layers as PSD`.

|![[pic: export psd button]](./source/export_psd.png)|
|:--:|
|Export layers to PSD button| {align=center}

Then the export dialog box will appear.

|![[pic: export psd dialog box]](./source/export_psd_dialog_box.png)|
|:--:|
|Export layers to PSD dialog box| {align=center}

Ucupaint uses [PSD-Tools](https://pypi.org/project/psd-tools/) module to make PSD import and export work, so ucupaint will download the module the first time you do PSD export/import. The necessary space needed is about 50-80MB, so the download process might take a couple of seconds to minutes, depending on your internet connection.

There are two options for the export, the first one is `Channel`, which only layers that use that channel will be exported.  The second option is `Convert Solid Colors to pixels`, this is to convert solid color layers to standard pixel layers. This is useful since not all 2D applications can read color fill layer from PSD file (example: Gimp).

The comparison below is the exported layers as shown in Photopea.

|![[pic: convert solid color disabled]](./source/convert_solid_color_to_pixels_disabled.png)|![[pic: convert solid color enabled]](./source/convert_solid_color_to_pixels_enabled.png)|
|:--:|:--:|
| `Convert Solid Colors to pixels` disabled | `Convert Solid Colors to pixels` enabled| {align=center}

## Import Layers from PSD

To import layers from a PSD file, you only need to open the image as layer. And there will be a menu to read the layers if you select a PSD file.

|![[pic: open image button]](./source/open_image_as_layer.png)|
|:--:|
|Open image as layer| {align=center}

|![[pic: read psd layers option]](./source/read_psd_layers_option.png)|
|:--:|
| `Read Photoshop layers` will show up when you select a PSD file| {align=center}

The option `Convert Flat Layer to Solid Color` will detect the standard pixel image, and if the values are the same for all the pixels, it will be converted to a solid color layer.

## Limitations
- Only layers with types of `Image`, `Solid Color`, or `Group` are currently supported for export
- Group mask is currently not supported because of the PSD-Tools limitation
- PSD can only have one mask per layer, so only one image mask is supported for export
- Adjustment layers are not supported yet
- Modifiers from ucupaint are also not supported yet

## Tips

If the color or the blending looks weird on your 2D app. Check the actual color by enabling the color channel's `Preview Mode`. And if it still looks too different, you can also try to disable `Use Linear Color Blending`. By disabling that, the blending colors between layers will be more similar to Photoshop.

|![[pic: use linear color blending option]](./source/use_linear_color_blending_option.png)|
|:--:|
|`Use Linear Color Blending` should be **disabled** to make the blending in ucupaint look the same as in Photoshop | {align=center}


