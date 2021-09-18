def is_prime(number):
    if (number <= 1):
        return False
    for i in range(2,int(number/2)+1):
        if (number % i == 0):
            return False
    return True

checked_number = int(input("Enter a number: "))
if (is_prime(checked_number)):
    print(f"{checked_number} is a prime number")
else:
    print(f"{checked_number} is not a prime number")