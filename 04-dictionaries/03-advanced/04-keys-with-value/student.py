# Write your code here


def keys_with_value(dictionary, value):
    new_list = []
    for k, v in dictionary.items():
        if v == value:
            new_list.append(k)
    return new_list
