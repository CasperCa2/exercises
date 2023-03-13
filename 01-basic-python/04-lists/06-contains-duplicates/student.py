# Write your code here


def contains_duplicates(xs):
    gevonden = []
    for i in xs:
        if i in gevonden:
            return True
        else:
            gevonden.append(i)
    return False
