# Import of libraries 
import pandas as p
import tkinter 
import time as t

# INITIAL DATAFRAME PARSING
# Assign the table of CSV content to a variable, dataFrame

dataFrame = p.read_csv(r'C:\Users\aaron\OneDrive - University of Strathclyde\EE106 Engineering Design for Software\Semester 2 project\Repository\mobilephone_table.csv') # Reads CSV file, ensure csv file is in the same folder 
dataFrame.drop_duplicates(keep='first',inplace=True) # Remove duplicate rows, keeping first set to prevent data loss, inplace means the dataFrame is updated along
dataFrame.dropna(inplace=True) # Drops any NaN values or (empty) cells, inplace to keep changes permanent 
dataFrame.drop(dataFrame.index[24], inplace=True) # Removes the one extra heading in posiiton 24
dataFrame['Cost'] = dataFrame.Cost.str.split(',').str.join('') # Splits the cost to integer rather than string with comma separated values

print("\nHello, welcome to the Mobile Phone Comparison.")
print("There are in total: {0} phones.".format(len(dataFrame))) # Prints total number of rows and columns

# CLASS FILTERING (MAIN)
class Filtering: 
    def __init__(self): # Initialise attributes of the class # VarOne, VarTwo
       self.dataFrame = dataFrame # Import set of data
       #self.VarOne = VarOne # WIP
       #self.VarTwo = VarTwo

    # COMPLETED        
    def dropColumn(self): 
        print("\nThe column headings are as followed:\n{0}".format(', '.join(list(dataFrame)))) # Displays the column headings which the user can choose to remove 
        # Which is formatted to suit the print expression followed by seperation of ', ' then joins each column name together.
        while True: # Input validation
            try:
                dropCount = int(input("\nHow many column(s) do you want to drop? "))
                break
            except ValueError: # If value is not int or is zero
                print("Must be int.")
        for i in range(1,dropCount+1): # Add one to compensate 
            dropSelection = ""
            while dropSelection not in list(self.dataFrame): # Input validation for when user input =/= to any column headings            
                dropSelection = input("Please enter column {0} you want to remove: ".format(i)) # Ensures readability e.g 1... 2.. etc.
            self.dataFrame.drop(columns=[dropSelection],inplace=True) # Start to drop coloumn(s), the use of inplace allows for modification of the dataframe without having to re-assign it             
        print(self.dataFrame) # Show the most up-to-date table after alteration(s) 

    # COMPLETED     
    def sortBy(self): # Add alpha./numerical order sorting functionality
        ColumnSelected,AscendingInput = "",True
        print("\nThe column headings are as followed:\n{0}".format(', '.join(list(dataFrame)))) # Displays the column headings which the user can choose to remove 
        while ColumnSelected == "" and AscendingInput == True: # Input Validation
            ColumnSelected,AscendingInput = input("\nPlease enter a column to sort in order: "),  input("\n[Y] for ascending order, [N] for descending order: ").lower()
            while ColumnSelected not in list(dataFrame):
                ColumnSelected = input("\n(Please re-enter) A column to sort in order: ")
            while AscendingInput != "y" and AscendingInput != "n":
                AscendingInput = input("\n(Please re-enter) [Y] for ascending order, [N] for descending order: ").lower()
        if AscendingInput == "y": # Will be ascending
            AscendingOrder = True
        elif AscendingInput == "n": # Will be descending
            AscendingOrder = False
        self.dataFrame.sort_values(ColumnSelected,ascending=AscendingOrder,inplace=True) # Now sort according to user chosen options
        print(self.dataFrame)

    # COMPLETED
    def narrowSearch(self):
        UserChoice = input("\nWould you like to narrow (delete) your searches based on:\n\n[A] Phone Name\n[B] Cost\n\nEnter choice: ").lower() # Prompt user for desired services
        while UserChoice != "a" and UserChoice != "b": # Input validation
            UserChoice = input("\n(Error) must be either A for Phone Name or B or Phone Cost: ").lower()
        if UserChoice == "a":
            phonenameChoice = input("\nPlease enter the phone name: ") # Set desired phone name
            self.dataFrame = self.dataFrame[~self.dataFrame.Name.str.contains(phonenameChoice)] # If the row contains a phone that the user has specified, it will be deleted
            # Unable to use inplace=True in this case as it has to be defined.
            print(self.dataFrame)

        elif UserChoice == "b": # User can narrow according to cost paramater
            phonecostChoice = input("\nPlease enter the cost: ") # Set desired phone price
            costNarrowChoice = input("\nWould you like to narrow (delete) phones that cost {0} [A], less than [B], or greater than? [C]: ".format(phonecostChoice)).lower() # Choice to choose between equal to, less than or greater than their cost input
            while costNarrowChoice != "a" and costNarrowChoice != "b" and costNarrowChoice != "c":
                costNarrowChoice = input("\n(Error) must be either A for same cost, B for less than or C for greater than: ").lower()
            if costNarrowChoice == "a":
                self.dataFrame.drop(self.dataFrame[dataFrame.Cost == phonecostChoice].index, inplace=True) # Drops phones that cost phonecostChoice, inplace ensures table is constantly updated
                print(self.dataFrame)
            elif costNarrowChoice == "b": # Drops phones that cost less than or equal to phonecostChoice 
                self.dataFrame.drop(self.dataFrame[dataFrame.Cost <= phonecostChoice].index, inplace=True)
                print(self.dataFrame)
            elif costNarrowChoice == "c": # Drops phones that cost greater than or equal to phonecostChoice
                self.dataFrame.drop(self.dataFrame[dataFrame.Cost >= phonecostChoice].index, inplace=True)
                print(self.dataFrame)
                
    def specificSearch(self): # An alternative rather than going through all of the above        
        columnHeadings = ['Name','Storage_details','Camera_details','Battery_details','Processor','Cost']
        print("Please select a phone based on its:\n{0}".format(', '.join(list(columnHeadings))))
        # Define local var 
        columnTerm = ""
        while columnTerm not in columnHeadings: # Input validation for when user input =/= to any column headings
            columnTerm = input("Please enter desired column here: ")            
        searchTerm = input("Please now enter the item you wish to explicitly search within {0}: ".format(columnTerm))
        self.dataFrame = self.dataFrame[self.dataFrame[columnTerm].str.contains(searchTerm)] # If the row contains a phone that the user has specified, it shown
        print(self.dataFrame)

    # COMPLETED
    def initial(self):
        print("\nPlease select the desired function by its number: ")
        print("\n[1] Drop columns \n[2] Sort in alph./number order \n[3] Narrow Search\n[4] Specific Search") # Display list of options to choose from
    # WIP ABOVE (WILL ADD MORE OPTIONS)
        user_input = 0 # Define local variables 
        # Input validation (USING WHILE)
        while True:
            try:
                while user_input < 1 or user_input > 5: # Detects if user_input is within range (1,5)
                    user_input = int(input("\nEnter here: "))
                break
            except ValueError: # If user_input is not an integer it will be detected (ValueError)
                print("Error must be int.")
        if user_input == 1: # Drop columns
            self.dropColumn()
            self.repeat() # Allows for repeatadability functionality 
        elif user_input == 2: # Sort in alph./number order
            self.sortBy()
            self.repeat()
        elif user_input == 3: # Narrow searches
            self.narrowSearch()
            self.repeat()
        elif user_input == 4: # Specific search
            self.specificSearch()
            self.repeat()    
        elif user_input == 5:  # HIDDEN/TEMPORARY (EXIT FOR PROGRAM TESTING PURPOSES)
            self.testingExit() 

    # WIP                            
    def repeat(self): # Program repeatability 
        # Define local var
        userRequest = ""
        # Input validation (makes sure user enters y/n only)
        while userRequest != "y" and userRequest != "n":
            userRequest = input("Would you like to further narrow/filter results? [Y/N]: ").lower()
        # Program will continue re-iterating the functions until the user is finished and enters n 
        if userRequest == "y":
            self.initial()
        elif userRequest == "n":
            print(self.dataFrame) # Print dataFrame state at the moment in time
            # Define local var
            downloadResults = "" 
            # Input validation
            while downloadResults != "y" and downloadResults != "n":
                downloadResults = input("Would you like a copy of the dataframe in Excel file format? [Y/N]: ").lower()
                if downloadResults == "y": # Prints a copy of the dataFrame to Excel format, path is explicitly defined for now - desktop
                    self.dataFrame.to_csv(r'C:\Users\aaron\Desktop\FilteredMobileList.csv', index=False) # No need for numbering down the left side hence index = False
                else: # If user does not want to print it will exit.
                    print("\nHave a nice day! :)") 
                    t.sleep(10)
                    raise SystemExit # Shuts down program with 10 second wait before      
        # WIP

    # TEMPORARY (EXIT FOR PROGRAM TESTING PURPOSES)
    def testingExit(self):
        raise SystemExit

# CLASS COMPARISON (COMPARE TWO DATAFRAMES)
class Comparison:
    def __init__(self):
        self.dataFrame_copy = dataFrame.copy() # Copies the DataFrame as backup for later reference

    def mobileComparison(self): # Compare two dataframes together
        print("Hello") # WIP

# CALL CLASSES
x = Filtering()
x.initial()
