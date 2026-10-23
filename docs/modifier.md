# Modifier

Modifiers are useful to add non-destructive effects. You can apply modifiers to a layer, a mask, or the layer channel.

|![Pic: Modifier menu location, legend channel modifier, layer modifer, layer channel modifier, mask modifier](./media/modifier/add_modifier_buttons.png)|
|:--:|
|Various `Add Modifier` menu locations| {align=center}

Keep in mind that not all modifier types are available for every item type. For example, there are only three modifiers available for masks (Invert, Ramp, and Curve).

|![type:video](./media/modifier/add_remove_modifier_on_various_data.mp4)|
|:--:|
|Adding modifier to a layer, a layer channel, and a mask| {align=center, width=100%}

## Modifier types

- **Invert**: will invert selected RGB and alpha values
- **RGB to Alpha**: will convert the RGB of your layer to intensity/alpha and replace the layer's RGB values with a single color.
- **Alpha to RGB**: will convert the alpha of your layer to RGB and replace the layer's alpha value itself with a solid value
- **Color Ramp**: will map the layer RGB values to a color ramp
- **RGB Curve**: will tweak the RGB values using a curve
- **Hue Saturation**: will tweak the RGB values using hue and saturation parameters
- **Brightness Contrast**: will tweak the RGB values using brightness and contrast parameters
- **Math**: will tweak the RGB and alpha values using math operations

## Modifier orders

Be aware if you have more than one modifier, modifier order will affect the result. The order is from bottom to top, so the top modifier will be executed last. You can edit modifier order using this menu.

|![pic: Modifier menu](./media/modifier/modifier_menu.png)|
|:--:|
|Menu for reordering modifier| {align=center}

## Adjustment Layer

If you create a new layer, there's an option to create an adjustment layer. An adjustment layer actually uses a layer type called `Previous Layers` with a modifier applied. The modifier applied to the `Previous Layers` layer will be applied to the all previous layers of the current layer and it will be applied to all channels selected on the layer.

|![type:video](./media/modifier/adjustment_layer_demo.mp4)|
|:--:|
| Adjustment Layer Demo| {align=center, width=100%}

## Transition Modifiers

Transition modifiers are special modifiers that are applied to the layer alpha (including masks) gradient value. It applied on the layer channel but will also affect other channels.

### Transition Bump

Transition bump can be only added to a Height layer channel, it's to sharpen the alpha transition, very useful to create bump lines.

|![type:video](./media/modifier/transition_bump_demo.mp4)|
|:--:|
|Transition Bump Demo| {align=center, width=100%}

Options for transition bump are:

- **Max Height**: Height of the transition bump. The layer height's midlevel will be at the level of the transition bump max height.
- **Edge 1**: The sharpness of the outer edge of the alpha gradient
- **Edge 2**: The sharpness of the inner edge of the alpha gradient
- **Affected Masks**: Number of masks that the transition bump will be applied to
- **Flip**: Flip the transition bump height, this will produce a different effect than just using a negative value of the max height
- **Crease**: Add crease at the outside of the transition bump effect (Can only be used if `Flip` is disabled)
- **Falloff**: Add falloff to the alpha gradient falloff.

On other channels than height, a `Transition Factor` will appear to control the sharpness of the alpha transition of that specific channel.

### Transition Ramp

Transition ramp is for adding a ramp modifier along the alpha gradient value. The transition ramp effect will be sharper if there is also a transition bump enabled in the height channel.

|![type:video](./media/modifier/transition_ramp_demo.mp4)|
|:--:|
|Transition Ramp Demo| {align=center, width=100%}

Options for the transition ramp are:

- **Opacity**: Opacity of the transition ramp
- **Blend**: Blend type of the transition ramp

There's an extra option in the gear button called `Unlink Ramp with Channel Intensity`, it's for unpairing the channel opacity value with the transition ramp colors, so the layer channel can be transparent, but the transition ramp will still be opaque.

### Transition AO

Transition AO is for adding a fake ambient occlusion effect in the area outside of the transition bump. You need the transition bump to be enabled on the height first to use Transition AO.

|![type:video](./media/modifier/transition_ao_demo.mp4)|
|:--:|
|Transition AO Demo| {align=center, width=100%}

Options for transition AO are:

- **Opacity**: Opacity of the transition AO
- **Blend**: Blend type of the transition AO
- **Power**: Strength of the AO
- **Color**: Color of the AO
- **Inside**: Will also add AO inside the inner part of the transition bump
