FILENAME = 'numbers20x20grid.txt'
numbers = []


def vertical(numbers):
    v_largest_product = 0
    for m in range(len(numbers) - 3):
        for n in range(len(numbers[m])):
            a = int(numbers[m][n])
            b = int(numbers[m + 1][n])
            c = int(numbers[m + 2][n])
            d = int(numbers[m + 3][n])
            # print(a, b, c, d)
            product = a * b * c * d
            if product > v_largest_product:
                v_largest_product = product
    return v_largest_product


def horizontal(numbers):
    h_largest_product = 0
    for m in range(len(numbers)):
        for n in range(len(numbers[m]) - 3):
            a = int(numbers[m][n])
            b = int(numbers[m][n + 1])
            c = int(numbers[m][n + 2])
            d = int(numbers[m][n + 3])
            # print(a, b, c, d)
            product = a * b * c * d
            if product > h_largest_product:
                h_largest_product = product
    return h_largest_product


def diagonal(numbers):
    d_largest_product = 0
    for m in range(len(numbers) - 3):
        for n in range(len(numbers[m]) - 3):
            a = int(numbers[m][n])
            b = int(numbers[m + 1][n + 1])
            c = int(numbers[m + 2][n + 2])
            d = int(numbers[m + 3][n + 3])
            # print(a, b, c, d)
            product = a * b * c * d
            if product > d_largest_product:
                d_largest_product = product
    for m in range(3, len(numbers)):
        for n in range(len(numbers[m]) - 3):
            a = int(numbers[m][n])
            b = int(numbers[m - 1][n + 1])
            c = int(numbers[m - 2][n + 2])
            d = int(numbers[m - 3][n + 3])
            # print(a, b, c, d)
            product = a * b * c * d
            if product > d_largest_product:
                d_largest_product = product
    return d_largest_product


def find_largest_product(numbers):
    v = vertical(numbers)
    h = horizontal(numbers)
    d = diagonal(numbers)
    return max(v, h, d)


if __name__ == '__main__':
    with open(FILENAME, 'r') as f:
        all_numbers = f.read().splitlines()
        for i in range(len(all_numbers)):
            numbers.append(all_numbers[i].split(' '))
            # print(numbers[i])
        f.close()
    result = find_largest_product(numbers)
    print(result)
