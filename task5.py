if __name__ == '__main__':
    number = 0
    while True:
        number += 20
        cond = True
        for delimiter in range(2, 21):
            if cond:
                if number % delimiter != 0:
                    cond = False
        print(number)
        if cond:
            print(number, 'is result')
            break
