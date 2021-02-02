def input_list():
    nunber = int(input("list length "))
    a = []
    for i in range(nunber):
        a.append(input("enter a num: "))
    return a

def inc_or_dec():
    a = input_list()
    temp_list = []
    for i in range(0,len(a)-1):
        if a[i] > a[i+1]:
            temp_list.append("+")
        elif a[i] < a[i+1]:
            temp_list.append("-")
        else:
            temp_list.append("=")
    print(a)
    print(temp_list)
# m = [1, 4, 4, 2, 3, 6, 7, 8, 5, 5]


inc_or_dec()
