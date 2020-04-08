def statement(celsius):
    farenheit = calcul(celsius)
    message = str(celsius) + " degrees Celsius are " + str(farenheit) + " degrees Farenheit."
    return message

def calcul(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

print(statement(50))
