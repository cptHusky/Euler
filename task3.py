# answer is 6857
import time
from functions import prime_gen

TEST_NUMBER = 600851475143


if __name__ == '__main__':
    t = time.time()
    primes = prime_gen(10000)
    i = len(primes) - 1
    while i > 0:
        if TEST_NUMBER % primes[i] == 0:
            print(primes[i])
            break
        i -= 1
    print(time.time() - t, 'seconds spent\n\n')
