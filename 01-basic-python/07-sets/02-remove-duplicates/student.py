# Write your code here


def remove_duplicates(xs):
    list = []
    found = set()
    for k in xs:
        if k not in found:
            list.append(k)
            found.add(k)
    return list
