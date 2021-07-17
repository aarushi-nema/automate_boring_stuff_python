#The | character is called a pipe. You can use it anywhere you want to match one
#of many expressions. 

import re

heroRegex = re.compile(r'Batman|Tina Frey')
#When both Batman and Tina Fey occur in the searched string, the first
#occurrence of matching text will be returned as the Match object.
heroName = heroRegex.search('Batman and Tina Frey')
print(heroName.group())

heroName = heroRegex.search('Tina Frey and Batman')
print(heroName.group())

#You can also use the pipe to match one of several patterns as part of
#your regex
batVehicleRegex = re.compile(r'Bat(man|mobile|copter|bat)')
batVehicle = batVehicleRegex.search('The Batmobile has lost its wheels')
#The method call mo.group() returns the full matched text 'Batmobile',
#while mo.group(1) returns just the part of the matched text inside the first
#parentheses group
print(batVehicle.group())
print(batVehicle.group(1))

#If you need to match an actual pipe character, escape it with a backslash, like \|.
