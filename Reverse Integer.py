x = 123
rev_x = 0
len = len(str(x)) - 1

while x != 0:
    rem = x % 10
    if len == 0:
        rev_x += rem
        break

    rev_x = rev_x + (rem * (10 ** len))
    len = len - 1
    x = x // 10

print(rev_x)



x = 123
rev_x = 0

while x != 0:
    rev_x = rev_x * 10 + (x % 10)
    x = x // 10

print(rev_x)



x = 123
rev_x = int(str(x)[::-1])
print(rev_x)
