
num_list = [1, 0, 2, 4, 3, 1, 2, 0, 2]
a = [2, 1, 5, 4, 7, 8]
temp = []
# counter = {}
#
# for i in num_list:
#      if counter.get(i) == None:
#         counter[i] = 1
#      else:
#         counter[i] += 1
# print(counter)

for i in num_list:
     if num_list[i] not in temp:
         temp.append(num_list[i])
print(temp)

