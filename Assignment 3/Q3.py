def character_analysis(a):
    s = str(a).lower()
    vowels = ["a", "e", "i", "o", "u"]

    if ord(a) < 97 or ord(a) > 122:
        return "other"

    if s in vowels:
        return "vowel"
    else:
        return "Consonant"

def test(a):
    for i in range (a):
        user_input = input("Give a character: ")
        if (len(user_input) > 1):
            print("Invalid character length! Must be exactly 1")
        else:
            print(character_analysis(user_input))

number_test = int(input("Enter number of test "))

test(number_test)
