#! python3
#Script to find Phone Numbers(Europe) and email addresses on the clipboard

import pyperclip, re

Phone =re.compile(r'''(
((\+\d\d) | (0) | (00\d\d))        #Land Code or Without (Belgium)
( )?                    #Potential Space after Land code
(\d{3})                 #First 3 digits
(\s|-|\.)?              #Potential whitespace or other character
(\d{2})                 #2 digits
(\s|-|\.)?              #Potential whitespace or other character
(\d{2})                 #2 digits
(\s|-|\.)?              #Potential whitespace or other character
(\d{2})                 #2 digits
)''', re.VERBOSE) 

Email=re.compile(r'''(
    [a-zA-z0-9._%+-]+            #First Words
    @                            #@ Symbol   
    [a-zA-z0-9._%+-]+            #Domain
    (\.[a-zA-z]{2,4})            #Dot-Something
)''',re.VERBOSE)            

text= str(pyperclip.paste())