#The star or asterisk means match zero or more, the group
#that precedes the star can occur any number of times in the text. It can be
#completely absent or repeated over and over again.

import re

batRegex = re.compile(r'Bat(wo)*man')

batmanMatchObject = batRegex.search('The Adventures of Batman')
print(batmanMatchObject.group())

batwomanMatchObject = batRegex.search('The Adventures of Batwoman')
print(batwomanMatchObject.group())

batwomanMatchObject2 = batRegex.search('The Adventures of Batwowowowoman')
print(batwomanMatchObject2.group())

#If you need to match an actual star character, prefix the star in the regular expression with a backslash, \*