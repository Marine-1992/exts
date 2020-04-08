a = float(input("Enter a number: "))
b = float(input("Enter a second number: "))
result = a - b

if result > 10:
    print("The result is greater than 10.")
elif result > 0:
    print("The result is greater than 0 but not greater than 10.")
elif result == 0:
    print("The result is zero.")
else:
    print("Negative number!")

print("You can try again!")
