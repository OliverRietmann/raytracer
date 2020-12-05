from numpy import inf

def get_nearest_obstacle(v, w, object_list, condition=lambda o: True):
    t = inf
    nearest_obstacle = None
    for obstacle in object_list:
        s = obstacle.intersect(v, w)
        if (s < t) and condition(obstacle):
            t = s
            nearest_obstacle = obstacle
    return nearest_obstacle, t
