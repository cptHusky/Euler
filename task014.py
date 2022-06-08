MAX = 0


def collatz_iterations(n):
    iter = 0
    # print(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2
            iter += 1
        else:
            n = 3 * n + 1
            iter += 1
        # print(iter, n)
    return iter


if __name__ == '__main__':
    for i in range(1, 1000001):
        if collatz_iterations(i) + 1 > MAX:
            MAX = collatz_iterations(i) + 1
            print(f'{i} has updated MAX, current value is {MAX}')
    print(MAX)
