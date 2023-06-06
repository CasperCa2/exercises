

def merge_dictionaries(d1,d2,merge_function):
    dictionary = dict(d1)
    for k,v in d2.items():
        if k not in dictionary:
            dictionary[k] = v
        else:
            dictionary[k] = merge_function(d1[k],d2[k])

            
    return dictionary