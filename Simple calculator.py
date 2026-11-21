print("---Simple Calculator---")
try:
    # Take Value from user 
    Num1 = float(input("Enter your first number: "))
    Num2 = float(input("Enter your second number: "))

    # Take operation from user like +,- etc. 
    operation = input("Enter an operation: ")  

    # perform the operation based on user's input 
    if operation == "+":
        print("Result:", Num1 + Num2)
    elif operation == "-":
        print("Result:", Num1 - Num2)
    elif operation == "*":
        print("Result:", Num1 * Num2)
    elif operation == "/":
        try:
            print("Result:", Num1 / Num2)
        except ZeroDivisionError:
            print("Cannot divide by zero!") 
    else:
        print("Invalid operation")
except ValueError:
    print("Please enter a valid number!")  