# Write your code here


def target_sum(ns, target):
    for i in ns:
        for k in ns:
            if i + k == target:
                return True

    return False
