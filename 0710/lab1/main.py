import utilities

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (add, sub, mul, div): ")
    
    if operation == "add":
        result = utilities.add(num1, num2)
    elif operation == "sub":
        result = utilities.sub(num1, num2)
    elif operation == "mul":
        result = utilities.mul(num1, num2)
    elif operation == "div":
        result = utilities.div(num1, num2)
    else :
        print("Invalid operation")
        
    print(f"The result is {result}")
    
if __name__ == "__main__":
    main()