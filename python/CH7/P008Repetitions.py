#If you have a group that you want to repeat a specific number of times, fol-
#low the group in your regex with a number in curly brackets.

#Instead of one number, you can specify a range by writing a minimum,
#a comma, and a maximum in between the curly brackets. For example, the
#regex (Ha){3,5} will match HaHaHa, HaHaHaHa, and HaHaHaHaHa.

import re

laughRegex = re.compile(r'(Ha){3}')

laughMatchObject = laughRegex.search('HaHaHaHa')
print(laughMatchObject.group())

laughMatchObject2 = laughRegex.search('Ha')
if (laughMatchObject2 != None):
    print(laughMatchObject2.group())
else:
    print("No match object found")


#Python regular expressions are greedy by default, which means that in
#ambiguous situations they will match the longest string possible.
greedyLaughRegex = re.compile(r'(Ha){3,5}')
greedyLaugh = greedyLaughRegex.search('HaHaHaHaHa')
print(greedyLaugh.group())

#The non-greedy version of the curly brackets, which matches the shortest string possible, 
#has the closing curly bracket followed by a question mark.
nonGreedyLaughRegex = re.compile(r'(Ha){3,5}?')
nonGreedyLaugh = nonGreedyLaughRegex.search('HaHaHaHaHa')
print(nonGreedyLaugh.group())