import math
def is_prime(num):
    """Checks if number is prime or not"""
    checks = True
    if num == 1 or num == 0 or num < 0:
        return False
    sqrt = int(math.sqrt(num))
    for i in range(2,sqrt+1):
        if num % i == 0:
            checks = False
            break
    return checks