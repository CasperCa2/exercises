def double_dict_values(dictionary):
    new_dict = {}

    for k, v in dictionary.items():
        new_dict[k] = v*2
    return new_dict
