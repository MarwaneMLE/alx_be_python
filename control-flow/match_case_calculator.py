num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /): ")

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
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case _:
        print("Please verify you input")"""
