#The . (or dot) character in a regular expression is called a wildcard and will
#match any character except for a newline.

import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

#Sometimes you will want to match everything and anything.

nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
nameMatchObject = nameRegex.search('First name: Aarushi Last name: Nema')
print(nameMatchObject.group(1))
print(nameMatchObject.group(2))

#The dot-star uses greedy mode: It will always try to match as much text as
#possible. To match any and all text in a nongreedy fashion, use the dot, star,
#and question mark ( .*? )