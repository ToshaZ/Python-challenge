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
    candidate_votes = []
    percent_vote = []
    winner_votes = 0
    winner_candidate= ""

    # Loop through the data
    for row in csvreader:
        
        # Count total votes
        total_votes = total_votes + 1

        # List of candidates 
        candidate_list.append(row[2])
    
    # Set unique canidate
    for x in set(candidate_list):
        unique_candidate.append(x)

        # Count votes per canidate
        votes = candidate_list.count(x)
        candidate_votes.append(votes)

        # Gather percent of votes per candidate
        percent = (votes/total_votes)*100
        percent_vote.append(percent)

#------------------------------

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------")
#Format output
for i in range(len(unique_candidate)):
            print(f"{unique_candidate[i]}: {percent_vote[i]}% ({candidate_votes[i]})")

            # Determine the Winner
            if (winner_votes < candidate_votes[i]):
               winner_votes = candidate_votes[i]
               winner_candidate = unique_candidate[i]

print("-----------------------------------")
print(f"Winner: {winner_candidate}")
print("-----------------------------------")