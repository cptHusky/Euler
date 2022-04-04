

def prime_gen(limit):
    number = 1
    counter = 1
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
    return primes
