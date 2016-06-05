import pytest
from is_prime import is_prime

def test_is_prime_1():
   assert isPrime(1) == False

def test_is_prime_2():
   assert isPrime(2) == True

def test_is_prime_509():
   assert isPrime(509) == True

def test_is_prime_511():
   assert isPrime(511) == False

# Note to students: continue writing additional tests
# for other values following the model above.

# The following tests check whether a ValueError is raised
# when the parameter is an inappropriate value

def test_raises_ValueError_when_n_is_float():
  pytest.raises(ValueError):
    x=isPrime(3.14159)
    
def test_raises_ValueError_when_n_less_than_1():
  pytest.raises(ValueError):
    x=isPrime(0)

# The following ensures that tests are run if/when the file is 
# executed in IDLE or via python test_is_prime.py at command line

if __name__ == '__main__':
    pytest.main()
