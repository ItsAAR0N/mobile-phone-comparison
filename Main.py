# Import of libraries 
import pandas as p
import time as t

# Assign the table of CSV content to a variable, dataFrame then pass to class
dataFrame = p.read_csv(r'C:\Users\aaron\OneDrive - University of Strathclyde\YEAR 1\EE106 Engineering Design for Software\Semester 2 project\Repository\mobilephone_table.csv') # Reads CSV file, ensure csv file is in the same folder 
# INITIAL DATAFRAME PARSING
dataFrame.drop_duplicates(keep='first',inplace=True) # Remove duplicate rows, keeping first set to prevent data loss, inplace means the dataFrame is updated along
dataFrame.dropna(inplace=True) # Drops any NaN values or (empty) cells, inplace to keep changes permanent 
dataFrame.drop(dataFrame.index[24], inplace=True) # Removes the one extra heading in position 24
dataFrame['Cost'] = dataFrame.Cost.str.split(',').str.join('').astype(int) # Splits the cost to integer rather than string with commas
# CREATE COPY FOR SECOND MOBILE PHONE COMPARISON.
copydataFrame = dataFrame.copy()

print("\nHello, welcome to the Mobile Phone Comparison!")

# CLASS FILTERING (MAIN)
class Filtering: 
    def __init__(self, RunSecondTime): # Initialise attributes of the class
        self.RunSecondTime = RunSecondTime
        if self.RunSecondTime == False: # Initially false since is it not known whether user wants to do it twice
            self.dataFrame = dataFrame # Import set of data
            # INITIAL DATAFRAME PARSING            
        elif self.RunSecondTime == True: # Run the functions using a copy of the dataframe. 
            self.dataFrame = copydataFrame # Import set of copy data    

    def dropColumn(self): 
        print("\nThe column headings are as followed:\n{0}".format(', '.join(list(self.dataFrame)))) # Displays the column headings which the user can choose to remove 
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
                dropSelection = input("Please enter column {0} you want to remove (Case sensitive): ".format(i)) # Ensures readability e.g 1... 2.. etc.
            self.dataFrame.drop(columns=[dropSelection],inplace=True) # Start to drop coloumn(s), the use of inplace allows for modification of the dataframe without having to re-assign it             
        print(self.dataFrame) # Show the most up-to-date table after alteration(s) 
  
    def sortBy(self): # Add alpha./numerical order sorting functionality
        print("\nThe column headings are as followed:\n{0}".format(', '.join(list(self.dataFrame)))) # Displays the column headings which the user can choose to remove 
        ColumnSelected,AscendingInput = "",True
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
        self.dataFrame.sort_values(by=[ColumnSelected],ascending=AscendingOrder,inplace=True) # Now sort according to user chosen options
        print(self.dataFrame)

    def narrowSearch(self):
        UserChoice = ""
        while UserChoice != "a" and UserChoice != "b": # Input validation
            UserChoice = input("\nWould you like to narrow (delete) your searches based on:\n\n[A] Phone Name\n[B] Cost\n\nEnter choice: ").lower() # Prompt user for desired services

        if UserChoice == "a":
            phonenameChoice = input("\nPlease enter the phone name: ") # Set desired phone name
            self.dataFrame = self.dataFrame[~self.dataFrame.Name.str.contains(phonenameChoice,case=False)] # If the row contains a phone that the user has specified, it will be deleted
            # Unable to use inplace=True in this case as it has to be defined. Case=False means that the input need not case sensitive
            print(self.dataFrame)

        elif UserChoice == "b": # User can narrow according to cost paramater
            # Input Validation
            while True:
                try:
                    phonecostChoice = int(input("\nPlease enter the cost: ")) # Set desired phone price
                    break
                except ValueError:
                    print("Error, must be int.")  
            costNarrowChoice = ""                 
            while costNarrowChoice != "a" and costNarrowChoice != "b" and costNarrowChoice != "c":
                costNarrowChoice = input("\nWould you like to narrow (delete) phones that cost {0} [A], less than [B], or greater than? [C]: ".format(phonecostChoice)).lower() # Choice to choose between equal to, less than or greater than their cost input
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
        columnHeadings = ['Name','Storage_details','Camera_details','Battery_details','Processor']
        print("Please select a phone based on its:\n{0}".format(', '.join(list(columnHeadings))))
        columnTerm = ""
        while columnTerm not in columnHeadings: # Input validation for when user input =/= to any column headings
           columnTerm = input("Please enter desired column here (Case sensitive): ")        
        searchTerm = input("Please now enter the item you wish to explicitly search within {0}: ".format(columnTerm))
        self.dataFrame = self.dataFrame[self.dataFrame[columnTerm].str.contains(searchTerm,case=False)] # If the row contains a phone that the user has specified, it shown
        print(self.dataFrame)

    def initial(self):
        print("\nPlease select the desired function by its number: ")
        print("\n[1] Drop columns \n[2] Sort in alph./number order \n[3] Narrow Search\n[4] Specific Search") # Display list of options to choose from
        # Input validation (USING WHILE)
        user_input = 0
        while True:
            try:
                while user_input < 1 or user_input > 4: # Detects if user_input is within range (1,5)
                    user_input = int(input("\nEnter here: "))
                break
            except ValueError: # If user_input is not an integer it will be detected (ValueError)
                print("Error must be int.")
        # Drop columns
        if user_input == 1: 
            self.dropColumn()
            self.repeat() # Allows for repeatadability functionality
        # Sort in alph./number order
        elif user_input == 2: 
            self.sortBy()
            self.repeat()
        # Narrow searches        
        elif user_input == 3: 
            self.narrowSearch()
            self.repeat()
        # Specific search
        elif user_input == 4: 
            self.specificSearch()
            self.repeat()    
                      
    def returndataFrame(self):
        global dataFrameOne,dataFrameTwo # Define as global var for later use
        if self.RunSecondTime == False: # Initially, it is not apparent if the user need be comparing phones, so initially false
            dataFrameOne = self.dataFrame # Define that as one initially
            self.desiredChoice = "" # Set it to "unknown" state since its not clear whether user want to compare

            return dataFrameOne # Return it to main 
        elif self.RunSecondTime == True: # IF user wants to do a comparison, the main variable will now be using the copy of the dataFrame
            dataFrameTwo = self.dataFrame
            self.desiredChoice = "n" # Set to "n" since no need to ask the user again after they compared

            return dataFrameTwo # Return it to main

    def repeat(self): # Program repeatability 
        # Input validation (makes sure user enters y/n only)
        userRequest = ""
        while userRequest != "y" and userRequest != "n":
            userRequest = input("Would you like to further narrow/filter results? [Y/N]: ").lower()
        # Program will continue re-iterating the functions until the user is finished and enters n 
        if userRequest == "y":
            self.initial()
        elif userRequest == "n":
            print(self.dataFrame) # Print dataFrame state at the moment in time
            # STORE DATAFRAME AS VARIABLE THEN RETURN
            self.returndataFrame()

            # Input validation
            downloadResults = ""
            while downloadResults != "y" and downloadResults != "n":
                downloadResults = input("Would you like a copy of the current dataframe in Excel file format? [Y/N]: ").lower()
                if downloadResults == "y": # Prints a copy of the dataFrame to Excel format, path is explicitly defined for now - desktop
                    filepath = r'C:\Users\aaron\Desktop\FilteredMobileList.csv' # Temporary, r stands for "raw string"                                      
                    self.dataFrame.to_csv(filepath, index=False) # No need for numbering down the left side hence index = False
                    print("Saved to {0} .".format(filepath))
                    self.mobileComparison()
                else: # If user does not want to print it will exit.
                    self.mobileComparison()
                   # And ask for comparison   

# CLASS COMPARISON (COMPARE TWO DATAFRAMES)

    def mobileComparison(self): # Compare two dataframes together
        while self.desiredChoice != "y" and self.desiredChoice != "n":
            self.desiredChoice = input("\nWould you like to compare two phones side by side? [Y/N]: ").lower()
        if self.desiredChoice == "y":
            global RunSecondTime 
            RunSecondTime = True # Since it will run the functions again, it is set to true
            z = Filtering(RunSecondTime) # Input para since var will now be using copy 
            z.initial() # Run through the filtering process again etc...
        elif self.desiredChoice == "n":
            print("EXITING PROGRAM...")
            t.sleep(5)
            
# CALL CLASSES

# START MAIN FUNCTIONS
RunSecondTime = False # Since initially only it is run once, it is set to false
callClass = Filtering(RunSecondTime)
callClass.initial()

if RunSecondTime == True:
    finalComparison = p.concat([dataFrameOne,dataFrameTwo]) # Concatenate two dataframes into one for comparison
    filepath = r'C:\Users\aaron\Desktop\FilteredMobileListCOMPARISON.csv' # Temporary, r stands for "raw string"
    print("The final comparison is now saved to {0}. Have a nice day! :)".format(filepath))
    finalComparison.to_csv(filepath, index=False) # Create file as final comparison dataframe
