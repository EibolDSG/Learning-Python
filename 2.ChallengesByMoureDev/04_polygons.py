"""
Challenge Nº4 by MoureDev - POLYGONS
"""

def area_polygon(polygon, b, h = 0):

    if polygon == "Triangle":
        print("Area = ", (b*h)/2)

    elif polygon == "Square":
        print("Area = ", b**2)

    elif polygon == "Rectangle":
        print("Area = ", b*h)


area_polygon("Square", 3)
