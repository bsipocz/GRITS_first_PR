def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_prime(value):
    #this is a brute force way, probably a smarter way
    if value < 2:
        return False
    for i in range(2,value):
        if (value % i) == 0:
            #found a factor, number is not prime
            return False
    #didn't find a factore, number  is prime
    return True
