import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')

csvpath=os.path.join('..', 'Resources','election_data.csv')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    line = next(csvreader,None) 



    candidates = {}
    total = candidates.values()
    total_votes = sum(total)
    list_candidates = candidates.keys()

    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        
        else: candidates[row[2]] = 1

        total = candidates.values()
        total_votes = sum(total) 

        list_candidates = candidates.keys()

    

        votes_per = [f'{(x/total_votes)*100:}%' for x in candidates.values()]
    




    winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
    print(winner)



print("Election Results")
print("-----------------")
print(f"Total votes: {int(total_votes)}")
print("-----------------")
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate}, {vote}, {votes_per[i]}')
    i+=1
print("---------------")
print(f" Winner: {winner}")
print("---------------")










