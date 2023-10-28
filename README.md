# Blender_Scripts
 A collection of scripts that might be convenient for blender works

Current scripts:

- flip_pose.py ------------------------

Target: Armature actions (animation)


This script actually has 2 functions: 
_A trim function for trimming unneeded keyframe points. This one works better than Blender's built in "clean keys" option for me.

_A flip function for flipping symmetrical armatures. This one only work correctly if your armature follow certain conditions.


Condition for flip function:
_The armature is symmetrical and separates left to right (.L and .R).

_All bones have the same "uneven axis". You can determine this axis by going into edit mode for your armature, turn on axes in "viewport display", go to the front view and check which of the 3 axis (X, Y, Z) looks unsymmetrical on for the left and right side. (You can test this with blender's human metarig, the "uneven axis" is the X axis). 


How to use: 
_The script targets all actions that ends with "_" in their name, then create a trimmed and a flipped version of each targeted action.

for example: to run the script on "action01"
-> Rename "action01" to "action01_" and run script.
-> Receive 2 new actions: "action01_trimmed" and "action01_trimmedflipped".

