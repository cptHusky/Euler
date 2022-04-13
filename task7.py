import time


def prime_gen(amount):
    number = 1
    counter = 1
    primes = [2, ]
    while counter < amount:
        number += 2
        is_prime = True
        for n in range(counter):
            if number % primes[n] == 0:
                is_prime = False
        if is_prime:
            primes.append(number)
            counter += 1
            print(f'{number} is prime')
    return primes


if __name__ == '__main__':
    t = time.time()
    primes = prime_gen(10001)
    print(primes[10000])
    print(time.time() - t, 'seconds spent\n\n')
