# Description:
# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938



def narcissistic( value ):
    sum = 0
    temp = value
    exp = len(str(value))
    while temp != 0:
        rem = temp % 10
        sum = sum + (rem ** exp)
        temp = temp // 10
    
    if sum == value:
        return True
    else:
        return False
    



def narcissistic(value):
    total = 0
    temp = value
    exp = len(str(value))
    
    while temp != 0:
        rem = temp % 10
        total += rem ** exp
        temp //= 10
    
    return total == value





def narcissistic(value):
    return value == sum(int(d)**len(str(value)) for d in str(value))
