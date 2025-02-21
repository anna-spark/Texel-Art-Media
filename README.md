# Blend Mocap module <br>

### Features
- Detection of [Mediapipe](https://google.github.io/mediapipe/) detection results in stream or video
    - Calculation of rotations for mediapipe data
- Transfer tracking data to rigs and generate new transfer configurations
  - currently, officially supports the transfer to generated [rifigy rigs](https://docs.blender.org/manual/en/latest/addons/rigging/rigify/index.html)
  - plan on implementing Mimaximo's 64 bone heirachy

# How to Install:
After cloning this repo, compress it and then install it from Edit > Prefrences (or just click <Crtl ,>).
Click on the dropdown triangle from the top right and click "Install From Disk..." select the compressed file
Make sure to install dependencies by clicking on the "Install Dependencies from the dropdown"



### Mediapipe Detection

Run Mediapipe within Blender to detect pose, hand, face or holistic features.
BlendArMocap calculates rotation data based on the detection results at runtime to drive rigs.<br>

**Caution:** Requires external dependencies which can be installed via the add-on preferences with elevated privileges.

### Transfer

Currently there's a preset configuration to transfer detection results to generated humanoid [rifigy rigs](https://docs.blender.org/manual/en/latest/addons/rigging/rigify/index.html).
To transfer, just select the generated humaniod rig as transfer target and press the `Transfer` Button.
The transfer is based on mapping objects which you can modify. The modifications you can save as own configurations.<br>

You'll find the mapping objects in the collections generated while tracking such as `cgt_HANDS`.
Mapping instructions are stored as object properties and can be modified in the `object data properties` panel (where the constraints live).
Here the concept of mapping objects:

````
mapping_object: object with instructions and constraints
driver_object: generated driver based on instructions
target_object: copies values from driver_object via constraints
````

If you happen to create a configuration to support another rig, feel free to send it to me for sharing via hello@cgtinker.com.<br>

## Uses cgtinker's module:
BlendArMocap is a tool preform markerless tracking within Blender using Google’s [Mediapipe](https://google.github.io/mediapipe/). <br>
For more information, please refer to the [documentation](https://cgtinker.github.io/BlendArMocap/).

