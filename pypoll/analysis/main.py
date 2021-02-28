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



## I wasn't able to figure out exporting a text file with the PyBbnk or Pypoll results in time.  
## Below was my last attempt of code script below, I may be confused and thought that I was originally writing a CSV file, which is not what was asked. I will need to look into this again.

with open(output_path, "w", newline='') as textfile:
    print("Election Results", file=textfile)
    print("------------------", file=textfile)
    print(f"Total Votes: {int(total_votes)}", file=textfile)
filewriter.write ("------------------", file=textfile)
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate}, {vote}, {votes_per[i]}', file=textfile)
    i+=1    
filewriter.write("------------------", file=textfile)

filewriter.write("------------------", file=textfile)
filewriter.write(f"Winner: {winner}", file=textfile)
filewriter.write("-------------------", file=textfile)

with open(output_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)








