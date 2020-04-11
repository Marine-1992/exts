def play():
    secret_number = 7
    secret_color = "pink"

    i1 = input("Pick a number between 1 and 20: ")
    i2 = input("Pick a color: ")

    if secret_number == int(i1) and secret_color == i2:
        print("You've found both the secret number and the secret color! ")
    elif secret_number == int(i1) or secret_color == i2:
        print("You've found at least one of the secrets !")
    else:
        print("You didnt' find any of the secrets !")
        print("Better luck next time !")

    print("Try again!")

play()