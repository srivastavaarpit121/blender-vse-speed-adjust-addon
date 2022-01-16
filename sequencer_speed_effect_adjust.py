import bpy



bl_info = {
    "name": "Sequencer Speed Effect Adjust",
    "author": "Arpit Srivastava",
    "version": (0, 1),
    "blender": (3, 0, 0),
    "location": "Operator Search (F3) -> Sequencer Speed Effect Adjust",
    "description": "Automatically adjusts video strip's length, based on speed effect strip's speed factor.",
    "category": "Sequencer",
}



class SpeedAdjust(bpy.types.Operator):
    bl_idname = "sequencer.speed_adjust"
    bl_label = "Sequencer Speed Effect Adjust"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        scene = bpy.context.scene
        active_strip = scene.sequence_editor.active_strip

        if (active_strip.type == "SPEED"):
            
            indep_strip = active_strip.input_1
            speed_factor = active_strip.speed_factor
            
            start = indep_strip.frame_start
            end = indep_strip.frame_final_end
            duration = indep_strip.frame_duration
            
            duration = int(duration/speed_factor)
            end = start + duration
            
            indep_strip.frame_final_start = start
            indep_strip.frame_final_end = end

        return {'FINISHED'}



def register():
    bpy.utils.register_class(SpeedAdjust)

def unregister():
    bpy.utils.unregister_class(SpeedAdjust)



if __name__ == "__main__":
    register()