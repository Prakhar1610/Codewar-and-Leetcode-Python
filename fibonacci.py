n = int(input("Enter the nth number: "))

a = 0
b = 1
c = 0

print("The fibonacci series upto {}th", {n})
print(a, end = " ")
print(b, end = " ")
for i in range(2, n):
    c = a + b
    print(c, end = " ")
    a = b
    b = c