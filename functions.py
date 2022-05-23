

def prime_gen(limit):
    status_gap = 10000
    status = 0
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
            if number > status:
                print(f'{number} out of {limit}')
                status += status_gap
    return primes
