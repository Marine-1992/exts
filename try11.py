def temp_converter(celsius):
    msg_1 = " degrees Celsius are "
    msg_2 = " degrees Farenheit."
    result = (celsius * 9/5) + 32
    return str(celsius) + msg_1 + str(result) + msg_2

user_input = input("Enter a temperature in degrees Celsius: ")
farenheit_result = temp_converter(float(user_input))

if float(user_input) > 38:
    print("It's really hot!")

print(farenheit_result)


