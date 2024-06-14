print("Enter radius of circle: ")
radius = input()

if radius.isnumeric:
    radius = float(radius)
    perimiter = 3.14*radius*radius
    print("Area: " + str(perimiter))
