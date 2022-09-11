'''
Temperature Conversion: get two inputs from the user: Unit From and Temperature
Display converted temperature
Units: Celsius and Fahrenheit.
'''

print("Touheda Khanom")
print("CST 3529 HW#1: Temperature & Distance Conversion")


def temperature_conversion():
    user_inputs = input("Choose the conversion unit Celsius or Fahrenheit (C/F)? ").lower()
    if user_inputs == "f":
        celsius = float(input("Enter the temperature to convert from celsius to fahrenheit: "))
        fahrenheit = 1.8 * celsius + 32.0
        print("Temperature in Fahrenheit:", fahrenheit)
    elif user_inputs == "c":
        fahrenheit = float(input("Enter the temperature to convert from fahrenheit to celsius: "))
        celsius = (fahrenheit - 32) / 1.8
        print("Temperature in Celsius:", celsius)
    else:
        print("Choose F for Fahrenheit or C for Celsius.")


'''
Distance Conversion: again, get two inputs: Unit From and Distance
Display converted distance
Units: Meter and Miles
'''


def distance_conversion():
    user_inputs = input("Choose the conversion unit meter or miles (ME/MI)? ").lower()
    if user_inputs == "me":
        meter = float(input("Enter distance to convert to meter from miles: "))
        miles = meter * 0.00062137
        print("Distance in miles:", miles)
    elif user_inputs == "mi":
        miles = float(input("Enter distance to convert to miles from meter: "))
        meter = miles * 1609.344
        print("Distance in meter:", meter)
    else:
        print("Choose ME for Meter and MI for Miles")


temperature_conversion()
distance_conversion()
