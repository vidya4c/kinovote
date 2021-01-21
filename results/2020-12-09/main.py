import csv
import pyrankvote as pv
import re

def ranked_vote(table, places):
    themes = table[0]
    themes = [re.search(r'\[(.*)\]$', theme)[1] for theme in themes]
    themes = [pv.Candidate(theme) for theme in themes]

    print('Themes:')
    for theme in themes: print(f'\t{theme.name}')
    print()

    choices_text = ['1st Choice', '2nd Choice', '3rd Choice'] + [str(i) + 'th Choice' for i in range(4,len(themes)+1)]

    raw_votes = [line[1:-1] for line in lines[1:]]
    votes = []
    for raw_vote in raw_votes:
        vote = []
        for ct in choices_text:
            try:
                i = raw_vote.index(ct)
                vote.append(themes[i])
            except ValueError: pass
        votes.append(vote)
    
    print('Votes:')
    for i, vote in enumerate(votes):
        print(f'\t{i+1}.', end='')
        print(', '.join([choice.name for choice in vote]))
    print()

    ballots = [pv.Ballot(ranked_candidates=vote) for vote in votes]

    election_result = pv.single_transferable_vote(themes, ballots, places)

    print(election_result)

    

with open('results.csv') as f:
    lines = list(csv.reader(f))

Q1 = [line[1:-2] for line in lines]

ranked_vote(Q1, 3)

