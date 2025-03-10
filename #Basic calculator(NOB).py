#Basic calculator
# Import the math module for the square root function
import math

# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    # Check if the second number is zero to avoid division by zero error
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

# Define a function for square (x^2)
def square(x):
    return x ** 2

# Define a function for square root (√x)
def square_root(x):
    # Check if the number is negative to avoid math domain error
    if x < 0:
        return "Error: Cannot calculate square root of a negative number!"
    return math.sqrt(x)

# Main function for the calculator
def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Loop to allow multiple calculations
    while True:
        try:
            # Ask the user to input a number (or two numbers for some operations)
            print("Select operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Square (x^2)")
            print("6. Square Root (√x)")
            choice = input("Enter choice (1/2/3/4/5/6): ")
            
            # Perform the selected operation
            if choice in ['1', '2', '3', '4']:
                # For addition, subtraction, multiplication, and division, ask for two numbers
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == '1':
                    print(f"Result: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {divide(num1, num2)}")
            
            elif choice == '5':
                # For square, ask for one number
                num = float(input("Enter a number: "))
                print(f"Result: {square(num)}")
            
            elif choice == '6':
                # For square root, ask for one number
                num = float(input("Enter a number: "))
                print(f"Result: {square_root(num)}")
            
            else:
                print("Invalid choice! Please select a valid operation.")
        
        # Handle invalid input (e.g., if the user enters a non-number)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        
        # Ask the user if they want to perform another calculation
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != "yes":
            print("Thank you for using the Simple Calculator!")
            break

# Run the calculator
if __name__ == "__main__":
    calculator()