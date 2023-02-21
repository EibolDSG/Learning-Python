"""
Challenge Nº4 by MoureDev - POLYGONS
"""

def area_polygon(polygon, b, h = 0):

    if polygon == "Triangle":
        if h == 0:
            print("Error, I need h to calculate the area")
        else:
            print("Area = ", (b*h)/2)

    elif polygon == "Square":
        print("Area = ", b**2)

    elif polygon == "Rectangle":
        if h == 0:
            print("Error, I need h to calculate the area")
        else:
            print("Area = ", b*h)


area_polygon("Rectangle", 3)
