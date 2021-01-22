# Import os and csv
import os
import csv

# Set CSV file
PyPoll_csv = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("------------------")

# Create variables to store lists
candidates = []
votes = []

# Open CSV for reading
with open(PyPoll_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Start reading the header row
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        votes.append(row[0])
        candidates.append(row[2])

    # Tally the total votes
    total_votes = (len(votes))
    print(f"Total Votes: {total_votes}")
    print("------------------")

    # Separate and count the votes by candidate
    khan = int(candidates.count("Khan"))
    correy = int(candidates.count("Correy"))
    li = int(candidates.count("Li"))
    otooley = int(candidates.count("O'Tooley"))

    # Display the total votes per candidate as a percentage
    khan_percentage = (khan/total_votes) * 100
    khan_percent = "{:.3f}".format(khan_percentage)
    correy_percentage = (correy/total_votes) * 100
    correy_percent = "{:.3f}".format(correy_percentage)
    li_percentage = (li/total_votes) * 100
    li_percent = "{:.3f}".format(li_percentage)
    otooley_percentage = (otooley/total_votes) * 100
    otooley_percent = "{:.3f}".format(otooley_percentage)

    print(f"Khan: {khan_percent}% ({khan})")
    print(f"Correy: {correy_percent}% ({correy})")
    print(f"Li: {li_percent}% ({li})")
    print(f"O'Tooley: {otooley_percent}% ({otooley})")

    # Loop the candidate votes total to find the winner
    if khan > correy > li > otooley:
        winner = "Khan"
    elif correy > khan > li > otooley:
        winner = "Correy"
    elif li > khan > correy > otooley:
        winner = "Li"
    elif otooley > khan > correy > li:
        winner = "O'Tooley"

    print("------------------")
    print(f"Winner: {winner}")
    print("------------------")