import bpy

class BlenderMocapHandler():
    def clear_scene(self):
        """Manually removes all objects instead of resetting to factory settings."""
        if bpy.context.object and bpy.context.object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')  # Switch to object mode
        bpy.ops.object.select_all(action='SELECT')  # Select all objects
        bpy.ops.object.delete()  # Delete selected objects
        for collection in bpy.data.collections:
            bpy.data.collections.remove(collection)  # Remove all collections

        # Ensure there's no lingering data
        for block in bpy.data.objects:
            bpy.data.objects.remove(block)
        for block in bpy.data.meshes:
            bpy.data.meshes.remove(block)
        for block in bpy.data.materials:
            bpy.data.materials.remove(block)
        for block in bpy.data.textures:
            bpy.data.textures.remove(block)
        for block in bpy.data.images:
            bpy.data.images.remove(block)
        
        bpy.ops.outliner.orphans_purge(do_recursive=True)
        print("Scene cleared")

    # Clear the scene at the start
    def __init__(self):
        # Ensure add-on is enabled
        addon_name = "BlendArMocap"
            
        if addon_name not in bpy.context.preferences.addons:
            bpy.ops.preferences.addon_enable(module=addon_name)
        # Set the parameters
        # Remove the default cube
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        bpy.context.scene.cgtinker_mediapipe.detection_input_type = "movie"
        self.clear_scene()
        
    def detect(self, video_path, detection_type="POSE", key_frame_step=4, min_detection_confidence=0.5):
        # Start detection using EXEC_DEFAULT instead of INVOKE_DEFAULT
        bpy.context.scene.cgtinker_mediapipe.mov_data_path = video_path # "/home/personooo/Desktop/Code/Texel-Art-Media/src/Walk.mp4"
        bpy.context.scene.cgtinker_mediapipe.enum_detection_type = detection_type
        bpy.context.scene.cgtinker_mediapipe.key_frame_step = key_frame_step
        bpy.context.scene.cgtinker_mediapipe.min_detection_confidence = min_detection_confidence
        print("Starting detection...")
        bpy.ops.wm.cgt_feature_detection_operator('EXEC_DEFAULT')
        print("Detection complete")
        
    def get_cgt_points():
        """Extracts cgt_POINTS from the scene and returns a list of dictionaries."""
        cgt_points = []
        for obj in bpy.data.objects:
            if obj.name.startswith("cgt_"):  # Assuming all relevant points start with 'cgt_'
                cgt_points.append({
                    "name": obj.name,
                    "x": obj.location.x,
                    "y": obj.location.y,
                    "z": obj.location.z
                })
        return cgt_points

    
handler = BlenderMocapHandler()
handler.detect("/home/personooo/Desktop/Code/Texel-Art-Media/src/Walk.mp4")
