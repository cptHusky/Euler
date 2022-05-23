from functions import prime_gen

if __name__ == '__main__':
    sum = 0
    primes = prime_gen(2000000)
    for i in range(len(primes)):
        sum += primes[i]
    print(sum)