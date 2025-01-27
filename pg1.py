import math

def calculate_circle_area():
    # Ask the user to input the radius
    radius = float(input("Enter the radius of the circle: "))

    # Calculate the area of the circle
    area = math.pi * (radius ** 2)

    # Display the result
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

# Call the function
if __name__ == "__main__":
    calculate_circle_area()
