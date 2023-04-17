# Write your code here

import re


def ababa(string):
    return re.fullmatch(r"(.+)(.+)\1\2\1", string)

#\1 refered naar de eerste haakjes 
#\2 refered naar de tweede haakjes