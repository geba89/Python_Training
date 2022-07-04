def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    crashed = params["is_offtrack"]
    speed = params["speed"]
    angle = params["steering_angle"]
    wheels = params["all_wheels_on_track"]
    
    marker_0 = 0.05 * track_width
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.5 * track_width
    
    #distance from center

    if distance_from_center <= marker_0:
        reward = 1.5
    elif distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.25
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 0.0001

    #speed and angle
    if speed > 1.5 and (angle < 5 and angle > -5) and wheels:
        reward = reward * 2
    elif (speed <= 1.5 and speed >= 0.5) and (angle >=5 and angle <= -5) and wheels:
        reward = reward * 2
    elif wheels: 
        reward = reward * 1
    else:
        reward = reward * 0.1
    
    return float(reward)