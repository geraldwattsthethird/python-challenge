# Import os and csv
import os
import csv

# Set CSV file

PyPoll_csv = os.path.join("Resources", "election_data.csv")

# Create variables to store lists

candidate = []
votes = []
voters = []
votepercentage = []

# Count the votes

count = 0

# Open CSV for reading

with open(PyPoll_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Set the loops

    for row in csv_reader:

        count = count + 1
        candidate.append(row[2])

    for x in set(candidate):
            
        unique_candidate.append(x)
        y = candidate.count(x)
        votes.append(y)
        z = (y/count)*100
        votepercentage.append(z)

    
