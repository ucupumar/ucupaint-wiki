# Roadmaps

This page roughly lists all the planned features for ucupaint. Items listed here may evolve as the development progresses.

## Ucupaint 3.0

Ucupaint 3.0 will have a lot of internal refactors and some UI redesigns to make it easier to navigate.

| Feature | Status | Comments |
|---------|---------|-----------|
| Base layer | WIP (90%) | For less confusion, Ucupaint node inputs will be accessible as a base layer rather than channel settings. |
| New `Previous Layers` type for in-between layers adjustment| WIP (80%) | This type of layer will use the previous layer stacks as the input. It’s useful for adjusting the channel value in the middle of the layer stack. |
| Unified bake target system | WIP (40%) | This will integrate the current bake channels system into the bake target system. |
| Dealing with collapsed main channel panel by default | No | The main channel list will be collapsed by default since most of the settings are moved somewhere else. Make sure useful features like preview mode are still accessible with the panel collapsed. |
| Normal and height separation | WIP (70%) | Currently normal, bump, and vector displacement are implemented in a single channel. Separating them requires a lot of refactoring, but it is worth it to avoid unnecessary complexity in the future. |
| Better dropdown in layer list | Considered | Trying to improve mask and custom data dropdown on layer list. |
| Rename `Vector` input to `Coordinate` | No | In Ucupaint, `Vector` makes more sense if renamed to `Coordinate`. |

## Ucupaint 3.1

Ucupaint 3.1 will focus on baking any layer/layer group as image(s).

| Feature | Status | Comments |
|---------|---------|-----------|
| Bake layer as images for any layer types | No | Currently the system only works for layer types that have a source node with only one socket output. |
| Map any image channel into ucupaint layer channel | No | Useful to use ORM image as layer. |

## Ucupaint 3.x

Ucupaint 3.x versions will focus on custom node support

| Feature | Status | Comments |
|---------|---------|-----------|
| Custom node group as layer/mask | No |  |
| Image size presets | WIP (60%) | While early testing shows that it is possible, there’s a roadblock that makes the implementation trickier. If the workaround doesn’t work, this feature probably will be pushed to later releases. |


## Future features that aren’t in planned milestones yet

These are planned features that will be implemented in future releases. Could be in ucupaint 3.x or even 4.0.

| Feature | Status | Comments |
|---------|---------|-----------|
| Any attributes data support | No | Currently ucupaint can only use color attributes. |
| Multiple decals in a single layer/mask | No |  |
| Vector/Coordinate warp | Testing | Manipulating vector mapping using images/attributes/generated textures |
| Multi-material batch baking | No |  |
| Baking multiple maps at the same time (AO, Pointiness, etc) | No |  |
| Multi-user node group support | No |  |
| Lock layers | No |  |
| Passthrough Group | No |  |
| Normal map-aware edge detect | Not sure if possible |  |
| Use blender layer backend | Not possible yet | Since Blender already planned to create a native layer system. If that’s implemented, it will be better to use that as the backend of Ucupaint. |
| Reimplement parallax | No |  |

## Documentation Roadmaps

| Feature | Status | Comments |
|---------|---------|-----------|
| Automated video clips recording| No | Since ucupaint UI still subject to changes, it's better to create a script to automate ucupaint demo clip recordings. So when the UI changes again, just tweak some parameters and run the script again to rerecord all the clips.|
| Multi-version documentation| No | It's better to be able to switch ucupaint version documentation|
