def group_by_commas(n):
    s = str(n)
    s = s.replace(",", "")
    new_s = ""
    three_num = 0
    
    if len(s) <= 3:
        return s
    
    for i in s[::-1]:
            if three_num == 3:
                new_s = "," + new_s
                three_num = 0
            new_s = i + new_s
            three_num = three_num + 1
    return new_s





def group_by_commas(n):
    s = str(n).replace(",", "")
    new_s = ""
    count = 0

    if len(s) <= 3:
        return s

    for ch in reversed(s):
        if count == 3:
            new_s = "," + new_s
            count = 0
        new_s = ch + new_s
        count += 1

    return new_s




def group_by_commas(n):
    return f"{int(str(n).replace(',', '')):,}"




# Examples
#        1  ->           "1"
#       10  ->          "10"
#      100  ->         "100"
#     1000  ->       "1,000"
#    10000  ->      "10,000"
#   100000  ->     "100,000"
#  1000000  ->   "1,000,000"
# 35235235  ->  "35,235,235"