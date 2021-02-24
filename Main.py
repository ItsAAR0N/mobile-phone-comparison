# Import of libraries 
import pandas as p
import tkinter 

# Assign the table of CSV content to a variable, dataFrame
dataFrame = p.read_csv('mobilephone_table.csv') # Reads CSV file, ensure csv file is in the same folder 
print("There are in total: {0}".format(len(dataFrame))) # Prints total number of rows and columns

print("Hello, welcome to the Mobile Phone Comparison.")

# CLASS FILTERING (MAIN)
class Filtering: 
    def __init__(self, VarOne, VarTwo): # Initialise attributes of the class 
        self.VarOne = VarOne # WIP
        self.VarTwo = VarTwo
        self.dataFrame = p.read_csv('mobilephone_table.csv') # Import set of data
    
    def dropColumn(self):
        print("The column headings are as followed:\n{0}".format(', '.join(list(dataFrame)))) # Displays the column headings which the user can choose to remove 
        # Which is formatted to suit the print expression followed by seperation of ', ' then joins each column name together.
        dropCount = int(input("How many column(s) do you want to drop? "))
        for i in range(1,dropCount+1): # Add one to compensate 
            dropSelection = input("Please enter column {0} you want to remove".format(i)) # Ensures readability e.g 1... 2.. etc.
            self.UpdatedTable = dataFrame.drop(columns=[dropSelection]) # Start to drop coloumn(s) 
            print(self.UpdatedTable) # Show the most up-to-date table after alteration(s)

    def sortBy(self): # Add alpha./numerical order sorting functionality
        print("Hello!") # WIP

    def narrowSearch(self): # Add range narrow searcher functionality
        print("Hello!") # WIP

    def specificSearch(self): # An alternative rather than going through all of the above
        print("Hello") # WIP - user can explicity search for specific phones in one go.
    
    def initial(self):
        print("Please start off by selecting the desired function by its number: ")
        print("\n[1] Drop columns \n[2] Sort in alph./number order \n[3] Narrow Search") # Display list of options to choose from
        # WIP ABOVE (WILL ADD MORE OPTIONS)
        user_input = "" # Define local variables 
        # Input validation (USING WHILE)
        while user_input == "" or user_input < 1 or user_input > 3:
            user_input = int(input("\nEnter here: "))
        if user_input == 1:
            self.dropColumn()
        elif user_input == 2:
            self.sortBy()
        else:
            self.narrowSearch()
        
        # WIP

# CLASS COMPARISON (COMPARE TWO DATAFRAMES)
class Comparison:
    def mobileComparison(self): # Compare two dataframes together
        print("Hello") # WIP