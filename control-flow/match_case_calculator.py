num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")

match operator:
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        result = num1 / num2
        if num2 != 0:
            print(f"The result is {result}.")
        else:
           print("Error, you can't divide by 0")
    """case '+':
        print(f"The result is {num1 + num2}.")
    case '-':
        print(f"The result is {num1 - num2}.")
    case _:
        print("Please verify you input")"""
