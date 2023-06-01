
def create_dictionary(keys, values):
    dictionary = dict()
    list = (zip(keys, values))

    for k, v in list:
        dictionary[k] = v
    return dictionary
