# Performance Tips

Here's some performance tips while using ucupaint

- Use less generated textures like noise or voronoi if you want the shader compilation faster
- If you still want many generated textures, it's better to bake them as image since the performace will be a lot faster. The option to `Bake Mask as Image` is inside the gear button beside the mask.
- If you get lag after did a brushstroke, it's probably because Blender want to refresh the material preview image, so closing the material panel that shows the preview will likely make the lag gone.
- Using `Sculpt Mode` to paint color attribute layer/mask will have better performance than using `Vertex Paint Mode`