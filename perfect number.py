num = int(input("Enter the number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("{} is a perfect number.".format(num))
else:
    print("{} is not a perfect number.".format(num))