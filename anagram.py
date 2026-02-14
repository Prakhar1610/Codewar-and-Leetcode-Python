str1 = input("Enter the string 1: ")
str2 = input("Enter the string 2: ")

freq = {}

if len(str1) != len(str2) :
    print("Both \"{}\" and \"{}\" are not Anagram.".format(str1, str2))

else:
    for i in str1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for j in str2:
        if j in freq:
            freq[j] -= 1
        else:
            break

    if all(value == 0 for value in freq.values()):
        print("Both \"{}\" and \"{}\" are Anagram.".format(str1, str2))
    else:
        print("Both \"{}\" and \"{}\" are not Anagram.".format(str1, str2))


# String1 = input("Enter the 1st string :")
# String2 = input("Enter the 2nd string :"")
# #check if length matches
# if len(String1) != len(String2):
#     #if False
#     print(‘Strings are not anagram’)
# else:
#     #sorted function sort string by characters
#     String1 = sorted(String1)
#     String2 = sorted(String2)
# #check if now strings matches
# if String1 == String2:
# #if True
#     print(‘Strings are anagram’)
# else:
#     print(‘Strings are not anagram’)



# from collections import Counter

# print("Strings are anagram" if Counter(input("Enter 1st string: ")) == Counter(input("Enter 2nd string: ")) else "Strings are not anagram")
