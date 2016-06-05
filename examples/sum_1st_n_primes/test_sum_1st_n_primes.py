import pytest
from sum_of_first_n_primes import sum_of_first_n_primes

def test_given_1_returns_2():
  assert sum_1st_n_primes(1)==2

def test_given_2_returns_5():
  assert sum_1st_n_primes(2)==5
  
def test_negative_int_raises_ValueError():
    with pytest.raises(ValueError):
        x = sum_1st_n_primes(-4)
        
def test_param_not_an_int_raises_ValueError():
    with pytest.raises(ValueError):
        x = sum_1st_n_primes("foo")
