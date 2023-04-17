
# Write your code here

import re


def is_number(string):
    return re.fullmatch('[0-9]+(\.[0-9]+)?', string)
# return re.match("[0-9]+(\.[0-9]+)?", string)
