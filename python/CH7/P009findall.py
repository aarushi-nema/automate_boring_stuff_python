#While search() will return a Match object of the first matched text
#in the searched string, the findall() method will return the strings of every
#match in the searched string.

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

phoneMatchObject =  phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(phoneMatchObject)

#If there are groups in the regular expression, then findall() will return
#a list of tuples.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneMatchObject2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(phoneMatchObject2)