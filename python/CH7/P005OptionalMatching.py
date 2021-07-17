#This feature is for patterns that you want to match only optionally.
#That is, the regex should find a match whether or not that bit of text is there.
#The ? character flags the group that precedes it as an optional part of the pattern.

import re

#The (wo)? part of the regular expression means that the pattern wo is an optional group
#The regex will match text that has zero instances or
#one instance of wo in it
batRegex = re.compile(r'Bat(wo)?man')
batman = batRegex.search('The Adventures of Batman')
print(batman.group()) #Batman

batwoman = batRegex.search('The Adventures of Batwoman')
print(batwoman.group())  #Batwoman

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneNumberAreaCode = phoneRegex.search('My number is 415-555-4242')
print(phoneNumberAreaCode.group())

phoneNumberNoAreaCode = phoneRegex.search('My number is 555-4242')
print(phoneNumberNoAreaCode.group())