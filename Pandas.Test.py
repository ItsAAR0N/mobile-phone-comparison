# Ensure Pandas is installed firstly, Ensure you are on Python 3.9.1
import pandas as p

# Assign variables
n = 10
# Assign the table of CSV content to a variable, dataFrame
dataFrame = p.read_csv('mobilephone_table.csv') # Reads CSV file, ensure csv file is in the same folder 

# .head() will print from top to bottom
# .tail() will print from bottom to top

# This will find the first 10 phones that cost 4,999 which is then been assigned a variable
cost5000 = dataFrame[(dataFrame["Cost"] == '7,999')]

print(cost5000.head(n))
# Will print the first 10 phones
#cost5000.to_csv('cost-5000.csv') # Creates a new CSV with the parameters

# You can also do len() to get no.
print("Test")

