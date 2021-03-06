# DISPLAYS SIMPLE COMMANDS
# Ensure Pandas is installed firstly, Ensure you are on Python 3.9.1
import pandas as p

# Add print() to display data to any

mobile_dataFrame = p.read_csv('mobilephonetable.csv') # Reads CSV file, ensure csv file is in the same folder

mobile_dataFrame.head() # Prints the 1st 5 datasets by default unless specific
# Head means (top) to (bottom)

mobile_dataFrame.describe()
# Shows the count, mean, std, min, quartile values and max

mobile_dataFrame.drop(['ImageUrl','Camera_details'],axis=1).head()
# Removes/trims any column as one desires

mobile_dataFrame.isnull().sum()
# Counts for any invalid/empty cells 

mobile_dataFrame.value_counts(mobile_dataFrame['Cost']).plot.bar()
# Plot any bar graph under any column and display

mobile_dataFrame['Cost'].mean()
# Finds the mean cost for example

