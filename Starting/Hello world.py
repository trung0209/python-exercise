import math
import random

def myfunc(x, y, z):
    print(x, y, z)

def dangerous_func(n):
    if n < 10:
        return "a string"
    else:
        return 4
age = 90
print("hello " + str(age+10) + " lol")
tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}
myfunc(*tuple_vec)
myfunc(**dict_vec)
print(dangerous_func(12) + 3)
transportations = ["car","bike"]

def good_func(n: int) -> str: # Parameters type int
    if n < 10:
        return "a string"
    else:
        return "other string"
print(good_func(4))
def equation():
    a = float(input("nhap a "))
    b = float(input("nhap b "))
    c = float(input("nhap c "))
    if (a == 0) :
        if b==0 :
            if c==0:
                print("phuong trinh vo so nghiem")
            else:
                print("phuong trinh vo nghiem")
        else:
            if c==0:
                print("phuong trinh co 1 nghiem x = 0")
            else:
                x = -c/b
                print("phuong trinh co 1 nghiem x = " + str(x))
    else:
        delta = math.pow(b,2) - 4*a*c
        if delta < 0:
            print("phuong trinh vo nghiem")
        elif delta == 0:
            x = -b/2*a
            print("phuong trinh co nghiem kep x = " +str(x))
        else:
            x1 = (-b+math.sqrt(delta))/(2*a)
            x2 = (-b-math.sqrt(delta))/(2*a)
            print("phuong trinh co 2 nghiem phan biet x1 = " + str(x1) + " x2 = " + str(x2))

# equation()


def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit

low, high = get_boundaries(100, 20)
def daomang():
    a = list(input("nhap mang"))
    temp = ""
    length = len(a)
    for i in range(0,length):
        temp = str(a[i]) + temp

    print(list(temp))
# daomang()
def anagram():
    a = input("mang 1")
    b = input("mang 2")
    if (sorted(a) == sorted(b)):
        print("is anagram")
    else:
        print("not anagram")
# anagram()
def nguyento(x):
    for i in range (4,x+1):
        half = int(i/2+1)
        for j in range (2,half):
            if i % j == 0:
             break
        else:
            print(i)

# nguyento()

# class Car:
#     def __init__(con, manufacturer, model):
#         con.manufacturer = manufacturer
#         con.model = model
#
#     def __str__(con):
#        return f"{con.model} by {con.manufacturer}"
#
#     def run(self):       print("car runs")
#
#     def stop(self):       print("car stops")
#
# # fadil = Car("Vinfast", "Fadil")
# # fadil.run()
# # fadil.stop()
# # print(fadil)
# # triton = Car("Mitsubishi", "Triton")
# # triton.run()
# # print(triton)

def randomguest():
    randNum = int(random.random()*10)
    while True:
        guess = int(input("Nhap "))
        if (guess > 0 and guess <= 10):
            break
        print("phai nhap tu 0 den 10")
    times = 10
    if guess == randNum:
        print("Win")
    else:
        print("wrong")
        print(randNum)
        randNum = int(random.random() * 10)
        times -= 1
        while times != 0:
            print("Number of guess:" + str(times))
            while True:
                guess = int(input("Nhap "))
                if (guess > 0 and guess <= 10):
                    break
                print("phai nhap tu 0 den 10")
            if guess == randNum:
                print("Win")
            else:
                print("wrong")
                print(randNum)
                randNum = int(random.random() * 10)
                times -= 1
        else:
            print("loss")

# randomguest()
def vote():
    a = list(input("nhap list"))
    a.sort()
    temp = []

    count = 1
    for i in range(0,len(a)):
        temp.append(a.count(a[i]))
    values = list(dict.fromkeys(temp))
    print(max(values))
# vote()
def variadic(*x):
    temp = []
    for num in x:
        temp.append(num)
    temp.sort()
    print(temp[len(temp)-1])
    print(temp[len(temp)-2])
def inc_or_dec(a:list):
    temp_list = []
    for i in range(0,len(a)-1):
        if a[i] > a[i+1]:
            temp_list.append("+")
        elif a[i] < a[i+1]:
            temp_list.append("-")
        else:
            temp_list.append("=")
    print(temp_list)

# variadic(1,100,32,99,5,1)
first_name = "Rodrigo"
last_name = "Villanueva"
m = [1, 4, 4, 2, 3, 6, 7, 8, 5, 5]
inc_or_dec(m)
