# Write your code here
import math


def middle(ns):
    x = len(ns) / 2
    x = math.ceil(x)
    x -= 1
    return ns[x]
