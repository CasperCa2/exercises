
def is_increasing(ns):
    ms = ns[1:]
    for (i, k) in (zip(ns, ms)):
        if i > k:
            return False
    return True
