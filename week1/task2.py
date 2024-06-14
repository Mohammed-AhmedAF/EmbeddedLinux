
def askForRadius():
    print("Enter radius of circle: ")
    radius = input()
    calculatePerimiter(radius)

def calculatePerimiter(radius):
    if radius.isnumeric:
        try:
            radius = float(radius)
            perimiter = 3.14*radius*radius
            print("Area: " + str(perimiter))
        except:
            askForRadius()
    else:
        askForRadius()

if __name__=="__main__":
    askForRadius()