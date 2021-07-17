#Suppose you want to separate the area code from the rest of the phone number.
#Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).

import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')

#you can use the group() match object method to grab the matching
#text from just one group.

# By passing the integer 1 or 2 to the group() match
#object method, you can grab different parts of the matched text.
print(mo.group(1))
print(mo.group(2))

#Passing 0 or nothing to the group() method will return the entire matched text
print(mo.group(0))
print(mo.group())

#If you would like to retrieve all the groups at once, use the groups()
#method—note the plural form for the name.
print(mo.groups())    #('415', '555-4242')

#Since mo.groups() returns a tuple of multiple values, you can use the
#multiple-assignment trick to assign each value to a separate variable
areaCode, mainNumber = mo.groups()
print("Area Code: ", areaCode)     #Area Code:  415
print("Main Number: ", mainNumber)   #Main Number:  555-4242

#Match a parenthesis in your text
#The \( and \) escape characters in the raw string passed to re.compile()
#will match actual parenthesis characters.
parenthesisPhoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mobileNumber = parenthesisPhoneNumberRegex.search('My phone number is (415) 555-4242.')
print(mobileNumber.group(1))   #(415)