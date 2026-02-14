num = int(input("Enter a number: "))
temp = num
reverse_num = 0

while temp > 0:
    rem = temp % 10
    reverse_num = (reverse_num * 10) + rem
    temp = temp // 10

print("The Given number is {} and Reverse is {}".format(num, reverse_num))