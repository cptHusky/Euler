# answer is 4613732
import time


if __name__ == '__main__':
    t = time.time()
    numbers = [1, 1]
    even_sum = 0
    while numbers[1] in range(4000000):
        buffer = numbers[0]
        numbers[0] = numbers[1]
        numbers[1] += buffer
        if numbers[0] % 2 == 0:
            even_sum += numbers[0]
        print(numbers, '   ', even_sum)
    print(time.time() - t, 'seconds spent\n\n')
