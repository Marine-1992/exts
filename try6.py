def money(euro):
    dollar = euro * 1.08
    msg_1 = "The conversion from "
    msg_2 = " euros is "
    msg_3 = " dollars."
    message = msg_1 + str(euro) + msg_2 + str(dollar) + msg_3
    return message

print(money(50))

def measures(centimeter):
    inches = 2.54 * centimeter
    msg_1 = "The conversion from "
    msg_2 = " centimeters is "
    msg_3 = " inches."
    message = msg_1 + str(centimeter) + msg_2 + str(inches) + msg_3
    return message

print(measures(10))
