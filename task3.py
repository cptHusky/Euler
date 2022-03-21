TEST_NUMBER = 600851475143
# TEST_NUMBER = 100


def prime_gen(limit):
    number = 1
    global primes
    primes = [2, ]
    while number < limit:
        number += 2
        is_prime = True
        for delimiter in range(2, number):
            if number % delimiter == 0:
                is_prime = False
        if is_prime:
            primes.append(number)
            print(f'{number} is prime')



if __name__ == '__main__':
    prime_gen(100000)
    i = len(primes) - 1
    while i > 0:
        if TEST_NUMBER % primes[i] == 0:
            print(primes[i])
            break
        i -= 1