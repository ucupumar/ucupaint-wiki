# Performance Tips

Here are some performance tips while using ucupaint

- Use fewer generated textures, like noise or voronoi, if you want the shader compilation to be faster
- If you still want many generated textures, it's better to bake them as an image since the performance will be a lot faster. The option to `Bake Mask as Image` is inside the gear button beside the mask.
- If you get lag after doing a brushstroke, it's probably because Blender wants to refresh the material preview image, so closing the material panel that shows the preview will likely make the lag go away.
- Using `Sculpt Mode` to paint a color attribute layer/mask will have better performance than using `Vertex Paint Mode`
