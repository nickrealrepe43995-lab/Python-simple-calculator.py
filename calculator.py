# Python Simple Calculator

print("=== Simple Calculator ===")

num1 = float(input("Enter 1st number: "))
operator = input("Choose an operator (+, -, *, /): ")
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operator!")