from pr_tutorial.simple_functions import factorial
from pr_tutorial.simple_functions import is_prime


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_is_prime():
    '''Example of composite number'''
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(49) == False
    assert is_prime(73) == True
    assert is_prime(459) == False

