# Write your code here

def cakes(eggs, butter, flour):
    rest_eggs = eggs // 5
    rest_butter = butter // 250
    rest_flour = flour // 250

    amount_cakes = min(rest_eggs, rest_butter, rest_flour)

    return amount_cakes
