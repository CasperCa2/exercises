# Write your code here

import math


def median(ns):

    ns.sort()
    if len(ns) % 2 == 0:  # even
        g1 = int(len(ns) / 2)
        g2 = int(g1 - 1)
        mediaan = (ns[g1] + ns[g2]) / 2
    else:
        midden = int(len(ns) / 2)
        mediaan = ns[midden]

    return mediaan
