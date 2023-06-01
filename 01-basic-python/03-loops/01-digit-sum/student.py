
def digit_sum(n):
    sum = 0
    for i in str(n):
        i = int(i)
        sum += i
    return sum


def last_digit(n):
    return n % 10


def remove_last_digit(n):
    return n // 10
