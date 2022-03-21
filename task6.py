import time


if __name__ == '__main__':
    t = time.time()
    sum_sq = 0
    sq_sum = 0
    for i in range(100001):
        sum_sq += pow(i, 2)
        sq_sum += i
    result = sq_sum ^ 2 - sum_sq
    print(f'difference between {sq_sum ^ 2} and {sum_sq} is {abs(pow(i, 2) - sum_sq)}')
    print(time.time() - t, '\n\n')
