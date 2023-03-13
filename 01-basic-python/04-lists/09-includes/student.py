# Write your code here


def includes(xs, ys):
    voorkomend = []
    for i in xs:
        voorkomend.append(i)
    for k in ys:
        if k not in voorkomend:
            return False
    return True
