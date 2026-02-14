str = "Hello, my name is Prakhar Singh."

freq = {}

for i in str:
    if i.isalpha() :
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # if i in ",./\|;:()*&^%$#@!~`><?{}][_-+=]":
    #     continue
    # elif i == " ":
    #     continue
    # elif i in freq:
    #     freq[i] += 1
    # else:
    #     freq[i] = 1

print("Frequency of each alphabets in given string:")
print(freq)