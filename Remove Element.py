def removeElement(nums, val):
    for i in nums:
        if i == val:
            nums.remove(i)
    return len(nums)
nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))




# def removeElement(nums, val):
#     k = 0  # New length of list
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1
#     return k

# nums = [3,2,2,3]
# val = 3
# new_length = removeElement(nums, val)
# print(new_length)       # Output: 2
# print(nums[:new_length]) # Output: [2, 2]
