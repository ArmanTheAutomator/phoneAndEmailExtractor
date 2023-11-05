#! python3
# phoneAndEmail
# This program will parse through any block of text that you copy to your
# clipboard, and extract any/all phone numbers and emails from it.
# Simply copy any block of text to your clipboard, and run this program.
# When complete, the program will then copy the phone numbers & emails back
# to the clipboard.

import pyperclip, re


# Phone number regex 

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


# Create email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 # username
    @                                 # @ symbol
    [a-zA-Z0-9.-]+                    # domain name
    (\.[a-zA-Z]{2,4})                 # dot-something
    )''', re.VERBOSE)


# Find matches in clipboard text.

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    

# Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers of email addresses found.')

    

