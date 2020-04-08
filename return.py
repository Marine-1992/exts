def add(number_one, number_two):
    result = number_one + number_two
    return result

total = add(3, 7)
print(total)

def greet (name, weather):
    message = "Hi " + name + ". It is a " + weather + " day."
    return message

greetings = greet("Sasha", "rainy")
print(greetings)

greetings = greet("Carl", "sunny")
print(greetings)
