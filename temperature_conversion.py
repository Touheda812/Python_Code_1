'''
Temperature Conversion: get two inputs from the user: Unit From and Temperature
Display converted temperature
Units: Celsius and Fahrenheit.
'''

print("CST 3529 HW#1: Temperature Conversion")
user_inputs = input("Choose the conversion unit Celsius or Fahrenheit (C/F)? ").lower()
if user_inputs == "c":
    celsius = float(input("Temperature in Celsius: "))
    fahrenheit = 1.8 * celsius + 32.0
    print("Temperature in Fahrenheit:", fahrenheit)
elif user_inputs == "f":
    fahrenheit = float(input("Temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Temperature in Celsius:", celsius)
else:
    print("Choose F for Fahrenheit or C for Celsius.")
