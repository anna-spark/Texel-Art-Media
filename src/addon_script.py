import bpy
bpy.ops.wm.read_factory_settings(use_empty=True)  # Clears default Blender scene
class BlenderMocapHandler():
    def __init__(self):
        print("Initializing BlenderMocapHandler...")
        # Ensure add-on is enabled
        addon_name = "BlendArMocap"
        if addon_name not in bpy.context.preferences.addons:
            bpy.ops.preferences.addon_enable(module=addon_name)
        print("Addon enabled")
        # Set the parameters
        # Remove the default cube
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        bpy.context.scene.cgtinker_mediapipe.detection_input_type = "movie"
        print("Parameters set")
        
    def detect(self, video_path, detection_type="POSE", key_frame_step=4, min_detection_confidence=0.5):
        # Start detection using EXEC_DEFAULT instead of INVOKE_DEFAULT
        bpy.context.scene.cgtinker_mediapipe.mov_data_path = video_path # "/home/personooo/Desktop/Code/Texel-Art-Media/src/Walk.mp4"
        bpy.context.scene.cgtinker_mediapipe.enum_detection_type = detection_type
        bpy.context.scene.cgtinker_mediapipe.key_frame_step = key_frame_step
        bpy.context.scene.cgtinker_mediapipe.min_detection_confidence = min_detection_confidence
        print("Starting detection...")
        bpy.ops.wm.cgt_feature_detection_operator('EXEC_DEFAULT')
        print("Detection complete")
    
handler = BlenderMocapHandler()
handler.detect("/home/personooo/Desktop/Code/Texel-Art-Media/src/Walk.mp4")
