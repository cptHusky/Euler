# answer is 232792560
def get_triplet(m, n):
    a = pow(m, 2) - pow(n, 2)
    b = 2 * m * n
    c = pow(m, 2) + pow(n, 2)
    triplet = [a, b, c]
    return triplet


if __name__ == '__main__':
    abc_production = 1
    for m in range(25):
        for n in range(25):
            if m >= n:
                if sum(get_triplet(m, n)) == 1000:
                    triplet = get_triplet(m, n)
                    for i in range(3):
                        abc_production *= triplet[i]
                    print(abc_production)
