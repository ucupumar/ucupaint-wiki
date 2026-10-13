# Mapping

The layer mapping defines how layer is projected onto the mesh. Ucupaint provides several mapping methods, each using a different coordinate system to determine how the layer is applied to the surface. By default, layers and masks use UV mapping.

## Mapping controls

Most mapping methods provide controls to adjust the mapping position and orientation, including offset, rotation, scale, and transform vector. Decal mapping is the only mapping method that does not provide these transform controls.

|![Default Menu](./media/mapping/DefaultMenu.png)|
|:--:|
|Default Menu| {align=center}

The mapping panel includes the following configurable parameters.

- **Coordinate**: Select the mapping method. See mapping methods bellow. 
- **UV Map**: Only availale for `UV Map` coordinate. Specifies the UV map of the object that will be used.
- **Projection Blend**: Only availale for `Generated` and `Object` coordinate. It's to blend the textures around the projection corners.
- **Transform**: Specifies the transformation space or type.
- **Offset**: Shifts the position on the texture across axis.
- **Rotation**: Rotates the texture oriantation.
- **Scale**: Scales the Textrue along axis. 
- **Blur**: Applies a noise blur filter to mapping vector. You need to increase the sample value if you want to bake the layer/mask/node.

Other than decal, the rest of coordinate types has Transform, Offset, Rotation, and Scale controls.

## Coordinate Types

To ilustrate the mapping coordinate types, The examples use the same image to demonstrate how it is projected onto the mesh.

|![Texture](./media/mapping/Rainbow-gradient-fully-saturated.png)|
|:--:|
|Texture used for example| {align=center}

### Generated

Generated mapping projects the layer around the mesh from all directions using coordinates generated from its geometry, creating a box-like projection around the object.

|![type:video](./media/mapping/mapping_generated.mp4)|
|:--:|
|Generated| {align=center}

### Normal

Normal mapping projects the layer onto the mesh using the direction of its surface normals, creating a projection that follows the orientation of the surface.

|![type:video](./media/mapping/mapping_normal.mp4)|
|:--:|
|Normal| {align=center}

### UV

UV mapping projects the layer onto the mesh using its UV coordinates, allowing the layer to follow the existing UV layout of the object.

|![type:video](./media/mapping/mapping_uv.mp4)|
|:--:|
|UV| {align=center}

### Object

Object mapping projects the layer using the mesh's coordinates in Blender's 3D space, creating a three-dimensional projection around the object.

|![type:video](./media/mapping/mapping_object.mp4)|
|:--:|
|Object| {align=center}

### Camera

Camera mapping projects the layer onto the mesh from the camera's viewpoint, creating a projection that follows the camera's position and orientation.

|![type:video](./media/mapping/mapping_camera.mp4)|
|:--:|
|Camera| {align=center}

### Window

Window mapping projects the layer onto the mesh using screen-space coordinates, similar to cutting out a picture in the shape of the mesh from the background.

|![type:video](./media/mapping/mapping_window.mp4)|
|:--:|
|Window| {align=center}

### Reflection

Reflection mapping projects the layer onto the mesh using reflection directions calculated from the camera and the surface normals, similar to reflecting a ray off a reflective surface to determine where the texture is sampled.

|![type:video](./media/mapping/mapping_reflection.mp4)|
|:--:|
|Reflection| {align=center}

### Decal

Decal mapping projects the layer onto the mesh using a defined projection shape. After selecting decal coordinate mapping, Ucupaint will spawn an empty object that will control the decal. By default it's parented to the active object.

The Decal method is an exception and does not provide Transform, Offset, Scale, or Rotate options. Instead, it possesses the following options:

- **Decal Object**: Points to object in scene to use as decal projection. By default it points to the spawned empty object, but can be replaced by any other object.
- **Mode**: Choses from decal projections methods (Flat, Cylinder, Sphere)
- **Scale**: Only available for Cylinder and Sphere Decal. It provides scaling for the image X and Y across the decal projection allowing for repetition or cropping of the decal projected part. 
- **Decal constraint**: Only available for flat decal. Applies constraints to surface modifier, pulling decal to be always on surface of the object.
- **Decal Distance**: Controls how far texture is projected.
- **Select Decal Object**: A button that automatically selects the decal object.
- **Set Position to cursor**: Sets the 3d space cursor to the decal position. 

#### Plane Decal

Plane decal mapping projects the layer from a flat plane onto the mesh, similar to projecting an image straight onto a surface.

|![type:video](./media/mapping/mapping_decal_plane.mp4)|
|:--:|
|Decal plane| {align=center}

#### Cylinder

Cylinder decal mapping projects the layer from the inside of a cylinder onto the mesh, like placing the image on the inside of a tube and projecting it onto the object.

|![type:video](./media/mapping/mapping_decal_cylinder.mp4)|
|:--:|
|Decal cylinder| {align=center}

#### Sphere

Sphere decal mapping projects the layer from the inside of a sphere onto the mesh, like placing the image on the inside of a ball and projecting it onto the object.

|![type:video](./media/mapping/mapping_decal_sphere.mp4)|
|:--:|
|Decal sphere| {align=center}
