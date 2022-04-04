# answer is 232792560
import time
from collections import deque
from functions import prime_gen

DIAPASON_MAX = 20
single_number_delimiters = deque()
diapason_delimiters = []
buf_delimiters = []


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
    buf_delimiters.clear()
    buf_delimiters.extend(diapason_delimiters)
    while deq:
        d = deq.pop()
        if d in buf_delimiters:
            buf_delimiters.remove(d)
        else:
            diapason_delimiters.append(d)


if __name__ == '__main__':
    t = time.time()
    result = 1
    primes = prime_gen(DIAPASON_MAX / 2)
    for number in range(2, DIAPASON_MAX + 1):
        add_delimiters(factor(number))
        if number % 1000 == 0:
            print(number)
    for i in range(len(diapason_delimiters)):
        result *= diapason_delimiters[i]
    print(f'result {result}')
    print(time.time() - t, 'seconds spent\n\n')


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
#
