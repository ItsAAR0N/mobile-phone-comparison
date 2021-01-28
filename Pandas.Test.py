# Ensure Pandas is installed firstly
import pandas as p

# Assign the table of CSV content to a variable, dataFrame
dataFrame = p.read_csv('mobilephone_table.csv') # Reads CSV file, ensure csv file is in the same folder 

print(dataFrame.head()) # It will print the top 5 lines of the dataFrame, aka CSV file.
#.tail() will print from top to bottom. 

