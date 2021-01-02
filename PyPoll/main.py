# Import csv data to read
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# Open and read the CSV file
with open(csvpath) as csvfile:

    # Split the data by a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove the header
    header = next(csvreader)

    # Assign values to variables
    total_votes = 0

    # Loop through the data
    for row in csvreader:
        
        # Count total months
        total_votes = total_votes + 1


#------------------------------

print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")