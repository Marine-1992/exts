
def greet(gender):
    if gender == "male":
        return "Hello Sir! Welcome back."
    elif gender == "female":
        return "Hello Madam! Welcome back."
    else:
        return "Hello ! Welcome back."

gender = input("Please enter your gender: ")

print(greet("male"))
print(greet("female"))
print(greet("not specified"))

