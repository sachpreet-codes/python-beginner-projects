print("Welcome to Computer Quiz!!")

playing = input("Do you want to play the quiz? ").lower()

if playing != "yes":
    quit()

print("Then Let's play :)")
score = 0

answer = input("What is CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is PSU stands for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print(f"You got {score} question correct")
print(f"You got {(score / 4) * 100}%")

