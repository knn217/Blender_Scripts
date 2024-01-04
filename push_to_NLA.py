import bpy

def add_NLA_strips(object):
    text_file = open("D:\\OGRE_NEXT\\action_enum.txt", "w")
    text = ""
    text += "enum character_anim { \n"
    enum_value = 0
    
    for action in bpy.data.actions:
        if action.name.endswith(("_trimmed", "_trimmedflipped")):
            track = object.animation_data.nla_tracks.new()
            track.strips.new(action.name, int(action.frame_range[0]), action)
            
            if action.name.endswith(("_trimmed")):
                enum  = action.name.replace('_trimmed', '')
            elif action.name.endswith(("_trimmedflipped")):
                enum  = action.name.replace('trimmed', '')
            
            enum = "\tanim_" + enum
            
            #track.name = str(enum_value)
            #track.name = action.name
            track.name = enum
            text += enum + " = " + str(enum_value) + ",\n"
            enum_value += 1
    text += "};\n"
    text_file.write(text)

# If there are many armatures in the scene
for obj in bpy.data.objects:
    if obj.type != 'ARMATURE':
        continue
    
    add_NLA_strips(obj)