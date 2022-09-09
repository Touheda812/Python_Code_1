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

if age >= 18:
    print("You are old enough to play!!")
    want_play = input("Do you want to play?? ")
    if want_play.lower() == "yes":
        print("Let's Play!!")
else:
    print("You are not 18 years old!!")
