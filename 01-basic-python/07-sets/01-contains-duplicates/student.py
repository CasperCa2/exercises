# Write your code here


def contains_duplicates(ns):
    if len(ns) == set(ns):
        return True
    else:
        return False
