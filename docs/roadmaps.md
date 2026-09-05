# Roadmaps

This page roughly lists all the planned features for ucupaint and ucupaint plus. Items listed here may evolve as the development progresses.

## Ucupaint Plus Roadmap

Roadmap for Ucupaint Plus, which is available for at least [silver sponsors on GitHub](https://github.com/sponsors/ucupumar). Some of these features will probably eventually come to regular ucupaint if the funding goes well.

| Feature | Status | Planned for version | Comments |
|---------|---------|-----------|------|
| PSD file export-import | Done | 2.4.7 | |
| Krita KRA file export-import | WIP | 3.x | |
| Gimp XCF file export-import | WIP | 3.x | |
| Sync External File | No | 3.x if the [first goal achieved for GitHub Sponsors](https://github.com/sponsors/ucupumar) | Sync external layered files like PSD, KRA, or XCF so if you edited the file in Blender or an outside application, there is a way to sync between those two. |
| Export layers to Godot shader | Internal testing | 3.x | This will create a native ucupaint file and a Godot plugin to read the data and convert it to a shader. |
| Godot ucupaint editor | No | 3.x or 4.x | UI for ucupaint layers and channels in Godot |
| Painting a layer in Godot | No | 4.x or 5.x | Paint directly on layers in Godot |

## Ucupaint Roadmap

Roadmap for the standard ucupaint release, which will be available for free for all users.

### Ucupaint 3.0

Ucupaint 3.0 will have a lot of internal refactors and some UI redesigns to make it easier to navigate.

| Feature | Status | Comments |
|---------|---------|-----------|
| Normal and height separation | WIP (95%) | Currently normal, bump, and vector displacement are implemented in a single channel. Separating them requires a lot of refactoring, but it is worth it to avoid unnecessary complexity in the future. [(#356)](https://github.com/ucupumar/ucupaint/issues/356)|
| Unified bake target system | Done | This will integrate the current bake channels system into the bake target system. [(#323)](https://github.com/ucupumar/ucupaint/issues/323) |
| Base layer | Done | For less confusion, Ucupaint node inputs will be accessible as a base layer rather than channel settings. [(#392)](https://github.com/ucupumar/ucupaint/issues/392) |
| New `Previous Layers` type for in-between layers adjustment| Done | This type of layer will use the previous layer stacks as the input. It’s useful for adjusting the channel value in the middle of the layer stack. [(#393)](https://github.com/ucupumar/ucupaint/issues/393) |
| Ability to use color attributes as custom bake target | Done | Will likely implemented alongside new bake target system [(#97)](https://github.com/ucupumar/ucupaint/issues/97) |
| Dealing with collapsed main channel panel by default | Done | The main channel list will be collapsed by default since most of the settings are moved somewhere else. Make sure useful features like preview mode are still accessible with the panel collapsed. [(#395)](https://github.com/ucupumar/ucupaint/issues/395)|
| Rename `Vector` input to `Mapping` | Done | In Ucupaint, `Vector` makes more sense if renamed to `Mapping`. [(#394)](https://github.com/ucupumar/ucupaint/issues/394)|

### Ucupaint 3.1

Ucupaint 3.1 versions will focus on custom node support

| Feature | Status | Comments |
|---------|---------|-----------|
| Custom node group as layer/mask | No | [#90](https://github.com/ucupumar/ucupaint/issues/90) |
| Node inputs as layer/mask | No | [#426](https://github.com/ucupumar/ucupaint/issues/426) |

### Ucupaint 3.x

Ucupaint 3.x will focus on baking any layer/layer group as image(s).

| Feature | Status | Comments |
|---------|---------|-----------|
| Bake layer as images for any layer types | No | Currently the system only works for layer types that have a source node with only one socket output. [(#65)](https://github.com/ucupumar/ucupaint/issues/65)|
| Map any image channel into ucupaint layer channel | No | Useful to use ORM image as layer. [(#128)](https://github.com/ucupumar/ucupaint/issues/128) |
| Better dropdown in layer list | No | Trying to improve mask and custom data dropdown on layer list. |
| Image size presets | WIP (60%) | While early testing shows that it is possible, there’s a roadblock that makes the implementation trickier. If the workaround doesn’t work, this feature probably will be pushed to later releases. [(#350)](https://github.com/ucupumar/ucupaint/issues/350)|

### Future features that aren’t in planned milestones yet

These are planned features that will be implemented in future releases. Could be in ucupaint 3.x or even 4.0.

| Feature | Status | Comments |
|---------|---------|-----------|
| Any attributes data support | No | Currently ucupaint can only use color attributes. [(#358)](https://github.com/ucupumar/ucupaint/issues/358)|
| Multiple decals in a single layer/mask | No | [#396](https://github.com/ucupumar/ucupaint/issues/396) |
| Mirrored decal option | No | [#270](https://github.com/ucupumar/ucupaint/issues/270) |
| Vector/Coordinate warp | Testing | Manipulating vector mapping using images/attributes/generated textures. [(#96)](https://github.com/ucupumar/ucupaint/issues/96) |
| Multi-material batch baking | No | Probably will be implemented alongside [#77](https://github.com/ucupumar/ucupaint/issues/77) |
| Baking multiple maps at the same time (AO, Pointiness, etc) | No | [#399](https://github.com/ucupumar/ucupaint/issues/399) |
| Multi-user node group support | No | [#398](https://github.com/ucupumar/ucupaint/issues/398) |
| Lock layers | No | [#199](https://github.com/ucupumar/ucupaint/issues/199) |
| Passthrough Group | No | [#134](https://github.com/ucupumar/ucupaint/issues/134) |
| Copy paste modifier | No | [#89](https://github.com/ucupumar/ucupaint/issues/89) |
| Duplicate mask | No | [#153](https://github.com/ucupumar/ucupaint/issues/153) |
| Option to apply baked layer/mask as standard image | No | [#313](https://github.com/ucupumar/ucupaint/issues/313) |
| Reimplement parallax | No | [#397](https://github.com/ucupumar/ucupaint/issues/397) |
| Principled BSDF layering support | No | [#353](https://github.com/ucupumar/ucupaint/issues/353) |
| Normal map-aware edge detect | Not sure if possible |  |
| Use blender layer backend | Not possible yet | Since Blender already planned to create a native layer system. If that’s implemented, it will be better to use that as the backend of Ucupaint. |

## Documentation Roadmap

| Feature | Status | Comments |
|---------|---------|-----------|
| Automated video clips recording| No | Since ucupaint UI still subject to changes, it's better to create a script to automate ucupaint demo clip recordings. So when the UI changes again, just tweak some parameters and run the script again to rerecord all the clips.|
| Multi-version documentation| No | It's better to be able to switch ucupaint version documentation|
