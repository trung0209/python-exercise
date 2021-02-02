from stack import Stack

# brunch = Menu("brunch", {
#     'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
#     'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
# }, "11am", "4pm")
# print(brunch)
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print("\nLet's play Towers of Hanoi!!")
# from stack import Stack
#
# print("\nLet's play Towers of Hanoi!!")
#
# # Create the Stacks
# stacks = []
# left_stack = Stack("Left")
# middle_stack = Stack("Middle")
# right_stack = Stack("Right")
# stacks.append(left_stack)
# stacks.append(middle_stack)
# stacks.append(right_stack)
# # Set up the Game
# num_disks = int(input("\nHow many disks do you want to play with?\n"))
# num_optimal_moves = 2 ** num_disks - 1
# print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")
# # Get User Input
# for i in range(num_disks, 0, -1):
#   left_stack.push(i)
#
#
# def get_input():
#   choices = [x.get_name()[0] for x in stacks]
#   while (True):
#     for i in range(len(stacks)):
#       name = stacks[i].get_name()
#       letter = choices[i]
#       print(f"Enter {name} for {letter}")
#
#     user_input = input();
#     if (user_input.capitalize() in choices):
#       for i in range(len(stacks)):
#           return stacks[i]
#
# # Play the Game
# num_user_moves = 0
# while (right_stack.get_size() != num_disks):
#   print("\n\n\n...Current Stacks...")
#   for i in stacks:
#     i.print_items()
#   while (True):
#     print("\nWhich stack do you want to move from?\n")
#     from_stack = get_input()
#     print("\nWhich stack do you want to move to?\n")
#     to_stack = get_input()
#     if (from_stack.get_size() == 0):
#       print("\n\nInvalid Move. Try Again")
#     elif (to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek()):
#       disk = from_stack.pop()
#       to_stack.push(disk)
#       num_user_moves += 1
#       break
#     else:
#       print("\n\nInvalid Move. Try Again")
#
# print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")
#
# def fibonaci(num):
#     if num <= 1:
#         return num
#     return fibonaci(num-1) + fibonaci(num-2)
# nterms = 10
# print("Fibonacci sequence:")
# for i in range(nterms):
#     print(fibonaci(i))
#
# def sum_digit(num):
#     if num <= 1:
#         return num
#     first = num % 10
#     next = num // 10
#     return first + sum_digit(next)
# # print(sum_digit(111))
# def add_one(num):
#     num += 1
# n = 2
# add_one(n)
# print(n)
test = [1,2,4,41,51,5135,134,124]
print(-len(test))
for i in range(1,61):
    if i % 4 == 3:
        print(i)