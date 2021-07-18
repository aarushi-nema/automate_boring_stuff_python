#While * means match zero or more, the + (or plus) means match one or
#more. Unlike the star, which does not require its group to appear in the
#matched string, the group preceding a plus must appear at least once. It is
#not optional.

import re

batRegex = re.compile(r'Bat(wo)+man')

batwomanMatchObject = batRegex.search('The Adventures of Batwoman')
print(batwomanMatchObject.group())

batwomanMatchObject2 = batRegex.search('The Adventures of Batwowowoman')
print(batwomanMatchObject2.group())

batwomanMatchObject3 = batRegex.search('The Adventures of Batman')
if (batwomanMatchObject3 != None):
    print(batwomanMatchObject3.group())
else:
    print("No match object found")

#If you need to match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+