## modules
import os
import csv

## read in CSV (with header)
csvpath = os.path.join('PyBank/budget_data.csv')
csvpath

budget_data = []

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        budget_data.append(row)
        print(row)

## total number of months in dataset (total months)
total_months = len(budget_data)
print(total_months)

## create a new list containing only the profit/loss column
pro_los_col = []

for x in budget_data:
    pl = x[1]
    pro_los_col.append(pl)

print(pro_los_col)

## convert pro_lost_col to integers 
pro_los_int = []

for x in pro_los_col:
    i = int(x)
    pro_los_int.append(i)

print(pro_los_int)

## net total amount of profit/losses over the entire period (total)
total = sum(pro_los_int)
print(total)

## calculate changes in profit/losses over the entire period
pro_los_change = []
for x in pro_los_int:
    x_index = pro_los_int.index(x)
    if x_index+1 < len(pro_los_int):
        next_x = pro_los_int[x_index+1]
        diff = x - next_x
        pro_los_change.append(diff)

print(pro_los_change)

## calculate average of changes in profit/losses (average change)
average_change = sum(pro_los_change)/len(pro_los_change)
print(average_change)

# calculate greatest increase in profits over the entire period (greatest increase)
greatest_increase_in_profits = max(pro_los_change)
print(greatest_increase_in_profits)

# calculate greatest decrease in profits over the entire period (greatest decrease)
greatest_decrease_in_profits = min(pro_los_change)
print(greatest_decrease_in_profits)

## results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: $-{average_change}')
print(f'Greatest Increase in Profits: Aug-16 (${greatest_increase_in_profits}')
print(f'Greatest Decrease in Profits: Feb-14 (${greatest_decrease_in_profits})')

financial_analysis = f'Total Months: {total_months}, Total: ${total}, Average Change: $-{average_change}, Greatest Increase in Profits: Aug-16 (${greatest_increase_in_profits}), Greatest Decrease in Profits: Feb-14 (${greatest_decrease_in_profits})'
file = open('output.txt', 'w')
file.write(financial_analysis)
file.close()

git add