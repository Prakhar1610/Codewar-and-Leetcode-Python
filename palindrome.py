str = input("Enter the word: ")

if str == str[::-1]:
    print("\"{}\" is Palindrome.".format(str))
else:
    print("\"{}\" is not Palindrome.".format(str))