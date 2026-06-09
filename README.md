# Python-simple-calculator.py
Initial upload of calculator projectClick Commit changes. 

#Simple calculator


num1 = float(input("Enter 1st number: "))
operator = input("Choose an operator  +, -, *, / : ")
num2 = float(input("Enter 2nd number: "))
 
if operator == "+": 
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)

else:
    print("Invalid operator!")

