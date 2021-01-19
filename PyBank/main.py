#Import os and csv
import os
import csv

#Import the csv file
PyBankcsv = os.path.join("..", "Resources","budget_data.csv")

#Define the variables and how they are contained
dates = []
profit = []
monthly_change = []


#Start from the beginning of each variable
count = 0
initial_profit = 0
final_profit = 0
total_profit = 0
total_profit_change = 0


#Open PyBank with the CSV
with open(PyBankcsv, "w", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvreader)
    
    #Start the Loop
    for row in csvreader:
        
        # Count the number of months
        count = count + 1
        
        # Add each column from the start
        dates.append(row[0])
        
        # Add each profit to calculate total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        
        # Calculate avg change in profits
        final_profit = int(row[1])
        monthly_profit_changes = final_profit - initial_profit
        
        # Add monthly changes to list
        monthly_change.append(monthly_profit_changes)
        
        # Declare the list for the calculations
        total_profit_changes = total_profit_changes + monthly_profit_changes
        initial_profit = final_profit
        
        # Calculate avg change
        average_profit_change = (total_profit_changes/count)
        
        # Find the greatest increase and decrease in profits
        greatest_increase = max(monthly_changes)
        greatest_decrease = min(monthly_changes)
        
        # Find the dates of the increase and decrease
        increase_date = date[monthly_changes.index(greatest_increase)]
        decrease_date = date[monthly_changes.index(greatest_decrease)]
        
        print("Financial Analysis)")
        print("----------------------------")
        print("Total Months: " + str(count))
        print("Total Profits: " + "$" + str(total_profit))
        print("Average Change: " + "$" + str(int(average_profit_change)))
        print("Greatest Increase in Profits: " + str(increase_date) + "($" + str(greatest_increase) + ")")
        print("Greatest Decrease in Profits: " + str(decrease_date) + "($" + str(greatest_decrease) + ")")





