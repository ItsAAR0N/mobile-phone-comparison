import pandas as p
# DEMONSTRATION OF INTEGRATION OF CLASSES
# WILL BE USEFUL FOR OUR PROGRAM WHICH REQUIRES DIFFERENT ASSESSOR METHODS TO FUNCTIONS


# Assign the table of CSV content to a variable, dataFrame
dataFrame = p.read_csv('mobilephone_table.csv') # Reads CSV file, ensure csv file is in the same folder 

# Best that we use classes and functions to store functionality

class MobileComparison:
    def __init__(self, ValueOne, ValueTwo): # Initialise variables
        self.ValueOne,self.ValueTwo = ValueOne,ValueTwo
        self.dataFrame = p.read_csv('mobilephone_table.csv') # Import set o fdata

    def range(self):
        # Display set of data from range N to N
        SetRange = self.dataFrame.loc[self.ValueOne:self.ValueTwo,] 
        print(SetRange) 

    def setSpecific(self):
        setName = "Cost" # Can add different methods to get desired column
        searchTerm = '7,999' # Can add a search function/parameter to find desired results
        SpecificSet = self.dataFrame[(self.dataFrame[setName] == searchTerm)] # Will find phones that cost 7,999 then display it. Cost being an example
        # This method of filtering can be applied to other columns such as name, size etc.
        totalNo = len(SpecificSet)
        print("The total number of values returned: {0}".format(totalNo)) # Finds number of terms returned
        print(SpecificSet.head(totalNo)) # Prints dataFrame

    def Example1(self):
        print("Example")
    
    def Example2(self):
        print("Example")

# Define variables
ValueOne,ValueTwo = 0,0 # Range(X,Y)

while ValueOne == 0 and ValueTwo == 0: # Input Validation
    ValueOne,ValueTwo = int(input("Please enter Min Value: ")),  int(input("Please enter Max Value: "))
    while ValueTwo < ValueOne: # Top (Max) number cannot be less than the starting (min)
        print("\nError, Max value must be less than Min")
        ValueOne,ValueTwo = int(input("Please enter Min Value: ")),  int(input("Please enter Max Value: "))           
    break

Mobile = MobileComparison(ValueOne,ValueTwo) # Input parameters
Mobile.range()
Mobile.setSpecific() # Calls their function under class 

# Printing the total number of rows (1200)
print("The number of datasets is: {0}.".format(len(dataFrame)))


# DEMONSTRATION OF INTEGRATION OF CLASSES
# WILL BE USEFUL FOR OUR PROGRAM WHICH REQUIRES DIFFERENT ASSESSOR METHODS TO FUNCTIONS