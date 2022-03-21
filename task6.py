if __name__ == '__main__':
    sum_sq = 0
    sum = 0
    for i in range(101):
        sum_sq += i^2
        sum += i
    result = sum^2 - sum_sq
    print(f'difference between {sum^2} and {sum_sq}{sum^2 - sum_sq}')
