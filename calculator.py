import sys
import math

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
# a -- addend
# b -- augend
def add(a, b):
    return a + b

# Subtract function
# a -- minuend
# b -- subtrahend
def sub(a, b):
    return a - b

# Multiply function
# a -- multiplicand
# b -- multiplier
def mult(a, b):
    return a * b

# Divide function
# a -- dividend
# b -- divisor
def div(a, b):
   if b == 0:
       return "Error! Division by zero is not allowed."
   return a / b

# Modulus function
# a -- dividend
# b -- divisor
def mod(a, b):
   if b == 0:
       return "Error! Division by zero is not allowed."
   return a % b

# Exponentiation function
# a -- base
# b -- exponent
def exp(a, b):
   return a ** b

# Integer Division function
# a -- dividend
# b -- divisor
def int_div(a, b):
   if b == 0:
       return "Error! Division by zero is not allowed."
   return a // b

# Square Root function
# a -- number to find the square root of
def sqrt(a):
   if a < 0:
       return "Error! Square root of a negative number is not defined in real numbers."
   return math.sqrt(a)

# -------------------------------------------------------- #
# -- MAIN FUNCTIONALITY ---------------------------------- #
# -------------------------------------------------------- #

def main():
    if len(sys.argv) == 4:
        # Command-line arguments mode
        try:
            a = float(sys.argv[1])
            op = sys.argv[2]
            b = float(sys.argv[3])
        except ValueError:
            print("Invalid number argument...")
            return

        result = calculate(a, op, b)
        print("Result: ", result)

    else:
        # Interactive mode
        while True:
            try:
                a = float(input("Enter the first argument: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            while True:
                op = input("Enter the operation (+, -, *, /, %, **, //, sqrt) or 'help' for options: ")

                if op == "help":
                    show_help()
                    continue

                if op == "sqrt":
                    result = sqrt(a)
                    print(f"Square root of {a} is: {result}")
                else:
                    try:
                        b = float(input("Enter the second argument: "))
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue

                    result = calculate(a, op, b)
                    print(f"Result: {a} {op} {b} = {result}")

                q = input("Do you want to continue with this result? [y/n]: ")
                if q.lower() == 'y':
                    a = result
                else:
                    break

            q = input("Quit the calculator? [y/n]: ")
            if q.lower() == 'y':
                break

def calculate(a, op, b=None):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mult(a, b)
    elif op == "/":
        return div(a, b)
    elif op == "%":
        return mod(a, b)
    elif op == "**":
        return exp(a, b)
    elif op == "//":
        return int_div(a, b)
    else:
        return "Invalid operation"

def show_help():
    print("Available operations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("% : Modulus")
    print("** : Exponentiation")
    print("// : Integer Division")
    print("sqrt : Square Root")

if __name__ == "__main__":
    main()

# -------------------------------------------------------- #
