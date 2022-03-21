if __name__ == '__main__':
    numbers = [1, 1]
    even_sum = 0
    while numbers[1] < 4000000:
        buffer = numbers[0]
        numbers[0] = numbers[1]
        numbers[1] += buffer
        if numbers[0] % 2 == 0:
            even_sum += numbers[0]
        print(numbers, '   ', even_sum)