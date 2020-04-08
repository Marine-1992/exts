
#celsius = input("Enter the temperature in Celsius: ")
#farenheit = (float(celsius) * 9/5) + 32
#message = celsius + " degrees Celsius convert into " + str(farenheit) + " degrees Farenheit."
#print(message)

def converter(c):
    f = (float(c) * 9 / 5) + 32
    return str(c) + " degrees celsius are " + str(f) + " degrees Farenheit."

i = input("Enter a temperature in degrees Celsius: ")

