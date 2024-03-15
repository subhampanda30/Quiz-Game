print("Welcome to my computer quiz1")

playing=input("Do you want to play?")

if playing !="yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower()== "central processing unit":
    print('Correct!')
    score+=1

else:
    print("incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score+=1

else:
    print("incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score+=1

else:
    print("incorrect!")

answer = input("What does HTML stand for? ")
if answer.lower() == "hyper text markup language":
    print('Correct!')
    score+=1

else:
    print("incorrect!")

answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheets":
    print('Correct!')
    score+=1

else:
    print("incorrect!")

print("you got" + str(score) + "questions correct!")
print("you got" + str((score/4)*100)+"%.")

