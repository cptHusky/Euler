FILENAME = '100x50Digits.txt'
numbers = []

if __name__ == '__main__':
    with open(FILENAME) as f:
        numbers = f.readlines()
        f.close()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i].replace('\n', ''))
    print(str(sum(numbers))[:10])
