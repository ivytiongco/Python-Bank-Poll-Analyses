# import the os module to allow us to create file paths across operating systems
import os

# module for reading CSV files
import csv

# set path for file
polldata = os.path.join('Desktop/Python-Bank-Poll-Analyses/PyPoll', 'election_data.csv')

# open the CSV
with open(polldata) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # read the header row first
    csv_header = next(csvreader)
    
    # variables
    id = []
    candidate = []
    percentage = []
    
    # read each row of data after the header
    for row in csvreader:
        
        # add 
        id.append(row[0])
        candidate.append(int(row[1]))

# print first lines of results
    print(" ")
    print("Financial Analysis")
    print("------------------------------")

# total number of months included in the dataset
#    print("Total Months: " + str(len(date)))
    print(f"Total Months: {len[date]}")

# net total amount of Profit/Losses
    print("Total: $" + str(sum(amount)))

# find difference between rows
    for i in range(1, len(amount)):
        amount_change.append(amount[i] - amount[i-1])

# average of difference between rows
        avg_amount_change = sum(amount_change)/len(amount_change)

# maximum of amount change is greatest increase in profits
        max_amount_change = max(amount_change)

# greatest decrease in losses (date and amount)
        min_amount_change = min(amount_change)

#find dates
        max_amount_change_date = str(date[amount_change.index(max(amount_change))+ 1])
        min_amount_change_date = str(date[amount_change.index(min(amount_change))+ 1])

# print avg, greatest inc, greatest dec
    print("Average Change: $" + str(round(avg_amount_change,2)))
    print("Greatest Increase in Profits: " + max_amount_change_date + " ($" + str(max_amount_change) + ")")
    print("Greatest Decrease in Losses: " + min_amount_change_date + " ($" + str(min_amount_change) + ")")

# set path for text file of results
output_path = os.path.join('Desktop/Python-Bank-Poll-Analyses/PyPoll', "pypoll.txt")

# create text file and print results to it
f = open(output_path, 'w')
print(" ", file = f)
print("Financial Analysis", file = f)
print("------------------------------", file = f)
print("Total Months: " + str(len(date)), file = f)
print("Total: $" + str(sum(amount)), file = f)
print("Average Change: $" + str(round(avg_amount_change,2)), file = f)
print("Greatest Increase in Profits: " + max_amount_change_date + " ($" + str(max_amount_change) + ")", file = f)
print("Greatest Decrease in Losses: " + min_amount_change_date + " ($" + str(min_amount_change) + ")", file = f)