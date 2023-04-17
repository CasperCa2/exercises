# Write your code here

import re


def only_digits(string):
    return re.fullmatch("\d*", string)


# [1234567890]* is also and option
