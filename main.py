from arithmetic import add, subtract
from geometry import area_rectangle, perimeter_rectangle

def main():
    print("=== Arithmetic Operations ===")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\n--- Arithmetic Results ---")
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))

    print("\n=== Rectangle Calculations ===")
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    print("\n--- Geometry Results ---")
    print("Area of Rectangle:", area_rectangle(length, breadth))
    print("Perimeter of Rectangle:", perimeter_rectangle(length, breadth))

if __name__ == "__main__":
    main()