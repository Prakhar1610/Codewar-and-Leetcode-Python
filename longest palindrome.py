def isPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False


def longestPalindrome(lst):
    max = 0
    maxPalin = ""
    for i in lst:
        if isPalindrome(i):
            i_len = len(i)
            if i_len > max:
                max = i_len
                maxPalin = i
    return maxPalin


lst = ["racecar", "level", "hello", "madam", "world"]

print(longestPalindrome(lst))