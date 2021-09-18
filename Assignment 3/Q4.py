user_input = [int(input()) for i in range(1,21)] #multiple line input

# user_input = list(map(int,input().split(" ")))

count_positive = 0
count_negative = 0
count_odd = 0
count_even = 0
number_of_zero = 0

for i in user_input:
    if i >= 0:
        count_positive += 1
    else:
        count_negative += 1
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

number_of_zero = user_input.count(0)

print(f"positive: {count_positive}")
print(f"negative: {count_negative}")
print(f"odd: {count_odd}")
print(f"even: {count_even}")
print(f"Number of zero: {number_of_zero}")
