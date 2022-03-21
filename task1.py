# answer is 233168 for LIMIT = 1000
import time

LIMIT = 1000


def arif_seq_sum(step):
    local_limit = LIMIT - 1
    first_number = step
    last_number = int(local_limit/step) * step
    sum = ((first_number + last_number) * int(local_limit/step))/2
    return sum


if __name__ == '__main__':
    t = time.time()
    sum3 = arif_seq_sum(3)
    sum5 = arif_seq_sum(5)
    sum15 = arif_seq_sum(15)
    print(sum3, sum5, sum15)
    print(sum3 + sum5 - sum15)
    print(time.time() - t, '\n\n')


# --------------STUPID WAY--------------------
if __name__ == '__main__':
    t = time.time()
    s = 0
    for number in range(1, LIMIT):
        if number % 3 == 0:
            s += number
        elif number % 5 == 0:
            s += number
    print(s)
    print(time.time() - t, '\n\n')
