from numpy import inf

"""
Bestimmt das Objekt, welches vom Strahl
v + t * w, t > 0 getroffen wird und gibt
zudem den Schnittpunkt-Parameter t zurück
"""
def get_nearest_obstacle(v, w, object_list):
    t = inf
    nearest_obstacle = None
    for obstacle in object_list:
        s = obstacle.intersect(v, w)
        if (s < t):
            t = s
            nearest_obstacle = obstacle
    return nearest_obstacle, t
