from numpy import inf

def get_nearest_obstacle(ray, object_list, condition=lambda o: True):
    t = inf
    nearest_obstacle = None
    for obstacle in object_list:
        s = obstacle.intersect(ray)
        if (s < t) and condition(obstacle):
            t = s
            nearest_obstacle = obstacle
    return nearest_obstacle, t
