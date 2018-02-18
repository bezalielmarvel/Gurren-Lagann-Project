from geometrie3D import Objet3D, Polygone3D

def point_inside_polygon(x,y,poly):
    """determine si un point est a l'interieur d'un polygone
        Polygone est une liste de (x,y) pairs."""
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not(inside)
        p1x, p1y = p2x ,p2y

    return inside