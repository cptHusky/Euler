# answer is 906609
import time

if __name__ == '__main__':
    t = time.time()
    largest = 0
    for number1 in range(1000):
        for number2 in range(1000):
            test = number1 * number2
            if str(test) == str(test)[::-1]:
                if largest < test:
                    largest = test
    print(f'{number1} x {number2} = {largest}')
    print(time.time() - t, 'seconds spent\n\n')
