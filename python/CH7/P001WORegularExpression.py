#Finding patterns of text without Regular Expressions

#Say you want to find a phone number in a string. You know the pattern:
#three numbers, a hyphen, three numbers, a hyphen, and four numbers.
# Here’s an example: 415-555-4242.
# Let’s use a function named isPhoneNumber() to check whether a string
# matches this pattern, returning either True or False . 

#Function isPhoneNumber checks whether a given string (text) matches the patterns of a US phone number
def isPhoneNumber(text):
    #check if the string has a length of 12
    if(len(text)!=12):
        return False
    
    #check if the first three characters are numbers
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    
    #check if the 4th character is a hyphen
    if text[3] != '-':
        return False

    #check if the next three characters are numbers
    for i in range (4,7):
        if not text[i].isdecimal():
            return False

    #check if the 4th character is a hyphen
    if text[7] != '-':
        return False

    #check if the last four characters are numbers
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    
    #return true if all the above conditions are not met
    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

#now we'll extract the phone number from a larger string
message= 'Call me at 415-555-4242. 415-555-4242 is my office number'

#run a loop through the length of the string
for i in range (len(message)):
    #chunk: stores the next 12 characters from the current character 
    #note that if the number of characters left in the string is <12 then it takes the remaining characters
    chunk= message[i:i+12]
    #check if the 12 characters in chunk represent a phone number
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
#once you are done looping through message, print 'Done'        
print('Done')

# Concepts learnt:
# 1. The len() function returns the length of the object. This is generally used to find the length of a String 
# 2. Python String isdecimal() function returns True if all the characters in the string are decimal characters, otherwise      False. If the string is empty then this function returns False.
