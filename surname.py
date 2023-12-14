###
#Given a test string, , write a RegEx that matches

#under the following conditions:

#must start with Mr., Mrs., Ms., Dr. or Er..
#The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
###
Regex_Pattern = r'^(Mr|Mrs|MS|Dr|Er)\.[a-zA-Z]+$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
