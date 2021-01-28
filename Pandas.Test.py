# Ensure Pandas is installed firstly
import pandas as p

# Assign the table of CSV content to a variable, dataFrame
dataFrame = p.read_csv('mobilephone_table.csv') # Reads CSV file, ensure csv file is in the same folder 

n = 10 
print(dataFrame.head(n)) # It will print the top (first) 10 rows of the dataFrame, aka CSV file.
#.tail() will print from bottom to top

