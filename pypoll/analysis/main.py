import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')

csvpath=os.path.join('..', 'Resources','election_data.csv')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    candidates = {}

    
    for row in csvreader:
        if row [2] in candidates.keys():
            candidates[row[2]]+=1
        
        else: candidates[row[2]] = 1

    total = candidates.values()
    total_votes = sum(total)



print("Election Results")
print("-----------------")
print(f"Total votes: {int(total_votes)}")
print("----------------")









