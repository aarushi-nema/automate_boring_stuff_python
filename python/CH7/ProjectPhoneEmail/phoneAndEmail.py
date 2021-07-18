import re

#Create a regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #Area code
    (\s|-|\.)?                      #Separator
    (\d{3})                         #First three digits
    (\s|-|\.)                       #Separator
    (\d{4})                         #Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #Extension
)''')