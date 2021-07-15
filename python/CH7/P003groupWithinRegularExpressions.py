#Suppose you want to separate the area code from the rest of the phone number.
#Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).

import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')

#you can use the group() match object method to grab the matching
#text from just one group.
print(mo.group(1))
print(mo.group(2))
