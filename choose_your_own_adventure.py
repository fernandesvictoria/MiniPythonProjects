name = input("Type your name: ")
print("Welcome", name,"to this adventure!")

answer = input("You're in a dirt rode, it has come to an end and you can go left or right. Which is do you wanna go? ").lower()

if answer == "left":
    answer = input("You come to a river, do you want to walk around it or swim across? Type walk or swim. ")

    if answer == 'swim':
        print('You swam across and an alligator appeared... he gave you a ride to the other side :D')
        answer= input('You encounter a bridge, it looks wobbly. Do you want to cross the bridge or head back? (cross/back)')
        if answer == 'cross':
         answer = input('You crossed the bridge and meet a stranger, do you wanna talk to them? (yes/no)')

        if answer == 'yes':
            print('You talk to the stranger and they give you gold, You win!')
        
        elif answer == 'no':
            print('The stranger had the prize, and since you ignored him you didnt get it... You lost.')
        
        else:
            print('Not valid option you lost')
    elif answer == 'walk':
        print('You walked for many miles without water and died of dehydration, you lost. ')
    else:
        print('Not valid option you lose.')

elif answer == 'right':
    answer= input('You encounter a bridge, it looks wobbly. Do you want to cross the bridge or head back? (cross/back)')

    if answer == 'cross':
        answer = input('You crossed the bridge and meet a stranger, do you wanna talk to them? (yes/no)')

        if answer == 'yes':
            print('You talk to the stranger and they give you gold, You win!')
        
        elif answer == 'no':
            print('The stranger had the prize, and since you ignored him you didnt get it... You lost.')
        
        else:
            print('Not valid option you lost')

    elif answer == 'back':
        print('You get lost in the woods and die of starvation.')
    else:
        print('Not valid option you lose.')
else:
    print("Not a valid option, you lose.")


print('THANK YOU FOR PlAYING', name.upper(),'.')