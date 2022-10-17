"""
Riddler Classic
Today I happen to be celebrating the birthday of a family member, 
which got me wondering about how likely it is for two people in a room 
to have the same birthday.

Suppose people walk into a room, one at a time. Their birthdays happen 
to be randomly distributed throughout the 365 days of the year (and no 
one was born on a leap day). The moment two people in the room have the 
same birthday, no more people enter the room and everyone inside celebrates 
by eating cake, regardless of whether that common birthday happens to be today.

On average, what is the expected number of people in the room when they eat cake?

Extra credit: Suppose everyone eats cake the moment three people in the room have 
the same birthday. On average, what is this expected number of people?

https://fivethirtyeight.com/features/can-you-salvage-your-rug/


RESOURCES
https://www.probabilisticworld.com/birthday-problem-analytic-solution/
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html#r7bf2e556f491-1
https://carpentries-incubator.github.io/python-interactive-data-visualizations/08-publish-your-app/index.html


"""

### Numerical Solution ###
import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

def bday_match(same_bday_limit=2,days=365):
    
    bday_index = []
    days = 365
    partygoer = 0
    same_bday_count = 0
    
    while same_bday_count < same_bday_limit:

        partygoer = partygoer + 1
        bday = random.randrange(days)

        bday_index.append(bday)

        same_bday_count = bday_index.count(bday)
    
    return partygoer

limit_test_range = 12
test_results = {}

#first set match count criteria
for test in range(limit_test_range):
    trials = 50
    parties = 100
    bday_limit = test

    trial_list = []

    for trial in range(trials):
        party_list = []
        for party in range(parties):
            party_list.append(bday_match(same_bday_limit=bday_limit))

        trial_list.append(sum(party_list)/len(party_list))

    trial_array = np.array(trial_list)
    k2, p = stats.normaltest(trial_array)
    alpha = 0.05

    if p < alpha:
        chart_note = 0
    else:
        chart_note = 1

    print(f'Average number of arrivals before {bday_limit} matching birthdays: {np.mean(trial_array)} {chart_note}')

    test_results[test] = [np.mean(trial_array),chart_note]

print(test_results)
