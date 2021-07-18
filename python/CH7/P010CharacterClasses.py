# \d : Any numberic digit from 0 to 9
# \D : Any character that is not a numeric digit
# \w : Any letter, numeric digit, or the underscore chracter
# \W : Any character that is not a letter, numeric digit, or underscore character
# \s : Any space, tab, or newline character
# \S : Any character that is not a space, letter, or newline character

import re

xmasRegex = re.compile(r'\d+\s\w+')
xmasSong = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 patridge')
print(xmasSong)

#There are times when you want to match a set of characters but the short-
#hand character classes ( \d , \w , \s , and so on) are too broad. You can define
#your own character class using square brackets.

#the character class [aeiouAEIOU] will match any vowel
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelString = vowelRegex.findall('Robocop eats baby food. BABY FOOD')
print(vowelString)

#You can also include ranges of letters or numbers by using a hyphen.
#For example, the character class [a-zA-Z0-9] will match all lowercase letters,
#uppercase letters, and numbers.

#By placing a caret character ( ^ ) just after the character class opening
#bracket, you can make a negative character class. A negative character class
#will match all the characters that are not in the character class.
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantString = consonantRegex.findall('Robocop eats baby food. BABY FOOD')
print(consonantString)

#You can also use the caret symbol ( ^ ) at the start of a regex to indicate that
#a match must occur at the beginning of the searched text.
beginsWithHello = re.compile(r'^Hello')
helloString = beginsWithHello.search('Hello World!')
noHelloString = beginsWithHello.search('He said hello')
print(helloString)
if (noHelloString == None):
    print('String does not begin with hello')
else:
    print(noHelloString)

#you can put a dollar sign ( $ ) at the end of the regex to indicate the string must end
#with this regex pattern.
endsWithDigit = re.compile(r'\d$')
digitString = endsWithDigit.search('I like the number 32')
noDigitsString = endsWithDigit.search('42 is my favourite number')
print(digitString)
if(noDigitsString == None):
    print('No digit at the end of the string')
else:
    print(noDigitsString)