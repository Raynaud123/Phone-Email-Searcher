#! python3
#Script to find Phone Numbers(Europe) and email addresses on the clipboard

import pyperclip, re
#Making the regex for the phonenumbers and for the email
phone =re.compile(r'''(
((\+\d\d) | (00\d\d))?        #Land Code or Without (Belgium)
( )?                    #Potential Space after Land code
((0)?\d{3})             #First 3 digits with or without 0
(\s|-|\.)?              #Potential whitespace or other character
(\d{2})                 #2 digits
(\s|-|\.)?              #Potential whitespace or other character
(\d{2})                 #2 digits
(\s|-|\.)?              #Potential whitespace or other character
(\d{2})                 #2 digits
)''', re.VERBOSE) 

email=re.compile(r'''(
    [a-zA-z0-9._%+-]+            #First Words
    @                            #@ Symbol   
    [a-zA-z0-9._%+-]+            #Domain
    (\.[a-zA-z]{2,4})            #Dot-Something
)''',re.VERBOSE)            
#Reading the text and returning the values in a appropiate matter
text= str(pyperclip.paste())
emailMatches=[]
phoneMatches=[]
for groups in email.findall(text):
    emailMatches.append(groups[0])
for groups in phone.findall(text):
    if groups[8]==None:
        ' '.join([groups[1],groups[3],groups[5],groups[7]])
    elif groups[1]==' ':
        ' '.join([groups[2],groups[4],groups[6],groups[8]])
    elif groups[2]==' ':
        ' '.join([groups[1],groups[3],groups[5],groups[7],groups[9]])

