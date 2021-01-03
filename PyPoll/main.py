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
    candidate_list = []
    unique_candidate = []

    # Loop through the data
    for row in csvreader:
        
        # Count total votes
        total_votes = total_votes + 1

        # List of candidates 
        candidate_list.append(row[2])
    
    # Set unique canidate
    for x in set(candidate_list):
        unique_candidate.append(x)


#------------------------------

print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
print(f"{unique_candidate}: ")
