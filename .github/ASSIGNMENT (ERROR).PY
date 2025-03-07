try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



try:
    num = int("abc")
except ValueError:
    print("Error: Invalid input, please enter a number.")



try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file was not found.")



try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Error: Index out of range.")



try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError:
    print("Error: Key not found in the dictionary.")



try:
    result = "hello" + 5
except TypeError:
    print("Error: Unsupported operation between string and integer.")



try:
    my_string = "hello"
    my_string.append(" world")
except AttributeError:
    print("Error: 'str' object has no attribute 'append'.")



try:
    print(unknown_variable)
except NameError:
    print("Error: The variable is not defined.")



try:
    assert 2 + 2 == 5
except AssertionError:
    print("Error: The assertion failed.")



try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Error: Division by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
