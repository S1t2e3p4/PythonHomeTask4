# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os
os.system('cls')

def check():
    d = int(input('Введите значение "d" (до какого колличества знаков, после запятой, необходимо произвести округление): '))
    while not 1<=d<=10:
        print('Некорректный ввод. Уточните значение')
        d = int(input('Введите значение "d" (до какого колличества знаков, после запятой, необходимо произвести округление): '))
    return int(d)

def main():
    rounding = check()
    d = 10**(-rounding)
    print(f'd = %.{rounding}f'%d)
    print(f'10 / 3 = {round(10/3,rounding)}')


if __name__ == "__main__":
    main()