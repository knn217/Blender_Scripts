# Blender_Scripts
 A collection of scripts that might be convenient for blender works

Current scripts:

#**flip_pose.py** 

##_Target:_ <br />
Armature actions (animation)<br />


##_This script actually has 2 functions:_ <br />
A trim function for trimming unneeded keyframe points. This one works better than Blender's built in "clean keys" option for me.<br />

A flip function for flipping symmetrical armatures. This one only work correctly if your armature follow certain conditions.<br />


##_Condition for flip function:_ <br />
The armature is symmetrical and separates left to right (.L and .R).<br />

All bones have the same "uneven axis". You can determine this axis by going into edit mode for your armature, turn on axes in "viewport display", go to the front view and check which of the 3 axis (X, Y, Z) looks unsymmetrical on for the left and right side. (You can test this with blender's human metarig, the "uneven axis" is the X axis). <br />


##_How to use:_ <br />
The script targets all actions that ends with "_" in their name, then create a trimmed and a flipped version of each targeted action.<br />

##_for example:_ <br />
To run the script on "action01"<br />
-> Rename "action01" to "action01_" and run script.<br />
-> Receive 2 new actions: "action01_trimmed" and "action01_trimmedflipped".<br />

