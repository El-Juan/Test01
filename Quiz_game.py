print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay - let's play!")

score = 0

answer = input("What does cpu stand for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Idiota!")


