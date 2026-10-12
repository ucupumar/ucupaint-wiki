# Preview Mode

Preview Mode is used to isolate and directly view individual layers, layer alphas, final channel outputs, or specific mask/data without interference from scene lighting.

## Channel Preview Mode

The option `Channel` in preview mode will output the entire selected channel output of the channel

|![type:video](./media/preview_mode/channel_preview_mode.mp4)|
|:--:|
|Using channel preview mode| {align=center}

## Layer Preview Mode

The option `Layer` in preview mode lets you see only a single layer that uses the selected channel. If the layer doesn't use the selected channel or if it's disabled, it will show you a pink grid material.

|![type:video](./media/preview_mode/layer_preview_mode.mp4)|
|:--:|
|Using layer preview mode| {align=center}

## Layer Alpha Preview Mode

The option `Layer Alpha` in preview mode is to see only the alpha value of the single layer that uses the selected channel.

|![type:video](./media/preview_mode/layer_alpha_preview_mode.mp4)|
|:--:|
|Using layer alpha preview mode| {align=center}

## Active Data/Mask Preview Mode

The option `Active Mask/Data` in preview mode is to see the selected active data/mask.

|![type:video](./media/preview_mode/data_preview_mode.mp4)|
|:--:|
|Using active mask/data preview mode| {align=center}

## Normal space in preview mode

If normal channel is selected, there will be an option to change the space. By default it uses `View Space` since it's the one that the most helpful to check the surface of the object. You can also choose to use `World Space` or `Object Space`, these options are helpful for painting custom normal. (**TODO: Demo Needed**)

