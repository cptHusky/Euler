if __name__ == '__main__':
    largest = 0
    for number1 in range(1000):
        for number2 in range(1000):
            test = number1 * number2
            if str(test) == str(test)[::-1]:
                if largest < test:
                    largest = test
    print(largest)