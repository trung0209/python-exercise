import random
import numpy as np

def sum(num_list: list):
    temp = 0
    for num in num_list:
       temp += num
    return temp

def daomang(main_list: list):
    return main_list[::-1]

def vote(a: list):
    temp = []
    for i in range(0,len(a)):
        temp.append(a.count(a[i]))
    values = list(dict.fromkeys(temp))
    return max(values)

def sorting_ascending(x: list):
    length = len(x)
    for i in range(0,length):
        for j in range(i+1,length):
            if x[i] > x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x

def sorting_descending(x: list):
    length = len(x)
    for i in range(0,length):
        for j in range(i+1,length):
            if x[i] < x[j]:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return x

def Matrix():
    m = int(input("nhap m"))
    n = int(input("nhap n"))
    i=0
    while i  < m:
        matrix = [[int(random.random()*10)]*m]*n
        i += 1
    for row in matrix:
        print(row)





a = [2, 4, 1, 5]
b = [1, 2, 1, 2, 1, 3, 1, 4]
c = [2, 1, 5, 4, 7, 8]
# print(sum(a))
# # print(daomang(a))
# print(vote(b))
# print(sorting_ascending(c))
# print(sorting_descending(c))
Matrix()