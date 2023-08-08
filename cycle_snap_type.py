import bpy
from bpy.props import BoolProperty

class op_cycle_snap_type(bpy.types.Operator):
    """Cycles through the different snap types."""
    bl_idname = "snap.cycle_snap_element_type"
    bl_label = "Cycle Snap Element Type"
    bl_options = {'REGISTER'}

    reverse_cycle: BoolProperty(
        name="Reverse Cycle",
        description="Reverse the cycle direction",
        default=False,
    )

    snap_element_items = ["INCREMENT",
        "VERTEX",
        "EDGE",
        "FACE",
        "FACE_NEAREST",
        "VOLUME",
        "EDGE_MIDPOINT",
        "EDGE_PERPENDICULAR"]

    def cycle_direction(self):
        if(self.reverse_cycle):
            return -1
        else:
            return 1

    def execute(self, context):

        direction = self.cycle_direction()

        items = self.snap_element_items

        current = list(bpy.context.scene.tool_settings.snap_elements)

        if(len(current) > 1):
            bpy.context.scene.tool_settings.snap_elements = items[0]
        else:
    
            currentindex = items.index(current[0])
            nextindex = (currentindex + direction) % len(items)

            bpy.context.scene.tool_settings.snap_elements = {items[nextindex]}

        return {'FINISHED'}

# Registration
def register():
    bpy.utils.register_class(op_cycle_snap_type)


def unregister():
    bpy.utils.unregister_class(op_cycle_snap_type)

