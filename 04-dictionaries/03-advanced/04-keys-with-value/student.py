
def keys_with_value(dictionary, value):
    list = []
    for k, v in dictionary.items():
        if v == value:
            list.append(k)
    return list
