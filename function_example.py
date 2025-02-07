def greet():
    """
    This function prints 'hello!' and returns 0.

    :return: 0
    """
    print("hello!")
    return 0

def greet_improved(name):
    """
    This function prints a greeting message including the given name.

    :param name: The name of the person to greet.
    :return: None
    """
    print("hello", name)

greet_improved("John")
greet_improved("Jane")

def custom_op(x=0, y=0):
    """
    This function returns the result of the operation 10*x + y.

    :param x: The first number (default is 0).
    :param y: The second number (default is 0).
    :return: The result of 10*x + y.
    """
    result = 10 * x + y
    return result

print(custom_op(5, 8))  # 58
x = custom_op(5, 9)
print(f"The result of custom_op is: {x}")  # The result of custom_op is: 59
print(custom_op(y=9, x=5))  # 59
print(f"The result of custom_op is: {x}")  # The result of custom_op is: 59
print(custom_op(5))  # 50 (y prend sa valeur par défaut 0)
print(custom_op())  # 0 (x et y prennent leur valeur par défaut 0)
print(custom_op(y=9))  # 9 (x prend sa valeur par défaut 0)


def bond_intro(name):
    print("The name is:", name)

def bond_name(first, last):
    return f"{last}, {first}, {last}"

print(bond_name("Bogdan", "Ratiu"))
bond_intro(bond_name("Bogdan", "Ratiu"))
bond_intro(bond_name())