# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls')

def simple_mult(n):
    simple_mult_list = []
    if n%2==0:
        simple_mult_list.append(2)

    for i in range(3, n, 2):
        if n % i == 0:
            if 2 <= i <= 3:
                simple_mult_list.append(i)
            else:
                for num in range(3, i, 2):
                    if i % num == 0:
                        break
                else:
                    simple_mult_list.append(i)
    return simple_mult_list

def check():
    n = input('Введите число N: ')
    while not n.isdigit():
        print('Некорректный ввод. Уточните значение')
        n = input('Введите число N: ')
    return int(n)

def main():
    print(simple_mult(check()))

if __name__ == "__main__":
    main()