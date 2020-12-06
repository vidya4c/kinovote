import csv
import pyrankvote as pv
import re

with open('results/2020-12/themes.csv') as f:
    lines = list(csv.reader(f))

themes = lines[0][1:-1]
themes = [re.search(r'\[(.*)\]$', theme)[1] for theme in themes]
themes = [pv.Candidate(theme) for theme in themes]

choices_text = ['1st Choice', '2nd Choice', '3rd Choice'] + [str(i) + 'th Choice' for i in range(4,len(themes))]

raw_votes = [line[1:-1] for line in lines[1:]]

raw_vote = raw_votes[0]

votes = []
for raw_vote in raw_votes:
    vote = []
    for ct in choices_text:
        try:
            i = raw_vote.index(ct)
            vote.append(themes[i])
        except ValueError: pass
    votes.append(vote)

ballots = [pv.Ballot(ranked_candidates=vote) for vote in votes]

election_result = pv.single_transferable_vote(themes, ballots, 2)

print(election_result)