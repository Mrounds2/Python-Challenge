import csv

# Define the file path
file_path = "resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    header = next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # Check if the candidate is already in the dictionary
        if candidate_name in candidates:
            # Increment the candidate's vote count
            candidates[candidate_name] += 1
        else:
            # Add the candidate to the dictionary with an initial vote count of 1
            candidates[candidate_name] = 1

# Print the total number of votes cast
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate_name, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate_name}: {percentage:.3f}% ({votes})")

    # Check if the current candidate has more votes than the previous winner
    if votes > winner_votes:
        winner = candidate_name
        winner_votes = votes

print("-------------------------")

# Print the winner of the election
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
output_file = "election_results.txt"
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate_name, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate_name}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Results have been saved to {output_file}")
