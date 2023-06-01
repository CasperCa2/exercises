# Write your code here

def is_prime(n):
    for k in range(2, n-1):
        if n % k == 0:
            return False
    return n > 1
