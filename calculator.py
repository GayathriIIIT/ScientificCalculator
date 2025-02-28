import math

# Define functions
def square_root(num):
    return math.sqrt(num)

def factorial(num):
    return math.factorial(num)

def natural_log(num):
    return math.log(num)

def power(base, exp):
    return math.pow(base, exp)

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Log (ln(x))")
        print("4. Power (x^b)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            num = float(input("Enter number: "))
            print("Result:", square_root(num))

        elif choice == "2":
            num = int(input("Enter number: "))
            print("Result:", factorial(num))

        elif choice == "3":
            num = float(input("Enter number: "))
            print("Result:", natural_log(num))

        elif choice == "4":
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print("Result:", power(base, exp))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

