infoF = open("NJTollInfo.txt", "r")
index = 0


# Class for the Toll object, will hold the location name and the mile marker
class Toll:
    def __init__(self, location, mile):
        self.location = location
        self.mile = mile

    def tostring(self):
        print("Toll Location: " + self.location, "Mile Marker: " + self.mile)


# Creating the list of tolls located on the NJ Parkway, read from a text file
tollList = []
for index in range(34):
    index += 1
    tollLocation = infoF.readline()
    tollMileMarker = infoF.readline()
    t1 = Toll(tollLocation, tollMileMarker)
    tollList.append(t1)
    tollList[index - 1].tostring()

# User inputs their information
customerName = input("Enter Customer Name: ")
customerPlate = input("Enter Customer License Plate: ")
print("Name is: " + customerName)
print("License Plate: " + customerPlate)

# User inputs monthly EZPass fees and the yearly estimate is calculated
monthlyTotal = float(input("How much were you charged in EZPass fees: "))
yearlyEstimate = monthlyTotal * 12
format_money = "{:.2f}".format(yearlyEstimate)
print("Estimated yearly EzPass cost: $" + format_money)
