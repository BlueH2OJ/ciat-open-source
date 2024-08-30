import sys

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

# Exponential function
# a -- base
# b -- exponent
def exp(a, b):
    return a ** b



# -------------------------------------------------------- #
# -- MAIN FUNCTIONALITY ---------------------------------- #
# -------------------------------------------------------- #

def main():
    if len(sys.argv) == 4:
        # Command-line arguments mode
        try:
            a = int(sys.argv[1])
            op = sys.argv[2]
            b = int(sys.argv[3])
        except ValueError:
            print("Invalid number argument...")
            return

        if op == "+":
            print("Sum: ", add(a, b))
        elif op == "-":
            print("Difference: ", sub(a, b))
        elif op == "*":
            print("Product: ", mult(a, b))
        elif op == "/":
            print("Quotient: ", div(a, b))
        elif op == "**":
            print("Exponentiation: ", exp(a, b))
        else:
            print("Invalid operation...")
    else:
        # Interactive mode
        a = None
        b = None
        op = None

        while True:
            # get input values
            a = input("Enter the first argument: ")
            op = input("Enter the operation: ")
            b = input("Enter the second argument: ")
            try:
                a = int(a)
                b = int(b)
            except ValueError:
                print("Invalid number argument...")
                op = None

            # decide function
            if op != None:
                if op == "+":
                    print("Sum: ", add(a, b))
                elif op == "-":
                    print("Difference: ", sub(a, b))
                elif op == "*":
                    print("Product: ", mult(a, b))
                elif op == "/":
                    print("Quotient: ", div(a, b))
                elif op == "**":
                    print("Exponentiation: ", exp(a, b))
                else:
                    print("Invalid operation...")

            q = input("Quit? [y/n] ")
            if q == "y" or q == "Y":
                break

if __name__ == "__main__":
    main()

# -------------------------------------------------------- #