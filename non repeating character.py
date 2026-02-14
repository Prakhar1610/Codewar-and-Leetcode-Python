def non_repeating_chars(s):
    result = []
    for ch in s:
        if s.count(ch) == 1:
            result.append(ch)
    return result

string = "swiss"
print("Non-repeating characters:", non_repeating_chars(string))





# from collections import Counter

# def non_repeating_chars(s):
#     freq = Counter(s)   
#     return [ch for ch in s if freq[ch] == 1]

# string = "swiss"
# result = non_repeating_chars(string)
# print("Non-repeating characters:", result)
