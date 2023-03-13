# Write your code here


def contains_duplicates(ns):

    if len(set(ns)) < len(ns):
        return True
    else:
        return False
