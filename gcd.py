num1 = int(input("Enter the the first number: "))
num2 = int(input("Enter the the second number: "))

small = 0
gcd = 0
if num1 > num2:
    small = num2
else:
    small = num1

for i in range(1, small + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("The Greatest Common Divisor of {} and {} is {}.".format(num1, num2, gcd))