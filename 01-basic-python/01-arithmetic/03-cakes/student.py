# Write your code here

def cakes(eggs, butter, flour):
    eggs = eggs // 5
    butter = butter // 250
    flour = flour // 250
    amount_of_cakes = min(eggs, butter, flour)
    return amount_of_cakes
