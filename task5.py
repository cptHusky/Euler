# answer is 232792560
import time
from collections import deque

DIAPASON_MAX = 1000
single_number_delimiters = deque()
# global diapason_delimiters
diapason_delimiters = []
buf_delimiters = []
tim = []


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
            # print(f'{number} is prime')


def factor(number_var):
    single_number_delimiters.clear()
    i = 0
    while i < len(primes):
        if number_var != 1:
            if number_var % primes[i] == 0:
                single_number_delimiters.append(primes[i])
                number_var /= primes[i]
                i -= 1
        i += 1
    if not single_number_delimiters:
        single_number_delimiters.append(number_var)
    return single_number_delimiters


def add_delimiters(deq):
    global diapason_delimiters
    # print(deq)
    buf_delimiters = diapason_delimiters
    while deq:
        # d = deq.popleft()
        if deq[0] not in buf_delimiters:
            diapason_delimiters.append(deq.popleft())
        # print(diapason_delimiters)
        else:
            if diapason_delimiters[-1:] in buf_delimiters:
                buf_delimiters.remove(diapason_delimiters[-1:])




if __name__ == '__main__':
    t = time.time()
    number = 124954
    prime_gen(DIAPASON_MAX / 2)
    for number in range(2, DIAPASON_MAX + 1):
        # buffer_deque = factor(number)
        add_delimiters(factor(number))
        if number % 100 == 0:
            print(number)
    print(diapason_delimiters)
    print(time.time() - t, 'seconds spent\n\n')


        # print(type(buffer_list), '\n', buffer_list)








# --------------STUPID WAY--------------------
# if __name__ == '__main__':
#     t = time.time()
#     number = 0
#     while True:
#         number += DIAPASON_MAX
#         cond = True
#         for delimiter in range(2, DIAPASON_MAX + 1):
#             if cond:
#                 if number % delimiter != 0:
#                     cond = False
#         print(number)
#         if cond:
#             print(number, 'is result')
#             break
#     print(time.time() - t, 'seconds spent\n\n')


