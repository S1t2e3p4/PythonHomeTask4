# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import os
import random
os.system('cls')

def list_creation(num, limit):
    new_list = []
    for _ in range(num+1):
        new_list.append(random.randint(0, 100))
    print('Список коэффициентов:', new_list)
    return new_list

def check():
    k = int(input('Введите число "K", соответствующее степени, в которую необходимо возвести коэффициенты списка: '))
    while not 0<=k<=100:
        print('Некорректный ввод. Уточните значение')
        k = int(input('Введите число "K", соответствующее степени, в которую необходимо возвести коэффициенты списка: '))
    return int(k)

def polynom_creation(degree, new_list, filevslist):
    with open(filevslist, 'w') as data:
        for i in range(degree+1):
                if new_list[i]==0:
                    continue
                elif new_list[i]==1:
                    data.write(f' x^{degree-i} +')
                elif (degree-i)==1:
                    data.write(f' {new_list[i]*1}x +')
                elif (degree-i)==0:
                    data.write(f' {new_list[i]*1}')
                else:
                    data.write(f' {new_list[i]}x^{degree-i} +')
        data.write(' = 0')

def polynoms_sum(degree, new_list1, new_list2, filevslist):
    with open(filevslist, 'w') as data:
        for i in range(degree+1):
                if new_list1[i]==0 and new_list2[i]==0:
                    continue
                elif new_list1[i]==1 and new_list2[i]==0 or new_list1[i]==0 and new_list2[i]==1:
                    data.write(f' x^{degree-i} +')
                elif (degree-i)==1:
                    data.write(f' {(new_list1[i]+new_list2[i])*1}x +')
                elif (degree-i)==0:
                    data.write(f' {new_list1[i]+new_list2[i]}')
                else:
                    data.write(f' {new_list1[i]+new_list2[i]}x^{degree-i} +')
        data.write(' = 0')

def main():
    k = check()
    coef_list_1 = list_creation(k, 100)
    polynom_creation(k, coef_list_1, 'filevslist1.txt')

    coef_list_2 = list_creation(k, 100)
    polynom_creation(k, coef_list_2, 'filevslist2.txt')

    polynoms_sum(k, coef_list_1, coef_list_2, 'filesumlists.txt')

if __name__ == "__main__":
    main()
