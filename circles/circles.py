from math import pi

def circle_area(r):
    """Returns area of a circle"""
    if r < 0:
        raise ValueError("Radius cannot be negative")

    return pi*(r**2)


# print(circle_area.__doc__)

