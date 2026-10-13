
# Maximum images per Material in Blender
If you exceed the number of images, material in Blender can appear pink in the viewport. The number of image limit varies across machine specifications and Blender versions. Here are some limitations found.

|     GPU    | UDIM Images Limit (Blender 4.1) | Standard Images Limit (Blender 4.1) | UDIM Images Limit (Blender 4.2) | Standard Images Limit (Blender 4.2) |
| :--------: | :---------------: | :-------------------: | :---------------: | :-------------------: |
|   NVIDIA*  |        27         |          55           |        15         |          30           |
|   Radeon*  |        12         |          24           |        15         |          31           |
|  Apple M series*  |        58         |         116           |        60         |         121           |
|   Intel    |         ?         |           ?           |         ?         |           ?           |

_* tested with RTX 4080, Radeon 6800M, and Apple M3 Laptop_

PC platform (Nvidia, AMD Radeon, Intel) has so much lower image limits compared to Apple Mac M series platform, at least on Blender 4.1 and 4.2. There are at least two solutions to circumvent the image limit issue: by using Vulkan or image atlas.

### Using Vulkan
For modern PCs, it's recommended to use **Vulkan** on Blender 4.4 or above since it can handle more than 100 images. You can change the settings in `System` tab on Blender Preferences.

![image](https://github.com/user-attachments/assets/bcd9db0f-13e7-49f8-a886-83b7cf28f02d)

Blender 4.3 actually can also use Vulkan, but there's a bug that won't let you paint in texture paint mode.

### Converting to Image Atlas
For older Blender versions (Blender 4.3 or lesser), you can convert already used layer/mask images to image atlas.

![image](https://github.com/user-attachments/assets/7f51fd36-6a6d-4942-9ca7-dd56b31e3093)

