def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("GCD =", gcd(a, b))
