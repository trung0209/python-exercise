def print_str_averages(str1, str2, str3, str4, str5):
    average_value = (int(str1) + int(str2) + int(str3) + int(str4) + int(str5)) / 5
    total_length = (len(str1) + len(str2) + len(str3) + len(str4) + len(str5))
    average_length = total_length / 5
    print(f"Average value: {average_value}")
    print(f"Total length: {total_length}")
    print(f"Average length: {average_length}")


s1 = input("Please give number 1: ")
s2 = input("Please give number 2: ")
s3 = input("Please give number 3: ")
s4 = input("Please give number 4: ")
s5 = input("Please give number 5: ")
print_str_averages(s1, s2, s3, s4, s5)
