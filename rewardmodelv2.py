def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    angle = params["steering_angle"]
    speed = params["speed"]
    left_of_center = params["is_left_of_center"]

    on_track = params["all_wheels_on_track"]
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    reward = 1


    if distance_from_center <= marker_1:
       reward = reward * 1.2
    elif distance_from_center <= marker_2:
       reward = reward * 0.8
    elif distance_from_center <= marker_3:
       reward = reward * 0.5
    else:
       reward = 1e-3  

    if angle < -10 and left_of_center:
      reward = reward * 1.2
    elif angle < -10 and not left_of_center:
      reward = reward * 0.7
    elif angle > 10 and not left_of_center:
      reward = reward * 1.2
    elif angle > 10 and left_of_center:
      reward = reward * 0.7

   
    return float(reward)