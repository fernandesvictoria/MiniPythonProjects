print("Welcome to my little animal quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

points = 0
incorrect = ("Incorrect answer.")
correct = ("Correct aswer!")

print("Ok! Lets play :)")
print("Answer with true or false only")

answer = input("Male seahorses get pregnant. ")
if answer.lower() == "true":
    print(correct)
    points += 1
else:
    print(incorrect)
   
   
answer = input("Killer whales kill people. ")
if answer.lower() == "false":
    print(correct)
    points += 1
else:
    print(incorrect)


answer = input("Dolphins don't have ears. ")
if answer.lower() == "false":
    print(correct)
    points += 1
else:
    print(incorrect)

answer = input("Octopuses have three hearts. ")
if answer.lower() == "true":
    print(correct)
    points += 1
else:
    print(incorrect)


print("You got " + str((points/4) * 100) + "% correct!")