import random
def randomguest():
    randNum = int(random.random()*100)
    point = 0
    times = 10
    while True:
        while True:
            try:
                guess = int(input("Enter a number "))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                break
        if (guess >= 0 and guess <= 100):
            break
        print("Must be from 0 to 100")
    if guess == randNum:
        point += 1
        times -= 1
    else:
        print(randNum)
        print("Wrong")
        randNum = int(random.random() * 100)
        times -= 1
        while times != 0:
            print("Number of guess:" + str(times))
            while True:
                guess = int(input("Enter a number  "))
                if (guess >= 0 or guess <= 100):
                    break
                print("Must be from 0 to 100")
            if guess == randNum:
                point += 1
                times -= 1
            else:
                print(randNum)
                print("Wrong")
                randNum = int(random.random() * 100)
                times -= 1
        else:
          print(f"Point has earned {point}")
          print("End")

randomguest()
