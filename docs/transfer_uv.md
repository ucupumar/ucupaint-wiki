# Transfer UV

Transfer UV can be useful when you need to transfer an image from one UV map to another UV map. This can be useful if your original UV map wasn't very good and you already created a better one.  The transfer process can take a while since it uses Blender's baking system.

Transfer UV is accessible beside the UV Map section in the expanded mapping panel.

|![type:image](./media/uv_transfer/transfer_uv_menu.png)|
|:--:|
| Transfer UV menu | {align=center}

There are two operators that you can choose, `Transfer UV` will only transfer the current image layer/mask, while `Transfer All Layers & Masks UV` will transfer all image layers/masks that use the same UV.

The `Transfer UV` operator options are:

- **From UV**: Only available for `Transfer All Layers & Masks UV`. All image layers and masks that use this UV will be transferred to new UV.
- **Target UV** / **To UV**: The target UV that the image will be transferred into.
- **Samples**: Samples for the transferred image, the default is using one sample. It's generally fine, but try to increase it if the bake result has jagged lines or noise.
- **Margin**: Number of color pixels spread along the edge of UV islands to hide the UV seams, please increase it if the seam of your model looks visible in the far distance.
- **Delete From UV**: Only available for `Transfer All Layers & Masks UV`. Selected UV on `From UV` will be deleted after the transfer process is done. Useful if you don't want to use the original UV anymore.

## Demo

For example, we can transfer an image from the original UV (_UVMap_) where the image is painted to other UV (_UVMap.001_).

|![type:video](./media/uv_transfer/uv_transfer.mp4)|
|:--:|
|Transfer UV Demo| {align=center}

|![result uv](./media/uv_transfer/original_uv_image.png)|![result uv](./media/uv_transfer/result_uv_image.png)|
|:--:|:--:|
| Original Image is using _UVMap_ | `Transfer UV` Result on _UVMap.001_ |

