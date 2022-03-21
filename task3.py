# answer is 6857
import time

TEST_NUMBER = 600851475143


def prime_gen(limit):
    number = 1
    counter = 1
    global primes
    primes = [2, ]
    while number < limit:
        number += 2
        is_prime = True
        for n in range(counter):
            if number % primes[n] == 0:
                is_prime = False
        if is_prime:
            primes.append(number)
            counter += 1
            print(f'{number} is prime')


if __name__ == '__main__':
    t = time.time()
    prime_gen(10000)
    i = len(primes) - 1
    while i > 0:
        if TEST_NUMBER % primes[i] == 0:
            print(primes[i])
            break
        i -= 1
    print(time.time() - t, '\n\n')
