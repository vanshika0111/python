# regular expressions (built-in module)

"""
Functions in re:
    1. findall: finds a specific string and returns
    2. search: returns a match object
    3. split: splits the data
    4. sub:
    5. finditer:
"""

# raw string: print("\n")  --> escapes a line
#             print(r'\n') --> prints \n
import re

mystr = '''
    Name: Solace
    Roll number: 18
    Qualification: Higher secondary education 
    Currently: Graduate student
    Email: solace12@gmail.com
    Country: India
'''

# -------------META CHARACTERS-----------
# CASE 1
# patt = re.compile(r'higher')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)
#     print(mystr[20:30])

# CASE 2
# patt = re.compile(r'.')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 3
# patt = re.compile(r'.and')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 4
# patt = re.compile(r'^and')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 5
# patt = re.compile(r'and$')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 6
# patt = re.compile(r'ai*')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 7
# patt = re.compile(r'ai+')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 8
# patt = re.compile(r'ai{2}')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 9
# patt = re.compile(r'(ai){2}')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 10
# patt = re.compile(r'(ai){1}|Fax')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# -------------SPECIAL CHARACTERS-----------

# CASE 1
# patt = re.compile(r'\AName')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 2
# patt = re.compile(r'\bName')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)

# CASE 3
# patt = re.compile(r'Name\b')
# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)