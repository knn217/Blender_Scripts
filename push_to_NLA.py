import bpy

def add_NLA_strips(object):

    for action in bpy.data.actions:
        if action.name.endswith(("_trimmed", "_trimmedflipped")):
            track = object.animation_data.nla_tracks.new()
            track.strips.new(action.name, int(action.frame_range[0]), action)
            track.name = action.name

# If there are many armatures in the scene
for obj in bpy.data.objects:
    if obj.type != 'ARMATURE':
        continue
    
    add_NLA_strips(obj)