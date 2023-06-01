
def odd_keys_dict(dictionary):
    new_dict = dict()

    for k, v in dictionary.items():
        if k % 2 != 0:
            new_dict[k] = v

    return new_dict
