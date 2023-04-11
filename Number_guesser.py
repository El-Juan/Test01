import random

top_range = input("Type a number: ")
guesses = 0
first_try = True

if  top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Type a number next time!")
    quit()

r_n = random.randint(0, top_range)

while True:
    if first_try == True:
        guesses += 1

    user_guess = input("Make a guess: ")

    if  user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if  user_guess == r_n:
        print("You got it!")
        print("It took you " + guesses.__str__() + " to complete.")
        break
    else:
        print("You are wrong. The answer was " + r_n.__str__())
        r_n = random.randint(0 , top_range)
        continue
    break
