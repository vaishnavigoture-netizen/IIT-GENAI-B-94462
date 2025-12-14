import math

def area_circle(r):
    return math.pi * r * r

def area_rectangle(l, w):
    return l * w

def area_triangle(b, h):
    return 0.5 * b * h

if __name__ == "__main__":
    
    radius = float(input("Enter radius of circle: "))
    print("Area of circle =", area_circle(radius))

    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    print("Area of rectangle =", area_rectangle(length, width))

    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    print("Area of triangle =", area_triangle(base, height))
