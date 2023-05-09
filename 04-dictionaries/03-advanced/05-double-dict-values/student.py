# Write your code here


def double_dict_values(dictionary):
    dictionary2 = {}
    for k, v in dictionary.items():
        dictionary2[k] = v*2
    return dictionary2
