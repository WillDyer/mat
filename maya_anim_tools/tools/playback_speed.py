import maya.cmds as cmds

def set_playback_speed():
    current_playback_speed = cmds.playbackOptions(q=True, playbackSpeed=True)
    print(f"Current playback speed: {current_playback_speed}")

    # Define custom playback speeds mapped to Maya's indices
    playback_speeds = [0.5, 1, 2.0]

    current_index = playback_speeds.index(current_playback_speed)
    next = current_index + 1
    
    try:
        speed_to_set = playback_speeds[next]
    except IndexError:
        speed_to_set = playback_speeds[0]
        print("end of list setting to beginning")
    
    cmds.playbackOptions(playbackSpeed=speed_to_set)

    cmds.warning(f"Playback speed set to: {speed_to_set}")
