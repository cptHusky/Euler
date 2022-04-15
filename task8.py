import re
from collections import deque

FILENAME = '1000DigitNumberS.txt'
AMOUNT_IN_SEQ = 13


def find_max_seq(big_set, seq_len):
    print(f'big set {big_set}\npredicted {len(big_set) - seq_len + 1} iterations\n')
    for i in range(len(big_set) - seq_len + 1):
        small_set = big_set[i:seq_len + i]
        print(f'iteration {i} with\nset {small_set}')
        numbers = deque(small_set)
        product = 1
        for m in range(seq_len):
            product *= int(numbers.pop())
        print(f'product {product}')
        products = {small_set: product}


if __name__ == '__main__':
    with open(FILENAME) as file:
        digits = file.read()
        sets = re.split('0', digits)
    file.close()

    sets[1] = '12345678123456'
    for i in range(len(sets)):
        if len(sets[i]) >= AMOUNT_IN_SEQ:
            print(f'set number {i} length {len(sets[i])}|{sets[i]}')
    print()

    for i in range(len(sets)-1):
        print(f'\nset number {i} length {len(sets[i])}')
        if len(sets[i]) >= AMOUNT_IN_SEQ:
            find_max_seq(sets[i], AMOUNT_IN_SEQ)
    # print('\n\n', products)
