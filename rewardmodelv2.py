def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    angle = params["steering_angle"]
    speed = params["speed"]
    on_track = params["all_wheels_on_track"]
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    if on_track:
        reward = 3
    else:
        reward = 1e-3
    #Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
       reward = reward * 2
    elif distance_from_center <= marker_2:
       reward = reward * 1.5
    else:
       reward = 1e-3  # likely crashed/ close to off track
    
    # if abs(angle) > 20:
    #     if speed > 1 and speed < 0.5:
    #         reward = 1e-3
    #     else:
    #         reward = reward * 2
    # elif abs(angle) > 10:
    #     if speed > 1.5 and speed < 0.8:
    #         reward = 1e-3
    #     else:
    #         reward = reward * 2
    # elif abs(angle) >= 5:
    #     if speed > 2 and speed < 1:
    #         reward = 1e-3
    #     else:
    #         reward = reward * 2
    # elif abs(angle) < 5:
    #     if speed > 3 and speed < 2:
    #         reward = 1e-3
    #     else:
    #         reward = reward * 2


    return float(reward)