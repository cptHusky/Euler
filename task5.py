# answer is 232792560
import time

DIAPASON_MAX = 20
prime_delimiters_single = []
prime_delimiters_diapason = []


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
    number = 0
    while True:
        number += DIAPASON_MAX
        cond = True
        for delimiter in range(2, DIAPASON_MAX + 1):
            if cond:
                if number % delimiter != 0:
                    cond = False
        print(number)
        if cond:
            print(number, 'is result')
            break
    print(time.time() - t, 'seconds spent\n\n')
