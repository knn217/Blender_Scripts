import bpy
import os
# clear terminal
os.system('cls')

square_width = 150
left_foot = [0, 0]
right_foot = [0, 0]
left_knee = [0, 0]
right_knee = [0, 0]
left_hip = [0, 0]
right_hip = [0, 0]
left_hand = [0, 0]
right_hand = [0, 0]
left_elbow = [0, 0]
right_elbow = [0, 0]
left_chest = [0, 0]
right_chest = [0, 0]
head = [0, 0]
torso_high = [0, 0]
torso_low = [0, 0]
collision = [0, 0]


def iterate_through_actions(object):
    text_file = open("D:\\OGRE_NEXT\\state_frame.txt", "w")
    text = ""
    
    for action in bpy.data.actions:
        #===============================================#
        # MARK THE ANIMATIONS YOU WANT TO TRIM AND FLIP # 
        #       WITH A '_' AT THE END OF THE NAME       #
        #===============================================#
        if action.name.endswith(('_')):
            # set this action to active
            bpy.context.object.animation_data.action = action
            
            if action.name.endswith((
            'idle_', 'walk_forward_', 'walk_backward_', 
            'crouch_', 'crawl_forward_', 'crawl_backward_'
            )):
                start_frame = 1
                end_frame = 2
                text += "const int16_t char01_" + action.name[:-1] + "[1][2][16] = { "
            else:
                start_frame = int(action.frame_range[0])
                end_frame = int(action.frame_range[1])            
                text += "const int16_t char01_" + action.name[:-1] + "[" + str(end_frame-1) + "][2][16] = { "
            #print(text)
            
            for i in range(start_frame, end_frame):
                print(i)
                bpy.context.scene.frame_set(i)             
                for bone in bpy.data.objects['metarig_custom'].pose.bones:
                                        
                    # left foot 
                    if bone.name.endswith(('foot_hurtbox.L')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        left_foot[0] = (global_location[1] * 1000)
                        left_foot[1] = (global_location[2] * 1000)

                    # right foot 
                    if bone.name.endswith(('foot_hurtbox.R')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        right_foot[0] = (global_location[1] * 1000)
                        right_foot[1] = (global_location[2] * 1000)

                    # left knee 
                    if bone.name.endswith(('knee.L')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        left_knee[0] = (global_location[1] * 1000)
                        left_knee[1] = (global_location[2] * 1000)

                    # right knee 
                    if bone.name.endswith(('knee.R')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        right_knee[0] = (global_location[1] * 1000)
                        right_knee[1] = (global_location[2] * 1000)

                    # left hip 
                    if bone.name.endswith(('thigh_deform.L')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        left_hip[0] = (global_location[1] * 1000)
                        left_hip[1] = (global_location[2] * 1000)

                    # right hip
                    if bone.name.endswith(('thigh_deform.R')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        right_hip[0] = (global_location[1] * 1000)
                        right_hip[1] = (global_location[2] * 1000)

                    # left hand 
                    if bone.name.endswith(('wrist.L')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        left_hand[0] = (global_location[1] * 1000)
                        left_hand[1] = (global_location[2] * 1000)

                    # right hand
                    if bone.name.endswith(('wrist.R')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        right_hand[0] = (global_location[1] * 1000)
                        right_hand[1] = (global_location[2] * 1000)
                        
                    # left elbow
                    if bone.name.endswith(('forearm.L')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        left_elbow[0] = (global_location[1] * 1000)
                        left_elbow[1] = (global_location[2] * 1000)

                    # right elbow
                    if bone.name.endswith(('forearm.R')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        right_elbow[0] = (global_location[1] * 1000)
                        right_elbow[1] = (global_location[2] * 1000)
                        
                    # left chest
                    if bone.name.endswith(('upper_arm.L')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        left_chest[0] = (global_location[1] * 1000)
                        left_chest[1] = (global_location[2] * 1000)

                    # right chest
                    if bone.name.endswith(('upper_arm.R')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        right_chest[0] = (global_location[1] * 1000)
                        right_chest[1] = (global_location[2] * 1000)

                    # head
                    if bone.name.endswith(('spine.007')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        head[0] = (global_location[1] * 1000)
                        head[1] = (global_location[2] * 1000)
                        
                    # torso_high
                    if bone.name.endswith(('spine.003')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        torso_high[0] = (global_location[1] * 1000)
                        torso_high[1] = (global_location[2] * 1000)
                        
                    # torso_low
                    if bone.name.endswith(('spine.002')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        torso_low[0] = (global_location[1] * 1000)
                        torso_low[1] = (global_location[2] * 1000)
                        
                    # collision
                    if bone.name.endswith(('spine.002')):
                        global_location = bpy.context.object.matrix_world @ bone.matrix @ bone.location
                        collision[0] = (global_location[1] * 1000)
                        collision[1] = (global_location[2] * 1000)

                
                # "left" actually means front because of the direction 
                if (end_frame - start_frame) <= 1:
                    pass
                else:
                    text += "\n\t"
                text+= "{ {"
                text+= str(int(left_foot[0])) + ", "
                text+= str(int(right_foot[0])) + ", "
                text+= str(int(left_knee[0])) + ", "
                text+= str(int(right_knee[0])) + ", "
                text+= str(int(left_hip[0])) + ", "
                text+= str(int(right_hip[0])) + ", "
                text+= str(int(torso_high[0])) + ", "
                text+= str(int(torso_low[0])) + ", "
                text+= str(int(left_hand[0])) + ", "
                text+= str(int(right_hand[0])) + ", "
                text+= str(int(left_elbow[0])) + ", "
                text+= str(int(right_elbow[0])) + ", "
                text+= str(int(left_chest[0])) + ", "
                text+= str(int(right_chest[0])) + ", "
                text+= str(int(head[0])) + ", "
                text+= str(int(collision[0]))
                text+= " }, { "
                text+= str(int(left_foot[1])) + ", "
                text+= str(int(right_foot[1])) + ", "
                text+= str(int(left_knee[1])) + ", "
                text+= str(int(right_knee[1])) + ", "
                text+= str(int(left_hip[1])) + ", "
                text+= str(int(right_hip[1])) + ", "
                text+= str(int(torso_high[1])) + ", "
                text+= str(int(torso_low[1])) + ", "
                text+= str(int(left_hand[1])) + ", "
                text+= str(int(right_hand[1])) + ", "
                text+= str(int(left_elbow[1])) + ", "
                text+= str(int(right_elbow[1])) + ", "
                text+= str(int(left_chest[1])) + ", "
                text+= str(int(right_chest[1])) + ", "
                text+= str(int(head[1])) + ", "
                text+= str(int(collision[1]))
                text+= " } },"
            text+= "  }; \n" 
                
    text += "typedef const int16_t(boxes_ptr)[2][16];\n"               
    text_file.write(text)

for obj in bpy.data.objects:
    if obj.type != 'ARMATURE':
        continue
    iterate_through_actions(obj)




#bpy.context.scene.frame_set(1)

"""
obj = bpy.context.object
for bone in bpy.data.objects['metarig_custom'].pose.bones:
    global_location = obj.matrix_world @ bone.matrix @ bone.location
    
    print(f'{bone.name}.location = {global_location}')
    #print(f'{bone.name}.location = {bone.location}')
"""