name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way you would like "
               "to go? ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around it or swim "
                   "across: ")

    if answer == "swim":
        print("You swam across and were eaten by a alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You can back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them or no? ")
        if answer == "yes":
            print("YOu talk to the stranger and they gave you a gift")
        elif answer == "no":
            print("You lose")
else:
    print("Not a valid option. you lose.")
print("Thank you for trying ")