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
    # special cases
    if value < 2:       return False
    if value == 2:      return True
    if value % 2 == 0:  return False
    # step over odd numbers up to maximum possible factor for a composite
    i = 3
    while i*i <= value: 
        if value % i == 0:
            return False
        i+=2
    return True
