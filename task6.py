# answer is 25164150
import time

LIMIT = 100


if __name__ == '__main__':
    t = time.time()
    sum_sq = (LIMIT * (LIMIT + 1) * (LIMIT * 2 + 1)) / 6
    sq_sum = pow(int(((1 + LIMIT) * int(LIMIT))/2), 2)
    result = abs(sq_sum - sum_sq)
    print(f'difference between {sq_sum} and {sum_sq} is {result}')
    print(time.time() - t, 'seconds spent\n\n')
