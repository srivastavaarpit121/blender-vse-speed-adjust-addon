# Blender VSE Speed Adjust Addon

When using Video Sequence Editor in Blender, the speed effect strip doesn't auto-adjusts clip length when changing its speed factor. As a result, we have to manually change the length of the video strip.

Using this very basic addon, we can adjust video strip length based on the speed factor we set.


# Prerequisite
- Blender 3.0.0 or above.
- ```Developer Extras``` option should be enabled, under Edit -> Preferences -> Interface.


# Installation
- Go to Edit -> Preferences -> Addons.
- Press the "Install" button.
- Select the ```sequencer_speed_effect_adjust.py``` file.
- Wait for a few seconds before the installation completes.
- Check the ```Sequencer Speed Effect Adjust``` option to enable it for use.


# How to use?
- Add ```Speed``` effect strip to a video strip.
- Set ```Speed Control``` to ```Multiply```.
- Set your desired ```Multiply Factor/Speed Factor```.
- Video strip's speed will now be increased, but its length will remain the same.
- To change the length, open ```Operator Search``` menu. Default hotkey is ``F3``.
- Type in ```Sequencer Speed Effect Adjust``` to search for this operator, select it, and press enter.

<br>

And that's it. The video strip length will be auto-adjusted to the new speed we set.
