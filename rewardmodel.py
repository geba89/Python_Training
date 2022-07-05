def reward_function(params):
    
    # inputs
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params["speed"]
    angle = params["steering_angle"]
    wheels = params["all_wheels_on_track"]
    
    marker_0 = 0.05 * track_width
    marker_1 = 0.1 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.5 * track_width
    
    #distance from center
    if distance_from_center <= marker_0:
        reward = 5
    elif distance_from_center <= marker_1:
        reward = 3
    elif distance_from_center <= marker_2:
        reward = 1
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3

    #speed, angle and wheels on track
    if abs(angle) <= 3 and wheels:
        if speed > 2:
            reward = reward * 5
        elif speed > 1:
            reward = reward * 3
        else:
            reward = reward * 1       
    elif abs(angle) > 3 and wheels:
        if speed < 0.5:
            reward = reward * 1
        elif speed < 0.8:
            reward = reward * 3
        else:
            reward = reward * 5
    

    return float(reward)