#all regex functions are in the re module
import re

#Passing a string value representing your regular expression to re.compile()
#returns a Regex pattern object (or simply, a Regex object).

# \d is a digit characater

#by putting an r before the first quote of the string value, you
#can mark the string as a raw string , which does not escape characters.
phoneNumRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#A Regex object’s search() method searches the string it is passed for any
#matches to the regex. The search() method will return None if the regex pat-
#tern is not found in the string. If the pattern is found, the search() method
#returns a Match object.
mo= phoneNumRegex.search('My number is 415-455-4242.')


print('Phone number found: ' + mo.group())

#adding parenthesis will create groups within the regular expression
