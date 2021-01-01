# Import csv data to read
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..', '..','..', 'nu_bootcamp', 'nu-chi-data-pt-11-2020-u-c', 'Homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

# Open and read the CSV file
with open(csvpath) as csvfile:

    # Split the data by a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove the header
    header = next(csvreader)

    # Assign values to variables
    total_months = 0
    total_revenue = 0
    
    # Loop through the data
    for row in csvreader:
        
        # Count total months
        total_months = total_months + 1

        # Add total revenue
        total_revenue = total_revenue + int(row[1])



    #--------------------------------

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
