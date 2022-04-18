import re
from collections import deque

FILENAME = '1000DigitNumber.txt'
AMOUNT_IN_SEQ = 13
products = {}


def find_max_seq(big_set, seq_len):
    global products
    # print(f'big set {big_set}\npredicted {len(big_set) - seq_len + 1} iterations\n')
    for i in range(len(big_set) - seq_len + 1):
        small_set = big_set[i:seq_len + i]
        # print(f'iteration {i} with\n{small_set}')
        numbers = deque(small_set)
        product = 1
        for m in range(seq_len):
            product *= int(numbers.pop())
        # print(f'product is {product}')
        products[small_set] = product


if __name__ == '__main__':
    with open(FILENAME) as file:
        digits = file.read()
        sets = re.split('0', digits)
    file.close()
    for i in range(len(sets)-1):
        # print(f'\nset number {i} length {len(sets[i])}')
        if len(sets[i]) >= AMOUNT_IN_SEQ:
            find_max_seq(sets[i], AMOUNT_IN_SEQ)
    print(max(products.items(), key=lambda k: k[1]))
