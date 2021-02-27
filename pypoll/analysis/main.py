import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')

csvpath=os.path.join('..', 'Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

votes = 0
vote_count = []
candidates = []



