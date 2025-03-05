# Calculator in Python ( 2 Attempt )

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def percentage(num1, num2):
    return num1 % num2


print(" Operations-")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Percentage")

choice =  int(input("Select one Operation :"))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if choice == 1 :
        print(number1, "+", number2, "=", add(number1, number2))
        
elif choice == 2 :
        print(number1, "-", number2, "=", subtract(number1, number2))
        
elif choice == 3 :
        print(number1, "*", number2, "=", multiply(number1, number2))
        
elif choice == 4 :
        print(number1, "/", number2, "=", divide(number1, number2))
        
elif choice == 5 :
        print(number1, "%", number2, "=", percentage(number1, number2))            
else:
    print("Wrong Input 💀")
        



