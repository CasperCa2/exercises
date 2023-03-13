# Write your code here


def add_indices(lijst):
    new_list = []
    for i in range(len(lijst)):
        new_list.append(i)

    antwoord = list(zip(new_list, lijst))
    return antwoord
