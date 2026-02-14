def nonRepeat(lst):
    count = {}

    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    non_repeating = [k for k, v in count.items() if v == 1]
    return non_repeating


lst = [1, 4, 2, 5, 1, 4, 4, 2, 0]

print(nonRepeat(lst))