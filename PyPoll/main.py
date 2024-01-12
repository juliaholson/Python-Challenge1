## PyPoll

import os
import csv

csvpath = os.path.join('PyPoll/election_data.csv')
## or alternatively: csvpath = os.path.join('/Users/juliaolson/Python-Challenge1/PyPoll/election_data.csv')
csvpath

election_data = []

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        election_data.append(row)

print(election_data)

## total votes
total_votes = len(election_data)
print(total_votes)

## list of canidates
can_list = []

for x in election_data:
    c = x[2]
    can_list.append(c)

print(can_list)

## total votes for charles
charles = []
for x in can_list:
    y = (x == 'Charles Casper Stockham')
    charles.append(y)

## number of votes
charles_votes = sum(charles)

## percent of votes
charles_pct = (charles_votes/total_votes)*100

print(charles_votes)
print(charles_pct)

## total votes for diana
diana = []
for x in can_list:
    y = (x == 'Diana DeGette')
    diana.append(y)

## number of votes
diana_votes = sum(diana)

## percent of votes
diana_pct = (diana_votes/total_votes)*100

print(diana_votes)
print(diana_pct)

## total votes for raymon
raymon = []
for x in can_list:
    y = (x == 'Raymon Anthony Doane')
    raymon.append(y)

## number of votes
raymon_votes = sum(raymon)

## percent of votes
raymon_pct = (raymon_votes/total_votes)*100

print(raymon_votes)
print(raymon_pct)

## results
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'Charles Casper Stockham: {charles_pct}% ({charles_votes})')
print(f'Diana DeGette: {diana_pct}% ({diana_pct})')
print(f'Raymon Anthony Doane: {raymon_pct}% ({raymon_votes}')
print('-------------------------')
print('Winner: Diana DeGette')
print('-------------------------')

## export as txt file
election_analysis = f'Total Votes: {total_votes}, Charles Casper Stockham: {charles_pct}% ({charles_votes}), Diana DeGette: {diana_pct}% ({diana_pct}), Raymon Anthony Doane: {raymon_pct}% ({raymon_votes}, Winner: Diana DeGette'
file = open('output.txt', 'w')
file.write(election_analysis)
file.close()
