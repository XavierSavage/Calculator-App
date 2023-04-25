def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def average(x, y):
    return (x + y) / 2


print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Average")


def check_is_float(n):
    try:
        n = int(n)
    except:
        print("Type Error")
        return False
    return n


def check_in_range(n, range):
    if n in range:
        return True
    else:
        print("Not in correct range")
        return False


try:
    choice = int(input("Enter choice(1/2/3/4/5): "))
    print(choice)
except ValueError:
    print("Thats not a number")
    exit(0)

while True:

    def check_is_float(n):
        try:
            n = int(n)
        except:
            print("Type Error")
            return False
        return n


    try:
        num1 = int(input("Enter first number: "))
        print(num1)
    except ValueError:
        print("Thats not a number")
        exit(0)

    try:
        num2 = int(input("Enter second number: "))
        print(num2)
    except ValueError: 
        print("Thats not a number")
        exit(0)

    if num1 == False or num2 == False:
        print("Invalid Input")
        break

    match choice:
        case 1:
            print(num1, "+", num2, "=", add(num1, num2))
        case 2:
            print(num1, "-", num2, "=", subtract(num1, num2))
        case 3:
            print(num1, "x", num2, "=", multiply(num1, num2))
        case 4:
            print(num1, "/", num2, "=", divide(num1, num2))
        case 5:
            print(num1, "avg", num2, "=", average(num1, num2))
        case other:
            print("Choice not valid")
            break
    break
else:
    print("Invalid Input")
