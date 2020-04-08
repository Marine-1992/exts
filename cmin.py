def convert(cm):
    if cm < 0:
        print("Beware ! This is a negative value!")
        
    msg_1 = " centimeters are "
    msg_2 = " inches."
    result = cm / 2.54
    return str(cm) + msg_1 + str(result) + msg_2

print(convert(6.87))

