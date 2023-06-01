
def split_in_two(ns):
    half = len(ns) // 2
    first_half = ns[:half]
    second_half = ns[half:]
    return first_half, second_half
