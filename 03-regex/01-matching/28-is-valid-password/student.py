# Write your code here
import re


def is_valid_password(string):
    needed_regexes = [
        r'.{12}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]',

    ]

    notneeded_regexes = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'

    ]

    for regex in needed_regexes:
        if not re.search(regex, string):
            return False

    for regex in notneeded_regexes:
        if re.search(regex, string):
            return False

    return True
