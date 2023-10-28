import bpy
import os
# clear terminal
os.system('cls')

                 #=============#
                 # INSTRUCTION #
#===============================================#
# MARK THE ANIMATIONS YOU WANT TO TRIM AND FLIP # 
#       WITH A '_' AT THE END OF THE NAME       #
#===============================================#


# create new empty action
def create_new_action(name):
    new_act = bpy.data.actions.new(name)
    return new_act


# create a keyframe trimmed action from an original action
def create_trimmed_action(orig_action):
    print('trimming')
    # if an action with the same name already existed, delete it
    for action in bpy.data.actions:
        if action.name == orig_action.name + 'trimmed':
            bpy.data.actions.remove(action, do_unlink=True)
            
    # create trimmed action
    trimmed_act = create_new_action(orig_action.name + 'trimmed')
            
    for fc in orig_action.fcurves:
        # This if filters curves with property of 'loc, rot, scale'
        if fc.data_path.endswith(('location','rotation_euler','rotation_quaternion','scale')):
            # Create a new fcurve for the trimmed action
            new_fc = trimmed_act.fcurves.new(
                fc.data_path, 
                index=fc.array_index, 
                action_group=fc.group.name)
            
            old_left_flag = True
            left_flag = True
            right_flag = True
            old_value = None
            previous_keyframe = None
            for key in fc.keyframe_points :
                # 1st keyframe
                if key == fc.keyframe_points[0]:                    
                    # set flags
                    left_flag = True
                    right_flag = (key.co[1] == key.handle_right[1])
                    previous_keyframe = None # make sure not to copy last keyframe 
                    
                    # always copy 1st keyframe to the new action
                    new_key = new_fc.keyframe_points.insert(
                        key.co[0],
                        key.co[1],
                        options={'NEEDED'},
                        keyframe_type=key.type)
                    
                    new_key.handle_left = key.handle_left    
                    new_key.handle_left_type = key.handle_left_type
                    new_key.handle_right = key.handle_right     
                    new_key.handle_right_type = key.handle_right_type                                         
                
                # final keyframe 
                elif key == fc.keyframe_points[-1]:
                    # set flags
                    left_flag = right_flag & (key.co[1] == old_value) & (key.handle_left[1] == old_value)
                    right_flag = True
                    
                    # Copy previous frame if any flag is false
                    if not (left_flag & old_left_flag):
                        if (previous_keyframe != None):
                            # copy to new action
                            new_key = new_fc.keyframe_points.insert(
                                previous_keyframe.co[0],
                                previous_keyframe.co[1],
                                options={'NEEDED'},
                                keyframe_type=previous_keyframe.type)
                            
                            new_key.handle_left = previous_keyframe.handle_left    
                            new_key.handle_left_type = previous_keyframe.handle_left_type
                            new_key.handle_right = previous_keyframe.handle_right     
                            new_key.handle_right_type = previous_keyframe.handle_right_type 
                    
                    # still check to copy last keyframe, but also check to copy the ending keyframe 
                    # COPY AT THE END!
                    # CHANGING THE ORDER WHILE COPYING WILL CHANGE THE F_CURVE
                    if not left_flag:
                        # copy to new action
                        new_key = new_fc.keyframe_points.insert(
                            key.co[0],
                            key.co[1],
                            options={'NEEDED'},
                            keyframe_type=key.type) 
                        
                        new_key.handle_left = key.handle_left    
                        new_key.handle_left_type = key.handle_left_type
                        new_key.handle_right = key.handle_right     
                        new_key.handle_right_type = key.handle_right_type 
                
                # other keyframes        
                else:
                    # set flags
                    left_flag = right_flag & (key.co[1] == old_value) & (key.handle_left[1] == old_value)
                    right_flag = (key.co[1] == key.handle_right[1])
                    # save current keyframe if not start or end
                    previous_keyframe = key
                    
                    # Copy last frame if any flag is false
                    if not (left_flag & old_left_flag):
                        if (previous_keyframe != None):
                            # copy to new action
                            new_key = new_fc.keyframe_points.insert(
                                previous_keyframe.co[0],
                                previous_keyframe.co[1],
                                options={'NEEDED'},
                                keyframe_type=previous_keyframe.type)
                            
                            new_key.handle_left = previous_keyframe.handle_left    
                            new_key.handle_left_type = previous_keyframe.handle_left_type
                            new_key.handle_right = previous_keyframe.handle_right     
                            new_key.handle_right_type = previous_keyframe.handle_right_type  
                                        
                
                # save old value and old left flag
                old_value = key.co[1]
                old_left_flag = left_flag
                                                        
    return trimmed_act


# create a flipped action from an original action if the uneven axis is specified
# The uneven axis: the axis that points at unsymetrical directions on left and right bones in edit mode
# If your armature does not have the same uneven axis on all bones, the results might be wrong
def create_flipped_action(orig_action, uneven_axis):
    print('flipping')
    if (uneven_axis == 'X') | (uneven_axis == 'x'):
        flip_axis_index = 0
    elif (uneven_axis == 'Y') | (uneven_axis == 'y'):
        flip_axis_index = 1
    elif (uneven_axis == 'Z') | (uneven_axis == 'z'):
        flip_axis_index = 2
    # if an action with the same name already existed, delete it
    for action in bpy.data.actions:
        if action.name == orig_action.name + 'flipped':
            bpy.data.actions.remove(action, do_unlink=True)
            
    # create flipped action
    flipped_act = create_new_action(orig_action.name + 'flipped')
    
    for fc in orig_action.fcurves:
        # This if filters curves with property of 'loc, rot, scale'
        if fc.data_path.endswith(('location','rotation_euler','rotation_quaternion','scale')):
            # create new fcurve for the new flipped action
            # thre are 3 cases: .L, .R and neutral
            if fc.data_path.endswith(('.R"].location','.R"].rotation_euler','.R"].rotation_quaternion','.R"].scale')):
                new_data_path = fc.data_path.replace('.R"].', '.L"].')
                new_group_name = fc.group.name.replace('.R','.L')
            elif fc.data_path.endswith(('.L"].location','.L"].rotation_euler','.L"].rotation_quaternion','.L"].scale')):
                new_data_path = fc.data_path.replace('.L"].', '.R"].')
                new_group_name = fc.group.name.replace('.L','.R')
            else:
                new_data_path = fc.data_path
                new_group_name = fc.group.name
            
            
            new_fc = flipped_act.fcurves.new(
                new_data_path, 
                index=fc.array_index,           # even if flipped, they should have the same index
                action_group=new_group_name)
            
            for key in fc.keyframe_points :
                # Handle left and right of key frames 
                # location: flip axis not symmetrical, the rest are symmetrical
                if fc.data_path.endswith('location'):
                    if fc.array_index == flip_axis_index:
                        flip_value = -1
                    else:
                        flip_value = 1
                
                # rotation euler: flip axis is symmetrical, the rest are not
                # ALL EULER ROCATIONS (XYZ, YZX,...) SEEMS TO HAVE THE SAME ORDER:
                # X = 0; Y = 1; Z = 2
                # I couldn't find the exact source that confirms this,
                # the conclusion is based on the order in the action editor and the script's result
                elif fc.data_path.endswith('rotation_euler'):
                    if fc.array_index == flip_axis_index:
                        flip_value = 1
                    else:
                        flip_value = -1
                
                # rotation quaternion: w and flip axis are symmetrical, the rest are not
                elif fc.data_path.endswith('rotation_quaternion'):
                    if (fc.array_index == (flip_axis_index + 1)) | (fc.array_index == 0):
                        flip_value = 1
                    else:
                        flip_value = -1
                
                # scale: all are symmetrical
                elif fc.data_path.endswith('scale'):
                    flip_value = 1
                    
                new_key = new_fc.keyframe_points.insert(
                    key.co[0],
                    key.co[1] * flip_value,
                    options={'NEEDED'},
                    keyframe_type=key.type)
                    
                new_key.handle_left = key.handle_left
                new_key.handle_left[1] *= flip_value
                new_key.handle_left_type = key.handle_left_type
                
                new_key.handle_right = key.handle_right 
                new_key.handle_right[1] *= flip_value    
                new_key.handle_right_type = key.handle_right_type  
                                        
    return flipped_act


def iterate_through_actions(object):
    for action in bpy.data.actions:
        #===============================================#
        # MARK THE ANIMATIONS YOU WANT TO TRIM AND FLIP # 
        #       WITH A '_' AT THE END OF THE NAME       #
        #===============================================#
        if action.name.endswith(('_')):
            # create trimmed action from the original action
            trimmed_action = create_trimmed_action(action)
            # create flipped action from the trimmed action           
            flipped_action = create_flipped_action(trimmed_action, 'X')
                 


# If there are many armatures in the scene
for obj in bpy.data.objects:
    if obj.type != 'ARMATURE':
        continue
    iterate_through_actions(obj)

