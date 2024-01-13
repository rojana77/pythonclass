num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -,*,/): ")

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operator."


result = calculator(num1, num2, operator)

print(f"Result: {result}")
