from prime import is_prime

def test_small_primes():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)

def test_non_primes():
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(9)
    assert not is_prime(15)

def test_large_prime():
    assert is_prime(97)
