
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
import random
os.system('cls')

def list_creation(n, limit):
    new_list = []
    for _ in range(n):
        new_list.append(random.randint(-limit, limit))
    return new_list

def unique_list(new_list):
        non_repeat_list = []
        for i in range(len(new_list)):
            if new_list.count(new_list[i])==1:
                non_repeat_list.append(new_list[i])
        return non_repeat_list

def main():    
    n = abs(int(input('Введите длину списка: ')))
    limit = abs(int(input('Введите максимальное значение переменной в списке: ')))
    my_list = list_creation(n, limit)
    print(my_list)
    print(unique_list(my_list))

if __name__ == "__main__":
    main()
