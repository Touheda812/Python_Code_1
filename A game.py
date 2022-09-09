# This is another way of commenting 3 quotations
'''
data types in python: String, int, float, bool
string: "hello", "hi"
int: 9, -9
float: 0.9
bool: True, False
'''

print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.")

health = 10
print("You are staring with", health, "health")

if age >= 18:
    print("You are old enough to play!!")
    want_play = input("Do you want to play?? ").lower()
    if want_play == "yes":
        print("Let's Play!!")

        left_right = input("First choice: Left/Right?? ")
        if left_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around ("
                        "across/around)? ")
            if ans == "around":
                print("YOu went around and reached the other side of the lake")

            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
            health -=5

        ans = input("You noticed a house and a river which do you go to (river/house)? ")
        if ans == "house":
            print("You go to the house and are greeted by the owner. He doesn't like you and you lose 5 health")
            health -=5

            if health <= 0:
                print("You now have 0 health and you lost the game..")
            else:
                print("You have survived...You win!!")
        else:
            print("You fell down and lost...")
    else:
        print("BYE")
else:
    print("You are not 18 years old!!")
