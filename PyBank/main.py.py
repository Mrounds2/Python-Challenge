import csv

# Set up file path
file_path = "resources/budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the net total amount of profit/losses
        net_total += int(row[1])

        # Calculate the change in profit/losses
        current_profit_loss = int(row[1])
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            total_change += change

            # Check for the greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change

            # Check for the greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change

        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1)

# Format the output
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

# Print the output
print(output)

# Write the output to a text file
with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write(output)