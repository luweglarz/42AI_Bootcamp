import sys


if len(sys.argv) < 2:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("python operations.py 10 3")
if len(sys.argv) > 3:
    print("InputError: too many arguments")

ope1 = int(sys.argv[1])
ope2 = int(sys.argv[2])
print("{:<12}".format("Sum:"), (ope1 + ope2))
print("{:<12}".format("Difference:"), (ope1 - ope2))
print("{:<12}".format("Product:"), (ope1 * ope2))
print("{:<12}".format("Quotient:"), "Error" if ope2 == 0 else (ope1 / ope2))
print("{:<12}".format("Quotient:"), "Error" if ope2 == 0 else (ope1 % ope2))
