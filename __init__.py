bl_info = {
    "name": "Blenderfolk Verktøykasse",
    "author": "Bjørnar",
    "version": (0, 1),
    "blender": (3, 4, 0),
    "location": "Hotkeys only atm.",
    "description": "",
    "warning": "",
    "doc_url": "",
    "category": "NORGE",
}

from . import cycle_snap_type

classes = [
    cycle_snap_type
]

import importlib

# if this is true, it means Blender did bpy.ops.scripts.reload()
# if false, it's a fresh boot of Blender
if("bpy" in globals()):

    print("Reloading Blenderfolk Verktøy")

    for c in classes:
        importlib.reload(c)

import bpy

# ----------------
# REGISTRATION
# ----------------

def register():
    for c in classes:
        c.register()

def unregister():
    for c in classes:
        c.unregister()


if __name__ == "__main__":
    register()
