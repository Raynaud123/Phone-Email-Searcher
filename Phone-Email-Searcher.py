#! python3
#Script to find Phone Numbers(Europe) and email addresses on the clipboard

import pyperclip, re

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

text= str(pyperclip.paste())
emailMatches=[]
phoneMatches=[]
for groups in email.findall(text):
    emailMatches.append(groups[0])
for groups in phone.findall(text):
    if groups[1]==' ':
        ' '.join([groups[2]])
    elif groups[9]==' ':
        ' '.join([])
    else:
        ' '.join([])

